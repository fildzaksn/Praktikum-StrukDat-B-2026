#imuttable, ga punya indeks
#item dr set tidak bs diubah, tapi bisa di hapus dan di tambhakan
#set pakai kurung kurawal
#set adlh himpunan matematika
"""
Elemen di dalam set tidak berurutan, tidak dapat diakses menggunakan indeks, tidak mengizinkan elemen duplikat
"""

benda = {"meja", "kipas", "kursi"}
print(benda)

#dalam satu set, tidak boleh memiliki dua item degan nilai yang sama
#Jika terdapat elemen yang sama, maka elemen tersebut hanya akan disimpan satu kali.
benda = {"piring", "sendok", "garpu", "piring"}
print(benda)

#item dalam set dapat berupa tipe data apapun
nama = {"halo", 123, True}

#konstruktor set
#selain menggunakan tanda kurung kurawal {}, set juga dapat dibuat dengan konstruktor set
#digunakan untuk membuat himpunan (set) baru dari data yg diberikan
warna = set(("merah", "pink", "ungu", "biru"))
print(warna)

#item pada set tidak dapat diakses dengan merujuk pada indeks atau key
#namun kita bisa menggunakan for loop atau keyword in
tingkat = {"1A", "1B", "1C", "1D"}

for x in tingkat:
    print(x)

#memeriksa apakah suatu elemen terdapat di dalam set
tingkat= {"1A", "1B", "1C", "1D"}
print("1B" in tingkat)
print("1B" not in tingkat)

#setelah set dibuat, itemnya tidak dapat diubah karena ia bersifat mutable
#akan tetapi kita bisa menambahkan item baru ke dalamnya
kode = {"me", "ji", "ku"}

kode.add("hi")
print(kode) #set adalah himpunan tidak berurut, jadi item set dapat muncuk dalam urutan berbeda setiap kali digunakan

#add sets
#method update() dapat digunakan untuk menambahkan item dari set lain ke set saat ini
#bukan hanya set, bisa juga berupa tuple, list dll
kodeSet = {"me", "ji", "ku"}
kodeList = ["hi", "bi", "ni", "u"]

kodeSet.update(kodeList)
print(kodeSet)

#remove item
#sama seperti list, set juga dapat menggunakan method remove(), pop(), clear(), dan del
#method pop() akan menghapus item secara acak, dan akan mengembalikan nilai berupa item yang dihapus

#selain menggunakan remove(), kita juga dapat menggunakann discard() untuk menghapus item
#sama seperti list, set juga dapat menggunakan method remove(), pop(), clear(), dan del
#method pop() akan menghapus item secara acak, dan akan mengembalikan nilai berupa item yang dihapus

#selain menggunakan remove(), kita juga dapat menggunakann discard() untuk menghapus item
tingkat= {"1A", "1B", "1C", "1D"}

tingkat.discard("1C")
print(tingkat)
#jika item yang akan dihapus tidak ada, akan muncul error

#python join sets
#method union() dan update() untuk menggabungkan semua item dari beberapa himpunan
set1 = {"air", "udara", "api"}
set2 = {1, 2, 3}
set3 = {"hutan", "kayu", "daun"}

gabung_set = set1.union(set2, set3)
print(gabung_set)

#method union() juga bisa untuk menggabungkan sebuah himpunan dengan tipe data lain
x = {12, 7, 9}
y = ("ayam", "ikan", "tahu")

gabungan = x.union(y)
print(gabungan)
#contoh diatas adalah gabungan set dengan tuple

#method update()
#digunakan untuk menambah semua elemen dari satu set ke set lainnya
#method ini mengubah set asli dan tidak menghasilkan set baru
bil1 = {10, 12, 11}
bil2 = {100, 120, 110}

bil1.update(bil2)
print(bil1)

#intersection
#digunakan untuk menyimpan hanya elemen yang sama (duplikat) dari dua set.
matkul_TIA = {"kwu", "bindo", "bing"}
matkul_TIB = {"kwu", "arsikom", "bindo"}

hasil = matkul_TIA.intersection(matkul_TIB)
print(hasil)

#mencari elemen yang sama (intersection) dari dua set menggunakan operator &
matkul_TIA = {"kwu", "bindo", "bing"}
matkul_TIB = {"kwu", "arsikom", "bindo"}

hasil = matkul_TIA & matkul_TIB
print(hasil)

#difference()
#digunakan untuk mengambil elemen yang hanya ada pada set pertama, tetapi tidak ada pada set kedua.
matkul_TIA = {"kwu", "bindo", "bing"}
matkul_TIB = {"kwu", "arsikom", "bindo"}

diff = matkul_TIA.difference(matkul_TIB)
print(diff)

#contoh dengan menggunakan operator -
matkul_TIA = {"kwu", "bindo", "bing"}
matkul_TIB = {"kwu", "arsikom", "bindo"}

diff = matkul_TIA - matkul_TIB
print(diff)

#symetrics difference
#digunakan untuk menyimpan elemen yang tidak sama dari dua set, atau dengan kata lain elemen yang hanya ada di salah satu set saja.
#method ini akan menghasilkan set baru yang berisi elemen yang tidak terdapat pada kedua set secara bersamaan.
himpunan1 = {10, 20, 30, 40}
himpunan2 = {10, 15, 20, 25, 35}

hasil = himpunan1.symmetric_difference(himpunan2)
print(hasil)

#contoh dengan menggunakan operator ^
#Operator ^ hanya bisa untuk untuk menggabungkan himpunan dengan himpunan lain, dan bukan dengan tipe data lain seperti yang dapat Anda lakukan dengan symmetric_difference() method
himpunan1 = {10, 20, 30, 40}
himpunan2 = {10, 15, 20, 25, 35}

hasil = himpunan1 ^ himpunan2
print(hasil)

#frozen set
#adalah versi set yang bersifat immutable
#menyimpan elemen unik,tidak berurutan, dan tidak boleh ada duplikat
contoh = frozenset(["apel", "pisang", "mangga"])
print(contoh)
#frozenset dapat digunakan ketika membutuhkan struktur data seperti set, tetapi dengan isi yang tidak boleh diubah