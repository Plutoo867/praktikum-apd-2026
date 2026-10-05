username = "mia"
password = "048"

print('''
=======================================
  Badan Penanggulangan Bencana Daerah
=======================================
Selamat datang!!
''')


while True:
    input_username = input("Silahkan masukkan Username anda: ")
    input_password = input("Silahkan masukkan Password anda: ")

    if input_username == "" or input_password == "":
        print("Username dan Password tidak boleh kosong")

    elif input_username != username and input_password != password:
        print("Username dan Password salah!")

    elif input_username != username:
        print("Username salah!")

    elif input_password != password:
        print("Password salah!")

    else:
        break

total_kal_gambut = 0
total_kal_mineral = 0
total_sum_gambut = 0
total_sum_mineral = 0

data = "y"
while data == "y":
    while True:
        print('''
=======================================
            WILAYAH PULAU
=======================================
1. KALIMANTAN
2. SUMATERA
=======================================
''')
        pulau = input("Silahkan pilih wilayah pulau: ")
        if pulau == "":
            print("Input tidak boleh kosong!")

        elif pulau == "1" or pulau == "2":
            break

        else:
            print("Silahkan pilih antara 1 atau 2")

    kategori = ""

    if pulau == "1":
        while True:
            print('''
=======================================
            JENIS LAHAN
=======================================
1. GAMBUT
2. MINERAL
=======================================
''')
            jenis_lahan = input("Silahkan pilih jenis lahan: ")
            if jenis_lahan == "":
                print("Input tidak boleh kosong!")

            elif jenis_lahan == "1":
                kategori = "Kalimantan-Gambut"
                break
            elif jenis_lahan == "2":
                kategori = "Kalimantan-Mineral"
                break
            else:
                print("Silahkan pilih antara 1 atau 2")
    else:
        while True:
            print('''
=======================================
            JENIS LAHAN
=======================================
1. GAMBUT
2. MINERAL
=======================================
''')
            jenis_lahan = input("Silahkan pilih jenis lahan: ")
            if jenis_lahan == "":
                print("Input tidak boleh kosong!")
            elif jenis_lahan == "1":
                kategori = "Sumatera-Gambut"
                break
            elif jenis_lahan == "2":
                kategori = "Sumatera-Mineral"
                break
            else:
                print("Silahkan pilih antara 1 atau 2")

    print('''
=======================================
            JUMLAH TITIK API
=======================================
''')
    while True:
        titik_api = input("Silahkan masukkan jumlah titik penyebaran api: ")
        if titik_api == "":
            print("Jumlah titik api tidak boleh kosong!")
        elif not titik_api.isdigit():
            print("Masukkan angka bulat saja!")
        else:
            jumlah_titik = int(titik_api)
            break

    konversi = jumlah_titik * 5
    print(f"Kategori : {kategori} Jumlah Titik : {jumlah_titik} Luas Lahan : {konversi} Hektare")

    if kategori == "Kalimantan-Gambut":
        total_kal_gambut = total_kal_gambut + konversi
    elif kategori == "Kalimantan-Mineral":
        total_kal_mineral = total_kal_mineral + konversi
    elif kategori == "Sumatera-Gambut":
        total_sum_gambut = total_sum_gambut + konversi
    else:
        total_sum_mineral = total_sum_mineral + konversi

    while True:
        data = input("\nApakah anda ingin memasukkan titik penyebaran lain (y/t)? ").lower()
        if data == "y" or data == "t":
            break
        print("Jawaban tidak valid!")

print(f'''
=======================================
   RINGKASAN TOTAL LAHAN TERBAKAR
=======================================
Kalimantan-Gambut  : {total_kal_gambut} Hektare
Kalimantan-Mineral : {total_kal_mineral} Hektare
Sumatera-Gambut    : {total_sum_gambut} Hektare
Sumatera-Mineral   : {total_sum_mineral} Hektare
=======================================''')
