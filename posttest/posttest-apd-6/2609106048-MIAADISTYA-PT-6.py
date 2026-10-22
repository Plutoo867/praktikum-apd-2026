ensiklopedia = {}
id_terakhir = 0

data_user = {
    "admin" : {
        "role" : "admin",
        "username" : "admin",
        "password" : "admin123"
    }}

while True:
    print('''
===============================    
     MENU LOGIN & REGISTER
===============================
1. REGISTER
2. LOGIN
3. KELUAR
===============================
''')
    pilihan = input("Masukkan pilihan (1/2/3): ")
    if pilihan == "1":
        input_username = input("Silahkan masukkan Username anda: ").strip()
        input_password = input("Silahkan masukkan Password anda: ")

        if input_username == "" or input_password == "":
            print("Username dan Password tidak boleh kosong")
            continue

        username_terpakai = False
        for user in data_user.values():
            if input_username == user["username"]:
                username_terpakai = True
                break

        if username_terpakai:
            print("Username sudah dipakai!")
            continue

        i = (len(data_user)-1) + 1

        data_user.update({
            f"user{i}": {
                "role": "user",
                "username": input_username,
                "password": input_password
            }
        })
        print("Register berhasil!")

    elif pilihan == "2":
        while True:
            input_username = input("Silakan masukkan Username anda: ")
            input_password = input("Silakan masukkan Password anda: ")

            if input_username == "" or input_password == "":
                print("Username dan Password tidak boleh kosong")
                continue

            login_berhasil = False
            role_login = ""
            for user in data_user.values():
                if input_username == user["username"] and input_password == user["password"]:
                    login_berhasil = True
                    role_login = user["role"]
                    break

            if not login_berhasil:
                print("Username atau Password salah!")
                continue

            print("Login berhasil!")

            if role_login == "admin":
                while True:
                    print('''
=======================================
          ENSIKLOPEDIA BUNGA
=======================================
1. LIHAT KOLEKSI BUNGA 
2. TAMBAHKAN KOLEKSI BUNGA
3. EDIT KOLEKSI BUNGA
4. HAPUS KOLEKSI BUNGA
5. LOGOUT
=======================================
                    ''')
                    pilihan_admin = input("Masukkan pilihan (1/2/3/4/5): ")

                    if pilihan_admin == "1":
                        while True:
                            print("0. Kembali ke menu utama")
                            nomor = 1
                            print('''
=======================================
              DAFTAR BUNGA
=======================================
''')
                            for bunga in ensiklopedia.values():
                                print(f"{nomor}. {bunga["bunga"]}")
                                nomor += 1

                            detail = input("Masukkan nomor bunga untuk melihat detail: ")
                            if detail == "":
                                print("Input tidak boleh kosong!")

                            elif not detail.isdigit():
                                print("Input harus berupa angka!")

                            else:
                                detail = int(detail)
                                if detail >= 1 and detail <= len(ensiklopedia):
                                    id_bunga = list(ensiklopedia.keys()) 
                                    bunga_terpilih = ensiklopedia[id_bunga[detail - 1]]
                                    print('''
=======================================
              DETAIL BUNGA
=======================================
''')
                                    print(f"Nama Bunga   : {bunga_terpilih["bunga"]}")
                                    print(f"Deskripsi    : {bunga_terpilih["deskripsi"]}")
                                    print(f"Makna Bunga  : {bunga_terpilih["makna"]}")
                                elif detail == 0:
                                    break
                                else:
                                    print("Nomor bunga tidak valid.")

                    elif pilihan_admin == "2":
                        while True:
                            nama = input("Masukkan nama bunga      : ")
                            desk = input("Masukkan deskripsi bunga : ")
                            makna = input("Masukkan makna bunga     : ")

                            if nama == "" or desk == "" or makna == "":
                                print("Kolom tidak boleh kosong!")
                                continue
                    
                            bunga_terpakai = False
                            for bunga in ensiklopedia.values():
                                if nama == bunga["bunga"]:
                                    bunga_terpakai = True
                                    break
                    
                            if bunga_terpakai:
                                print("Koleksi sudah tersedia, silahkan input ulang!")
                                print("=============================================")
                                continue

                            else:
                                id_terakhir += 1

                                ensiklopedia[f"id{id_terakhir}"] =(
                                                {
                                                "bunga": nama,
                                                "deskripsi": desk, 
                                                "makna": makna
                                                }
                                            )
                                print("Koleksi berhasil di tambahkan!")
                                break

                    elif pilihan_admin == "3":
                        print("0. Kembali ke menu utama")
                        nomor = 1
                        print('''
=======================================
              DAFTAR BUNGA
=======================================
''')
                        for i in ensiklopedia.values():
                            print(f"{nomor}. {i["bunga"]}")
                            nomor += 1

                        edit = input("Masukkan nomor bunga yang ingin diedit: ")
                        if edit == "":
                            print("Input tidak boleh kosong!")

                        elif not edit.isdigit():
                            print("Input harus berupa angka!")

                        else:
                            edit = int(edit)
                            if edit == 0:
                                pass
                            elif edit >= 1 and edit <= len(ensiklopedia):
                                id_bunga = list(ensiklopedia.keys()) 
                                bunga_edit = ensiklopedia[id_bunga[edit - 1]]
                                print('''
=======================================
              EDIT BUNGA
=======================================
(Tekan Enter jika tidak ingin mengubah)
''')
                                nama_baru = input(f"Nama Bunga [{bunga_edit["bunga"]}]: ")
                                deskripsi_baru = input(f"Deskripsi [{bunga_edit["deskripsi"]}]: ")
                                makna_baru = input(f"Makna Bunga [{bunga_edit["makna"]}]: ")

                                if nama_baru != "":
                                    bunga_edit["bunga"] = nama_baru
                                if deskripsi_baru != "":
                                    bunga_edit["deskripsi"] = deskripsi_baru
                                if makna_baru != "":
                                    bunga_edit["makna"] = makna_baru

                                print("Koleksi berhasil diedit!")

                            else:
                                print("Nomor bunga tidak valid.")

                    elif pilihan_admin == "4":
                        print("0. Kembali ke menu utama")
                        nomor = 1
                        print('''
=======================================
              DAFTAR BUNGA
=======================================
''')
                        for i in ensiklopedia.values():
                            print(f"{nomor}. {i["bunga"]}")
                            nomor += 1
                        hapus = input("Masukkan nomor bunga yang ingin dihapus: ")
                        if hapus == "":
                            print("Input tidak boleh kosong!")

                        elif not hapus.isdigit():
                            print("Input harus berupa angka!")

                        else:
                            hapus = int(hapus)
                            if hapus == 0:
                                pass
                            elif hapus >= 1 and hapus <= len(ensiklopedia):
                                id_bunga = list(ensiklopedia.keys()) 
                                bunga_hapus = ensiklopedia[id_bunga[hapus - 1]]
                                konfirmasi = input(f"Yakin hapus '{bunga_hapus["bunga"]}'(y/t)?: ").lower()
                                if konfirmasi == "y":
                                    ensiklopedia.pop(id_bunga[hapus - 1])
                                    print("Koleksi berhasil dihapus!")
                                else:
                                    print("Penghapusan dibatalkan.")
                            else:
                                print("Nomor bunga tidak valid.")

                    elif pilihan_admin == "5":
                        print("Terimakasih telah mengunjungi Ensiklopedia Bunga!")
                        break

                    elif pilihan_admin == "":
                        print("Pilihan tidak boleh kosong!")

                    else:
                        print("pilihan tidak tersedia!")
            
            else:
                while True:
                    print('''
=======================================
        ENSIKLOPEDIA BUNGA
=======================================
1. LIHAT KOLEKSI BUNGA 
2. LOGOUT
=======================================
''')
                    pilihan_user = input("Masukkan pilihan (1/2): ")
                    if pilihan_user == "1":
                        while True:
                            print("0. Kembali ke menu utama")
                            nomor = 1
                            print('''
=======================================
             DAFTAR BUNGA
=======================================
''')
                            for i in ensiklopedia.values():
                                print(f"{nomor}. {i["bunga"]}")
                                nomor += 1

                            detail = input("Masukkan nomor bunga untuk melihat detail: ")
                            if detail == "":
                                print("Input tidak boleh kosong!")

                            elif not detail.isdigit():
                                print("Input harus berupa angka!")

                            else:
                                detail = int(detail)
                                if detail >= 1 and detail <= len(ensiklopedia):
                                    id_bunga = list(ensiklopedia.keys()) 
                                    bunga_terpilih = ensiklopedia[id_bunga[detail - 1]]
                                    print('''
=======================================
             DETAIL BUNGA
=======================================
''')
                                    print(f"Nama Bunga   : {bunga_terpilih["bunga"]}")
                                    print(f"Deskripsi    : {bunga_terpilih["deskripsi"]}")
                                    print(f"Makna Bunga  : {bunga_terpilih["makna"]}")
                                elif detail == 0:
                                    kembali = True
                                    break
                                else:
                                    print("Nomor bunga tidak valid.")

                    elif pilihan_user == "2":
                        print("Terimakasih telah mengunjungi Ensiklopedia Bunga!")
                        break

                    elif pilihan_user == "":
                        print("Pilihan tidak boleh kosong!")
                    
                    else:
                        print("Pilihan tidak tersedia!")
            
            break

    elif pilihan == "3":
        print("Terimakasih telah mengunjungi Ensiklopedia Bunga!")
        break

    elif pilihan == "":
        print("Pilihan tidak boleh kosong!")

    else:
        print("Pilihan tidak tersedia!")