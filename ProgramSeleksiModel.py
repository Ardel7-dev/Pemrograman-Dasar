# TSABITAH ARDELIA WAHYUDI #
# 1A #

print("THE NEXT CATWALK MODEL")

Gender = input("Masukkan gender Anda (Wanita/Pria):")
Usia = int(input("Masukkan usia Anda:"))
TinggiBadan = int(input("Masukkan tinggi badan Anda (dalam centimeter):"))
IQ = int(input("Masukkan IQ Anda:"))

if(Gender == "Wanita"):
    if(Usia >= 18 and Usia <= 25):
        if(TinggiBadan >= 170):
            if(IQ >= 130):
                print("Selamat, Anda masuk ke dalam kriteria model catwalk wanita!")
            elif(IQ < 130):
                print("Mohon maaf, IQ Anda tidak memenuhi kriteria.")
        elif(TinggiBadan < 170):
            print("Mohon maaf, tinggi badan Anda tidak memenuhi kriteria.")
    elif(Usia < 18):
        print("Mohon maaf, usia Anda tidak memenuhi kriteria.")
    elif(Usia > 25):
        print("Mohon maaf, usia Anda tidak memenuhi kriteria.")
elif(Gender == "Pria"):
    if(Usia >= 18 and Usia <= 25):
        if(TinggiBadan >= 175):
            if(IQ >= 130):
                print("Selamat, Anda masuk ke dalam kriteria model catwalk pria!")
            elif(IQ < 130):
                print("Mohon maaf, IQ Anda tidak memenuhi kriteria.")
        elif(TinggiBadan < 175):
            print("Mohon maaf, tinggi badan Anda tidak memenuhi kriteria.")
    elif(Usia < 18):
        print("Mohon maaf, usia Anda tidak memenuhi kriteria.")
    elif(Usia > 25):
        print("Mohon maaf, usia Anda tidak memenuhi kriteria.")

print("TERIMA KASIH KARENA TELAH MENGGUNAKAN SISTEM PENGECEKAN INI ^-^")
