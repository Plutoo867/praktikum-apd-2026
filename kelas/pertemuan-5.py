# #set
# kartu = {"kartu merah", "kartu biru", "kartu hijau"}
# mia = {"kartu", 6, 7, 8, 5, 9, 10, "jeny", "mia", "aida", "aulia", "siska", "nabila"}
# print(kartu)
# print(mia)

# # set menggunakan list
# matkul = ["apd", "orsikom", "apd", "kalkulus"]
# print(matkul)
# sks = set(matkul)
# print(sks)

# #set menggunakan tuple
# buah = set(("apel", "jeruk", "mangga", "apel"))
# print(buah)

# buah = set(["apel", "jeruk", "mangga", "apel"])
# buah1 = list(buah)
# print(buah)
# print(buah1)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print(angka)

# kelas = {"a", "b", "c"}
# kelas.add("d")
# print(kelas)

# buah = {"apel", "mangga", "jeruk"}
# buah.remove("mangga")
# print(buah)

# kelas = {"mia", "falih", "juna", "nabil"}
# kelas.discard("gabriel")
# print(kelas)

# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}
# angka1 = {1, 2, 3, 4, 5}
# angka2 = {2, 4, 6, 8, 10}
# gabung = aslab1.union(aslab2)
# print(gabung)
# irisan = angka1.intersection(angka2)
# print(irisan)
# perbedaan = angka1.difference(angka2)
# print(perbedaan)
# baru = aslab1.update(angka2)
# print(aslab1)

# Matkul = {
# "Matkul_ganjil" : "kalkulus",
# "Matkul_genap" : "statistik"
# }
# print(Matkul["Matkul_ganjil"])
# print(Matkul)

# data_diri = {
#     "ktp": {
#         "nama" : "mia",
#         "umur" : 19,
#         "alamat" : "jl. merpati no. 26"
#     },
#     "sim": {
#         "nama" : "mia", 
#         "masa_berlaku" : "2025-12-31"

#     }
# }

# for i, j in data_diri.items():
#     print(f"{i}: {j}")

# for i in data_diri.values():
#     print(i)
# for i in data_diri:
#     print(i)

# print(data_diri["ktp"]["nama"])
# print(data_diri)

# tumbuhan = {
#     "buah" : ["apel", "jeruk", "mangga"],
#     "sayur" : ("bayam", "kangkung", "sawi"),
# }
# print(tumbuhan)
# print(tumbuhan["buah"][1])

# List_game = dict(Genshin_Impact="Open World", Mole="Moba", Stardew_Valley="Farming Simulation")
# print(List_game)

# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }
# print(f"Nama saya adalah {Biodata['Nama']}")
# print(f"Saya mengambil mata kuliah {Biodata['KRS'][0]} dan {Biodata['KRS'][1]}")
# print(f"Nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))

# game = {
#     "pou" : "chill",
#     "genshin impact" : "action",
#     "valorant" : "fps",
#     "minecraft" : "sandbox",
#     "mobile legend" : "moba",
#     "mia" : ["print", "game", "coding"]
# }
# for i in game:
#     print(i)
# for i in game.keys():
#     print(i)
# for i in game.values():
#     print(i)
# for i, j in game.items():
#     print(f"{i} adalah jenis game {j}")
#     print(i, j)

# game["apaajalah"] = "open world"
# print(game)

# game = {
#     "pou" : "chill",
#     "genshin impact" : "action",
#     "valorant" : "fps",
#     "minecraft" : "sandbox",
#     "mobile legend" : "moba"
# }

# game.update({"resident evil" : "horror"})
# print(game)

# tambah = game.setdefault("resident evil", "horror")
# print(game)
# print("Tipe game", game.setdefault("grow a garden", "gardening"))

# game = {
#     "pou" : "chill",
#     "genshin impact" : "action",
#     "valorant" : "fps",
#     "minecraft" : "sandbox",
#     "mobile legend" : "moba"
# }
# print(game)
# game["genshin impact"] = "adventure"
# print(game)
# game.update({"genshin impact" : "horror"})
# print(game)

# aset = {
#     "jenis" : "rumah",
#     "harga" : 120000000,
#     "alamat" : "Jl. Raya No. 1",
#     "berpenghuni" : True,
#     "luas" : "120m x 80m"
# }

# print(aset)
# del aset["luas"]
# print(aset)
# print(aset.get("luas"))

# print(aset)
# cache = aset.pop("luas")
# print(aset)
# print(aset.get("luas"))
# print(cache)

# aset = {
#     "jenis" : "rumah",
#     "harga" : 120000000,
#     "alamat" : "Jl. Raya No. 1",
#     "berpenghuni" : True,
#     "luas" : "120m x 80m"
# }
# print(aset)
# aset.clear()
# print(aset)

# aset = {
#     "jenis" : "rumah",
#     "harga" : 120000000,
#     "alamat" : "Jl. Raya No. 1",
#     "berpenghuni" : True,
#     "luas" : "120m x 80m"
#     }
# print("Panjang dictionary :", len(aset))
# print(len(aset))

# menu = {
#     "ayam geprek" : 15000,
#     "ayam goreng" : 13000,
#     "ayam bakar" : 17000,
#     "nasi goreng" : 12000,
#     "mie goreng" : 10000
# }
# menu_baru = menu.copy()
# menu_baru["nasi goreng"] = 15000
# print(menu)
# print(menu_baru)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000
# menu = dict.fromkeys(key, value)
# print(menu)

menu = {
    "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
    "nasi" : ["nasi goreng", "nasi uduk"],
    "mie" : ["mie goreng rendang", "mie goreng aceh"],
    "kuah" : ["soto", "rawon", "sop iga"]
}
for i, j in menu.items():
    print(f"Kategori {i} memiliki menu :")
    print("")
    for kategori in j:
        print(kategori)
    print("")