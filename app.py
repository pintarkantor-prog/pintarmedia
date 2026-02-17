import streamlit as st
import requests  
import pandas as pd
import gspread 
import time
import pytz
import json
import re
from datetime import datetime, timedelta
from google.oauth2.service_account import Credentials

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

st.set_page_config(page_title="PINTAR MEDIA | Studio", layout="wide")

# ==============================================================================
# FUNGSI ABSENSI OTOMATIS (MESIN ABSEN)
# ==============================================================================
def log_absen_otomatis(nama_user):
    if nama_user.lower() in ["dian", "tamu"]:
        return
    
    url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
    tz_wib = pytz.timezone('Asia/Jakarta')
    waktu_skrg = datetime.now(tz_wib)
    
    jam = waktu_skrg.hour
    tgl_skrg = waktu_skrg.strftime("%Y-%m-%d")
    jam_skrg = waktu_skrg.strftime("%H:%M")

    # Syarat: Hanya mencatat jika login antara jam 08:00 - 10:00 WIB
    if 8 <= jam < 10: # Kembalikan ke False/True kalau mau tes malam
        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
            client = gspread.authorize(creds)
            sheet_absen = client.open_by_url(url_gsheet).worksheet("Absensi")
            
            data_absen = sheet_absen.get_all_records()
            sudah_absen = any(str(row.get('Tanggal')) == tgl_skrg and str(row.get('Nama')).upper() == nama_user.upper() for row in data_absen)
            
            if not sudah_absen:
                sheet_absen.append_row([nama_user.upper(), tgl_skrg, jam_skrg, "HADIR"])
                st.toast(f"⏰ Absen Berhasil (Jam {jam_skrg})", icon="✅")
        except:
            pass

# ==============================================================================
# BAGIAN 2: SISTEM KEAMANAN & INISIALISASI DATA (SESSION STATE)
# ==============================================================================
def inisialisasi_keamanan():
    if 'sudah_login' not in st.session_state:
        st.session_state.sudah_login = False
    
    if 'data_produksi' not in st.session_state:
        st.session_state.data_produksi = {
            "jumlah_karakter": 2,
            "karakter": [ {"nama": "", "wear": "", "fisik": ""} for _ in range(4) ],
            "jumlah_adegan": 5,
            "adegan": {} 
        }

    # Perbaikan: Jangan update session login otomatis dari params di sini jika bikin bentrok
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
        
        # AKTIVASI ABSEN
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
            if submit: 
                proses_login(u, p)
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
        st.toast("🚀 Berhasil disimpan ke Cloud!", icon="☁️")
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
    st.info("🚀 **Gaskeun!** Ide cerita di mode **Manual**, atau langsung jadi naskah di mode **Otomatis**!")
    
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
    with st.expander("👥 DETAIL KARAKTER", expanded=True):
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
                    st.session_state.memori_s[i] = st.text_input(f"S{i}", value=st.session_state.memori_s[i], key=f"inp_s_{i}", placeholder="Detail fisik/pakaian...", label_visibility="collapsed")
                    n_f = st.session_state.memori_n[i] if st.session_state.memori_n[i] else label_k
                    list_karakter.append(f"{i+1}. {n_f.upper()}: {st.session_state.memori_s[i]}")

    st.write("---")

    # --- 3. TAB MENU (MANUAL & OTOMATIS) ---
    tab_manual, tab_otomatis = st.tabs(["🛠️ Mode Manual", "⚡ Mode Otomatis"])

    # MODE MANUAL
    with tab_manual:
        with st.expander("📝 KONFIGURASI MANUAL", expanded=True):
            col_m1, col_m2 = st.columns([2, 1])
            with col_m1:
                st.markdown("**📝 Topik Utama**")
                topik_m = st.text_area("T", placeholder="Ketik ide ceritanya di sini...", height=245, key="m_topik", label_visibility="collapsed")
            with col_m2:
                st.markdown("**🎭 Pola & Style**")
                pola_m = st.selectbox("Pola", opsi_pola, key="m_pola")
                visual_m = st.selectbox("Visual", opsi_visual, key="m_visual")
                adegan_m = st.number_input("Jumlah Adegan", 3, 10, 5, key="m_adegan")

            if st.button("✨ GENERATE NASKAH CERITA", use_container_width=True, type="primary"):
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
                    st.success("✨ **Naskah ide cerita Siap!**")
                    st.code(mantra_sakti, language="text")
                    st.toast("Mantra sudah siap di-copy!", icon="🚀")

    # MODE OTOMATIS
    with tab_otomatis:
        with st.expander("⚡ KONFIGURASI OTOMATIS", expanded=True):
            col_o1, col_o2 = st.columns([2, 1])
            with col_o1:
                st.markdown("**📝 Topik Utama**")
                topik_o = st.text_area("O", placeholder="Ketik ide ceritanya di sini...", height=245, key="o_topik", label_visibility="collapsed")
            with col_o2:
                st.markdown("**⚙️ Konfigurasi Otomatis**")
                pola_o = st.selectbox("Pola Cerita", opsi_pola, key="o_pola")
                adegan_o = st.number_input("Jumlah Adegan API", 3, 10, 5, key="o_adegan_api")
                st.info("AI otomatis menyesuaikan ide cerita.")

            if st.button("🔥 GENERATE NASKAH CERITA", use_container_width=True, type="primary"):
                if api_key_groq and topik_o:
                    st.toast("Sedang menghubungkan...", icon="🌐")
                    with st.spinner("lagi ngetik naskah gila..."):
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
                            st.toast("Naskah Berhasil Dibuat!", icon="✅")
                        except Exception as e:
                            st.error(f"Error: {e}")

        # HASIL NASKAH OTOMATIS: Versi 3 Tombol Sejajar
        if st.session_state.lab_hasil_otomatis:
            st.write("") 
            with st.expander("🎬 NASKAH JADI (OTOMATIS)", expanded=True):
                st.markdown(st.session_state.lab_hasil_otomatis)
                
                st.divider()
                
                # Kita bagi jadi 3 kolom agar rapi
                btn_col1, btn_col2, btn_col3 = st.columns(3)
                
                with btn_col1:
                    # LOGIKA KIRIM (TETAP ADA)
                    if st.button("🚀 KIRIM KE RUANG PRODUKSI", use_container_width=True):
                        st.session_state.naskah_siap_produksi = st.session_state.lab_hasil_otomatis
                        st.session_state.data_produksi["jumlah_adegan"] = adegan_o 
                        st.toast("Naskah sukses terkirim!", icon="🚀")
                
                with btn_col2:
                    # LOGIKA BERSIHKAN (BARU)
                    if st.button("🗑️ BERSIHKAN NASKAH", use_container_width=True):
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
    st.title("⚡ QUICK PROMPT")
    
    st.info("""
    💡 **PINTAR MEDIA - INSTAN PROMPT:**
    - Fokus pada ketajaman optik Ultra-Sharp & Infinite Depth.
    - Karakter bersifat default (sesuaikan di naskah aksi).
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
            st.markdown('<p class="small-label">📸 NASKAH VISUAL & AKSI</p>', unsafe_allow_html=True)
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
            
            st.success("✅ Prompt Instan Berhasil Dirakit!")
            with st.expander("📋 Hasil Prompt", expanded=True):
                c_res1, c_res2 = st.columns(2)
                with c_res1:
                    st.markdown('<p class="small-label">📷 PROMPT GAMBAR</p>', unsafe_allow_html=True)
                    st.code(img_p, language="text")
                with c_res2:
                    st.markdown('<p class="small-label">🎥 PROMPT VIDEO</p>', unsafe_allow_html=True)
                    st.code(vid_p, language="text")
        else:
            st.warning("Mohon isi dulu aksinya!")
            
import requests # Pastikan ini ada di baris paling atas app.py

def kirim_notif_wa(pesan):
    """Fungsi otomatis untuk kirim laporan ke Grup WA YT YT 🔥"""
    token = "f4CApLBAJDTPrVHHZCDF"
    target = "120363407726656878@g.us"
    url = "https://api.fonnte.com/send"
    payload = {'target': target, 'message': pesan, 'countryCode': '62'}
    headers = {'Authorization': token}
    try:
        requests.post(url, data=payload, headers=headers, timeout=10)
    except:
        pass

def tampilkan_tugas_kerja():
    st.title("🚀 PINTAR INTEGRATED SYSTEM")
    
    url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
    user_sekarang = st.session_state.get("user_aktif", "tamu").lower()
    tz_wib = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz_wib)
    
    foto_staff_default = "https://cdn-icons-png.flaticon.com/512/847/847969.png"
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
        sheet_log = client.open_by_url(url_gsheet).worksheet("Log_Aktivitas")
        sheet_staff = client.open_by_url(url_gsheet).worksheet("Staff")
        sheet_absensi = client.open_by_url(url_gsheet).worksheet("Absensi")
        
        data_tugas = sheet_tugas.get_all_records()
        df_all_tugas = pd.DataFrame(data_tugas)
        
        if not df_all_tugas.empty:
            df_all_tugas['Deadline_DT'] = pd.to_datetime(df_all_tugas['Deadline'], errors='coerce')
        
        df_staff_raw = pd.DataFrame(sheet_staff.get_all_records())
        staf_options = df_staff_raw['Nama'].unique().tolist()

        def catat_log(aksi):
            waktu_log = datetime.now(tz_wib).strftime("%d/%m/%Y %H:%M:%S")
            sheet_log.append_row([waktu_log, user_sekarang.upper(), aksi])

    except Exception as e:
        st.error(f"❌ Database Offline: {e}")
        return

    # --- 1. LEADERBOARD ---
    if not df_all_tugas.empty:
        mask_l = (df_all_tugas['Deadline_DT'].dt.month == sekarang.month) & \
                 (df_all_tugas['Deadline_DT'].dt.year == sekarang.year) & \
                 (df_all_tugas['Status'].astype(str).str.upper() == "FINISH")
        
        df_finish_l = df_all_tugas[mask_l].copy()
        if not df_finish_l.empty:
            skor = df_finish_l['Staf'].astype(str).str.strip().str.upper().value_counts().reset_index()
            skor.columns = ['Nama', 'Video']
            ranks = skor.values.tolist()
            c1, c2, c3 = st.columns(3)
            with c1: 
                if len(ranks) > 0: st.metric("🥇 JUARA 1", ranks[0][0], f"{ranks[0][1]} Video")
            with c2: 
                if len(ranks) > 1: st.metric("🥈 JUARA 2", ranks[1][0], f"{ranks[1][1]} Video")
            with c3: 
                if len(ranks) > 2: st.metric("🥉 JUARA 3", ranks[2][0], f"{ranks[2][1]} Video")

    st.divider()

    # --- 2. PANEL ADMIN (DEPLOY TUGAS) ---
    if user_sekarang == "dian":
        with st.expander("✨ **KIRIM TUGAS BARU**", expanded=False):
            c2, c1 = st.columns([2, 1]) 
            with c2:
                isi_tugas = st.text_area("Instruksi Tugas", height=150)
            with c1:
                staf_tujuan = st.selectbox("Pilih Editor", staf_options)
            if st.button("🚀 KIRIM KE EDITOR", use_container_width=True):
                if isi_tugas:
                    t_id = f"ID{datetime.now(tz_wib).strftime('%m%d%H%M%S')}"
                    tgl_deploy = datetime.now(tz_wib).strftime("%Y-%m-%d") 
                    sheet_tugas.append_row([t_id, staf_tujuan, tgl_deploy, isi_tugas, "PROSES", "-", "", ""])
                    catat_log(f"Kirim Tugas Baru {t_id} ke {staf_tujuan}")
                    
                    # --- NOTIF WA ---
                    kirim_notif_wa(f"✨ *INFO TUGAS BARU*\n\n👤 *Untuk:* {staf_tujuan.upper()}\n🆔 *ID:* {t_id}\n📝 *Detail:* {isi_tugas[:100]}...\n\n_Silakan cek dashboard untuk pengerjaan._ 🚀")
                    st.success("✅ Berhasil terkirim!"); time.sleep(1); st.rerun()

    # --- 3. DAFTAR TUGAS AKTIF ---
    st.subheader("📑 Tugas On-Progress")
    tugas_terfilter = []
    if not df_all_tugas.empty:
        if user_sekarang == "dian":
            tugas_terfilter = [t for t in data_tugas if str(t["Status"]).upper() != "FINISH"]
        else:
            tugas_terfilter = [t for t in data_tugas if str(t["Staf"]).lower() == user_sekarang and str(t["Status"]).upper() != "FINISH"]

    if not tugas_terfilter:
        st.info(f"☕ Belum ada tugas aktif.")
    else:
        for t in reversed(tugas_terfilter):
            status = str(t["Status"]).upper()
            nama_key = str(t["Staf"]).lower()
            url_foto = foto_staff.get(nama_key, foto_staff_default)
            
            try: selisih = (sekarang.date() - pd.to_datetime(t['Deadline']).date()).days
            except: selisih = 0
            is_telat = status in ["PROSES", "REVISI"] and selisih >= 2
            
            st.markdown(f'<div style="border: 2px solid {"#ff4b4b" if is_telat else "rgba(255,255,255,0.1)"}; padding: 15px; border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">', unsafe_allow_html=True)
            c1, c2, c3, c4, c5 = st.columns([0.8, 1.5, 1.5, 1.5, 2])
            with c1: st.image(url_foto, width=90)
            with c2: 
                st.write(f"**{str(t['Staf']).upper()}**")
                st.caption(f"{status} {'⚠️ DEADLINE!' if is_telat else ''}")
            with c3: st.caption("🆔 ID"); st.write(t['ID'])
            with c4: st.caption("📅 DEADLINE"); st.write(t['Deadline'])
            with c5: st.caption("⏰ SETOR"); st.write(t['Waktu_Kirim'])

            with st.expander("🔍 CEK TUGAS KERJA HARIAN"):
                st.code(t["Instruksi"])
                if t.get("Link_Hasil") and t["Link_Hasil"] != "-":
                    links = str(t["Link_Hasil"]).split(",")
                    for i, link in enumerate(links):
                        if "http" in link: st.write(f"🔗 [LINK {i+1}]({link.strip()})")
                
                if t.get("Catatan_Revisi"): st.warning(f"⚠️ {t['Catatan_Revisi']}")
                st.divider()
                
                if user_sekarang != "dian" and user_sekarang != "tamu":
                    if status in ["PROSES", "REVISI"]:
                        l_in = st.text_input("Link GDrive:", value=t.get("Link_Hasil", ""), key=f"l_{t['ID']}")
                        if st.button("🚩 SETOR HASIL", key=f"b_{t['ID']}", use_container_width=True):
                            cell = sheet_tugas.find(str(t['ID']).strip())
                            sheet_tugas.update_cell(cell.row, 5, "SEDANG DI REVIEW")
                            sheet_tugas.update_cell(cell.row, 7, l_in)
                            sheet_tugas.update_cell(cell.row, 6, sekarang.strftime("%d/%m/%Y %H:%M"))
                            catat_log(f"Menyetor tugas {t['ID']}")
                            
                            # --- NOTIF WA ---
                            kirim_notif_wa(f"📤 *UPDATE SETORAN TUGAS*\n\n👤 *Nama:* {user_sekarang.upper()}\n🆔 *ID:* {t['ID']}\n🔗 *Link:* {l_in}\n\n_Tugas sudah dikirim ke sistem._ 🍿")
                            st.success("✅ Berhasil terkirim!"); time.sleep(1); st.rerun()
                elif user_sekarang == "dian" and status != "FINISH":
                    cat = st.text_area("Catatan Revisi:", key=f"cat_{t['ID']}")
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("🟢 VALIDASI (FINISH)", key=f"f_{t['ID']}", use_container_width=True):
                            cell = sheet_tugas.find(str(t['ID']).strip())
                            sheet_tugas.update_cell(cell.row, 5, "FINISH")
                            catat_log(f"Finish tugas {t['ID']}")
                            
                            # --- NOTIF WA ---
                            kirim_notif_wa(f"✅ *TUGAS SELESAI*\n\nTugas Nama *{t['Staf'].upper()}* (ID: {t['ID']}) telah divalidasi.\n✨ Hasil kerja sudah masuk rekapan bulanan.")
                            st.success("✅ Validasi Selesai!"); time.sleep(1); st.rerun()
                    with col2:
                        if st.button("🔴 MINTA REVISI", key=f"r_{t['ID']}", use_container_width=True):
                            cell = sheet_tugas.find(str(t['ID']).strip())
                            sheet_tugas.update_cell(cell.row, 5, "REVISI")
                            sheet_tugas.update_cell(cell.row, 8, cat)
                            catat_log(f"Revisi tugas {t['ID']}")
                            
                            # --- NOTIF WA ---
                            kirim_notif_wa(f"⚠️ *NOTIFIKASI REVISI*\n\n👤 *Nama:* {t['Staf'].upper()}\n🆔 *ID:* {t['ID']}\n📝 *Catatan:* {cat}\n\n_Mohon untuk diperbaiki kembali._ 🛠️")
                            st.success("✅ Permintaan revisi dikirim!"); time.sleep(1); st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    # --- 4. LACI ARSIP ---
    st.divider()
    df_arsip = pd.DataFrame()
    with st.expander("📜 Riwayat Tugas Selesai (Bulan Ini)"):
        if not df_all_tugas.empty:
            mask_s = (df_all_tugas['Deadline_DT'].dt.month == sekarang.month) & \
                     (df_all_tugas['Deadline_DT'].dt.year == sekarang.year) & \
                     (df_all_tugas['Status'].astype(str).str.upper() == "FINISH")
            if user_sekarang != "dian": mask_s &= (df_all_tugas['Staf'].astype(str).str.lower() == user_sekarang)
            df_arsip = df_all_tugas[mask_s].copy()
            if not df_arsip.empty: st.dataframe(df_arsip[['ID', 'Staf', 'Deadline', 'Status']], hide_index=True)
            else: st.write("Belum ada riwayat.")

    # --- 5. GAJIAN ---
    if user_sekarang != "dian" and user_sekarang != "tamu" and sekarang.day >= 28:
        st.divider()
        with st.expander("💰 **KLAIM SLIP GAJI BULAN INI**"):
            try:
                jml_video = len(df_arsip)
                data_absensi = sheet_absensi.get_all_records()
                df_absensi = pd.DataFrame(data_absensi)
                if not df_absensi.empty:
                    df_absensi['Tgl_DT'] = pd.to_datetime(df_absensi['Tanggal'], errors='coerce')
                    mask_ab = (df_absensi['Nama'].str.upper() == user_sekarang.upper()) & (df_absensi['Tgl_DT'].dt.month == sekarang.month)
                    jml_hadir = len(df_absensi[mask_ab])
                else: jml_hadir = 0
                
                row_s = df_staff_raw[df_staff_raw['Nama'].str.lower() == user_sekarang]
                gapok = int(row_s['Gaji_Pokok'].values[0]) if not row_s.empty else 0
                tunjangan = int(row_s['Tunjangan'].values[0]) if not row_s.empty else 0
                total_gaji = gapok + tunjangan + (jml_video * 10000) + (jml_hadir * 50000)
                
                st.write(f"### Rincian Gaji {sekarang.strftime('%B %Y')}")
                st.metric("ESTIMASI TOTAL", f"Rp {total_gaji:,}")
                if st.button("🧧 KONFIRMASI TERIMA GAJI", use_container_width=True):
                    catat_log(f"Konfirmasi gaji Rp {total_gaji:,}")
                    
                    # --- NOTIF WA ---
                    kirim_notif_wa(f"🧧 *KONFIRMASI GAJI*\n👤 *Nama:* {user_sekarang.upper()}\n💰 *Total:* Rp {total_gaji:,}\n📅 *Hadir:* {jml_hadir} hari\n🎬 *Video:* {jml_video} clips\n\n_Data telah terekam secara otomatis._ ✅")
                    st.success("Konfirmasi Berhasil!")
            except: st.warning("Sedang memproses data...")
                
def tampilkan_kendali_tim():
    user_sekarang = st.session_state.get("user_aktif", "tamu").lower()
    
    # 1. PROTEKSI AKSES (Hanya Dian)
    if user_sekarang != "dian":
        st.title("⚡ KENDALI TIM")
        st.divider()
        st.warning("🔒 **AREA TERBATAS**")
        return

    # 2. HALAMAN KHUSUS ADMIN
    st.title("⚡ PUSAT KENDALI TIM (ADMIN)")
    
    url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
    tz_wib = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz_wib)
    
    c_bln, c_thn = st.columns([2, 2])
    daftar_bulan = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
    pilihan_nama = c_bln.selectbox("📅 Pilih Bulan Laporan:", list(daftar_bulan.values()), index=sekarang.month - 1)
    bulan_dipilih = [k for k, v in daftar_bulan.items() if v == pilihan_nama][0]
    tahun_dipilih = c_thn.number_input("📅 Tahun:", value=sekarang.year, min_value=2024, max_value=2030)

    st.divider()

    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
        client = gspread.authorize(creds)
        sh = client.open_by_url(url_gsheet)
        
        # --- AMBIL DATA DASAR & NORMALISASI HEADER ---
        def ambil_data(nama_sheet):
            ws = sh.worksheet(nama_sheet)
            data = ws.get_all_records()
            df = pd.DataFrame(data)
            df.columns = [str(c).strip().upper() for c in df.columns]
            return df

        df_staff = ambil_data("Staff")
        df_absen = ambil_data("Absensi")
        df_kas = ambil_data("Arus_Kas")
        ws_tugas = sh.worksheet("Tugas")

        # Ambil Data Tugas Manual
        raw_t = ws_tugas.get_all_values()
        if len(raw_t) > 1:
            h_t = [str(h).strip().upper() for h in raw_t[0]]
            df_tugas = pd.DataFrame(raw_t[1:], columns=h_t)
            if len(df_tugas.columns) >= 5:
                df_tugas.columns.values[4] = "STATUS"
        else:
            df_tugas = pd.DataFrame(columns=['STAF', 'DEADLINE', 'INSTRUKSI', 'STATUS'])

        # --- FUNGSI FILTER TANGGAL AMAN ---
        def saring_tgl(df, kolom, bln, thn):
            if df.empty or kolom.upper() not in df.columns: 
                return pd.DataFrame()
            df['TGL_TEMP'] = pd.to_datetime(df[kolom.upper()], dayfirst=True, errors='coerce')
            mask = df['TGL_TEMP'].apply(lambda x: x.month == bln and x.year == thn if pd.notnull(x) else False)
            return df[mask].copy()

        df_t_bln = saring_tgl(df_tugas, 'DEADLINE', bulan_dipilih, tahun_dipilih)
        df_a_f = saring_tgl(df_absen, 'TANGGAL', bulan_dipilih, tahun_dipilih)
        df_k_f = saring_tgl(df_kas, 'TANGGAL', bulan_dipilih, tahun_dipilih)

        # --- LOGIKA HITUNG KEUANGAN (DIPINDAHKAN KE ATAS TAMPILAN) ---
        df_f_f = df_t_bln[df_t_bln['STATUS'].astype(str).str.upper() == "FINISH"] if not df_t_bln.empty else pd.DataFrame()
        rekap_a = df_a_f['NAMA'].str.upper().value_counts().to_dict() if not df_a_f.empty else {}
        rekap_f = df_f_f['STAF'].str.upper().value_counts().to_dict() if not df_f_f.empty else {}
        
        inc = pd.to_numeric(df_k_f[df_k_f['TIPE'] == 'PENDAPATAN']['NOMINAL'], errors='coerce').sum() if not df_k_f.empty else 0
        ops = pd.to_numeric(df_k_f[df_k_f['TIPE'] == 'PENGELUARAN']['NOMINAL'], errors='coerce').sum() if not df_k_f.empty else 0
        
        pay = 0
        for _, s in df_staff.iterrows():
            n_up = str(s['NAMA']).upper()
            ha, vi = rekap_a.get(n_up, 0), rekap_f.get(n_up, 0)
            if ha > 0 or vi > 0:
                pay += (int(s['GAJI_POKOK']) + int(s['TUNJANGAN']) + (ha*50000) + (vi*10000))

        # --- TAMPILAN 1: DASHBOARD KEUANGAN (POSISI PALING ATAS) ---
        st.subheader("💰 LAPORAN KEUANGAN")
        m1, m2, m3 = st.columns(3)
        m1.metric("💰 PENDAPATAN", f"Rp {inc:,}")
        m2.metric("💸 PENGELUARAN", f"Rp {(pay+ops):,}")
        m3.metric("💎 BERSIH", f"Rp {inc-(pay+ops):,}")

        # --- TAMPILAN 2: INPUT TRANSAKSI (POSISI KEDUA) ---
        with st.expander("📝 **INPUT TRANSAKSI KEUANGAN**", expanded=True):
            with st.form("form_kas", clear_on_submit=True):
                c_tipe, c_kat, c_nom = st.columns(3)
                f_tipe = c_tipe.selectbox("Jenis:", ["PENDAPATAN", "PENGELUARAN"])
                f_kat = c_kat.selectbox("Kategori:", ["YouTube", "Brand Deal", "Tool AI", "Internet", "Listrik", "Lainnya"])
                f_nom = c_nom.number_input("Nominal (Rp):", min_value=0, step=10000)
                f_ket = st.text_input("Keterangan:")
                if st.form_submit_button("Simpan Transaksi"):
                    sh.worksheet("Arus_Kas").append_row([sekarang.strftime('%Y-%m-%d'), f_tipe, f_kat, int(f_nom), f_ket, "Dian"])
                    st.success("Tersimpan!"); time.sleep(1); st.rerun()

        st.divider()

        # --- TAMPILAN 3: RUANG QC ---
        st.subheader("🔍 RUANG PEMERIKSAAN (QC)")
        df_qc = df_tugas[df_tugas['STATUS'].astype(str).str.upper() == "WAITING QC"].copy() if not df_tugas.empty else pd.DataFrame()
        
        if not df_qc.empty:
            for i, r in df_qc.iterrows():
                with st.container(border=True):
                    c1, c2, c3 = st.columns([3, 1, 1])
                    c1.write(f"🎬 **{r.get('INSTRUKSI', 'Tanpa Judul')}**")
                    c1.caption(f"Editor: {r.get('STAF', 'Anonim')}")
                    idx = r.name + 2
                    if c2.button("✅ ACC", key=f"acc_{idx}", use_container_width=True):
                        ws_tugas.update_cell(idx, 5, "FINISH"); st.rerun()
                    if c3.button("❌ REV", key=f"rev_{idx}", use_container_width=True):
                        ws_tugas.update_cell(idx, 5, "REVISI"); st.rerun()
        else:
            st.info("Antrean QC kosong. ✨")

        # --- TAMPILAN 4: JADWAL PRODUKSI ---
        st.subheader("📅 JADWAL PRODUKSI")
        if not df_t_bln.empty:
            for _, t in df_t_bln.sort_values('TGL_TEMP').iterrows():
                ikon = {"FINISH": "🟢", "WAITING QC": "🔵", "PROSES": "🟡", "REVISI": "🔴"}.get(str(t['STATUS']).upper(), "⚪")
                st.write(f"{ikon} **{t['TGL_TEMP'].strftime('%d %b')}** - {t.get('INSTRUKSI')} ({t.get('STAF')})")
        else:
            st.caption("Tidak ada jadwal untuk periode ini.")

        # --- TAMPILAN 5: GRAFIK PRODUKTIVITAS ---
        with st.expander("📊 Grafik Produktivitas"):
            if rekap_f:
                st.bar_chart(pd.Series(rekap_f))
            else:
                st.info("Belum ada video selesai bulan ini.")

        # --- TAMPILAN 6: SLIP GAJI (RINCIAN DETAIL UTUH) ---
        with st.expander("💰 RINCIAN GAJI & SLIP (FULL)", expanded=True):
            ada_kerja = False
            for _, s in df_staff.iterrows():
                n_up = str(s['NAMA']).upper()
                ha, vi = rekap_a.get(n_up, 0), rekap_f.get(n_up, 0)
                if ha > 0 or vi > 0:
                    ada_kerja = True
                    b_ha, b_vi = ha*50000, vi*10000
                    tg = int(s['GAJI_POKOK']) + int(s['TUNJANGAN']) + b_ha + b_vi
                    with st.container(border=True):
                        c1, c2, c3 = st.columns([2, 1, 1])
                        c1.write(f"👤 **{s['NAMA']}**"); c1.caption(f"💼 {s['JABATAN']}")
                        c2.write(f"📅 {ha} Hadir"); c3.write(f"🎬 {vi} Video")
                        if st.button(f"🧾 LIHAT SLIP {n_up}", key=f"btn_{n_up}"):
                            slip_html = f"""
                            <div style="background-color: white; color: black; padding: 25px; border-radius: 12px; border: 4px solid #1d976c; font-family: sans-serif; width: 320px; margin: auto; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
                                <div style="text-align: center; margin-bottom: 15px;">
                                    <img src="https://raw.githubusercontent.com/pintarkantor-prog/pintarmedia/main/PINTAR.png" width="130" style="margin-bottom: 5px;">
                                    <div style="font-size: 10px; color: #666;">Creative AI Studio & Production</div>
                                    <hr style="border: 0.5px dashed #1d976c; margin: 12px 0;">
                                    <div style="background-color: #1d976c; color: white; display: inline-block; padding: 5px 15px; border-radius: 6px; font-weight: bold; font-size: 12px;">SLIP GAJI</div>
                                </div>
                                <table style="width: 100%; font-size: 13px; border-collapse: collapse; color: black;">
                                    <tr><td>Staf</td><td align="right"><b>{s_asli}</b></td></tr>
                                    <tr><td>Jabatan</td><td align="right">{jabatan}</td></tr>
                                    <tr><td>Periode</td><td align="right">{pilihan_nama} {tahun_dipilih}</td></tr>
                                    <tr><td colspan="2"><hr style="border: 0.5px solid #eee; margin: 8px 0;"></td></tr>
                                    <tr><td>Gaji Pokok</td><td align="right">Rp {int(gapok):,}</td></tr>
                                    <tr><td>Tunjangan</td><td align="right">Rp {int(tunjangan):,}</td></tr>
                                    <tr><td>Bonus Hadir ({jml_hadir}x)</td><td align="right">Rp {bonus_hadir:,}</td></tr>
                                    <tr><td>Bonus Video ({jml_video}x)</td><td align="right">Rp {bonus_video:,}</td></tr>
                                    <tr><td colspan="2"><hr style="border: 1px dashed black; margin: 15px 0;"></td></tr>
                                    <tr style="font-weight: bold; font-size: 16px; color: #1d976c;">
                                        <td>TOTAL TERIMA</td><td align="right">Rp {total_terima:,}</td></tr>
                                </table>
                                <div style="margin-top: 25px; text-align: center; border-top: 1px solid #eee; padding-top: 10px;">
                                    <div style="font-size: 9px; color: #999;">Diterbitkan otomatis oleh</div>
                                    <div style="font-size: 11px; font-weight: bold; color: #1d976c;">PINTAR MEDIA SYSTEM</div>
                                    <div style="font-size: 8px; color: #ccc; margin-top: 5px;">{datetime.now(tz_wib).strftime('%d/%m/%Y %H:%M')} WIB</div>
                                </div>
                            </div>
                            """
                            st.components.v1.html(slip_html, height=480)
            
            if not ada_kerja:
                st.info("Tidak ada aktivitas staf yang tercatat untuk periode ini.")

    except Exception as e:
        st.error(f"⚠️ Terjadi Kendala Sistem: {e}")
        
# ==============================================================================
# BAGIAN 6: MODUL UTAMA - RUANG PRODUKSI (VERSI TOTAL FULL - NO CUT)
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

    # --- QUALITY BOOSTER & NEGATIVE CONFIG ---
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
    
    no_text_strict = (
        "STRICTLY NO text, NO typography, NO watermark, NO letters, NO subtitles, "
        "NO captions, NO speech bubbles, NO dialogue boxes, NO labels, NO black bars, "
        "NO burned-in text, NO characters speaking with visible words, "
        "the image must be a CLEAN cinematic shot without any written characters."
    )
    negative_motion_strict = (
        "STRICTLY NO morphing, NO extra limbs, NO distorted faces, NO teleporting objects, "
        "NO flickering textures, NO sudden lighting jumps, NO floating hair artifacts."
    )

    # HEADER UI
    c1, c_kosong, c2 = st.columns([2, 0.5, 1.5]) 
    with c1:
        st.markdown("# 🚀 RUANG PRODUKSI")
    with c2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(f"🛰️ {nama_hari}, {tgl} {nama_bulan} | Staf: {user_aktif}")
    
    data = st.session_state.data_produksi
    ver = st.session_state.get("form_version", 0)

    # 1. INTEGRASI REFERENSI NASKAH
    if 'naskah_siap_produksi' in st.session_state and st.session_state.naskah_siap_produksi:
        with st.expander("📖 NASKAH REFERENSI PINTAR AI LAB", expanded=True):
            st.markdown(st.session_state.naskah_siap_produksi)
            if st.button("🗑️ Bersihkan Naskah Referensi", use_container_width=True):
                st.session_state.naskah_siap_produksi = ""
                st.rerun()

    # 2. IDENTITY LOCK
    with st.expander("🛡️ IDENTITY LOCK - Detail Karakter", expanded=True):
        data["jumlah_karakter"] = st.number_input("Jumlah Karakter", 1, 4, data["jumlah_karakter"], label_visibility="collapsed", key=f"num_char_{ver}")
        cols_char = st.columns(data["jumlah_karakter"])
        for i in range(data["jumlah_karakter"]):
            with cols_char[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                data["karakter"][i]["nama"] = st.text_input("Nama", value=data["karakter"][i]["nama"], key=f"char_nama_{i}_{ver}", placeholder="Nama...", label_visibility="collapsed")
                data["karakter"][i]["wear"] = st.text_input("Pakaian", value=data["karakter"][i]["wear"], key=f"char_wear_{i}_{ver}", placeholder="Pakaian...", label_visibility="collapsed")
                data["karakter"][i]["fisik"] = st.text_area("Ciri Fisik", value=data["karakter"][i]["fisik"], key=f"char_fix_{i}_{ver}", height=80, placeholder="Fisik...", label_visibility="collapsed")

    # 3. INPUT ADEGAN (LENGKAP: LIGHTING, RATIO, DLL)
    for s in range(data["jumlah_adegan"]):
        scene_id = s + 1
        if scene_id not in data["adegan"]:
            data["adegan"][scene_id] = {"aksi": "", "style": OPTS_STYLE[0], "light": OPTS_LIGHT[0], "arah": OPTS_ARAH[0], "shot": OPTS_SHOT[0], "ratio": OPTS_RATIO[0], "cam": OPTS_CAM[0], "loc": "", "dialogs": [""]*4}

        with st.expander(f"🎬 ADEGAN {scene_id}", expanded=(scene_id == 1)):
            col_text, col_set = st.columns([1.5, 1])
            with col_text:
                st.markdown('<p class="small-label">📸 NASKAH VISUAL & AKSI</p>', unsafe_allow_html=True)
                data["adegan"][scene_id]["aksi"] = st.text_area(f"Aksi_{scene_id}", value=data["adegan"][scene_id]["aksi"], height=345, key=f"act_{scene_id}_{ver}", label_visibility="collapsed")
            
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
                    curr_ratio = data["adegan"][scene_id].get("ratio", OPTS_RATIO[0])
                    idx_ratio = OPTS_RATIO.index(curr_ratio) if curr_ratio in OPTS_RATIO else 0
                    data["adegan"][scene_id]["ratio"] = st.selectbox(f"R_{scene_id}", OPTS_RATIO, index=idx_ratio, key=f"ratio_{scene_id}_{ver}", label_visibility="collapsed")
                    
                    st.markdown('<p class="small-label" style="margin-top:15px;">🎥 GERAKAN</p>', unsafe_allow_html=True)
                    curr_cam = data["adegan"][scene_id].get("cam", OPTS_CAM[0])
                    idx_cam = OPTS_CAM.index(curr_cam) if curr_cam in OPTS_CAM else 0
                    data["adegan"][scene_id]["cam"] = st.selectbox(f"C_{scene_id}", OPTS_CAM, index=idx_cam, key=f"cam_{scene_id}_{ver}", label_visibility="collapsed")
                
                st.markdown('<p class="small-label" style="margin-top:15px;">📍 LOKASI</p>', unsafe_allow_html=True)
                data["adegan"][scene_id]["loc"] = st.text_input(f"Loc_{scene_id}", value=data["adegan"][scene_id]["loc"], key=f"loc_{scene_id}_{ver}", label_visibility="collapsed", placeholder="Lokasi adegan...")

            # --- DIALOG SECTION ---
            cols_d = st.columns(data["jumlah_karakter"])
            for i in range(data["jumlah_karakter"]):
                with cols_d[i]:
                    char_n = data["karakter"][i]["nama"] or f"K_{i+1}"
                    st.markdown(f'<p class="small-label">Dialog {char_n}</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["dialogs"][i] = st.text_input(f"D_{scene_id}_{i}", value=data["adegan"][scene_id]["dialogs"][i], key=f"d_{scene_id}_{i}_{ver}", label_visibility="collapsed")

    # --- 4. GLOBAL COMPILER LOGIC (LOGIKA SS) ---
    st.markdown("---")
    if st.button("🚀 GENERATE SEMUA PROMPT", use_container_width=True, type="primary"):
        adegan_terisi = [s_id for s_id, isi in data["adegan"].items() if isi["aksi"].strip() != ""]
        if not adegan_terisi:
            st.error("⚠️ Gagal: Kamu belum mengisi 'NASKAH VISUAL & AKSI'!")
        else:
            user_nama = st.session_state.get("user_aktif", "User").capitalize()
            st.markdown(f"## 🎬 Hasil Prompt: {user_nama} ❤️")
            
            for scene_id in adegan_terisi:
                sc = data["adegan"][scene_id]
                v_text_low = sc["aksi"].lower()
                
                # A. SCAN KARAKTER
                found = []
                jml_c = data.get("jumlah_karakter", 2)
                for i in range(jml_c):
                    c = data["karakter"][i]
                    if c['nama'] and re.search(rf'\b{re.escape(c["nama"].lower())}\b', v_text_low):
                        found.append({"id": i+1, "nama": c['nama'].upper(), "fisik": c['fisik'], "wear": c['wear']})

                # B. LOGIKA SS (ULTIMATE BIOMETRIC LOCK - RE-ORDERED)
                if len(found) > 1:
                    h_rule = "STRICT IDENTITY: REFER TO UPLOADED PHOTOS #1 AND #2. 100% face match required."
                    dna_lock = " AND ".join([
                        f"[[ Character_{m['nama']}: (SKS person:1.6), biometric-identical-face-lock with PHOTO #{m['id']}, "
                        f"exact bone structure, maintain 100% facial features from source. "
                        f"Wear: {m['wear']}. Fisik: {m['fisik']}. ]]" 
                        for m in found
                    ])
                
                elif len(found) == 1:
                    m = found[0]
                    h_rule = f"STRICT IDENTITY: REFER TO UPLOADED PHOTO #{m['id']}. Zero identity deviation."
                    dna_lock = (
                        f"[[ Character_{m['nama']}: (SKS person:1.6), biometric-identical-face-lock with PHOTO #{m['id']}, "
                        f"identical facial geometry, matching facial anatomy, 100% consistency. "
                        f"Wear: {m['wear']}. Fisik: {m['fisik']}. ]]"
                    )
                else:
                    h_rule = "IDENTITY: Refer to Photo #1."
                    c1 = data["karakter"][0]
                    dna_lock = f"[[ Main_Character: (SKS person:1.5), biometric face match with PHOTO #1. ]]"

                # C. SMART FILTER (TETAP SAMA)
                loc_lower = sc['loc'].lower()
                is_outdoor = any(x in loc_lower for x in ['hutan', 'jalan', 'taman', 'luar', 'pantai', 'desa', 'kebun', 'sawah', 'langit'])
                bumbu_final = "hyper-detailed grit, leaf veins" if is_outdoor else "hyper-detailed wood grain, ray-traced reflections"

                with st.expander(f"💎 MASTERPIECE RESULT | ADEGAN {scene_id}", expanded=True):
                    # --- MANTRA GAMBAR (SUNTIKAN URUTAN PRIORITAS BARU) ---
                    # Perhatikan: DNA LOCK sekarang ada di PALING ATAS
                    img_p = (
                        f"PRIORITY DNA: {dna_lock}\n"
                        f"RULE: {h_rule}\n\n"
                        f"ACTION: {sc['aksi']}\n"
                        f"ENVIRONMENT: {sc['loc']}. {bumbu_final}. NO SOFTENING.\n"
                        f"CAMERA: {sc['shot']}, {sc['arah']} view, focal-point-on-face, {QB_IMG}\n"
                        f"TECHNICAL: {sc['style']}, {sc['light']}, extreme-edge-enhancement\n"
                        f"NEGATIVE PROMPT: {no_text_strict}, different face, generic person, improvising facial features\n"
                        f"FORMAT: Aspect Ratio {sc['ratio']}, Ultra-HD RAW Output"
                    )
                    
                    vid_p = (
                        f"RULE: {h_rule}\n\n"
                        f"IDENTITY LOCK: {dna_lock}\n"
                        f"SCENE: {sc['aksi']} at {sc['loc']}. {bumbu_final}.\n"
                        f"MOTION: {sc['cam']}, cinematic character-tracking, fluid movement.\n"
                        f"TECHNICAL: {QB_VID}, {sc['style']}, {sc['shot']}\n"
                        f"NEGATIVE PROMPT: {no_text_strict}, {negative_motion_strict}\n"
                        f"FORMAT: {sc['ratio']} Vertical Aspect, 8k Ultra-HD Cinematic Render"
                    )

                    c_img, c_vid = st.columns(2)
                    with c_img: st.markdown("📷 **PROMPT GAMBAR**"); st.code(img_p, language="text")
                    with c_vid: st.markdown("🎥 **PROMPT VIDEO**"); st.code(vid_p, language="text")
                
                st.markdown('<div style="margin-bottom: -15px;"></div>', unsafe_allow_html=True)
                
# ==============================================================================
# BAGIAN 7: PENGENDALI UTAMA
# ==============================================================================
def utama():
    inisialisasi_keamanan() 
    pasang_css_kustom() # Tambahkan ini agar CSS kamu langsung aktif saat login
    
    if not cek_autentikasi():
        tampilkan_halaman_login()
    else:
        # Panggil Sidebar & Menu setelah login berhasil
        menu = tampilkan_navigasi_sidebar()
        
        # Logika Menu
        if menu == "🚀 RUANG PRODUKSI": tampilkan_ruang_produksi()
        elif menu == "🧠 PINTAR AI LAB": tampilkan_ai_lab()
        elif menu == "⚡ QUICK PROMPT": tampilkan_quick_prompt()
        elif menu == "📋 TUGAS KERJA": tampilkan_tugas_kerja()
        elif menu == "⚡ KENDALI TIM": tampilkan_kendali_tim()

# --- BAGIAN PALING BAWAH ---
if __name__ == "__main__":
    utama()














