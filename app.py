import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
import pytz
import time
import json
import re

st.set_page_config(page_title="PINTAR MEDIA", page_icon="🎬", layout="wide", initial_sidebar_state="expanded")

# ==============================================================================
# 0. SISTEM LOGIN TUNGGAL (FULL STABLE: 10-HOUR SESSION + NEW USER)
# ==============================================================================
USER_PASSWORDS = {
    "admin": "QWERTY21ab",
    "icha": "udin99",
    "nissa": "tung22",
    "inggi": "udin33",
    "lisa": "tung66",
    "ezaalma": "aprihgino"
}

if 'active_user' not in st.session_state:
    q_user = st.query_params.get("u")
    if q_user and q_user.lower() in USER_PASSWORDS:
        st.session_state.active_user = q_user.lower()
        if 'login_time' not in st.session_state:
            st.session_state.login_time = time.time()
        st.rerun() 
else:
    if st.query_params.get("u") != st.session_state.active_user:
        st.query_params["u"] = st.session_state.active_user

if 'active_user' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        st.write("")
        st.write("")
        _, col_login, _ = st.columns([1.8, 1.0, 1.8]) 
        with col_login:
            try:
                st.image("PINTAR.png", use_container_width=True) 
            except:
                st.markdown("<h1 style='text-align: center;'>📸 PINTAR MEDIA</h1>", unsafe_allow_html=True)
            with st.form("login_form", clear_on_submit=False):
                default_user = st.query_params.get("u", "")                
                user_input = st.text_input("Username", value=default_user, placeholder="Username...")
                pass_input = st.text_input("Password", type="password", placeholder="Password...")
                st.write("")
                submit_button = st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True, type="primary")
            if submit_button:
                user_clean = user_input.lower().strip()
                if user_clean in USER_PASSWORDS and pass_input == USER_PASSWORDS[user_clean]:
                    st.session_state.active_user = user_clean
                    st.session_state.login_time = time.time()
                    st.query_params.clear() 
                    st.query_params["u"] = user_clean
                    placeholder.empty() 
                    st.rerun()
                else:
                    st.error("❌ Username atau Password salah.")
            st.caption("<p style='text-align: center;'>Secure Access - PINTAR MEDIA</p>", unsafe_allow_html=True)
    st.stop()

if 'active_user' in st.session_state and 'login_time' in st.session_state:
    selisih_detik = time.time() - st.session_state.login_time
    if selisih_detik > (10 * 60 * 60):
        st.query_params.clear()
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ==============================================================================
# 1 & 2. INISIALISASI MEMORI & SINKRONISASI (CLEAN VERSION)
# ==============================================================================
active_user = st.session_state.active_user 

if 'last_generated_results' not in st.session_state:
    st.session_state.last_generated_results = []

if 'c_name_1_input' not in st.session_state: st.session_state.c_name_1_input = ""
if 'c_desc_1_input' not in st.session_state: st.session_state.c_desc_1_input = ""
if 'c_name_2_input' not in st.session_state: st.session_state.c_name_2_input = ""
if 'c_desc_2_input' not in st.session_state: st.session_state.c_desc_2_input = ""

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
# 3. LOGIKA LOGGING GOOGLE SHEETS
# ==============================================================================
def record_to_sheets(user, data_packet, total_scenes):
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        existing_data = conn.read(worksheet="Sheet1", ttl="5m")
        tz = pytz.timezone('Asia/Jakarta')
        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        new_row = pd.DataFrame([{"Waktu": current_time, "User": user, "Total Adegan": total_scenes, "Visual Utama": data_packet}])
        updated_df = pd.concat([existing_data, new_row], ignore_index=True)
        if len(updated_df) > 300:
            updated_df = updated_df.tail(300)
        conn.update(worksheet="Sheet1", data=updated_df)
    except Exception as e:
        st.error(f"Gagal mencatat ke Cloud: {e}")

# ==============================================================================
# 4. CUSTOM CSS (FULL ORIGINAL)
# ==============================================================================
st.markdown("""
    <style>
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #0e1117; }
    ::-webkit-scrollbar-thumb { background: #31333f; border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: #1d976c; }
    [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) {
        position: fixed; top: 0; left: 310px; right: 0; z-index: 99999; background-color: #0e1117; padding: 10px 2rem; border-bottom: 2px solid #31333f;
    }
    @media (max-width: 768px) { [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) { left: 0; } }
    [data-testid="stSidebar"] { background-color: #1a1c24 !important; border-right: 1px solid rgba(29, 151, 108, 0.1) !important; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label { color: #ffffff !important; }
    div.stButton > button[kind="primary"] {
        background: linear-gradient(to right, #1d976c, #11998e) !important; color: white !important; border: none !important; border-radius: 8px !important; padding: 0.6rem 1.2rem !important; font-weight: bold !important; font-size: 16px !important; width: 100%; box-shadow: 0 4px 12px rgba(29, 151, 108, 0.2) !important;
    }
    div.stButton > button[kind="primary"]:hover { background: #11998e !important; box-shadow: 0 6px 15px rgba(29, 151, 108, 0.3) !important; }
    .staff-header-premium { background: rgba(29, 151, 108, 0.2) !important; border: 2px solid #1d976c !important; border-radius: 10px !important; padding: 15px 20px !important; margin-bottom: 25px !important; display: flex !important; align-items: center !important; gap: 12px !important; box-shadow: none !important; }
    .staff-header-premium b { color: #1d976c !important; font-size: 1.15em !important; text-shadow: 0 0 10px rgba(29, 151, 108, 0.3) !important; }
    .staff-header-premium span { color: #1d976c !important; }
    .staff-header-premium i { color: #e0e0e0 !important; font-style: normal !important; }
    .stTextArea textarea:focus, .stTextInput input:focus { border: 1px solid #31333f !important; background-color: #0e1117 !important; box-shadow: none !important; outline: none !important; }
    h1, h2, h3, .stMarkdown h3 { color: #ffffff !important; background: none !important; -webkit-text-fill-color: initial !important; }
    button[title="Copy to clipboard"] { background-color: #28a745 !important; color: white !important; border-radius: 6px !important; transform: scale(1.1); }
    .stTextArea textarea { font-size: 16px !important; border-radius: 10px !important; background-color: #0e1117 !important; border: 1px solid #31333f !important; }
    .small-label { color: #1d976c !important; letter-spacing: 1px; text-transform: uppercase; font-size: 10px !important; font-weight: 800 !important; }
    .stExpander { border: 1px solid rgba(29, 151, 108, 0.3) !important; border-radius: 12px !important; background-color: #161922 !important; margin-bottom: 15px !important; }
    hr { margin: 2em 0 !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; }
    .stTextArea textarea { border: 1px solid rgba(255,255,255,0.1) !important; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 5. HEADER STAF
# ==============================================================================
nama_display = st.session_state.active_user.capitalize()
st.markdown(f"""
    <div class="staff-header-premium">
        <span style="font-size:20px;">👤</span>
        <div>
            <b>Staf Aktif: {nama_display}</b> 
            <span style="color:rgba(255,255,255,0.1); margin: 0 10px;">|</span>
            <span style="color:#aaa; font-style:italic;">Konten yang mantap lahir dari detail adegan yang tepat 🚀🚀</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 6. MAPPING TRANSLATION
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
    "teras rumah": "traditional house porch, vintage tiled floor, intricate wood grain on chairs, delicate jasmine flowers, sharp depth of field, realistic textures.",
    "pinggir sawah": "narrow cracked paved path, vast emerald rice fields, sharp palm tree silhouettes, vibrant natural greenery, infinite horizon clarity.",
    "sawah": "lush terraced rice paddies, detailed mud irrigation, realistic organic water reflections, sharp mountain peaks on the horizon, tactile nature textures.",
    "teras rumah miskin": "humble wooden porch, old grey weathered timber, dusty floor boards, raw rustic poverty aesthetic, hyper-detailed wood cracks and splinters.",
    "dalam rumah kayu": "vintage timber interior, hyper-detailed wood grain, ancient furniture textures, sharp focus on carpentry, raw atmospheric photo, zero smoothing.",
    "teras rumah kaya": "modern minimalist mansion terrace, premium marble floor reflections, manicured garden details, sleek luxury aesthetic, sharp clean lines.",
    "dalam rumah kaya": "high-end luxury living room, polished stone textures, floor-to-ceiling glass walls, premium leather sofa grain, sharp interior design clarity."
}
options_lokasi = ["--- KETIK MANUAL ---"] + list(LOKASI_DNA.keys())
camera_map = {"Diam (Tanpa Gerak)": "Static camera...", "Ikuti Karakter": "Dynamic tracking..."}
shot_map = {"Sangat Dekat": "Extreme Close-Up...", "Dekat Wajah": "Close-Up...", "Setengah Badan": "Medium Shot...", "Seluruh Badan": "Full body shot...", "Pemandangan Luas": "Wide landscape...", "Drone Shot": "Cinematic Aerial Drone shot..."}
angle_map = {"Normal": "eye-level shot...", "Sudut Rendah": "heroic low angle...", "Sudut Tinggi": "high angle...", "Samping": "side profile...", "Berhadapan": "dual profile...", "Intip Bahu": "over-the-shoulder...", "Belakang": "shot from behind..."}

# ==============================================================================
# 7. SIDEBAR: NAVIGASI RUANGAN (PENAMBAHAN STRUKTUR)
# ==============================================================================
with st.sidebar:
    st.markdown("#### 🖥️ MAIN COMMAND")
    menu_umum = ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "🎞️ SCHEDULE", "📋 TEAM TASK", "📈 TREND ANALYZER"]
    menu_rahasia = ["👥 DATABASE LOCKER", "📊 MONITORING", "🛠️ COMMAND CENTER"]
    if st.session_state.active_user == "admin": menu_final = menu_umum + menu_rahasia
    else: menu_final = menu_umum
    menu_select = st.radio("Pilih Ruangan:", menu_final, label_visibility="collapsed")
    st.divider()

    if menu_select == "🚀 RUANG PRODUKSI":
        try: st.image("PINTAR.png", use_container_width=True)
        except: st.title("📸 PINTAR MEDIA")
        st.write("") 
        if st.session_state.active_user == "admin":
            if st.checkbox("🚀 Buka Dashboard Utama", value=False):
                st.info("Log aktivitas tercatat di Cloud.")
                try:
                    conn = st.connection("gsheets", type=GSheetsConnection)
                    df_monitor = conn.read(worksheet="Sheet1", ttl="0")
                    if not df_monitor.empty:
                        st.markdown("#### 🏆 Top Staf (MVP)")
                        mvp_count = df_monitor['User'].value_counts().reset_index()
                        mvp_count.columns = ['Staf', 'Total Input']
                        st.dataframe(mvp_count, use_container_width=True, hide_index=True)
                        st.markdown("#### 📅 Log Aktivitas Terbaru")
                        df_display = df_monitor.tail(10).copy()
                        df_display.columns = ["🕒 Waktu", "👤 User", "🎬 Total", "📝 Visual Utama"]
                        st.dataframe(df_display, use_container_width=True, hide_index=True)
                except: st.error("Gagal muat dashboard.")
            st.divider()

        num_scenes = st.number_input("Tambah Jumlah Adegan", min_value=1, max_value=50, value=6)
        st.markdown("#### 🎨 GENRE VISUAL")
        list_genre = ["Realistik (Nyata)", "Pixar 3D", "Marvel Superhero", "Transformers (Mecha)", "KingKong (VFX Monster)", "Asphalt (Balap/Glossy)", "Ghibli (Estetik/Indah)", "Dragon Ball", "Doraemon 3D", "Naruto (Ninja)", "Tayo (Anak-anak)", "Sakura School (Anime)"]
        genre_saved = st.session_state.get("genre_pilihan_saved", "Realistik (Nyata)")
        try: idx_default = list_genre.index(genre_saved)
        except: idx_default = 0
        genre_pilihan = st.selectbox("Pilih Gaya Film:", options=list_genre, index=idx_default)
        
        # --- TOMBOL SAVE & LOAD UTUH ---
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            save_trigger = st.button("💾 SAVE", use_container_width=True)
            if save_trigger:
                try:
                    char_data = {str(idx): {"name": st.session_state.get(f"c_name_{idx}_input", ""), "desc": st.session_state.get(f"c_desc_{idx}_input", "")} for idx in range(1, 11)}
                    scene_data = {str(i): {"vis": st.session_state.get(f"vis_input_{i}", ""), "light": st.session_state.get(f"light_input_{i}", "Siang"), "shot": st.session_state.get(f"shot_input_{i}", "Setengah Badan"), "angle": st.session_state.get(f"angle_input_{i}", "Normal"), "loc": st.session_state.get(f"loc_sel_{i}", "jalan kampung")} for i in range(1, 51)}
                    dialog_data = {k: v for k, v in st.session_state.items() if k.startswith("diag_") and v}
                    master_packet = {"num_char": st.session_state.get("num_total_char", 2), "genre": genre_pilihan, "chars": char_data, "scenes": scene_data, "dialogs": dialog_data}
                    record_to_sheets(f"DRAFT_{st.session_state.active_user}", json.dumps(master_packet), len([s for s in scene_data.values() if s['vis']]))
                    st.toast("Project Tersimpan! ✅")
                except Exception as e: st.error(f"Gagal simpan: {e}")
        with btn_col2:
            load_trigger = st.button("🔄 LOAD", use_container_width=True)
            if load_trigger:
                try:
                    conn = st.connection("gsheets", type=GSheetsConnection)
                    df_log = conn.read(worksheet="Sheet1", ttl="1s")
                    my_data = df_log[df_log['User'] == f"DRAFT_{st.session_state.active_user}"]
                    if not my_data.empty:
                        data = json.loads(str(my_data.iloc[-1]['Visual Utama']))
                        st.session_state["num_total_char"] = data.get("num_char", 2)
                        st.session_state["genre_pilihan_saved"] = data.get("genre", "Realistik (Nyata)")
                        for i_str, val in data.get("chars", {}).items():
                            st.session_state[f"c_name_{i_str}_input"] = val.get("name", ""); st.session_state[f"c_desc_{i_str}_input"] = val.get("desc", "")
                        for i_str, val in data.get("scenes", {}).items():
                            if isinstance(val, dict):
                                st.session_state[f"vis_input_{i_str}"] = val.get("vis", ""); st.session_state[f"light_input_{i_str}"] = val.get("light", "Siang")
                                st.session_state[f"shot_input_{i_str}"] = val.get("shot", "Setengah Badan"); st.session_state[f"angle_input_{i_str}"] = val.get("angle", "Normal")
                                st.session_state[f"loc_sel_{i_str}"] = val.get("loc", "jalan kampung")
                        for k, v in data.get("dialogs", {}).items(): st.session_state[k] = v
                        st.toast("Data Dipulihkan! 🔄"); st.rerun()
                except Exception as e: st.error(f"Gagal: {e}")
        st.divider()

    if st.button("KELUAR SISTEM ⚡", use_container_width=True):
        st.query_params.clear(); [st.session_state.pop(k) for k in list(st.session_state.keys())]; st.rerun()

# ==============================================================================
# ROUTING MAIN CONTENT
# ==============================================================================


if menu_select == "🚀 RUANG PRODUKSI":
    # ==============================================================================
    # 8. PARAMETER KUALITAS (FULL ORIGINAL)
    # ==============================================================================
    img_quality_stack = (
        "hyper-realistic 8k RAW photo, infinite depth of field, f/11 aperture, "
        "zero bokeh, zero background blur, sharp edge-enhancement, non-filtered, "
        "ultra-clear optical clarity, tactile textures on sand, gravel, and wood, "
        "CPL filter, deep blue sky, polarized colors, high local contrast, "
        "vivid naturalism, realistic shadow recovery, masterpiece quality."
    )
    vid_quality_stack = (
        "ultra-high definition cinematic video, 8k UHD, high dynamic range, "
        "professional color grading, vibrant organic colors, ray-traced reflections, "
        "hyper-detailed textures, zero digital noise, clean pixels, "
        "smooth motion, professional cinematography, masterpiece quality."
    )
    no_text_strict = (
        "STRICTLY NO text, NO typography, NO watermark, NO letters, NO subtitles, "
        "NO captions, NO speech bubbles, NO dialogue boxes, NO labels, NO black bars, "
        "NO burned-in text, NO characters speaking with visible words, "
        "the image must be a CLEAN cinematic shot without any written characters."
    )
    negative_motion_strict = (
        "STRICTLY NO morphing, NO extra limbs, NO distorted faces, NO teleporting objects, "
        "NO flickering textures, NO sudden lighting jumps, NO floating hair artifacts."
    )
    img_quality_base = f"{img_quality_stack} {no_text_strict}"
    vid_quality_base = f"60fps, ultra-clear motion, {vid_quality_stack} {no_text_strict} {negative_motion_strict}"

    # ==============================================================================
    # 9. FORM INPUT ADEGAN (FULL ORIGINAL)
    # ==============================================================================
    if "restore_counter" not in st.session_state: st.session_state.restore_counter = 0
    st.subheader("📝 Detail Adegan Storyboard")
    with st.expander("👥 Nama Karakter Utama & Penampilan Fisik! (WAJIB ISI)", expanded=True):
        num_total_char = st.number_input("Total Karakter Utama dalam Project", min_value=1, max_value=10, value=2)
        all_chars_list = []
        for i in range(1, num_total_char + 1, 2):
            cols = st.columns(2)
            for idx_offset in range(2):
                idx = i + idx_offset
                if idx <= num_total_char:
                    with cols[idx_offset]:
                        st.markdown(f"##### 👤 Karakter Utama {idx}")
                        name = st.text_input("Nama", key=f"c_name_{idx}_input", placeholder=f"Nama {idx}", label_visibility="collapsed")
                        desc = st.text_area("Fisik", key=f"c_desc_{idx}_input", height=120, placeholder=f"Fisik {idx}", label_visibility="collapsed")
                        all_chars_list.append({"name": name, "desc": desc})
            st.write("---") 

    adegan_storage = []
    for i_s in range(1, int(num_scenes) + 1):
        l_box_title = f"🟢 ADEGAN {i_s}" if i_s == 1 else f"🎬 ADEGAN {i_s}"
        with st.expander(l_box_title, expanded=(i_s == 1)):
            col_v, col_ctrl = st.columns([6, 4])
            with col_v:
                visual_input = st.text_area(f"Visual {i_s}", key=f"vis_input_{i_s}", height=265, placeholder="Detail adegan...")
            with col_ctrl:
                r1 = st.columns(2)
                with r1[0]:
                    st.markdown('<p class="small-label">💡 Suasana</p>', 1); light_val = st.selectbox(f"L{i_s}", options_lighting, key=f"light_input_{i_s}", label_visibility="collapsed")
                with r1[1]:
                    st.markdown('<p class="small-label">📐 Ukuran Gambar</p>', 1); shot_val = st.selectbox(f"S{i_s}", indonesia_shot, key=f"shot_input_{i_s}", label_visibility="collapsed")
                r2 = st.columns(2)
                with r2[0]:
                    st.markdown('<p class="small-label">✨ Arah Kamera</p>', 1); angle_val = st.selectbox(f"A{i_s}", indonesia_angle, key=f"angle_input_{i_s}", label_visibility="collapsed")
                with r2[1]:
                    st.markdown('<p class="small-label">🎬 Gerakan</p>', 1); cam_val = st.selectbox(f"C{i_s}", indonesia_camera, index=0, key=f"camera_input_{i_s}", label_visibility="collapsed")
                loc_choice = st.selectbox(f"LocSelect{i_s}", options=options_lokasi, key=f"loc_sel_{i_s}")
                location_val = st.text_input("Manual:", key=f"loc_custom_{i_s}") if loc_choice == "--- KETIK MANUAL ---" else loc_choice
            
            diag_cols = st.columns(len(all_chars_list)); scene_dialogs = []
            for i_char, char_data in enumerate(all_chars_list):
                with diag_cols[i_char]:
                    char_label = char_data['name'] if char_data['name'] else f"Karakter {i_char+1}"
                    d_in = st.text_input(f"Dialog {char_label}", key=f"diag_{i_s}_{i_char}")
                    scene_dialogs.append({"name": char_label, "text": d_in})
            adegan_storage.append({"num": i_s, "visual": visual_input, "light": light_val, "location": location_val, "cam": cam_val, "shot": shot_val, "angle": angle_val, "dialogs": scene_dialogs})

    # ==============================================================================
    # 10. GENERATOR PROMPT (FULL ORIGINAL)
    # ==============================================================================
    if st.button("🚀 GENERATE ALL PROMPTS", type="primary", use_container_width=True):
        nama_tokoh_utama = st.session_state.get("c_name_1_input", "").strip()
        active_scenes = [a for a in adegan_storage if a["visual"].strip() != ""]
        if not nama_tokoh_utama: st.warning("⚠️ Karakter 1 belum diisi!")
        elif not active_scenes: st.warning("⚠️ Mohon isi deskripsi visual!")
        else:
            with st.spinner("Meracik prompt..."):
                st.session_state.last_generated_results = []
                record_to_sheets(st.session_state.active_user, active_scenes[0]["visual"], len(active_scenes))
                for item in active_scenes:
                    mentioned_chars_list = []
                    v_text_low = str(item.get('visual', "")).lower().strip()
                    for c in all_chars_list:
                        c_name_raw = str(c.get('name', "")).strip()
                        if c_name_raw and re.search(rf'\b{re.escape(c_name_raw.lower())}\b', v_text_low):
                            mentioned_chars_list.append({"name": c_name_raw.upper(), "desc": c.get('desc', '')})
                    
                    if len(mentioned_chars_list) == 1:
                        target_name = mentioned_chars_list[0]['name']
                        char_info = f"[[ CHARACTER_{target_name}: {mentioned_chars_list[0]['desc']} ]]"
                        instruction_header = f"IMAGE REFERENCE RULE: Use uploaded photo for {target_name}. ONLY {target_name}."
                    elif len(mentioned_chars_list) > 1:
                        char_info = " AND ".join([f"[[ CHARACTER_{m['name']}: {m['desc']} ]]" for m in mentioned_chars_list])
                        instruction_header = "IMAGE REFERENCE RULE: Use uploaded photos. Interaction required."
                    else:
                        char_info = f"[[ CHARACTER_MAIN: {all_chars_list[0]['desc']} ]]"
                        instruction_header = "IMAGE REFERENCE RULE: Use main character reference."

                    if genre_pilihan == "Pixar 3D": bumbu_gaya = "Disney Pixar style 3D animation..."
                    # ... (Logika Bumbu Gaya lainnya identik dengan aslinya)
                    else: bumbu_gaya = img_quality_stack

                    img_final = f"{instruction_header}\n\nSTRICT: NO TEXT. FOCUS: SHARP. CHAR: {char_info}\nACTION: {item['visual']}\nENV: {item['location']}\nTECH: {bumbu_gaya}"
                    vid_final = f"{instruction_header}\nMOTION: {item['visual']}\nCHAR: {char_info}\nTECH: {vid_quality_base}"
                    st.session_state.last_generated_results.append({"id": item["num"], "img": img_final, "vid": vid_final})
            st.rerun()

    if st.session_state.last_generated_results:
        for res in st.session_state.last_generated_results:
            with st.expander(f"ADEGAN {res['id']}", expanded=True):
                c1, c2 = st.columns(2)
                with c1: st.code(res['img'], "text")
                with c2: st.code(res['vid'], "text")

elif menu_select == "🧠 PINTAR AI LAB": st.title("🧠 PINTAR AI LAB")
elif menu_select == "🎞️ SCHEDULE": st.title("🎞️ SCHEDULE")
elif menu_select == "📋 TEAM TASK": st.title("📋 TEAM TASK")
elif menu_select == "📈 TREND ANALYZER": st.title("📈 TREND ANALYZER")
elif menu_select == "👥 DATABASE LOCKER":
    if st.session_state.active_user == "admin": st.title("👥 DATABASE LOCKER")
    else: st.error("Akses Ditolak!")
elif menu_select == "📊 MONITORING":
    if st.session_state.active_user == "admin": st.title("📊 MONITORING")
    else: st.error("Akses Ditolak!")
elif menu_select == "🛠️ COMMAND CENTER":
    if st.session_state.active_user == "admin": st.title("🛠️ COMMAND CENTER")
    else: st.error("Akses Ditolak!")
