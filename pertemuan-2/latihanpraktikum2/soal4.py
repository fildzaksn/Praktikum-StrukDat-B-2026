""" 4. Sebuah data mahasiswa disimpan dalam bentuk dictionary:
mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika",
"ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem
Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika",
"ipk": 3.75}
}
1. Tampilkan nama mahasiswa yang memiliki IPK di atas 3.5.
2. Hitung rata-rata IPK seluruh mahasiswa.
3. Tambahkan satu data mahasiswa baru ke dalam dictionary tersebut."""


mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika",
"ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika",
"ipk": 3.75}
}

#1
jumlah = 0
total = 0

for x in  mahasiswa:
   jumlah = jumlah + (mahasiswa[x]["ipk"])
   total = total +1
   rata = jumlah / total
   
print(rata)

#2
for x in mahasiswa:
   if (mahasiswa[x]["ipk"]) > 3.5:
      print(mahasiswa[x]["nama"])
      
#3
mahasiswa["A004"] = {"nama" : "Fildza", "prodi" : "Informatika", "ipk": 3.9}
print(mahasiswa)