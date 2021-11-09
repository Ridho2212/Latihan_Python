# list makanan dengan 2 dimensi
daftar_makanan = [
    ["Bakwan", "Combro", "Misro"],
    ["Sop Iga", "Sop Buntut", "Sop Kaki"],
    ["Nasi Uduk", "Nasi Goreng", "Nasi Remes"]
]

print('------cetak per item-------')
print(daftar_makanan[0][0])
print(daftar_makanan[1][2])
print(daftar_makanan[2][2])
print('------cetak semuanya dengan nestedloop------')
for menu in daftar_makanan:
    for makanan in menu:
        print(makanan)
