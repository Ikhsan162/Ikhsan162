import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_modern_ecommerce():
    # Menggunakan situs uji coba e-commerce produk modern (Ponsel)
    url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
    
    print(f"Sedang mengambil data dari situs: {url}")
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Gagal mengakses situs web.")
        return None
    
    # Parsing HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Menemukan semua kartu produk pada halaman modern ini
    products = soup.find_all('div', class_='thumbnail')
    
    data_list = []
    for product in products:
        # Mengambil judul/nama produk
        title_element = product.find('a', class_='title')
        title = title_element['title'] if title_element else "Tidak ada nama"
        
        # Mengambil harga produk
        price_element = product.find('h4', class_='price')
        price = price_element.text.strip() if price_element else "Tidak ada harga"
        
        # Mengambil deskripsi singkat produk
        desc_element = product.find('p', class_='description')
        description = desc_element.text.strip() if desc_element else "Tidak ada deskripsi"
        
        # Mengambil rating (jumlah review)
        rating_element = product.find('div', class_='ratings')
        reviews_count = len(rating_element.find_all('span', class_='glyphicon-star')) if rating_element else 0
        
        data_list.append({
            'Nama Produk': title,
            'Harga': price,
            'Deskripsi': description,
            'Jumlah Rating Bintang': reviews_count
        })
        
    # Ubah data ke dalam DataFrame Pandas
    df = pd.DataFrame(data_list)
    return df

if __name__ == "__main__":
    df_result = scrape_modern_ecommerce()
    if df_result is not None:
        print(df_result.head())