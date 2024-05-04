class Contact:
    def __init__(self, nama, nomor_telepon, email):
        self.nama = nama
        self.nomor_telepon = nomor_telepon
        self.email = email

class ContactManager:
    def __init__(self):
        self.daftar_kontak = []

    def tambah_kontak(self, nama, nomor_telepon, email):
        self.daftar_kontak.append(Contact(nama, nomor_telepon, email))
        print("Kontak berhasil ditambahkan.")

    def lihat_semua_kontak(self):
        for kontak in self.daftar_kontak:
            print(f"Nama: {kontak.nama}, Telepon: {kontak.nomor_telepon}, Email: {kontak.email}")

    def hapus_kontak(self, nama):
        for kontak in self.daftar_kontak:
            if kontak.nama == nama:
                self.daftar_kontak.remove(kontak)
                print(f"Kontak {nama} berhasil dihapus.")
                return
        print(f"Kontak dengan nama {nama} tidak ditemukan.")

    def cari_kontak(self, nama):
        for kontak in self.daftar_kontak:
            if kontak.nama == nama:
                print(f"Nama: {kontak.nama}, Telepon: {kontak.nomor_telepon}, Email: {kontak.email}")
                return
        print(f"Kontak dengan nama {nama} tidak ditemukan.")

if __name__ == "__main__":
    manager = ContactManager()

    while True:
        print("\nPilih operasi yang ingin Anda lakukan:")
        print("1. Tambah Kontak")
        print("2. Lihat Semua Kontak")
        print("3. Hapus Kontak")
        print("4. Cari Kontak")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == "1":
            nama = input("Masukkan nama kontak: ")
            nomor_telepon = input("Masukkan nomor telepon kontak: ")
            email = input("Masukkan email kontak: ")
            manager.tambah_kontak(nama, nomor_telepon, email)
        elif pilihan == "2":
            manager.lihat_semua_kontak()
        elif pilihan == "3":
            nama = input("Masukkan nama kontak yang ingin dihapus: ")
            manager.hapus_kontak(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama kontak yang ingin dicari: ")
            manager.cari_kontak(nama)
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")