import streamlit as st
import uuid
import socket
import time
from datetime import timedelta
from modules import database

# --- CONFIG HALAMAN ---
st.set_page_config(page_title="PINTAR MEDIA v2.0", page_icon="🖼️", layout="wide")

# Inisialisasi ID Browser Unik (Dibuat sekali per buka browser)
if "browser_session_id" not in st.session_state:
    st.session_state["browser_session_id"] = str(uuid.uuid4())

if "is_login" not in st.session_state:
    st.session_state["is_login"] = False

# CSS Sembunyikan Sidebar jika belum login
if not st.session_state["is_login"]:
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

def proses_logout(pesan=None):
    for key in list(st.session_state.keys()):
        if key != "browser_session_id":
            del st.session_state[key]
    if pesan:
        st.toast(pesan, icon="⚠️")
        time.sleep(2)
    st.rerun()

# --- TAMPILAN LOGIN ---
def halaman_login():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1.2, 1, 1.2])
    
    with col2:
        st.image("PINTAR.png", use_container_width=True)
        st.markdown("<h2 style='text-align:center;'>🔐 PINTAR SECURE LOGIN</h2>", unsafe_allow_html=True)
        
        with st.form("login_station"):
            u = st.text_input("Username", placeholder="Masukkan Nama...").strip().upper()
            p = st.text_input("Password", type="password", placeholder="Password...")
            submit = st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True)
            
            if submit:
                df_staff = database.ambil_data("Staff")
                # Cari user yang cocok (Case Sensitive untuk password)
                user_row = df_staff[(df_staff['Nama'] == u) & (df_staff['Password'] == p)]
                
                if not user_row.empty:
                    level = user_row.iloc[0]['Level'].upper()
                    hostname_pc = socket.gethostname()

                    # 1. CEK WHITELIST PC (Kecuali Dian/Owner)
                    if level != "OWNER":
                        if not database.cek_pc_whitelist(hostname_pc):
                            st.error(f"Akses Ditolak! PC ({hostname_pc}) Tidak Terdaftar.")
                            return

                    # 2. UPDATE SESI (Kick device lain)
                    database.update_sesi(u, st.session_state["browser_session_id"])
                    
                    # 3. SET SESSION STATE
                    st.session_state["is_login"] = True
                    st.session_state["user_aktif"] = u
                    st.session_state["user_level"] = level
                    st.session_state["waktu_login"] = database.ambil_waktu_sekarang()
                    st.success(f"Selamat Datang, {u}!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Username atau Password salah!")

# --- MONITORING KEAMANAN REAL-TIME ---
if st.session_state["is_login"]:
    # A. Cek Durasi 10 Jam (WIB)
    waktu_sekarang = database.ambil_waktu_sekarang()
    durasi = waktu_sekarang - st.session_state["waktu_login"]
    
    if durasi > timedelta(hours=10):
        proses_logout("Sesi habis (Maksimal 10 Jam).")

    # B. Cek Single Device (Anti-Sharing)
    if not database.cek_sesi_valid(st.session_state["user_aktif"], st.session_state["browser_session_id"]):
        proses_logout("Akun login di perangkat lain. Sesi ini diputus!")

# --- JALANKAN APLIKASI ---
if not st.session_state["is_login"]:
    halaman_login()
else:
    # Sidebar Info
    st.sidebar.image("PINTAR.png", width=100)
    st.sidebar.write(f"👤 **{st.session_state['user_aktif']}**")
    st.sidebar.write(f"🛡️ Level: {st.session_state['user_level']}")
    
    if st.sidebar.button("Keluar (Logout)"):
        proses_logout()

    # Dashboard Utama
    st.title("🚀 Dashboard PINTAR MEDIA v2.0")
    st.write(f"Waktu Login Anda (WIB): {st.session_state['waktu_login'].strftime('%H:%M:%S')}")
    
    sisa = timedelta(hours=10) - (database.ambil_waktu_sekarang() - st.session_state["waktu_login"])
    st.info(f"Sisa waktu sesi Anda: {str(sisa).split('.')[0]}")
