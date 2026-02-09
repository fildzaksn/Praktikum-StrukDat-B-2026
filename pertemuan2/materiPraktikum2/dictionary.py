"""muttable, ordered, don't duplicate"""

#key harus berupa string, valuenya terserah
biodata = { 
    "nama" : "fildza",
    "umur" : 18,
    "hobi" : "memasak"
}

print(biodata)
print(biodata["nama"])  #bisa diakses valuenya, dengan mengacu key-nya

#method get()
print(biodata.get("umur"))


#tidak boleh ada key yg duplikat, kalau ada duplikat, yg kebaca cuma value yg terakhir
contoh = {
    "hari" : "senin", 
    "tanggal" : 20, 
    "bulan" : 2, 
    "tahun" : 2026, 
    "tanggal" : 12
}
print(contoh)
print()
print(len(contoh))


#item dictionary bisa berisi nilai dengan tipe data apapun
bio = {
    "nama": "fildza",
    "umur": 18,
    "status pelajar": True,
    "tanggal lahir": [21, "september", 2007]
}
print(bio)


#cara lain untuk menuliskan dict (konstruktor dict)
bunga = dict(jenis = 'mawar', warna = 'merah', jumlah = 10)
print(bunga)


""" === nested dictionary === """
menu = {
"oven1": {"nama": "brownies", "rasa": "coklat", "jumlah": 5},
"oven2": {"nama": "cookies", "rasa": "red velvet", "jumlah": 12}
}
print(menu)

print(len(menu))  #panjangnya 2

print()
#menambahkan beberapa dictionary kedalam sebuah dictionary
oven1 = dict(jenis = "bolu", varian = "oreo", jumlah = 5)
oven2 = dict(jenis = "tart", varian = "vanila", jumlah = 5)

totalKue ={
    "oven1" : oven1,
    "oven2" : oven2
}
print(totalKue)

#mengakses item dari nested dictionary
menu = {
"oven1": {"nama": "brownies", "rasa": "coklat", "jumlah": 5},
"oven2": {"nama": "cookies", "rasa": "red velvet", "jumlah": 12}
}
print(menu["oven2"]["jumlah"])

#loop through dictionary
for x, data in menu.items(): #x = key dari dictionary menu, data itu valuenya (bentuknya dict juga)
    print(x)
    for y in data:  #y = key dari dictionary data
        print(y + ':', data[y]) #data[y] = value dari key y


""" === get keys === """
bunga = {
    "jenis": "tulip",
    "warna": "kuning", 
    "jumlah": "10"
}

x = bunga.keys()
print(x) #sebelum berubah

bunga["pemesan"] = "rania"
print(x) #setelah menambahkan key value

#get values
y = bunga.values()
print(y) #sebelum berubah

bunga["pemesan"] = "fildza"
print(y)

#get items
print(bunga.items())

#mengecek apakah key ada di dalam dictionary
bunga = {
    "jenis": "tulip",
    "warna": "kuning", 
    "jumlah": "10"
}
if "warna" in bunga:
    print("ada key 'warna' di dalam dictionary")


""" === mengubah nilai === """
menu = {
    "nama": "cookies",
    "rasa": "coklat",
    "jumlah": "2"
}
menu["rasa"] = "original"
print(menu)

#method update()
menu.update({"rasa": "original"})
menu.update({"varian": "oreo"})
print(menu)



""" === menghapus item === """
menu = {
    "nama": "cookies",
    "rasa": "coklat",
    "jumlah": "2"
}

#pop() -> akan menghapus item dengan nama key yang ditentukan
menu.pop("rasa")
print(menu)

#popitem() -> menghapus item terakhir yang dimasukkan 
menu = {
    "nama": "cookies",
    "rasa": "coklat",
    "jumlah": "2"
}
menu.popitem()
print(menu)

#keyword del -> menghapus item dengan nama key yang ditentukan
menu = {
    "nama": "bolu",
    "rasa": "coklat",
    "juumlah": 2 
}
del menu["rasa"]
print(menu)

#clear() untuk mengosongkan dictionary
menu = {
    "nama": "bolu",
    "rasa": "coklat",
    "juumlah": 2 
}
menu.clear()
print(menu)


""" === loop dictionaries === """
#loop pada dictionary secara default menghasilkan key
bunga = {
    "jenis": "tulip",
    "warna": "kuning", 
    "jumlah": "10"
}
for x in bunga:
    print(x)


#untuk menampilkan value, dapat menggunakan method tertentu
bunga = {
    "jenis": "tulip",
    "warna": "kuning", 
    "jumlah": "10"
}
for x in bunga:
    print(bunga[x])

#bisa juga pakai method values()
bunga = {
    "jenis": "mawar",
    "warna": "pink", 
    "jumlah": "21"
}
for x in bunga.values():
    print(x)

#kita bisa juga buat perulangan key dan value sekaligus dengan method items()
for x, y in bunga.items():
    print(x ,y)

print()
""" === copy dictionary === """
#method copy() untuk menyalin dictionary 
menu = {
    "nama": "cookies",
    "rasa": "coklat",
    "jumlah": "2"
}
salinMenu = menu.copy()
print(salinMenu)

#atau juga bisa pakai fungsi dict()
pesan = {
    "nama": "fildza",
    "pesanan": "susu",
    "jumlah": "1"
}
pesanan = dict(pesan)
print(pesanan)