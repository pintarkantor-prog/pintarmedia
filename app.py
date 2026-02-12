# ==============================================================================
# BAGIAN 1: KONFIGURASI DAN DATABASE PENGGUNA
# ==============================================================================
import streamlit as st
from datetime import datetime, timedelta
import json
import pandas as pd
import gspread # Menambahkan mesin gspread
from google.oauth2.service_account import Credentials # Menambahkan sistem kunci
from streamlit_gsheets import GSheetsConnection # Tetap biarkan jika masih dipakai

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
    
    # LACI PENYIMPANAN DATA (TIDAK DIUBAH)
    if 'data_produksi' not in st.session_state:
        st.session_state.data_produksi = {
            "jumlah_karakter": 2,
            "karakter": [ {"nama": "", "wear": "", "fisik": ""} for _ in range(4) ],
            "jumlah_adegan": 5,
            "adegan": {} 
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
    st.session_state.clear()
    st.query_params.clear()
    st.rerun()

# FUNGSI BACKUP (Fokus GSheet lewat Secrets)
def simpan_ke_gsheet():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        # Pakai st.secrets (tidak pakai file kunci.json)
        creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
        client = gspread.authorize(creds)
        
        url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
        sheet = client.open_by_url(url_gsheet).sheet1
        
        user = st.session_state.get("user_aktif", "Staff")
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data_json = json.dumps(st.session_state.data_produksi)
        
        sheet.append_row([user, waktu, data_json])
        st.toast("🚀 Berhasil disimpan ke Cloud GSheet!", icon="☁️")
    except Exception as e:
        st.error(f"Gagal Simpan Cloud: {e}")

def muat_dari_gsheet():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
        client = gspread.authorize(creds)
        
        url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
        sheet = client.open_by_url(url_gsheet).sheet1
        
        semua_data = sheet.get_all_records()
        user_sekarang = st.session_state.get("user_aktif", "").lower()
        
        user_rows = [row for row in semua_data if str(row.get('Username', '')).lower() == user_sekarang]
        
        if user_rows:
            # Ambil data JSON mentah
            naskah_mentah = user_rows[-1]['Data_Naskah']
            data_termuat = json.loads(naskah_mentah)
            
            # --- PROSES PERBAIKAN STRUKTUR (PENTING!) ---
            # Mengubah kunci adegan dari "teks" kembali ke "angka"
            if "adegan" in data_termuat:
                adegan_baru = {}
                for k, v in data_termuat["adegan"].items():
                    adegan_baru[int(k)] = v # Paksa jadi angka 1, 2, 3...
                data_termuat["adegan"] = adegan_baru
            
            # Masukkan ke laci utama
            st.session_state.data_produksi = data_termuat
            
            # Update versi form agar layar dipaksa gambar ulang
            if 'form_version' not in st.session_state:
                st.session_state.form_version = 0
            st.session_state.form_version += 1
            
            st.success(f"🔄 Naskah {user_sekarang} Berhasil Dipulihkan!")
            st.rerun()
        else:
            st.warning("⚠️ Data tidak ditemukan di Cloud.")
    except Exception as e:
        st.error(f"Gagal memuat: {e}")
        
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
        /* 8. COPY TO CLIPBOARD - BUTTON STYLING */
        /* Kotak kodenya kita buat lebih tegas */
        .stCodeBlock {
            border: 1px solid #30363d !important;
            border-radius: 10px !important;
            background-color: #0d1117 !important;
            padding: 10px !important;
        }
        
        /* Tombol copy bawaan Streamlit dibuat besar & berwarna hijau */
        button[title="Copy to clipboard"] {
            background-color: #238636 !important;
            color: white !important;
            transform: scale(1.6); /* Memperbesar ukuran ikon */
            margin-right: 15px !important;
            margin-top: 15px !important;
            border-radius: 6px !important;
            border: none !important;
            transition: all 0.2s ease-in-out !important;
        }
        
        /* Efek saat kursor menempel (Hover) */
        button[title="Copy to clipboard"]:hover {
            background-color: #2ea043 !important;
            transform: scale(1.8) !important;
            cursor: pointer !important;
        }

        /* Menghilangkan background bawaan agar warna hijau kita solid */
        button[title="Copy to clipboard"]:active {
            background-color: #3fb950 !important;
        }

        /* 9. PROTEKSI LAYAR (PC ONLY) - DI POSISI PALING BAWAH */
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
# BAGIAN 4: NAVIGASI SIDEBAR (VERSI CLOUD ONLY)
# ==============================================================================
def tampilkan_navigasi_sidebar():
    with st.sidebar:
        # 1. JUDUL DENGAN IKON (Sesuai Gambar)
        st.markdown("""
            <div style='display: flex; align-items: center; margin-bottom: 10px; margin-top: 10px;'>
                <span style='font-size: 20px; margin-right: 10px;'>🖥️</span>
                <span style='font-size: 14px; color: white; font-weight: bold; letter-spacing: 1px;'>
                    MAIN COMMAND
                </span>
            </div>
        """, unsafe_allow_html=True)
        
        # 2. MENU RADIO (Daftar Pilihan)
        pilihan = st.radio(
            "COMMAND_MENU",
            [
                "🚀 RUANG PRODUKSI", 
                "🧠 PINTAR AI LAB", 
                "⚡ QUICK PROMPT", 
                "📋 TUGAS KERJA", 
                "⚡ KENDALI TIM"
            ],
            label_visibility="collapsed"
        )
        
        # 3. GARIS PEMISAH & SPASI KE BAWAH
        st.markdown("<hr style='margin: 20px 0; border-color: #30363d;'>", unsafe_allow_html=True)
        
        # 1. KOTAK DURASI FILM
        st.markdown("<p class='small-label'>🎬 DURASI FILM (ADEGAN)</p>", unsafe_allow_html=True)
        st.session_state.data_produksi["jumlah_adegan"] = st.number_input(
            "Jumlah Adegan", 1, 50, 
            value=st.session_state.data_produksi["jumlah_adegan"],
            label_visibility="collapsed"
        )
        
        # 2. SISTEM DATABASE CLOUD (GSHEET)
        st.markdown("<p class='small-label'>☁️ CLOUD DATABASE (GSHEET)</p>", unsafe_allow_html=True)
        
        # Tombol Backup & Restore Berdampingan dengan tampilan default
        col1, col2 = st.columns(2)
        with col1:
            # type="primary" dihapus agar warnanya default (abu-abu)
            if st.button("📤 BACKUP", use_container_width=True): 
                simpan_ke_gsheet()
        with col2:
            if st.button("🔄 RESTORE", use_container_width=True):
                muat_dari_gsheet()
                
        st.markdown('<div style="margin-top: 50px;"></div>', unsafe_allow_html=True)   
        
        if st.button("⚡ KELUAR SISTEM", use_container_width=True):
            proses_logout()
        
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
# BAGIAN 5: MODUL-MODUL PENDUKUNG (PINTAR AI LAB - PERSISTENT VERSION)
# ==============================================================================

def tampilkan_ai_lab():
    st.title("🧠 PINTAR AI LAB")
    st.caption("Solusi cerdas buat staf Pintar Media. Data aman dan sinkron!")
    st.divider() 

    # --- 1. DEFINISI DAFTAR PILIHAN (Agar Konsisten) ---
    opsi_pola = [
        "Viral Drama (Zero to Hero / Revenge)", 
        "Lomba Konyol (Komedi Interaktif / Call to Action)",
        "Drama Plot Twist (Standard)",
        "Komedi Slapstick"
    ]
    
    opsi_visual = [
        "Cinematic Realistic (Seperti Film Nyata)",
        "3D Pixar Style (Ceria & Detail)",
        "Anime / Manga Style",
        "Retro Cartoon"
    ]

    # --- 2. INISIALISASI SESSION STATE ---
    if 'lab_topik' not in st.session_state: st.session_state.lab_topik = ""
    if 'lab_pola' not in st.session_state: st.session_state.lab_pola = opsi_pola[0]
    if 'lab_visual' not in st.session_state: st.session_state.lab_visual = opsi_visual[0]
    if 'lab_adegan' not in st.session_state: st.session_state.lab_adegan = 5
    if 'jumlah_karakter' not in st.session_state: st.session_state.jumlah_karakter = 2
    if 'lab_hasil_mantra' not in st.session_state: st.session_state.lab_hasil_mantra = None

    # --- 3. LAYOUT UTAMA ---
    col_kerja, col_sidebar = st.columns([2, 1.5], gap="large")

    with col_kerja:
        st.subheader("📝 Topik & Premis Utama")
        st.session_state.lab_topik = st.text_area(
            "Detail Cerita", 
            value=st.session_state.lab_topik,
            placeholder="Contoh: Udin dituduh mencuri di toko emas...",
            height=300, 
            label_visibility="collapsed"
        )
        
        st.write(" ")
        st.markdown("**🎬 Jumlah Adegan**")
        st.session_state.lab_adegan = st.select_slider(
            "Pilih jumlah adegan",
            options=list(range(3, 11)),
            value=st.session_state.lab_adegan,
            label_visibility="collapsed"
        )
        
        st.write(" ")
        btn_generate = st.button("✨ GENERATE MASTER PROMPT", use_container_width=True, type="primary")

        # Tombol Reset (Opsional, ditaruh kecil di bawah)
        if st.button("🗑️ Reset Form", use_container_width=False):
            st.session_state.lab_topik = ""
            st.session_state.lab_hasil_mantra = None
            st.rerun()

    with col_sidebar:
        st.subheader("👤 Pengaturan")
        
        # Kontrol Karakter
        c_add, c_rem = st.columns(2)
        with c_add:
            if st.button("➕ Tambah Tokoh", use_container_width=True) and st.session_state.jumlah_karakter < 4:
                st.session_state.jumlah_karakter += 1
                st.rerun()
        with c_rem:
            if st.button("➖ Kurang Tokoh", use_container_width=True) and st.session_state.jumlah_karakter > 1:
                st.session_state.jumlah_karakter -= 1
                st.rerun()

        st.write("---")
        
        list_karakter = []
        char_col1, char_col2 = st.columns(2)
        
        for i in range(st.session_state.jumlah_karakter):
            target_col = char_col1 if i % 2 == 0 else char_col2
            with target_col:
                with st.container(border=True):
                    st.markdown(f"**Tokoh {i+1}**")
                    nama = st.text_input(f"Nama {i}", value=f"Tokoh {i+1}", key=f"lab_n_{i}", label_visibility="collapsed")
                    sifat = st.text_input(f"Sifat {i}", placeholder="Sifat/Visual", key=f"lab_s_{i}", label_visibility="collapsed")
                    list_karakter.append(f"{i+1}. {nama.upper()}: {sifat}")

        st.write("---")
        
        # Menggunakan .index() yang lebih aman karena list opsi sudah didefinisikan di atas
        st.session_state.lab_pola = st.selectbox(
            "🎭 Pola Alur", 
            options=opsi_pola,
            index=opsi_pola.index(st.session_state.lab_pola)
        )
        
        st.session_state.lab_visual = st.selectbox(
            "🎨 Gaya Visual", 
            options=opsi_visual,
            index=opsi_visual.index(st.session_state.lab_visual)
        )

    # --- 4. LOGIKA GENERATE ---
    if btn_generate:
        if st.session_state.lab_topik:
            # Mapping Produksi
            visual_map = {
                "Cinematic Realistic (Seperti Film Nyata)": "Cinematic realistic photography, 8k resolution, highly detailed texture.",
                "3D Pixar Style (Ceria & Detail)": "3D Pixar-style animation, vibrant colors, cinematic lighting.",
                "Anime / Manga Style": "Modern anime style, vibrant colors, clean lines.",
                "Retro Cartoon": "1990s retro cartoon style, bold outlines."
            }
            prompt_visual = visual_map[st.session_state.lab_visual]
            str_karakter = "\n".join(list_karakter)
            tokoh_utama = list_karakter[0].split(". ")[1].split(":")[0]

            if st.session_state.lab_pola == "Viral Drama (Zero to Hero / Revenge)":
                alur_spesifik = f"Adegan 1: {tokoh_utama} dituduh/dihina. Adegan Akhir: {tokoh_utama} terbukti hebat."
                judul_v = f"🔥 JUDUL: Dituduh {st.session_state.lab_topik[:20]}..., Ternyata {tokoh_utama} Adalah..."
            elif st.session_state.lab_pola == "Lomba Konyol (Komedi Interaktif / Call to Action)":
                alur_spesifik = f"Adegan 1-3: Lomba konyol. Adegan 4: {tokoh_utama} minta LIKE & SUB. Adegan 5: Juara konyol."
                judul_v = f"🤣 JUDUL: Lomba {st.session_state.lab_topik[:20]}... Paling Absurd!"
            else:
                alur_spesifik = "Alur standar dengan plot twist."
                judul_v = f"🎬 JUDUL: Kisah {st.session_state.lab_topik[:20]}..."

            st.session_state.lab_hasil_mantra = {
                "judul": judul_v,
                "mantra": f"""Identitas: Kamu adalah Scriptwriter Pro untuk channel 'Pintar Media'.
Karakter Wajib:
{str_karakter}

Tugas: Buatkan naskah {st.session_state.lab_adegan} adegan dengan pola: {st.session_state.lab_pola}.
Topik Cerita: {st.session_state.lab_topik}
Alur Spesifik: {alur_spesifik}

Format Output: Tabel (Adegan, Aksi Visual Detail, Prompt Gambar Inggris, SFX).
Gaya Visual: {prompt_visual}"""
            }

    if st.session_state.lab_hasil_mantra:
        st.divider()
        st.subheader("📜 Hasil Produksi")
        res_c1, res_c2 = st.columns([0.4, 0.6])
        with res_c1:
            st.info("💎 Judul Clickbait")
            st.code(st.session_state.lab_hasil_mantra["judul"], language="text")
        with res_c2:
            st.info("🔮 Mantra Naskah")
            st.code(st.session_state.lab_hasil_mantra["mantra"], language="text")
            
def tampilkan_quick_prompt(): 
    st.markdown("### ⚡ Quick Prompt")
    st.info("Halaman ini sedang disiapkan untuk settingan kualitas global (Quality Booster).")

def tampilkan_tugas_kerja(): 
    st.markdown("### 📋 Tugas Kerja")
    st.info("Daftar tugas tim produksi Pintar Media.")

def tampilkan_kendali_tim(): 
    st.markdown("### ⚡ Kendali Tim")
    st.info("Area manajemen staf dan performa.")

# ==============================================================================
# BAGIAN 6: MODUL UTAMA - RUANG PRODUKSI (VERSI MODULAR QUALITY)
# ==============================================================================
def tampilkan_ruang_produksi():
    sekarang = datetime.utcnow() + timedelta(hours=7) 
    hari_id = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    bulan_id = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    nama_hari = hari_id[sekarang.weekday()]
    tgl = sekarang.day
    nama_bulan = bulan_id[sekarang.month - 1]
    user_aktif = st.session_state.get("user_aktif", "User").upper()

    # --- [NEW] QUALITY BOOSTER (Settingan Umum Pusat) ---
    # Nantinya QB ini bisa kamu kendalikan dari halaman QUICK PROMPT
    QB_IMG = "shot on Fujifilm X-T4, 8k, skin pores detail, sharp focus, ray-traced ambient occlusion, NO SOFTENING"
    QB_VID = "Unreal Engine 5.4, Octane Render, 8k, cinematic production, stable motion, high-fidelity fabric texture"

    # HEADER
    c1, c_kosong, c2 = st.columns([2, 0.5, 0.9]) 
    with c1:
        st.markdown("# 🚀 RUANG PRODUKSI")
    with c2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(f"🛰️ {nama_hari}, {tgl} {nama_bulan} | Staf: {user_aktif}")
    
    data = st.session_state.data_produksi
    ver = st.session_state.get("form_version", 0)

    # 1. IDENTITY LOCK
    with st.expander("🛡️ IDENTITY LOCK - Referensi Foto", expanded=True):
        data["jumlah_karakter"] = st.number_input("Jumlah Karakter", 1, 4, data["jumlah_karakter"], label_visibility="collapsed", key=f"num_char_{ver}")
        
        cols_char = st.columns(data["jumlah_karakter"])
        for i in range(data["jumlah_karakter"]):
            with cols_char[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                data["karakter"][i]["nama"] = st.text_input("Nama", value=data["karakter"][i]["nama"], key=f"char_nama_{i}_{ver}", placeholder="Nama...", label_visibility="collapsed")
                data["karakter"][i]["wear"] = st.text_input("Pakaian", value=data["karakter"][i]["wear"], key=f"char_wear_{i}_{ver}", placeholder="Pakaian...", label_visibility="collapsed")
                data["karakter"][i]["fisik"] = st.text_area("Ciri Fisik", value=data["karakter"][i]["fisik"], key=f"char_fix_{i}_{ver}", height=80, placeholder="Fisik...", label_visibility="collapsed")

    # 2. GENERASI INPUT ADEGAN
    for s in range(data["jumlah_adegan"]):
        scene_id = s + 1
        
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
                st.markdown('<p class="small-label">📸 NASKAH VISUAL & AKSI</p>', unsafe_allow_html=True)
                data["adegan"][scene_id]["aksi"] = st.text_area(f"Aksi_{scene_id}", value=data["adegan"][scene_id]["aksi"], height=345, key=f"act_{scene_id}_{ver}", label_visibility="collapsed", placeholder="Tulis aksi visual di sini...")
            
            with col_set:
                sub1, sub2 = st.columns(2)
                opts_style = ["Realistis", "Pixar 3D", "Glossy Asphalt", "Naruto Anime"]
                opts_light = ["Golden Hour", "Studio", "Natural"]
                opts_arah  = ["Normal", "Sudut Tinggi", "Samping", "Berhadapan"]
                opts_shot  = ["Dekat Wajah", "Setengah Badan", "Seluruh Badan", "Pemandangan Luas", "Drone Shot"]
                opts_ratio = ["16:9", "9:16", "1:1"]
                opts_cam   = ["Static", "Zoom In", "Tracking"]

                with sub1:
                    st.markdown('<p class="small-label">✨ STYLE</p>', unsafe_allow_html=True)
                    curr_style = data["adegan"][scene_id].get("style", "Realistis")
                    idx_style = opts_style.index(curr_style) if curr_style in opts_style else 0
                    data["adegan"][scene_id]["style"] = st.selectbox(f"S_{scene_id}", opts_style, index=idx_style, key=f"mood_{scene_id}_{ver}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">💡 LIGHTING</p>', unsafe_allow_html=True)
                    curr_light = data["adegan"][scene_id].get("light", "Studio")
                    idx_light = opts_light.index(curr_light) if curr_light in opts_light else 0
                    data["adegan"][scene_id]["light"] = st.selectbox(f"L_{scene_id}", opts_light, index=idx_light, key=f"light_{scene_id}_{ver}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">📐 ARAH KAMERA</p>', unsafe_allow_html=True)
                    curr_arah = data["adegan"][scene_id].get("arah", "Normal")
                    idx_arah = opts_arah.index(curr_arah) if curr_arah in opts_arah else 0
                    data["adegan"][scene_id]["arah"] = st.selectbox(f"A_{scene_id}", opts_arah, index=idx_arah, key=f"arah_{scene_id}_{ver}", label_visibility="collapsed")

                with sub2:
                    st.markdown('<p class="small-label">🔍 UKURAN GAMBAR</p>', unsafe_allow_html=True)
                    curr_shot = data["adegan"][scene_id].get("shot", "Setengah Badan")
                    idx_shot = opts_shot.index(curr_shot) if curr_shot in opts_shot else 0
                    data["adegan"][scene_id]["shot"] = st.selectbox(f"Sh_{scene_id}", opts_shot, index=idx_shot, key=f"shot_{scene_id}_{ver}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">📺 ASPECT RATIO</p>', unsafe_allow_html=True)
                    curr_ratio = data["adegan"][scene_id].get("ratio", "16:9")
                    idx_ratio = opts_ratio.index(curr_ratio) if curr_ratio in opts_ratio else 0
                    data["adegan"][scene_id]["ratio"] = st.selectbox(f"R_{scene_id}", opts_ratio, index=idx_ratio, key=f"ratio_{scene_id}_{ver}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">🎥 GERAKAN</p>', unsafe_allow_html=True)
                    curr_cam = data["adegan"][scene_id].get("cam", "Static")
                    idx_cam = opts_cam.index(curr_cam) if curr_cam in opts_cam else 0
                    data["adegan"][scene_id]["cam"] = st.selectbox(f"C_{scene_id}", opts_cam, index=idx_cam, key=f"cam_{scene_id}_{ver}", label_visibility="collapsed")
                
                st.markdown('<p class="small-label" style="margin-top:15px;">📍 LOKASI</p>', unsafe_allow_html=True)
                data["adegan"][scene_id]["loc"] = st.text_input(f"Loc_{scene_id}", value=data["adegan"][scene_id]["loc"], key=f"loc_{scene_id}_{ver}", label_visibility="collapsed", placeholder="Lokasi adegan...")

            cols_d = st.columns(data["jumlah_karakter"])
            for i in range(data["jumlah_karakter"]):
                with cols_d[i]:
                    char_name = data["karakter"][i]["nama"] if data["karakter"][i]["nama"] else f"Karakter {i+1}"
                    st.markdown(f'<p class="small-label">Dialog {char_name}</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["dialogs"][i] = st.text_input(f"D_{scene_id}_{i}", value=data["adegan"][scene_id]["dialogs"][i], key=f"d_{scene_id}_{i}_{ver}", label_visibility="collapsed", placeholder="Dialog...")

    # --- 3. GLOBAL COMPILER LOGIC ---
    st.markdown("---")
    if st.button("🚀 GENERATE ALL SCENES PROMPT", use_container_width=True, type="primary"):
        adegan_terisi = [s_id for s_id, isi in data["adegan"].items() if isi["aksi"].strip() != ""]
        
        if not adegan_terisi:
            st.error("⚠️ Gagal: Kamu belum mengisi 'NASKAH VISUAL & AKSI' di adegan manapun.")
        else:
            user_nama = st.session_state.get("user_aktif", "User").capitalize()
            st.markdown(f"## 🎬 Hasil Prompt: {user_nama} ❤️")
            
            char_ids = " AND ".join([f"[[ CHARACTER_{c['nama'].upper()}: {c['fisik']}, organic macro-texture, maintain 100% exact facial features. ]]" for c in data["karakter"] if c['nama']])
            char_profiles = ", ".join([f"{c['nama']} (pakaian: {c['wear']}, high-fidelity fabric texture)" for c in data["karakter"] if c['nama']])

            no_text_strict = "STRICTLY NO text, NO typography, NO watermark, NO letters, NO subtitles, NO captions, NO speech bubbles, NO dialogue boxes, NO labels, NO black bars, CLEAN cinematic shot."
            negative_motion_strict = "STRICTLY NO morphing, NO extra limbs, NO distorted faces, NO teleporting objects, NO flickering textures, NO sudden lighting jumps, NO floating hair artifacts."

            for scene_id in adegan_terisi:
                sc = data["adegan"][scene_id]
                
                # --- SMART FILTER LOGIC ---
                loc_lower = sc['loc'].lower()
                is_outdoor = any(x in loc_lower for x in ['hutan', 'jalan', 'taman', 'luar', 'pantai', 'desa', 'kebun', 'sawah', 'langit'])
                tech_base = "extreme edge-enhancement, every pixel is sharp, deep color saturation"

                if is_outdoor:
                    bumbu_final = "hyper-detailed grit, leaf veins, micro-texture on leaves, razor-sharp horizons, cloud texture, NO SOFTENING"
                else:
                    bumbu_final = "hyper-detailed wood grain, fabric textures, polished surfaces, ray-traced reflections, NO SOFTENING"

                with st.expander(f"⌛ PROSES | ADEGAN {scene_id}", expanded=True):
                    img_p = (f"CHARACTER: {char_ids}\n"
                             f"ACTION: {sc['aksi']}\n"
                             f"ENV: {sc['loc']}. {bumbu_final}.\n"
                             f"CAMERA: {QB_IMG}\n" # Memanggil Booster Pusat
                             f"TECH: {sc['style']}, {sc['light']}, {sc['shot']}, {tech_base}\n"
                             f"NEGATIVE PROMPT: {no_text_strict} --ar {sc['ratio']} --v 6.0")
                    
                    vid_p = (f"Profiles: {char_profiles}\n"
                             f"Scene: {sc['aksi']} at {sc['loc']}. {bumbu_final}.\n"
                             f"Tech: {sc['style']}, {sc['shot']}, {sc['cam']}, {QB_VID}\n" # Memanggil Booster Pusat
                             f"NEGATIVE PROMPT: {no_text_strict}, {negative_motion_strict}")

                    c_img, c_vid = st.columns(2)
                    with c_img:
                        st.markdown('<p class="small-label">📷 GAMBAR (ULTRA-SHARP)</p>', unsafe_allow_html=True)
                        st.code(img_p, language="text")
                    with c_vid:
                        st.markdown('<p class="small-label">🎥 VIDEO (ULTRA-SHARP)</p>', unsafe_allow_html=True)
                        st.code(vid_p, language="text")
                
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
























