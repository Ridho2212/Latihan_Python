def infoSuhu():
    lokasi = input('Masukkan Lokasi\t: ')
    suhu = int(input('Masukkan Suhu\t: '))

    def status():
        if (suhu <= 0):
            kondisi = 'Beku'
        elif (suhu > 0 and suhu <= 16):
            kondisi = 'Dingin'
        elif (suhu > 16 and suhu <= 20):
            kondisi = 'Sejuk'
        elif (suhu > 20 and suhu <= 30):
            kondisi = 'Biasa'
        else:
            kondisi = panas

        return kondisi

    print('Lokasi di %s dengan suhuh %i kondisinya %s' %
          (lokasi, suhu, status()))


# panggil fungsi
infoSuhu()
