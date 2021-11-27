print("-------------Tugas 2 DDP Ridho Setiawan-------------")
nape = str(input("Masukkan Nama Pelanggan\t: "))
propil = str(input("Produk Pilihan\t\t: "))

if (propil == "Kipas Angin"):
    harga = 1000000
    print("Harga Produk\t\t: %i" % (harga))

elif (propil == "TV"):
    harga = 2000000
    print("Harga Produk\t\t: %i" % (harga))

elif (propil == "Mesin Cuci"):
    harga = 3000000
    print("Harga Produk\t\t: %i" % (harga))

elif (propil == "AC"):
    harga = 4000000
    print("Harga Produk\t\t: %i" % (harga))

else:
    harga = 5000000
    print("Harga Produk\t\t: %i" % (harga))

jumbel = int(input("Jumlah Barang\t\t: "))
harkot = harga * jumbel
print("Harga Kotor\t\t: %i" % (harkot))

if (propil == "Kulkas" or "kulkas" and jumbel >= 5):
    dsc = 0.20 * harkot
    print('Diskon\t\t\t: %i' % (dsc))
elif (propil == "AC" or "ac" and jumbel >= 3):
    dsc = 0.10 * harkot
    print('Diskon\t\t\t: %i' % (dsc))
else:
    dsc = 0.05 * harkot
    print('Diskon: %i' % (dsc))

pajak = harkot - dsc * 0.10
print("PPN\t\t\t: %i" % (pajak))

haber = harkot - dsc + pajak
print("Harga Bersih\t\t: %i" % (haber))
