"""Diberikan sebuah list angka:
angka = [10, 20, 30, 40, 50]
1. Tambahkan angka 60 ke dalam list.
2. Hapus angka 20 dari list.
3. Tampilkan angka tertinggi dan terendah
4. Hitung rata-rata angka setelah perubahan data
5. Tampilkan seluruh isi list setelah perubahan."""

angka = [10, 20, 30, 40, 50]

#1 tambah angka 60 ke dalam list dengan fungsi append()
angka.append(60)
print(angka)

#1 hapus angka 20 menggunakan fungsi remove()
angka.remove(20)
print(angka)

#3 tampilkan angka tertinggi dan terendah
tertinggi = max(angka) #menyimoan angka tertinggi dari list angka
terendah = min(angka) #menyimpan angka terendah dari list angka

print(tertinggi)
print(terendah)

#4 hitung rata-rata
total = 0 #menyimpan jumlah seluruh elemen  dalam list
jumlah = 0 #menyimpan banyaknya elemen dalam list

for x in angka:
    total+=x  #tambah nilai elemen ke total
    jumlah+=1  #tambah jumlah elemen
    rata = total / jumlah
print("rata rata angka adalah", rata)

#5tampilan seluruh isi setelah perubahan
print(angka)
