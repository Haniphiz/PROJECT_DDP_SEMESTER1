# File: kalkulator_kalori.py

class Person:
    def __init__(self, usia, tinggi_badan, berat_badan, jenis_kelamin, aktivitas, tujuan):
        self.usia = usia
        self.tinggi_badan = tinggi_badan
        self.berat_badan = berat_badan
        self.jenis_kelamin = jenis_kelamin
        self.aktivitas = aktivitas
        self.tujuan = tujuan

    def hitung_kalori(self):
        # Menghitung Basal Metabolic Rate (BMR)
        if self.jenis_kelamin == "Pria":
            bmr = 10 * self.berat_badan + 6.25 * self.tinggi_badan - 5 * self.usia + 5
        else:
            bmr = 10 * self.berat_badan + 6.25 * self.tinggi_badan - 5 * self.usia - 161

        # Faktor aktivitas harian (TDEE)
        aktivitas_tdee = {
            "Santai/Suka Rebahan": 1.2,
            "Aktivitas Ringan,Olahraga 1-2 kali/seminggu": 1.375,
            "Aktivitas Sedang,Olahraga 3-5 kali/seminggu": 1.55,
            "Aktivitas Berat,Olahraga 6-7 kali/seminggu": 1.725,
            "Pekerja fisik,Olahraga Setiap Hari": 1.9
        }

        # Ambil nilai TDEE sesuai aktivitas pengguna
        tdee = aktivitas_tdee[self.aktivitas]
        total_kalori = bmr * tdee

        # Penyesuaian kalori berdasarkan tujuan
        if self.tujuan == "menurunkan berat badan":
            total_kalori -= 500
        elif self.tujuan == "meningkatkan berat badan":
            total_kalori += 500

        return bmr, total_kalori  # Kembalikan BMR dan total kalori
