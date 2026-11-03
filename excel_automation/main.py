from process_data import process_complex_excel_reports

def main():
    # Jalankan proses konsolidasi dan pembersihan kompleks
    df_clean = process_complex_excel_reports()
    
    if df_clean is not None and not df_clean.empty:
        # Tentukan nama file laporan akhir gabungan
        output_file = "laporan_nasional_terkonsolidasi.xlsx"
        
        # Simpan hasil akhir ke file Excel
        df_clean.to_excel(output_file, index=False)
        
        print(f"\nSukses! Laporan gabungan yang bersih telah disimpan ke '{output_file}'.")
        print("\nPratinjau Hasil Laporan Akhir:")
        print(df_clean.head(10))
    else:
        print("\nProses dihentikan karena tidak ada data yang dapat diproses.")

if __name__ == "__main__":
    main()