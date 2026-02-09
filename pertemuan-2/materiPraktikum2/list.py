#list muttable
#list memiliki indeks
#memiliki fungsi len()
#bisa memiliki tipe data yg berbeda dalam satu himpunan
makanan = ["ikan", "ayam", "pecel"]
print(makanan)

#panjang list
minuman = ["teh", "kopi", "susu"]
print(len(minuman))

#list allow duplicates
kegiatan = ["makan", "tidur", "belajar", "makan"]
print(kegiatan)

""" === akses item (mengakses dengan merujuk pada nomor indeksnya) ==="""
makanan = ["ikan", "ayam", "pecel"]
print(makanan[0])

#negative indexing
boygroup = ["nct", "dream", "127", "wayV", "wish"]
print(boygroup[-1])
#-1 mengacu pada item terakhir, -2 pada item kedua terakhir, dan seterusnya

#range of indexes
boygroup = ["nct", "dream", "127", "wayV", "wish", "ateez", "lngshot"]
print(boygroup[2:5])
#aturan rangenya [start:stop], yang dimana start itu inklusif, dan stop bersifat eksklusif(angkanya ga termasuk)

boygroup = ["nct", "dream", "127", "wayV", "wish", "ateez", "lngshot"]
print(boygroup[:3])
#jika nilai awalnya tidak ditulis, maka range akan dimulai dari indeks pertama (nol)

boygroup = ["nct", "dream", "127", "wayV", "wish", "ateez", "lngshot"]
print(boygroup[2:])
#jika tidak menuliskan nilai akhir, range akan berlanjut hingga indeks terakhir


""" === check if item exists === """
makanan = ["ayam", "ikan", "sayur"]

print("ikan" in makanan) #hasilnya True atau False

#contoh lain
if "ayam" in makanan:
  print("'ayam' ada di dalam list") #jika 'ayam' ada di dalam list, maka cetak pesan


""" === change value item (dengan mengacu nomor indeksnya) === """
warna = ["merah", "biru", "kuning", "hijau"]
warna[1] = "jingga" #mengganti elemen pada indeks ke-1 dengan 'jingga'
print(warna)

#jika ingin mengganti beberapa elemen list sekaligus,
#bisa dengan menentukan rentang indeks dan list nilai pengganti
tempat = ["sungai", "pantai", "gunung", "kota", "pedesaan", "rumah"]
tempat[1:3] = ["laut", "kebun"]
print(tempat)

#panjang daftar akan berubah ketika jumlah item yang dimasukkan tidak sesuai dengan jumlah item yang diganti
warna = ["merah", "biru", "kuning"]
warna[1:3] = ["jingga"] #mengubah nilai kedua dan ketiga dengan satu nilai
print(warna)
#hasilnya, elemen kedua dan ketiga akan dihapus dan digantikan oleh satu elemen baru.

#insert items(tanpa mengganti nilai yang sudah ada)
tempat = ["pantai", "sawit", "gunung"]
tempat.insert(2, "pedesaan")
print(tempat)
#gunung akan pindah ke indeks ke-3, karena pedesaan disisipkan pada indeks ke-2
#kemudian list akan berubah sisinya menjadi 4 item

#bisa juga menggunakan append() untuk menambahkan item baru ke akhir list
nama = ["fildza", "rania", "najwa"]
nama.append("syifa")
print(nama)#syifa akan ditambahkan di bagian akhir list

#extend list
#untuk menambahkan elemen dari list lain ke list saat ini, gunakan method extend()
makanan = ["mie", "nasi", "tempe"]
minuman = ["jus", "kopi", "es teh"]
makanan.extend(minuman)

print(makanan)
#method ini tidak harus menambhkan list saja, tapi juga bisa menambahkan objek iterable apapun

#remove specified item
tempat = ["gunung", "kebun", "sawit"]
tempat.remove("sawit")
print(tempat)

#contoh lain
makanan = ["telur", "ayam", "gulai", "ikan", "ayam"]
makanan.remove("ayam")
print(makanan)
#yang dihapus hanya 'ayam' dibagian pertama saja.
#karena yang di cek indeks pertama, begitu selanjutnya terus sampai akhirnya ketemu yang ingin dihapus, selesai. bagian setelahnya tidak akan di cek lagi

#menghapus menggunakan indeks spesifik
minuman = ["eskrim", "sirup", "susu"]
minuman.pop(1)
print(minuman)

#keyword del
minuman = ["es teh", "cendol", "es tebak"]
del minuman[0]  #indeks pertama akan di hapus
print(minuman)

#clear the list (mengosongkan list)
tempat = ["aula", "kelas", "kantin"]
tempat.clear()
print(tempat)

""" loop list """
makanan = ["ayam", "ikan", "sate"]
for x in makanan:      #untuk setiap x di list makanan
  print(x) #cetak elemen satu persatu

#Loop Through the Index Numbers (perulangan pada list dengan mengaskses elemen berdasarkan nomor indeksnya)
tempat = ["rumah", "kelas", "laboraturium"]
for i in range(len(tempat)):
  print(tempat[i])  #menampilkan elemen list sesuai indeks ke-i

#while loop (untuk menampilkan setiap elemen list berdasarkan indek)
nama = ["fildza", "najwa", "salwa"]
i = 0
while i < len(nama):
  print(nama[i])  #tampilkan elemen list sesuai indeks ke i
  i = i + 1

#list comprehension (perulangan singkat unutk mencetak sisi list)
nama = ["fildza", "najwa", "salwa"]
[print(x) for x in nama]

#membuat list baru untuk elemen yang memiliki huruf 'a' menggunakan list comprehension dengan for dan if
tempat = ["rumah", "kelas", "IC", "kantin", "RS"]
tempatBaru = []

for x in tempat:
  if "a" in x:
    tempatBaru.append(x)

print(tempatBaru)

#mengatur nilai output list baru
tempatBaru = ['Di' +x for x in tempat] 
#loop setiap x di list, setiap elemen di list baru diawali teks "Di"

#Customize Sort Function
#mengurutkan list berdasarkan jarak nilai terhadap angka tertentu
def hitungJarak(n):
  return abs(n - 10)

nilai = [90, 40, 54, 12, 23]
nilai.sort(key = hitungJarak) #diurutkan dari selisihnya paling dekat ke 10
print(nilai)

