# TSABITAH ARDELIA WAHYUDI #
# 1A #

print("Program Menghitung Selisih Waktu")
print("Selamat datang!")
print()

def SelisihWaktu(JamAwal, MenitAwal, DetikAwal, JamAkhir, MenitAkhir, DetikAkhir):
    TotalAwal = (JamAwal * 3600) + (MenitAwal * 60) + DetikAwal
    TotalAkhir = (JamAkhir * 3600) + (MenitAkhir * 60) + DetikAkhir

    if TotalAkhir < TotalAwal:
        TotalAkhir += (24 * 3600)
        print("Berada di hari yang berbeda.")
    else:
        print("Berada di hari yang sama.")

    Selisih = (TotalAkhir - TotalAwal)

    JamSelisih = (Selisih // 3600)
    MenitSelisih = (Selisih % 3600) // 60
    DetikSelisih = (Selisih % 60)

    return JamSelisih, MenitSelisih, DetikSelisih

print("Waktu Mulai")
JamAwal = int(input("Jam: "))
MenitAwal = int(input("Menit: "))
DetikAwal = int(input("Detik: "))

print()

print("Waktu Selesai")
JamAkhir = int(input("Jam: "))
MenitAkhir = int(input("Menit: "))
DetikAkhir = int(input("Detik: "))

JamSelisih, MenitSelisih, DetikSelisih = SelisihWaktu(JamAwal, MenitAwal, DetikAwal, JamAkhir, MenitAkhir, DetikAkhir)

print()
print("Perhitungan Selisih")
print(f"{JamSelisih} jam - {MenitSelisih} menit - {DetikSelisih} detik")

print()
print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI ^-^")