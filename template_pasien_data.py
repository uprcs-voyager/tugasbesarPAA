from data_storage_template import Pasien 

list_antrean = [
    # Kategori: Gawat Darurat (Skor 41 - 50)
    Pasien("P001", "Budi Santoso", "L", 45, "Henti Jantung", 50),
    Pasien("P002", "Siti Aminah", "P", 30, "Trauma Kepala Berat", 48),
    Pasien("P003", "Andi Wijaya", "L", 62, "Stroke Akut", 45),
    Pasien("P004", "Rini Lestari", "P", 25, "Pendarahan Hebat", 42),
    
    # Kategori: Gawat (Skor 31 - 40)
    Pasien("P005", "Eko Prasetyo", "L", 38, "Asma Akut (Sesak Berat)", 40),
    Pasien("P006", "Dewi Rahmawati", "P", 50, "Patah Tulang Terbuka", 38),
    Pasien("P007", "Gani Nugroho", "L", 19, "Dehidrasi Berat", 35),
    Pasien("P008", "Mega Utami", "P", 28, "Luka Bakar Derajat 2", 32),
    
    # Kategori: Menengah (Skor 21 - 30)
    Pasien("P009", "Hendra Wijaya", "L", 41, "Krisis Hipertensi", 30),
    Pasien("P010", "Nina Kartika", "P", 22, "Nyeri Akut Usus Buntu", 27),
    Pasien("P011", "Fajar Ramadhan", "L", 15, "Demam Berdarah (DHF)", 25),
    Pasien("P012", "Tari Handayani", "P", 65, "Vertigo Berat", 22),
    
    # Kategori: Ringan (Skor 11 - 20)
    Pasien("P013", "Joni Iskandar", "L", 34, "Asam Lambung Akut (GERD)", 20),
    Pasien("P014", "Maya Sopha", "P", 47, "Migrain Kronis", 18),
    Pasien("P015", "Rizky Fauzi", "L", 12, "Tonsilitis (Amandel)", 15),
    Pasien("P016", "Sinta Dewi", "P", 55, "Nyeri Sendi (Gout)", 12),
    
    # Kategori: Tidak Bahaya (Skor 1 - 10)
    Pasien("P017", "Anton Budiman", "L", 29, "Influenza dan Batuk", 10),
    Pasien("P018", "Cici Paramitha", "P", 8, "Demam Ringan", 8),
    Pasien("P019", "Bagus Permana", "L", 24, "Luka Gores Ringan", 5),
    Pasien("P020", "Putri Amelia", "P", 17, "Alergi Kulit (Gatal)", 2)
]