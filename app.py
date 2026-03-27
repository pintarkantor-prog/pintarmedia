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

# --- EKSEKUSI PANGGILAN ---
local_css("assets/style.css")

# --- CONFIG HALAMAN ---
st.set_page_config(page_title="PINTAR MEDIA | Studio", layout="wide")

# Inisialisasi ID Browser Unik
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
    with st.container():
        st.markdown("<br><br>", unsafe_allow_html=True)
        col_l, col_m, col_r = st.columns([1.5, 1, 1.5]) 
        
        with col_m:
            try:
                st.image("PINTAR.png", use_container_width=True)
            except:
                st.markdown("<h2 style='text-align:center;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
            
            with st.form("login_station", clear_on_submit=False):
                u = st.text_input("Username", placeholder="Username...", key="input_u").strip().upper()
                p = st.text_input("Password", type="password", placeholder="Password...", key="input_p")
                submit = st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True)
                
                if submit:
                    if u and p:
                        df_staff = database.ambil_data("Staff")
                        user_row = df_staff[(df_staff['Nama'] == u) & (df_staff['Password'] == p)]
                        
                        if not user_row.empty:
                            user_data = user_row.iloc[0]
                            level = str(user_data['Level']).upper()
                            hostname_pc = socket.gethostname()

                            if level != "OWNER":
                                if not database.cek_pc_whitelist(hostname_pc):
                                    st.error(f"❌ Akses Ditolak! PC ({hostname_pc}) Tidak Terdaftar.")
                                    st.stop()

                            st.session_state["is_login"] = True
                            st.session_state["user_aktif"] = u
                            st.session_state["user_level"] = level
                            st.session_state["waktu_login"] = database.ambil_waktu_sekarang()
                            database.update_sesi(u, st.session_state["browser_session_id"])
                            
                            st.toast(f"✅ Selamat Datang {u}")
                            time.sleep(1) 
                            st.rerun()
                        else:
                            st.error("❌ Username atau Password salah!")
                    else:
                        st.warning("⚠️ Isi dulu Username dan Password!")

# --- NAVIGASI SIDEBAR (Style Klasik) ---
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
        
        # Menu yang diinginkan: AI LAB, DATABASE CHANNEL, AREA STAF, KENDALI TIM
        menu_list = [
            "🧠 PINTAR AI LAB", 
            "📱 DATABASE CHANNEL",
            "📘 AREA STAF"
        ]
        
        if user_level in ["OWNER", "ADMIN"]:
            menu_list.append("⚡ KENDALI TIM")

        # Navigasi Radio
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

# --- LOGIKA JALANKAN APLIKASI ---
if not st.session_state["is_login"]:
    halaman_login()
else:
    # A. Cek Keamanan Real-time
    waktu_sekarang = database.ambil_waktu_sekarang()
    if (waktu_sekarang - st.session_state["waktu_login"]) > timedelta(hours=10):
        proses_logout()
    if not database.cek_sesi_valid(st.session_state["user_aktif"], st.session_state["browser_session_id"]):
        proses_logout()

    # B. Panggil Navigasi
    menu = tampilkan_navigasi_sidebar()

    # C. Routing Halaman (Otomatis ke AI LAB karena jadi pilihan pertama di radio)
    if menu == "🧠 PINTAR AI LAB":
        ai_lab.tampilkan_halaman()
        # Isi konten AI LAB kamu di sini

    elif menu == "📱 DATABASE CHANNEL":
        st.title("📱 Database Channel")
        # Nanti kita panggil: pages_content.database_channel.tampilkan_halaman()
        st.write("Daftar akun email dan channel kamu.")

    elif menu == "📘 AREA STAF":
        st.title("📘 Area Staf")
        st.write("Pusat informasi dan koordinasi tim.")

    elif menu == "⚡ KENDALI TIM":
        st.title("⚡ Kendali Tim")
        st.write("Panel manajemen khusus Owner/Admin.")
