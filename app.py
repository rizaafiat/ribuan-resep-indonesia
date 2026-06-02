from flask import Flask, jsonify, request, send_from_directory
import json, os, re

app = Flask(__name__, static_folder='static')

with open(os.path.join(os.path.dirname(__file__), 'recipes_all.json'), 'r', encoding='utf-8') as f:
    RECIPES = json.load(f)

def build_index():
    keywords = {}
    for i, r in enumerate(RECIPES):
        text = (r.get('title', '') + ' ' + str(r.get('ingredients', ''))).lower()
        words = set(re.findall(r'\w+', text))
        for w in words:
            if len(w) > 2:
                keywords.setdefault(w, set()).add(i)
    return keywords

INDEX = build_index()
print(f"Loaded {len(RECIPES)} recipes, {len(INDEX)} keywords indexed")

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/recipes')
def get_recipes():
    q = request.args.get('q', '').lower().strip()
    limit = min(int(request.args.get('limit', 20)), 100)
    offset = int(request.args.get('offset', 0))
    if q:
        words = [w for w in re.findall(r'\w+', q) if len(w) > 2]
        if words:
            matched = None
            for w in words:
                if w in INDEX:
                    if matched is None:
                        matched = INDEX[w].copy()
                    else:
                        matched &= INDEX[w]
                else:
                    matched = set()
                    break
            if matched is None:
                matched = set()
            results = [RECIPES[i] for i in sorted(matched)]
        else:
            results = []
    else:
        results = RECIPES
    total = len(results)
    page = results[offset:offset + limit]
    return jsonify({'total': total, 'offset': offset, 'limit': limit, 'recipes': page})

@app.route('/api/recipes/<int:recipe_id>')
def get_recipe(recipe_id):
    if 0 <= recipe_id < len(RECIPES):
        return jsonify(RECIPES[recipe_id])
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/random')
def random_recipe():
    import random
    count = min(int(request.args.get('count', 1)), 10)
    samples = random.sample(RECIPES, count)
    return jsonify({'recipes': samples})

@app.route('/api/stats')
def stats():
    return jsonify({'total': len(RECIPES)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
