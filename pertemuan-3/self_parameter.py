"""
- parameter self merujuk pada dirinya sendiri (objek yg baru dibuat) 
- digunakan untuk mengakses properti dan method yang dimiliki oleh class
- parameter self harus jadi parameter pertama dari method manapun di dalam kelas
"""
#parameter self digunakan untuk mengakses atribut class
#parameter self digunakan untuk mengakses atribut class
class Buku:
    def __init__(self, nama, kode): #parameternya ada self, nama, kode
        self.nama = nama #self.nama itu atribut instance
        self.kode = kode

    def pinjam(self): #self merujuk ke objek yang memanggil method ini
        print(f"Buku {self.nama} telah dipinjam") 

buku1 = Buku("Resonance", 2320) #disini, self di __init__() merujuk ke objek buku1

buku1.pinjam()


#use other words instead of self
'''self bisa diganti dengan kata lain, asalkan harus menjadi parameter pertama dari method apapun di dalam class tersebut'''

#mengganti self dengan kata ini dan abc
class Tiket:
    def __init__(ini, nama, tujuan):
        ini.nama = nama
        ini.tujuan = tujuan

    def pesan(abc):
        print(f"Anda memesan tiket dengan tujuan {abc.tujuan}")

tiket1 = Tiket("Jisung", "Pekanbaru")
tiket1.pesan()

#memanggil method lain di dalam class menggunakan self
class Band:
    def __init__(self, nama_grup):
        self.nama = nama_grup

    def perkenalan(self):
        return "Halo, kami " +self.nama
    
    def sapa(self):
        sapaan = self.perkenalan()
        print(sapaan + "! Salam kenal! " )

grup1 = Band("Aespa")
grup1.sapa()