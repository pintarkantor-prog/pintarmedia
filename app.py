import streamlit as st
import uuid
import socket
import time
import os
from datetime import timedelta
from modules import database
from pages_content import ai_lab, area_staf, database_channel, kendali_tim

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
st.set_page_config(page_title="PINTAR MEDIA | Studio", layout="wide", initial_sidebar_state="expanded")

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

# --- 1. PROSES LOGIN (Pembersihan Total Whitelist) ---
def proses_login(u, p):
    try:
        # 1. Ambil data Staff (Database Utama)
        df_staff = database.ambil_data("Staff")
        u_input = str(u).strip().upper()
        p_input = str(p).strip()

        # 2. Cari user berdasarkan NAMA dan PASSWORD (Case Insensitive untuk Nama)
        user_row = df_staff[
            (df_staff['NAMA'].astype(str).str.upper() == u_input) & 
            (df_staff['PASSWORD'].astype(str) == p_input)
        ]
        
        if not user_row.empty:
            user_data = user_row.iloc[0]
            
            # --- KUNCI: STANDARISASI LEVEL ---
            # Kita paksa UPPER agar sinkron dengan dict ketentuan di area_staf.py
            level = str(user_data.get('LEVEL', 'STAFF')).upper().strip()

            # --- FITUR WHITELIST PC TELAH DIHAPUS ---
            # (Staf sekarang bisa login dari perangkat mana saja)

            # 3. SET SESSION STATE
            st.session_state["is_login"] = True
            st.session_state["user_aktif"] = u_input
            st.session_state["user_level"] = level
            st.session_state["waktu_login"] = database.ambil_waktu_sekarang()
            
            # Catat sesi login ke Supabase
            database.update_sesi(u_input, st.session_state.get("browser_session_id", "Unknown"))
            
            st.toast(f"✅ Selamat Datang {u_input}")
            time.sleep(0.5)
            st.rerun()
        else:
            st.error("❌ Username atau Password salah!")
            
    except Exception as e:
        # Debugging jika ada kolom yang hilang di database
        st.error(f"Sistem Login Error: {e}")
        if 'df_staff' in locals():
            st.write("Kolom terdeteksi:", list(df_staff.columns))
            
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
    user_level = st.session_state.get("user_level", "STAFF").upper() # Pastikan UPPER
    user_aktif = st.session_state.get("user_aktif", "USER").upper()
    
    with st.sidebar:
        st.markdown("""
            <div style='display: flex; align-items: center; margin-bottom: 10px; margin-top: 10px;'>
                <span style='font-size: 20px; margin-right: 10px;'>🖥️</span>
                <span style='font-size: 14px; color: white; font-weight: bold; letter-spacing: 1px;'>MAIN COMMAND</span>
            </div>
        """, unsafe_allow_html=True)
        
        # --- KUNCI SIDEBAR: Menu Dasar untuk Semua ---
        menu_list = ["🧠 PINTAR AI LAB", "📘 AREA STAF"]
        
        # --- KUNCI OWNER & ADMIN: Tambah Menu Rahasia ---
        if user_level in ["OWNER", "ADMIN"]:
            # Kita sisipkan di tengah atau akhir sesuai selera lo
            menu_list.insert(1, "📱 DATABASE CHANNEL") 
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

# --- JALANKAN APLIKASI (VERSI TANPA SPINNER - TETEP BERSIH) ---
if not cek_autentikasi():
    halaman_login()
else:
    menu = tampilkan_navigasi_sidebar()
    user_level = st.session_state.get("user_level", "STAFF").upper()

    # --- JURUS KUNCI: WADAH KOSONG (WIPE LAYAR) ---
    # Kita bikin satu wadah kosong yang bakal kita isi ulang tiap pindah menu
    wadah_utama = st.empty()

    with wadah_utama.container():
        # Kasih jeda tipis banget (0.3-0.5 detik) buat sinkronisasi browser
        # Tanpa spinner, ini bakal berasa kenceng tapi layarnya sempet bersih
        time.sleep(1) 
        
        # --- ROUTING HALAMAN ---
        if menu == "🧠 PINTAR AI LAB":
            ai_lab.tampilkan_halaman()

        elif menu == "📱 DATABASE CHANNEL":
            if user_level in ["OWNER", "ADMIN"]:
                database_channel.tampilkan_database_channel()
            else:
                st.error("🚫 Akses Ditolak!")

        elif menu == "📘 AREA STAF":
            area_staf.tampilkan_area_staf()

        elif menu == "⚡ KENDALI TIM":
            if user_level in ["OWNER", "ADMIN"]:
                kendali_tim.tampilkan_kendali_tim()
            else:
                st.error("🚫 Akses Ditolak!")
