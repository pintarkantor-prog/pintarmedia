import streamlit as st
import requests  
from datetime import datetime, timedelta
import json
import pandas as pd
import gspread 
from google.oauth2.service_account import Credentials 
from streamlit_gsheets import GSheetsConnection 
import time
import pytz

# ==============================================================================
# BAGIAN 1: PUSAT KENDALI OPSI (SINKRONISASI GLOBAL)
# ==============================================================================
OPTS_STYLE = ["Realistis", "Pixar 3D", "Glossy Asphalt", "Naruto Anime"]
OPTS_LIGHT = ["Golden Hour", "Studio", "Natural", "Cinematic Neon"]
OPTS_ARAH  = ["Normal", "Sudut Tinggi", "Samping", "Berhadapan"]
OPTS_SHOT  = ["Dekat Wajah", "Setengah Badan", "Seluruh Badan", "Drone Shot"]
OPTS_RATIO = ["9:16", "16:9", "1:1"] 
OPTS_CAM   = ["Static", "Zoom In", "Tracking"]

DAFTAR_USER = {
    "dian": "QWERTY21ab", "icha": "udin99", "nissa": "tung22",
    "inggi": "udin33", "lisa": "tung66", "tamu": "123"
}

st.set_page_config(page_title="PINTAR MEDIA | AI Studio", layout="wide")

# ==============================================================================
# FUNGSI ABSENSI OTOMATIS (MESIN ABSEN)
# ==============================================================================
def log_absen_otomatis(nama_user):
    # Dian (Bos) & Tamu tidak perlu masuk hitungan absen
    if nama_user.lower() in ["dian", "tamu"]:
        return
    
    url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
    tz_wib = pytz.timezone('Asia/Jakarta')
    waktu_skrg = datetime.now(tz_wib)
    
    jam = waktu_skrg.hour
    tgl_skrg = waktu_skrg.strftime("%Y-%m-%d")
    jam_skrg = waktu_skrg.strftime("%H:%M")

    # Syarat: Hanya mencatat jika login antara jam 13:00 - 14:00 WIB
    if 13 <= jam < 14:
        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
            client = gspread.authorize(creds)
            sheet_absen = client.open_by_url(url_gsheet).worksheet("Absensi")
            
            # Cek agar tidak tercatat dua kali di hari yang sama
            data_absen = sheet_absen.get_all_records()
            sudah_absen = any(str(row.get('Tanggal')) == tgl_skrg and str(row.get('Nama')).lower() == nama_user.lower() for row in data_absen)
            
            if not sudah_absen:
                sheet_absen.append_row([tgl_skrg, nama_user.upper(), jam_skrg, "HADIR"])
        except:
            pass # Gagal absen tidak boleh bikin aplikasi macet

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
        
        # --- BARIS BARU (Hanya ini yang ditambah) ---
        log_absen_otomatis(user)
        
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
# BAGIAN 5: PINTAR AI LAB - PRO EDITION (SYNCHRONIZED MANTRA)
# ==============================================================================

def tampilkan_ai_lab():
    st.title("🧠 PINTAR AI LAB")
    st.info("🚀 **Gaskeun!** Rakit mantra di mode **Manual**, atau langsung jadi naskah gila di mode **Otomatis** via API Groq!")
    
    # --- 1. KONFIGURASI & SESSION STATE ---
    if 'lab_hasil_otomatis' not in st.session_state: st.session_state.lab_hasil_otomatis = ""
    if 'jumlah_karakter' not in st.session_state: st.session_state.jumlah_karakter = 2
    if 'memori_n' not in st.session_state: st.session_state.memori_n = {}
    if 'memori_s' not in st.session_state: st.session_state.memori_s = {}
    
    opsi_pola = ["Viral Drama (Zero to Hero / Revenge)", "Lomba Konyol (Komedi Interaktif)", "Drama Plot Twist (Standard)", "Komedi Slapstick"]
    opsi_visual = ["Cinematic Realistic (Film Nyata)", "3D Pixar Style (Ceria)", "Anime / Manga Style", "Retro Cartoon"]

    try:
        api_key_groq = st.secrets["GROQ_API_KEY"]
    except:
        api_key_groq = None

    # --- 2. AREA PENGATURAN KARAKTER ---
    st.subheader("👤 Pengaturan Karakter")
    c_add, c_rem, c_spacer = st.columns([0.25, 0.25, 0.5])
    with c_add:
        if st.button("➕ Tambah Karakter", use_container_width=True) and st.session_state.jumlah_karakter < 4:
            st.session_state.jumlah_karakter += 1
            st.rerun()
    with c_rem:
        if st.button("➖ Kurang Karakter", use_container_width=True) and st.session_state.jumlah_karakter > 1:
            st.session_state.jumlah_karakter -= 1
            st.rerun()

    list_karakter = []
    
    # DETAIL KARAKTER (Kontras Navy vs Hitam)
    with st.expander("👥 DETAIL KARAKTER PINTAR MEDIA", expanded=True):
        char_cols = st.columns(2)
        for i in range(st.session_state.jumlah_karakter):
            if i not in st.session_state.memori_n: st.session_state.memori_n[i] = ""
            if i not in st.session_state.memori_s: st.session_state.memori_s[i] = ""
            with char_cols[i % 2]:
                with st.container(border=True):
                    label_k = "Karakter Utama" if i == 0 else f"Karakter {i+1}"
                    st.markdown(f"**{label_k}**")
                    # Input tetap hitam pekat
                    st.session_state.memori_n[i] = st.text_input(f"N{i}", value=st.session_state.memori_n[i], key=f"inp_n_{i}", placeholder="Nama...", label_visibility="collapsed")
                    st.session_state.memori_s[i] = st.text_input(f"S{i}", value=st.session_state.memori_s[i], key=f"inp_s_{i}", placeholder="Sifat/Visual...", label_visibility="collapsed")
                    n_f = st.session_state.memori_n[i] if st.session_state.memori_n[i] else label_k
                    list_karakter.append(f"{i+1}. {n_f.upper()}: {st.session_state.memori_s[i]}")

    st.write("---")

    # --- 3. TAB MENU (MANUAL & OTOMATIS) ---
    tab_manual, tab_otomatis = st.tabs(["🛠️ Mode Manual (Mantra)", "⚡ Mode Otomatis (Groq)"])

    # MODE MANUAL
    with tab_manual:
        with st.expander("📝 TOPIK UTAMA & KONFIGURASI", expanded=True):
            col_m1, col_m2 = st.columns([2, 1])
            with col_m1:
                st.markdown("**📝 Topik Utama**")
                topik_m = st.text_area("T", placeholder="Misal: Udin ingin jadi YouTuber tapi dibully...", height=245, key="m_topik", label_visibility="collapsed")
            with col_m2:
                st.markdown("**🎭 Pola & Style**")
                pola_m = st.selectbox("Pola", opsi_pola, key="m_pola")
                visual_m = st.selectbox("Visual", opsi_visual, key="m_visual")
                adegan_m = st.number_input("Jumlah Adegan", 3, 10, 5, key="m_adegan")

            if st.button("✨ GENERATE MASTER PROMPT", use_container_width=True, type="primary"):
                if topik_m:
                    str_k = "\n".join(list_karakter)
                    mantra_sakti = f"""Kamu adalah Scriptwriter Pro Pintar Media. 
Buatkan naskah YouTube Shorts dalam bentuk TABEL (Adegan, Visual Detail, Prompt Gambar Inggris, SFX).

Karakter:
{str_k}

Topik: {topik_m}
Pola: {pola_m}
Gaya Visual: {visual_m}

Aturan: Gunakan bahasa Indonesia yang viral, santai, dan bikin penasaran. Naskah harus {adegan_m} adegan."""
                    st.divider()
                    st.success("✨ **Mantra Sakti Siap!**")
                    st.code(mantra_sakti, language="text")
                    st.toast("Mantra sudah siap di-copy!", icon="🚀")

    # MODE OTOMATIS
    with tab_otomatis:
        with st.expander("⚡ AI INSTANT GENERATION", expanded=True):
            col_o1, col_o2 = st.columns([2, 1])
            with col_o1:
                st.markdown("**📝 Ide Cerita (API)**")
                topik_o = st.text_area("O", placeholder="Ketik ide ceritanya di sini...", height=245, key="o_topik", label_visibility="collapsed")
            with col_o2:
                st.markdown("**⚙️ Konfigurasi AI**")
                pola_o = st.selectbox("Pola Cerita", opsi_pola, key="o_pola")
                adegan_o = st.number_input("Jumlah Adegan API", 3, 10, 5, key="o_adegan_api")
                st.info("AI otomatis menyesuaikan visual cinematic.")

            if st.button("🔥 GENERATE INSTANT SCRIPT", use_container_width=True, type="primary"):
                if api_key_groq and topik_o:
                    st.toast("Menghubungkan ke Groq...", icon="🌐")
                    with st.spinner("Groq lagi ngetik naskah gila..."):
                        try:
                            import requests
                            headers = {"Authorization": f"Bearer {api_key_groq}", "Content-Type": "application/json"}
                            str_k = "\n".join(list_karakter)
                            prompt_otomatis = f"""Kamu adalah Scriptwriter Pro Pintar Media. 
Buatkan naskah YouTube Shorts VIRAL dalam format TABEL MARKDOWN.

Karakter:
{str_k}

Topik: {topik_o}
Pola: {pola_o}

STRUKTUR TABEL WAJIB:
| Adegan | Visual Detail & Prompt (Indonesia) | Visual Detail & Prompt (Inggris) | Dialog (Bahasa Indonesia) |

Aturan Main:
1. Kolom "Visual Detail & Prompt (Inggris)" harus berisi terjemahan detail dari kolom Indonesia untuk digunakan sebagai Prompt AI Image.
2. Dialog harus santai, viral, dan bikin penasaran.
3. Naskah harus {adegan_o} adegan.
4. JANGAN memberikan kata pembuka, LANGSUNG TABELNYA SAJA.
"""

                            payload = {
                                "model": "llama-3.3-70b-versatile", 
                                "messages": [{"role": "user", "content": prompt_otomatis}],
                                "temperature": 0.7
                            }
                            res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
                            st.session_state.lab_hasil_otomatis = res.json()['choices'][0]['message']['content']
                            st.balloons()
                            st.toast("Naskah Berhasil Dibuat!", icon="✅")
                        except Exception as e:
                            st.error(f"Error: {e}")

        # HASIL NASKAH OTOMATIS: Versi 3 Tombol Sejajar
        if st.session_state.lab_hasil_otomatis:
            st.write("") 
            with st.expander("🎬 NASKAH JADI (HASIL GROQ)", expanded=True):
                st.markdown(st.session_state.lab_hasil_otomatis)
                
                st.divider()
                
                # Kita bagi jadi 3 kolom agar rapi
                btn_col1, btn_col2, btn_col3 = st.columns(3)
                
                with btn_col1:
                    # LOGIKA KIRIM (TETAP ADA)
                    if st.button("🚀 KIRIM KE RUANG PRODUKSI", use_container_width=True):
                        st.session_state.naskah_siap_produksi = st.session_state.lab_hasil_otomatis
                        st.session_state.data_produksi["jumlah_adegan"] = adegan_o 
                        st.toast("Naskah & Adegan terkirim!", icon="🚀")
                
                with btn_col2:
                    # LOGIKA BERSIHKAN (BARU)
                    if st.button("🗑️ BERSIHKAN REFERENSI", use_container_width=True):
                        st.session_state.naskah_siap_produksi = ""
                        st.toast("Referensi dibersihkan!", icon="🗑️")
                
                with btn_col3:
                    # LOGIKA DOWNLOAD (TETAP ADA)
                    st.download_button(
                        "📥 DOWNLOAD NASKAH (.txt)", 
                        st.session_state.lab_hasil_otomatis, 
                        file_name="naskah_pintar_media.txt", 
                        use_container_width=True
                    )
                
def tampilkan_quick_prompt():
    st.title("⚡ QUICK PROMPT (INSTAN)")
    
    st.info("""
    💡 **PINTAR MEDIA - MASTERPIECE MODE:**
    - Fokus pada ketajaman optik Ultra-Sharp & Infinite Depth.
    - Karakter bersifat default (sesuaikan di naskah aksi).
    - Mantra Gambar & Video berbaris rapi (List Mode).
    """)

    # --- QUALITY BOOSTER (ULTRA-SHARP SETTINGS) ---
    QB_IMG = (
        "hyper-realistic 8k RAW photo, infinite depth of field, f/11 aperture, "
        "zero bokeh, zero background blur, sharp edge-enhancement, non-filtered, "
        "ultra-clear optical clarity, CPL filter, high local contrast, vivid naturalism"
    )
    
    QB_VID = (
        "Unreal Engine 5.4, 60fps, ultra-clear motion, 8k UHD, high dynamic range, "
        "professional color grading, ray-traced reflections, hyper-detailed textures, "
        "zero digital noise, clean pixels, smooth motion, professional cinematography"
    )

    no_text_strict = "STRICTLY NO text, NO typography, NO watermark, NO letters, CLEAN cinematic shot."
    neg_vid_strict = "STRICTLY NO morphing, NO extra limbs, NO distorted faces, NO sudden lighting jumps."

    # --- WORKSPACE UTAMA ---
    with st.expander("🚀 WORKSPACE PRODUKSI INSTAN", expanded=True):
        col_naskah, col_settings = st.columns([1.5, 1])
        
        with col_naskah:
            st.markdown('<p class="small-label">📸 NASKAH VISUAL & AKSI (SATU ADEGAN)</p>', unsafe_allow_html=True)
            aksi_q = st.text_area("Aksi Q", height=300, placeholder="KETIK DI SINI: Deskripsi aksi dan karakter...", key="q_aksi", label_visibility="collapsed")
        
        with col_settings:
            s1, s2 = st.columns(2)
            with s1:
                st.markdown('<p class="small-label">✨ STYLE</p>', unsafe_allow_html=True)
                style_q = st.selectbox("S_Q", OPTS_STYLE, key="q_style", label_visibility="collapsed")
                st.markdown('<p class="small-label" style="margin-top:20px;">🔍 UKURAN</p>', unsafe_allow_html=True)
                shot_q = st.selectbox("Sh_Q", OPTS_SHOT, key="q_shot", label_visibility="collapsed")
            with s2:
                st.markdown('<p class="small-label">💡 LIGHTING</p>', unsafe_allow_html=True)
                light_q = st.selectbox("L_Q", OPTS_LIGHT, key="q_light", label_visibility="collapsed")
                st.markdown('<p class="small-label" style="margin-top:20px;">📐 ARAH</p>', unsafe_allow_html=True)
                arah_q = st.selectbox("A_Q", OPTS_ARAH, key="q_arah", label_visibility="collapsed")

        st.markdown('<p class="small-label" style="margin-top:10px;">📍 LOKASI</p>', unsafe_allow_html=True)
        loc_q = st.text_input("Loc Q", placeholder="CONTOH: Sawah pedesaan...", key="q_loc", label_visibility="collapsed")

    # --- GENERATE LOGIC ---
    st.markdown("---")
    if st.button("🔥 GENERATE MASTERPIECE PROMPT", use_container_width=True, type="primary"):
        if aksi_q:
            bumbu = "hyper-detailed grit, sand, leaf veins, tactile micro-textures" if any(x in loc_q.lower() for x in ['hutan', 'jalan', 'luar', 'sawah']) else "hyper-detailed wood grain, ray-traced reflections"
            
            # --- MANTRA GAMBAR (OPTIMAL & RAPI) ---
            img_p = (
                f"ACTION: {aksi_q}\n\n"
                f"ENV: {loc_q}. {bumbu}. NO SOFTENING.\n\n"
                f"RULE: Use uploaded photos for each character. Interaction required.\n\n"
                f"CAMERA: {shot_q}, {arah_q} view, full profile perspective, {QB_IMG}\n\n"
                f"TECHNICAL: {style_q}, {light_q}, extreme edge-enhancement\n\n"
                f"NEGATIVE PROMPT: {no_text_strict}\n\n"
                f"FORMAT: Aspect Ratio {OPTS_RATIO[0]}, Ultra-HD Photorealistic RAW Output"
            )

            # --- MANTRA VIDEO (OPTIMAL & RAPI) ---
            vid_p = (
                f"SCENE: {aksi_q} at {loc_q}\n\n"
                f"RULE: Character Interaction Required. Consistency from uploaded photo reference.\n\n"
                f"ACTION & MOTION: Character must move naturally with fluid cinematic motion, no robotic movement, no stiffness.\n\n"
                f"TECHNICAL: {QB_VID}, {style_q}, {shot_q}, cinematic character-tracking motion\n\n"
                f"NEGATIVE PROMPT: {no_text_strict}, {neg_vid_strict}\n\n"
                f"FORMAT: 9:16 Vertical Aspect, 8k Ultra-HD Cinematic Motion Render, Zero Compression"
            )
            
            st.success("✅ Mantra Masterpiece Berhasil Dirakit!")
            with st.expander("📋 HASIL RAKITAN MANTRA", expanded=True):
                c_res1, c_res2 = st.columns(2)
                with c_res1:
                    st.markdown('<p class="small-label">📷 MANTRA GAMBAR</p>', unsafe_allow_html=True)
                    st.code(img_p, language="text")
                with c_res2:
                    st.markdown('<p class="small-label">🎥 MANTRA VIDEO</p>', unsafe_allow_html=True)
                    st.code(vid_p, language="text")
        else:
            st.warning("Isi dulu aksinya, Bos!")
            
def tampilkan_tugas_kerja():
    st.title("🚀 PINTAR INTEGRATED SYSTEM")
    
    url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
    user_sekarang = st.session_state.get("user_aktif", "tamu").lower()
    tz_wib = pytz.timezone('Asia/Jakarta')
    
    foto_staff = {
        "icha": "https://cdn-icons-png.flaticon.com/512/6997/6997662.png", 
        "nissa": "https://cdn-icons-png.flaticon.com/512/6997/6997674.png",
        "inggi": "https://cdn-icons-png.flaticon.com/512/6997/6997662.png",
        "lisa": "https://cdn-icons-png.flaticon.com/512/6997/6997674.png"
    }
    
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
        client = gspread.authorize(creds)
        sheet_tugas = client.open_by_url(url_gsheet).worksheet("Tugas")
        data_tugas = sheet_tugas.get_all_records()
    except Exception as e:
        st.error(f"❌ Database Offline: {e}")
        return

    # ==============================================================================
    # 1. PANEL BOS DIAN (Hanya Dian yang bisa input)
    # ==============================================================================
    if user_sekarang == "dian":
        with st.expander("✨ **DEPLOY TUGAS EDIT BARU**", expanded=False):
            c2, c1 = st.columns([2, 1]) 
            with c2:
                st.write("**📝 INSTRUKSI EDIT / MANTRA**")
                isi_tugas = st.text_area("Isi", height=160, placeholder="Ketik mantra...", label_visibility="collapsed")
            with c1:
                st.write("**👤 TARGET EDITOR**")
                staf_tujuan = st.selectbox("Editor", ["Icha", "Nissa", "Inggi", "Lisa"], label_visibility="collapsed")
            
            if st.button("🚀 KIRIM KE EDITOR", use_container_width=True):
                if isi_tugas:
                    t_id = f"ID{datetime.now(tz_wib).strftime('%m%d%H%M%S')}"
                    tgl_deploy = datetime.now(tz_wib).strftime("%Y-%m-%d") 
                    sheet_tugas.append_row([t_id, staf_tujuan, tgl_deploy, isi_tugas, "PROSES", "-", "", ""])
                    st.success("✅ Berhasil!")
                    time.sleep(1); st.rerun()

    st.divider()

    # ==============================================================================
    # 2. DAFTAR TUGAS (FILTER: HILANG JIKA FINISH & SESUAI LOGIN)
    # ==============================================================================
    st.subheader("📑 Tugas On-Progress")
    
    if not data_tugas:
        st.info("Belum ada tugas di database.")
    else:
        # --- DISINI TEMPAT FILTERNYA ---
        if user_sekarang == "dian":
            # Dian lihat semua staf, tapi status FINISH disembunyikan
            tugas_terfilter = [t for t in data_tugas if str(t["Status"]).upper() != "FINISH"]
        else:
            # Staf lihat miliknya sendiri DAN status FINISH disembunyikan
            tugas_terfilter = [t for t in data_tugas if str(t["Staf"]).lower() == user_sekarang and str(t["Status"]).upper() != "FINISH"]

        if not tugas_terfilter:
            st.info(f"☕ Luar biasa {user_sekarang.capitalize()}! Semua tugas sudah beres.")
        else:
            for t in reversed(tugas_terfilter):
                status = str(t["Status"]).upper()
                nama_key = t["Staf"].lower()
                url_foto = foto_staff.get(nama_key, "https://cdn-icons-png.flaticon.com/512/847/847969.png")
                warna_icon = "🔵" if status == "PROSES" else "🔴" if status == "REVISI" else "🟠"

                bg_stat = "#007bff" if status == "PROSES" else "#dc3545" if status == "REVISI" else "#ffc107"
                txt_stat = "white" if status != "SEDANG DI REVIEW" else "black"

                with st.container(border=True):
                    # VCard 5-Kolom Sejajar
                    c1, c2, c3, c4, c5 = st.columns([0.8, 1.5, 1.5, 1.5, 2])
                    
                    with c1:
                        st.image(url_foto, width=90)
                    
                    with c2:
                        st.write(f"**{warna_icon} {t['Staf'].upper()}**")
                        st.markdown(f"""<div style="background-color:{bg_stat}; color:{txt_stat}; 
                                    padding:3px 10px; border-radius:8px; text-align:center; 
                                    font-size:11px; font-weight:bold; width:95px; border: 1px solid rgba(255,255,255,0.1);">
                                    {status}</div>""", unsafe_allow_html=True)

                    with c3:
                        st.caption("🆔 ID TUGAS")
                        st.write(f"**{t['ID']}**")

                    with c4:
                        st.caption("📅 TGL DEPLOY")
                        st.write(f"**{t['Deadline']}**")

                    with c5:
                        st.caption("⏰ WAKTU SETOR")
                        st.write(f"**{t['Waktu_Kirim']}**")

                    with st.expander("🔍 DETAIL MANTRA & AKSI"):
                        st.code(t["Instruksi"], language="text")
                        if t.get("Link_Hasil"):
                            st.write(f"🔗 [HASIL VIDEO]({t['Link_Hasil']})")
                        if t.get("Catatan_Revisi"):
                            st.warning(f"⚠️ **REVISI:** {t['Catatan_Revisi']}")
                        
                        st.divider()
                        
                        # --- LOGIKA TOMBOL STAF ---
                        if user_sekarang != "dian" and user_sekarang != "tamu":
                            if status in ["PROSES", "REVISI"]:
                                link_input = st.text_input("Link GDrive:", value=t.get("Link_Hasil", ""), key=f"link_{t['ID']}")
                                if st.button("🚩 SETOR HASIL", key=f"btn_s_{t['ID']}", use_container_width=True, disabled=not link_input.strip()):
                                    try:
                                        cell = sheet_tugas.find(str(t['ID']).strip())
                                        jam_setor = datetime.now(tz_wib).strftime("%d/%m/%Y %H:%M WIB")
                                        sheet_tugas.update_cell(cell.row, 5, "SEDANG DI REVIEW")
                                        sheet_tugas.update_cell(cell.row, 7, link_input)
                                        sheet_tugas.update_cell(cell.row, 6, jam_setor)
                                    except: pass
                                    st.success("✅ Berhasil!"); time.sleep(1); st.rerun()
                            else:
                                st.write(f"🕒 Laporan: {t['Waktu_Kirim']}")

                        # --- LOGIKA TOMBOL BOS DIAN ---
                        elif user_sekarang == "dian" and status != "FINISH":
                            c_cat, c_act = st.columns([2, 1])
                            with c_cat: catatan = st.text_area("Catatan:", key=f"cat_{t['ID']}")
                            with c_act:
                                if st.button("🟢 FINISH TOTAL", key=f"fin_{t['ID']}", use_container_width=True):
                                    try:
                                        cell = sheet_tugas.find(str(t['ID']).strip())
                                        sheet_tugas.update_cell(cell.row, 5, "FINISH")
                                    except: pass
                                    st.success("✅ Selesai!"); time.sleep(1); st.rerun()
                                if st.button("🔴 REVISI", key=f"rev_{t['ID']}", use_container_width=True):
                                    try:
                                        cell = sheet_tugas.find(str(t['ID']).strip())
                                        sheet_tugas.update_cell(cell.row, 5, "REVISI"); sheet_tugas.update_cell(cell.row, 8, catatan)
                                    except: pass
                                    st.success("✅ Revisi!"); time.sleep(1); st.rerun()
                                    
def tampilkan_kendali_tim():
    user_sekarang = st.session_state.get("user_aktif", "tamu").lower()
    
    # 1. PROTEKSI AKSES (Hanya Dian yang bisa buka)
    if user_sekarang != "dian":
        st.title("⚡ KENDALI TIM")
        st.divider()
        st.warning("🔒 **AREA TERBATAS**")
        st.info(f"Maaf **{user_sekarang.capitalize()}**, halaman ini hanya dapat diakses oleh Admin untuk pantauan performa.")
        # Menampilkan gambar gembok sebagai pengganti rumah
        st.image("https://cdn-icons-png.flaticon.com/512/2575/2575515.png", width=120)
        return

    # 2. HALAMAN KHUSUS BOS DIAN
    st.title("⚡ PUSAT KENDALI TIM (ADMIN)")
    st.write(f"Monitor performa **Pintar Media** secara real-time.")
    
    url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
    tz_wib = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz_wib)
    
    # Filter Otomatis Bulan & Tahun Berjalan
    bulan_ini = sekarang.month
    tahun_ini = sekarang.year
    nama_bulan = sekarang.strftime("%B %Y")

    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
        client = gspread.authorize(creds)
        
        # --- BAGIAN A: ANALISA PRODUKTIVITAS ---
        sheet_tugas = client.open_by_url(url_gsheet).worksheet("Tugas")
        df_tugas = pd.DataFrame(sheet_tugas.get_all_records())

        st.subheader(f"📊 Produktivitas Editor ({nama_bulan})")
        
        if not df_tugas.empty:
            # Pastikan format tanggal kolom Deadline benar
            df_tugas['Deadline'] = pd.to_datetime(df_tugas['Deadline'])
            
            # Filter: Bulan berjalan & Status FINISH
            mask = (df_tugas['Deadline'].dt.month == bulan_ini) & \
                   (df_tugas['Deadline'].dt.year == tahun_ini) & \
                   (df_tugas['Status'] == "FINISH")
            
            df_bulan_ini = df_tugas[mask]

            if not df_bulan_ini.empty:
                # Grafik Batang Produktivitas 
                prod_counts = df_bulan_ini['Staf'].value_counts()
                st.bar_chart(prod_counts) 
                
                # Metrik Angka Utama
                m1, m2, m3 = st.columns(3)
                with m1: st.metric("Total Video Finish", len(df_bulan_ini))
                with m2: st.metric("Top Editor", prod_counts.idxmax())
                with m3: st.metric("Periode", nama_bulan)
            else:
                st.info("Belum ada data tugas yang selesai (FINISH) di bulan ini.")

        st.divider()

        # --- BAGIAN B: LAPORAN ABSENSI ---
        st.subheader("🕒 Laporan Kehadiran (Auto-Absen)")
        try:
            sheet_absen = client.open_by_url(url_gsheet).worksheet("Absensi")
            df_absen = pd.DataFrame(sheet_absen.get_all_records())
            
            if not df_absen.empty:
                df_absen['Tanggal'] = pd.to_datetime(df_absen['Tanggal'])
                # Filter absen bulan berjalan
                mask_absen = (df_absen['Tanggal'].dt.month == bulan_ini) & \
                             (df_absen['Tanggal'].dt.year == tahun_ini)
                
                df_absen_final = df_absen[mask_absen].sort_values(by="Tanggal", ascending=False)
                
                if not df_absen_final.empty:
                    st.dataframe(df_absen_final, use_container_width=True, hide_index=True)
                else:
                    st.write("Belum ada data kehadiran bulan ini.")
            else:
                st.write("Data kehadiran masih kosong.")
        except:
            st.warning("⚠️ Tab 'Absensi' tidak ditemukan. Pastikan kamu sudah buat tab 'Absensi' di Google Sheets.")

    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
    
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

    # --- [SUNTIKAN MASTERPIECE] QUALITY BOOSTER ---
    # Menggunakan f/11 & CPL Filter untuk ketajaman optik maksimal di Banana & SuperGrok
    QB_IMG = (
        "hyper-realistic 8k RAW photo, infinite depth of field, f/11 aperture, "
        "zero bokeh, zero background blur, sharp edge-enhancement, non-filtered, "
        "ultra-clear optical clarity, CPL filter, high local contrast, vivid naturalism"
    )
    
    # Menggunakan Unreal 5.4 & 60fps untuk fluid motion maksimal di Veo
    QB_VID = (
        "Unreal Engine 5.4, 60fps, ultra-clear motion, 8k UHD, high dynamic range, "
        "professional color grading, ray-traced reflections, hyper-detailed textures, "
        "zero digital noise, clean pixels, smooth motion, professional cinematography"
    )

    # HEADER
    c1, c_kosong, c2 = st.columns([2, 0.5, 0.9]) 
    with c1:
        st.markdown("# 🚀 RUANG PRODUKSI")
    with c2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(f"🛰️ {nama_hari}, {tgl} {nama_bulan} | Staf: {user_aktif}")
    
    data = st.session_state.data_produksi
    ver = st.session_state.get("form_version", 0)

    # 1. INTEGRASI NASKAH DARI AI LAB
    if 'naskah_siap_produksi' in st.session_state and st.session_state.naskah_siap_produksi:
        with st.expander("📖 NASKAH DARI PINTAR AI LAB (REFERENSI)", expanded=True):
            st.info("💡 Gunakan tabel di bawah ini sebagai panduan mengisi Aksi Visual dan Dialog adegan.")
            st.markdown(st.session_state.naskah_siap_produksi)
            
            if st.button("🗑️ Bersihkan Naskah Referensi", use_container_width=True):
                st.session_state.naskah_siap_produksi = ""
                st.rerun()

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
                "aksi": "", 
                "style": OPTS_STYLE[0], 
                "light": OPTS_LIGHT[0], 
                "arah": OPTS_ARAH[0], 
                "shot": OPTS_SHOT[0], 
                "ratio": OPTS_RATIO[0],
                "cam": OPTS_CAM[0],
                "loc": "", 
                "dialogs": [""]*4
            }

        with st.expander(f"🎬 ADEGAN {scene_id}", expanded=(scene_id == 1)):
            col_text, col_set = st.columns([1.5, 1])
            
            with col_text:
                st.markdown('<p class="small-label">📸 NASKAH VISUAL & AKSI</p>', unsafe_allow_html=True)
                data["adegan"][scene_id]["aksi"] = st.text_area(f"Aksi_{scene_id}", value=data["adegan"][scene_id]["aksi"], height=345, key=f"act_{scene_id}_{ver}", label_visibility="collapsed", placeholder="Tulis aksi visual di sini...")
            
            with col_set:
                sub1, sub2 = st.columns(2)
                
                with sub1:
                    st.markdown('<p class="small-label">✨ STYLE</p>', unsafe_allow_html=True)
                    curr_style = data["adegan"][scene_id].get("style", OPTS_STYLE[0])
                    idx_style = OPTS_STYLE.index(curr_style) if curr_style in OPTS_STYLE else 0
                    data["adegan"][scene_id]["style"] = st.selectbox(f"S_{scene_id}", OPTS_STYLE, index=idx_style, key=f"mood_{scene_id}_{ver}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">💡 LIGHTING</p>', unsafe_allow_html=True)
                    curr_light = data["adegan"][scene_id].get("light", OPTS_LIGHT[0])
                    idx_light = OPTS_LIGHT.index(curr_light) if curr_light in OPTS_LIGHT else 0
                    data["adegan"][scene_id]["light"] = st.selectbox(f"L_{scene_id}", OPTS_LIGHT, index=idx_light, key=f"light_{scene_id}_{ver}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">📐 ARAH KAMERA</p>', unsafe_allow_html=True)
                    curr_arah = data["adegan"][scene_id].get("arah", OPTS_ARAH[0])
                    idx_arah = OPTS_ARAH.index(curr_arah) if curr_arah in OPTS_ARAH else 0
                    data["adegan"][scene_id]["arah"] = st.selectbox(f"A_{scene_id}", OPTS_ARAH, index=idx_arah, key=f"arah_{scene_id}_{ver}", label_visibility="collapsed")

                with sub2:
                    st.markdown('<p class="small-label">🔍 UKURAN GAMBAR</p>', unsafe_allow_html=True)
                    curr_shot = data["adegan"][scene_id].get("shot", OPTS_SHOT[0])
                    idx_shot = OPTS_SHOT.index(curr_shot) if curr_shot in OPTS_SHOT else 0
                    data["adegan"][scene_id]["shot"] = st.selectbox(f"Sh_{scene_id}", OPTS_SHOT, index=idx_shot, key=f"shot_{scene_id}_{ver}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">📺 ASPECT RATIO</p>', unsafe_allow_html=True)
                    curr_ratio = data["adegan"][scene_id].get("ratio", OPTS_RATIO[0]) # Memanggil OPTS_RATIO
                    idx_ratio = OPTS_RATIO.index(curr_ratio) if curr_ratio in OPTS_RATIO else 0
                    data["adegan"][scene_id]["ratio"] = st.selectbox(f"R_{scene_id}", OPTS_RATIO, index=idx_ratio, key=f"ratio_{scene_id}_{ver}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">🎥 GERAKAN</p>', unsafe_allow_html=True)
                    curr_cam = data["adegan"][scene_id].get("cam", OPTS_CAM[0]) # Memanggil OPTS_CAM
                    idx_cam = OPTS_CAM.index(curr_cam) if curr_cam in OPTS_CAM else 0
                    data["adegan"][scene_id]["cam"] = st.selectbox(f"C_{scene_id}", OPTS_CAM, index=idx_cam, key=f"cam_{scene_id}_{ver}", label_visibility="collapsed")
                
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

                with st.expander(f"💎 MASTERPIECE RESULT | ADEGAN {scene_id}", expanded=True):
                    # --- MANTRA GAMBAR (LIST MODE & DETAIL CAMERA) ---
                    img_p = (
                        f"CHARACTER: {char_ids}\n\n"
                        f"ACTION: {sc['aksi']}\n\n"
                        f"ENV: {sc['loc']}. {bumbu_final}. NO SOFTENING.\n\n"
                        f"RULE: Use uploaded photos for each character. Interaction required.\n\n"
                        f"CAMERA: {sc['shot']}, {sc['arah']} view, full profile perspective, {QB_IMG}\n\n"
                        f"TECH: {sc['style']}, {sc['light']}, {tech_base}\n\n"
                        f"NEGATIVE PROMPT: {no_text_strict}\n\n"
                        f"FORMAT: Aspect Ratio {sc['ratio']}, Ultra-HD Photorealistic RAW Output"
                    )
                    
                    # --- MANTRA VIDEO (LIST MODE & MOTION MASTERY) ---
                    vid_p = (
                        f"PROFILES: {char_profiles}\n\n"
                        f"SCENE: {sc['aksi']} at {sc['loc']}. {bumbu_final}.\n\n"
                        f"RULE: Character Interaction Required. Consistency from uploaded photo reference.\n\n"
                        f"ACTION & MOTION: Character must move naturally with fluid cinematic motion, no robotic movement, no stiffness.\n\n"
                        f"TECHNICAL: {QB_VID}, {sc['style']}, {sc['shot']}, {sc['cam']}, cinematic character-tracking\n\n"
                        f"NEGATIVE PROMPT: {no_text_strict}, {negative_motion_strict}\n\n"
                        f"FORMAT: {sc['ratio']} Vertical Aspect, 8k Ultra-HD Cinematic Motion Render, Zero Compression"
                    )

                    c_img, c_vid = st.columns(2)
                    with c_img:
                        st.markdown('<p class="small-label">📷 MANTRA GAMBAR</p>', unsafe_allow_html=True)
                        st.code(img_p, language="text")
                    with c_vid:
                        st.markdown('<p class="small-label">🎥 MANTRA VIDEO</p>', unsafe_allow_html=True)
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









































