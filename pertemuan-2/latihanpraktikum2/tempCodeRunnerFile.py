mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

#1 tampilkan mahasiswa yang ipk di atas 3. 5
for x in mahasiswa: #untuk setiap elemen (x) di dict mahasiswa
   if mahasiswa[x]["ipk"] > 3.5: 
      print(mahasiswa[x]["nama"])

for value in mahasiswa.values():
   print(value)