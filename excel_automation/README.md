# Python Excel Automation & Multi-Source Data Consolidation

Proyek otomasi berbasis Python untuk menggabungkan, membersihkan, dan mengonsolidasikan laporan dari berbagai sumber file (Excel/CSV multi-cabang) secara otomatis. Dirancang untuk menghemat waktu pemrosesan data manual dan meminimalkan *human error* bagi kebutuhan bisnis operasional dan keuangan.

## 🚀 Fitur Utama
* **Multi-File Batch Processing:** Secara otomatis memindai dan menggabungkan seluruh file laporan `.xlsx` dan `.csv` dari dalam folder `data_mentah/`.
* **Advanced Data Cleaning:** 
  * Menghilangkan spasi berlebih (*whitespaces*) pada data teks.
  * Menyeragamkan format penulisan nama produk menjadi *Title Case*.
  * Menghapus baris data duplikat secara otomatis.
  * Menangani nilai data yang kosong (*missing values*) agar perhitungan tetap akurat.
* **Automated Business Calculation:** Menghitung total pendapatan secara otomatis (`Jumlah` × `Harga Satuan`).
* **Professional Export:** Mengekspor hasil akhir konsolidasi menjadi satu laporan nasional yang bersih dan siap disajikan ke manajemen.

## 📂 Struktur Proyek
```text
excel_automation/
│
├── data_mentah/                  # Folder tempat meletakkan file laporan mentah (.xlsx / .csv)
├── venv/                         # Python Virtual Environment
├── process_data.py               # Skrip modular untuk logika pembersihan & konsolidasi data
├── main.py                       # Titik masuk (entry point) eksekusi program
└── laporan_nasional_terkonsolidasi.xlsx # File hasil laporan akhir