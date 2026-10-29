ensiklopedia = {}

data_user = {
    "admin" : {
        "role" : "admin",
        "username" : "admin",
        "password" : "admin123"
    }}

garis = "=" * 40
id_terakhir = 1

def menu_utama():
    print('''
========================================   
         MENU LOGIN & REGISTER
========================================
1. REGISTER
2. LOGIN
3. KELUAR
========================================
 ''')

def menu_admin():
    print('''
========================================
           ENSIKLOPEDIA BUNGA
========================================
1. LIHAT KOLEKSI BUNGA 
2. TAMBAHKAN KOLEKSI BUNGA
3. EDIT KOLEKSI BUNGA
4. HAPUS KOLEKSI BUNGA
5. LOGOUT
========================================
''')

def menu_user():
    print('''
========================================
           ENSIKLOPEDIA BUNGA
========================================
1. LIHAT KOLEKSI BUNGA 
2. LOGOUT
========================================
''')

def table(label, isi):
    awal = f"{label:<15}: "
    lebar_isi = len(garis) - len(awal)
    baris = ""
    pertama = True

    for kata in isi.split():
        if baris and len(baris) + 1 + len(kata) > lebar_isi:
            print((awal if pertama else " " * len(awal)) + baris)
            pertama = False
            baris = kata
        else:
            baris = f"{baris} {kata}".strip()

    print((awal if pertama else " " * len(awal)) + baris)

def read():
    while True:
        print("0. Kembali ke menu utama")
        print(garis)
        print("DAFTAR BUNGA".center(40))
        print(garis)
        nomor = 1
        for bunga in ensiklopedia.values():
            print(f"{nomor}. {bunga["bunga"]}")
            nomor += 1
        print(garis)
        try:
            detail = int(input("Masukkan nomor bunga untuk melihat detail: "))
            if detail >= 1 and detail <= len(ensiklopedia):
                id_bunga = list(ensiklopedia.keys()) 
                bunga_terpilih = ensiklopedia[id_bunga[detail - 1]]
                print(garis)
                print("DETAL BUNGA".center(40))
                print(garis)
                table("Nama Bunga", bunga_terpilih["bunga"])
                table("Deskripsi", bunga_terpilih["deskripsi"])
                table("Makna Bunga",  bunga_terpilih["makna"])
                print(garis)

            elif detail == 0:
                break
            else:
                print("Koleksi tidak tersedia!")
                print(garis)
        except ValueError:
            print("Input tidak valid!")

def cek_bunga(nama):
    for bunga in ensiklopedia.values():
        if nama.lower() == bunga["bunga"].lower():
            return True
    return False

def id_bunga():
    global id_terakhir
    id_terakhir += 1
    return f"id{id_terakhir}"

def create():
    while True:
        try:
            nama = input("Masukkan nama bunga       : ")
            desk = input("Masukkan deskripsi bunga  : ")
            makna = input("Masukkan makna bunga      : ")

            if cek_bunga(nama):
                print("Koleksi sudah tersedia, silahkan input ulang!")
                print(garis)
                continue

            elif nama == "" or desk == "" or makna == "":
                print("Kolom tidak boleh kosong!")
                continue

            else:
                ensiklopedia[id_bunga()] =({
                                "bunga": nama,
                                "deskripsi": desk, 
                                "makna": makna
                                })
                print("Koleksi berhasil di tambahkan!")
                break
        except ValueError():
            print("Input tidak valid!")
        
def update():
    print("0. Kembali ke menu utama")
    print(garis)
    print("DAFTAR BUNGA".center(40))
    print(garis)

    nomor = 1
    for i in ensiklopedia.values():
        print(f"{nomor}. {i["bunga"]}")
        nomor += 1

    try:
        edit = int(input("Masukkan nomor bunga yang ingin diedit: "))

        if edit == 0:
            pass
        elif edit >= 1 and edit <= len(ensiklopedia):
            id_bunga = list(ensiklopedia.keys()) 
            bunga_edit = ensiklopedia[id_bunga[edit - 1]]

            print(garis)
            print("EDIT BUNGA".center(40))
            print(garis)
            print("(Tekan Enter jika tidak ingin mengubah)")
            print(garis)

            while True:   
                nama_baru = input(f"Nama Bunga [{bunga_edit["bunga"]}]: ")
                deskripsi_baru = input(f"Deskripsi [{bunga_edit["deskripsi"]}]: ")
                makna_baru = input(f"Makna Bunga [{bunga_edit["makna"]}]: ")

                if nama_baru != "" and cek_bunga(nama_baru):
                    print("Koleksi sudah tersedia, silahkan input ulang!")
                    print(garis)
                    continue

                if nama_baru != "":
                    bunga_edit["bunga"] = nama_baru
                if deskripsi_baru != "":
                    bunga_edit["deskripsi"] = deskripsi_baru
                if makna_baru != "":
                    bunga_edit["makna"] = makna_baru

                
                print("Koleksi berhasil diedit!")
                break
        else:
            print("Koleksi tidak tersedi!")
    except ValueError():
        print("Input Tidak Valid!")

def delete():
    print("0. Kembali ke menu utama")
    print(garis)
    print("DAFTAR BUNGA".center(40))
    print(garis)

    nomor = 1
    for i in ensiklopedia.values():
        print(f"{nomor}. {i["bunga"]}")
        nomor += 1
    try:
        hapus = int(input("Masukkan nomor bunga yang ingin dihapus: "))
        if hapus == 0:
            pass
        elif hapus >= 1 and hapus <= len(ensiklopedia):
            id_bunga = list(ensiklopedia.keys()) 
            bunga_hapus = ensiklopedia[id_bunga[hapus - 1]]
            konfirmasi = input(f"Yakin hapus '{bunga_hapus["bunga"]}'(y/t)?: ").lower()
            if konfirmasi == "y":
                ensiklopedia.pop(id_bunga[hapus - 1])
                print("Koleksi berhasil dihapus!")
            elif konfirmasi == "t":
                print("Penghapusan dibatalkan.")
            else:
                print("Input tidak valid! pilih antara y/t")
        else:
            print("Koleksi tidak tersedi!")
    except ValueError():
        print("Input Tidak Valid!")

def cek_username(username):
    for user in data_user.values():
        if username == user["username"]:
            return True
    return False

def regis():
    while True:
        username = input("Silakan masukkan Username anda: ").strip()
        password = input("Silakan masukkan Password anda: ")

        if username == "" or password == "":
            print("Username dan Password tidak boleh kosong!")
            continue

        if cek_username(username):
            print("Username sudah dipakai!")
            continue

        id_baru = f"user{len(data_user)}"
        data_user[id_baru] = {
            "role": "user",
            "username": username,
            "password": password
        }
        print("Register berhasil! Silakan login.")
        break

def login(percobaan = 0):
    if percobaan == 3:                    
        print("Terlalu banyak percobaan gagal, kembali ke menu utama.")
        return None

    input_username = input("Silakan masukkan Username anda: ").strip()
    input_password = input("Silakan masukkan Password anda: ")

    for user in data_user.values():
        if input_username == user["username"] and input_password == user["password"]:
            return user["role"]            

    print(f"Username atau Password salah! Sisa percobaan: {2 - percobaan}")
    return login(percobaan + 1)

def admin():
    while True:
        menu_admin()
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
        if pilihan == "1":
            read()
        elif pilihan == "2":
            create()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            delete()
        elif pilihan == "5":
            print("Terimakasih telah mengunjungi Ensiklopedia!")
            break
        else:
            print("Pilihan Tidak Valid!")

def user():
    while True:
        menu_user()
        pilihan = input("Masukkan pilihan (1/2): ")
        if pilihan == "1":
            read()
        elif pilihan == "2":
            print("Terimakasih telah mengunjungi Ensiklopedia!")
            break
        else:
            print("Pilihan Tidak Valid!")

def menu():
    while True:
        menu_utama()
        pilihan = input("Masukkan pilihan (1/2/3): ")
        if pilihan == "1":
            regis()
        elif pilihan == "2":
            role = login()
            if role == "admin":
                admin()
            elif role == "user":
                user()
            else:
                menu()
        elif pilihan == "3":
            print("Terimakasih telah mengunjungi Ensiklopedia!")
            exit()
        else:
            print("Pilihan Tidak Valid!")

menu()
