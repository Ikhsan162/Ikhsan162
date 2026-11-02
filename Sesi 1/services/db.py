import mysql.connector

db = mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
    database="mini_market"  
)

def insert_item(kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s,%s)", (kode_barang, nama_barang, harga_barang, stok_barang))
    db.commit()

    if cursor.rowcount > 0:
        print("\nData berhasil dimasukan\n")
    else:
        print("\nData gagal di insert\n")
        
def fetch_item():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_barang")
    result = cursor.fetchall()
    return result

def update_item(kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    sql = "UPDATE tbl_barang SET nama_barang = %s, harga_barang = %s, stok_barang = %s WHERE kode_barang = %s"
    values = (nama_barang, harga_barang, stok_barang, kode_barang)
    cursor.execute(sql, values)
    db.commit()
    
    if cursor.rowcount > 0:
        print("Data berhasil diupdate!")
    else:
        print("Data gagal diupdate atau kode barang tidak ditemukan.")

def delete_item(kode_barang):
    cursor = db.cursor()
    sql = "DELETE FROM tbl_barang WHERE kode_barang = %s"
    values = (kode_barang,)
    cursor.execute(sql, values)
    db.commit()
    
    if cursor.rowcount > 0:
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan atau gagal dihapus.")