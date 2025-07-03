# aut.py
from database import users

def login():
    percobaan = 0
    while percobaan < 3:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if not username or not password:
            print("Username dan/atau password tidak boleh kosong.\n")
        elif username in users and users[username] == password:
            print("Login berhasil!\n")
            return True
        elif username in users:
            print("Password salah.\n")
        elif password in users.values():
            print("Username salah.\n")
        else:
            print("Username dan password salah.\n")

        percobaan += 1
        print(f"Percobaan ke-{percobaan} dari 3\n")

    print("Login gagal lebih dari 3 kali. Program berhenti.")
    return False