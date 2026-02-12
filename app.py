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
# Styling login → super minimal, centered, elegant dark mode
# ────────────────────────────────────────────────
st.markdown("""
    <style>
        /* Reset & centering */
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        }
        section.main {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 0 !important;
        }
        .st-emotion-cache-1wivap2 {
            max-width: 420px !important;
            margin: auto !important;
        }

        /* Login card */
        .login-card {
            background: #1e293b;
            border-radius: 16px;
            padding: 40px 36px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
            border: 1px solid #334155;
            width: 100%;
            max-width: 380px;
            text-align: center;
        }
        .login-title {
            color: #e2e8f0;
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 36px;
            letter-spacing: -0.5px;
        }
        .login-subtitle {
            color: #94a3b8;
            font-size: 15px;
            margin-bottom: 28px;
            line-height: 1.4;
        }

        /* Inputs */
        .stTextInput > div > div > input {
            background: #0f172a;
            color: #e2e8f0;
            border: 1px solid #475569;
            border-radius: 10px;
            padding: 14px 16px;
            font-size: 16px;
            transition: all 0.2s;
        }
        .stTextInput > div > div > input:focus {
            border-color: #60a5fa;
            box-shadow: 0 0 0 3px rgba(96,165,250,0.25);
            background: #1e293b;
        }
        .stTextInput > div > label {
            display: none !important;
        }

        /* Button */
        .stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #3b82f6, #60a5fa);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 14px;
            font-size: 16px;
            font-weight: 600;
            margin-top: 24px;
            transition: all 0.25s;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(59,130,246,0.4);
            background: linear-gradient(90deg, #2563eb, #3b82f6);
        }

        /* Alerts */
        .stAlert {
            border-radius: 10px;
            margin-top: 20px;
            background: #334155;
            color: #e2e8f0;
        }

        /* Hide unnecessary elements */
        footer, .stDeployButton, .reportview-container .main footer { display: none !important; }
        .st-emotion-cache-1y4p8pa { padding-top: 0 !important; }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Halaman Login (centered & minimal)
# ────────────────────────────────────────────────
if not st.session_state.logged_in:
    with st.container():
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        st.markdown('<div class="login-title">Generator Prompt</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Masuk untuk mulai membuat prompt konsisten</div>', unsafe_allow_html=True)
        
        username = st.text_input(
            label="Username",
            placeholder="Username",
            key="login_user",
            label_visibility="collapsed"
        )
        password = st.text_input(
            label="Password",
            type="password",
            placeholder="Password",
            key="login_pass",
            label_visibility="collapsed"
        )
        
        if st.button("Masuk"):
            if username in USERS and USERS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.login_time = datetime.now().isoformat()
                st.session_state.data = load_data()
                st.success(f"Selamat datang kembali, {username}", icon="✨")
                time.sleep(0.6)
                st.rerun()
            else:
                st.error("Username atau password salah", icon="🔒")
        
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

