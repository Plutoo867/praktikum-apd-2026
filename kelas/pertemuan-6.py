# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas

# print("Luas persegi panjang:", luas_persegi_panjang())

# def luas_persegi():
#     sisi = int(input("luas: "))
#     luas = sisi * sisi
#     return luas
# print("Luas persegi:", luas_persegi())

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# print("Luas persegi:", luas_persegi(7))

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# sisi = int(input("sisi: "))
# hasil = luas_persegi(sisi)
# print("Luas persegi:", hasil)

# def luas_persegi(panjang, lebar):
#     luas = panjang * lebar
#     return luas

# panjang = int(input("panjang: "))
# lebar = int(input("lebar: "))
# hasil = luas_persegi(panjang, lebar)
# print("Luas persegi:", hasil)

# def pengumuman():
#     print("Hari ini Pengujian Proyek Akhir")

# for i in range(3):
#     pengumuman()

# def sapa_pengguna(nama_pengguna):
#     print(f"Halo, selamat datang {nama_pengguna}")

# sapa_pengguna("88")

# #Membuat variabel global
# nama = "Larry"
# prodi = "Informatika"

#Membuat variabel lokal
# def data():
#     nama = "Teknik Kedokteran"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)

# data()
# print("Nama:", nama)
# print("Prodi:", prodi)

# def faktorial(n):
# #Base Case: Kondisi fungsi berhenti
#     if n == 0 or n == 1:
#         return 1
#     #Rekursive Case: Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# #Memanggil fungsi
# hasil_faktorial = faktorial(8)
# print(f"Hasil dari 6! {hasil_faktorial}")

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else:
#     print(f'Angka yang kamu input : {angka}')
# finally:
#     print('Blok Try Selesai')
while True:
    try:
        usn = input('Username yang diinginkan : ')
        if len(usn) < 5:
            raise ValueError('Nama Minimal Memiliki 5 karakter')
        elif len(usn) > 8:
            raise ValueError('hum hum hum')
        break
    except ValueError as e:
        print(e)