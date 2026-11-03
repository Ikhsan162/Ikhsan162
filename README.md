# 🚀 Python Automation & Data Engineering Portfolio

Kumpulan proyek otomatisasi berbasis Python yang dirancang untuk mengoptimalkan alur kerja data—mulai dari pengambilan data otomatis (*web scraping*) hingga konsolidasi dan pembersihan laporan bisnis (*data cleaning & automation*).

---

## 📂 Daftar Proyek

1. [E-Commerce Product Scraper](#1-e-commerce-product-scraper)
2. [Excel Automation & Multi-Source Data Consolidation](#2-excel-automation--multi-source-data-consolidation)

---

## 1. E-Commerce Product Scraper

Aplikasi berbasis Python yang dirancang untuk melakukan *Web Scraping* pada situs *e-commerce* secara otomatis, mengekstrak data produk penting (nama, harga, deskripsi, dan rating), serta merapikannya langsung ke dalam format laporan Excel.

### 🌟 Fitur Utama
* **Otomasi Pengambilan Data:** Mengambil data produk secara otomatis tanpa harus *copy-paste* secara manual.
* **Pengolahan Data (Pandas):** Menyaring, menstrukturkan, dan mengelola data mentah menjadi tabel yang bersih dan siap dianalisis.
* **Ekspor Otomatis ke Excel:** Menyimpan hasil *scraping* langsung ke file Excel menggunakan modul `openpyxl` dan `pandas`.
* **Struktur Kode Modular:** Memisahkan logika pengambilan data (*scraping*) dan eksekusi utama agar kode lebih mudah dibaca dan dikembangkan.

---

## 2. Excel Automation & Multi-Source Data Consolidation

Aplikasi berbasis Python untuk melakukan konsolidasi, pembersihan data (*data cleaning*), dan otomatisasi laporan dari berbagai sumber file (Excel/CSV multi-cabang) secara efisien guna meminimalkan *human error*.

### 🌟 Fitur Utama
* **Multi-File Batch Processing:** Secara otomatis memindai dan menggabungkan seluruh file laporan `.xlsx` dan `.csv` yang ada di dalam folder `data_mentah/`.
* **Advanced Data Cleaning:** 
  * Membersihkan spasi berlebih (*whitespaces*) pada data teks.
  * Menyeragamkan format penulisan nama produk menjadi *Title Case*.
  * Menghapus baris data duplikat secara otomatis.
  * Menangani nilai data yang kosong (*missing values*) agar perhitungan tetap akurat.
* **Automated Business Calculation:** Menghitung total pendapatan secara otomatis (`Jumlah` × `Harga Satuan`).
* **Professional Export:** Mengekspor hasil akhir konsolidasi menjadi satu laporan nasional yang bersih dan siap disajikan ke manajemen.

---

## 🛠️ Teknologi yang Digunakan
* **Python**
* **Pandas** (Manipulasi dan analisis data tabular)
* **OpenPyxl** (Membaca dan menulis file Excel)

---

## ⚙️ Cara Menjalankan Proyek
1. Pastikan Anda sudah menginstal Python di komputer.
2. Buat dan aktifkan *Virtual Environment*:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
