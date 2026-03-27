import streamlit as st
import uuid
import socket
import time
import os
from datetime import timedelta
from modules import database
from pages_content import ai_lab


# --- FUNGSI PANGGIL CSS ---
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.error(f"File {file_name} tidak ditemukan!")

# --- EKSEKUSI PANGGILAN CSS ---
local_css("assets/style.css")

# --- CONFIG HALAMAN ---
st.set_page_config(page_title="PINTAR MEDIA | Studio", layout="wide")

# Inisialisasi ID Browser & Status Login
if "browser_session_id" not in st.session_state:
    st.session_state["browser_session_id"] = str(uuid.uuid4())

if "is_login" not in st.session_state:
    st.session_state["is_login"] = False

# Sembunyikan Sidebar jika belum login
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

# --- 1. PROSES LOGIN (Logika Murni) ---
def proses_login(u, p):
    try:
        # 1. Ambil data (Sudah dipaksa KAPITAL oleh fungsi ambil_data)
        df_staff = database.ambil_data("Staff")
        u_input = str(u).strip().upper()
        p_input = str(p).strip()

        # 2. Cari user (Gunakan nama kolom KAPITAL: 'NAMA' dan 'PASSWORD')
        # Kita pakai .astype(str) untuk jaga-jaga kalau pass di DB dianggap angka
        user_row = df_staff[
            (df_staff['NAMA'].astype(str).str.upper() == u_input) & 
            (df_staff['PASSWORD'].astype(str) == p_input)
        ]
        
        if not user_row.empty:
            user_data = user_row.iloc[0]
            
            # Ambil LEVEL (Pakai kapital juga)
            level = str(user_data['LEVEL']).upper()
            hostname_pc = socket.gethostname()

            # 3. Cek Whitelist (Kecuali Owner)
            if level != "OWNER":
                if not database.cek_pc_whitelist(hostname_pc):
                    st.error(f"❌ Akses Ditolak! PC ({hostname_pc}) Tidak Terdaftar.")
                    st.stop()

            # 4. SET SESSION STATE
            st.session_state["is_login"] = True
            st.session_state["user_aktif"] = u_input
            st.session_state["user_level"] = level
            st.session_state["waktu_login"] = database.ambil_waktu_sekarang()
            
            # Catat login
            database.update_sesi(u_input, st.session_state.get("browser_session_id", "Unknown"))
            
            st.toast(f"✅ Selamat Datang {u_input}")
            time.sleep(0.5)
            st.rerun()
        else:
            st.error("❌ Username atau Password salah!")
            
    except Exception as e:
        # Menampilkan detail kolom yang tersedia kalau masih error (buat debug)
        st.error(f"Sistem Login Error: {e}")
        if 'df_staff' in locals():
            st.write("Kolom tersedia:", list(df_staff.columns))

# --- 2. TAMPILAN LOGIN (UI Form) ---
def halaman_login():
    with st.container():
        st.markdown("<br><br>", unsafe_allow_html=True)
        col_l, col_m, col_r = st.columns([1.5, 1, 1.5]) 
        
        with col_m:
            try:
                st.image("PINTAR.png", use_container_width=True)
            except:
                st.markdown("<h2 style='text-align:center;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
            
            with st.form("login_station", clear_on_submit=False):
                u = st.text_input("Username", placeholder="Username...", key="input_u")
                p = st.text_input("Password", type="password", placeholder="Password...", key="input_p")
                submit = st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True)
                
                if submit:
                    if u.strip() and p.strip():
                        proses_login(u, p)
                    else:
                        st.warning("⚠️ Isi dulu Bos!")

# --- 3. CEK AUTENTIKASI (Satpam Durasi) ---
def cek_autentikasi():
    if st.session_state.get("is_login", False):
        # Hanya cek durasi login 10 jam (Fitur tendang-tendangan sudah dihapus)
        waktu_sekarang = database.ambil_waktu_sekarang()
        if (waktu_sekarang - st.session_state["waktu_login"]) > timedelta(hours=10):
            proses_logout("Sesi berakhir.")
            return False
        return True
    return False

# --- 4. NAVIGASI SIDEBAR ---
def tampilkan_navigasi_sidebar():
    user_level = st.session_state.get("user_level", "STAFF")
    user_aktif = st.session_state.get("user_aktif", "USER").upper()
    
    with st.sidebar:
        st.markdown("""
            <div style='display: flex; align-items: center; margin-bottom: 10px; margin-top: 10px;'>
                <span style='font-size: 20px; margin-right: 10px;'>🖥️</span>
                <span style='font-size: 14px; color: white; font-weight: bold; letter-spacing: 1px;'>MAIN COMMAND</span>
            </div>
        """, unsafe_allow_html=True)
        
        menu_list = ["🧠 PINTAR AI LAB", "📱 DATABASE CHANNEL", "📘 AREA STAF"]
        if user_level in ["OWNER", "ADMIN"]:
            menu_list.append("⚡ KENDALI TIM")

        pilihan = st.radio("COMMAND_MENU", menu_list, label_visibility="collapsed")
        st.markdown("<hr style='margin: 20px 0; border-color: #30363d;'>", unsafe_allow_html=True)
        
        st.markdown('<div style="margin-top: 50px;"></div>', unsafe_allow_html=True)   
        if st.button("⚡ KELUAR SISTEM", key="btn_logout", use_container_width=True):
            proses_logout()
        
        st.markdown(f'''
            <div style="border-top: 1px solid #30363d; padding-top: 15px; margin-top: 10px;">
                <p class="status-footer">
                    🛰️ STATION: {user_aktif}_SESSION<br>
                    🟢 STATUS: {user_level}
                </p>
            </div>
        ''', unsafe_allow_html=True)
    return pilihan

# --- JALANKAN APLIKASI ---
if not cek_autentikasi():
    halaman_login()
else:
    menu = tampilkan_navigasi_sidebar()

    # ROUTING HALAMAN
    if menu == "🧠 PINTAR AI LAB":
        ai_lab.tampilkan_halaman()

    elif menu == "📱 DATABASE CHANNEL":
        # Lazy Loading: Hanya import saat menu diklik agar web kencang
        try:
            from pages_content import database_channel
            database_channel.tampilkan_database_channel()
        except Exception as e:
            st.title("📱 Database Channel")
            st.error(f"Gagal memuat halaman: {e}")

    elif menu == "📘 AREA STAF":
        st.title("📘 Area Staf")
        st.write("Pusat informasi tim.")

    elif menu == "⚡ KENDALI TIM":
        # Lazy Loading: Tarik menu keuangan pas diklik biar studio tetep enteng
        try:
            from pages_content import kendali_tim
            kendali_tim.tampilkan_kendali_tim()
        except Exception as e:
            st.title("⚡ Kendali Tim")
            st.error(f"Gagal memuat sistem keuangan: {e}")
