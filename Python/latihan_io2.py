print('--------Banyak Input----------')
nama = input('Nama: ')
gender = str(input('Jenis Kelamin: '))
umur = int(input('Umur: '))
beratbadan = float(input('Berat Badan: '))

print("Nama\t\t: %s"
      "\nJenis Kelamin\t: %s"
      "\nUmur\t\t: %i tahun"
      "\nBerat Badan\t: %.2f KG" % (nama, gender, umur, beratbadan))
