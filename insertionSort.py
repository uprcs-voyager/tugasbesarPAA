class Pasien : 
    def __init__(self, id_pasien, nama_pasien, jenis_kelamin, umur, gejala, skor) : 
        self.id_pasien = id_pasien
        self.nama_pasien = nama_pasien
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur
        self.gejala = gejala
        self.skor =skor

list_antrean = []


def descending_insertionSort(list_antrean):
    n = len(list_antrean)

    for i in range(1,n):
        terbaru = list_antrean[i]
        j = i-1

        while j >= 0 and list_antrean[j].skor < terbaru.skor:
            list_antrean[j + 1] = list_antrean[j]
            j -= 1

        list_antrean[j + 1] = terbaru

    
    return list_antrean

def ascending_insertionSort(list_antrean):
    n = len(list_antrean)

    for i in range(1,n):
        terbaru = list_antrean[i]
        j = i-1

        while j >= 0 and list_antrean[j].skor > terbaru.skor:
            list_antrean[j + 1] = list_antrean[j]
            j -= 1

        list_antrean[j + 1] = terbaru

    
    return list_antrean


def tambah_pasien_baru(list_antrean) :
    print("======== SILAHKAN MASUKAN DATA PASIEN BARU ===========")
    id_pasien = input("Masukan ID pasien: ")
    nama_pasien = input("Masukan nama pasien: ")
    jenis_kelamin = input("Masukan jenis kelamin pasien (L/P): ").lower()
    while True:
        if jenis_kelamin != "l" and jenis_kelamin != "p":
            print("Silahkan input sesuai opsi!")
            jenis_kelamin = input("Masukan jenis kelamin pasien (L/P): ").lower()
            continue
        break
    
    while True:
        try:
            umur_pasien = int(input("Masukan umur pasien: "))

            if umur_pasien < 1:
                print("Umur Pasien tidak bisa kurang dari 0!")
                continue
            break
        except ValueError:
            print("Data umur harus berupa angka!")

    gejala_pasien = input("Jelaskan gejala pasien: ")

    while True:
        try:
            skor_pasien = int(input("Berikan skor kegawatan kepada pasien (1-50): "))

            if skor_pasien < 1 or skor_pasien > 50:
                print("Skor Darurat Pasien hanya terdiri dari 1-50!")
                continue
            break
        except ValueError:
            print("Data skor darurat pasien harus berupa angka!")

    pasien_baru = Pasien(id_pasien, nama_pasien, jenis_kelamin, umur_pasien, gejala_pasien, skor_pasien)

    list_antrean.append(pasien_baru)

    descending_insertionSort(list_antrean)

    print("Data Pasien Berhasil Ditambahkan")
    return list_antrean


def menu_utama():
    print("====================----SELAMAT DATANG SILAHKAN PILIH DARI MENU DIBAWAH INI ----=======================")
    print("1. Tambahkan pasien")
    print("2. Cari Pasien")
    print("3. Keluar")

    while True: 
        try:
            pilihan_user = (int(input("Silahkan masukan pilihan anda (1 - 3): ")))
            if 1 <= pilihan_user <= 3:
                return pilihan_user
            else:
                print("Pilihan yang tersedia hanya 1 sampai 3!")
        except ValueError:
            print("Input harus berupa angka")


pilihan_user = 0

while pilihan_user != 3:
    pilihan_user = menu_utama()

    if pilihan_user == 1 : 
        tambah_pasien_baru(list_antrean)
    elif pilihan_user == 2 : 
        if not list_antrean:
            print("Saat ini belum ada data pasien dalam antrean!")
            continue

        print("\n=== PILIH JENIS PENGURUTAN ===")
        print("1. Skor darurat tertinggi")
        print("2. Skor darurat terendah")

        while True:
            try:
                pilihan_sort = int(input("Masukkan pilihan (1-2): "))

                if pilihan_sort == 1:
                    descending_insertionSort(list_antrean)
                    break

                elif pilihan_sort == 2:
                    ascending_insertionSort(list_antrean)
                    break

                else:
                    print("Pilihan hanya 1 atau 2!")

            except ValueError:
                print("Input harus berupa angka!")

        print("\n=== DAFTAR ANTREAN PASIEN ===")
        for pasien in list_antrean:
            print(
                f"ID: {pasien.id_pasien} | "
                f"Nama: {pasien.nama_pasien} | "
                f"Skor: {pasien.skor}"
            )
    

print("Terima Kasih Telah Menggunakan Layanan Ini! ")

