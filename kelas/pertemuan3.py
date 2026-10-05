# batas = 5

# for i in range(batas):
#     print("Perulangan ke-", i)

# game = ["Ghensin", 7.0, True]
# for i in game:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
#     print('') #biar ada jarak tiap iterasi

# jawab = "ya"
# hitung = 0

# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total Perulangan : {hitung}")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# angka_benar = 7

# while True:
#     print("=== Game tebak angka ===")

#     angka_input = int(input("masukkan angka (1-10): "))

#     if angka_benar == angka_input:
#         print("gokil")
#         break
#     else:
#         print("kurang gokil")

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
count = 0
n = int(input("masukkan bill: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1
    else:
        print(f"bilangan ganjil dari 1 sampai {n} adalah {i} berjuamlah {count}")