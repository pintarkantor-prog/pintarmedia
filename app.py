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
# 0. SISTEM LOGIN TUNGGAL (FULL STABLE: 10-HOUR SESSION + NEW USER)
# ==============================================================================
st.set_page_config(page_title="PINTAR MEDIA", page_icon="🎬", layout="wide", initial_sidebar_state="expanded")

USER_PASSWORDS = {
    "admin": "QWERTY21ab",
    "icha": "udin99",
    "nissa": "tung22",
    "inggi": "udin33",
    "lisa": "tung66",
    "ezaalma": "aprihgino"
}

# --- 1. FITUR SINKRONISASI SESI & AUTO-RECOVERY (SOLUSI REFRESH) ---
if 'active_user' not in st.session_state:
    q_user = st.query_params.get("u")
    if q_user and q_user.lower() in USER_PASSWORDS:
        # LOGIKA PENYELAMAT: Jika user ada di URL, langsung pulihkan sesi
        # Ini yang membuat REFRESH tidak logout
        st.session_state.active_user = q_user.lower()
        if 'login_time' not in st.session_state:
            st.session_state.login_time = time.time()
        st.rerun() 
else:
    # Jaga agar URL tetap sinkron saat sedang bekerja
    if st.query_params.get("u") != st.session_state.active_user:
        st.query_params["u"] = st.session_state.active_user

# --- 2. LAYAR LOGIN (Hanya muncul jika recovery di atas gagal) ---
if 'active_user' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        st.write("")
        st.write("")
        
        # Penjepit tetap 1.8 agar ramping di layout Wide
        _, col_login, _ = st.columns([1.8, 1.0, 1.8]) 
        
        with col_login:
            try:
                st.image("PINTAR.png", use_container_width=True) 
            except:
                st.markdown("<h1 style='text-align: center;'>📸 PINTAR MEDIA</h1>", unsafe_allow_html=True)
            
            with st.form("login_form", clear_on_submit=False):
                # Prefill tetap ada buat user baru yang pertama kali masuk lewat link
                default_user = st.query_params.get("u", "")                
                user_input = st.text_input("Username", value=default_user, placeholder="Username...")
                pass_input = st.text_input("Password", type="password", placeholder="Password...")
                
                st.write("")
                submit_button = st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True, type="primary")
            
            if submit_button:
                user_clean = user_input.lower().strip()
                if user_clean in USER_PASSWORDS and pass_input == USER_PASSWORDS[user_clean]:
                    # 1. Simpan ke session
                    st.session_state.active_user = user_clean
                    st.session_state.login_time = time.time()
                    # 2. BERSIHKAN URL (Buang password & sampah lainnya)
                    st.query_params.clear() 
                    # 3. SET ULANG URL (Hanya nama user)
                    st.query_params["u"] = user_clean
                    
                    placeholder.empty() 
                    with placeholder.container():
                        st.write("")
                        st.markdown("<h3 style='text-align: center; color: #28a745;'>✅ AKSES DITERIMA!</h3>", unsafe_allow_html=True)
                        st.markdown(f"<h1 style='text-align: center;'>Selamat bekerja, {user_clean.capitalize()}!</h1>", unsafe_allow_html=True)
                        time.sleep(1.0)
                    st.rerun()
                else:
                    st.error("❌ Username atau Password salah.")
            
            st.caption("<p style='text-align: center;'>Secure Access - PINTAR MEDIA</p>", unsafe_allow_html=True)
    st.stop()

# --- 3. PROTEKSI SESI (AUTO-LOGOUT 10 JAM) ---
if 'active_user' in st.session_state and 'login_time' in st.session_state:
    selisih_detik = time.time() - st.session_state.login_time
    if selisih_detik > (10 * 60 * 60): # 10 Jam
        st.query_params.clear()
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ==============================================================================
# 1 & 2. INISIALISASI MEMORI & SINKRONISASI (CLEAN VERSION)
# ==============================================================================
# Mengambil user aktif dari session login
active_user = st.session_state.active_user 

# 1. Siapkan Lemari Hasil Generate
if 'last_generated_results' not in st.session_state:
    st.session_state.last_generated_results = []

# 2. Inisialisasi Identitas Tokoh (Default Kosong)
if 'c_name_1_input' not in st.session_state: st.session_state.c_name_1_input = ""
if 'c_desc_1_input' not in st.session_state: st.session_state.c_desc_1_input = ""
if 'c_name_2_input' not in st.session_state: st.session_state.c_name_2_input = ""
if 'c_desc_2_input' not in st.session_state: st.session_state.c_desc_2_input = ""

# 3. Inisialisasi Adegan v1 - v50 (SINKRON DENGAN BAGIAN 6)
for i in range(1, 51):
    for key, default in [
        (f"vis_input_{i}", ""),
        (f"light_input_{i}", "Siang"),
        (f"camera_input_{i}", "Diam (Tanpa Gerak)"),
        (f"shot_input_{i}", "Setengah Badan"),
        (f"angle_input_{i}", "Normal"),
        (f"loc_sel_{i}", "--- KETIK MANUAL ---"),
        (f"loc_custom_{i}", "")
    ]:
        if key not in st.session_state: 
            st.session_state[key] = default

# ==============================================================================
# 3. LOGIKA LOGGING GOOGLE SHEETS (SERVICE ACCOUNT MODE - FULL DATA)
# ==============================================================================
def record_to_sheets(user, data_packet, total_scenes):
    """Mencatat aktivitas. Jika data_packet adalah JSON (Draft), simpan utuh."""
    try:
        # 1. Koneksi (Gunakan TTL agar hemat kuota)
        conn = st.connection("gsheets", type=GSheetsConnection)
        
        # 2. Baca data lama (Kasih TTL agar tidak kena Error 429)
        existing_data = conn.read(worksheet="Sheet1", ttl="5m")
        
        # 3. Setting Waktu Jakarta (WIB)
        tz = pytz.timezone('Asia/Jakarta')
        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        
        # 4. Buat baris baru (PASTIKAN TIDAK ADA [:150])
        new_row = pd.DataFrame([{
            "Waktu": current_time,
            "User": user,
            "Total Adegan": total_scenes,
            "Visual Utama": data_packet 
        }])
        
        # 5. Gabungkan data lama dan baru
        updated_df = pd.concat([existing_data, new_row], ignore_index=True)
        
        # 6. Batasi history maksimal 300 baris agar tidak berat
        if len(updated_df) > 300:
            updated_df = updated_df.tail(300)
        
        # 7. Update kembali ke Google Sheets
        conn.update(worksheet="Sheet1", data=updated_df)
        
    except Exception as e:
        st.error(f"Gagal mencatat ke Cloud: {e}")

# ==============================================================================
# 3.5 INISIALISASI MESIN AI GEMINI (IDENTIK RUMAH LAMA)
# ==============================================================================
API_KEY = "AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"
try:
    genai.configure(api_key=API_KEY)
    available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available else 'models/gemini-pro'
    model = genai.GenerativeModel(model_name)
except: 
    pass

# ==============================================================================
# 4. CUSTOM CSS (VERSION: BOLD FOCUS & INSTANT RESPONSE)
# ==============================================================================
st.markdown("""
    <style>
    /* CSS Sultan Utuh di sini... */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-thumb { background: #1d976c; border-radius: 10px; }
    [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) {
        position: fixed; top: 0; left: 310px; right: 0; z-index: 99999;
        background-color: #0e1117; padding: 10px 2rem; border-bottom: 2px solid #31333f;
    }
    div.stButton > button[kind="primary"] { background: linear-gradient(to right, #1d976c, #11998e) !important; color: white !important; font-weight: bold; width: 100%; border-radius: 8px; }
    .staff-header-premium { background: rgba(29, 151, 108, 0.2) !important; border: 2px solid #1d976c !important; border-radius: 10px !important; padding: 15px 20px !important; margin-bottom: 25px; display: flex; align-items: center; gap: 12px; }
    .staff-header-premium b { color: #1d976c !important; font-size: 1.15em; }
    .small-label { color: #1d976c !important; letter-spacing: 1px; text-transform: uppercase; font-size: 10px !important; font-weight: 800 !important; }
    .stExpander { border: 1px solid rgba(29, 151, 108, 0.3) !important; border-radius: 12px !important; background-color: #161922 !important; margin-bottom: 15px !important; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 5. SIDEBAR & NAVIGASI (9 MENU)
# ==============================================================================
with st.sidebar:
    try: st.image("PINTAR.png", use_container_width=True)
    except: st.title("📸 PINTAR MEDIA")
    st.write(f"Staf Aktif: **{st.session_state.active_user.upper()}** ✅")
    st.divider()
    
    menu = st.radio("NAVIGASI UTAMA:", [
        "🏠 DASHBOARD", "🚀 PRODUCTION HUB", "🧠 AI LAB", 
        "🎞️ SCHEDULE", "📋 TEAM TASK", "📈 TREND ANALYZER", 
        "💡 IDEAS BANK", "👥 DATABASE LOCKER", "🛠️ COMMAND CENTER"
    ])
    st.divider()

    num_scenes = st.number_input("Tambah Jumlah Adegan", 1, 50, 6)
    
    list_genre = ["Realistik (Nyata)", "Pixar 3D", "Marvel Superhero", "Transformers (Mecha)", "KingKong (VFX Monster)", "Asphalt (Balap/Glossy)", "Ghibli (Estetik/Indah)", "Dragon Ball", "Doraemon 3D", "Naruto (Ninja)", "Tayo (Anak-anak)", "Sakura School (Anime)"]
    genre_saved = st.session_state.get("genre_pilihan_saved", "Realistik (Nyata)")
    genre_pilihan = st.selectbox("Pilih Gaya Film:", options=list_genre, index=list_genre.index(genre_saved) if genre_saved in list_genre else 0)

    # --- TOMBOL SAVE & LOAD ---
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
                        st.session_state[f"c_name_{i_str}_input"] = val.get("name", "")
                        st.session_state[f"c_desc_{i_str}_input"] = val.get("desc", "")
                    for i_str, val in data.get("scenes", {}).items():
                        if isinstance(val, dict):
                            st.session_state[f"vis_input_{i_str}"] = val.get("vis", "")
                            st.session_state[f"light_input_{i_str}"] = val.get("light", "Siang")
                            st.session_state[f"shot_input_{i_str}"] = val.get("shot", "Setengah Badan")
                            st.session_state[f"angle_input_{i_str}"] = val.get("angle", "Normal")
                            st.session_state[f"loc_sel_{i_str}"] = val.get("loc", "jalan kampung")
                    for k, v in data.get("dialogs", {}).items(): st.session_state[k] = v
                    st.rerun()
            except: st.error("Draft kosong.")

    if st.button("KELUAR SISTEM ⚡", use_container_width=True):
        st.query_params.clear()
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

# ==============================================================================
# 6. MAPPING & DNA LOKASI (IDENTIK RUMAH LAMA)
# ==============================================================================
indonesia_camera = ["Diam (Tanpa Gerak)", "Ikuti Karakter", "Zoom Masuk", "Zoom Keluar", "Memutar (Orbit)"]
indonesia_shot = ["Sangat Dekat", "Dekat Wajah", "Setengah Badan", "Seluruh Badan", "Pemandangan Luas", "Drone Shot"]
indonesia_angle = ["Normal", "Sudut Rendah", "Sudut Tinggi", "Samping", "Berhadapan", "Intip Bahu", "Belakang"]
options_lighting = ["Pagi", "Siang", "Sore", "Malam"]

LOKASI_DNA = {
    "jalan kampung": "shabby dirt road in Indonesian village, dense banana trees, microscopic dust particles, weathered textures, ultra-detailed gravel and soil.",
    "jalan kota kecil": "rugged asphalt road, weathered 90s shophouses with peeling paint, messy tangled electricity wires, sharp urban grit, high-contrast textures.",
    "jalan kota besar": "metropolitan concrete highway, towering skyscrapers, hazy city smog, heavy metallic traffic, cinematic urban depth, sharp architectural edges.",
    "pasar": "authentic Indonesian wet market, wet muddy floor textures, vibrant organic produce, detailed wicker baskets, crowded stall textures, hyper-realistic.",
    "halaman rumah": "old front yard, potted frangipani trees with detailed bark, cracked cement floor with moss, tactile ground grit, ultra-sharp outdoor environment.",
    "teras rumah kaya": "modern minimalist mansion terrace, premium marble floor reflections, manicured garden details, sleek luxury aesthetic, sharp clean lines.",
    "dalam rumah kaya": "high-end luxury living room, polished stone textures, floor-to-ceiling glass walls, premium leather sofa grain, sharp interior design clarity."
}
options_lokasi = ["--- KETIK MANUAL ---"] + list(LOKASI_DNA.keys())

shot_map = {"Sangat Dekat": "Extreme Close-Up shot, macro photography, hyper-detailed micro textures", "Dekat Wajah": "Close-Up shot, focus on facial expressions and skin details", "Setengah Badan": "Medium Shot, waist-up framing, cinematic depth", "Seluruh Badan": "Full body shot, head-to-toe framing, environment visible", "Pemandangan Luas": "Wide landscape shot, expansive scenery, subject is small in frame", "Drone Shot": "Cinematic Aerial Drone shot, high altitude, bird's-eye view from above"}
angle_map = {"Normal": "eye-level shot, straight on perspective, natural head-on view", "Sudut Rendah": "heroic low angle shot, looking up from below, monumental framing", "Sudut Tinggi": "high angle shot, looking down at the subject, making it look smaller", "Samping": "side profile view, 90-degree side angle, parallel to camera, full profile perspective", "Berhadapan": "dual profile view, two subjects facing each other, face-to-face, symmetrical", "Intip Bahu": "over-the-shoulder shot, foreground shoulder blur, cinematic dialogue depth", "Belakang": "shot from behind, back view, following the subject, looking away from camera"}

# ==============================================================================
# 7. LOGIKA MENU: DASHBOARD
# ==============================================================================
if menu == "🏠 DASHBOARD":
    st.header("🏠 Dashboard Utama")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("#### 📅 Log Aktivitas Terbaru")
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            df_monitor = conn.read(worksheet="Sheet1", ttl="0")
            st.dataframe(df_monitor.tail(10), use_container_width=True, hide_index=True)
        except: st.info("Sinkronisasi database...")
    with col2:
        st.markdown("#### 🏆 Top Staf (MVP)")
        try:
            mvp_count = df_monitor['User'].value_counts().reset_index()
            mvp_count.columns = ['Staf', 'Total']
            st.dataframe(mvp_count, use_container_width=True, hide_index=True)
        except: pass

# ==============================================================================
# 8. LOGIKA MENU: PRODUCTION HUB (STORYBOARD TOTAL & PROMPT GEN)
# ==============================================================================
elif menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    st.markdown(f"""<div class="staff-header-premium"><span style="font-size:20px;">👤</span><div><b>Staf Aktif: {st.session_state.active_user.capitalize()}</b> | <span style="color:#aaa; font-style:italic;">Konten yang mantap lahir dari detail adegan yang tepat 🚀🚀</span></div></div>""", unsafe_allow_html=True)
    
    st.subheader("📝 Detail Adegan Storyboard")
    with st.expander("👥 Nama Karakter Utama & Penampilan Fisik!", expanded=True):
        num_total_char = st.number_input("Total Karakter Utama", 1, 10, 2)
        all_chars_list = []
        for i in range(1, num_total_char + 1, 2):
            cols = st.columns(2)
            for idx_offset in range(2):
                idx = i + idx_offset
                if idx <= num_total_char:
                    with cols[idx_offset]:
                        name = st.text_input(f"Nama {idx}", key=f"c_name_{idx}_input")
                        desc = st.text_area(f"Fisik {idx}", key=f"c_desc_{idx}_input", height=120)
                        all_chars_list.append({"name": name, "desc": desc})

    adegan_storage = []
    for i_s in range(1, int(num_scenes) + 1):
        with st.expander(f"🎬 ADEGAN {i_s}", expanded=(i_s == 1)):
            col_v, col_ctrl = st.columns([6, 4])
            with col_v:
                visual_input = st.text_area(f"Cerita Visual {i_s}", key=f"vis_input_{i_s}", height=265)
            with col_ctrl:
                r1 = st.columns(2)
                with r1[0]: 
                    st.markdown('<p class="small-label">💡 Suasana</p>', unsafe_allow_html=True)
                    light_val = st.selectbox(f"L{i_s}", options_lighting, key=f"light_input_{i_s}", label_visibility="collapsed")
                with r1[1]:
                    st.markdown('<p class="small-label">📐 Shot</p>', unsafe_allow_html=True)
                    shot_val = st.selectbox(f"S{i_s}", indonesia_shot, key=f"shot_input_{i_s}", label_visibility="collapsed")
                r2 = st.columns(2)
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

    # --- MEGA GENERATOR PROMPT (IDENTIK RUMAH LAMA) ---
    if st.button("🚀 GENERATE ALL PROMPTS", type="primary"):
        active_scenes = [a for a in adegan_storage if a["visual"].strip() != ""]
        if active_scenes:
            with st.spinner("Meracik prompt tajam..."):
                st.session_state.last_generated_results = []
                img_quality_stack = "hyper-realistic 8k RAW photo, infinite depth of field, f/11 aperture, zero bokeh, zero background blur, sharp edge-enhancement, non-filtered, ultra-clear optical clarity, tactile textures, masterpiece quality."
                no_text_strict = "STRICTLY NO text, NO typography, NO watermark, NO letters, NO subtitles, NO captions, NO speech bubbles, NO dialogue boxes."

                for item in active_scenes:
                    v_text_low = item["visual"].lower()
                    mentioned = [f"[[ CHARACTER_{c['name'].upper()}: {c['desc']} ]]" for c in all_chars_list if c["name"] and re.search(rf'\b{re.escape(c["name"].lower())}\b', v_text_low)]
                    char_info = " AND ".join(mentioned) if mentioned else f"[[ CHARACTER_MAIN: {all_chars_list[0]['desc']} ]]"

                    # BUMBU GAYA
                    if genre_pilihan == "Pixar 3D": bumbu_gaya = "Disney Pixar style 3D animation, Octane render, ray-traced global illumination"
                    elif genre_pilihan == "Marvel Superhero": bumbu_gaya = "Marvel Cinematic Universe aesthetic, heroic cinematic lighting"
                    elif genre_pilihan == "Transformers (Mecha)": bumbu_gaya = "Michael Bay cinematic style, Transformers mechanical realism"
                    elif genre_pilihan == "KingKong (VFX Monster)": bumbu_gaya = "Photorealistic CGI, ILM blockbuster VFX quality"
                    elif genre_pilihan == "Asphalt (Balap/Glossy)": bumbu_gaya = "Asphalt 9 gaming aesthetic, ultra-glossy metallic paint"
                    elif genre_pilihan == "Ghibli (Estetik/Indah)": bumbu_gaya = "Studio Ghibli hand-painted style, watercolor textures"
                    elif genre_pilihan == "Dragon Ball": bumbu_gaya = "Dragon Ball Super anime style, sharp ink lineart"
                    elif genre_pilihan == "Doraemon 3D": bumbu_gaya = "Stand By Me Doraemon style, high-end 3D CGI"
                    elif genre_pilihan == "Naruto (Ninja)": bumbu_gaya = "Naruto Shippuden anime style, bold ink lines"
                    elif genre_pilihan == "Tayo (Anak-anak)": bumbu_gaya = "3D CGI animation for kids, Tayo aesthetic"
                    elif genre_pilihan == "Sakura School (Anime)": bumbu_gaya = "Sakura School Simulator style, high-quality 3D anime game graphics"
                    else: bumbu_gaya = img_quality_stack

                    dna_env = LOKASI_DNA.get(item["location"].lower(), f"{item['location']}, sharp focus.")
                    prompt_img = f"STRICT VISUAL RULE: {no_text_strict}\nCHARACTER: {char_info}\nACTION: {item['visual']}\nENV: {dna_env}\nCAM: {shot_map[item['shot']]}, {angle_map[item['angle']]}\nTECH: {bumbu_gaya}"
                    st.session_state.last_generated_results.append({"id": item["num"], "img": prompt_img})
                
                record_to_sheets(st.session_state.active_user, active_scenes[0]["visual"], len(active_scenes))
                st.rerun()

    if st.session_state.last_generated_results:
        for res in st.session_state.last_generated_results:
            with st.expander(f"ADEGAN {res['id']}"):
                st.code(res["img"])

# --- MENU LAIN ---
else:
    st.header(menu)
    st.info("Fitur sedang disinkronisasi V2.")
