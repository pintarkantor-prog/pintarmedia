# ==============================================================================
# BAGIAN 1: KONFIGURASI DAN DATABASE PENGGUNA
# ==============================================================================
import streamlit as st
from datetime import datetime, timedelta
from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(password="pintarmedia_kunci_rahasia_2026")
if not cookies.ready():
    st.stop()

DAFTAR_USER = {
    "dian": "QWERTY21ab", "icha": "udin99", "nissa": "tung22",
    "inggi": "udin33", "lisa": "tung66", "tamu": "123"
}

st.set_page_config(page_title="Pintar Media | AI Studio", layout="wide")

# ==============================================================================
# BAGIAN 2: SISTEM KEAMANAN (LOGIN, LOGOUT, DAN SESI)
# ==============================================================================
def cek_autentikasi():
    sudah_login = cookies.get("sudah_login") == "True"
    waktu_login_str = cookies.get("waktu_login")
    if sudah_login and waktu_login_str:
        waktu_login_dt = datetime.fromisoformat(waktu_login_str)
        if datetime.now() - waktu_login_dt > timedelta(hours=10):
            proses_logout()
            st.rerun()
    return sudah_login

def proses_login(user, pwd):
    if user in DAFTAR_USER and DAFTAR_USER[user] == pwd:
        cookies["sudah_login"] = "True"
        cookies["user_aktif"] = user
        cookies["waktu_login"] = datetime.now().isoformat()
        cookies.save()
        st.rerun()
    else:
        st.error("Login gagal.")

def proses_logout():
    cookies.delete("sudah_login")
    cookies.delete("user_aktif")
    cookies.delete("waktu_login")
    cookies.save()
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
        .streamlit-expanderContent { background-color: #0d1117 !important; }
        div[data-baseweb="input"], div[data-baseweb="textarea"] { background-color: #161b22 !important; border: 1px solid #30363d !important; border-radius: 8px !important; }
        .status-footer { position: fixed; bottom: 20px; left: 20px; font-size: 10px; color: #484f58; text-transform: uppercase; font-family: monospace; }
        @media (max-width: 1024px) {
            .main { display: none !important; }
            [data-testid="stSidebar"] { display: none !important; }
            .stApp::before { content: '⚠️ AKSES TERBATAS: GUNAKAN PC'; display: flex; justify-content: center; align-items: center; height: 100vh; color: white; background-color: #0e1117; }
        }
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# BAGIAN 4: NAVIGASI SIDEBAR
# ==============================================================================
def tampilkan_navigasi_sidebar():
    with st.sidebar:
        st.markdown("<br>", unsafe_allow_html=True)
        pilihan_menu = st.radio(
            "NAVIGASI WORKSPACE", 
            ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"]
        )
        st.markdown("<br>"*12, unsafe_allow_html=True)
        if st.button("KELUAR SISTEM", use_container_width=True):
            proses_logout()
        nama_user = cookies.get("user_aktif", "TIDAK DIKENAL")
        st.markdown(f'<div class="status-footer">STATION: {nama_user.upper()}_SESSION<br>STATUS: AKTIF</div>', unsafe_allow_html=True)
    return pilihan_menu

# ==============================================================================
# BAGIAN 5: MODUL-MODUL PENDUKUNG
# ==============================================================================
def tampilkan_ai_lab():
    st.markdown("### 🧠 Pintar AI Lab")
    st.info("Area riset prompt dan eksperimen.")

def tampilkan_quick_prompt():
    st.markdown("### ⚡ Quick Prompt")
    st.info("Generator prompt kilat.")

def tampilkan_tugas_kerja():
    st.markdown("### 📋 Tugas Kerja")
    st.info("Monitoring antrian produksi tim.")

def tampilkan_kendali_tim():
    st.markdown("### ⚡ Kendali Tim")
    st.info("Pengaturan akses dan koordinasi.")

# ==============================================================================
# BAGIAN 6: MODUL UTAMA - RUANG PRODUKSI
# ==============================================================================
def tampilkan_ruang_produksi():
    st.markdown("### 🚀 Ruang Produksi")
    st.write("---")
    
    # SEKSI KARAKTER
    with st.expander("👥 Karakter Utama & Penampilan Fisik", expanded=True):
        jumlah = st.number_input("Total Karakter", 1, 5, 2)
        cols = st.columns(jumlah)
        for i in range(jumlah):
            with cols[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                st.text_input(f"Nama", key=f"n_{i}")
                st.text_area(f"Ciri Fisik", key=f"d_{i}", height=120)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # SEKSI ADEGAN
    with st.expander("🟢 ADEGAN 1"):
        c1, c2 = st.columns([1, 2])
        with c1: st.text_input("Lokasi Adegan 1", key="loc1")
        with c2: st.text_area("Aksi Adegan 1", key="act1")

    if st.button("🚀 COMPILE MASTER PROMPT", use_container_width=True):
        st.success("Prompt berhasil dikompilasi!")

# ==============================================================================
# BAGIAN 7: PENGENDALI UTAMA (MAIN ROUTER)
# ==============================================================================
def utama():
    pasang_css_kustom()
    
    if not cek_autentikasi():
        st.markdown("<br><br>", unsafe_allow_html=True)
        col_kiri, col_tengah, col_kanan = st.columns([1, 1.2, 1])
        with col_tengah:
            st.markdown("<h2 style='text-align: center;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
            u_input = st.text_input("Username").lower()
            p_input = st.text_input("Password", type="password")
            if st.button("MASUK", use_container_width=True):
                proses_login(u_input, p_input)
    else:
        menu_aktif = tampilkan_navigasi_sidebar()
        
        if menu_aktif == "🚀 RUANG PRODUKSI":
            tampilkan_ruang_produksi()
        elif menu_aktif == "🧠 PINTAR AI LAB":
            tampilkan_ai_lab()
        elif menu_aktif == "⚡ QUICK PROMPT":
            tampilkan_quick_prompt()
        elif menu_aktif == "📋 TUGAS KERJA":
            tampilkan_tugas_kerja()
        elif menu_aktif == "⚡ KENDALI TIM":
            tampilkan_kendali_tim()

if __name__ == "__main__":
    utama()

