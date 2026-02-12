import streamlit as st
import json
import os
import time
from datetime import datetime, timedelta

# ────────────────────────────────────────────────
# KONFIGURASI
# ────────────────────────────────────────────────
USERS = {
    "dian": "QWERTY21ab",
    "icha": "udin99",
    "nissa": "tung22",
    "inggi": "udin11",
    "lisa": "tung55",
    "tamu": "tamu123",
}

AUTO_LOGOUT_HOURS = 10
DATA_FILE = "produksi_data.json"

# ────────────────────────────────────────────────
# Fungsi bantu
# ────────────────────────────────────────────────
def is_desktop():
    ua = st.context.headers.get("User-Agent", "").lower()
    mobile_keywords = ["mobile", "android", "iphone", "ipad", "ipod", "tablet", "kindle", "silk"]
    return not any(kw in ua for kw in mobile_keywords)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"scenes": [], "last_updated": None}

def save_data(data):
    data["last_updated"] = datetime.now().isoformat()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ────────────────────────────────────────────────
# Inisialisasi session state
# ────────────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.login_time = None
    st.session_state.data = {"scenes": []}

# ────────────────────────────────────────────────
# Cek auto logout
# ────────────────────────────────────────────────
if st.session_state.logged_in and st.session_state.login_time:
    login_dt = datetime.fromisoformat(st.session_state.login_time)
    if datetime.now() - login_dt > timedelta(hours=AUTO_LOGOUT_HOURS):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.login_time = None
        st.rerun()

# ────────────────────────────────────────────────
# Cek device (hanya PC boleh akses)
# ────────────────────────────────────────────────
if not is_desktop():
    st.title("Akses Ditolak")
    st.error("Aplikasi ini **hanya boleh diakses dari PC / Desktop**.")
    st.warning("Gunakan komputer/laptop. HP, tablet, atau perangkat mobile diblokir.")
    st.info("Alasan: Pengalaman optimal & keamanan workflow produksi.")
    st.stop()

# ────────────────────────────────────────────────
# Styling login elegan, simpel, compact
# ────────────────────────────────────────────────
st.markdown("""
    <style>
        .login-box {
            max-width: 380px;
            margin: 80px auto 0 auto;
            padding: 40px 32px;
            background: white;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.12);
            text-align: center;
        }
        .login-title {
            font-size: 26px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 32px;
        }
        .stTextInput > div > div > input {
            border: 1px solid #d1d5db;
            border-radius: 10px;
            padding: 14px 16px;
            font-size: 16px;
            background: #f9fafb;
        }
        .stTextInput > div > div > input:focus {
            border-color: #3b82f6;
            box-shadow: 0 0 0 3px rgba(59,130,246,0.2);
        }
        .stButton > button {
            width: 100%;
            background: #3b82f6;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 14px;
            font-size: 16px;
            font-weight: 600;
            margin-top: 20px;
            transition: all 0.2s;
        }
        .stButton > button:hover {
            background: #2563eb;
        }
        .stAlert {
            border-radius: 10px;
            margin-top: 16px;
        }
        .main > div {padding-top: 0 !important;}
        footer {visibility: hidden;}
        section[data-testid="stSidebar"] {background-color: #f8fafc;}
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Halaman Login
# ────────────────────────────────────────────────
if not st.session_state.logged_in:
    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        
        st.markdown('<div class="login-title">Generator Prompt</div>', unsafe_allow_html=True)
        
        username = st.text_input("", placeholder="Username", key="login_user", label_visibility="collapsed")
        password = st.text_input("", type="password", placeholder="Password", key="login_pass", label_visibility="collapsed")
        
        if st.button("Masuk"):
            if username in USERS and USERS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.login_time = datetime.now().isoformat()
                st.session_state.data = load_data()
                st.success(f"Selamat datang, {username}!", icon="👋")
                time.sleep(0.7)
                st.rerun()
            else:
                st.error("Username atau password salah", icon="🚫")
        
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ────────────────────────────────────────────────
# Sidebar & Logout
# ────────────────────────────────────────────────
st.sidebar.title(f"Halo, {st.session_state.username}")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.login_time = None
    st.rerun()

st.sidebar.markdown(f"**Sisa waktu sesi:** ~{AUTO_LOGOUT_HOURS} jam sejak login")
st.sidebar.markdown("---")

page = st.sidebar.radio("Menu", [
    "🚀 RUANG PRODUKSI",
    "🧠 PINTAR AI LAB",
    "⚡ QUICK PROMPT",
    "📋 TUGAS KERJA",
    "⚡ KENDALI TIM"
])

# ────────────────────────────────────────────────
# RUANG PRODUKSI
# ────────────────────────────────────────────────
if page == "🚀 RUANG PRODUKSI":
    st.header("RUANG PRODUKSI – Generator 10 Adegan Konsisten")

    scenes = st.session_state.data.get("scenes", [])

    col1, col2 = st.columns([3,1])
    with col1:
        tema = st.text_input("Tema / Karakter Utama / Gaya Visual", 
                             value="Gadis cyberpunk berambut neon di kota malam hujan")
        style = st.text_input("Style prompt (contoh: cinematic, ultra detailed, 8k)", 
                              value="cinematic, highly detailed, moody lighting, 8k")

    if st.button("Generate 10 Adegan Otomatis"):
        if tema.strip():
            base_prompt = f"{tema}, {style}"
            new_scenes = [f"Adegan {i+1}: {base_prompt} – variasi {i+1}" for i in range(10)]
            scenes.extend(new_scenes)
            st.session_state.data["scenes"] = scenes
            save_data(st.session_state.data)
            st.success("10 adegan berhasil ditambahkan!")
            st.rerun()
        else:
            st.warning("Masukkan tema terlebih dahulu.")

    with st.expander("➕ Tambah Adegan Manual"):
        manual_prompt = st.text_area("Tulis prompt adegan", height=100)
        if st.button("Tambahkan Adegan"):
            if manual_prompt.strip():
                scenes.append(manual_prompt)
                st.session_state.data["scenes"] = scenes
                save_data(st.session_state.data)
                st.success("Adegan ditambahkan!")
                st.rerun()
            else:
                st.warning("Prompt tidak boleh kosong.")

    st.markdown("### Daftar Adegan Saat Ini")
    if scenes:
        for idx, scene in enumerate(scenes):
            with st.container(border=True):
                col_a, col_b = st.columns([8,2])
                col_a.markdown(f"**Adegan {idx+1}**  \n{scene}")
                if col_b.button("🗑️ Hapus", key=f"del_{idx}"):
                    scenes.pop(idx)
                    st.session_state.data["scenes"] = scenes
                    save_data(st.session_state.data)
                    st.rerun()
    else:
        st.info("Belum ada adegan. Generate atau tambah manual dulu.")

    if st.button("💾 Simpan Data Sekarang"):
        save_data(st.session_state.data)
        st.success("Data tersimpan!")

# ────────────────────────────────────────────────
# Menu lain (placeholder)
# ────────────────────────────────────────────────
elif page == "🧠 PINTAR AI LAB":
    st.header("🧠 PINTAR AI LAB")
    st.write("Masukkan premis atau alur cerita → AI bantu kembangkan ide + twist")
    premis = st.text_area("Premis utama cerita")
    if st.button("Generate Ide"):
        st.info("(Fitur AI akan ditambahkan nanti – saat ini placeholder)")

elif page == "⚡ QUICK PROMPT":
    st.header("⚡ QUICK PROMPT")
    st.write("Buat satu prompt gambar atau video dengan cepat")
    quick = st.text_area("Deskripsi gambar / video")
    if st.button("Buat Prompt"):
        if quick.strip():
            st.code(quick, language="text")
        else:
            st.warning("Masukkan deskripsi dulu")

elif page == "📋 TUGAS KERJA":
    st.header("📋 TUGAS KERJA – Staff")
    st.write("Area untuk mencatat tugas harian staff (dalam pengembangan)")

elif page == "⚡ KENDALI TIM":
    st.header("⚡ KENDALI TIM")
    st.write("Monitor progress & kinerja tim (placeholder)")
