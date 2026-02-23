#properti atau atribut adalah variabel di dalam class yang menyimpan data atau properti objek. 
#properti dapat diakses dengan menggunakan notasi titik

class Donat:
    def __init__(self, varian, ukuran):
        self.varian = varian
        self.ukuran = ukuran

donat1 = Donat("donat coklat", "L")

print(donat1.varian)
#output donat coklat

#mengubah nilai properti pada objek
class Sepatu:
    def __init__(self, warna, ukuran):
        self.warna = warna
        self.ukuran = ukuran

    def beli(self):
        print(f"Sepatu berwarna {self.warna} dengan ukuran {self.ukuran}")
    
s1 = Sepatu("hitam", 40)
print("Pilihan pertama:", s1.warna)

s1.warna = "putih"
print("Pilihan terakhir:", s1.warna)

#untuk menghapus properti, gunakan keyword del
class Tiket:
    def __init__(self, nama, tujuan):
        self.nama = nama
        self.tujuan = tujuan

    def pesan(self):
        print(f"Anda memesan tiket dengan tujuan {self.tujuan}")

tiket1 = Tiket("Jisung", "Pekanbaru")

del tiket1.tujuan

print(tiket1.nama)
print(tiket1.tujuan) #akan menimbulkan eror

#properti class vs properti object
#properti class adalah atribut yang dimiliki class dan dibagikan ke seluruh instance. 
#atribut ini ditulis langsung di dalam class, tetapi di luar method.
#sedangkan properti object adalah atribut yang didefinisikan di dalam __init__() dan dimiliki setiap instance secara terpisah

class Hewan:
    jenis = "peliharaan" #properti class

    def __init__(self, nama):
        self.nama = nama #properti instance

h1 = Hewan("kucing")

print(h1.nama)
print(h1.jenis)

#modifikasi properti class menggunakan notasi titik
class Hewan:
    jenis = "peliharaan" #properti class

    def __init__(self, nama):
        self.nama = nama #properti instance

h1 = Hewan("kucing")
h2 = Hewan("kelinci")

Hewan.jenis = "liar"

print(h1.nama, h1.jenis)
print(h2.nama, h2.jenis)

#menambahkan properti baru ke objek yang sudah ada
class Bunga:
    def __init__(self, nama):
        self.nama = nama

b1 = Bunga("mawar")

b1.warna = "merah"
b1.jumlah = 5

print(b1.jumlah, b1.nama, b1.warna)