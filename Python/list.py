# index/key dari sebuah list dimulai dari 0
ar_buah = ['Pepaya', 'Mangga', 'Pisang', 'Jambu', 'Belimbing']


for buah in ar_buah:  # cetak seluruh list buah
    print("Buah", buah)

# cetak sebuah element array dgn panggil key/index

ar_buah[2] = 'apel'  # ganti element list
print("buah index 2 = ", ar_buah[2])

del ar_buah[4]  # hapus element list
print("buah index 4 = ", ar_buah[4])
