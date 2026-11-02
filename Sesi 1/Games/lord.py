import random
import main

def start():
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4  # INI TETEP HARUS KOSONG

        lord_position = random.randint(1, 4)

        goa = goa_kosong.copy()  # INI ADALAH TEMPAT BARU UNTUK SI CUYPY
        goa[lord_position - 1] = "|0_0|"

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)

        print(f'Coba perhatikan goa dibawah ini\n\n{goa_kosong}\n')
        pilihan_user = int(input("Menurut kamu di goa nomor berapa lord berada? [1 / 2 / 3 / 4]: "))

        # Menyesuaikan dengan cuypy_position
        if pilihan_user == lord_position:
            print(f"\n{goa}\n\nSelamat Kamu Menang 🏆")
        else:
            print(f"\n{goa}\n\nMaaf kamu kalah 🙈")

        play_again = input("\n\nApakah ingin melanjutkan gamenya lagi? [y/n]: ")
        if play_again.lower() == "n":
            main.menu()

if __name__ == "__main__":
    start()