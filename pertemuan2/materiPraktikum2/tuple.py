#imuttable
#tuple pakai kurung biasa
#secara harfiah sama aja kek list

#tuple adalah kumpulan yang terurut dan tidak dapat diubah
#tuple juga dapat berisi berbagai tipe data
data = ("hijau", "kuning", 20, True)
print(data)

#mengaskses item tuple
#untuk mengakses item tuple, dapat dengan merujuk pada nomor indeks yang berada di dalam tanda []
warna = ("hijau", "kuning", "merah")
print(warna[1])
#tuple juga bisa menggunakan negative indexing, seperti list

"""Change Tuple Values
Setelah sebuah tuple dibuat, nilainya tidak dapat diubah(tuple bersifat immutable).
ada cara alternatif (workaround) untuk mengubah nilai tuple, yaitu dengan mengubah tuple menjadi list, 
melakukan perubahan pada list tersebut, 
lalu mengubahnya kembali menjadi tuple."""

x = ("merah", "kuning", "hijau")
y = list(x)
y[1] = "jingga"
x = tuple(y)

print(x)

#add items
#sama seperti cara mengubah nilai tuple
buah = ("apel", "pisang")

list_buah = list(buah)
list_buah.append("mangga")

buah = tuple(list_buah)
print(buah)


#unpack tuple
#saat kita membuat tuple dan langsung mengisinya dengan beberapa nilai, proses ini disebut packing tuple
#jadi unpacking tuple adalah proses mengeluarkan nilai-nilai dalam tuple ke bbrp variabel
warna = ("merah", "biru", "hijau")
(w1, w2, w3) = warna

print(w1)
print(w2)
print(w3)

#using asterisk
#kalau jumlah variabel lebih sedikit daripada jumlah isi tuple, kita bisa pakai * supaya sisa nilainya masuk ke list
warna = ("merah", "biru", "hijau", "kuning", "ungu")

(warna1, warna2, *sisa_warna) = warna

print(warna1)
print(warna2)
print(sisa_warna)

#kalau tanda asterisk * tidak diletakkan di variabel terakhir,
#maka python akan mengisi variabel bertanda * dengan beberapa nilai hingga sisa nilai cukup untuk mengisi variabel setelahnya
warna = ("merah", "biru", "hijau", "kuning", "ungu")

(warna_awal, *warna_tengah, warna_akhir) = warna

print(warna_awal)
print(warna_tengah)
print(warna_akhir)

#loop tuples
#untuk loop through a tuple itu sama saja dengan yang di list

#loop through the index numbers
#kita bisa melakukan perulangan pada tuple dengan menggunakan nomor indeksnya, dengan menggabungkan fungsi range() dan len()
warna = ("merah", "biru", "hijau", "kuning")

for i in range(len(warna)):
    print(warna[i])

#while loop
#perulangan pada tuple menggunakan while loop dilakukan dengan memanfaatkan indeks dari setiap elemen tuple
warna = ("merah", "biru", "hijau", "kuning")

i = 0
while i < len(warna):
    print(warna[i])
    i = i + 1

#join two tuples
#untuk menggabungkan 2 atau lebih tuple, dapat menggunakan operator +
satu = ("bakwan", "pisang", "tahu")
dua = (5, 3, 2)

hasil = satu + dua
print(hasil)

#multiple tuples
#menggandakan isi tuple sebanyak jumlah tertentu dengan menggunakan operator *
warna = ("merah", "biru", "hijau")
hasil = warna * 2

print(hasil)
