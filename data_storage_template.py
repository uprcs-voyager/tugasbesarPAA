class Pasien : 
    def __init__(self, id_pasien, nama_pasien, jenis_kelamin, umur, gejala, skor) : 
        self.id_pasien = id_pasien
        self.nama_pasien = nama_pasien
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur
        self.gejala = gejala
        self.skor =skor

list_antrean = []

def tambah_pasien_baru() :
    print("======== SILAHKAN MASUKAN DATA PASIEN BARU ===========")
    id_pasien = input("Masukan ID pasien: ")
    nama_pasien = input("Masukan nama pasien")
    jenis_kelamin = input ("Masukan jenis kelamin pasien (L/P): ")
    umur_pasien = int(input("Masukan umur pasien: "))
    gejala_pasien = input("Jelaskan gejala pasien: ")
    skor_pasien = int(input("Berikan skor kegawatan kepada pasien (1-50): "))

    pasien_baru = Pasien(id_pasien, nama_pasien, jenis_kelamin, umur_pasien, gejala_pasien, skor_pasien)


print("====================----SELAMAT DATANG SILAHKAN PILIH DARI MENU DIBAWAH INI ----=======================")
print("1. Tambahkan pasien")
print("2. Cari Pasien")
pilihan_user = (int(input("Silahkan masukan pilihan anda (1/2): ")))

if pilihan_user == 1 : 
    tambah_pasien_baru()
elif pilihan_user == 2 : 
    print("fitur pencarian masih dibuat")
else : 
    print("Masukan anda tidak valid ")

