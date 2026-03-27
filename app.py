import streamlit as st
import uuid
import socket
import time
import os # Tambahkan ini untuk cek file
from datetime import timedelta
from modules import database

# --- FUNGSI PANGGIL CSS ---
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.error(f"File {file_name} tidak ditemukan!")

# --- EKSEKUSI PANGGILAN ---
# Pastikan jalurnya benar: folder assets / file style.css
local_css("assets/style.css")

# --- CONFIG HALAMAN ---
st.set_page_config(page_title="PINTAR MEDIA | Studio", layout="wide")

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

# --- TAMPILAN LOGIN (Wajah Lama, Mesin Baru) ---
def halaman_login():
    with st.container():
        st.markdown("<br><br>", unsafe_allow_html=True)
        col_l, col_m, col_r = st.columns([1.5, 1, 1.5]) 
        
        with col_m:
            try:
                st.image("PINTAR.png", use_container_width=True)
            except:
                st.markdown("<h2 style='text-align:center;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
            
            # Form Login Station
            with st.form("login_station", clear_on_submit=False):
                u = st.text_input("Username", placeholder="Username...", key="input_u").strip().upper()
                p = st.text_input("Password", type="password", placeholder="Password...", key="input_p")
                submit = st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True)
                
                if submit:
                    if u and p:
                        # --- AMBIL DATA STAFF ---
                        df_staff = database.ambil_data("Staff")
                        
                        # Filter (Pastikan Nama di DB besar semua kalau kamu pakai .upper() di input)
                        user_row = df_staff[(df_staff['Nama'] == u) & (df_staff['Password'] == p)]
                        
                        if not user_row.empty:
                            user_data = user_row.iloc[0]
                            level = str(user_data['Level']).upper()
                            hostname_pc = socket.gethostname()

                            # 1. CEK WHITELIST PC
                            if level != "OWNER":
                                if not database.cek_pc_whitelist(hostname_pc):
                                    st.error(f"❌ Akses Ditolak! PC ({hostname_pc}) Tidak Terdaftar.")
                                    st.stop() # Paksa berhenti biar nggak lanjut ke bawah

                            # 2. SET SESSION STATE (Wajib diisi SEMUA sebelum rerun)
                            st.session_state["is_login"] = True
                            st.session_state["user_aktif"] = u
                            st.session_state["user_level"] = level
                            st.session_state["waktu_login"] = database.ambil_waktu_sekarang()

                            # 3. UPDATE SESI DI DATABASE (Anti-Sharing)
                            database.update_sesi(u, st.session_state["browser_session_id"])
                            
                            # 4. NOTIFIKASI & REFRESH INSTAN
                            st.toast(f"✅ Selamat Datang {u}")
                            
                            # Jeda super singkat saja
                            time.sleep(1) 
                            st.rerun() # <--- INI WAJIB ADA DI PALING BAWAH
                        else:
                            st.error("❌ Username atau Password salah!")
                    else:
                        st.warning("⚠️ Isi dulu Username dan Password!")

# --- MONITORING KEAMANAN REAL-TIME (SILENT MODE) ---
if st.session_state["is_login"]:
    # A. Cek Durasi 10 Jam (WIB)
    waktu_sekarang = database.ambil_waktu_sekarang()
    durasi = waktu_sekarang - st.session_state["waktu_login"]
    
    if durasi > timedelta(hours=10):
        proses_logout() # Keluar otomatis tanpa notif berisik

    # B. Cek Single Device (Anti-Sharing)
    if not database.cek_sesi_valid(st.session_state["user_aktif"], st.session_state["browser_session_id"]):
        proses_logout() # Langsung kick jika ada login baru di device lain

# --- JALANKAN APLIKASI ---
if not st.session_state["is_login"]:
    halaman_login()
else:
    # Sidebar Info (Minimalis)
    st.sidebar.write(f"👤 **{st.session_state['user_aktif']}**")
    st.sidebar.write(f"🛡️ Level: {st.session_state['user_level']}")
    
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    if st.sidebar.button("Keluar (Logout)", use_container_width=True):
        proses_logout()

    # Dashboard Utama (Bersih & Rapi)
    st.title("🚀 Dashboard PINTAR MEDIA")
    st.write(f"Selamat datang kembali, {st.session_state['user_aktif']}.")
    
    # Space kosong buat konten berikutnya
    st.divider()
