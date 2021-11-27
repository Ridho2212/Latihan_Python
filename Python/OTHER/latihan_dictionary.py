data_nilai = {'Siti': 75, 'Inaya': 98, 'Bedu': 59,
              'Fawaz': 100, 'Zaki': 88, 'Ina': 40}
data_nilai['Siti'] = 80  # ubah data
data_nilai.pop('Ina')
del data_nilai['Zaki']
# cetak all
print('Data nilai:', data_nilai)
# cetak nilai value nya saja
for nilai in data_nilai.values():
    print('Daftar Nilai:', nilai)
# cetak key nya saja
for nama in data_nilai.keys():
    print('Daftar Nama:', nama)
# cetak Value dan keys secara manual
for nama, nilai in data_nilai.items():
    ket = ('Lulus', 'Gagal')[nilai < 60]
    print('Siswa:', nama, '\tNilai:', nilai, '\tDinyatakan:', ket)
