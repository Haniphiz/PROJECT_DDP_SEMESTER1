import streamlit as st
import pandas as pd 
from PIL import Image
from Kalkulator import Person

st.set_page_config(layout="wide")

st.title(':green[K]ALORI:green[K]U')



with st.sidebar:
    st.title(':green[K]ALORI:green[K]U')
    
    st.header("Pilihan hitung kalori")
    data_option = st.radio("Menu :", ["Informasi","Kalkulator","My Food Portion Ruler", "Tabel Kalori"])


with st.container():


    if data_option == "Informasi":
        st.header('Apa itu kalori? ')
        st.write('''Kalori adalah jumlah energi yang didapatkan dari makanan dan minuman. Ini juga merupakan jumlah energi yang dibakar tubuh melalui aktivitas sehari-hari. Artinya, kalori adalah energi yang dibutuhkan tubuh agar bisa beraktivitas dan menjalankan fungsinya dengan baik. Pada saat melihat label nutrisi pada kemasan makanan atau minuman, Anda mungkin melihat istilah “kkal”.''')
        st.header('Fungsi Kalori ')
        ('''Kalori yang diperoleh dari makanan dan minuman akan diubah menjadi energi melalui proses metabolisme. Energi tersebut akan digunakan untuk mendukung kinerja dan fungsi berbagai \organ tubuh. Sisa kalori yang tidak diubah menjadi energi akan disimpan dalam tubuh sebagai lemak. ''')

        st.header('Metode Penghitungan Kebutuhan Kalori tubuh')
        st.markdown('''**BMR** (Basal Metabolic Rate)
        BMR adalah jumlah kalori yang dibutuhkan untuk melakukan aktivitas minimum seperti bernafas. Kalkulator ini menghitung BMR menggunakan rumus **Mifflin St. Jeor** sebagai berikut.''')
        st.markdown("""
        <style>
        .center-box {
            text-align: center;
            width: 350px;
            height:70px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            border: 2px solid #ccc;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="center-box">Pria = 10 x BB + 6.25 x TB - 5 x U + 5 <br/>Wanita = 10 x BB + 6.25 x TB - 5 x U - 161</div>', unsafe_allow_html=True)

        st.header('Kebutuhan Kalori Harian (TDEE)')
        st.markdown('''**TDEE** (Total Daily Energy Expenditure) adalah total kalori yang anda butuhkan dalam melakukan aktivitas sehari-hari. Mifflin St. Jeor mengelompokkan TDEE ke dalam beberapa kategori sebagai berikut.''')
        
        st.markdown("""
        <ul>
        <li>Minimal bergerak atau kerja kantoran, pengali TDEE = 1.2</li>
        <li>Aktivitas ringan, olahraga 1-2 kali/minggu, pengali TDEE = 1.375</li>
        <li>Aktivitas sedang, olahraga 3-5 kali/minggu, pengali TDEE = 1.55</li>
        <li>Aktivitas sedang, olahraga 3-5 kali/minggu, pengali TDEE = 1.55</li>
        <li>Aktivitas berat, olahraga 6-7 kali/minggu, pengali TDEE = 1.725</li>
        <li>Aktivitas ekstrim, olahraga 2 kali sehari atau lebih, pengali TDEE = 1.9</li>
        </ul>
        """, unsafe_allow_html=True)



    

#   AKHIR INFORMASI


    if data_option == "Kalkulator":

        st.header("Cek kebutuhan kalori harianmu!")

        # Input 
        usia = st.number_input("Usia", min_value=0, max_value=120, value=0)
        tinggi_badan = st.number_input("Tinggi badan (cm)", min_value=0, max_value=250, value=0)
        berat_badan = st.number_input("Berat badan (kg)", min_value=0, max_value=300, value=0)
        jenis_kelamin = st.selectbox('Pilih jenis kelamin', ('Pria', 'Wanita'))
        aktivitas = st.selectbox("Aktivitas Harian", [
            "Santai/Suka Rebahan",
            "Aktivitas Ringan,Olahraga 1-2 kali/seminggu",
            "Aktivitas Sedang,Olahraga 3-5 kali/seminggu",
            "Aktivitas Berat,Olahraga 6-7 kali/seminggu",
            "Pekerja fisik,Olahraga Setiap Hari"
        ])
        tujuan = st.selectbox("Pencapaian", [
            "menurunkan berat badan",
            "menjaga berat badan",
            "meningkatkan berat badan"
        ])

        
        if st.button("Hitung Kalori"):
            
            kalkulator = Person(
                usia,
                tinggi_badan,
                berat_badan,
                jenis_kelamin,
                aktivitas,
                tujuan
            )

            # Menghitung BMR dan kalori
            bmr, kalori = kalkulator.hitung_kalori()

            #hasil kalkulasi BMR dan total kalori
            st.success(f"Kebutuhan kalori /harian kamu sekarang adalah :orange[{kalori:.0f}].")
            st.warning(f"Kalori BMR kamu adalah :blue[{bmr:.0f}]")
            # Pesan motivasi 
            if tujuan == "menurunkan berat badan":
                st.info("Tahan godaan kecil hari ini, karena hasil besarnya akan membuatmu bangga nanti!")
            elif tujuan == "menjaga berat badan":
                st.info("Menjaga berat badan adalah perjalanan jangka panjang, tapi kamu sudah membuktikan bahwa kamu punya kekuatan untuk melakukannya.")
            else:
                st.info("Proses ini membutuhkan kesabaran, tapi setiap gigitan sehat yang kamu pilih adalah langkah kecil menuju tujuanmu. Jangan menyerah!")




# FOOD PORTION
    if data_option == "My Food Portion Ruler":
        st.title('MY FOOD P0RTI0N RULER')

        
        col1, col2 = st.columns(2)
        
        with col1:
            makananpokok = st.selectbox('Pilih makanan pokok', [
                'Tidak Memilih Satupun', 'Nasi', 'Roti Tawar', 'Jagung', 'Kentang', 'Singkong'
            ])
        
        with col2:
            beratpokok = st.number_input("Makanan pokok (g)", min_value=0, step=1)

        #pilihan makanan pokok
        info_placeholder = st.empty()
        if makananpokok == "Nasi":
            info_placeholder.info("Satu centong nasi biasanya setara dengan 100 gram nasi.")
        elif makananpokok == "Roti Tawar":
            info_placeholder.info("Satu lembar roti biasanya memiliki berat 50 gram.")
        elif makananpokok == "Jagung":
            info_placeholder.info("Satu bonggol jagung ukuran sedang memiliki berat bersih berkisar 100 gram.")
        elif makananpokok == "Kentang":
            info_placeholder.info("Satu kentang berukuran sedang memiliki berat berkisar 100 gram.")
        elif makananpokok == "Singkong":
            info_placeholder.info("Satu singkong berukuran sedang memiliki berat berkisar 100 gram.")
        else:
            info_placeholder.info("Tidak ada makanan pokok yang dipilih.")

        # makanan lauk dan berat lauk
        col1, col2 = st.columns(2)
        
        with col1:
            makananlauk = st.selectbox('Pilih makanan lauk', [
                'Tidak Memilih Satupun', 'Ikan Bandeng Goreng', 'Ayam Goreng', 'Telur Dadar'
            ])
        
        with col2:
            beratlauk = st.number_input("Makanan lauk (g)", min_value=0, step=1)
        
        info_placeholder = st.empty()
        if makananlauk == "Ikan Bandeng Goreng":
            info_placeholder.info("Satu ikan berukuran sedang memiliki berat berkisar 40 gram.")
        elif makananlauk == "Ayam Goreng":
            info_placeholder.info("Ayam ukuran 1/4 memiliki berat berkisar 100 gram.")
        elif makananlauk == "Telur Dadar":
            info_placeholder.info("Satu telur ukuran sedang memiliki berat berkisar 60 gram.")
        else:
            info_placeholder.info("Tidak ada makanan lauk yang dipilih.")

        # makanan pendamping
        col1, col2 = st.columns(2)
        
        with col1:
            makananpendamping = st.selectbox('Pilih makanan samping', [
                'Tidak Memilih Satupun', 'Tahu Goreng', 'Tempe Goreng', 'Bakwan'
            ])
        
        with col2:
            beratsamping = st.number_input("Makanan samping (g)", min_value=0, step=1)
        
        info_placeholder = st.empty()
        if makananpendamping == "Tahu Goreng":
            info_placeholder.info("Satu tahu ukuran sedang memiliki berat berkisar 50 gram.")
        elif makananpendamping == "Tempe Goreng":
            info_placeholder.info("Tempe goreng potongan sedang memiliki berat berkisar 50 gram.")
        elif makananpendamping == "Bakwan":
            info_placeholder.info("Satu bakwan ukuran sedang memiliki berat berkisar 60 gram.")
        else:
            info_placeholder.info("Tidak ada makanan pendamping yang dipilih.")

        # makanan sayuran
        col1, col2 = st.columns(2)
        
        with col1:
            makanansayuran = st.selectbox('Pilih makanan sayuran', [
                'Tidak Memilih Satupun', 'Bayam', 'Tumis Kangkung', 'Sayur Asem'
            ])
        
        with col2:
            beratsayuran = st.number_input("Makanan sayuran (g)", min_value=0, step=1)
        
        info_placeholder = st.empty()
        if makanansayuran == "Bayam":
            info_placeholder.info("Satu mangkuk bayam memiliki berat berkisar 90 gram.")
        elif makanansayuran == "Tumis Kangkung":
            info_placeholder.info("Satu ikat kangkung yang ditumis memiliki berat berkisar 100 gram.")
        elif makanansayuran == "Sayur Asem":
            info_placeholder.info("Satu mangkuk sayur asem memiliki berat berkisar 90 gram.")
        else:
            info_placeholder.info("Tidak ada makanan sayuran yang dipilih.")

        #buah-buahan
        col1, col2 = st.columns(2)
        
        with col1:
            buahbuahsehat = st.selectbox('Pilih buah', [
                'Tidak Memilih Satupun', 'Apel', 'Pisang', 'Semangka', 'Pepaya'
            ])
        
        with col2:
            beratbuahbuahan = st.number_input("Buah (g)", min_value=0, step=1)
        
        info_placeholder = st.empty()
        if buahbuahsehat == "Apel":
            info_placeholder.info("Satu buah apel memiliki berat berkisar 150 gram.")
        elif buahbuahsehat == "Pisang":
            info_placeholder.info("Satu buah pisang ukuran sedang memiliki berat berkisar 110 gram.")
        elif buahbuahsehat == "Semangka":
            info_placeholder.info("Satu potong semangka memiliki berat berkisar 65 gram.")
        elif buahbuahsehat == "Pepaya":
            info_placeholder.info("Satu potong pepaya memiliki berat berkisar 100 gram.")
        else:
            info_placeholder.info("Tidak ada buah yang dipilih.")

    # Perhitungan kalori
        if st.button('Hitung Kalori'):
            def kalori_pokok(makanan, berat):
                if makanan == "Nasi":
                    return 1.29 * berat
                elif makanan == "Roti Tawar":
                    return 2.7 * berat
                elif makanan == "Jagung":
                    return 0.93 * berat
                elif makanan == "Kentang":
                    return 0.87 * berat
                elif makanan == "Singkong":
                    return 1.46 * berat
                else:
                    return 0

            def kalori_lauk(makanan, berat):
                if makanan == "Ikan Bandeng Goreng":
                    return 2.33 * berat
                elif makanan == "Ayam Goreng":
                    return 2.60 * berat
                elif makanan == "Telur Dadar":
                    return 1.27 * berat
                else:
                    return 0

            def kalori_pendamping(makanan, berat):
                if makanan == "Tahu Goreng":
                    return 0.78 * berat
                elif makanan == "Tempe Goreng":
                    return 1.93 * berat
                elif makanan == "Bakwan":
                    return 2.28 * berat
                else:
                    return 0

            def kalori_sayuran(makanan, berat):
                if makanan == "Bayam":
                    return 0.36 * berat
                elif makanan == "Tumis Kangkung":
                    return 0.98 * berat
                elif makanan == "Sayur Asem":
                    return 0.33 * berat
                else:
                    return 0

            def kalori_buah(makanan, berat):
                if makanan == "Apel":
                    return 0.52 * berat
                elif makanan == "Pisang":
                    return 0.89 * berat
                elif makanan == "Semangka":
                    return 0.30 * berat
                elif makanan == "Pepaya":
                    return 0.39 * berat
                else:
                    return 0

            total_kalori = (
                kalori_pokok(makananpokok, beratpokok) +
                kalori_lauk(makananlauk, beratlauk) +
                kalori_pendamping(makananpendamping, beratsamping) +
                kalori_sayuran(makanansayuran, beratsayuran) +
                kalori_buah(buahbuahsehat, beratbuahbuahan)
            )

            st.success(f'Total kalori dalam piring ini adalah :orange[{total_kalori:.0f}] kalori')  

            # Detail kalori
            detail_makanan = [
                (makananpokok, kalori_pokok(makananpokok, beratpokok)),
                (makananlauk, kalori_lauk(makananlauk, beratlauk)),
                (makananpendamping, kalori_pendamping(makananpendamping, beratsamping)),
                (makanansayuran, kalori_sayuran(makanansayuran, beratsayuran)),
                (buahbuahsehat, kalori_buah(buahbuahsehat, beratbuahbuahan))
            ]
            
            st.subheader("Detail Kalori")
            for makanan, kalori in detail_makanan:
                if makanan != "Tidak Memilih Satupun":
                    st.write(f"{makanan}: {kalori:.0f} kalori")

            def info_makanan(makanan, info_dict):
                if makanan in info_dict:
                    return info_dict[makanan]
                return "Tidak ada informasi."


# TABEL
    if data_option == "Tabel Kalori":
# tabel makanan
        st.header('Jumlah kalori dalam makanan')
        data = {
        'Makanan Pokok': ['Nasi putih', 'Nasi merah', 'Kentang rebus', 'Ubi jalar', 'Singkong', 'Roti putih', 'Roti gandum', 'Mi goreng instan'],
        'Satuan': ['100 gram', '100 gram', '100 gram', '100 gram', '100 gram', '1 iris', '1 iris', '80 gram'],
        'Energi': ['175 kalori', '110 kalori', '87 kkal', '86 kkal', '160 kkal', '66 kkal', '67 kkal', '350 kkal']
    }
        
        df = pd.DataFrame(data)
        df = df.reset_index(drop=True)
        df.index = df.index + 1
        df.index.name = 'No'
        st.table(df)

# tabel LAUK
        st.header('Jumlah kalori dalam Lauk')
        data = {
            'Nama makanan': [
                'Dada ayam goreng (dengan kulit)', 'Dada ayam goreng (tanpa kulit)', 'Bebek goreng',
                'Ikan kembung', 'Ikan lele goreng', 'Ikan salmon panggang', 'Udang goreng tepung',
                'Bakso sapi', 'Chicken nugget', 'Telur orak arik', 'Telur rebus', 'Telur dadar',
                'Telur ceplok', 'Tempe goreng', 'Tempe bacem', 'Tahu bacem', 'Tahu isi',
                'Tahu bakso', 'Tahu sumedang', 'Tumis labu siam', 'Tumis kangkung',
                'Tumis kacang panjang dan tempe', 'Sambal goreng kentang', 'Perkedel kentang'
            ],
            'Satuan': [
                '100 gram', '100 gram', '100 gram', '100 gram', '100 gram', '100 gram', '100 gram',
                '100 gram', '100 gram', '2 btr telur sedang', '1 btr sedang', '1 btr besar',
                '1 btr besar', '1 porsi', '1 porsi', '1 porsi', '1 porsi', '1 porsi', '1 porsi',
                '100 gram', '85 gram', '110 gram', '100 gram', '75 gram'
            ],
            'Energi': [
                '216 kkal', '184 kkal', '286 kkal', '167 kkal', '105 kkal', '171 kkal', '150 kkal',
                '202 kkal', '297 kkal', '199 kkal', '68 kkal', '93 kkal', '92 kkal', '118 kkal',
                '157 kkal', '119 kkal', '124 kkal', '119 kkal', '113 kkal', '106 kkal', '155 kkal',
                '102 kkal', '107 kkal', '117 kkal'
            ]
        }

        df = pd.DataFrame(data)
        df = df.reset_index(drop=True)
        df.index = df.index + 1
        df.index.name = 'No'
        st.table(df)

# Tabel Buah Buahan
        st.header('Kalori dalam Buah-Buahan')
        data = {
            'Nama buah': [
                'Apel', 'Pisang', 'Jambu biji', 'Jambu air', 'Semangka', 'Melon', 'Alpukat',
                'Anggur', 'Jeruk', 'Salak', 'Manggis', 'Mangga manalagi', 'Buah naga', 'Pepaya'
            ],
            'Satuan': [
                '1 buah sedang', '1 buah sedang', '1 buah', '1 buah', '100 gram', '100 gram',
                '100 gram', '100 gram', '1 buah', '1 buah', '100 gram', '1 buah', '1 buah sedang', '100 gram'
            ],
            'Energi': [
                '72 kkal', '105 kkal', '37 kkal', '55 kkal', '30 kkal', '34 kkal', '322 kkal',
                '69 kkal', '62 kkal', '8 kalori', '73 kkal', '72 kkal', '50 kkal', '39 kkal'
            ]
        }

        df = pd.DataFrame(data)
        df = df.reset_index(drop=True)
        df.index = df.index + 1
        df.index.name = 'No'
        st.table(df)

# Tabel Sayur sayuran
        st.header('Kalori dalam Sayur Sayuran')
        data = {
            'Nama sayuran': [
                'Bayam', 'Toge', 'Brokoli', 'Cabai', 'Mentimun', 'Zuchini', 'Kale',
                'Buncis', 'Kacang Kapri', 'Bawang bombai', 'Terung', 'Bunga kol', 'Buncis merah', 'Wortel','Asparagus'
            ],
            'Satuan': [
                '100 gram','100 gram', '100 gram','100 gram','100 gram', '100 gram',
                '100 gram', '100 gram','100 gram', '100 gram', '100 gram', '100 gram', '100 gram', '100 gram','100 gram'
            ],
            'Energi': [
                '29 kkal', '42 kkal', '40 kkal', '23 kkal', '16 kkal', '20 kkal', '39 kkal',
                '31 kkal', '38 kkal', '40 kalori', '20 kkal', '43 kkal', '36 kkal', '42 kkal','28 kkal'
            ]
        }

        df = pd.DataFrame(data)
        df = df.reset_index(drop=True)
        df.index = df.index + 1
        df.index.name = 'No'
        st.table(df)

