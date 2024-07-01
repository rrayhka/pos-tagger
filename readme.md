
---

# POS Tagger

Proyek ini adalah implementasi sederhana dari POS (Part-of-Speech) Tagger menggunakan model dari Hugging Face. Aplikasi ini menggunakan Flask untuk backend dan HTML/CSS untuk frontend.

## Persyaratan

Pastikan Anda telah menginstal:

- Python 3.6 atau lebih tinggi
- pip (Python package installer)

## Cara Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di mesin lokal Anda:

### 1. Clone Repositori

Clone repositori ini ke direktori lokal Anda menggunakan perintah berikut:

```bash
git clone https://github.com/rrayhka/pos-tagger.git
```

### 2. Install Dependencies

Masuk ke direktori proyek yang baru saja di-clone dan install dependencies yang diperlukan:

```bash
cd pos-tagger
pip install -r requirements.txt
```

### 3. Unduh Model

Jalankan skrip `download_model.py` untuk mengunduh model dan tokenizer dari Hugging Face dan menyimpannya secara lokal:

```bash
python download_model.py
```

### 4. Jalankan Aplikasi

Jalankan aplikasi Flask menggunakan perintah berikut:

```bash
python app.py
```

## File Utama

- `app.py`: Script untuk menjalankan backend Flask.
- `download_model.py`: Script untuk mengunduh dan menyimpan model dan tokenizer dari Hugging Face.
- `index.html`: File HTML untuk frontend aplikasi.
- `requirements.txt`: Daftar dependencies yang diperlukan untuk menjalankan aplikasi.

## Menggunakan Aplikasi

1. Buka `index.html` di browser Anda.
2. Masukkan teks bahasa Indonesia di textarea yang disediakan.
3. Klik tombol "Tag POS".
4. Hasil POS tagging akan ditampilkan di bawah form input.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request atau buka isu di repositori GitHub.

## Lisensi

Proyek ini dilisensikan di bawah MIT License. Lihat file `LICENSE` untuk informasi lebih lanjut.

---