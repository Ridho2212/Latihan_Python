# If Multi Kondisi
nama = "Ridho Setiawan"
matpel = "Matematika"
nilai = 80
# tentukan kelulusan dgn ternary

ket = "Lulus" if nilai >= 60 else "Gagal"

# uji grade dengan if Multi Kondisi

if(nilai >= 85 and nilai <= 100):
    grade = 'A'
elif(nilai >= 75 and nilai < 85):
    grade = 'B'
elif(nilai >= 60 and nilai < 75):
    grade = 'C'
elif(nilai >= 30 and nilai < 60):
    grade = 'D'
else:
    grade = '-'\

print("Data Nilai Siswa :"
      "\nNama\t\t:", nama,
      "\nMata Pelajaran\t:", matpel,
      "\nNilai\t\t:", nilai,
      "\nKeterangan\t:", ket,
      "\nGrade\t\t:", grade
      )
