import streamlit as st
import google.generativeai as genai
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
import pytz
import time
import json
import re

# ==============================================================================
# 1. KONFIGURASI HALAMAN & LOGIN (MIGRASI TOTAL DARI RUMAH LAMA)
# ==============================================================================
st.set_page_config(page_title="PINTAR MEDIA V2", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")

USER_PASSWORDS = {
    "admin": "QWERTY21ab", "icha": "udin99", "nissa": "tung22",
    "inggi": "udin33", "lisa": "tung66", "ezaalma": "aprihgino"
}

# --- FITUR SINKRONISASI SESI & AUTO-RECOVERY ---
if 'active_user' not in st.session_state:
    q_user = st.query_params.get("u")
    if q_user and q_user.lower() in USER_PASSWORDS:
        st.session_state.active_user = q_user.lower()
        st.session_state.login_time = time.time()
        st.rerun()

# --- LAYAR LOGIN ---
if 'active_user' not in st.session_state:
    _, col_login, _ = st.columns([1.8, 1.0, 1.8])
    with col_login:
        try: st.image("PINTAR.png", use_container_width=True)
        except: st.markdown("<h1 style='text-align: center;'>📸 PINTAR MEDIA</h1>", unsafe_allow_html=True)
        with st.form("login_form"):
            u_input = st.text_input("Username", value=st.query_params.get("u", ""))
            p_input = st.text_input("Password", type="password")
            if st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True, type="primary"):
                u_clean = u_input.lower().strip()
                if u_clean in USER_PASSWORDS and p_input == USER_PASSWORDS[u_clean]:
                    st.session_state.active_user = u_clean
                    st.session_state.login_time = time.time()
                    st.query_params["u"] = u_clean
                    st.rerun()
                else: st.error("❌ Akses Ditolak")
    st.stop()

# ==============================================================================
# 2. KONFIGURASI AI & DATA DNA (MIGRASI MAPPING)
# ==============================================================================
API_KEY = "AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"

@st.cache_resource
def load_ai_engine():
    try:
        genai.configure(api_key=API_KEY)
        # Deteksi model agar anti-404
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available else 'models/gemini-pro'
        return genai.GenerativeModel(target)
    except: return None

model_ai = load_ai_engine()

# --- MAPPING DATA (DNA RUMAH LAMA) ---
LOKASI_DNA = {
    "jalan kampung": "shabby dirt road in Indonesian village, weathered textures, ultra-detailed gravel.",
    "jalan kota kecil": "rugged asphalt road, weathered 90s shophouses, sharp urban grit.",
    "pasar": "authentic Indonesian wet market, wet muddy floor, vibrant organic produce.",
    "halaman rumah": "old front yard, potted frangipani trees, mossy cement floor.",
    "teras rumah miskin": "humble wooden porch, old grey weathered timber, dusty floor boards.",
    "dalam rumah kayu": "vintage timber interior, hyper-detailed wood grain, ancient furniture.",
    "teras rumah kaya": "modern minimalist mansion terrace, marble floor, manicured garden.",
    "dalam rumah kaya": "high-end luxury living room, polished stone textures, glass walls."
}
options_lokasi = ["--- KETIK MANUAL ---"] + list(LOKASI_DNA.keys())

# ==============================================================================
# 3. CSS CUSTOM (MEWAH V2)
# ==============================================================================
st.markdown("""
    <style>
    header[data-testid="stHeader"] { background-color: #ff4b4b; }
    [data-testid="stSidebar"] { background-color: #1a1c24 !important; }
    .staff-header-premium { background: rgba(29, 151, 108, 0.2); border: 2px solid #1d976c; border-radius: 10px; padding: 15px; margin-bottom: 25px; }
    .stButton>button { border-radius: 10px; font-weight: bold; }
    .small-label { color: #1d976c; font-size: 10px; font-weight: 800; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. FUNGSI DATABASE (GOOGLE SHEETS)
# ==============================================================================
def record_to_sheets(user, data_packet, total_scenes):
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        existing_data = conn.read(worksheet="Sheet1", ttl="1m")
        tz = pytz.timezone('Asia/Jakarta')
        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        new_row = pd.DataFrame([{"Waktu": current_time, "User": user, "Total Adegan": total_scenes, "Visual Utama": data_packet}])
        updated_df = pd.concat([existing_data, new_row], ignore_index=True)
        conn.update(worksheet="Sheet1", data=updated_df.tail(300))
    except Exception as e: st.error(f"GSheets Error: {e}")

# ==============================================================================
# 5. SIDEBAR NAVIGATION
# ==============================================================================
with st.sidebar:
    try: st.image("PINTAR.png", use_container_width=True)
    except: st.title("🎬 PINTAR MEDIA")
    st.write(f"Staf: **{st.session_state.active_user.upper()}** ✅")
    st.divider()
    menu = st.radio("MENU:", ["🏠 DASHBOARD", "🚀 PRODUCTION HUB", "🧠 AI LAB", "📋 TEAM TASK", "🛠️ COMMAND CENTER"])
    if st.button("KELUAR SISTEM ⚡"):
        st.query_params.clear()
        st.session_state.clear()
        st.rerun()

# ==============================================================================
# 6. HALAMAN PRODUCTION HUB (STORYBOARD UI & LOGIC)
# ==============================================================================
if menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    st.markdown(f'<div class="staff-header-premium">👤 <b>Staf Aktif: {st.session_state.active_user.capitalize()}</b> | <i>Konten yang mantap lahir dari detail yang tepat.</i></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📝 AI Scriptwriter", "📋 Storyboard Detail"])
    
    with tab1:
        ide = st.text_area("Ide Konten:", placeholder="Ketik ide di sini...")
        if st.button("GENERATE NASKAH"):
            if model_ai and ide:
                with st.spinner("Menulis..."):
                    res = model_ai.generate_content(f"Buat naskah video pendek viral 6 adegan: {ide}")
                    st.write(res.text)

    with tab2:
        # --- IDENTITAS TOKOH (GRID 2 KOLOM) ---
        st.markdown("### 👥 Identitas Tokoh")
        c_cols = st.columns(2)
        with c_cols[0]:
            n1 = st.text_input("Nama Karakter 1", key="c_name_1_input", value="Sultan")
            d1 = st.text_area("Fisik 1", key="c_desc_1_input", height=100)
        with c_cols[1]:
            n2 = st.text_input("Nama Karakter 2", key="c_name_2_input")
            d2 = st.text_area("Fisik 2", key="c_desc_2_input", height=100)
        
        st.divider()

        # --- GRID ADEGAN (SINKRON RUMAH LAMA) ---
        num_scenes = st.slider("Jumlah Adegan", 1, 12, 6)
        all_chars = [{"name": n1, "desc": d1}, {"name": n2, "desc": d2}]
        
        adegan_list = []
        for i in range(1, num_scenes + 1):
            with st.expander(f"🎬 ADEGAN {i}", expanded=(i==1)):
                col_v, col_c = st.columns([2, 1])
                with col_v:
                    v_in = st.text_area(f"Cerita Visual {i}", key=f"vis_input_{i}", height=220)
                with col_c:
                    st.markdown('<p class="small-label">💡 Suasana</p>', unsafe_allow_html=True)
                    sua = st.selectbox(f"S{i}", ["Siang", "Pagi", "Sore", "Malam"], key=f"light_input_{i}", label_visibility="collapsed")
                    st.markdown('<p class="small-label">📐 Shot</p>', unsafe_allow_html=True)
                    sht = st.selectbox(f"SS{i}", ["Setengah Badan", "Close Up", "Long Shot", "Drone"], key=f"shot_input_{i}", label_visibility="collapsed")
                    st.markdown('<p class="small-label">📍 Lokasi</p>', unsafe_allow_html=True)
                    loc_s = st.selectbox(f"L{i}", options_lokasi, key=f"loc_sel_{i}", label_visibility="collapsed")
                    loc_m = ""
                    if loc_s == "--- KETIK MANUAL ---":
                        loc_m = st.text_input(f"Manual {i}", key=f"loc_custom_{i}", placeholder="Di mana?")
                    
                    loc_final = loc_m if loc_s == "--- KETIK MANUAL ---" else loc_s
                
                # Dialog (MIGRASI FUNGSI DIALOG)
                d_col = st.columns(2)
                d_in1 = d_col[0].text_input(f"Dialog {n1}", key=f"diag_{i}_0")
                d_in2 = d_col[1].text_input(f"Dialog {n2}", key=f"diag_{i}_1")
                
                adegan_list.append({"id": i, "visual": v_in, "suasana": sua, "shot": sht, "lokasi": loc_final, "dialogs": [d_in1, d_in2]})

        # --- TOMBOL SAVE & GENERATE (LOGIKA PROMPT SHARP) ---
        if st.button("🚀 SAVE & GENERATE PROMPTS", type="primary", use_container_width=True):
            if not v_in: st.warning("Isi visual dulu!")
            else:
                with st.spinner("Membangun Prompt Tajam..."):
                    results = []
                    for ad in adegan_list:
                        if ad["visual"]:
                            # Logika Scan Karakter (Regex)
                            mentioned = []
                            for char in all_chars:
                                if char["name"] and re.search(rf'\b{re.escape(char["name"].lower())}\b', ad["visual"].lower()):
                                    mentioned.append(f"CHARACTER_{char['name'].upper()}: {char['desc']}")
                            
                            char_info = " AND ".join(mentioned) if mentioned else f"MAIN_CHARACTER: {d1}"
                            env_dna = LOKASI_DNA.get(ad["lokasi"].lower(), f"{ad['lokasi']}, sharp focus.")
                            
                            # MEGA PROMPT (MIGRASI KUALITAS TAJAM)
                            p_img = (
                                f"STRICT RULE: 8k RAW photo, ultra-sharp edge enhancement, f/11 aperture.\n"
                                f"NO TEXT, NO SPEECH BUBBLES, NO SUBTITLES.\n"
                                f"CHARACTERS: {char_info}\n"
                                f"ACTION: {ad['visual']}\n"
                                f"ENVIRONMENT: {env_dna}, {ad['suasana']} lighting, {ad['shot']} size.\n"
                                f"TECHNICAL: hyper-detailed textures, vivid colors, masterpiece quality."
                            )
                            results.append({"id": ad["id"], "prompt": p_img})
                    
                    st.session_state.final_results = results
                    # Save ke Sheets (MIGRASI KOPER DATA)
                    record_to_sheets(st.session_state.active_user, f"Draft: {adegan_list[0]['visual'][:50]}", len(results))
                    st.balloons()

        # DISPLAY PROMPT
        if "final_results" in st.session_state:
            for r in st.session_state.final_results:
                with st.container():
                    st.write(f"**Prompt Adegan {r['id']}**")
                    st.code(r["prompt"], language="text")

# --- MENU: DASHBOARD (MIGRASI LOG) ---
elif menu == "🏠 DASHBOARD":
    st.header("🏠 Dashboard Utama")
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        df_log = conn.read(worksheet="Sheet1", ttl="1m")
        st.markdown("#### 📅 Log Aktivitas Tim")
        st.dataframe(df_log.tail(10), use_container_width=True, hide_index=True)
    except: st.info("Database Cloud sedang sinkronisasi...")

else:
    st.header(menu)
    st.info("Fitur sedang dimigrasi.")
