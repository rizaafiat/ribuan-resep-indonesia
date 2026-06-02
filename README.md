# resep-app

Aplikasi pencarian resep kuliner Indonesia dengan antarmuka web sederhana dan API terstruktur.

## Fitur

- Pencarian resep berdasarkan judul dan bahan
- Indeks kata kunci untuk hasil pencarian cepat
- Antarmuka responsif (HTML statis + Flask)
- API untuk integrasi ke aplikasi lain

## Sumber Data

Data resep pada repositori ini berasal dari dataset Hugging Face:
- [`junwatu/indonesian-recipes`](https://huggingface.co/datasets/junwatu/indonesian-recipes)

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

## Menjalankan

```bash
python3 app.py
```

## API

- `GET /api/recipes?q=ayam&limit=20&offset=0`
- `GET /api/recipes/<id>`
- `GET /api/random?count=1`
- `GET /api/stats`
- `GET /` untuk antarmuka web

## Cara Berkontribusi

1. Fork repositori ini.
2. Buat branch baru: `git checkout -b fitur/nama-fitur`.
3. Lakukan perubahan dan pastikan kode tetap bersih.
4. Commit perubahan: `git commit -m "feat: deskripsi singkat"`.
5. Push ke branch Anda: `git push origin fitur/nama-fitur`.
6. Buka Pull Request dan jelaskan perubahan yang Anda buat.

Kontribusi berupa perbaikan bug, peningkatan pencarian, serta penambahan dokumen sangat diharapkan.

## Lisensi

Proyek ini dilisensikan under the [MIT License](./LICENSE).
