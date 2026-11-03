from generate_invoice import buat_pdf_invoice

def main():
    print("Memulai proses pembuatan Invoice PDF secara otomatis...")
    
    # Data contoh daftar transaksi / pelanggan
    daftar_transaksi = [
        {
            "no_invoice": "INV-2026-001",
            "tanggal": "03 November 2026",
            "jatuh_tempo": "17 November 2026",
            "nama_pelanggan": "PT Woodone Integra Indonesia",
            "alamat_pelanggan": "Kawasan Industri, Jakarta",
            "items": [
                {"deskripsi": "Sewa Armada Truk Pendingin (CDE Reefer)", "jumlah": 2, "harga": 3500000},
                {"deskripsi": "Biaya Bongkar Muat & Driver", "jumlah": 1, "harga": 750000}
            ]
        },
        {
            "no_invoice": "INV-2026-002",
            "tanggal": "03 November 2026",
            "jatuh_tempo": "17 November 2026",
            "nama_pelanggan": "PT Indogal Agro Trading",
            "alamat_pelanggan": "Surabaya, Jawa Timur",
            "items": [
                {"deskripsi": "Pengiriman Logistik FTL Antar Pulau", "jumlah": 1, "harga": 12500000},
                {"deskripsi": "Asuransi Pengiriman Barang", "jumlah": 1, "harga": 500000}
            ]
        }
    ]
    
    # Loop untuk membuat invoice secara batch otomatis
    for data in daftar_transaksi:
        buat_pdf_invoice(data)
        
    print("\nSemua file PDF invoice berhasil dibuat di dalam folder 'output_pdf'!")

if __name__ == "__main__":
    main()