#contoh membuat class
class Buah:  #nama class pakai pascal case
  manis = "pisang"
  asam = "jeruk"

#membuat objek
b1 = Buah()    #buah adalah variabel atau objek yang menampung class
print(b1.manis)

#menghapus objek dengan keyword del
class Band:
    def __init__(self, nama_grup):
        self.nama = nama_grup

    def perkenalan(self):
        print("Halo, kami " + self.nama)

grup1 = Band("Aespa")

del grup1
print(grup1)

#menggunakan pass untuk menghindari eror saat definisi class kosong
class Rumah:
  pass