# # # Kondisi percabangan IF
# # angka = 6

# # if angka < 10: 
# #     print("Angka kurang dari 10")

# # umur = int(input("Masukkan umur: ")) # Input umur

# # if umur >= 17:
# #     print("Kamu sudah bisa membuat KTP") # Blok if dijalankan karena kondisi True
# # else:
# #     print("Kamu belum bisa membuat KTP") # Blok else tidak dijalankan



# kendaraan = input("Masukkan jenis kendaraan anda: ")

# if kendaraan == "mobil":
#     tarif_parkir = 10000
# elif kendaraan == "motor":
#     tarif_parkir = 5000
# else:
#     tarif_parkir = 15000

# print("Tarif parkir yang harus dibayar:", tarif_parkir)

# #programnya harus input nilai, klo nilai >90 = a, nilai >80 = b, nilai > 70 c, 69 <  

nilai = int(input("masukkan nilai anda: "))

if nilai >= 70:
    print("Nilai C")
elif nilai > 80:
    print("Nilai B")
elif nilai > 90:
    print("Niail A")
elif nilai > 50 and nilai < 69:
    print("Nilai D")
else :
    print("Nilai E")

pembelian = int(input("masukkan total pembelian anda: "))

if pembelian > 200000:
    print("mendapat diskon 30%")
elif pembelian > 100000:
    print("mendapat diskon 10%")
else:
    print("tidak mendapat diskon")

