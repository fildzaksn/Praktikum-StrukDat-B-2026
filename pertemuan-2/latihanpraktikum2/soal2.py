"""2. Diberikan sebuah tuple data mahasiswa:
mahasiswa = ("A001", "Budi", "Informatika")
1. Tampilkan nama mahasiswa dari tuple tersebut.
2. Tampilkan seluruh isi tuple menggunakan perulangan for.
3. Jelaskan satu alasan mengapa tuple tidak bisa diubah."""

mahasiswa = ("A001", "Budi", "Informatika")

#1 tampilkan nama mahasiswa
print(mahasiswa[1])

#2
for x in mahasiswa:
    print(x)

#3
#karena tuple bersifat immutable setelah dideklarasikan, jadi elemen-elemennya di dalam permanen