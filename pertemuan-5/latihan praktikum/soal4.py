# Diberikan data buku dalam bentuk dictionary: 
transaksi = [ 
{"produk": "Buku", "harga": 10000, "jumlah": 3}, 
{"produk": "Pena", "harga": 5000, "jumlah": 10}, 
{"produk": "Penghapus", "harga": 2000, "jumlah": 2} 
] 

# a. Ubah jumlah buku menjadi 8. 
transaksi[0]["jumlah"] = 8
print(transaksi)

# b. Tambahkan 2 produk baru. 
transaksi.append({"produk": "Tip x", "harga": 8000, "jumlah": 3})
transaksi.append( {"produk": "Tinta", "harga": 7000, "jumlah": 7})
print(transaksi)

# c. Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan perulangan. 
for x in transaksi:
    total = (x["harga"] * x["jumlah"])
    print(f"Produk: {x['produk']} | Total: {total}")

# Tampilkan ringkasan seperti ini: Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.
