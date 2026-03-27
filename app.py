import streamlit as st
from datetime import datetime, timedelta
from modules import database # Panggil si 'kurir' tadi

# 1. Satpam (Cek Autentikasi) - Kita ambil logika timedelta kamu
if "sudah_login" not in st.session_state:
    st.session_state["sudah_login"] = False

# CSS buat ngumpetin sidebar kalau belum login
if not st.session_state["sudah_login"]:
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

def tampilkan_halaman_login():
    with st.container():
        st.markdown("<br><br>", unsafe_allow_html=True)
        col_l, col_m, col_r = st.columns([1.5, 1, 1.5]) 
        with col_m:
            st.image("PINTAR.png", use_container_width=True)
            with st.form("login_station"):
                u = st.text_input("Username", placeholder="Username...").lower()
                p = st.text_input("Password", type="password", placeholder="Password...")
                submit = st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True)
                
                if submit:
                    # Panggil fungsi validasi dari modules/database.py
                    user_data = database.validasi_user(u, p)
                    
                    if user_data:
                        st.session_state["sudah_login"] = True
                        st.session_state["user_info"] = user_data # Simpan level user (Owner/Staff)
                        st.session_state["waktu_login"] = datetime.now()
                        st.success(f"Halo {user_data['Nama']}, Gaspol!")
                        st.rerun()
                    else:
                        st.error("Gagal Login! Cek Username/Password di Supabase.")

# LOGIKA UTAMA
if not st.session_state["sudah_login"]:
    tampilkan_halaman_login()
else:
    # Cek durasi login (logika 10 jam kamu)
    durasi = datetime.now() - st.session_state["waktu_login"]
    if durasi > timedelta(hours=10):
        st.session_state["sudah_login"] = False
        st.rerun()
    
    st.title(f"🏠 Dashboard {st.session_state['user_info']['Level']}")
    st.write(f"Selamat bekerja, {st.session_state['user_info']['Nama']}!")
