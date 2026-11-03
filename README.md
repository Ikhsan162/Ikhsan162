# 🛍️ E-Commerce Product Scraper & Excel Automation

Aplikasi berbasis Python yang dirancang untuk melakukan *Web Scraping* pada situs *e-commerce* modern secara otomatis, mengekstrak data produk penting (seperti nama, harga, deskripsi, dan rating), serta merapikannya langsung ke dalam format laporan **Excel (`.xlsx`)**.

---

## 🚀 Fitur Utama
* **Otomasi Pengambilan Data:** Mengambil data produk secara otomatis tanpa harus *copy-paste* secara manual.
* **Pengolahan Data (Pandas):** Menyaring, menstrukturkan, dan mengelola data mentah menjadi tabel yang bersih dan siap dianalisis.
* **Ekspor Otomatis ke Excel:** Menyimpan hasil *scraping* langsung ke file Excel menggunakan modul `openpyxl` dan `pandas`.
* **Struktur Kode Modular:** Memisahkan logika pengambilan data (*scraping*) dan eksekusi utama agar kode lebih mudah dibaca dan dikembangkan.

---

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python
* **Library Utama:**
  * `requests` (HTTP requests untuk mengakses halaman web)
  * `BeautifulSoup4` (Parsing HTML & ekstraksi elemen data)
  * `Pandas` (Manipulasi dan analisis data)
  * `OpenPyXL` (Mesin pembuat file Excel)

---

## 📂 Struktur Proyek

```text
ecommerce_scraper/
├── scraper.py          # Modul logika utama untuk mengambil dan memparsing data web
├── main.py             # Titik masuk program & eksekusi penyimpanan ke Excel
└── README.md           # Dokumentasi proyek untuk portofolio GitHub
