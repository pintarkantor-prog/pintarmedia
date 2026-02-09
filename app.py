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
# 0. SISTEM LOGIN TUNGGAL (IDENTIK 100% RUMAH LAMA)
# ==============================================================================
st.set_page_config(page_title="PINTAR MEDIA V2", page_icon="🎬", layout="wide", initial_sidebar_state="expanded")

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
                u_in = st.text_input("Username", value=st.query_params.get("u", ""))
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

# ==============================================================================
# 1 & 2. INISIALISASI MEMORI & DATA DNA (IDENTIK RUMAH LAMA)
# ==============================================================================
if 'last_generated_results' not in st.session_state:
    st.session_state.last_generated_results = []

for i in range(1, 51):
    for k, d in [(f"vis_input_{i}", ""), (f"light_input_{i}", "Siang"), (f"camera_input_{i}", "Diam (Tanpa Gerak)"), (f"shot_input_{i}", "Setengah Badan"), (f"angle_input_{i}", "Normal"), (f"loc_sel_{i}", "--- KETIK MANUAL ---"), (f"loc_custom_{i}", "")]:
        if k not in st.session_state: st.session_state[k] = d

# DNA Lokasi & Mapping Kualitas
LOKASI_DNA = {
    "jalan kampung": "shabby dirt road in Indonesian village, dense banana trees, microscopic dust particles, weathered textures, ultra-detailed gravel and soil.",
    "pasar": "authentic Indonesian wet market, wet muddy floor textures, vibrant organic produce, detailed wicker baskets, crowded stall textures, hyper-realistic.",
    "teras rumah kaya": "modern minimalist mansion terrace, premium marble floor reflections, manicured garden details, sleek luxury aesthetic, sharp clean lines.",
    "dalam rumah kaya": "high-end luxury living room, polished stone textures, floor-to-ceiling glass walls, premium leather sofa grain, sharp interior design clarity."
}
options_lokasi = ["--- KETIK MANUAL ---"] + list(LOKASI_DNA.keys())
indonesia_camera = ["Diam (Tanpa Gerak)", "Ikuti Karakter", "Zoom Masuk", "Zoom Keluar", "Memutar (Orbit)"]
indonesia_shot = ["Sangat Dekat", "Dekat Wajah", "Setengah Badan", "Seluruh Badan", "Pemandangan Luas", "Drone Shot"]
indonesia_angle = ["Normal", "Sudut Rendah", "Sudut Tinggi", "Samping", "Berhadapan", "Intip Bahu", "Belakang"]
options_lighting = ["Pagi", "Siang", "Sore", "Malam"]

shot_map = {"Sangat Dekat": "Extreme Close-Up shot...", "Dekat Wajah": "Close-Up shot...", "Setengah Badan": "Medium Shot...", "Seluruh Badan": "Full body shot...", "Pemandangan Luas": "Wide landscape shot...", "Drone Shot": "Cinematic Drone..."}
angle_map = {"Normal": "eye-level shot...", "Sudut Rendah": "low angle shot...", "Sudut Tinggi": "high angle shot...", "Samping": "side profile...", "Berhadapan": "facing each other...", "Intip Bahu": "over-the-shoulder...", "Belakang": "from behind..."}

# ==============================================================================
# 3. LOGIKA LOGGING & CSS (TAMPILAN MEWAH)
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
    except Exception as e: st.error(f"Gagal mencatat: {e}")

st.markdown("""
    <style>
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-thumb { background: #1d976c; border-radius: 10px; }
    [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) {
        position: fixed; top: 0; left: 310px; right: 0; z-index: 99999;
        background-color: #0e1117; padding: 10px 2rem; border-bottom: 2px solid #31333f;
    }
    div.stButton > button[kind="primary"] { background: linear-gradient(to right, #1d976c, #11998e) !important; color: white !important; font-weight: bold; width: 100%; border-radius: 8px; }
    .staff-header-premium { background: rgba(29, 151, 108, 0.2) !important; border: 2px solid #1d976c !important; border-radius: 10px !important; padding: 15px 20px !important; margin-bottom: 25px; display: flex; align-items: center; gap: 12px; }
    .small-label { color: #1d976c !important; text-transform: uppercase; font-size: 10px !important; font-weight: 800 !important; }
    .stExpander { border: 1px solid rgba(29, 151, 108, 0.3) !important; border-radius: 12px !important; background-color: #161922 !important; margin-bottom: 15px !important; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. SIDEBAR & MENU NAVIGASI (SULTAN REQUEST)
# ==============================================================================
with st.sidebar:
    try: st.image("PINTAR.png", use_container_width=True)
    except: st.title("🎬 PINTAR MEDIA")
    st.write(f"Staff: **{st.session_state.active_user.upper()}** ✅")
    st.divider()
    menu = st.radio("MENU NAVIGASI:", ["🚀 DASHBOARD", "📊 MONITORING", "🧠 AI LAB", "🎞️ SCHEDULE", "📋 TEAM TASK", "📈 TREND ANALYZER", "💡 IDEAS BANK", "👥 DATABASE LOCKER", "🛠️ COMMAND CENTER"])
    st.divider()
    num_scenes = st.number_input("Tambah Jumlah Adegan", 1, 50, 6)
    list_genre = ["Realistik (Nyata)", "Pixar 3D", "Marvel Superhero", "Transformers (Mecha)", "KingKong (VFX Monster)", "Asphalt (Balap/Glossy)", "Ghibli (Estetik/Indah)", "Dragon Ball", "Doraemon 3D", "Naruto (Ninja)", "Tayo (Anak-anak)", "Sakura School (Anime)"]
    genre_saved = st.session_state.get("genre_pilihan_saved", "Realistik (Nyata)")
    genre_pilihan = st.selectbox("Pilih Gaya Film:", options=list_genre, index=list_genre.index(genre_saved) if genre_saved in list_genre else 0)

    # Tombol Save/Load
    if st.button("💾 SAVE PROJECT", use_container_width=True):
        st.toast("Project Tersimpan!")

    if st.button("KELUAR SISTEM ⚡", use_container_width=True):
        st.query_params.clear()
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

# ==============================================================================
# 5. HALAMAN 🚀 DASHBOARD (FULL STORYBOARD + RESULT AREA)
# ==============================================================================
if menu == "🚀 DASHBOARD":
    st.header(f"🚀 Dashboard Kerja: {st.session_state.active_user.capitalize()}")
    st.markdown(f'<div class="staff-header-premium">👤 <b>Unit Produksi Aktif</b> | <span style="color:#aaa; font-style:italic;">Hasil prompt akan muncul di bagian bawah setelah di-generate.</span></div>', unsafe_allow_html=True)
    
    with st.expander("👥 Nama Karakter Utama & Penampilan Fisik!", expanded=True):
        num_total_char = st.number_input("Total Karakter", 1, 10, 2)
        all_chars_list = []
        for i in range(1, num_total_char + 1, 2):
            cols = st.columns(2)
            for idx_offset in range(2):
                idx = i + idx_offset
                if idx <= num_total_char:
                    with cols[idx_offset]:
                        name = st.text_input(f"Nama Karakter {idx}", key=f"c_name_{idx}_input")
                        desc = st.text_area(f"Fisik {idx}", key=f"c_desc_{idx}_input", height=120)
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
                loc_choice = st.selectbox(f"Loc{i_s}", options=options_lokasi, key=f"loc_sel_{i_s}", label_visibility="collapsed")
                location_val = st.text_input(f"Man{i_s}", key=f"loc_custom_{i_s}") if loc_choice == "--- KETIK MANUAL ---" else loc_choice
            adegan_storage.append({"num": i_s, "visual": visual_input, "light": light_val, "location": location_val, "cam": cam_val, "shot": shot_val, "angle": angle_val})

    # MEGA GENERATOR BUTTON
    if st.button("🚀 GENERATE ALL PROMPTS", type="primary", use_container_width=True):
        active_scenes = [a for a in adegan_storage if a["visual"].strip() != ""]
        if active_scenes:
            with st.spinner("Meracik prompt tajam..."):
                st.session_state.last_generated_results = []
                img_quality = "hyper-realistic 8k RAW photo, infinite depth of field, f/11 aperture, ultra-sharp focus, masterpiece quality."
                no_text = "STRICTLY NO text, NO typography, NO watermark, NO subtitles."

                for item in active_scenes:
                    v_low = item["visual"].lower()
                    mentioned = [f"[[ CHARACTER_{c['name'].upper()}: {c['desc']} ]]" for c in all_chars_list if c["name"] and re.search(rf'\b{re.escape(c["name"].lower())}\b', v_low)]
                    char_info = " AND ".join(mentioned) if mentioned else f"[[ CHARACTER_MAIN: {all_chars_list[0]['desc']} ]]"
                    
                    # Logika Genre
                    if genre_pilihan == "Pixar 3D": bumbu = "Disney Pixar style 3D animation, Octane render"
                    elif genre_pilihan == "Naruto (Ninja)": bumbu = "Naruto Shippuden anime style, bold ink lines"
                    else: bumbu = img_quality

                    p_img = f"RULE: {no_text}\nDATA: {char_info}\nACTION: {item['visual']}\nENV: {item['location']}\nTECH: {bumbu}, {shot_map[item['shot']]}, {angle_map[item['angle']]}"
                    p_vid = f"ULTRA-HD VIDEO: {char_info}, ACTION: {item['visual']}, GENRE: {genre_pilihan}, CAM: {item['cam']}"
                    
                    st.session_state.last_generated_results.append({"id": item["num"], "img": p_img, "vid": p_vid})
                
                record_to_sheets(st.session_state.active_user, active_scenes[0]["visual"], len(active_scenes))
                st.balloons()
                st.rerun()

    # --- BLOCK INI YANG TADI HILANG: AREA HASIL GENERATE ---
    if st.session_state.last_generated_results:
        st.divider()
        st.markdown(f"### 🎬 Hasil Prompt: {st.session_state.active_user.capitalize()} ❤️")
        
        for res in st.session_state.last_generated_results:
            done_key = f"mark_done_{res['id']}"
            is_done = st.session_state.get(done_key, False)
            status_tag = "✅ SELESAI" if is_done else "⏳ PROSES"
            
            with st.expander(f"{status_tag} | ADEGAN {res['id']}", expanded=not is_done):
                if is_done: st.success(f"Adegan {res['id']} Selesai!")
                
                c_img, c_vid = st.columns(2)
                with c_img:
                    st.markdown("**📸 PROMPT GAMBAR**")
                    st.code(res['img'], language="text")
                with c_vid:
                    st.markdown("**🎥 PROMPT VIDEO**")
                    st.code(res['vid'], language="text")
                
                st.checkbox("Tandai Adegan Selesai", key=done_key)

# ==============================================================================
# 6. HALAMAN 📊 MONITORING
# ==============================================================================
elif menu == "📊 MONITORING":
    st.header("📊 Monitoring Laporan")
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        df_log = conn.read(worksheet="Sheet1", ttl="0")
        st.dataframe(df_log.tail(30), use_container_width=True, hide_index=True)
    except: st.info("Gagal menarik data database...")

else:
    st.header(menu)
    st.info(f"Modul {menu} dalam tahap sinkronisasi.")
