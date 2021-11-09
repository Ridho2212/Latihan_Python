print("-------------Tugas 2 DDP Ridho Setiawan-------------")
nape = str(input("Masukkan Nama Pelanggan\t: "))
propil = input("Produk Pilihan\t\t: ")

if (propil == "Kipas Angin" or "kipas angin"):
    harga = 1000000
    print("Harga Produk\t\t: %i" % (harga))

elif (propil == "TV" or "tv"):
    harga = 2000000
    print("Harga Produk\t\t: %i" % (harga))

elif (propil == "Mesin Cuci" or "mesin cuci"):
    harga = 3000000
    print("Harga Produk\t\t: %i" % (harga))

elif (propil == "AC" or "ac"):
    harga = 4000000
    print("Harga Produk\t\t: %i" % (harga))

else:
    (propil == "Kulkas" or "kulkas")
    harga = 5000000
    print("Harga Produk\t\t: %i" % (harga))

jumbel = int(input("Jumlah Barang\t\t: "))
harkot = harga * jumbel
print("Harga Kotor\t\t: %i" % (harkot))

if (propil == "Kulkas" or "kulkas" and jumbel >= 5):
    dsc = 0.20 * harkot
elif (propil == "AC" or "ac" and jumbel >= 3):
    dsc = 0.10 * harkot
else:
    dsc = 0.05 * harkot

pajak = harkot - dsc * 0.10
print("PPN\t\t\t: %i" % (pajak))

haber = harkot - dsc + pajak
print("Harga Bersih\t\t: %i" % (haber))
