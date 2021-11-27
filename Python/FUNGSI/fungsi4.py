def hitungGaji():
    nama = input('Masukkan nama \t\t:')
    jabatan = input('Masukkan Jabatan \t:')
    agama = input('Masukkan agama \t\t:')
    jumlah = int(input('Masukkan Jumlah Anak \t:'))

    def gapok(jabatan):
        return{
            "General Manager": 20000000,
            "Manager": 10000000,
            "Staff": 5000000
        }[jabatan]
    tunja = 0.2 * gapok(jabatan)
    persen = 0.01
    if(jumlah > 0 and jumlah < 4):
        tunak = gapok(jabatan) * persen * jumlah
    elif(jumlah > 3):
        tunak = gapok(jabatan) * persen * (jumlah-(jumlah-3))
    else:
        tunak = 0
    gaji_kotor = gapok(jabatan) + tunak
    zakat = (0, 0.025 * gaji_kotor)[gaji_kotor >= 6000000 and agama == "Islam"]
    gaber = (gapok(jabatan) + tunak) - zakat
    print(
        'SLIP GAJI PT. XYZ'
        '\n---------------------------------'
        '\nNama Pegawai\t\t : %s'
        '\nJabatan\t\t\t : %s'
        '\nAgama\t\t\t : %s'
        '\nJumlah Anak\t\t : %i'
        '\nGaji Pokok\t\t : Rp. %i'
        '\nTunjangan Jabatan\t : Rp. %i'
        '\nGaji Kotor\t\t : Rp. %i'
        '\nZakat Profesi\t\t : Rp. %i'
        '\nTake Home Pay\t\t : Rp. %i'
        % (nama, jabatan, agama, jumlah, gapok(jabatan), tunja, gaji_kotor, zakat, gaber)
    )


print('----------Input Data Pegawai----------')
hitungGaji()
