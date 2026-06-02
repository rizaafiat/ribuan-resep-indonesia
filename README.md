# resep-app

Aplikasi pencarian resep kuliner Indonesia dengan antarmuka web sederhana.

## Fitur

- Pencarian resep berdasarkan judul dan bahan
- Indeks kata kunci untuk hasil pencarian cepat
- Antarmuka Responsif (HTML statis + Flask)

## Struktur

```text
resep-app/
├── app.py
├── recipes.json
├── recipes_all.json
├── start.sh
└── static/
    └── index.html
```

## Sumber Data

Data resep pada repositori ini berasal dari dataset Hugging Face:
- `junwatu/indonesian-recipes`

## Menjalankan

```bash
python3 app.py
```

## API

- `GET /api/recipes?q=ayam&limit=20&offset=0`
- `GET /` untuk antarmuka web
