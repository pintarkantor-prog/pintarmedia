# ==============================================================================
# BAGIAN 1: KONFIGURASI DAN DATABASE PENGGUNA
# ==============================================================================
import streamlit as st
from datetime import datetime, timedelta

# Daftar akun resmi Pintar Media
DAFTAR_USER = {
    "dian": "QWERTY21ab", "icha": "udin99", "nissa": "tung22",
    "inggi": "udin33", "lisa": "tung66", "tamu": "123"
}

st.set_page_config(page_title="Pintar Media | AI Studio", layout="wide")

# ==============================================================================
# BAGIAN 2: SISTEM KEAMANAN (LOGIN, LOGOUT, DAN SESI 10 JAM)
# ==============================================================================
def inisialisasi_sesi():
    """Menyiapkan variabel sesi agar tidak hilang saat refresh"""
    if 'sudah_login' not in st.session_state:
        st.session_state.sudah_login = False
    if 'user_aktif' not in st.session_state:
        st.session_state.user_aktif = ""
    if 'waktu_login' not in st.session_state:
        st.session_state.waktu_login = None

def cek_autentikasi():
    """Logika pengecekan login dan batas waktu 10 jam"""
    if st.session_state.sudah_login and st.session_state.waktu_login:
        # Hitung selisih waktu
        durasi_aktif = datetime.now() - st.session_state.waktu_login
        if durasi_aktif > timedelta(hours=10):
            proses_logout()
            st.warning("Sesi Anda berakhir setelah 10 jam. Silakan login kembali.")
            return False
        return True
    return False

def proses_login(user, pwd):
    if user in DAFTAR_USER and DAFTAR_USER[user] == pwd:
        st.session_state.sudah_login = True
        st.session_state.user_aktif = user
        st.session_state.waktu_login = datetime.now()
        st.rerun()
    else:
        st.error("Credential salah. Silakan coba lagi.")

def proses_logout():
    st.session_state.sudah_login = False
    st.session_state.user_aktif = ""
    st.session_state.waktu_login = None
    st.rerun()

# ==============================================================================
# BAGIAN 3: PENGATURAN TAMPILAN (CSS) DAN PROTEKSI PC
# ==============================================================================
def pasang_css_kustom():
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; color: #e0e0e0; }
        [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
        .streamlit-expanderHeader { background-color: #161b22 !important; border: 1px solid #30363d !important; border-radius: 8px !important; }
        div[data-baseweb="input"], div[data-baseweb="textarea"] { background-color: #161b22 !important; border: 1px solid #30363d !important; border-radius: 8px !important; }
        .status-footer { position: fixed; bottom: 20px; left: 20px; font-size: 10px; color: #484f58; text-transform: uppercase; font-family: monospace; }
        
        @media (max-width: 1024px) {
            .main { display: none !important; }
            [data-testid="stSidebar"] { display: none !important; }
            .stApp::before { 
                content: '⚠️ AKSES TERBATAS: Gunakan perangkat PC/Desktop.'; 
                display: flex; justify-content: center; align-items: center; 
                height: 100vh; color: white; background-color: #0e1117; padding: 40px; text-align: center;
            }
        }
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# BAGIAN 4: NAVIGASI SIDEBAR
# ==============================================================================
def tampilkan_navigasi_sidebar():
    with st.sidebar:
        st.markdown("<br>", unsafe_allow_html=True)
        pilihan = st.radio(
            "NAVIGASI WORKSPACE", 
            ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"]
        )
        st.markdown("<br>"*12, unsafe_allow_html=True)
        if st.button("KELUAR SISTEM", use_container_width=True):
            proses_logout()
        
        user = st.session_state.user_aktif.upper()
        tgl = st.session_state.waktu_login.strftime('%d.%m.%y')
        st.markdown(f'<div class="status-footer">STATION: {user}_SESSION<br>AKTIF SEJAK: {tgl}</div>', unsafe_allow_html=True)
    return pilihan

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
    
    with st.expander("👥 Karakter Utama & Penampilan Fisik", expanded=True):
        jumlah = st.number_input("Total Karakter", 1, 5, 2)
        cols = st.columns(jumlah)
        for i in range(jumlah):
            with cols[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                st.text_input(f"Nama", key=f"n_{i}")
                st.text_area(f"Ciri Fisik", key=f"d_{i}", height=120)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🟢 ADEGAN 1"):
        c1, c2 = st.columns([1, 2])
        with c1: st.text_input("Lokasi Adegan 1", key="loc1")
        with c2: st.text_area("Aksi Adegan 1", key="act1")

    if st.button("🚀 SUSUN MASTER PROMPT", use_container_width=True):
        st.success("Data berhasil diproses!")

# ==============================================================================
# BAGIAN 7: PENGENDALI UTAMA (MAIN ROUTER)
# ==============================================================================
def utama():
    inisialisasi_sesi()
    pasang_css_kustom()
    
    if not cek_autentikasi():
        st.markdown("<br><br>", unsafe_allow_html=True)
        col_l, col_m, col_r = st.columns([1, 1.2, 1])
        with col_m:
            st.markdown("<h2 style='text-align: center;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
            u = st.text_input("Username").lower()
            p = st.text_input("Password", type="password")
            if st.button("MASUK", use_container_width=True):
                proses_login(u, p)
    else:
        menu = tampilkan_navigasi_sidebar()
        if menu == "🚀 RUANG PRODUKSI":
            tampilkan_ruang_produksi()
        elif menu == "🧠 PINTAR AI LAB":
            tampilkan_ai_lab()
        elif menu == "⚡ QUICK PROMPT":
            tampilkan_quick_prompt()
        elif menu == "📋 TUGAS KERJA":
            tampilkan_tugas_kerja()
        elif menu == "⚡ KENDALI TIM":
            tampilkan_kendali_tim()

if __name__ == "__main__":
    utama()
