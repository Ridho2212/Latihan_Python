Pegawai = 'Ahmad', 'Alex'
Agama = 'Muslim', 'Kristen Protestan'
Gapok = 4000000, 6000000
Anak = 2, 5
Tunja = 0.2 * Gapok[0]
Tunja1 = 0.2 * Gapok[1]

# Pegawai Ahmad
if (Anak[0] <= 2):
    Tunke = 0.10 * Gapok[0]
elif (Anak[0] >= 2):
    Tunke = 0.20 * Gapok[0]

# Pegawai ALex
if (Anak[1] <= 2):
    Tunke1 = 0.10 * Gapok[1]
elif (Anak[1] >= 2):
    Tunke1 = 0.20 * Gapok[1]
else:
    Tunke = 0

Gator = Gapok[0] + Tunja + Tunke
Gator1 = Gapok[1] + Tunja1 + Tunke1

Zapro = (0, 0.025)[Agama == 'Muslim' and Gator >= 6000000]

Gaber = Gator - Zapro
Gaber1 = Gator1 - Zapro

print(
    'SLIP GAJI PT. XYZ'
    '\n---------------------------------'
    '\nNama Pegawai\t\t :', Pegawai[0],
    '\nAgama\t\t\t :', Agama[0],
    '\nJumlah Anak\t\t :', Anak[0],
    '\nGaji Pokok\t\t : Rp.', Gapok[0],
    '\nTunjangan Jabatan\t : Rp.', Tunja,
    '\nTunjangan Keluarga\t : Rp.', Tunke,
    '\nGaji Kotor\t\t : Rp.', Gator,
    '\nZakat Profesi\t\t : Rp.', Zapro,
    '\nTake Home Pay\t\t : Rp.', Gaber
)

print(
    'SLIP GAJI PT. XYZ'
    '\n----------------------------------'
    '\nNama Pegawai\t\t :', Pegawai[1],
    '\nAgama\t\t\t :', Agama[1],
    '\nJumlah Anak\t\t :', Anak[1],
    '\nGaji Pokok\t\t : Rp.', Gapok[1],
    '\nTunjangan Jabatan\t : Rp.', Tunja1,
    '\nTunjangan Keluarga\t : Rp.', Tunke1,
    '\nGaji Kotor\t\t : Rp.', Gator1,
    '\nZakat Profesi\t\t : Rp.', Zapro,
    '\nTake Home Pay\t\t : Rp.', Gaber1
)
