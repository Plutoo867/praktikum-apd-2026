ensiklopedia = []

data_user = [
    ["admin", "admin", "admin123"]
]

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
        for role, username, password in data_user:
            if input_username == username:
                username_terpakai = True
                break

        if username_terpakai:
            print("Username sudah dipakai!")
            continue

        data_user.append(["user", input_username, input_password])
        print("Register berhasil!")

    elif pilihan == "2":
        while True:
            input_username = input("Silahkan masukkan Username anda: ")
            input_password = input("Silahkan masukkan Password anda: ")

            if input_username == "" or input_password == "":
                print("Username dan Password tidak boleh kosong")
                continue

            login_berhasil = False
            role_login = ""
            for role, username, password in data_user:
                if input_username == username and input_password == password:
                    login_berhasil = True
                    role_login = role
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
5. KELUAR
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
                            for i in ensiklopedia:
                                print(f"{nomor}. {i[0]}")
                                nomor += 1

                            detail = input("Masukkan nomor bunga untuk melihat detail: ")
                            if detail == "":
                                print("Input tidak boleh kosong!")

                            elif not detail.isdigit():
                                print("Input harus berupa angka!")

                            else:
                                detail = int(detail)
                                if detail >= 1 and detail <= len(ensiklopedia):
                                    bunga_terpilih = ensiklopedia[detail - 1]
                                    print('''
=======================================
              DETAIL BUNGA
=======================================
''')
                                    print(f"Nama Bunga   : {bunga_terpilih[0]}")
                                    print(f"Deskripsi    : {bunga_terpilih[1]}")
                                    print(f"Makna Bunga  : {bunga_terpilih[2]}")
                                elif detail == 0:
                                    break
                                else:
                                    print("Nomor bunga tidak valid.")

                    elif pilihan_admin == "2":
                        nama = input("Masukkan nama bunga      : ")
                        desk = input("Masukkan deskripsi bunga : ")
                        makna = input("Masukkan makna bunga     : ")

                        if nama == "" and desk == "" and makna == "":
                            print("Input tidak boleh kosong!")

                        else:
                            print("Koleksi berhasil di tambahkan!")
                            ensiklopedia.append([nama, desk, makna])

                    elif pilihan_admin == "3":
                        print("0. Kembali ke menu utama")
                        nomor = 1
                        print('''
=======================================
              DAFTAR BUNGA
=======================================
''')
                        for i in ensiklopedia:
                            print(f"{nomor}. {i[0]}")
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
                                bunga_edit = ensiklopedia[edit - 1]
                                print('''
=======================================
              EDIT BUNGA
=======================================
(Tekan Enter jika tidak ingin mengubah)
''')
                                nama_baru = input(f"Nama Bunga [{bunga_edit[0]}]: ")
                                deskripsi_baru = input(f"Deskripsi [{bunga_edit[1]}]: ")
                                makna_baru = input(f"Makna Bunga [{bunga_edit[2]}]: ")

                                if nama_baru != "":
                                    bunga_edit[0] = nama_baru
                                if deskripsi_baru != "":
                                    bunga_edit[1] = deskripsi_baru
                                if makna_baru != "":
                                    bunga_edit[2] = makna_baru

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
                        for i in ensiklopedia:
                            print(f"{nomor}. {i[0]}")
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
                                bunga_hapus = ensiklopedia[hapus - 1]
                                konfirmasi = input(f"Yakin hapus '{bunga_hapus[0]}' (y/t)?: ").lower()
                                if konfirmasi == "y":
                                    ensiklopedia.pop(hapus - 1)
                                    print("Koleksi berhasil dihapus!")
                                else:
                                    print("Penghapusan dibatalkan.")
                            else:
                                print("Nomor bunga tidak valid.")

                    elif pilihan_admin == "5":
                        print("Terimakasih telah mengunjungi Ensiklopedia Bunga!")
                        exit()

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
2. KELUAR
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
                            for i in ensiklopedia:
                                print(f"{nomor}. {i[0]}")
                                nomor += 1

                            detail = input("Masukkan nomor bunga untuk melihat detail: ")
                            if detail == "":
                                print("Input tidak boleh kosong!")

                            elif not detail.isdigit():
                                print("Input harus berupa angka!")

                            else:
                                detail = int(detail)
                                if detail >= 1 and detail <= len(ensiklopedia):
                                    bunga_terpilih = ensiklopedia[detail - 1]
                                    print('''
=======================================
             DETAIL BUNGA
=======================================
''')
                                    print(f"Nama Bunga   : {bunga_terpilih[0]}")
                                    print(f"Deskripsi    : {bunga_terpilih[1]}")
                                    print(f"Makna Bunga  : {bunga_terpilih[2]}")
                                elif detail == 0:
                                    kembali = True
                                    break
                                else:
                                    print("Nomor bunga tidak valid.")

                    elif pilihan_user == "2":
                        print("Terimakasih telah mengunjungi Ensiklopedia Bunga!")
                        exit()

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
