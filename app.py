# ==============================================================================
# BAGIAN 1: KONFIGURASI DAN DATABASE PENGGUNA
# ==============================================================================
import streamlit as st
from datetime import datetime, timedelta

DAFTAR_USER = {
    "dian": "QWERTY21ab", "icha": "udin99", "nissa": "tung22",
    "inggi": "udin33", "lisa": "tung66", "tamu": "123"
}

st.set_page_config(page_title="PINTAR MEDIA | AI Studio", layout="wide")

# ==============================================================================
# BAGIAN 2: SISTEM KEAMANAN & INISIALISASI DATA (SESSION STATE)
# ==============================================================================
def inisialisasi_keamanan():
    if 'sudah_login' not in st.session_state:
        st.session_state.sudah_login = False
    
    # INISIALISASI LACI PENYIMPANAN DATA (ANTI-HILANG)
    if 'data_produksi' not in st.session_state:
        st.session_state.data_produksi = {
            "jumlah_karakter": 2,
            "karakter": [ {"nama": "", "wear": "", "fisik": ""} for _ in range(4) ],
            "jumlah_adegan": 5,
            "adegan": {} # Tempat menyimpan naskah per adegan
        }

    params = st.query_params
    if "auth" in params and params["auth"] == "true":
        if not st.session_state.sudah_login:
            st.session_state.sudah_login = True
            st.session_state.user_aktif = params.get("user", "User")
            st.session_state.waktu_login = datetime.now()

def proses_login(user, pwd):
    if user in DAFTAR_USER and DAFTAR_USER[user] == pwd:
        st.session_state.sudah_login = True
        st.session_state.user_aktif = user
        st.session_state.waktu_login = datetime.now()
        st.query_params.update({"auth": "true", "user": user})
        st.rerun()
    else:
        st.error("Username atau Password salah.")

def tampilkan_halaman_login():
    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_m, col_r = st.columns([2, 1, 2]) 
    with col_m:
        try:
            st.image("PINTAR.png", use_container_width=True)
        except:
            st.markdown("<h2 style='text-align: center;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
        with st.form("login_station"):
            u = st.text_input("Username", placeholder="Username...", key="login_user").lower()
            p = st.text_input("Password", type="password", placeholder="Password...", key="login_pass")
            submit = st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True)
            if submit: proses_login(u, p)
        st.markdown("<p style='text-align: center; color: #484f58; font-size: 11px; margin-top: 15px;'>Secure Access - PINTAR MEDIA</p>", unsafe_allow_html=True)

def cek_autentikasi():
    if st.session_state.sudah_login:
        if 'waktu_login' in st.session_state:
            durasi = datetime.now() - st.session_state.waktu_login
            if durasi > timedelta(hours=10):
                proses_logout()
                return False
        return True
    return False

def proses_logout():
    st.session_state.clear() # Bersihkan semua memori saat logout
    st.query_params.clear()
    st.rerun()

# ==============================================================================
# BAGIAN 3: PENGATURAN TAMPILAN (CSS) - TOTAL BORDERLESS & STATIC
# ==============================================================================
def pasang_css_kustom():
    st.markdown("""
        <style>
        /* 1. DASAR APLIKASI & SCROLLBAR */
        .stApp { background-color: #0b0e14; color: #e0e0e0; }
        [data-testid="stSidebar"] { 
            background-color: #1a1c24 !important; 
            border-right: 1px solid rgba(29, 151, 108, 0.1) !important; 
        }
        
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #0e1117; }
        ::-webkit-scrollbar-thumb { background: #31333f; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #1d976c; }

        /* 2. FIXED HEADER (STATION & JAM) */
        [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) {
            position: fixed; top: 0; left: 310px; right: 0; z-index: 99999;
            background-color: #0e1117; padding: 10px 2rem; border-bottom: 2px solid #31333f;
        }
        @media (max-width: 768px) {
            [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) { left: 0; }
        }

        /* 3. HANYA TOMBOL GENERATE YANG HIJAU (PRIMARY) */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(to right, #1d976c, #11998e) !important;
            color: white !important; 
            border: none !important; 
            border-radius: 8px !important;
            padding: 10px 20px !important;
            margin-top: 15px !important;
            margin-bottom: 10px !important;
            font-weight: bold !important;
            font-size: 14px !important;
            width: 100%; 
            box-shadow: 0 4px 12px rgba(29, 151, 108, 0.2) !important;
        }

        /* 4. MODE TANPA GARIS (BORDERLESS) PADA SEMUA INPUT */
        .stTextArea textarea, 
        .stTextInput input, 
        div[data-testid="stNumberInput"], 
        div[data-baseweb="input"],
        div[data-baseweb="textarea"],
        [data-baseweb="base-input"] {
            border: none !important;
            box-shadow: none !important;
            outline: none !important;
            background-color: #0d1117 !important;
            border-radius: 10px !important;
            color: #ffffff !important;
        }
        
        .stTextArea textarea:focus, 
        .stTextInput input:focus, 
        div[data-testid="stNumberInput"]:focus-within,
        div[data-baseweb="input"]:focus-within,
        [data-baseweb="base-input"]:focus-within {
            border: none !important;
            box-shadow: none !important;
            outline: none !important;
        }

        /* 5. STAFF HEADER & LABEL */
        .staff-header-premium {
            background: rgba(29, 151, 108, 0.2) !important;
            border: 2px solid #1d976c !important;
            border-radius: 10px !important;
            padding: 15px 20px !important; margin-bottom: 25px !important;
            display: flex !important; align-items: center !important; gap: 12px !important;
        }
        .staff-header-premium b { color: #1d976c !important; font-size: 1.15em !important; }
        
        .small-label {
            color: #1d976c !important; font-size: 10px !important;
            font-weight: 800 !important; letter-spacing: 1px; text-transform: uppercase;
            margin-bottom: 5px !important; display: block;
        }

        /* 6. KOMPONEN LAIN - KETEBALAN STANDAR WARNA DEFAULT */
        .stExpander {
            /* 1px adalah ukuran standar yang paling pas, warna abu-abu gelap */
            border: 1px solid #30363d !important; 
            border-radius: 12px !important; 
            background-color: #161922 !important;
            margin-bottom: 10px !important;
        }
        
        .status-footer { font-size: 11px !important; color: #8b949e !important; font-family: monospace; }
        
        /* Garis pemisah (hr) tipis warna default */
        hr { 
            border: none !important;
            border-top: 1px solid #30363d !important; 
            opacity: 0.3 !important; /* Dibuat samar agar dashboard terlihat bersih */
            margin: 15px 0 !important;
        }

        /* 7. PENGATURAN INPUT HALAMAN LOGIN */
        .stForm div[data-baseweb="input"] {
            background-color: #1a1f26 !important;
            border: 1px solid #30363d !important;
        }
        .stForm input {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }
        .stForm label p {
            color: #e0e0e0 !important;
            font-weight: 600 !important;
            font-size: 14px !important;
        }

        /* 8. PROTEKSI LAYAR (PC ONLY) - DI POSISI PALING BAWAH */
        @media (max-width: 1024px) {
            [data-testid="stAppViewContainer"], [data-testid="stSidebar"], .main { display: none !important; }
            body::before {
                content: "⚠️ Gunakan PC untuk akses Pintar Media!";
                display: flex; justify-content: center; align-items: center;
                height: 100vh; width: 100vw; background: #0e1117; color: white;
                position: fixed; top: 0; left: 0; z-index: 9999; text-align: center; padding: 20px;
                font-family: sans-serif; font-weight: bold;
            }
        }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# BAGIAN 4: NAVIGASI SIDEBAR
# ==============================================================================
def tampilkan_navigasi_sidebar():
    with st.sidebar:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 11px; color: #8b949e; font-weight: bold; letter-spacing: 1px;'>MAIN WORKSPACE</p>", unsafe_allow_html=True)
        
        pilihan = st.radio(
            "MODUL",
            ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Kotak Durasi Film
        st.markdown("<p class='small-label'>🎬 DURASI FILM (ADEGAN)</p>", unsafe_allow_html=True)
        st.session_state.data_produksi["jumlah_adegan"] = st.number_input(
            "Jumlah Adegan", 1, 50, 
            value=st.session_state.data_produksi["jumlah_adegan"],
            label_visibility="collapsed"
        )
        
        # Jarak Logout
        st.markdown("<br>" * 6, unsafe_allow_html=True)
        
        if st.button("⚡KELUAR SISTEM", use_container_width=True):
            proses_logout()
        
        # Baris ini harus sejajar kembali dengan 'if' di atas
        user = st.session_state.get("user_aktif", "USER").upper()
        st.markdown(f'''
            <div style="border-top: 1px solid #30363d; padding-top: 15px; margin-top: 10px;">
                <p class="status-footer">
                    🛰️ STATION: {user}_SESSION<br>
                    🟢 STATUS: AKTIF
                </p>
            </div>
        ''', unsafe_allow_html=True)
        
    return pilihan

# ==============================================================================
# BAGIAN 5: MODUL-MODUL PENDUKUNG
# ==============================================================================
def tampilkan_ai_lab(): st.markdown("### 🧠 Pintar AI Lab"); st.info("Area riset prompt.")
def tampilkan_quick_prompt(): st.markdown("### ⚡ Quick Prompt")
def tampilkan_tugas_kerja(): st.markdown("### 📋 Tugas Kerja")
def tampilkan_kendali_tim(): st.markdown("### ⚡ Kendali Tim")

# ==============================================================================
# BAGIAN 6: MODUL UTAMA - RUANG PRODUKSI (FULL CONSISTENT SMALL-LABEL)
# ==============================================================================
def tampilkan_ruang_produksi():
    # 1. LOGIKA WAKTU & USER (WIB)
    sekarang = datetime.utcnow() + timedelta(hours=7) 
    hari_id = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    bulan_id = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    nama_hari = hari_id[sekarang.weekday()]
    tgl = sekarang.day
    nama_bulan = bulan_id[sekarang.month - 1]
    user_aktif = st.session_state.get("user_aktif", "User").upper()

    # 2. HEADER: TEKNIK 3 KOLOM (Agar lebar teks pas)
    c1, c_kosong, c2 = st.columns([2, 0.5, 0.9]) 
    
    with c1:
        st.markdown("# 🚀 RUANG PRODUKSI")
        st.markdown("<p style='color:#8b949e; margin-top:-20px;'>Hybrid Cinematic Engine v2.0</p>", unsafe_allow_html=True)
        
    with c2:
        st.markdown("<br>", unsafe_allow_html=True)
        # Menggunakan st.success murni
        st.success(f"🛰️ {nama_hari}, {tgl} {nama_bulan} | Staf: {user_aktif}")
    
    st.write("---")
    
    data = st.session_state.data_produksi

    # 1. IDENTITY LOCK
    with st.expander("🛡️ IDENTITY LOCK - Referensi Foto", expanded=True):
        # Kata "Jumlah Karakter" sekarang tersembunyi
        data["jumlah_karakter"] = st.number_input("Jumlah Karakter", 1, 4, data["jumlah_karakter"], label_visibility="collapsed")
        
        cols_char = st.columns(data["jumlah_karakter"])
        for i in range(data["jumlah_karakter"]):
            with cols_char[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                data["karakter"][i]["nama"] = st.text_input("Nama", value=data["karakter"][i]["nama"], key=f"char_nama_{i}", placeholder="Nama...", label_visibility="collapsed")
                data["karakter"][i]["wear"] = st.text_input("Pakaian", value=data["karakter"][i]["wear"], key=f"char_wear_{i}", placeholder="Pakaian...", label_visibility="collapsed")
                data["karakter"][i]["fisik"] = st.text_area("Ciri Fisik", value=data["karakter"][i]["fisik"], key=f"char_fix_{i}", height=80, placeholder="Fisik...", label_visibility="collapsed")

    st.markdown('<div style="margin-bottom: -15px;"></div>', unsafe_allow_html=True)    
    # 2. GENERASI INPUT ADEGAN SECARA DINAMIS
    for s in range(data["jumlah_adegan"]):
        scene_id = s + 1
        
        # Inisialisasi struktur data adegan jika belum ada
        if scene_id not in data["adegan"]:
            data["adegan"][scene_id] = {
                "aksi": "", "style": "Realistis", "light": "Studio", 
                "arah": "Normal", "shot": "Setengah Badan", 
                "ratio": "16:9", "cam": "Static", "loc": "", 
                "dialogs": [""]*4
            }

        with st.expander(f"🎬 ADEGAN {scene_id}", expanded=(scene_id == 1)):
            col_text, col_set = st.columns([1.5, 1])
            
            with col_text:
                # KEMBALI KE SMALL-LABEL SESUAI REQUEST
                st.markdown('<p class="small-label">📸 NASKAH VISUAL & AKSI</p>', unsafe_allow_html=True)
                data["adegan"][scene_id]["aksi"] = st.text_area(f"Aksi_{scene_id}", value=data["adegan"][scene_id]["aksi"], height=345, key=f"act_{scene_id}", label_visibility="collapsed", placeholder="Tulis aksi visual di sini...")
            
            with col_set:
                sub1, sub2 = st.columns(2)
                with sub1:
                    st.markdown('<p class="small-label">✨ STYLE</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["style"] = st.selectbox(f"S_{scene_id}", ["Realistis", "Pixar 3D", "Glossy Asphalt", "Naruto Anime"], index=0, key=f"mood_{scene_id}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">💡 LIGHTING</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["light"] = st.selectbox(f"L_{scene_id}", ["Golden Hour", "Studio", "Natural"], key=f"light_{scene_id}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">📐 ARAH KAMERA</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["arah"] = st.selectbox(f"A_{scene_id}", ["Normal", "Sudut Tinggi", "Samping", "Berhadapan"], key=f"arah_{scene_id}", label_visibility="collapsed")

                with sub2:
                    st.markdown('<p class="small-label">🔍 UKURAN GAMBAR</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["shot"] = st.selectbox(f"Sh_{scene_id}", ["Dekat Wajah", "Setengah Badan", "Seluruh Badan", "Pemandangan Luas", "Drone Shot"], key=f"shot_{scene_id}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">📺 ASPECT RATIO</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["ratio"] = st.selectbox(f"R_{scene_id}", ["16:9", "9:16", "1:1"], key=f"ratio_{scene_id}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">🎥 GERAKAN</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["cam"] = st.selectbox(f"C_{scene_id}", ["Static", "Zoom In", "Tracking"], key=f"cam_{scene_id}", label_visibility="collapsed")
                
                st.markdown('<p class="small-label" style="margin-top:15px;">📍 LOKASI</p>', unsafe_allow_html=True)
                data["adegan"][scene_id]["loc"] = st.text_input(f"Loc_{scene_id}", value=data["adegan"][scene_id]["loc"], key=f"loc_{scene_id}", label_visibility="collapsed", placeholder="Lokasi adegan...")

            # Baris Dialog Sejajar Horizontal
            cols_d = st.columns(data["jumlah_karakter"])
            for i in range(data["jumlah_karakter"]):
                with cols_d[i]:
                    char_name = data["karakter"][i]["nama"] if data["karakter"][i]["nama"] else f"Karakter {i+1}"
                    st.markdown(f'<p class="small-label">Dialog {char_name}</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["dialogs"][i] = st.text_input(f"D_{scene_id}_{i}", value=data["adegan"][scene_id]["dialogs"][i], key=f"d_{scene_id}_{i}", label_visibility="collapsed", placeholder="Dialog...")

    # 3. GLOBAL COMPILER LOGIC (DENGAN NAMA USER DINAMIS)
    if st.button("🚀 GENERATE ALL SCENES PROMPT", use_container_width=True, type="primary"):
        
        adegan_terisi = [s_id for s_id, isi in data["adegan"].items() if isi["aksi"].strip() != ""]
        
        if not adegan_terisi:
            st.error("⚠️ Gagal: Kamu belum mengisi 'NASKAH VISUAL & AKSI' di adegan manapun.")
        else:
            # Ganti baris "---" dengan spasi kecil jika ingin lebih rapat
            st.markdown('<div style="margin-top: -10px;"></div>', unsafe_allow_html=True)
            
            # MENGAMBIL NAMA USER AKTIF UNTUK JUDUL
            user_nama = st.session_state.get("user_aktif", "User").capitalize()
            st.markdown(f"## 🎬 Hasil Prompt: {user_nama} ❤️")
            
            char_ids = " AND ".join([f"[[ CHARACTER_{c['nama'].upper()}: \"{c['fisik']}\" maintain 100% exact facial features. ]]" for c in data["karakter"] if c['nama']])
            char_profiles = ", ".join([f"{c['nama']} (pakaian: {c['wear']})" for c in data["karakter"] if c['nama']])

            for scene_id in adegan_terisi:
                sc = data["adegan"][scene_id]
                
                # MEMBUAT BLOK HASIL PER ADEGAN YANG RAPI
                with st.expander(f"⌛ PROSES | ADEGAN {scene_id}", expanded=True):
                    
                    all_d = " | ".join([f"{data['karakter'][i]['nama']}: '{sc['dialogs'][i]}'" 
                                        for i in range(data["jumlah_karakter"]) 
                                        if data['karakter'][i]['nama'] and sc['dialogs'][i]])
                    
                    img_p = f"CHARACTER DATA: {char_ids}\nVISUAL ACTION: {sc['aksi']}\nENVIRONMENT: {sc['loc']}\nTECHNICAL: {sc['style']}, {sc['light']}, {sc['shot']} --ar {sc['ratio']}"
                    vid_p = f"Profiles: {char_profiles}\nScene: {sc['aksi']} at {sc['loc']}\nActing: {all_d}\nTech: {sc['style']}, {sc['shot']}, {sc['cam']} at {sc['arah']}."

                    col_img, col_vid = st.columns(2)
                    
                    with col_img:
                        st.markdown('<p class="small-label">📷 PROMPT GAMBAR</p>', unsafe_allow_html=True)
                        st.code(img_p, language="text")
                    
                    with col_vid:
                        st.markdown('<p class="small-label">🎥 PROMPT VIDEO</p>', unsafe_allow_html=True)
                        st.code(vid_p, language="text")
                
                # Ganti <br> dengan margin negatif jika ingin antar kotak hasil lebih rapat
                st.markdown('<div style="margin-bottom: -15px;"></div>', unsafe_allow_html=True)
                
# ==============================================================================
# BAGIAN 7: PENGENDALI UTAMA
# ==============================================================================
def utama():
    inisialisasi_keamanan()
    pasang_css_kustom()
    if not cek_autentikasi():
        tampilkan_halaman_login()
    else:
        menu = tampilkan_navigasi_sidebar()
        if menu == "🚀 RUANG PRODUKSI": tampilkan_ruang_produksi()
        elif menu == "🧠 PINTAR AI LAB": tampilkan_ai_lab()
        elif menu == "⚡ QUICK PROMPT": tampilkan_quick_prompt()
        elif menu == "📋 TUGAS KERJA": tampilkan_tugas_kerja()
        elif menu == "⚡ KENDALI TIM": tampilkan_kendali_tim()

if __name__ == "__main__":
    utama()
