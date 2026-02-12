# ==============================================================================
# PART 1: KONFIGURASI & DATABASE USER
# ==============================================================================
import streamlit as st
from datetime import datetime, timedelta

# Daftar akun resmi Pintar Media
USERS_DB = {
    "dian": "QWERTY21ab",
    "icha": "udin99",
    "nissa": "tung22",
    "inggi": "udin33",
    "lisa": "tung66",
    "tamu": "123"
}

# Konfigurasi halaman diletakkan paling atas
st.set_page_config(
    page_title="Pintar Media | AI Studio", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ==============================================================================
# PART 2: PERSISTENT SESSION MANAGEMENT (ANTI-REFRESH & 10H TIMEOUT)
# ==============================================================================
# Inisialisasi state jika belum ada
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'login_time' not in st.session_state:
    st.session_state.login_time = None

# Logika Logout Otomatis 10 Jam
if st.session_state.logged_in and st.session_state.login_time:
    # Memastikan login_time tetap dalam objek datetime
    if isinstance(st.session_state.login_time, str):
        st.session_state.login_time = datetime.fromisoformat(st.session_state.login_time)
        
    elapsed = datetime.now() - st.session_state.login_time
    if elapsed > timedelta(hours=10):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.warning("Sesi berakhir (10 Jam).")
        st.rerun()

# ==============================================================================
# PART 3: CUSTOM CSS (DARK THEME & PROTEKSI PC ONLY)
# ==============================================================================
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
    
    /* Expander / Box Styling */
    .streamlit-expanderHeader {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }
    .streamlit-expanderContent { background-color: #0d1117 !important; border: 1px solid #30363d; border-top: none; }

    /* Input & Textarea */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }

    /* Footer Sidebar */
    .status-footer {
        position: fixed; bottom: 20px; left: 20px; font-size: 10px;
        color: #484f58; text-transform: uppercase; letter-spacing: 1px;
        line-height: 1.5; font-family: monospace;
    }

    /* PROTEKSI PC ONLY */
    @media (max-width: 1024px) {
        .main { display: none !important; }
        [data-testid="stSidebar"] { display: none !important; }
        .stApp::before {
            content: '⚠️ AKSES TERBATAS: Gunakan perangkat Desktop/PC untuk mengakses Ruang Produksi.';
            display: flex; justify-content: center; align-items: center;
            height: 100vh; color: white; text-align: center; padding: 40px; background-color: #0e1117;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# PART 4: HALAMAN LOGIN
# ==============================================================================
def login_screen():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<h2 style='text-align: center;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #8b949e;'>AI Production Studio Access</p>", unsafe_allow_html=True)
        
        user_val = st.text_input("Username", key="u_input").lower()
        pass_val = st.text_input("Password", type="password", key="p_input")
        
        if st.button("LOG IN", use_container_width=True):
            if user_val in USERS_DB and USERS_DB[user_val] == pass_val:
                st.session_state.logged_in = True
                st.session_state.user_name = user_val
                st.session_state.login_time = datetime.now()
                st.rerun()
            else:
                st.error("Credential salah.")

# ==============================================================================
# PART 5: SIDEBAR NAVIGATION
# ==============================================================================
def main_sidebar():
    with st.sidebar:
        st.markdown("<br>", unsafe_allow_html=True)
        # Navigasi Menu
        choice = st.radio(
            "MENU UTAMA",
            ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"]
        )
        
        st.markdown("<br>"*12, unsafe_allow_html=True)
        
        if st.button("LOGOUT SYSTEM", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.session_state.login_time = None
            st.rerun()

        # Footer Status
        if st.session_state.login_time:
            uptime = datetime.now() - st.session_state.login_time
            st.markdown(f"""
                <div class="status-footer">
                    STATION: {st.session_state.user_name.upper()}_SESSION <br>
                    ACTIVE: {uptime.seconds // 60}M — {st.session_state.login_time.strftime('%d.%m.%y')}
                </div>
            """, unsafe_allow_html=True)
        return choice

# ==============================================================================
# PART 6: RUANG PRODUKSI (KONTEN UTAMA)
# ==============================================================================
def show_ruang_produksi():
    st.markdown("### 📝 Detail Adegan Storyboard")
    
    with st.expander("👥 Karakter Utama & Penampilan Fisik", expanded=True):
        num = st.number_input("Jumlah Karakter Utama", 1, 5, 2)
        st.markdown("<br>", unsafe_allow_html=True)
        cols = st.columns(num)
        for i in range(num):
            with cols[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                st.text_input(f"Nama Karakter", key=f"nm_{i}", placeholder="Input Nama...")
                st.text_area(f"Ciri Fisik", key=f"cf_{i}", height=120, placeholder="Ciri fisik...")

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🟢 ADEGAN 1", expanded=False):
        c1, c2 = st.columns([1, 2])
        with c1: st.text_input("Lokasi", key="loc_1", placeholder="Lokasi Adegan 1...")
        with c2: st.text_area("Aksi / Kejadian", key="act_1", placeholder="Apa yang terjadi?")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 COMPILE MASTER PROMPT", use_container_width=True):
        st.success("Data Storyboard Berhasil Dikompilasi.")

# ==============================================================================
# PART 7: MAIN ROUTER
# ==============================================================================
if not st.session_state.logged_in:
    login_screen()
else:
    active_menu = main_sidebar()
    if active_menu == "🚀 RUANG PRODUKSI":
        show_ruang_produksi()
    else:
        st.title(active_menu)
        st.info(f"Modul {active_menu} sedang dalam tahap pengembangan.")
