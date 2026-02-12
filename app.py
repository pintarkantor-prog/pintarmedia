import streamlit as st
import json
import time
from datetime import datetime
import pytz

# ────────────────────────────────────────────────
# INISIALISASI SESSION STATE SECARA AMAN (WAJIB DI ATAS)
# ────────────────────────────────────────────────
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.login_time = None

# Auto logout setelah 10 jam
if st.session_state.get('logged_in', False) and st.session_state.get('login_time'):
    if time.time() - st.session_state.login_time > 36000:
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ────────────────────────────────────────────────
# KONFIGURASI HALAMAN & CSS
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="PINTAR MEDIA Generator",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Force dark background full app */
    .stApp, [data-testid="stAppViewContainer"], section.main {
        background-color: #0e1117 !important;
        color: #e0e0e0 !important;
    }

    /* Blokir HP */
    @media (max-width: 1024px) {
        .stApp { display: none !important; }
        body::before {
            content: "⚠️ Gunakan komputer / layar lebar!";
            display: flex !important;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: #0e1117;
            color: white;
            font-size: 1.5rem;
            font-weight: bold;
            text-align: center;
            position: fixed;
            inset: 0;
            z-index: 999999 !important;
        }
    }

    /* Login page styling */
    .login-wrapper {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
        background: #0e1117;
    }
    .login-box {
        width: 100%;
        max-width: 380px;
        background: #1a1c24 !important;
        border-radius: 12px;
        padding: 32px 24px;
        border: 1px solid #2d3748;
        box-shadow: 0 8px 32px rgba(0,0,0,0.5);
        text-align: center;
    }
    .logo-container {
        margin-bottom: 24px;
    }
    .welcome-msg {
        text-align: center;
        color: #28a745;
        font-size: 1.6rem;
        font-weight: bold;
        margin: 20px 0;
    }
    .footer {
        margin-top: 40px;
        color: #666;
        font-size: 0.85rem;
        text-align: center;
    }

    /* Input lebih kompak */
    div[data-testid="stTextInput"] {
        margin-bottom: 12px !important;
    }
    .stTextInput > div > div > input {
        background: #0e1117 !important;
        border: 1px solid #3a3f4a !important;
        border-radius: 6px;
        padding: 10px 12px !important;
        color: white !important;
    }
    .stTextInput label {
        color: #a0a0a0 !important;
        margin-bottom: 4px !important;
        font-size: 0.9rem !important;
    }

    /* Tombol lebih rapi */
    button[kind="primary"] {
        width: 100% !important;
        padding: 10px !important;
        font-size: 1rem !important;
        background: linear-gradient(90deg, #1d976c, #28a745) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# DATA USER & PASSWORD
# ────────────────────────────────────────────────
USER_PASSWORDS = {
    "dian": "QWERTY21ab",
    "icha": "udin99",
    "nissa": "tung22",
    "inggi": "udin11",
    "lisa": "tung55",
    "tamu": "tamu123",
}

# ────────────────────────────────────────────────
# HALAMAN LOGIN
# ────────────────────────────────────────────────
if not st.session_state.logged_in:
    st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    # Logo dari GitHub - GANTI URL RAW INI DENGAN YANG BENAR MILIKMU!
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    try:
        st.image(
            "https://raw.githubusercontent.com/PintarKantor/nama-repo-mu/main/PINTAR.png",
            use_container_width=True
        )
    except:
        st.markdown('<h2 style="color:#28a745; margin:0;">PINTAR MEDIA</h2>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="Username...", key="login_username", label_visibility="collapsed")
    password = st.text_input("Password", type="password", placeholder="Password...", key="login_password", label_visibility="collapsed")

    if st.button("MASUK", type="primary"):
        clean_user = username.strip().lower()
        if clean_user in USER_PASSWORDS and password == USER_PASSWORDS[clean_user]:
            st.session_state.logged_in = True
            st.session_state.user = clean_user
            st.session_state.login_time = time.time()
            st.markdown(f'<div class="welcome-msg">Selamat datang, {clean_user.capitalize()}!</div>', unsafe_allow_html=True)
            time.sleep(2)
            st.rerun()
        else:
            st.error("Username atau password salah.")

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">© 2026 PINTAR MEDIA • Akses Aman</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ────────────────────────────────────────────────
# SIDEBAR NAVIGASI
# ────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"**User aktif:** {st.session_state.user.upper()}")
    st.caption(f"Login sejak: {datetime.fromtimestamp(st.session_state.login_time, tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M WIB')}")

    menu_options = [
        "🚀 RUANG PRODUKSI",
        "🧠 PINTAR AI LAB",
        "⚡ QUICK PROMPT",
        "📋 TUGAS KERJA",
        "⚡ KENDALI TIM"
    ]
    selected_menu = st.radio("Pilih Ruangan", menu_options, label_visibility="collapsed")

    st.divider()
    if st.button("🚪 Keluar Sistem", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ────────────────────────────────────────────────
# MENU UTAMA
# ────────────────────────────────────────────────
if selected_menu == "🚀 RUANG PRODUKSI":
    st.title("🚀 RUANG PRODUKSI")
    st.caption("Buat storyboard adegan secara konsisten (bisa tambah adegan manual)")

    if 'scenes' not in st.session_state:
        st.session_state.scenes = [""] * 10
    if 'scene_count' not in st.session_state:
        st.session_state.scene_count = 10

    col_slider, col_apply = st.columns([4, 1])
    with col_slider:
        new_count = st.slider("Jumlah adegan", min_value=1, max_value=50, value=st.session_state.scene_count)
    with col_apply:
        if st.button("Terapkan"):
            st.session_state.scene_count = new_count
            if new_count > len(st.session_state.scenes):
                st.session_state.scenes += [""] * (new_count - len(st.session_state.scenes))
            else:
                st.session_state.scenes = st.session_state.scenes[:new_count]
            st.rerun()

    for i in range(st.session_state.scene_count):
        st.session_state.scenes[i] = st.text_area(
            f"Adegan {i+1}",
            value=st.session_state.scenes[i],
            height=130,
            key=f"scene_input_{i}"
        )

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Simpan Project", type="primary", use_container_width=True):
            project = {
                "user": st.session_state.user,
                "timestamp": datetime.now(pytz.timezone('Asia/Jakarta')).isoformat(),
                "scene_count": st.session_state.scene_count,
                "scenes": st.session_state.scenes
            }
            json_data = json.dumps(project, indent=2, ensure_ascii=False)
            st.download_button(
                label="Download file project (.json)",
                data=json_data,
                file_name=f"pintar_project_{st.session_state.user}_{datetime.now().strftime('%Y%m%d_%H%M')}.json",
                mime="application/json",
                use_container_width=True
            )
    with col2:
        uploaded_file = st.file_uploader("Upload project sebelumnya (.json)", type=["json"])
        if uploaded_file is not None:
            try:
                data = json.load(uploaded_file)
                st.session_state.scene_count = data.get("scene_count", 10)
                st.session_state.scenes = data.get("scenes", [""] * st.session_state.scene_count)
                st.success("Project berhasil dimuat!")
                st.rerun()
            except Exception as e:
                st.error(f"Gagal membaca file: {str(e)}")

    if st.button("🚀 Generate Semua Prompt", type="primary", use_container_width=True):
        st.info("Fitur generate prompt lengkap akan ditambahkan di sini.")

elif selected_menu == "🧠 PINTAR AI LAB":
    st.title("🧠 PINTAR AI LAB")
    st.caption("Generate ide cerita / naskah dasar dari premis yang kamu berikan")

    premis_text = st.text_area(
        "Premis / Alur Utama Cerita",
        height=160,
        placeholder="Contoh: Seorang gadis desa menemukan cincin ajaib yang bisa membawanya ke dunia paralel..."
    )

    target_scenes = st.slider("Jumlah adegan yang diinginkan", 4, 20, 8)

    if st.button("Generate Ide Cerita", type="primary"):
        if not premis_text.strip():
            st.warning("Masukkan premis terlebih dahulu.")
        else:
            st.info("Fitur ini membutuhkan koneksi ke LLM (Groq / Gemini / OpenAI). Saat ini hanya contoh output.")
            st.markdown("""
            **Contoh hasil yang diharapkan:**
            Adegan 1:
            - Suasana: Pagi cerah di desa
            - Alur: Gadis menemukan cincin di bawah pohon
            - Dialog: "Ini... apa ya?"
            Adegan 2: ...
            """)

elif selected_menu == "⚡ QUICK PROMPT":
    st.title("⚡ QUICK PROMPT")
    st.caption("Buat prompt gambar dan video untuk satu adegan saja")

    adegan_desc = st.text_area("Deskripsi adegan lengkap", height=180)

    col_a, col_b = st.columns(2)
    with col_a:
        gaya = st.selectbox("Gaya visual", ["Realistis", "Anime", "3D Pixar", "Cyberpunk", "Vintage", "Horror"])
    with col_b:
        ratio = st.selectbox("Aspect Ratio", ["16:9 (landscape)", "9:16 (portrait)", "1:1 (square)", "4:3"])

    if st.button("Generate Prompt", type="primary"):
        if adegan_desc.strip():
            ar_clean = ratio.split()[0]
            st.subheader("Prompt Gambar")
            st.code(f"{adegan_desc}, {gaya.lower()} style, cinematic lighting, ultra detailed, sharp focus --ar {ar_clean} --v 6 --q 2")
            st.subheader("Prompt Video")
            st.code(f"{adegan_desc}, {gaya.lower()} style, smooth cinematic motion, 8k, dynamic camera --ar {ar_clean} --fps 30")
        else:
            st.warning("Isi deskripsi adegan terlebih dahulu.")

elif selected_menu == "📋 TUGAS KERJA":
    st.title("📋 TUGAS KERJA")
    st.info("Daftar tugas harian / mingguan untuk staff")
    st.markdown("""
    **Tugas hari ini (contoh):**
    - Review storyboard dari 3 project
    - Generate prompt untuk iklan baru
    - Upload 2 video final ke platform
    - Koordinasi revisi dengan klien
    """)

elif selected_menu == "⚡ KENDALI TIM":
    st.title("⚡ KENDALI TIM")
    st.caption("Dashboard monitoring aktivitas & kinerja tim")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total prompt dibuat minggu ini", "312", delta="↑ 58")
    with col2:
        st.metric("Adegan selesai", "245 / 280", delta="87.5%")

    st.subheader("Aktivitas Terbaru")
    st.table([
        {"Waktu": "12 Feb 2026 13:30", "User": "icha", "Aksi": "Generate 15 adegan", "Durasi": "22 menit"},
        {"Waktu": "12 Feb 2026 10:15", "User": "nissa", "Aksi": "Load & edit project kemarin", "Durasi": "9 menit"},
    ])

    st.info("Untuk tracking real-time, sebaiknya integrasikan Google Sheets atau database sederhana.")
