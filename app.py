import streamlit as st
import json
import time
from datetime import datetime
import pytz

# ────────────────────────────────────────────────
# INISIALISASI SESSION STATE SECARA AMAN (HARUS DI ATAS SEMUA)
# ────────────────────────────────────────────────
# Ini wajib untuk mencegah error "_missing_attr_error_message"
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.login_time = None

# Auto logout setelah 10 jam (36.000 detik)
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

# CSS: Blokir HP + tema gelap dengan aksen hijau
st.markdown("""
    <style>
    /* Blokir akses dari HP / layar kecil */
    @media (max-width: 1024px) {
        .stApp { display: none !important; }
        body::before {
            content: "⚠️ Aplikasi ini hanya bisa diakses dari komputer / layar lebar";
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: #0e1117;
            color: #ffffff;
            font-size: 1.5rem;
            font-weight: bold;
            text-align: center;
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            z-index: 9999;
        }
    }
    /* Tema gelap + hijau accent */
    :root {
        --bg: #0e1117;
        --text: #e0e0e0;
        --accent: #1d976c;
        --accent-light: #28a745;
    }
    .stApp { background-color: var(--bg); color: var(--text); }
    .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, var(--accent), var(--accent-light));
        color: white;
        border: none;
    }
    h1, h2, h3 { color: var(--accent-light); }
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
    st.markdown("""
        <style>
        .login-container {
            max-width: 400px;
            margin: 100px auto;
            padding: 40px 30px;
            background: #1a1c24;
            border-radius: 16px;
            border: 1px solid #2d3748;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
            text-align: center;
        }
        .login-title {
            font-size: 3.2rem;
            font-weight: bold;
            background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #96c93d, #feca57);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 30px;
        }
        .welcome-message {
            text-align: center;
            font-size: 1.8rem;
            color: #28a745;
            margin: 20px 0;
            font-weight: bold;
        }
        .stTextInput > div > div > input {
            background: #0e1117;
            color: white;
            border: 1px solid #3a3f4a;
            border-radius: 8px;
            padding: 12px;
        }
        .stTextInput label {
            color: #a0a0a0 !important;
            font-size: 0.95rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    # Logo dari GitHub (ganti URL raw ini dengan URL asli milikmu!)
    try:
        st.image(
            "https://raw.githubusercontent.com/PintarKantor/nama-repo-mu/main/PINTAR.png",
            use_container_width=True
        )
    except:
        st.markdown('<h1 class="login-title">PINTAR MEDIA</h1>', unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="Username...", key="login_username")
    password = st.text_input("Password", type="password", placeholder="Password...", key="login_password")

    if st.button("MASUK", type="primary", use_container_width=True):
        clean_user = username.strip().lower()
        if clean_user in USER_PASSWORDS and password == USER_PASSWORDS[clean_user]:
            st.session_state.logged_in = True
            st.session_state.user = clean_user
            st.session_state.login_time = time.time()
            st.markdown(f'<div class="welcome-message">Selamat datang, {clean_user.capitalize()}!</div>', unsafe_allow_html=True)
            time.sleep(2)
            st.rerun()
        else:
            st.error("Username atau password salah.")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align:center; color:#666; margin-top:30px; font-size:0.85rem;">
            © 2026 PINTAR MEDIA • Akses Aman
        </div>
    """, unsafe_allow_html=True)

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
# MENU UTAMA (sama seperti sebelumnya)
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
        st.info("Fitur generate prompt lengkap akan ditambahkan di sini (genre, lighting, camera, dll).")

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




