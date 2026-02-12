# ==============================================================================
# BAGIAN 1: KONFIGURASI DAN DATABASE PENGGUNA
# ==============================================================================
import streamlit as st
from datetime import datetime, timedelta

DAFTAR_USER = {
    "dian": "QWERTY21ab", "icha": "udin99", "nissa": "tung22",
    "inggi": "udin33", "lisa": "tung66", "tamu": "123"
}

st.set_page_config(page_title="PINTAR MEDIA | AI Studio", layout="wide")

# ==============================================================================
# BAGIAN 2: SISTEM KEAMANAN & TAMPILAN LOGIN (AUTENTIKASI)
# ==============================================================================
def inisialisasi_keamanan():
    if 'sudah_login' not in st.session_state:
        st.session_state.sudah_login = False
    
    params = st.query_params
    if "auth" in params and params["auth"] == "true":
        if not st.session_state.sudah_login:
            st.session_state.sudah_login = True
            st.session_state.user_aktif = params.get("user", "User")
            st.session_state.waktu_login = datetime.now()

def proses_login(user, pwd):
    if user in DAFTAR_USER and DAFTAR_USER[user] == pwd:
        st.session_state.sudah_login = True
        st.session_state.user_aktif = user
        st.session_state.waktu_login = datetime.now()
        st.query_params.update({"auth": "true", "user": user})
        st.rerun()
    else:
        st.error("Username atau Password salah.")

def tampilkan_halaman_login():
    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_m, col_r = st.columns([2, 1, 2]) 
    
    with col_m:
        try:
            st.image("PINTAR.png", use_container_width=True)
        except:
            st.markdown("<h2 style='text-align: center;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
        
        with st.form("login_station"):
            u = st.text_input("Username", placeholder="Username...", key="login_user").lower()
            p = st.text_input("Password", type="password", placeholder="Password...", key="login_pass")
            
            submit = st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True)
            
            if submit:
                proses_login(u, p)
        
        st.markdown("<p style='text-align: center; color: #484f58; font-size: 11px; margin-top: 15px;'>Secure Access - PINTAR MEDIA</p>", unsafe_allow_html=True)

def cek_autentikasi():
    if st.session_state.sudah_login:
        if 'waktu_login' in st.session_state:
            durasi = datetime.now() - st.session_state.waktu_login
            if durasi > timedelta(hours=10):
                proses_logout()
                return False
        return True
    return False

def proses_logout():
    st.session_state.sudah_login = False
    st.session_state.user_aktif = ""
    st.query_params.clear()
    st.rerun()

# ==============================================================================
# BAGIAN 3: PENGATURAN TAMPILAN (CSS) - UPDATED
# ==============================================================================
def pasang_css_kustom():
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; color: #e0e0e0; }
        [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
        
        /* BOX LOGIN */
        div[data-testid="stForm"] {
            border: 1px solid #30363d !important;
            border-radius: 12px !important;
            padding: 20px !important;
        }

        /* TOMBOL DEGRADASI HIJAU */
        div[data-testid="stFormSubmitButton"] button {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
            color: white !important;
            border: none !important;
            height: 50px !important;
            border-radius: 10px !important;
            transition: all 0.4s ease !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
        }
        
        div[data-testid="stFormSubmitButton"] button p {
            color: white !important; font-weight: bold !important; font-size: 16px !important;
        }

        /* STYLE BARU: KOTAK HASIL PROMPT */
        .prompt-result {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-left: 5px solid #10b981;
            padding: 15px;
            border-radius: 8px;
            color: #e0e0e0;
            font-family: 'Courier New', Courier, monospace;
            margin-bottom: 20px;
            font-size: 14px;
        }

        div[data-baseweb="input"], div[data-baseweb="textarea"] {
            background-color: #1d2127 !important;
            border: 1px solid #30363d !important;
            border-radius: 8px !important;
        }

        .status-footer { position: fixed; bottom: 20px; left: 20px; font-size: 10px; color: #484f58; text-transform: uppercase; font-family: monospace; }
        
        @media (max-width: 1024px) {
            .main { display: none !important; }
            [data-testid="stSidebar"] { display: none !important; }
            .stApp::before { content: '⚠️ AKSES PC ONLY'; display: flex; justify-content: center; align-items: center; height: 100vh; color: white; background-color: #0e1117; }
        }
        </style>
        """, unsafe_allow_html=True)
    
# ==============================================================================
# BAGIAN 4: NAVIGASI SIDEBAR
# ==============================================================================
def tampilkan_navigasi_sidebar():
    with st.sidebar:
        st.markdown("<br>", unsafe_allow_html=True)
        pilihan = st.radio("NAVIGASI WORKSPACE", ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"])
        st.markdown("<br>"*12, unsafe_allow_html=True)
        if st.button("LOGOUT SYSTEM", use_container_width=True):
            proses_logout()
        user = st.session_state.get("user_aktif", "USER").upper()
        st.markdown(f'<div class="status-footer">STATION: {user}_SESSION<br>STATUS: AKTIF</div>', unsafe_allow_html=True)
    return pilihan

# ==============================================================================
# BAGIAN 5: MODUL-MODUL PENDUKUNG
# ==============================================================================
def tampilkan_ai_lab(): st.markdown("### 🧠 Pintar AI Lab"); st.info("Area riset prompt.")
def tampilkan_quick_prompt(): st.markdown("### ⚡ Quick Prompt")
def tampilkan_tugas_kerja(): st.markdown("### 📋 Tugas Kerja")
def tampilkan_kendali_tim(): st.markdown("### ⚡ Kendali Tim")

# ==============================================================================
# BAGIAN 6: MODUL UTAMA - RUANG PRODUKSI (HYBRID MASTER COMPILER)
# ==============================================================================
def tampilkan_ruang_produksi():
    st.markdown("### 🚀 Ruang Produksi - Hybrid Engine")
    st.write("---")
    
    # 1. IDENTITY LOCK (Mengunci Kemiripan Karakter)
    with st.expander("🛡️ IDENTITY LOCK - Referensi Foto", expanded=True):
        juml = st.number_input("Jumlah Karakter di Scene", 1, 3, 2)
        karakter_data = []
        cols = st.columns(juml)
        for i in range(juml):
            with cols[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                nama = st.text_input(f"Nama", key=f"h_nama_{i}", placeholder="Udin/Sari/Tung")
                pakaian = st.text_input(f"Pakaian", key=f"h_wear_{i}", placeholder="Kaos oranye/Batik")
                fisik = st.text_area(f"Ciri Fisik Utama", key=f"h_fix_{i}", height=80, placeholder="Maintain 100% exact facial features...")
                karakter_data.append({"nama": nama, "wear": pakaian, "fisik": fisik})

    # 2. SCENE & INTERACTION (Kekuatan Grup 2)
    with st.expander("🎬 DETAIL ALUR & EMOSI", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            lokasi = st.text_input("Lokasi / Environment", placeholder="Pasar tradisional/Jalan raya")
            mood = st.selectbox("Cinematic Style", ["Hyper-Realistic RAW Photo", "3D Animation Style", "Cinematic Film 90s"])
        with c2:
            rasio = st.selectbox("Aspect Ratio", ["16:9", "9:16", "1:1"])
            kamera = st.selectbox("Gerakan Kamera", ["Static Shot", "Tracking Side View", "Slow Zoom In", "Handheld Cinematic"])
            
        aksi = st.text_area("Aksi & Interaksi Karakter", height=100, placeholder="Udin menyalip Tung sambil tertawa...")
        dialog_cue = st.text_input("Acting Cue (Dialog untuk Emosi)", placeholder="Udin: 'Duluan ya Tung!'")

    # 3. HYBRID COMPILER LOGIC
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 GENERATE HYBRID MASTER PROMPT", use_container_width=True):
        st.markdown("---")
        
        # Logic Penggabungan Identitas (Grup 1 Style)
        char_identities = " AND ".join([
            f"[[ CHARACTER_{c['nama'].upper()}: \"{c['fisik']}\" maintain 100% exact facial features, anatomy, and textures. Wearing: {c['wear']} ]]" 
            for c in karakter_data if c['nama']
        ])

        # COMMON TECHNICAL RULES (Anti-Kacau)
        tech_rules = "STRICT VISUAL RULE: CLEAN PHOTOGRAPHY. NO TEXT. NO SUBTITLES. NO WATERMARK. f/11 aperture, infinite depth of field, ultra-sharp focus, 8k RAW photo, tactile textures."

        # OUTPUT 1: IMAGE PROMPT (Optimized for Grok/Flux)
        image_p = f"{char_identities}. Scene: {aksi} at {lokasi}. Mood: {mood}. {tech_rules} --ar {rasio}"

        # OUTPUT 2: VIDEO PROMPT (Optimized for Veo)
        video_p = f"{char_identities}. Action & Motion: {aksi} at {lokasi}. {mood} video. Acting Cue: '{dialog_cue}' (STRICTLY NO TEXT ON SCREEN). Camera: {kamera}. Smooth fluid complex movement, no morphing, no flickering, 60fps, cinematic high-fidelity animation."

        # DISPLAY RESULTS
        st.subheader("📋 Production Ready Prompts")
        
        st.markdown("##### 🖼️ Grok Image Prompt (Identity Lock)")
        st.markdown(f'<div class="prompt-result">{image_p}</div>', unsafe_allow_html=True)
        
        st.markdown("##### 🎬 Veo Video Prompt (Motion Control)")
        st.markdown(f'<div class="prompt-result">{video_p}</div>', unsafe_allow_html=True)
        
        st.success("Hybrid Prompt Berhasil Disusun! Karakter akan konsisten merujuk pada foto referensi.")

# ==============================================================================
# BAGIAN 7: PENGENDALI UTAMA (MAIN ROUTER)
# ==============================================================================
def utama():
    inisialisasi_keamanan()
    pasang_css_kustom()
    
    if not cek_autentikasi():
        tampilkan_halaman_login()
    else:
        menu = tampilkan_navigasi_sidebar()
        if menu == "🚀 RUANG PRODUKSI": tampilkan_ruang_produksi()
        elif menu == "🧠 PINTAR AI LAB": tampilkan_ai_lab()
        elif menu == "⚡ QUICK PROMPT": tampilkan_quick_prompt()
        elif menu == "📋 TUGAS KERJA": tampilkan_tugas_kerja()
        elif menu == "⚡ KENDALI TIM": tampilkan_kendali_tim()

if __name__ == "__main__":
    utama()



