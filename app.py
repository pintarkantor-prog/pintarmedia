# ==============================================================================
# BAGIAN 1: KONFIGURASI DAN DATABASE PENGGUNA
# ==============================================================================
import streamlit as st
from datetime import datetime, timedelta

DAFTAR_USER = {
    "dian": "QWERTY21ab", "icha": "udin99", "nissa": "tung22",
    "inggi": "udin33", "lisa": "tung66", "tamu": "123"
}

st.set_page_config(page_title="Pintar Media | AI Studio", layout="wide")

# ==============================================================================
# BAGIAN 2: SISTEM KEAMANAN & TAMPILAN LOGIN (AUTENTIKASI)
# ==============================================================================
def inisialisasi_keamanan():
    params = st.query_params
    if "auth" in params and params["auth"] == "true":
        if 'sudah_login' not in st.session_state:
            st.session_state.sudah_login = True
            st.session_state.user_aktif = params.get("user", "User")
            st.session_state.waktu_login = datetime.now()
    
    if 'sudah_login' not in st.session_state:
        st.session_state.sudah_login = False

def tampilkan_halaman_login():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_l, col_m, col_r = st.columns([1, 1.2, 1])
    
    with col_m:
        # Mengambil logo PINTAR.png dari root folder GitHub
        try:
            st.image("PINTAR.png", width=180)
        except:
            st.markdown("<h1 style='text-align: center;'>🎬</h1>", unsafe_allow_html=True)
        
        st.markdown("<h2 style='text-align: center; margin-top: -10px;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #484f58; font-size: 12px; margin-top: -15px;'>AI PRODUCTION STUDIO</p>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            u = st.text_input("Station Username").lower()
            p = st.text_input("Access Password", type="password")
            submit = st.form_submit_button("MASUK KE STATION", use_container_width=True)
            if submit:
                if u in DAFTAR_USER and DAFTAR_USER[u] == p:
                    st.session_state.sudah_login = True
                    st.session_state.user_aktif = u
                    st.session_state.waktu_login = datetime.now()
                    st.query_params.update({"auth": "true", "user": u})
                    st.rerun()
                else:
                    st.error("Username atau Password salah.")

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
    st.session_state.sudah_login = False
    st.session_state.user_aktif = ""
    st.query_params.clear()
    st.rerun()

# ==============================================================================
# BAGIAN 3: PENGATURAN TAMPILAN (CSS)
# ==============================================================================
def pasang_css_kustom():
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; color: #e0e0e0; }
        [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
        .streamlit-expanderHeader { background-color: #161b22 !important; border: 1px solid #30363d !important; border-radius: 8px !important; }
        div[data-baseweb="input"], div[data-baseweb="textarea"] { background-color: #161b22 !important; border: 1px solid #30363d !important; border-radius: 8px !important; }
        .status-footer { position: fixed; bottom: 20px; left: 20px; font-size: 10px; color: #484f58; text-transform: uppercase; font-family: monospace; }
        div[data-testid="stForm"] { border: none !important; padding: 0 !important; }
        @media (max-width: 1024px) {
            .main { display: none !important; }
            [data-testid="stSidebar"] { display: none !important; }
            .stApp::before { content: '⚠️ AKSES PC ONLY'; display: flex; justify-content: center; align-items: center; height: 100vh; color: white; background-color: #0e1117; }
        }
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# BAGIAN 4: NAVIGASI SIDEBAR
# ==============================================================================
def tampilkan_navigasi_sidebar():
    with st.sidebar:
        st.markdown("<br>", unsafe_allow_html=True)
        pilihan = st.radio("NAVIGASI", ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"])
        st.markdown("<br>"*12, unsafe_allow_html=True)
        if st.button("LOGOUT SYSTEM", use_container_width=True):
            proses_logout()
        user = st.session_state.get("user_aktif", "USER").upper()
        st.markdown(f'<div class="status-footer">STATION: {user}_SESSION<br>STATUS: AKTIF</div>', unsafe_allow_html=True)
    return pilihan

# ==============================================================================
# BAGIAN 5: MODUL-MODUL PENDUKUNG
# ==============================================================================
def tampilkan_ai_lab(): st.markdown("### 🧠 Pintar AI Lab"); st.info("Area riset.")
def tampilkan_quick_prompt(): st.markdown("### ⚡ Quick Prompt"); st.info("Generator kilat.")
def tampilkan_tugas_kerja(): st.markdown("### 📋 Tugas Kerja"); st.info("Antrian tim.")
def tampilkan_kendali_tim(): st.markdown("### ⚡ Kendali Tim"); st.info("Akses tim.")

# ==============================================================================
# BAGIAN 6: MODUL UTAMA - RUANG PRODUKSI
# ==============================================================================
def tampilkan_ruang_produksi():
    st.markdown("### 🚀 Ruang Produksi")
    st.write("---")
    with st.expander("👥 Karakter Utama & Penampilan Fisik", expanded=True):
        juml = st.number_input("Total Karakter", 1, 5, 2)
        cols = st.columns(juml)
        for i in range(juml):
            with cols[i]:
                st.text_input(f"Nama {i+1}", key=f"n_{i}")
                st.text_area(f"Ciri Fisik {i+1}", key=f"d_{i}", height=120)
    
    with st.expander("🟢 ADEGAN 1"):
        c1, c2 = st.columns([1, 2])
        with c1: st.text_input("Lokasi", key="loc1")
        with c2: st.text_area("Aksi", key="act1")

    if st.button("🚀 COMPILE MASTER PROMPT", use_container_width=True):
        st.success("Berhasil disusun!")

# ==============================================================================
# BAGIAN 7: PENGENDALI UTAMA (MAIN ROUTER)
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
