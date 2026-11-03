import pandas as pd
import os
import glob

def process_complex_excel_reports():
    print("--- Memulai Proses Otomasi & Konsolidasi Data Kompleks ---")
    
    input_folder = "data_mentah"
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"Folder '{input_folder}' dibuat. Silakan letakkan file laporan Anda di sini.")
        return None

    # Memindai semua file berformat .xlsx atau .csv di dalam folder data_mentah
    all_files = glob.glob(os.path.join(input_folder, "*.xlsx")) + glob.glob(os.path.join(input_folder, "*.csv"))
    
    if not all_files:
        print("\n[Info] Belum ada file laporan di dalam folder 'data_mentah'.")
        print("Membuat data simulasi multi-cabang otomatis untuk demonstrasi...")
        
        # Simulasi data mentah dari beberapa cabang (untuk latihan)
        df_dummy1 = pd.DataFrame({
            'Cabang': ['Jakarta', 'Jakarta', 'Surabaya'],
            'Nama Produk': ['  laptop ASUS ', 'Mouse Wireless', 'Keyboard Mechanical'],
            'Jumlah': [3, 10, 5],
            'Harga Satuan': [7000000, 150000, 350000]
        })
        df_dummy2 = pd.DataFrame({
            'Cabang': ['Surabaya', 'Medan', 'Medan'],
            'Nama Produk': ['Laptop Asus', 'Monitor LED', 'Mouse Wireless '],
            'Jumlah': [2, 4, 8],
            'Harga Satuan': [7000000, 1500000, 150000]
        })
        df_combined = pd.concat([df_dummy1, df_dummy2], ignore_index=True)
    else:
        # Membaca dan menggabungkan seluruh file nyata secara otomatis
        df_list = []
        for file in all_files:
            print(f"Membaca file: {file}")
            if file.endswith('.xlsx'):
                df_list.append(pd.read_excel(file))
            elif file.endswith('.csv'):
                df_list.append(pd.read_csv(file))
        df_combined = pd.concat(df_list, ignore_index=True)

    print(f"\n[Langkah 1] Berhasil menggabungkan data. Total baris mentah: {len(df_combined)}")

    # [Langkah 2] Pembersihan Data Lanjutan (Data Cleaning)
    if 'Nama Produk' in df_combined.columns:
        # Membersihkan spasi berforma aneh dan menyeragamkan huruf kapital (Title Case)
        df_combined['Nama Produk'] = df_combined['Nama Produk'].astype(str).str.strip().str.title()
    
    # Menghapus baris data yang duplikat persis
    df_combined = df_combined.drop_duplicates()
    
    # Menangani data kosong (missing values) pada kolom angka
    df_combined['Jumlah'] = pd.to_numeric(df_combined['Jumlah'], errors='coerce').fillna(0)
    df_combined['Harga Satuan'] = pd.to_numeric(df_combined['Harga Satuan'], errors='coerce').fillna(0)

    # [Langkah 3] Kalkulasi Bisnis Otomatis
    df_combined['Total Pendapatan'] = df_combined['Jumlah'] * df_combined['Harga Satuan']
    
    print("[Langkah 2 & 3] Pembersihan spasi, duplikat, dan kalkulasi pendapatan selesai.")
    return df_combined