class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        Mahasiswa.total_mahasiswa += 1

    def tampilkan_biodata(self):
        print("\n")
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Jurusan: ", self.jurusan)
       
        

    @classmethod
    def tampilkan_total_mahasiswa(cls):
        print("Total Mahasiswa: ", cls.total_mahasiswa)


# Input data mahasiswa
nama = input("Masukkan Nama Mahasiswa: ")
nim = input("Masukkan NIM Mahasiswa: ")
jurusan = input("Masukkan Jurusan Mahasiswa: ")



# Membuat objek mahasiswa
mahasiswa = Mahasiswa(nama, nim, jurusan)

# Menampilkan biodata mahasiswa
mahasiswa.tampilkan_biodata()

# Menampilkan total mahasiswa
Mahasiswa.tampilkan_total_mahasiswa()
