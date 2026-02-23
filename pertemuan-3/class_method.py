#method adalah fungsi yang dimiliki oleh sebuah class. 
#Method mendefinisikan perilaku objek yang dibuat dari class tersebut.
#contoh
class Band:
    def __init__(self, nama_grup):
        self.nama = nama_grup

    def sapa(self): #ini adalah method
        print("Halo! To the world, yeogin NCT " + self.nama)

grup1 = Band("Dream")
grup1.sapa()

#method dapat menerima parameter seperti fungsi biasa
class Hitung:
    def tambah(self, a, b):
        return a + b
    
    def kali(self, a, b):
        return a * b
    
hasil = Hitung()
print(hasil.tambah(2, 3))
print(hasil.kali(4, 5))

#method dapat mengakses dan memodifikasi properti objek menggunakan self
#contoh method yang mengakses properti objek
class Tiket:
    def __init__(self, nama, tujuan):
        self.nama = nama
        self.tujuan = tujuan

    def pesan(self):
        return f"Anda telah memesan tiket atas nama {self.nama} dengan tujuan {self.tujuan}"

tiket1 = Tiket("Chenle", "Pekanbaru")
print(tiket1.pesan())

#contoh method yang memodifikasi properti suatu objek
class Bunga:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def petik(self):
        self.jumlah += 1
        print(f"Petik bunga sebanyak {self.jumlah} tangkai")

b1 = Bunga("mawar", 5)
b1.petik()
b1.petik()

#__str__() method
#method ini adalah metode khusus yang menentukan apa yang dikembalikan saat objek dicetak

#contoh jika tanpa method __str__()
class Nilai:
    def __init__(self, nama, skor):
        self.nama = nama
        self.skor = skor

a1 = Nilai("Kayla", 99)
print(a1)


#contoh jika menggunakan method __str__()
class Nilai:
    def __init__(self, nama, skor):
        self.nama = nama
        self.skor = skor

    def __str__(self):
        return f"{self.nama} ({self.skor})"

a1 = Nilai("Kayla", 99)
print(a1)

#sebuah class dapat memiliki beberapa method yang dapat bekerja bersama-sama
class DramaList:
    def __init__(self, nama):
        self.nama = nama
        self.dramas = []

    def tambah_drama(self, drama):
        self.dramas.append(drama)
        print(f"Tambah drama baru: {drama}")

    def hapus_drama(self, drama):
        if drama in self.dramas:
            self.dramas.remove(drama)
            print(f"Hapus drama: {drama}")

    def tampilkan(self):
        print(f"List Drama '{self.nama}':")
        for drama in self.dramas:
            print(f"-{drama}")

d1 = DramaList("Belum ditonton")
d1.tambah_drama("Our Universe")
d1.tambah_drama("Taxi Drive 2")
d1.tampilkan()


#delete methods
#untuk menghapus methods dari sebuah kelas, gunakan keyword del
class Bunga:
    def __init__(self, nama):
        self.nama = nama

    def petik(self):
        print(f"petik bunga {self.nama}")

b1 = Bunga("tulip")

del Bunga.petik

b1.petik() #ini akan memunculkan eror