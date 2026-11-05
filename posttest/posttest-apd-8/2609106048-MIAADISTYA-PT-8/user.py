from crud import read
from prettytable import PrettyTable
from colored import fore, Style

def menu_user():
    while True:
        warna_judul: str = f"{fore(204)}"
        warna_isi: str = f"{fore(197)}"

        table = PrettyTable()
        table.title = f"{warna_judul}ENSIKLOPEDIA BUNGA{Style.reset}"
        table.field_names = ["No", "Menu"]
        table.header = False
        table.align["No"] = "c"
        table.align["Menu"] = "l"

        table.add_rows([
            [1, f"{warna_isi}LIHAT KOLEKSI BUNGA{Style.reset}"],
            [2, f"{warna_isi}LOGOUT{Style.reset}"],
        ])
        print(table)

        pilihan = input("Masukkan pilihan (1/2): ")
        if pilihan == "1":
            read()
        elif pilihan == "2":
            print(f"{fore(29)}Terimakasih telah mengunjungi Ensiklopedia!{Style.reset}")
            break
        else:
            print(f"{fore(124)}Input Tidak Valid!{Style.reset}")