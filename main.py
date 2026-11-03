from scraper import scrape_modern_ecommerce

def main():
    print("--- Memulai Program E-Commerce Scraper ---")
    
    # Panggil fungsi scraping dari file scraper.py
    df_result = scrape_modern_ecommerce()
    
    if df_result is not None and not df_result.empty:
        # Tentukan nama file output Excel
        output_file = "hasil_scraping_produk.xlsx"
        
        # Simpan hasil scraping ke file Excel secara otomatis
        df_result.to_excel(output_file, index=False)
        print(f"\nBerhasil! Data produk telah disimpan ke dalam file '{output_file}'.")
        print(f"Total produk yang berhasil diambil: {len(df_result)} item.")
        
        # Menampilkan pratinjau data di terminal
        print("\nPratinjau Data:")
        print(df_result.head())
    else:
        print("Tidak ada data yang berhasil diambil.")

if __name__ == "__main__":
    main()