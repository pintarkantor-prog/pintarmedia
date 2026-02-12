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
# Login page FINAL: clean, no labels on top, rainbow logo, red button
# ────────────────────────────────────────────────
st.markdown("""
    <style>
        .stApp {
            background: #0a0e17;
        }
        .main > div:first-child {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 0;
            margin: 0;
        }
        .rainbow-title {
            font-size: 48px;
            font-weight: 900;
            background: linear-gradient(90deg, #ff00cc, #3333ff, #00ff99, #ffcc00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 50px;
            letter-spacing: -1px;
        }
        .form-box {
            background: #111827;
            border-radius: 16px;
            padding: 40px 32px;
            border: 1px solid #374151;
            box-shadow: 0 15px 40px rgba(0,0,0,0.6);
            width: 100%;
            max-width: 380px;
        }
        .stTextInput > div > div > input {
            background: #1f2937;
            color: #f3f4f6;
            border: 1px solid #4b5563;
            border-radius: 10px;
            padding: 14px 16px;
            font-size: 16px;
            margin-bottom: 16px;
            width: 100%;
        }
        .stTextInput > div > div > input:focus {
            border-color: #6366f1;
            box-shadow: 0 0 0 3px rgba(99,102,241,0.25);
        }
        .stButton > button {
            width: 100%;
            background: #ef4444;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 14px;
            font-size: 16px;
            font-weight: 600;
            margin-top: 20px;
        }
        .stButton > button:hover {
            background: #dc2626;
        }
        .footer-text {
            color: #6b7280;
            font-size: 14px;
            margin-top: 32px;
            text-align: center;
        }
        footer {display: none !important;}
        section[data-testid="stSidebar"] {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# --- 2. LAYAR LOGIN ---
if 'active_user' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        # Kosongkan ruang atas supaya tidak memanjang
        st.markdown("<div style='height: 10vh;'></div>", unsafe_allow_html=True)

        # Centering lebih rapat
        _, col_login, _ = st.columns([2.0, 1.0, 2.0])  # lebih ramping dari 1.8

        with col_login:
            # Logo gambar atau fallback rainbow
            try:
                st.image("PINTAR.png", use_container_width=True)
            except:
                st.markdown("""
                    <h1 style='text-align: center; font-size: 42px; font-weight: 900;
                    background: linear-gradient(90deg, #ff00cc, #3333ff, #00ff99, #ffcc00);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                    margin: 0 0 30px 0;'>
                        PINTAR MEDIA
                    </h1>
                """, unsafe_allow_html=True)

            with st.form("login_form", clear_on_submit=False):
                # Input clean tanpa label tebal
                default_user = st.query_params.get("u", "")
                user_input = st.text_input("", value=default_user, placeholder="Username...", key="user_input")
                pass_input = st.text_input("", type="password", placeholder="Password...", key="pass_input")

                # Spasi kecil saja
                st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

                submit_button = st.form_submit_button(
                    "MASUK KE SISTEM 🚀",
                    use_container_width=True,
                    type="primary"  # biasanya merah/biru tergantung theme, bisa di-CSS kalau perlu
                )

            if submit_button:
                user_clean = user_input.lower().strip()
                if user_clean in USERS and USERS[user_clean] == pass_input:  # pakai USERS dari kode awalmu
                    st.session_state.active_user = user_clean
                    st.session_state.login_time = time.time()
                    st.session_state.username = user_clean.upper()  # jembatan tugas kerja

                    # Bersihkan & set query params
                    st.query_params.clear()
                    st.query_params["u"] = user_clean

                    placeholder.empty()
                    with placeholder.container():
                        st.markdown("<div style='height: 30vh;'></div>", unsafe_allow_html=True)
                        st.markdown(
                            "<h2 style='text-align: center; color: #10b981;'>AKSES DITERIMA! ✅</h2>",
                            unsafe_allow_html=True
                        )
                        st.markdown(
                            f"<h3 style='text-align: center; color: #e2e8f0;'>Selamat bekerja, {user_clean.capitalize()}!</h3>",
                            unsafe_allow_html=True
                        )
                        time.sleep(1.2)
                    st.rerun()
                else:
                    st.error("Username atau password salah", icon="🚫")

            # Footer kecil
            st.markdown(
                "<p style='text-align: center; color: #6b7280; font-size: 13px; margin-top: 24px;'>"
                "Secure Access - PINTAR MEDIA</p>",
                unsafe_allow_html=True
            )

    st.stop()

# --- 3. PROTEKSI SESI (AUTO-LOGOUT 10 JAM) ---
if 'active_user' in st.session_state and 'login_time' in st.session_state:
    selisih_detik = time.time() - st.session_state.login_time
    if selisih_detik > (10 * 60 * 60):
        st.query_params.clear()
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
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








