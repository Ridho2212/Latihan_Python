print('--------------Luas Bidang-----------------')
print('Pilih bidang:'
      '\n1. Lingkaran'
      '\n2. Segitiga'
      '\n3. Persegi Panjang')
pilihan = int(input('Pilih No.'))
# logic
if (pilihan == 1):
    bidang = 'Lingkaran'
    jari2 = float(input('Jari2: '))
    luas = 3.14 * jari2 * jari2
    print('Luas Bidang %s dengan Jari2 %2.f = %.2f' %
          (bidang, jari2, luas))

elif (pilihan == 2):
    bidang = 'Segitiga'
    alas = float(input('Alas: '))
    tinggi = float(input('Tinggi: '))
    luas = 0.5 * alas * tinggi
    print('Luas Bidang %s dengan Alas %2.f dan Tinggi %2.f' ' = %2.f'
          % (bidang, alas, tinggi, luas))

elif (pilihan == 3):
    bidang = 'Persegi Panjang'
    panjang = float(input('Panjang: '))
    lebar = float(input('Lebar: '))
    luas = panjang * lebar
    print('Luas Bidang %s dengan Panjang %2.f dan Luas %2.f' ' = %2.f'
          % (bidang, panjang, lebar, luas))

else:
    print("No. Bidang yang anda pilih tidak ada")
