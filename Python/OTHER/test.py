total_barang = 0
total = 0
print("Fitur Belanja")
while True:
    barang = input(
        "Masukan nama barang yang ingin di beli [x untuk berhenti]: ")
    if barang == "x":
        print("Terima kasih")
        break
    else:
        harga = int(input("Masukan Harga Produk: "))
    print("berhasil menambahkan", barang, "dengan harga", harga)
    total_barang += 1
    total += harga
if barang == "x":
    print("Total produk yang di beli : ", total_barang)
    print("Total harga yang dibayarkan : ", total)

# menanyakan keanggotaan
if total_barang > 0:
    anggota = input("Apakah anda seorang anggota: [Y/T]")
    if anggota == "T":
        print("Total harga yang harus dibayar", total)
        print("Terima kasih sudah berbelanja di NFElectronics.")
    else:
        while True:
            email = input("masukan email:")
            end = "@gmail.com"
            if end not in email:
                print("email tidak valid")
            else:
                break

    if anggota == "Y":
        while True:
            password = input("Masukan password: ")
            if len(password) <= 8:
                print("Password tidak valid")
            else:
                break
    if anggota == "Y":
        while True:
            level = input("Masukan level kepesertaan anda: ")
            if level == "gold" and total_barang < 5:
                print("Selamat! Anda mendapatkan diskon sebesar 5%")
                potongan = total*0.05
                break
            elif level == "gold" and total_barang >= 5:
                print("Selamat! Anda medapatkan diskon sebesar 10%")
                potongan = total*0.1
                break
            elif level == "silver" and total_barang < 5:
                print("Selamat! Anda medapatkan diskon sebesar 10%")
                potongan = total*0.1
                break
            elif level == "silver" and total_barang >= 5:
                print("Selamat! Anda medapatkan diskon sebesar 15%")
                potongan = total*0.15
                break
            elif level == "diamond" and total_barang < 5:
                print("Selamat! Anda medapatkan diskon sebesar 15%")
                potongan = total*0.15
                break
            elif level == "diamond" and total_barang >= 5:
                print("Selamat! Anda medapatkan diskon sebesar 20%")
                potongan = total*0.20
                break
            else:
                print("salah")
        print("Total harga yang harus dibayar: ", total-potongan)
        print("Terima kasih sudah berbelanja di NFElectronics")
