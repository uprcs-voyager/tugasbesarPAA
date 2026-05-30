# Kelompok 4 
# Judul Project : Adaftif Waiting line 
adaptif waiting line adalah sebuah program antrian yang digunakan pada lingkungan pelayanan kesehatan seperti puskesmas. Program ini bertujuan untuk mendemonstrasikan dua algoritma decrease and qonquer yaitu Binary Search & Insertion Sort 

### Program Input 
- ID pasien 
- Nama Pasien 
- Jenis Kelamin
- Umur Pasien
- Sakit yang diderita
- Skor Kegawatan

### Kategori kegawatan 
Kategori kegawatan adalah sistem yang digunakan untuk mengukur seberapa gawat kondisi pasien. Skor kegawatan dan kategori kegawatan dapat dilihat pada table dibawah ini 

| Skor kegawatan | Kategori Kegawatan |  
| --- | --- |
| 1-10 | Tidak Bahaya | 
| 11-20 | Ringan | 
| 21-30 | Menengah | 
| 31-40 | Gawat | 
| 41-50 | Gawat Darurat | 



### Pemanfaatan Insertion Sort 
Algoritma Insertion Sort digunakan saat petugas memasukan data pasien baru agar data yang disimpan tetap terurut. 
Secara default Sistem akan mengurutkan pasien yang memiliki skor kegawatan tertinggi terlebih dahulu ke pasien yang memiliki skor kegawatan terendah.

#### Pemanfaatan Algoritma Binary Search 
Algoritma ini digunakan pada fitur pencarian di program kami. Saat pengguna memilih fitur pencarian, maka program akan memberikan 2 pilihan pencarian yaitu cari berdasarkan kategori dan cari berdasarkan skor eksak.
1. Pencarian berdasarkan Kategori
   Saat pengguna memilih pilihan ini, program akan menampilkan kategori kegawatan yang ada, lalu pengguna dapat memilih kategori kegawatan yang ingin dicari. Setelah pengguna memilih kategori kegawatn yang ingin dicari, sistem akan menampilkan semua pasien yang ada di dalam kategori tersebut. 
###
2. Pencarian Berdasarkan skor eksak
   Jika pengguna memilih mode ini, sistem akan meminta pengguna untuk memasukan input berupa skor kegawatan yang ingin dicari petugas. Setelah petugas memasukan skor yang ingin dicari, sistem akan menampilkan semua pasien yang memiliki skor tersebut
