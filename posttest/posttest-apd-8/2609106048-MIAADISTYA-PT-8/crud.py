from data import ensiklopedia
from prettytable import PrettyTable
from colored import fore, Style

id_terakhir = 1

def daftar_bunga(ensiklopedia):
    warna_judul: str = f"{fore(204)}"
    warna_isi: str = f"{fore(197)}"
    table = PrettyTable()

    table.title = (f"{warna_judul}DAFTAR BUNGA{Style.reset}")
    table.field_names = ["No", "Nama Bunga"]
    table.header = False
    table.max_width["No"] = 3
    table.min_width["Nama Bunga"] = 35
    table.align["Nama Bunga"] = "l"


    for nomor, bunga in enumerate(ensiklopedia.values(), start=1):
        bunga = (f"{warna_isi}{bunga["bunga"]}{Style.reset}")
        table.add_row([nomor, bunga])

    print(table)

def table_detail(data):
    table = PrettyTable()

    table.title = "DETAIL BUNGA"
    table.field_names = ["Label", "Isi"]

    table.header = False
    table.align = "l"
    table.max_width["Label"] = 15
    table.min_width["Isi"] = 25
    table.max_width["Isi"] = 25

    for label, isi in data.items():
        table.add_row([label, isi])

    print(table)

def read():
    while True:
        print("0. Kembali ke menu utama")
        daftar_bunga(ensiklopedia)
        try:
            detail = int(input("Masukkan nomor bunga untuk melihat detail: "))
            if detail >= 1 and detail <= len(ensiklopedia):
                id_bunga = list(ensiklopedia.keys()) 
                bunga_terpilih = ensiklopedia[id_bunga[detail - 1]]
                detail_bunga = {
                    "Nama Bunga": bunga_terpilih["bunga"],
                    "Deskripsi": bunga_terpilih["deskripsi"],
                    "Makna Bunga": bunga_terpilih["makna"],
                }
                table_detail(detail_bunga)
            elif detail == 0:
                break
            else:
                print(f"{fore(124)}Koleksi tidak tersedia!{Style.reset}")
        except ValueError:
            print(f"{fore(124)}Input Tidak Valid!{Style.reset}")

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
                print(f"{fore(124)}Koleksi sudah tersedia, silahkan input ulang!{Style.reset}")
                continue

            elif nama == "" or desk == "" or makna == "":
                print(f"{fore(124)}Kolom tidak boleh kosong!{Style.reset}")
                continue

            else:
                ensiklopedia[id_bunga()] =({
                                "bunga": nama,
                                "deskripsi": desk, 
                                "makna": makna
                                })
                print(f"{fore(29)}Koleksi berhasil di tambahkan!{Style.reset}")
                break
        except ValueError:
            print(f"{fore(124)}Input Tidak Valid!{Style.reset}")
        
def update():
    print("0. Kembali ke menu utama")
    daftar_bunga(ensiklopedia)
    try:
        edit = int(input("Masukkan nomor bunga yang ingin diedit: "))

        if edit == 0:
            pass
        elif edit >= 1 and edit <= len(ensiklopedia):
            id_bunga = list(ensiklopedia.keys()) 
            bunga_edit = ensiklopedia[id_bunga[edit - 1]]

            print(f"{fore(29)}(Tekan Enter jika tidak ingin mengubah){Style.reset}")

            while True:   
                nama_baru = input(f"Nama Bunga [{bunga_edit["bunga"]}]: ")
                deskripsi_baru = input(f"Deskripsi [{bunga_edit["deskripsi"]}]: ")
                makna_baru = input(f"Makna Bunga [{bunga_edit["makna"]}]: ")

                if nama_baru != "" and cek_bunga(nama_baru):
                    print(f"{fore(124)}Koleksi sudah tersedia, silahkan input ulang!{Style.reset}")
                    continue

                if nama_baru != "":
                    bunga_edit["bunga"] = nama_baru
                if deskripsi_baru != "":
                    bunga_edit["deskripsi"] = deskripsi_baru
                if makna_baru != "":
                    bunga_edit["makna"] = makna_baru

                
                print(f"{fore(29)}Koleksi berhasil diedit!{Style.reset}")
                break
        else:
            print(f"{fore(124)}Koleksi tidak tersedi!{Style.reset}")
    except ValueError:
        print(f"{fore(124)}Input Tidak Valid!{Style.reset}")

def delete():
    print("0. Kembali ke menu utama")
    daftar_bunga(ensiklopedia)
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
                print(f"{fore(29)}Koleksi berhasil dihapus!{Style.reset}")
            elif konfirmasi == "t":
                print(f"{fore(29)}Penghapusan dibatalkan.{Style.reset}")
            else:
                print(f"{fore(124)}Input tidak valid! pilih antara y/t{Style.reset}")
        else:
            print(f"{fore(124)}Koleksi tidak tersedi!{Style.reset}")
    except ValueError:
        print(f"{fore(124)}Input Tidak Valid!{Style.reset}")