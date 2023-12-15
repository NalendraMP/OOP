class Mahasiswa:
    total_mahasiswa = 0
    daftar_mahasiswa = []

    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        Mahasiswa.total_mahasiswa += 1
        Mahasiswa.daftar_mahasiswa.append(self)

    def tampilkan_biodata(self):
        print("\n")
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Jurusan: ", self.jurusan)

    @classmethod
    def tampilkan_total_mahasiswa(cls):
        print("Total Mahasiswa: ", cls.total_mahasiswa)

    @classmethod
    def tampilkan_daftar_mahasiswa(cls):
        print("\nDaftar Mahasiswa:")
        for mahasiswa in cls.daftar_mahasiswa:
            print("Nama: ", mahasiswa.nama)
            print("NIM: ", mahasiswa.nim)
            print("Jurusan: ", mahasiswa.jurusan)

    @classmethod
    def tambah_mahasiswa(cls):
        nama = input("Masukkan Nama Mahasiswa: ")
        nim = input("Masukkan NIM Mahasiswa: ")
        jurusan = input("Masukkan Jurusan Mahasiswa: ")
        mahasiswa = Mahasiswa(nama, nim, jurusan)
        print("Mahasiswa berhasil ditambahkan!")

    @classmethod
    def ubah_mahasiswa(cls):
        nim = input("Masukkan NIM Mahasiswa yang ingin diubah: ")
        for mahasiswa in cls.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                nama = input("Masukkan Nama Mahasiswa baru: ")
                jurusan = input("Masukkan Jurusan Mahasiswa baru: ")
                mahasiswa.nama = nama
                mahasiswa.jurusan = jurusan
                print("Mahasiswa berhasil diubah!")
                return
        print("Mahasiswa dengan NIM tersebut tidak ditemukan!")

    @classmethod
    def hapus_mahasiswa(cls):
        nim = input("Masukkan NIM Mahasiswa yang ingin dihapus: ")
        for mahasiswa in cls.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                cls.daftar_mahasiswa.remove(mahasiswa)
                Mahasiswa.total_mahasiswa -= 1
                print("Mahasiswa berhasil dihapus!")
                return
        print("Mahasiswa dengan NIM tersebut tidak ditemukan!")

# Program Utama
while True:
    print("\nMenu:")
    print("1. Tambah Mahasiswa")
    print("2. Ubah Mahasiswa")
    print("3. Hapus Mahasiswa")
    print("4. Tampilkan Daftar Mahasiswa")
    print("5. Tampilkan Total Mahasiswa")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        Mahasiswa.tambah_mahasiswa()
    elif pilihan == "2":
        Mahasiswa.ubah_mahasiswa()
    elif pilihan == "3":
        Mahasiswa.hapus_mahasiswa()
    elif pilihan == "4":
        Mahasiswa.tampilkan_daftar_mahasiswa()
    elif pilihan == "5":
        Mahasiswa.tampilkan_total_mahasiswa()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
