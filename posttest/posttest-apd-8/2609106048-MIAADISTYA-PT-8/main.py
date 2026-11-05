from admin import menu_admin
from user import menu_user
from auth import regis, login
from prettytable import PrettyTable
from colored import fore, Style

def menu_utama():
    warna_judul: str = f"{fore(26)}"
    warna_isi: str = f"{fore(19)}"

    table = PrettyTable()
    table.title = (f"{warna_judul}MENU LOGIN & REGISTER{Style.reset}")
    table.field_names = ["No", "Menu"]
    table.header = False
    table.align["No"] = "c"
    table.align["Menu"] = "l"

    table.add_rows([
        [1, f"{warna_isi}REGISTER{Style.reset}"],
        [2, f"{warna_isi}LOGIN{Style.reset}"],
        [3, f"{warna_isi}KELUAR{Style.reset}"],
        ])

    print(table)

def menu():
    while True:
        menu_utama()
        pilihan = input("Masukkan pilihan (1/2/3): ")
        if pilihan == "1":
            regis()
        elif pilihan == "2":
            role = login()
            if role == "admin":
                menu_admin()
            elif role == "user":
                menu_user()
            else:
                menu()
        elif pilihan == "3":
            print(f"{fore(29)}Terimakasih telah mengunjungi Ensiklopedia!{Style.reset}")
            exit()
        else:
            print(f"{fore(124)}Input Tidak Valid!{Style.reset}")

menu()
