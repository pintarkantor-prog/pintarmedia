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
# BAGIAN 2: SISTEM KEAMANAN & TAMPILAN LOGIN (AUTENTIKASI)
# ==============================================================================
def inisialisasi_keamanan():
    if 'sudah_login' not in st.session_state:
        st.session_state.sudah_login = False
    
    params = st.query_params
    if "auth" in params and params["auth"] == "true":
        if not st.session_state.sudah_login:
            st.session_state.sudah_login = True
            st.session_state.user_aktif = params.get("user", "User")
            st.session_state.waktu_login = datetime.now()

def proses_login(user, pwd):
    """Fungsi mandiri untuk validasi login (DIKEMBALIKAN)"""
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
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.form("login_station"):
            u = st.text_input("Username", placeholder="Username...", key="login_user").lower()
            p = st.text_input("Password", type="password", placeholder="Password...", key="login_pass")
            st.markdown("<br>", unsafe_allow_html=True)
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
        div[data-testid="stForm"] { border: 1px solid #30363d !important; border-radius: 12px !important; padding: 20px !important; }
        button[kind="primaryFormSubmit"] { background-color: #10b981 !important; color: white !important; border: none !important; height: 45px !important; font-weight: bold !important; }
        div[data-baseweb="input"], div[data-baseweb="textarea"] { background-color: #1d2127 !important; border: 1px solid #30363d !important; border-radius: 8px !important; }
        .status-footer { position: fixed; bottom: 20px; left: 20px; font-size: 10px; color: #484f58; text-transform: uppercase; font-family: monospace; }
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
        pilihan = st.radio("NAVIGASI WORKSPACE", ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"])
        st.markdown("<br>"*12, unsafe_allow_html=True)
        if st.button("LOGOUT SYSTEM", use_container_width=True):
            proses_logout()
        user = st.session_state.get("user_aktif", "USER").upper()
        st.markdown(f'<div class="status-footer">STATION: {user}_SESSION<br>STATUS: AKTIF</div>', unsafe_allow_html=True)
    return pilihan

# ==============================================================================
# BAGIAN 5: MODUL-MODUL PENDUKUNG (DIKEMBALIKAN DETAIL)
# ==============================================================================
def tampilkan_ai_lab(): 
    st.markdown("### 🧠 Pintar AI Lab")
    st.info("Area riset prompt. Gunakan modul ini untuk bereksperimen dengan perintah AI baru.")

def tampilkan_quick_prompt(): 
    st.markdown("### ⚡ Quick Prompt")
    st.info("Generator kilat. Masukkan ide singkat untuk mendapatkan prompt instan.")

def tampilkan_tugas_kerja(): 
    st.markdown("### 📋 Tugas Kerja")
    st.info("Daftar antrian produksi. Pastikan setiap anggota tim menyelesaikan tugas sesuai jadwal.")

def tampilkan_kendali_tim(): 
    st.markdown("### ⚡ Kendali Tim")
    st.info("Panel administrasi untuk mengatur akses station dan pembagian beban kerja.")

# ==============================================================================
# BAGIAN 6: MODUL UTAMA - RUANG PRODUKSI (DIKEMBALIKAN FULL)
# ==============================================================================
def tampilkan_ruang_produksi():
    st.markdown("### 🚀 Ruang Produksi")
    st.write("---")
    
    with st.expander("👥 Karakter Utama & Penampilan Fisik", expanded=True):
        juml = st.number_input("Total Karakter", 1, 5, 2)
        cols = st.columns(juml)
        for i in range(juml):
            with cols[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                st.text_input(f"Nama Karakter {i+1}", key=f"n_{i}", placeholder="Nama...")
                st.text_area(f"Deskripsi Fisik {i+1}", key=f"d_{i}", height=150, placeholder="Detail fisik...")

    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.expander("🟢 ADEGAN 1", expanded=True):
        st.text_input("Lokasi Adegan 1", key="loc1", placeholder="Lokasi...")
        st.text_area("Aksi & Narasi Adegan 1", key="act1", height=200, placeholder="Narasi...")

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("🎬 ADEGAN 2", expanded=True):
        st.text_input("Lokasi Adegan 2", key="loc2", placeholder="Lokasi...")
        st.text_area("Aksi & Narasi Adegan 2", key="act2", height=200, placeholder="Narasi...")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 COMPILE MASTER PROMPT", use_container_width=True):
        st.success("Prompt berhasil disusun!")

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
