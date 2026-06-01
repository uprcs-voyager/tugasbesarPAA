import streamlit as st
import pandas as pd


# STRUKTUR DDATANYAA
class Pasien:
    def __init__(self, id_pasien, nama_pasien, jenis_kelamin, umur, gejala, skor):
        self.id_pasien = id_pasien
        self.nama_pasien = nama_pasien
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur
        self.gejala = gejala
        self.skor = skor
        self.kategori = self.tentukan_kategori()

    def tentukan_kategori(self):
        if 1 <= self.skor <= 10: return "Tidak Bahaya"
        elif 11 <= self.skor <= 20: return "Ringan"
        elif 21 <= self.skor <= 30: return "Menengah"
        elif 31 <= self.skor <= 40: return "Gawat"
        elif 41 <= self.skor <= 50: return "Gawat Darurat"
        return "Skor Tidak Valid"

# Inisialisasi Session State (Pengganti Database)
if 'list_antrean' not in st.session_state:
    st.session_state.list_antrean = [
        Pasien(1, "John Walker", "Lakik-lakik", 45, "Henti Jantung", 50),
        Pasien(2, "Arthur Morgan", "Lakik-lakik", 44, "tuberculosis", 45),
        Pasien(3, "john wick", "Lakik-lakik", 30, "kena peluru", 20),
        Pasien(4, "Luo Yi", "Perempuan", 23, "digigit serangga", 10),
        Pasien(5, "Layla", "Perempuan", 21, "kena peluru", 20),
    ]


# if 'list_antrean' not in st.session_state:
#     st.session_state.list_antrean = []

def data_ke_dataframe(data_list):
    #Konversi objek ke format tabel Pandassssssss 
    if not data_list: return pd.DataFrame()
    return pd.DataFrame([{
        "ID": p.id_pasien, 
        "Nama": p.nama_pasien, 
        "Lakie Lakie / Perempuan": p.jenis_kelamin.upper(), 
        "Umur (tahun)": p.umur, 
        "Gejala": p.gejala, 
        "Skor": p.skor, 
        "Kategori": p.kategori
    } for p in data_list])
















# 2. KODE  INTINYA INI JANGAN DIUBAH UBAH YA 

def insertionSort(antrean):
    n = len(antrean)
    for i in range(1, n):
        terbaru = antrean[i]
        j = i - 1
        while j >= 0 and antrean[j].skor < terbaru.skor:
            antrean[j + 1] = antrean[j]
            j -= 1
        antrean[j + 1] = terbaru
    return antrean

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















#UIIIIIIIIIIIIIIIIIIIIIIIIII
st.set_page_config(page_title="Sistem Antrean Adaptif", layout="wide")

st.sidebar.title("Navigasi Menu")
menu = st.sidebar.radio("Pilih Operasi:", ["Daftar Antrean", "Tambah Pasien", "Cari Kategori", "Cari Skor Eksak"])

# Pastikan data selalu terurut descending setiap ada interaksi
st.session_state.list_antrean = insertionSort(st.session_state.list_antrean)
data_utama = st.session_state.list_antrean

if menu == "Daftar Antrean":
    st.header(" Daftar Antrean Pasien sakiti")
    if not data_utama:
        st.info("Belum ada data pasien yak.")
    else:
        urutan = st.selectbox("Tampilkan Berdasarkan Urutan:", ["Descending (Kritis -> Ringan)", "Ascending (Ringan -> Kritis)"])
        
        if urutan == "Ascending (Ringan -> Kritis)":
            st.table(data_ke_dataframe(data_utama[::-1]).set_index("ID"))
        else:
            st.table(data_ke_dataframe(data_utama).set_index("ID"))
            
        st.caption(f"Total Pasien: {len(data_utama)}")









elif menu == "Tambah Pasien":
    st.header(" Tambah Data Pasien Baru")
    with st.form("form_tambah"):
        col1, col2 = st.columns(2)


        id_baru = col1.number_input("ID Pasien (masukan angka aja ya): ",min_value=1, step=1, format="%d")
        nama = col2.text_input("Nama Lengkap")
        jenis_kelamin = col1.selectbox("Jenis Kelamin", ["LAkie - Lakie", "Perempuan"])
        umur = col2.number_input("Umur (masukan angka saja ya)", min_value=1, step=1)
        gejala = st.text_input("Gejala Utama")
        skor = st.number_input("Skor Kegawatan (1-50)", min_value=1, max_value=50, step=1)
        
        submit = st.form_submit_button("Simpan Data")
        if submit:
            # cek apakah ID baru sama dengan ID yang sudah ada di sistem
            id_terpakai = any(pasien.id_pasien == id_baru for pasien in st.session_state.list_antrean)
            
            # cek apakah input issinya spasi doang atau ksong
            if not nama.strip() or not gejala.strip():
                st.error("Gagal ay, Nama Lengkap dan Gejala tidak boleh kosong atau hanya berisi spasi.")

            elif id_terpakai:
                st.error(f"Gagal! ID Pasien {id_baru} sudah terdaftar. Silakan gunakan ID lain.")
            else:
                pasien_baru = Pasien(id_baru, nama, jenis_kelamin, umur, gejala, skor)
                st.session_state.list_antrean.append(pasien_baru)
                # Sortir langsung habis ditambah
                st.session_state.list_antrean = insertionSort(st.session_state.list_antrean)
                st.success("Data berhasil ditambahkan dan antrean diurutkan ulang menggunakan algoritma insertion soert")





elif menu == "Cari Kategori":
    st.header(" Pencarian Berdasarkan Kategori")
    kategori_dict = {
        "Tidak Bahaya (1-10)": (1, 10),
        "Ringan (11-20)": (11, 20),
        "Menengah (21-30)": (21, 30),
        "Gawat (31-40)": (31, 40),
        "Gawat Darurat (41-50)": (41, 50)
    }
    pilihan = st.selectbox("Pilih Rentang Kategori:", list(kategori_dict.keys()))
    
    if st.button("Cari Kategori"):
        skor_min, skor_max = kategori_dict[pilihan]
        idx_kiri = cariBatasKiri(data_utama, skor_max)
        idx_kanan = cariBatasKanan(data_utama, skor_min)
        
        if idx_kiri == -1 or idx_kanan == -1 or idx_kiri > idx_kanan:
            st.warning(f"Tidak ada pasien dalam kategori {pilihan}.")
        else:
            hasil_data = data_utama[idx_kiri : idx_kanan + 1]
            st.success(f"Ditemukan {len(hasil_data)} pasien pada kategori {pilihan}")
            st.table(data_ke_dataframe(hasil_data).set_index("ID"))











elif menu == "Cari Skor Eksak":
    st.header("Pencarian Skor Spesifik (Binary Search)")
    target = st.number_input("Masukkan Skor yang dicari:", min_value=1, max_value=50, step=1)
    
    if st.button("Cari Skor"):
        hasil_idx = cariBerdasarkanSkor(data_utama, target)
        
        if hasil_idx == -1:
            st.warning(f"Tidak ditemukan pasien dengan skor tepat {target}.")
        else:
            batas_kiri = hasil_idx
            batas_kanan = hasil_idx
            
            while batas_kiri > 0 and data_utama[batas_kiri-1].skor == target:
                batas_kiri -= 1
            while batas_kanan < len(data_utama)-1 and data_utama[batas_kanan+1].skor == target:
                batas_kanan += 1
                
            hasil_data = data_utama[batas_kiri : batas_kanan + 1]
            st.success(f"Ditemukan {len(hasil_data)} pasien dengan skor {target}")
            st.table(data_ke_dataframe(hasil_data).set_index("ID"))