from interface_terminal import jalankan_aplikasi
from aut import login

if __name__ == "__main__":
    if login():
        jalankan_aplikasi()