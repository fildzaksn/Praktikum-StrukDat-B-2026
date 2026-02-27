#program utama yang mengimport kedua module

from kurs import kurs #import dictionary kurs dari module kurs
from konverter import konver #import fungsi konver() dari module konverter
from tabulate import tabulate #import fungsi tabulate dari library tabulate untuk menampilkan tabel

print("=== KONVERTER MATA UANG ===")

data = [] #list kosong untuk menampung pasangan [kode, kurs] agar bisa ditampilkan dg tabulate
for k, v in kurs.items():
    data.append([k, v])

print(tabulate(data, headers=['Kode', 'Kurs'], tablefmt="grid"))

dari = input("Dari (IDR/USD/EUR/SGD/JPY): ")
ke = input("Ke IDR/USD/EUR/SGD/JPY: ")
jumlah = int(input("Jumlah: "))

hasil = konver(dari, ke, jumlah, kurs) #memanggil fungsi dari modul konverter
print("\n")
print(f"{jumlah:,} {dari} = {hasil:.2f} {ke}".replace("," , "."))