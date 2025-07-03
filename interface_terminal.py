# presentation.py
import business_logic

def tampilkan_menu():
    print("\n=== Menu Produk ===")
    print("1. Tambah Produk")
    print("2. Lihat Produk")
    print("3. Hapus Produk")
    print("4. Keluar")

def jalankan_aplikasi():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama produk: ")
            try:
                harga = float(input("Harga produk: "))
                business_logic.buat_produk(nama, harga)
                print("Produk berhasil ditambahkan.")
            except ValueError as e:
                print(f"Error: {e}")

        elif pilihan == "2":
            produk = business_logic.ambil_produk()
            if not produk:
                print("Belum ada produk.")
            else:
                print("Daftar Produk:")
                for i, p in enumerate(produk):
                    print(f"{i+1}. {p['nama']} - Rp{p['harga']}")

        elif pilihan == "3":
            nama = input("Masukkan nama produk yang ingin dihapus: ")
            business_logic.hapus_produk(nama)
            print("Produk dihapus (jika ada).")

        elif pilihan == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")