import main
from services import db

def add():
    kode_barang = input('kode barang: ')
    nama_barang = input('nama barang: ')
    harga_barang = int(input('harga barang: '))
    stok_barang = int(input('stok barang: '))
    
    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)

def update():
    kode_barang = input('Masukkan kode barang yang ingin di-update: ')
    nama_barang = input('Nama barang baru: ')
    harga_barang = int(input('Harga barang baru: '))
    stok_barang = int(input('Stok barang baru: '))
    
    db.update_item(kode_barang, nama_barang, harga_barang, stok_barang)

def delete():
    kode_barang = input('Masukkan kode barang yang ingin dihapus: ')
    db.delete_item(kode_barang)
    
def check():
    items = db.fetch_item()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f'''
kode {kode_barang}
{nama_barang} | Rp {harga_barang}
stok: {stok_barang}
''')
 
def start():
    while True:
        menu = int(input('''
Menu Mini Market:
1. Tambah Barang
2. Check Barang
3. Update Barang
4. Hapus Barang
5. Keluar
Pilih menu (1-5): '''))
        
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            update()
        elif menu == 4:
            delete()
        elif menu == 5:
            print("Keluar dari program.")
            break
        else:
            print("Pilihan menu tidak valid.")
 
if __name__ == "__main__":
    start()