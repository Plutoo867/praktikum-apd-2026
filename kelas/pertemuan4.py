# f1 = ["mclaren", "ferrari", "mercedes", 1, 2, 3,]
# print(f1)

# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50, ["aida", 6, True]], ["mia", 1, 1.50]]
# print(formula1)
# print(formula1[3])
# print(formula1[4][2])
# print(formula1[4][3][2])
# print(formula1[5][0])

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# sirkuit.append(["Spa-Francorchamps", 9])
# print(sirkuit)
# print(sirkuit[4][0])
# sirkuit.extend(["Interlagos", "Monaco"])
# print(sirkuit)
# sirkuit.insert(2, "Hockenheimring")
# print(sirkuit)

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# sirkuit[1] = "Monza Italia"
# print(sirkuit)
# sirkuit[0:2] = ["Sepang", "Mugello"]
# print(sirkuit)
# sirkuit[4][2] = "Aida"
# print(sirkuit)

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# del sirkuit[2]
# print(sirkuit)
# sirkuit.remove("Suzuka")
# print(sirkuit)
# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# ambil_sirkuit = sirkuit.pop(2)
# print(ambil_sirkuit)
# print(sirkuit)
# sirkuit.pop(2)
# print(sirkuit)

# driver = ["Hamilton", "Verstappen", "Leclerc", "Sainz", "Russell", "Antoneli", "Norris",["Alonso", "Gasly", "Ocon"],["Perez", "Stroll", "Vettel"]]
# print(driver[1:8:2])

# team1 = ["Mercedes", "Ferrari", "MacLaren"]
# team2 = ["Red Bull", "Alpine", "Aston Martin"]
# gabung_team = team1 + team2
# print(gabung_team)

# juara_WDC = ["MacLaren", "Red Bull"]
# juara = juara_WDC * 3
# for i in juara:
#     print(i)

# line_up = [
#     ["Ferrari", "Leclerc", 16],
#     ["Mercedes", "Hamilton", 44],
#     ["Red Bull", "Verstappen", 1],
#     ["McLaren", "Norris", 4]
# ]
# print(line_up[2][1])
# for i in line_up:
#     for j in i:
#         print(j, end=" ")

# print(line_up[0][0], line_up[0][1], line_up[0][2])
# print(line_up[0:3:2])
# print(line_up[0][0:2])

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)
# print(listchara)
# print(chara)

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)
# listchara.append("Yui ")
# chara = tuple(listchara)
# print(chara)

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)
# listchara.extend(input("Masukkan karakter baru: ").split(","))
# chara = tuple(listchara)
# print(chara)

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)
# listchara.insert(2, "Senku")
# chara = tuple(listchara)
# print(chara)

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)
# listchara[0:2] = ["Senku", 17]
# chara = tuple(listchara)
# print(chara)

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)
# del listchara[3]
# chara = tuple(listchara)
# print(chara)

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)
# listchara.remove("Yukari")
# chara = tuple(listchara)
# print(chara[2:])
# print(chara[::2])

# data_harian = [
#     ["Senin", 36.5], 
#     ["Selasa", 37.1], 
#     ["Rabu", 36.8], 
#     ["Kamis", 37.0], 
#     ["Jumat", 36.6]
# ]

# print(data_harian[0][1], data_harian[1][1])

# chara = ("Yukari", "Yukino", "Odette", "Senku")
# (Persona, Oregairu, Genshin, DrStone) = chara
# print(Persona)
# print(Oregairu)

chara = ("Yukari", "Yukino", "Odette", "Senku", 8, 8)
(Persona, Oregairu, *anime, mia) = chara
print(Persona)
print(Oregairu)
print(anime)
print(mia)