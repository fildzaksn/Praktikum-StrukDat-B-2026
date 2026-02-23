"""
buatlah sebuah class dengan
-minimal 3 atribut / property
-2 method
lalu buat 3 object dr class tsb
lalu ubahlah salah satu atribut dari objek tersebut
"""

class Absen:
    def __init__(self, nama, kelas, status = "hadir"):
        self.nama = nama
        self.kelas = kelas
        self.status = status


    def izin(self):
        self.status = "izin"
        print(f"{self.nama} {self.kelas} {self.status}")

    def sakit(self):
        self.status = "sakit"
        print(f"{self.nama} {self.kelas} {self.status}")
    
    def ubah_status(self, status_baru):
        self.status = status_baru
    
absen1 = Absen("fildza", "TI B")
print(absen1.nama, absen1.kelas, absen1.status)

absen2 = Absen("rania", "TI B")
absen2.izin()

absen3 = Absen("najwa", "TI B")
absen3.sakit()

#mengubah atribut status dari objek absen2
print(f"sebelum status diubah {absen2.status}")
absen2.ubah_status("alpa")
print(f"status sekarang {absen2.status}")

