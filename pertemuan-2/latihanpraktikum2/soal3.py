"""3. Diberikan dua set mata kuliah pilihan:
kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}
1. Tentukan mata kuliah yang diambil oleh kedua kelas.
2. Tentukan mata kuliah yang hanya diambil kelas A.
3. Tentukan seluruh mata kuliah unik yang diambil oleh kelas A dan B."""


kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

# 1 method intersection() digunakan untuk mencari elemen yang sama antara dua set
matkul_sama = kelas_A.intersection(kelas_B) 
print(matkul_sama)

#2 perulangan for untuk menampilkan setiap mata kuliah yang diambil oleh kelas A
for x in kelas_A:
 print(x)

#yang benar
different = kelas_A.difference(kelas_B)
print(different)

#3 method update() untuk menambahkan seluruh elemen kelas_b ke dalam kelas_a tanpa adanya duplikasi
kelas_A.update(kelas_B)
print(kelas_A)

gabungan = kelas_A | kelas_B
print(gabungan)