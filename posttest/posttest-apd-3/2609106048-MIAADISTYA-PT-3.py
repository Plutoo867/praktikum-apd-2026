biaya_langganan = 1500000
nama = "mia"
nim = 48

print('''
=======================================
                ANGKASA 
=======================================
Selamat datang!!
''')
input_nama = input("Silahkan masukkan Nama anda: ")
input_nim = int(input("Silahkan masukkan NIM anda: "))

if input_nama == nama and input_nim == nim: 
    print('''
=======================================
             MENU ANGKASA
=======================================
1. Paket Orbit: Biaya admin 1% 
- Akses dasar ke lagu-lagu populer

2. Paket Nebula: Biaya admin 3% 
- Akses lagu premium  
- Playlist kustom

3. Paket Galaxy: Biaya admin 5%
- Akses lagu premium
- Playlist kustom
- Mode offline

4. Paket Supernova: Biaya admin 7% 
- Akses semua fitur
- Playlist kustom
- Mode offline
- Konten eksklusif artis

Biaya langganan sebesar Rp. 1.500.000
========================================
''')

    menu = int(input("Silahkan pilih menu antara 1-4 : "))
    if menu == 1:
        total_bayar = biaya_langganan + (biaya_langganan * 0.01)
        print(f'''
    Anda memilih Paket Orbit 
    Benefit : 
        - Akses dasar ke lagu lagu populer. 

    Berikut total pembayaran anda :
    Rp {total_bayar:,.0f} (sudah termasuk admin)'''.replace(",","."))

    elif menu == 2:
        total_bayar = biaya_langganan + (biaya_langganan * 0.03)
        print(f'''
    Anda memilih Paket Nebula 
    Benefit : 
        - Akses lagu premium  
        - Playlist kustom
            
    Berikut total pembayaran anda :
    Rp {total_bayar:,.0f} (sudah termasuk admin)'''.replace(",","."))
        
    elif menu == 3:
        total_bayar = biaya_langganan + (biaya_langganan * 0.05)
        print(f'''
    Anda memilih Paket Galaxy
    Benefit : 
        - Akses lagu premium
        - Playlist kustom
        - Mode offline
            
    Berikut total pembayaran anda :
    Rp {total_bayar:,.0f} (sudah termasuk admin)'''.replace(",","."))
     
    elif menu == 4:
        total_bayar = biaya_langganan + (biaya_langganan * 0.07)
        print(f'''
    Anda memilih Paket Supernova
    Benefit : 
        - Akses semua fitur
        - Playlist kustom
        - Mode offline
        - Konten eksklusif artis
            
    Berikut total pembayaran anda :
    Rp {total_bayar:,.0f} (sudah termasuk admin)'''.replace(",","."))

    else:
        print("Pilihan tidak tersedia. Pilih menu antara 1-4")

else:
    print("Login tidak berhasil, Nama atau NIM anda salah. Terimakasih telah mengunjungi ANGKASA")

