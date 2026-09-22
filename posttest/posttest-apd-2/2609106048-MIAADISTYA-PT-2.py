makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000
makanan_4 = 20000
makanan_5 = 21000
makanan_6 = 22000

harga_makanan = [makanan_1, makanan_2, makanan_3, makanan_4, makanan_5, makanan_6]

admin_gojek = 5000

total_bayar = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5 + makanan_6 + admin_gojek

konversi_euro = total_bayar/20437

rata_rata = total_bayar/len(harga_makanan)

nim = 48

bolean = nim != rata_rata

print("List harga makanan :", harga_makanan)
print("Admin gojek :", admin_gojek)
print("Total yang harus dibayar (IDR) :", total_bayar)
print("Total yang harus di bayar (EUR) :", konversi_euro, "EUR")
print("Rata-rata harga makanan :", rata_rata)
print("NIM :", nim)
print("nim != rata_rata? :", bolean)
print("List harga makanan dengan slice index negatif :", harga_makanan[-6:])

