# Meminta input dari pengguna
bilangan = int(input("Masukkan bilangan bulat: "))

# Menggunakan struktur kontrol if-then-else
if bilangan > 0:
    print("Bilangan tersebut adalah positif.")
else:
    if bilangan < 0:
        print("Bilangan tersebut adalah negatif.")
    else:
        print("Bilangan tersebut adalah nol.")
