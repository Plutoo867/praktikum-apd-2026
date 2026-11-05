from data import data_user
from colored import fore, Style

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
            print(f"{fore(124)}Username dan Password tidak boleh kosong!{Style.reset}")
            continue

        if cek_username(username):
            print(f"{fore(124)}Username sudah dipakai!{Style.reset}")
            continue

        id_baru = f"user{len(data_user)}"
        data_user[id_baru] = {
            "role": "user",
            "username": username,
            "password": password
        }
        print(f"{fore(29)}Register berhasil! Silakan login.{Style.reset}")
        break

def login(percobaan = 0):
    if percobaan == 3:                    
        print(f"{fore(124)}Terlalu banyak percobaan gagal, kembali ke menu utama.{Style.reset}")
        return None

    input_username = input("Silakan masukkan Username anda: ").strip()
    input_password = input("Silakan masukkan Password anda: ")

    for user in data_user.values():
        if input_username == user["username"] and input_password == user["password"]:
            return user["role"]            

    print(f"{fore(124)}Username atau Password salah! Sisa percobaan: {2 - percobaan}{Style.reset}")
    return login(percobaan + 1)