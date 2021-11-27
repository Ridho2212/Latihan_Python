# looping For
print("Cetak Angka 1 s/d 5")
angka = 10
for no in range(angka):
    no = no + 1
    print("Angka", no)

# Latihan Looping for
print("Cetak Angka 1 s/d 20")
angka = 20
for no in range(angka):
    no += 1
    print("Angka Ke-", no)

# Latihan Looping for 2
print("Cetak Bilangan Bulat 1 s/d 20")
angka = 20
for no in range(angka):
    no += 1
    if (no % 2 == 1):  # jika ingin bilangan bulat 1 ganti 0
        print("Bilangan Ganjil", no)
