# TSABITAH ARDELIA WAHYUDI #
# 1A #

print("Laboratorium Komputer SMAN 2 Harapan")
print("Selamat datang. Silakan login terlebih dahulu.")
print("Mohon diingat bahwa Anda hanya memiliki 3 kali kesempatan untuk login.")
print("Silakan hubungi admin jika akses terblokir.")
print()

def LoginLabKom(Maksimal = 3):
    Password = "Latihan"
    Kesempatan = Maksimal

    while Kesempatan > 0:
        Username = input("Silakan masukkan username Anda: ")
        PasswordUser = input("Silakan masukkan password Anda: ")

        if PasswordUser == Password:
            print(f"Login berhasil! Selamat datang, {Username}.")
            return True
        else:
            Kesempatan -= 1
            print("Maaf. Password Anda salah. Silakan coba lagi.")
            print(f"Kesempatan yang tersisa {Kesempatan}.")
            if Kesempatan == 0:
                print("Kesempatan Anda sudah habis. Akses ditolak.")
                return False

LoginLabKom(Maksimal = 3)

print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI! ^-^")