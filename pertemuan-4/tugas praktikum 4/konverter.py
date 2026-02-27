#fungsi yang menerima kode asal mata uang, kode tujuan konversi, jumlahnya, dan data kurs  
def konver(dari, ke, jumlah, kurs):
    if dari == 'IDR': 
        nilai_idr = jumlah
    else: #kalau 'dari' (mata uang asal) bukan idr
        nilai_idr = jumlah * kurs[dari] #kali jumlah dengan kurs untuk mendapatkan nilai dalam idr 

    if ke == 'IDR':
        hasil = nilai_idr
    else: #jika 'ke' (tujuan konversi) bukan idr
        hasil = nilai_idr / kurs[ke] #bagi nilai idr dengan kurs mata uang tujuan

    return hasil