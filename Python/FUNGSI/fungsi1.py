def hitungUmur(tahun_ini):
    nama = input('Nama Siswa : ')
    tahun = int(input('Tahun Lahir : '))
    umur = tahun_ini - tahun
    print("Siswa dengan nama %s yang lahir pada tahun %i berumur %2.f" %
          (nama, tahun, umur))


print('Data diri anda')
hitungUmur(2021)
