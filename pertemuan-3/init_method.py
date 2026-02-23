#__init__ method
#dia selalu dieksekusi ketika class diinisialisasi
class Buku:
  def __init__(self, nama, kode):    #argumennya ada self, nama, kode #self merujuk pada dirinya sendiri (objek yg baru dibuat) 
    self.nama = nama    #self.nama itu atribut atau disebut juga properti
    self.kode = kode

buku1 = Buku("Novel", 119) #disini, self merujuk pd objek buku1

print(buku1.nama)
print(buku1.kode)

#tanpa __init__()
class Buku:
  pass

buku1 = Buku() 
buku1.nama = "Neo"
buku1.kode = 127

print(buku1.nama)
print(buku1.kode)



#nilai default di __init__()
class Biodata:
  def __init__(self, nama, kelas = "TI B"): #TI B adalah nilai default untuk parameter kelas
    self.nama = nama
    self.kelas = kelas

mhs1 = Biodata("Haechan")
mhs2 = Biodata("Jeno", "TI A")

print(mhs1.nama, mhs1.kelas)
print(mhs2.nama, mhs2.kelas)

#metode __init__ dapat memiliki banyak parameter