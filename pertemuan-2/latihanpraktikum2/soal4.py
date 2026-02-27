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
"A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

#1 tampilkan mahasiswa yang ipk di atas 3. 5
for x in mahasiswa: #untuk setiap elemen (x) di dict mahasiswa
   if mahasiswa[x]["ipk"] > 3.5: 
      print(mahasiswa[x]["nama"])

#unutk mencetak valuenya aja
# for value in mahasiswa.values():
#    print(value)

#2
jumlah = 0 #untuk menyimpan total ipk
total = 0 #untuk menyimpan jumlah mahasiswa

for x in  mahasiswa: #untuk setiap elemen (x) di dict mahasiswa
   jumlah = jumlah + (mahasiswa[x]["ipk"]) 
   total = total +1 #tambah ipk ke variabel jumlah
   rata = jumlah / total #hitung rata rata 
   
print(rata)

#cara lain
rata_ipk = sum(data["ipk"] for data in mahasiswa.values()) / len(mahasiswa)
      
#3 menambahkan satu data 
mahasiswa["A004"] = {"nama" : "Fildza", "prodi" : "Informatika", "ipk": 3.9}
print(mahasiswa)