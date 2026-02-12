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
def is_mobile():
    ua = st.context.headers.get("User-Agent", "").lower()
    mobile_keywords = ["mobile", "android", "iphone", "ipad", "ipod"]
    return any(kw in ua for kw in mobile_keywords)

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
# Halaman Login
# ────────────────────────────────────────────────
if not st.session_state.logged_in:
    st.title("Login - Generator Prompt")

    # Batasi akses hanya dari HP (opsional – bisa di-comment jika tidak ingin)
    if not is_mobile():
        st.warning("Aplikasi ini hanya dapat diakses dari perangkat mobile (HP).")
        st.stop()

    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Masuk"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.login_time = datetime.now().isoformat()
            # Load data saat login
            st.session_state.data = load_data()
            st.success(f"Selamat datang, {username}!")
            time.sleep(0.8)
            st.rerun()
        else:
            st.error("Username atau password salah.")
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

    # Load dari session (sudah di-load saat login)
    scenes = st.session_state.data.get("scenes", [])

    col1, col2 = st.columns([3,1])
    with col1:
        tema = st.text_input("Tema / Karakter Utama / Gaya Visual", 
                             value="Gadis cyberpunk berambut neon di kota malam hujan", 
                             key="tema_utama")
        style = st.text_input("Style prompt (contoh: cinematic, ultra detailed, 8k)", 
                              value="cinematic, highly detailed, moody lighting, 8k", 
                              key="style_global")

    if st.button("Generate 10 Adegan Otomatis"):
        if tema.strip():
            base_prompt = f"{tema}, {style}"
            new_scenes = [f"Adegan {i+1}: {base_prompt} – variasi {i+1}" for i in range(10)]
            scenes.extend(new_scenes)
            st.session_state.data["scenes"] = scenes
            save_data(st.session_state.data)
            st.success("10 adegan berhasil ditambahkan!")
        else:
            st.warning("Masukkan tema terlebih dahulu.")

    # Tambah manual
    with st.expander("➕ Tambah Adegan Manual"):
        manual_prompt = st.text_area("Tulis prompt adegan", height=100)
        if st.button("Tambahkan Adegan"):
            if manual_prompt.strip():
                scenes.append(manual_prompt)
                st.session_state.data["scenes"] = scenes
                save_data(st.session_state.data)
                st.success("Adegan ditambahkan!")
            else:
                st.warning("Prompt tidak boleh kosong.")

    # Tampilkan semua adegan
    st.markdown("### Daftar Adegan Saat Ini")
    if scenes:
        for idx, scene in enumerate(scenes):
            with st.container():
                col_a, col_b = st.columns([8,2])
                col_a.markdown(f"**Adegan {idx+1}**  \n{scene}")
                if col_b.button("🗑️", key=f"del_{idx}"):
                    scenes.pop(idx)
                    st.session_state.data["scenes"] = scenes
                    save_data(st.session_state.data)
                    st.rerun()
    else:
        st.info("Belum ada adegan. Generate atau tambah manual.")

    if st.button("Simpan Data Sekarang"):
        save_data(st.session_state.data)
        st.success("Data tersimpan!")

# ────────────────────────────────────────────────
# Placeholder menu lain
# ────────────────────────────────────────────────
elif page == "🧠 PINTAR AI LAB":
    st.header("PINTAR AI LAB")
    st.write("Masukkan premis/alur cerita → AI bantu kembangkan ide cerita + twist")
    premis = st.text_area("Premis utama cerita")
    if st.button("Generate Ide"):
        st.info("Fitur ini akan terhubung ke model AI nanti (placeholder)")

elif page == "⚡ QUICK PROMPT":
    st.header("QUICK PROMPT")
    st.write("Buat satu prompt gambar atau video cepat")
    quick = st.text_area("Deskripsi gambar/video")
    if st.button("Buat Prompt"):
        st.code(quick or "Belum ada deskripsi", language="text")

elif page == "📋 TUGAS KERJA":
    st.header("TUGAS KERJA – Staff")
    st.write("Area untuk catat tugas harian staff (akan dikembangkan)")

elif page == "⚡ KENDALI TIM":
    st.header("KENDALI TIM")
    st.write("Monitor progress & kinerja staff (placeholder)")
