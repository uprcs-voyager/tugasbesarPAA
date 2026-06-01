# PROGRAM ANTRIAN ADAPTIF 


# membuat class untuk penyimpanan data pasien 
class Pasien : 
    def __init__(self, id_pasien, nama_pasien, jenis_kelamin, umur, gejala, skor) : 
        self.id_pasien = id_pasien
        self.nama_pasien = nama_pasien
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur
        self.gejala = gejala
        self.skor =skor
# tempat data pasien disimpan 
list_antrean = []







def insertionSort(list_antrean):
    n = len(list_antrean)

    for i in range(1,n):
        terbaru = list_antrean[i]
        j = i-1

        while j >= 0 and list_antrean[j].skor < terbaru.skor:
            list_antrean[j + 1] = list_antrean[j]
            j -= 1

        list_antrean[j + 1] = terbaru

    return list_antrean



# ===================================== kode pilihan metode pencarian user ==============================================
def cari_pasien():
    print("\nSilahkan pilih antara dua metode pencarian dibawah ini")
    print("1. Cari berdasarkan kategori")
    print("2. Cari berdasarkan skor kegawatan")
    pilihan_user = int(input("\nMasukan pilihan anda (1/2): "))
    if pilihan_user == 1 :
        cariBerdasarkanKategori()
    elif pilihan_user == 2 : 
        tampilancariBerdasarkanSkor()
    else : 
        print("Input anda tidak valid")
# ==================================================================================== Kode pencarian berdasarkan kategori ====================================================================================================================




# ==================================================================================== Kode pencarian berdasarkan kategori ====================================================================================================================

# Fungsi untuk mencari berdasarkan kategori kegawatan pasien 
def cariBerdasarkanKategori() : 
    print("\nSilahkan pilih kategori yang ingin anda cari: ")
    print("1. Tidak Bahaya(1-10)\n2. Ringan(11-20)\n3. Menengah(21-30)\n4. Gawat(31-40)\n5. Gawat Darurat(41-50)")
    try : 
        pilihan_user = int(input("Masukan Pilihan kategori yang ingin anda cari (1/2/3/4/5): "))
    except ValueError : 
        print("Masukan anda tidak valid")
    
    if pilihan_user == 1 : 
        skor_min = 1
        skor_max = 10
        kategori = "Tidak Bahaya"
    elif pilihan_user == 2 : 
        skor_min = 11
        skor_max = 20
        kategori = "Ringan"
    elif pilihan_user == 3 : 
        skor_min = 21
        skor_max = 30
        kategori = "Menengah"
    elif pilihan_user == 4 : 
        skor_min = 31
        skor_max = 40
        kategori = "Gawat"
    elif pilihan_user == 5 : 
        skor_min = 41
        skor_max= 50
        kategori = "Gawat Darurat"
    else :
        print("Pilihan tidak tersedia")

    idx_batas_kiri = cariBatasKiri(list_antrean, skor_max)
    idx_batas_kanan = cariBatasKanan(list_antrean, skor_min)

# Kode untuk menampilkan hasil dari data pasien yang sudah dicari ==============================================
    if idx_batas_kiri ==-1 or idx_batas_kanan ==-1 or idx_batas_kiri > idx_batas_kanan : 
        print(f"\ntidak menemukan pasien pada kategori {kategori}")
        return
    # Header
    print(f"\nBerikut adalah pasien yang ada pada kategori {kategori} (skor {skor_min} - {skor_max})")
    print("ID PASIEN  | Nama Pasien       | Kelamin Pasien  | Umur Pasien  |  Gejala Pasien            |  Skor Kegawatan")
# List perulangan untuk menampilkan data pasien 
    for i in range (idx_batas_kiri, idx_batas_kanan + 1) :
        pasien = list_antrean[i]
        print(f"| {pasien.id_pasien:<10} | {pasien.nama_pasien:<17} | {pasien.jenis_kelamin:<15} | {pasien.umur:<12} | {pasien.gejala:25} | {pasien.skor}")
        print("\n")
        
def cariBatasKiri(antrean, batas_atas) : 
    indeks_kiri = 0
    indeks_kanan = len(antrean) - 1
    indeks_hasil = -1

    while indeks_kiri <= indeks_kanan : 
        indeks_tengah = (indeks_kiri + indeks_kanan) //2
        skor_tengah = antrean[indeks_tengah].skor

        if skor_tengah > batas_atas : 
            indeks_kiri = indeks_tengah + 1
        
        else : 
            indeks_hasil = indeks_tengah

            indeks_kanan = indeks_tengah - 1 
    return indeks_hasil


def cariBatasKanan (antrean, batas_bawah) :
    indeks_kiri = 0
    indeks_kanan = len(antrean) - 1
    indeks_hasil = -1

    while indeks_kiri <= indeks_kanan : 
        indeks_tengah = (indeks_kanan + indeks_kiri) //2
        skor_tengah = antrean[indeks_tengah].skor

        if skor_tengah < batas_bawah : 
            indeks_kanan = indeks_tengah - 1 
        
        else : 
            indeks_hasil = indeks_tengah

            indeks_kiri = indeks_tengah + 1

    return indeks_hasil












# ========================= kode jikauser mencari berdasarkan skor eksak
def tampilancariBerdasarkanSkor() : 
    print("\nSilahkan masukan skor kegawatan yang ingin anda cari ")
    pilihan_user = int(input("Masukan skor kegawatan (angka): "))
    hasil = cariBerdasarkanSkor(list_antrean, pilihan_user)
    if hasil == -1:
        print(f"\nTidak ditemukan pasien dengan skor kegawatan {pilihan_user}.")
        return
# Header
    print(f"\nBerikut adalah pasien yang ada dengan skor {pilihan_user}")
    print("ID PASIEN  | Nama Pasien       | Kelamin Pasien  | Umur Pasien  |  Gejala Pasien            |  Skor Kegawatan")

    batas_kiri = hasil
    batas_kanan = hasil

    while batas_kiri > 0 and list_antrean[batas_kiri-1].skor ==  pilihan_user : 
        batas_kiri -=1
    while batas_kanan < len(list_antrean)-1 and list_antrean[batas_kanan+1].skor == pilihan_user : 
        batas_kanan +=1
    
    for i in range (batas_kiri, batas_kanan+1) : 
        pasien = list_antrean[i]
        print(f"| {pasien.id_pasien:<10} | {pasien.nama_pasien:<17} | {pasien.jenis_kelamin:<15} | {pasien.umur:<12} | {pasien.gejala:25} | {pasien.skor}")
        print("\n")

def cariBerdasarkanSkor(antrean, pilihan_user) : 
    low = 0
    high = len(antrean)-1
    while low <= high : 
        mid  = (low+high)//2
        # Ekstrak nilai skor dari variable 
        skor_tengah = antrean[mid].skor
        # Cek nilai tengah apakah sesuai dengan input user 
        if skor_tengah == pilihan_user : 
            return mid
        
        elif skor_tengah < pilihan_user : 
            high = mid-1

        else : 
            low = mid+1

    return -1






def tambah_pasien_baru(list_antrean) :
    print("\n======== SILAHKAN MASUKAN DATA PASIEN BARU ===========")
    id_pasien = int(input("Masukan ID pasien: "))
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

    insertionSort(list_antrean)

    print("\nData Pasien Berhasil Ditambahkan\n")
    return list_antrean












def menu_utama() : 
    print("====================----SELAMAT DATANG SILAHKAN PILIH DARI MENU DIBAWAH INI ----=======================")
    print("1. Tambahkan pasien")
    print("2. daftar antrian pasien")
    print("3. Cari Data Pasien")
    print("4. Keluar dari program")

    while True: 
        try:
            pilihan_user = (int(input("Silahkan masukan pilihan anda (1 - 4): ")))
            if 1 <= pilihan_user <= 4:
                return pilihan_user
            else:
                print("Pilihan yang tersedia hanya 1 sampai 4!")
        except ValueError:
            print("Input harus berupa angka")



pilihan_user = 0

while pilihan_user != 4:
    pilihan_user = menu_utama()


    if pilihan_user == 1 : 
        tambah_pasien_baru(list_antrean)
    elif pilihan_user == 2 : 
        insertionSort(list_antrean)
        print("\n=== DAFTAR ANTREAN PASIEN ===\n")
        
        for pasien in list_antrean:         
            if 1 <= pasien.skor <= 10:  
                kategori = "Tidak Bahaya"
            elif 11 <= pasien.skor <= 20:
                kategori = "Ringan"
            elif 21 <= pasien.skor <= 30:
                kategori = "Menengah"
            elif 31 <= pasien.skor <= 40:
                kategori = "Gawat"
            elif 41 <= pasien.skor <= 50:
                kategori = "Gawat Darurat"
            else:
                # fallback jika ada skor di luar rentang 1-50
                kategori = "Skor Tidak Valid"

            print(
                f"ID: {pasien.id_pasien} | "
                f"Nama: {pasien.nama_pasien} | "
                f"Skor: {pasien.skor} | "
                f"Kategori kegawatan: {kategori}"
            )
            print("\n")

    elif pilihan_user == 3 : 
        cari_pasien()
    elif pilihan_user == 4 : 
        print("Selamat tinggolu")
    else : 
        print("Masukan anda tidak valid ")



