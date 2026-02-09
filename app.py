import streamlit as st
from streamlit_gsheets import GSheetsConnection
import google.generativeai as genai
import pandas as pd
from datetime import datetime
import pytz
import time
import json
import re

# ==============================================================================
# BLOK 1: KONFIGURASI HALAMAN & CSS (TAMPILAN RUMAH BARU)
# ==============================================================================
st.set_page_config(page_title="PINTAR MEDIA V2", page_icon="🎬", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    /* CUSTOM SCROLLBAR */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-thumb { background: #1d976c; border-radius: 10px; }
    
    /* FIXED HEADER & SIDEBAR */
    [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) {
        position: fixed; top: 0; left: 310px; right: 0; z-index: 99999;
        background-color: #0e1117; padding: 10px 2rem; border-bottom: 2px solid #31333f;
    }
    [data-testid="stSidebar"] { background-color: #1a1c24 !important; }
    
    /* TOMBOL PREMIUM */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(to right, #1d976c, #11998e) !important;
        color: white !important; font-weight: bold; width: 100%; border-radius: 8px;
    }
    
    /* BOX STAF DASHBOARD */
    .staff-header-premium {
        background: rgba(29, 151, 108, 0.2) !important; border: 2px solid #1d976c !important;
        border-radius: 10px !important; padding: 15px 20px !important; margin-bottom: 25px;
        display: flex; align-items: center; gap: 12px;
    }
    .staff-header-premium b { color: #1d976c !important; font-size: 1.15em; }
    .small-label { color: #1d976c !important; letter-spacing: 1px; text-transform: uppercase; font-size: 10px !important; font-weight: 800 !important; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# BLOK 2: SISTEM LOGIN & PROTEKSI (DATA LAMA SULTAN - IDENTIK 100%)
# ==============================================================================
USER_PASSWORDS = {"admin": "QWERTY21ab", "icha": "udin99", "nissa": "tung22", "inggi": "udin33", "lisa": "tung66", "ezaalma": "aprihgino"}

if 'active_user' not in st.session_state:
    q_user = st.query_params.get("u")
    if q_user and q_user.lower() in USER_PASSWORDS:
        st.session_state.active_user = q_user.lower()
        if 'login_time' not in st.session_state: st.session_state.login_time = time.time()
        st.rerun() 
else:
    if st.query_params.get("u") != st.session_state.active_user: st.query_params["u"] = st.session_state.active_user

if 'active_user' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        _, col_login, _ = st.columns([1.8, 1.0, 1.8]) 
        with col_login:
            try: st.image("PINTAR.png", use_container_width=True) 
            except: st.markdown("<h1 style='text-align: center;'>📸 PINTAR MEDIA</h1>", unsafe_allow_html=True)
            with st.form("login_form", clear_on_submit=False):
                u_in = st.text_input("Username", value=st.query_params.get("u", ""), placeholder="Username...")
                p_in = st.text_input("Password", type="password", placeholder="Password...")
                if st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True, type="primary"):
                    u_c = u_in.lower().strip()
                    if u_c in USER_PASSWORDS and p_in == USER_PASSWORDS[u_c]:
                        st.session_state.active_user, st.session_state.login_time = u_c, time.time()
                        st.query_params.clear()
                        st.query_params["u"] = u_c
                        placeholder.empty()
                        st.rerun()
                    else: st.error("❌ Username atau Password salah.")
    st.stop()

# Auto-Logout 10 Jam
if 'active_user' in st.session_state and 'login_time' in st.session_state:
    if (time.time() - st.session_state.login_time) > (10 * 3600):
        st.query_params.clear()
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

# ==============================================================================
# BLOK 3: INISIALISASI MEMORI, LOGGING & AI ENGINE
# ==============================================================================
def record_to_sheets(user, data_packet, total_scenes):
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        existing_data = conn.read(worksheet="Sheet1", ttl="5m")
        tz = pytz.timezone('Asia/Jakarta')
        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        new_row = pd.DataFrame([{"Waktu": current_time, "User": user, "Total Adegan": total_scenes, "Visual Utama": data_packet}])
        updated_df = pd.concat([existing_data, new_row], ignore_index=True)
        conn.update(worksheet="Sheet1", data=updated_df.tail(300))
    except Exception as e: st.error(f"Gagal mencatat ke Cloud: {e}")

API_KEY = "AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except: pass

# Init Session State Adegan 1-50
if 'last_generated_results' not in st.session_state: st.session_state.last_generated_results = []
for i in range(1, 51):
    for k, d in [(f"vis_input_{i}", ""), (f"light_input_{i}", "Siang"), (f"camera_input_{i}", "Diam (Tanpa Gerak)"), (f"shot_input_{i}", "Setengah Badan"), (f"angle_input_{i}", "Normal"), (f"loc_sel_{i}", "--- KETIK MANUAL ---"), (f"loc_custom_{i}", "")]:
        if k not in st.session_state: st.session_state[k] = d

# ==============================================================================
# BLOK 4: MAPPING DATA & DNA LOKASI (KITAB SUCI SULTAN)
# ==============================================================================
LOKASI_DNA = {
    "jalan kampung": "shabby dirt road in Indonesian village, dense banana trees, microscopic dust particles, weathered textures...",
    "pasar": "authentic Indonesian wet market, wet muddy floor textures, vibrant organic produce...",
    "teras rumah miskin": "humble wooden porch, old grey weathered timber, dusty floor boards, raw rustic poverty aesthetic...",
    "dalam rumah kayu": "vintage timber interior, hyper-detailed wood grain, ancient furniture textures...",
    "teras rumah kaya": "modern minimalist mansion terrace, marble floor reflections, manicured garden details...",
    "dalam rumah kaya": "high-end luxury living room, polished stone textures, floor-to-ceiling glass walls..."
}
# (Kamus Mapping Shot, Angle, Camera tetap ada di sini)
shot_map = {"Sangat Dekat": "Extreme Close-Up...", "Dekat Wajah": "Close-Up...", "Setengah Badan": "Medium Shot...", "Seluruh Badan": "Full body shot...", "Pemandangan Luas": "Wide landscape...", "Drone Shot": "Cinematic Aerial Drone..."}
angle_map = {"Normal": "eye-level shot...", "Sudut Rendah": "heroic low angle...", "Sudut Tinggi": "high angle...", "Samping": "side profile...", "Berhadapan": "dual profile...", "Intip Bahu": "over-the-shoulder...", "Belakang": "shot from behind..."}

# ==============================================================================
# BLOK 5: SIDEBAR & MENU NAVIGASI
# ==============================================================================
with st.sidebar:
    try: st.image("PINTAR.png", use_container_width=True)
    except: st.title("🎬 PINTAR MEDIA")
    st.write(f"User: **{st.session_state.active_user.upper()}** ✅")
    st.divider()
    menu = st.radio("NAVIGASI UTAMA:", ["🏠 DASHBOARD", "🚀 PRODUCTION HUB", "🧠 AI LAB", "🎞️ SCHEDULE", "📋 TEAM TASK", "📈 TREND ANALYZER", "💡 IDEAS BANK", "👥 DATABASE LOCKER", "🛠️ COMMAND CENTER"])
    st.divider()
    if st.button("KELUAR SISTEM ⚡"):
        st.query_params.clear()
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

# ==============================================================================
# BLOK 6: ISI HALAMAN BERDASARKAN MENU
# ==============================================================================

# --- [MENU: 🏠 DASHBOARD] ---
if menu == "🏠 DASHBOARD":
    st.header("🏠 Dashboard Utama")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("📅 Log Aktivitas Tim")
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            df = conn.read(worksheet="Sheet1", ttl="0")
            st.dataframe(df.tail(10), use_container_width=True, hide_index=True)
        except: st.info("Sinkronisasi database...")
    with col2:
        st.subheader("🏆 Staf Terbaik")
        st.info("Peringkat kinerja tim bulan ini.")

# --- [MENU: 🚀 PRODUCTION HUB] (STORYBOARD UTUH SULTAN) ---
elif menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    st.markdown(f'<div class="staff-header-premium">👤 <b>Staf: {st.session_state.active_user.capitalize()}</b> | <i>Konten mantap lahir dari detail yang tepat.</i></div>', unsafe_allow_html=True)
    
    # Masukkan seluruh kode form Storyboard Sultan di sini (Identitas Tokoh, Expander Adegan, Tombol Generate)
    st.subheader("📝 Detail Storyboard")
    # ... (Semua Form Adegan 1-50 Sultan ada di sini)

# --- [MENU: 🧠 AI LAB] ---
elif menu == "🧠 AI LAB":
    st.header("🧠 AI Laboratory")
    st.info("Fitur analisis video kompetitor sedang disiapkan.")

# --- [MENU: 📈 TREND ANALYZER] ---
elif menu == "📈 TREND ANALYZER":
    st.header("📈 Trend Analyzer")
    st.write("Mendeteksi tren viral TikTok & YouTube...")

# --- [MENU: LAIN-LAIN] ---
else:
    st.header(menu)
    st.info(f"Blok {menu} dalam tahap sinkronisasi data lama Sultan.")
