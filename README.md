# 🛒 Mini-Market Management System (Python & MySQL)

Aplikasi berbasis Command-Line Interface (CLI) yang dibangun menggunakan **Python** dan terintegrasi dengan **MySQL Database** untuk mengelola sistem operasional mini-market secara sederhana, cepat, dan efisien.

## 🚀 Fitur Utama
* **Manajemen Barang (CRUD):** 
  * Menambahkan data barang baru ke database (`Create`)
  * Menampilkan daftar inventaris barang (`Read`)
  * Memperbarui informasi barang (`Update`)
  * Menghapus barang dari inventaris (`Delete`)
* **Antarmuka Modular:** Struktur kode yang terorganisir dengan pemisahan antara logika utama, utilitas terminal, dan pengelolaan database.
* **Sistem Keamanan & Lingkungan:** Dilengkapi dengan utilitas berbasis sistem (`socket`, `time`) untuk mempercantik tampilan awal dan animasi penutupan program (*countdown exit*).

---

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python
* **Database:** MySQL
* **Library Python:** 
  * `mysql-connector-python` (Koneksi database)
  * `socket` (Informasi host/sistem)
  * `time` (Utilitas jeda waktu / animasi keluar)

---

## 📂 Struktur Proyek

```text
├── Games/
│   ├── lord.py            # Modul game tambahan
│   └── warung_mini.py     # Logika utama sistem mini-market & CRUD
├── services/
│   └── db.py              # Konfigurasi dan fungsi query database MySQL
├── top.py                 # Utilitas antarmuka (Welcome message & Exit animation)
└── main.py                # Titik masuk utama (Entry point) program
