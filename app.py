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
# BLOK 1: KONFIGURASI HALAMAN & CSS (IDENTIK RUMAH LAMA + V2 STYLE)
# ==============================================================================
st.set_page_config(page_title="PINTAR MEDIA V2", page_icon="🎬", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-thumb { background: #1d976c; border-radius: 10px; }
    [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) {
        position: fixed; top: 0; left: 310px; right: 0; z-index: 99999;
        background-color: #0e1117; padding: 10px 2rem; border-bottom: 2px solid #31333f;
    }
    div.stButton > button[kind="primary"] {
        background: linear-gradient(to right, #1d976c, #11998e) !important;
        color: white !important; font-weight: bold; width: 100%; border-radius: 8px;
    }
    .staff-header-premium {
        background: rgba(29, 151, 108, 0.2) !important; border: 2px solid #1d976c !important;
        border-radius: 10px !important; padding: 15px 20px !important; margin-bottom: 25px;
        display: flex; align-items: center; gap: 12px;
    }
    .staff-header-premium b { color: #1d976c !important; font-size: 1.15em; }
    .small-label { color: #1d976c !important; letter-spacing: 1px; text-transform: uppercase; font-size: 10px !important; font-weight: 800 !important; }
    .stExpander { border: 1px solid rgba(29, 151, 108, 0.3) !important; border-radius: 12px !important; background-color: #161922 !important; margin-bottom: 15px !important; }
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
                p_in = st.text_input("Password", type="password")
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

if 'active_user' in st.session_state and 'login_time' in st.session_state:
    if (time.time() - st.session_state.login_time) > (10 * 3600):
        st.query_params.clear()
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

# ==============================================================================
# BLOK 3: INISIALISASI MEMORI, LOGGING & AI ENGINE (MESIN ASLI)
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

if 'last_generated_results' not in st.session_state: st.session_state.last_generated_results = []
if 'c_name_1_input' not in st.session_state: st.session_state.c_name_1_input = ""
if 'c_desc_1_input' not in st.session_state: st.session_state.c_desc_1_input = ""
if 'c_name_2_input' not in st.session_state: st.session_state.c_name_2_input = ""
if 'c_desc_2_input' not in st.session_state: st.session_state.c_desc_2_input = ""

for i in range(1, 51):
    for k, d in [(f"vis_input_{i}", ""), (f"light_input_{i}", "Siang"), (f"camera_input_{i}", "Diam (Tanpa Gerak)"), (f"shot_input_{i}", "Setengah Badan"), (f"angle_input_{i}", "Normal"), (f"loc_sel_{i}", "--- KETIK MANUAL ---"), (f"loc_custom_{i}", "")]:
        if k not in st.session_state: st.session_state[k] = d

# ==============================================================================
# BLOK 4: MAPPING DATA & DNA LOKASI (IDENTIK RUMAH LAMA)
# ==============================================================================
indonesia_camera = ["Diam (Tanpa Gerak)", "Ikuti Karakter", "Zoom Masuk", "Zoom Keluar", "Memutar (Orbit)"]
indonesia_shot = ["Sangat Dekat", "Dekat Wajah", "Setengah Badan", "Seluruh Badan", "Pemandangan Luas", "Drone Shot"]
indonesia_angle = ["Normal", "Sudut Rendah", "Sudut Tinggi", "Samping", "Berhadapan", "Intip Bahu", "Belakang"]
options_lighting = ["Pagi", "Siang", "Sore", "Malam"]

LOKASI_DNA = {
    "jalan kampung": "shabby dirt road in Indonesian village, dense banana trees, microscopic dust particles, weathered textures...",
    "pasar": "authentic Indonesian wet market, wet muddy floor textures, vibrant organic produce...",
    "teras rumah kaya": "modern minimalist mansion terrace, marble reflections, manicured garden details...",
    "dalam rumah kaya": "high-end luxury living room, polished stone textures, glass walls..."
}
options_lokasi = ["--- KETIK MANUAL ---"] + list(LOKASI_DNA.keys())
shot_map = {"Sangat Dekat": "Extreme Close-Up...", "Dekat Wajah": "Close-Up...", "Setengah Badan": "Medium Shot...", "Seluruh Badan": "Full body shot...", "Pemandangan Luas": "Wide landscape...", "Drone Shot": "Cinematic Drone..."}
angle_map = {"Normal": "eye-level...", "Sudut Rendah": "low angle...", "Sudut Tinggi": "high angle...", "Samping": "side profile...", "Berhadapan": "facing each other...", "Intip Bahu": "over-the-shoulder...", "Belakang": "from behind..."}

# ==============================================================================
# BLOK 5: SIDEBAR & MENU NAVIGASI (FINAL STRUCTURE)
# ==============================================================================
with st.sidebar:
    try: st.image("PINTAR.png", use_container_width=True)
    except: st.title("🎬 PINTAR MEDIA")
    st.write(f"Staff: **{st.session_state.active_user.upper()}** ✅")
    st.divider()
    
    # Halaman Utama = Dashboard (Isi Storyboard)
    menu = st.radio("MENU NAVIGASI:", ["🚀 DASHBOARD", "📊 MONITORING", "🧠 AI LAB", "🎞️ SCHEDULE", "📋 TEAM TASK", "📈 TREND ANALYZER", "💡 IDEAS BANK", "👥 DATABASE LOCKER", "🛠️ COMMAND CENTER"])
    st.divider()

    num_scenes = st.number_input("Tambah Jumlah Adegan", 1, 50, 6)
    list_genre = ["Realistik (Nyata)", "Pixar 3D", "Marvel Superhero", "Transformers (Mecha)", "KingKong (VFX Monster)", "Asphalt (Balap/Glossy)", "Ghibli (Estetik/Indah)", "Dragon Ball", "Doraemon 3D", "Naruto (Ninja)", "Tayo (Anak-anak)", "Sakura School (Anime)"]
    genre_saved = st.session_state.get("genre_pilihan_saved", "Realistik (Nyata)")
    genre_pilihan = st.selectbox("Pilih Gaya Film:", options=list_genre, index=list_genre.index(genre_saved) if genre_saved in list_genre else 0)

    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("💾 SAVE", use_container_width=True):
            char_data = {str(idx): {"name": st.session_state.get(f"c_name_{idx}_input", ""), "desc": st.session_state.get(f"c_desc_{idx}_input", "")} for idx in range(1, 11)}
            scene_data = {str(i): {"vis": st.session_state.get(f"vis_input_{i}", ""), "light": st.session_state.get(f"light_input_{i}", "Siang"), "shot": st.session_state.get(f"shot_input_{i}", "Setengah Badan"), "angle": st.session_state.get(f"angle_input_{i}", "Normal"), "loc": st.session_state.get(f"loc_sel_{i}", "jalan kampung")} for i in range(1, 51)}
            dialog_data = {k: v for k, v in st.session_state.items() if k.startswith("diag_") and v}
            master_packet = {"num_char": st.session_state.get("num_total_char", 2), "genre": genre_pilihan, "chars": char_data, "scenes": scene_data, "dialogs": dialog_data}
            record_to_sheets(f"DRAFT_{st.session_state.active_user}", json.dumps(master_packet), len([s for s in scene_data.values() if s['vis']]))
            st.toast("Project Tersimpan! ✅")
    with btn_col2:
        if st.button("🔄 LOAD", use_container_width=True):
            try:
                conn = st.connection("gsheets", type=GSheetsConnection)
                df_log = conn.read(worksheet="Sheet1", ttl="1s")
                my_data = df_log[df_log['User'] == f"DRAFT_{st.session_state.active_user}"]
                if not my_data.empty:
                    data = json.loads(str(my_data.iloc[-1]['Visual Utama']))
                    st.session_state["genre_pilihan_saved"] = data.get("genre", "Realistik (Nyata)")
                    for i_str, val in data.get("chars", {}).items():
                        st.session_state[f"c_name_{i_str}_input"], st.session_state[f"c_desc_{i_str}_input"] = val.get("name", ""), val.get("desc", "")
                    for i_str, val in data.get("scenes", {}).items():
                        if isinstance(val, dict):
                            st.session_state[f"vis_input_{i_str}"], st.session_state[f"light_input_{i_str}"] = val.get("vis", ""), val.get("light", "Siang")
                            st.session_state[f"shot_input_{i_str}"], st.session_state[f"angle_input_{i_str}"] = val.get("shot", "Setengah Badan"), val.get("angle", "Normal")
                            st.session_state[f"loc_sel_{i_str}"] = val.get("loc", "jalan kampung")
                    for k, v in data.get("dialogs", {}).items(): st.session_state[k] = v
                    st.rerun()
            except: st.error("Draft kosong.")
    if st.button("KELUAR SISTEM ⚡", use_container_width=True):
        st.query_params.clear()
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

# ==============================================================================
# BLOK 6: HALAMAN BERDASARKAN MENU
# ==============================================================================

# --- [MENU UTAMA: 🚀 DASHBOARD] (PRODUCTION UNIT) ---
if menu == "🚀 DASHBOARD":
    st.header(f"🚀 Dashboard Kerja: {st.session_state.active_user.capitalize()}")
    st.markdown(f'<div class="staff-header-premium"><span style="font-size:20px;">👤</span><div><b>Unit Produksi: Aktif</b> | <span style="color:#aaa; font-style:italic;">Siapkan detail storyboard untuk generate prompt 🚀🚀</span></div></div>', unsafe_allow_html=True)
    
    with st.expander("👥 Karakter & Penampilan Fisik!", expanded=True):
        num_total_char = st.number_input("Total Karakter", 1, 10, 2, key="num_total_char")
        all_chars_list = []
        for i in range(1, num_total_char + 1, 2):
            cols = st.columns(2)
            for idx_offset in range(2):
                idx = i + idx_offset
                if idx <= num_total_char:
                    with cols[idx_offset]:
                        st.markdown(f"##### 👤 Karakter {idx}")
                        name = st.text_input("Nama", key=f"c_name_{idx}_input", label_visibility="collapsed")
                        desc = st.text_area("Fisik", key=f"c_desc_{idx}_input", height=120, label_visibility="collapsed")
                        all_chars_list.append({"name": name, "desc": desc})

    adegan_storage = []
    for i_s in range(1, int(num_scenes) + 1):
        with st.expander(f"🎬 ADEGAN {i_s}", expanded=(i_s == 1)):
            col_v, col_ctrl = st.columns([6, 4])
            with col_v:
                visual_input = st.text_area(f"Cerita Visual {i_s}", key=f"vis_input_{i_s}", height=265)
            with col_ctrl:
                r1, r2 = st.columns(2), st.columns(2)
                with r1[0]: 
                    st.markdown('<p class="small-label">💡 Suasana</p>', unsafe_allow_html=True)
                    light_val = st.selectbox(f"L{i_s}", options_lighting, key=f"light_input_{i_s}", label_visibility="collapsed")
                with r1[1]:
                    st.markdown('<p class="small-label">📐 Shot</p>', unsafe_allow_html=True)
                    shot_val = st.selectbox(f"S{i_s}", indonesia_shot, key=f"shot_input_{i_s}", label_visibility="collapsed")
                with r2[0]:
                    st.markdown('<p class="small-label">✨ Angle</p>', unsafe_allow_html=True)
                    angle_val = st.selectbox(f"A{i_s}", indonesia_angle, key=f"angle_input_{i_s}", label_visibility="collapsed")
                with r2[1]:
                    st.markdown('<p class="small-label">🎬 Kamera</p>', unsafe_allow_html=True)
                    cam_val = st.selectbox(f"C{i_s}", indonesia_camera, key=f"camera_input_{i_s}", label_visibility="collapsed")
                st.markdown('<p class="small-label">📍 Lokasi</p>', unsafe_allow_html=True)
                loc_choice = st.selectbox(f"LocSelect{i_s}", options=options_lokasi, key=f"loc_sel_{i_s}", label_visibility="collapsed")
                location_val = st.text_input(f"Manual {i_s}", key=f"loc_custom_{i_s}") if loc_choice == "--- KETIK MANUAL ---" else loc_choice

            diag_cols = st.columns(len(all_chars_list))
            scene_dialogs_list = []
            for i_char, char_data in enumerate(all_chars_list):
                with diag_cols[i_char]:
                    d_in = st.text_input(f"Dialog {char_data['name']}", key=f"diag_{i_s}_{i_char}")
                    scene_dialogs_list.append({"name": char_data['name'], "text": d_in})
            adegan_storage.append({"num": i_s, "visual": visual_input, "light": light_val, "location": location_val, "cam": cam_val, "shot": shot_val, "angle": angle_val, "dialogs": scene_dialogs_list})

    if st.button("🚀 GENERATE ALL PROMPTS", type="primary", use_container_width=True):
        active_scenes = [a for a in adegan_storage if a["visual"].strip() != ""]
        if active_scenes:
            with st.spinner("Meracik prompt..."):
                st.session_state.last_generated_results = []
                for item in active_scenes:
                    v_low = item["visual"].lower()
                    m = [f"[[ CHAR_{c['name'].upper()}: {c['desc']} ]]" for c in all_chars_list if c["name"] and re.search(rf'\b{re.escape(c["name"].lower())}\b', v_low)]
                    char_info = " AND ".join(m) if m else f"[[ CHAR_MAIN: {all_chars_list[0]['desc']} ]]"
                    prompt_img = f"STRICT 8K RAW: {char_info}, ACTION: {item['visual']}, GENRE: {genre_pilihan}"
                    st.session_state.last_generated_results.append({"id": item["num"], "img": prompt_img})
                record_to_sheets(st.session_state.active_user, active_scenes[0]["visual"], len(active_scenes))
                st.rerun()

    if st.session_state.last_generated_results:
        for res in st.session_state.last_generated_results:
            with st.expander(f"ADEGAN {res['id']}"):
                st.code(res["img"])

# --- [MENU: 📊 MONITORING] ---
elif menu == "📊 MONITORING":
    st.header("📊 Monitoring Laporan")
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        df_log = conn.read(worksheet="Sheet1", ttl="0")
        st.dataframe(df_log.tail(30), use_container_width=True, hide_index=True)
    except: st.info("Sedang menarik data dari Cloud...")

# --- [MENU LAIN] ---
else:
    st.header(menu)
    st.info(f"Fitur {menu} sedang disinkronisasi.")
