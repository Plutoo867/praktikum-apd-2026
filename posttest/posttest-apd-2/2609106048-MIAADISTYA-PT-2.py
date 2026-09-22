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

print(harga_makanan)
print(admin_gojek)
print(total_bayar)
print(rata_rata)
print(nim)
print(bolean)
print(konversi_euro)
print(harga_makanan[-6:])
