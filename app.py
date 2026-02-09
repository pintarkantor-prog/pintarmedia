import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
import pytz
import time
import google.generativeai as genai

# ==============================================================================
# KONFIGURASI OTAK AI (VERSI GACOR & ANTI-LIMIT)
# ==============================================================================
genai.configure(api_key="AIzaSyADIKUFF4Sr_uXHleJa7qFr7SNGXmJ1lQM")

# 1. Cari model yang tersedia secara otomatis
available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]

# 2. Pilih model (Utamakan gemini-1.5-flash karena kuota lebih banyak & stabil)
selected_model_name = 'models/gemini-1.5-flash'
if available_models:
    flash_models = [m for m in available_models if '1.5-flash' in m.lower()]
    selected_model_name = flash_models[0] if flash_models else available_models[0]

# 3. SOP PINTAR MEDIA (INSTRUKSI WAJIB SKAKMAT)
SOP_PINTAR_MEDIA = """
Kamu adalah Scriptwriter Senior PINTAR MEDIA, spesialis video Shorts 'Karma Visual'.
GAYA BAHASA: 
- Sangat lokal, bahasa tongkrongan, ceplas-ceplos, dan nyelekit.
- Karakter Antagonis (TUNG) harus sangat menyebalkan dan merendahkan di awal.
- Karakter Protagonis (UDIN) harus memberikan balasan 'SKAKMAT' yang memuaskan penonton.
- Gunakan instruksi [ACTION] untuk gerakan visual (seperti: lempar uang, kaget melongo, ludah, atau pamer kacamata).
- JANGAN SOPAN. Fokus pada konflik sosial (Hutang, Sombong, Meremehkan).
"""

# 4. Inisialisasi Model
model = genai.GenerativeModel(
    model_name=selected_model_name,
    system_instruction=SOP_PINTAR_MEDIA
)

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
# Kita pastikan nilai default-nya ada di dalam pilihan menu kamu
for i in range(1, 51):
    for key, default in [
        (f"vis_input_{i}", ""),
        (f"light_input_{i}", "Siang"),       # Sesuai options_lighting
        (f"camera_input_{i}", "Diam (Tanpa Gerak)"), # Sesuai indonesia_camera
        (f"shot_input_{i}", "Setengah Badan"),       # Sesuai indonesia_shot
        (f"angle_input_{i}", "Normal"),      # Sesuai indonesia_angle
        (f"loc_sel_{i}", "--- KETIK MANUAL ---"),  # Sesuai options_lokasi
        (f"loc_custom_{i}", "")  # <--- WAJIB TAMBAH INI! Agar input manual punya wadah
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
            "Visual Utama": data_packet # <--- Di sini data koper disimpan utuh
        }])
        
        # 5. Gabungkan data lama dan baru
        updated_df = pd.concat([existing_data, new_row], ignore_index=True)
        
        # 6. Batasi history maksimal 300 baris agar tidak berat
        if len(updated_df) > 300:
            updated_df = updated_df.tail(300)
        
        # 7. Update kembali ke Google Sheets
        conn.update(worksheet="Sheet1", data=updated_df)
        
    except Exception as e:
        # Menampilkan error agar kamu tahu kalau koneksinya bermasalah
        st.error(f"Gagal mencatat ke Cloud: {e}")
        
# ==============================================================================
# 4. CUSTOM CSS (VERSION: CLEAN OBSIDIAN - NO GREEN BORDER)
# ==============================================================================
st.markdown("""
    <style>
    /* A. CUSTOM SCROLLBAR */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #0e1117; }
    ::-webkit-scrollbar-thumb { background: #31333f; border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: #31333f; }

    /* 1. RESPONSIVE HEADER (UNLOCKED & SCROLLABLE) */
    [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) {
        position: relative;
        top: 0; left: 0; right: 0;
        z-index: 99;
        background-color: transparent;
        padding: 10px 0px;
        border-bottom: 2px solid #31333f;
        margin-bottom: 20px;
        width: 100%;
    }

    /* 2. STYLE SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #1a1c24 !important;
        border-right: 1px solid rgba(29, 151, 108, 0.1) !important;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
        color: #ffffff !important;
    }

    /* 3. TOMBOL GENERATE (KEMBALI KE RESPONS INSTAN - TANPA TRANSISI) */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(to right, #1d976c, #11998e) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: bold !important;
        font-size: 16px !important;
        width: 100%;
        box-shadow: 0 4px 12px rgba(29, 151, 108, 0.2) !important;
        /* Transition dihapus agar kembali instan */
    }

    div.stButton > button[kind="primary"]:hover {
        background: #11998e !important;
        box-shadow: 0 6px 15px rgba(29, 151, 108, 0.3) !important;
    }

    /* 4. MODIFIKASI BOX STAF AKTIF */
    .staff-header-premium {
        background: rgba(29, 151, 108, 0.1) !important;
        border: 1px solid #1d976c !important;
        border-radius: 12px !important;
        padding: 12px 20px !important;
        display: flex !important;
        align-items: center !important;
        gap: 15px !important;
    }
    .staff-header-premium b { color: #1d976c !important; }
    .staff-header-premium i { color: #a1a1a1 !important; font-style: normal !important; }

    /* 5. EFEK FOKUS (KEMBALI KE DEFAULT) */
    /* Menghapus semua border-color hijau agar kembali ke default sistem */
    .stTextArea textarea:focus, .stTextInput input:focus {
        box-shadow: none !important;
        outline: none !important;
    }

    /* 6. STYLE LAINNYA (CLEAN & NO OVERLAP) */
    h1, h2, h3 { color: #ffffff !important; }

    button[title="Copy to clipboard"] {
        background-color: #262730 !important;
        color: white !important;
    }
    .small-label {
        font-size: 12px; font-weight: bold; color: #a1a1a1; margin-bottom: 2px;
    }
    
    .stTextArea textarea, .stTextInput input {
        font-size: 16px !important;
        border-radius: 8px !important; 
        background-color: #0e1117 !important; 
        color: #ffffff !important;
        border: 1px solid #31333f !important; 
    }

    .small-label {
        color: #1d976c !important; /* <--- GANTI WARNA DI SINI */
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 10px !important;
        font-weight: 800 !important;
    }

    /* 7. OPTIMASI KOTAK ADEGAN */
    .stExpander {
        border: 1px solid #31333f !important;
        border-radius: 8px !important;
        background-color: #11151c !important;
        margin-bottom: 10px !important;
    }

    hr {
        margin: 1.5em 0 !important;
        border: 0;
        border-top: 1px solid rgba(255,255,255,0.05) !important;
    }

    /* MENGHAPUS SEMUA PERINTAH DUPLIKAT DI BAWAH */
    div[data-baseweb="input"], div[data-baseweb="textarea"] { border: none !important; }
    @media (max-width: 1024px) {
        /* Sembunyikan semua konten utama */
        [data-testid="stAppViewContainer"], 
        [data-testid="stSidebar"], 
        .main {
            display: none !important;
        }

        /* Tampilkan pesan peringatan di layar HP/Tab */
        body::before {
            content: "⚠️ AKSES DITOLAK \A Gunakan PC / Laptop!";
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            width: 100vw;
            background-color: #0e1117;
            color: #ffffff;
            font-family: 'Segoe UI', Roboto, sans-serif;
            font-weight: bold;
            text-align: center;
            padding: 40px;
            font-size: 20px;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 9999;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 5. GLOBAL HEADER (Muncul di semua halaman)
# ==============================================================================
if 'active_user' in st.session_state:
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
# 6. MAPPING TRANSLATION (REVISED & SYNCHRONIZED)
# ==============================================================================

# --- DAFTAR PILIHAN (Apa yang muncul di tombol) ---
indonesia_camera = ["Diam (Tanpa Gerak)", "Ikuti Karakter", "Zoom Masuk", "Zoom Keluar", "Memutar (Orbit)"]
indonesia_shot = ["Sangat Dekat", "Dekat Wajah", "Setengah Badan", "Seluruh Badan", "Pemandangan Luas", "Drone Shot"]
indonesia_angle = ["Normal", "Sudut Rendah", "Sudut Tinggi", "Samping", "Berhadapan", "Intip Bahu", "Belakang"]
options_lighting = ["Pagi", "Siang", "Sore", "Malam"]

# --- DNA LOKASI (Gudang Data Lokasi - ULTIMATE TEXTURE & NEUTRAL LIGHT) ---
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

# --- KAMUS TERJEMAHAN UNTUK AI ---
camera_map = {
    "Diam (Tanpa Gerak)": "Static camera, no movement, stable shot",
    "Ikuti Karakter": "Dynamic tracking shot following the subject's movement",
    "Zoom Masuk": "Slow cinematic zoom-in, intensifying focus",
    "Zoom Keluar": "Slow cinematic zoom-out, revealing environment",
    "Memutar (Orbit)": "360-degree orbital circular camera rotation"
}

shot_map = {
    "Sangat Dekat": "Extreme Close-Up shot, macro photography, hyper-detailed micro textures",
    "Dekat Wajah": "Close-Up shot, focus on facial expressions and skin details",
    "Setengah Badan": "Medium Shot, waist-up framing, cinematic depth",
    "Seluruh Badan": "Full body shot, head-to-toe framing, environment visible",
    "Pemandangan Luas": "Wide landscape shot, expansive scenery, subject is small in frame",
    "Drone Shot": "Cinematic Aerial Drone shot, high altitude, bird's-eye view from above"
}

angle_map = {
    "Normal": "eye-level shot, straight on perspective, natural head-on view",
    "Sudut Rendah": "heroic low angle shot, looking up from below, monumental framing",
    "Sudut Tinggi": "high angle shot, looking down at the subject, making it look smaller",
    "Samping": "side profile view, 90-degree side angle, parallel to camera, full profile perspective",
    "Berhadapan": "dual profile view, two subjects facing each other, face-to-face, symmetrical",
    "Intip Bahu": "over-the-shoulder shot, foreground shoulder blur, cinematic dialogue depth",
    "Belakang": "shot from behind, back view, following the subject, looking away from camera"
}

# --- INISIALISASI SESSION STATE AWAL ---
if 'm_light' not in st.session_state: st.session_state.m_light = "Siang"
if 'm_cam' not in st.session_state: st.session_state.m_cam = "Diam (Tanpa Gerak)"
if 'm_shot' not in st.session_state: st.session_state.m_shot = "Setengah Badan"
if 'm_angle' not in st.session_state: st.session_state.m_angle = "Normal"

def global_sync_v920():
    if "light_input_1" in st.session_state:
        lt1 = st.session_state.light_input_1
        cm1 = st.session_state.camera_input_1
        st1 = st.session_state.shot_input_1
        ag1 = st.session_state.angle_input_1
        
        st.session_state.m_light = lt1
        st.session_state.m_cam = cm1
        st.session_state.m_shot = st1
        st.session_state.m_angle = ag1
        
        for key in st.session_state.keys():
            if key.startswith("light_input_"): st.session_state[key] = lt1
            if key.startswith("camera_input_"): st.session_state[key] = cm1
            if key.startswith("shot_input_"): st.session_state[key] = st1
            if key.startswith("angle_input_"): st.session_state[key] = ag1
# ==============================================================================
# 7. SIDEBAR: NAVIGATION & CONFIGURATION
# ==============================================================================
with st.sidebar:
    # --- 1. LOGO SIDEBAR ---
    try:
        st.image("PINTAR.png", use_container_width=True)
    except:
        st.title("📸 PINTAR MEDIA")

    st.write("") 

    # --- 2. MENU NAVIGASI UTAMA ---
    st.markdown("#### 🖥️ MAIN COMMAND")
    menu_select = st.radio(
        "Pilih Ruangan:",
        ["🚀 PRODUCTION HUB", "🧠 AI LAB", "🎞️ SCHEDULE", "📋 TEAM TASK", 
         "📈 TREND ANALYZER", "💡 IDEAS BANK", "👥 DATABASE LOCKER", 
         "📊 MONITORING", "🛠️ COMMAND CENTER"],
        label_visibility="collapsed"
    )
    
    st.divider()

    # --- 3. LOGIKA KONTROL (KHUSUS PRODUCTION HUB) ---
    if menu_select == "🚀 PRODUCTION HUB":
        # SEMUA DI BAWAH INI SEKARANG MASUK KE DALAM IF (MENJOROK KE KANAN)

        # --- LOGIKA ADMIN ---
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
                    else:
                        st.warning("Belum ada data aktivitas tercatat.")
                except Exception as e:
                    st.error(f"Gagal memuat data Cloud: {e}")
            st.divider()

        # --- KONFIGURASI UMUM ---
        num_scenes = st.number_input("Tambah Jumlah Adegan", min_value=1, max_value=50, value=6)
        
        st.write("") 
        st.markdown("#### 🎨 GENRE VISUAL")
        list_genre = [
            "Realistik (Nyata)", "Pixar 3D", "Marvel Superhero", "Transformers (Mecha)",
            "KingKong (VFX Monster)", "Asphalt (Balap/Glossy)", "Ghibli (Estetik/Indah)",
            "Dragon Ball", "Doraemon 3D", "Naruto (Ninja)", "Tayo (Anak-anak)", "Sakura School (Anime)"
        ]
        
        genre_saved = st.session_state.get("genre_pilihan_saved", "Realistik (Nyata)")
        try: 
            idx_default = list_genre.index(genre_saved)
        except: 
            idx_default = 0

        genre_pilihan = st.selectbox("Pilih Gaya Film:", options=list_genre, index=idx_default)
        st.write("")
        
        # --- STATUS PRODUKSI ---
        if st.session_state.last_generated_results:
            st.markdown("### 🗺️ STATUS PRODUKSI")
            total_p = len(st.session_state.last_generated_results)
            done_p = sum(1 for res in st.session_state.last_generated_results if st.session_state.get(f"mark_done_{res['id']}", False))
            st.progress(done_p / total_p)
            if done_p == total_p and total_p > 0:
                st.balloons()
                st.success("🎉 Semua Adegan Selesai!")
        
        st.divider()

        # --- TOMBOL SAVE & LOAD ---
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("💾 SAVE", use_container_width=True):
                import json
                try:
                    char_data = {str(idx): {"name": st.session_state.get(f"c_name_{idx}_input", ""), "desc": st.session_state.get(f"c_desc_{idx}_input", "")} for idx in range(1, 11)}
                    scene_data = {str(i): {"vis": st.session_state.get(f"vis_input_{i}", ""), "light": st.session_state.get(f"light_input_{i}", "Siang"), "shot": st.session_state.get(f"shot_input_{i}", "Setengah Badan"), "angle": st.session_state.get(f"angle_input_{i}", "Normal"), "loc": st.session_state.get(f"loc_sel_{i}", "jalan kampung")} for i in range(1, 51)}
                    dialog_data = {k: v for k, v in st.session_state.items() if k.startswith("diag_") and v}
                    master_packet = {"num_char": st.session_state.get("num_total_char", 2), "genre": genre_pilihan, "chars": char_data, "scenes": scene_data, "dialogs": dialog_data}
                    record_to_sheets(f"DRAFT_{st.session_state.active_user}", json.dumps(master_packet), len([s for s in scene_data.values() if s['vis']]))
                    st.toast("Project Tersimpan! ✅")
                except Exception as e:
                    st.error(f"Gagal simpan: {e}")

        with btn_col2:
            if st.button("🔄 LOAD", use_container_width=True):
                import json
                try:
                    conn = st.connection("gsheets", type=GSheetsConnection)
                    df_log = conn.read(worksheet="Sheet1", ttl="1s")
                    my_data = df_log[df_log['User'] == f"DRAFT_{st.session_state.active_user}"]
                    if not my_data.empty:
                        data = json.loads(str(my_data.iloc[-1]['Visual Utama']))
                        st.session_state["num_total_char"] = data.get("num_char", 2)
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
                        for k, v in data.get("dialogs", {}).items(): 
                            st.session_state[k] = v
                        st.toast("Data Dipulihkan! 🔄")
                        st.rerun()
                    else:
                        st.error("Draft kosong.")
                except Exception as e:
                    st.error(f"Gagal: {e}")

    # --- 4. TOMBOL LOGOUT (Selalu muncul di semua menu) ---
    st.divider()
    if st.button("KELUAR SISTEM ⚡", use_container_width=True):
        st.query_params.clear() 
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
# ==============================================================================
# 8. PARAMETER KUALITAS (VERSION: APEX SHARPNESS & VIVID)
# ==============================================================================
# --- STACK UNTUK FOTO (Tajam, Statis, Tekstur Pori-pori) ---
img_quality_stack = (
    "hyper-realistic 8k RAW photo, infinite depth of field, f/11 aperture, "
    "zero bokeh, zero background blur, sharp edge-enhancement, non-filtered, "
    "ultra-clear optical clarity, tactile textures on sand, gravel, and wood, "
    "CPL filter, deep blue sky, polarized colors, high local contrast, "
    "vivid naturalism, realistic shadow recovery, masterpiece quality."
)

# --- STACK UNTUK VIDEO (Motion Blur Natural, Cinematic, Smooth) ---
vid_quality_stack = (
    "ultra-high definition cinematic video, 8k UHD, high dynamic range, "
    "professional color grading, vibrant organic colors, ray-traced reflections, "
    "hyper-detailed textures, zero digital noise, clean pixels, "
    "smooth motion, professional cinematography, masterpiece quality."
)

# --- PENGUAT NEGATIF (Mencegah Glitch & Teks) ---
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

# --- HASIL AKHIR (SANGAT BERBEDA ANTARA GAMBAR & VIDEO) ---
img_quality_base = f"{img_quality_stack} {no_text_strict}"
vid_quality_base = f"60fps, ultra-clear motion, {vid_quality_stack} {no_text_strict} {negative_motion_strict}"

# ==============================================================================
# 9. PINTU MENU UTAMA (LOGIKA NAVIGASI HALAMAN)
# ==============================================================================

if menu_select == "🚀 PRODUCTION HUB":
    
    if "restore_counter" not in st.session_state:
        st.session_state.restore_counter = 0

    st.subheader("📝 Detail Storyboard")

    # --- IDENTITAS TOKOH (VERSI ELEGANT GRID) ---
    with st.expander("👥 Nama Karakter Utama & Penampilan Fisik! (WAJIB ISI)", expanded=True):
        num_total_char = st.number_input("Total Karakter Utama dalam Project", min_value=1, max_value=10, value=2)
        st.write("") 

        all_chars_list = []
        for i in range(1, num_total_char + 1, 2):
            cols = st.columns(2)
            for idx_offset in range(2):
                idx = i + idx_offset
                if idx <= num_total_char:
                    with cols[idx_offset]:
                        st.markdown(f"##### 👤 Karakter Utama {idx}")
                        name = st.text_input("Nama", key=f"c_name_{idx}_input", placeholder=f"Nama Karakter Utama {idx}", label_visibility="collapsed")
                        desc = st.text_area("Penampilan Fisik", key=f"c_desc_{idx}_input", height=120, placeholder=f"Ciri fisik Karakter Utama {idx}...", label_visibility="collapsed")
                        all_chars_list.append({"name": name, "desc": desc})
            st.write("") 

    # --- LIST ADEGAN ---
    adegan_storage = []
    for i_s in range(1, int(num_scenes) + 1):
        l_box_title = f"🟢 ADEGAN {i_s}" if i_s == 1 else f"🎬 ADEGAN {i_s}"
        with st.expander(l_box_title, expanded=(i_s == 1)):
            col_v, col_ctrl = st.columns([6, 4])
            
            with col_v:
                visual_input = st.text_area(
                    f"Cerita Visual {i_s}", 
                    key=f"vis_input_{i_s}", 
                    height=265, 
                    placeholder="Ceritakan detail adegannya di sini..."
                )
            
            with col_ctrl:
                r1 = st.columns(2)
                with r1[0]:
                    st.markdown('<p class="small-label">💡 Suasana</p>', unsafe_allow_html=True)
                    light_val = st.selectbox(f"L{i_s}", options_lighting, key=f"light_input_{i_s}", label_visibility="collapsed")
                with r1[1]:
                    st.markdown('<p class="small-label">📐 Ukuran Gambar</p>', unsafe_allow_html=True)
                    shot_val = st.selectbox(f"S{i_s}", indonesia_shot, key=f"shot_input_{i_s}", label_visibility="collapsed")
                
                r2 = st.columns(2)
                with r2[0]:
                    st.markdown('<p class="small-label">✨ Arah Kamera</p>', unsafe_allow_html=True)
                    angle_val = st.selectbox(f"A{i_s}", indonesia_angle, key=f"angle_input_{i_s}", label_visibility="collapsed")
                with r2[1]:
                    st.markdown('<p class="small-label">🎬 Gerakan Kamera (khusus video)</p>', unsafe_allow_html=True)
                    cam_val = st.selectbox(f"C{i_s}", indonesia_camera, index=0, key=f"camera_input_{i_s}", label_visibility="collapsed")
                
                r3 = st.columns(1)
                with r3[0]:
                    st.markdown('<p class="small-label">📍 Lokasi</p>', unsafe_allow_html=True)
                    loc_choice = st.selectbox(f"LocSelect{i_s}", options=options_lokasi, key=f"loc_sel_{i_s}", label_visibility="collapsed")
                    
                    if loc_choice == "--- KETIK MANUAL ---":
                        location_val = st.text_input(
                            "Tulis lokasi spesifik latar cerita di sini:", 
                            key=f"loc_custom_{i_s}", 
                            placeholder="Contoh: di dalam gerbong kereta api tua..."
                        )
                    else:
                        location_val = loc_choice

            diag_cols = st.columns(len(all_chars_list))
            scene_dialogs_list = []
            for i_char, char_data in enumerate(all_chars_list):
                with diag_cols[i_char]:
                    char_label = char_data['name'] if char_data['name'] else f"Karakter {i_char+1}"
                    d_in = st.text_input(f"Dialog {char_label}", key=f"diag_{i_s}_{i_char}")
                    scene_dialogs_list.append({"name": char_label, "text": d_in})
            
            adegan_storage.append({
                "num": i_s, 
                "visual": visual_input, 
                "light": light_val,
                "location": location_val,
                "cam": cam_val, 
                "shot": shot_val,
                "angle": angle_val, 
                "dialogs": scene_dialogs_list
            })

    # ==============================================================================
    # 10. GENERATOR PROMPT & MEGA-DRAFT
    # ==============================================================================
    import json

    if 'last_generated_results' not in st.session_state:
        st.session_state.last_generated_results = []

    st.write("")

    if st.button("🚀 GENERATE ALL PROMPTS", type="primary", use_container_width=True):
        nama_tokoh_utama = st.session_state.get("c_name_1_input", "").strip()
        active_scenes = [a for a in adegan_storage if a["visual"].strip() != ""]
        
        if not nama_tokoh_utama:
            st.warning("⚠️ **Nama Karakter 1 belum diisi!**")
        elif not active_scenes:
            st.warning("⚠️ **Mohon isi deskripsi cerita visual!**")
        else:
            with st.spinner(f"⏳ Sedang meracik prompt tajam..."):
                st.session_state.last_generated_results = []
                try:
                    captured_scenes_auto = {f"v{i}": st.session_state.get(f"vis_input_{i}") for i in range(1, int(num_scenes) + 1) if st.session_state.get(f"vis_input_{i}")}
                    auto_packet = {
                        "n1": st.session_state.get("c_name_1_input", ""), "p1": st.session_state.get("c_desc_1_input", ""),
                        "n2": st.session_state.get("c_name_2_input", ""), "p2": st.session_state.get("c_desc_2_input", ""),
                        "scenes": captured_scenes_auto
                    }
                    record_to_sheets(f"AUTO_{st.session_state.active_user}", json.dumps(auto_packet), len(captured_scenes_auto))
                except: pass
            
                record_to_sheets(st.session_state.active_user, active_scenes[0]["visual"], len(active_scenes))
                
                for item in active_scenes:
                    import re
                    mentioned_chars_list = []
                    v_text_low = str(item.get('visual', "")).lower().strip()
                    for c in all_chars_list:
                        c_name_raw = str(c.get('name', "")).strip()
                        if c_name_raw:
                            if re.search(rf'\b{re.escape(c_name_raw.lower())}\b', v_text_low):
                                mentioned_chars_list.append({"name": c_name_raw.upper(), "desc": c.get('desc', '')})
                    
                    if len(mentioned_chars_list) == 1:
                        target_name = mentioned_chars_list[0]['name']
                        char_info = f"[[ CHARACTER_{target_name}: {mentioned_chars_list[0]['desc']} ]]"
                        instruction_header = f"IMAGE REFERENCE RULE: Use the uploaded photo for {target_name}'s face and body.\nSTRICT LIMIT: This scene MUST ONLY feature {target_name}."
                    elif len(mentioned_chars_list) > 1:
                        char_info = " AND ".join([f"[[ CHARACTER_{m['name']}: {m['desc']} ]]" for m in mentioned_chars_list])
                        instruction_header = "IMAGE REFERENCE RULE: Use uploaded photos for each character."
                    else:
                        char_info = f"[[ CHARACTER_MAIN: {all_chars_list[0]['desc']} ]]"
                        instruction_header = "IMAGE REFERENCE RULE: Use the main character reference."

                    if genre_pilihan == "Pixar 3D": bumbu_gaya = "Disney Pixar style 3D animation, Octane render"
                    elif genre_pilihan == "Marvel Superhero": bumbu_gaya = "Marvel Cinematic Universe aesthetic"
                    else: bumbu_gaya = img_quality_stack

                    pilihan_dropdown = st.session_state.get(f"loc_sel_{item['num']}", "")
                    if pilihan_dropdown == "--- KETIK MANUAL ---":
                        manual_text = st.session_state.get(f"loc_custom_{item['num']}", "").strip()
                        dna_env = f"{manual_text}, highly detailed textures" if manual_text else "cinematic environment"
                    else:
                        dna_env = LOKASI_DNA.get(pilihan_dropdown.lower(), f"{pilihan_dropdown}, sharp focus.")

                    e_shot = shot_map.get(item["shot"], "Medium Shot")
                    e_angle = angle_map.get(item["angle"], "")
                    camera_final = f"{e_shot}, {e_angle}, infinite depth of field"

                    if "Pagi" in item["light"]: l_cmd = "6 AM early morning sunlight"
                    elif "Siang" in item["light"]: l_cmd = "Direct harsh midday sunlight"
                    elif "Sore" in item["light"]: l_cmd = "4 PM golden hour"
                    elif "Malam" in item["light"]: l_cmd = "Cinematic night photography"
                    else: l_cmd = "Natural lighting"

                    try: d_text_full = " ".join([f"{d['name']}: {d['text']}" for d in item.get('dialogs', []) if d.get('text')])
                    except: d_text_full = ""
                    image_emo = f"Expressions mood: '{d_text_full}'" if d_text_full else "Natural expression"

                    img_final = f"{instruction_header}\n\nCHARACTER: {char_info}\nACTION: {item['visual']}. {image_emo}\nENVIRONMENT: {dna_env}\nCAMERA: {camera_final}\nTECHNICAL: {bumbu_gaya}, {l_cmd}"
                    vid_final = f"{instruction_header}\nACTION: {item['visual']}\nCHARACTER: {char_info}\nENVIRONMENT: {dna_env}\nLIGHTING: {l_cmd}\nTECHNICAL: {vid_quality_base}"

                    st.session_state.last_generated_results.append({"id": item["num"], "img": img_final, "vid": vid_final})
            st.toast("Prompt Berhasil Diracik! 🚀")
            st.rerun()

    # --- AREA TAMPILAN HASIL ---
    if st.session_state.last_generated_results:
        st.markdown(f"### 🎬 Hasil Prompt: {st.session_state.active_user.capitalize()}❤️")
        for res in st.session_state.last_generated_results:
            done_key = f"mark_done_{res['id']}"
            is_done = st.session_state.get(done_key, False)
            status_tag = "✅ SELESAI" if is_done else "⏳ PROSES"
            with st.expander(f"{status_tag} | ADEGAN {res['id']}", expanded=not is_done):
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("**📸 PROMPT GAMBAR**")
                    st.code(res['img'], language="text")
                with c2:
                    st.markdown("**🎥 PROMPT VIDEO**")
                    st.code(res['vid'], language="text")

# ==============================================================================
# 11. HALAMAN AI LAB (RUANGAN IDE GOKIL - VERSI SKAKMAT)
# ==============================================================================
elif menu_select == "🧠 AI LAB":
    nama_display = st.session_state.active_user.capitalize() 
    
    st.title("🧠 AI LAB: GUDANG IDE GACOR")
    st.markdown("---")
    st.write(f"Halo **{nama_display}**! Pilih ide maut di bawah atau buat baru, lalu eksekusi jadi naskah skakmat!")

    # --- TABS ---
    tab_spy, tab_cloner, tab_storyboard = st.tabs([
        "📦 1. GUDANG IDE (STOK GACOR)", 
        "🔄 2. SUNTIK NASKAH DIALOG", 
        "📝 3. STORYBOARD VISUAL"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: GUDANG IDE (ANTI-LIMIT / ANTI-PUSING)
    # --------------------------------------------------------------------------
    with tab_spy:
        mode_ide = st.radio("Metode Cari Ide:", ["📦 Pakai Ide Stok (Hemat Kuota)", "💡 Buat Ide Baru (AI Generator)"], horizontal=True)
        st.markdown("---")

        if mode_ide == "📦 Pakai Ide Stok (Hemat Kuota)":
            gudang_ide = {
                "--- Pilih Menu Ide ---": "",
                "Karma Konten Palsu (Uang Ditarik)": "Tung kasih sejuta ke pengemis (Udin) demi konten, abis kamera mati ditarik lagi. Udin ternyata pake kacamata kamera tersembunyi & lagi live bongkar konten palsu.",
                "Antri Bansos Pake Mobil": "Tung pake mobil mewah antre bansos & maki-maki petugas (Udin). Udin cek data: Tung palsuin data kemiskinan. Polisi dateng, mobil disita di tempat.",
                "Bos Nyamar jadi OB Kantor": "Tung karyawan baru sombong bentak Udin yang lagi ngepel gara-gara bajunya kesenggol. Pas jam meeting, Udin duduk di kursi CEO. Tung langsung kicep.",
                "Hutang Gaya Elit (Pamer HP)": "Tung pamer HP lipat baru di tongkrongan sambil ngatain Udin miskin. Udin telpon leasing depan umum: Ternyata HP Tung barang tarikan yang nunggak 5 bulan.",
                "Sombong di Showroom Mobil": "Tung pamer di showroom, ngeremehin sales (Udin) yang penampilannya biasa. Ternyata Udin itu pemilik showroom yang lagi cek stok. Tung diusir gak boleh beli."
            }
            pilihan = st.selectbox("Daftar Premis Gacor:", list(gudang_ide.keys()))
            if pilihan != "--- Pilih Menu Ide ---":
                st.info(f"**Alur:** {gudang_ide[pilihan]}")
                if st.button("KUNCI IDE INI ⚡", use_container_width=True):
                    st.session_state['temp_script_spy'] = gudang_ide[pilihan]
                    st.balloons()
                    st.success("Ide Berhasil Dikunci! Sekarang lanjut ke Tab 2.")

        else: # AUTO GENERATOR (ALUR DIKUNCI SKAKMAT)
            col1, col2 = st.columns(2)
            with col1:
                vibe = st.selectbox("Vibe Cerita:", ["Sombong Kena Karma", "Pamer Harta Palsu", "Meremehkan Orang Sakti"])
                lokasi = st.selectbox("Setting Tempat:", ["Parkiran", "Restoran Mewah", "Pasar", "Kantor", "Sekolah"])
            with col2:
                nyelekit = st.select_slider("Level Pedas:", options=["Sinis", "Pedas", "Bikin Darah Tinggi"])
            
            if st.button("RAKIT IDE SKAKMAT 🚀", use_container_width=True):
                with st.spinner("Merancang plot..."):
                    try:
                        prompt_auto = f"Buat 1 premis cerita Shorts Gacor. Vibe: {vibe}, Lokasi: {lokasi}, Level: {nyelekit}. ALUR WAJIB: Karakter A (Jahat) menghina Karakter B (Sabar), lalu Karakter B membalas dengan SKAKMAT yang memalukan di depan umum."
                        response = model.generate_content(prompt_auto)
                        st.session_state['temp_script_spy'] = response.text
                        st.markdown(response.text)
                    except Exception as e:
                        st.error("Waduh, AI lagi capek (Limit). Coba lagi 30 detik ya!")

    # --------------------------------------------------------------------------
    # TAB 2: SUNTIK NASKAH DIALOG (HASIL SEPERTI CONTOH USER)
    # --------------------------------------------------------------------------
    with tab_cloner:
        st.subheader("🔄 Langkah 2: Suntik Dialog Nyelekit")
        if 'temp_script_spy' in st.session_state:
            nama_tokoh = st.text_input("Tulis Nama Tokoh:", value="UDIN, TUNG")
            
            if st.button("GENERATE NASKAH SKAKMAT 🧪", use_container_width=True):
                with st.spinner("Menyusun dialog & aksi visual..."):
                    try:
                        prompt_dialog = f"""
                        Jadikan ide ini naskah dialog Shorts: {st.session_state['temp_script_spy']}
                        
                        WAJIB IKUTI FORMAT INI:
                        1. Gunakan [ACTION] untuk instruksi visual (contoh: [Tung lempar receh ke muka Udin]).
                        2. Dialog TUNG: Harus sangat sombong dan jahat di awal.
                        3. Dialog UDIN: Harus memberikan kalimat SKAKMAT di akhir.
                        4. Karakter: {nama_tokoh}.
                        5. Gaya bahasa: Indonesia tongkrongan yang natural dan pedas.
                        """
                        response = model.generate_content(prompt_dialog)
                        st.session_state['ready_script'] = response.text
                        st.markdown("---")
                        st.markdown(response.text)
                    except Exception as e:
                        st.error("Limit tercapai! Tunggu 1 menit ya.")
        else:
            st.warning("Pilih ide dulu di Tab 1!")

    # --------------------------------------------------------------------------
    # TAB 3: STORYBOARD
    # --------------------------------------------------------------------------
    with tab_storyboard:
        st.subheader("📝 Langkah 3: Storyboard Produksi")
        if 'ready_script' in st.session_state:
            if st.button("PECAH ADEGAN VISUAL 🎬", use_container_width=True):
                with st.spinner("Merancang visual per adegan..."):
                    try:
                        prompt_st = f"Buat tabel storyboard 8 adegan visual dari naskah ini: {st.session_state['ready_script']}"
                        response = model.generate_content(prompt_st)
                        st.markdown(response.text)
                    except Exception as e:
                        st.error("Gagal buat storyboard. Coba klik lagi.")
        else:
            st.error("Bikin naskahnya dulu di Tab 2!")

