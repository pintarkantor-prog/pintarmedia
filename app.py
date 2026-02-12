# ==============================================================================
# PART 1: KONFIGURASI & DATABASE USER
# ==============================================================================
import streamlit as st
from datetime import datetime

# Daftar user resmi Pintar Media
USERS_DB = {
    "dian": "QWERTY21ab",
    "icha": "udin99",
    "nissa": "tung22",
    "inggi": "udin33",
    "lisa": "tung66",
    "tamu": "123"
}

st.set_page_config(
    page_title="Pintar Media | AI Studio", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ==============================================================================
# PART 2: SESSION MANAGEMENT (ANTI-LOGOUT REFRESH)
# ==============================================================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'login_time' not in st.session_state:
    st.session_state.login_time = None

# ==============================================================================
# PART 3: CUSTOM CSS (DARK THEME & PROTEKSI PC ONLY)
# ==============================================================================
st.markdown("""
    <style>
    /* Global Background */
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    
    /* Sidebar Area */
    [data-testid="stSidebar"] { 
        background-color: #161b22 !important; 
        border-right: 1px solid #30363d; 
    }
    
    /* Expander / Box Adegan */
    .streamlit-expanderHeader {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        font-size: 14px !important;
    }
    .streamlit-expanderContent {
        background-color: #0d1117 !important;
        border: 1px solid #30363d !important;
    }

    /* Input & Textarea Dark Style */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }

    /* Footer Sidebar (Status Info) */
    .status-footer {
        position: fixed;
        bottom: 20px;
        left: 20px;
        font-size: 10px;
        color: #484f58;
        text-transform: uppercase;
        letter-spacing: 1px;
        line-height: 1.5;
        font-family: 'Courier New', Courier, monospace;
    }

    /* --- PROTEKSI PC ONLY --- */
    @media (max-width: 1024px) {
        .main { display: none !important; }
        [data-testid="stSidebar"] { display: none !important; }
        .stApp::before {
            content: '⚠️ AKSES TERBATAS: Sistem Ruang Produksi Pintar Media hanya dapat diakses melalui perangkat PC / Desktop.';
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
            text-align: center;
            padding: 40px;
            background-color: #0e1117;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# PART 4: LOGIKA HALAMAN LOGIN
# ==============================================================================
def show_login_page():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    
    with col2:
        st.markdown("<h2 style='text-align: center; color: white;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #8b949e;'>AI Production Studio Login</p>", unsafe_allow_html=True)
        
        user_input = st.text_input("Username").lower()
        pass_input = st.text_input("Password", type="password")
        
        if st.button("LOG IN", use_container_width=True):
            if user_input in USERS_DB and USERS_DB[user_input] == pass_input:
                st.session_state.logged_in = True
                st.session_state.user_name = user_input
                st.session_state.login_time = datetime.now()
                st.rerun()
            else:
                st.error("Credential tidak valid. Silakan hubungi admin.")

# ==============================================================================
# PART 5: SIDEBAR NAVIGATION & FOOTER STATUS
# ==============================================================================
def show_sidebar():
    with st.sidebar:
        st.markdown("<h2 style='color: white; letter-spacing: 2px;'>LAB AREA</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Menu Navigasi
        selection = st.radio(
            "MENU UTAMA",
            ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"]
        )
        
        st.markdown("<br>"*8, unsafe_allow_html=True)
        
        # Logout Area
        if st.button("LOGOUT SYSTEM", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.rerun()

        # Footer Dinamis: Station Info & Uptime
        uptime = datetime.now() - st.session_state.login_time
        st.markdown(f"""
            <div class="status-footer">
                STATION: {st.session_state.user_name.upper()}_SESSION <br>
                ACTIVE: {uptime.seconds // 60}M — {datetime.now().strftime('%d.%m.%y')}
            </div>
        """, unsafe_allow_html=True)
        
        return selection

# ==============================================================================
# PART 6: KONTEN UTAMA - RUANG PRODUKSI
# ==============================================================================
def ruang_produksi():
    st.markdown("### 📝 Detail Adegan Storyboard")
    
    # --- SUB-PART: KARAKTER ---
    with st.expander("👥 Karakter Utama & Penampilan Fisik", expanded=True):
        num_chars = st.number_input("Jumlah Karakter Utama", 1, 5, 2)
        st.markdown("<br>", unsafe_allow_html=True)
        
        char_cols = st.columns(num_chars)
        for i in range(num_chars):
            with char_cols[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                st.text_input(f"Nama Karakter", key=f"name_{i}", placeholder="Input Nama...")
                st.text_area(f"Ciri Fisik", key=f"desc_{i}", height=120, placeholder="Rambut, Pakaian, Atribut...")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SUB-PART: DAFTAR ADEGAN ---
    with st.expander("🟢 ADEGAN 1", expanded=False):
        c1a, c1b = st.columns([1, 2])
        with c1a: st.text_input("Lokasi", key="l1", placeholder="Lokasi Adegan 1...")
        with c1b: st.text_area("Aksi / Kejadian", key="a1", placeholder="Apa yang terjadi?")

    with st.expander("🎬 ADEGAN 2", expanded=False):
        c2a, c2b = st.columns([1, 2])
        with c2a: st.text_input("Lokasi", key="l2", placeholder="Lokasi Adegan 2...")
        with c2b: st.text_area("Aksi / Kejadian", key="a2", placeholder="Apa yang terjadi?")

    # --- SUB-PART: GENERATOR BUTTON ---
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 COMPILE MASTER PROMPT", use_container_width=True):
        st.success("Data Storyboard Berhasil Dikompilasi. Siap dikirim ke Gemini.")

# ==============================================================================
# PART 7: MAIN ROUTER (MENJALANKAN SISTEM)
# ==============================================================================
if not st.session_state.logged_in:
    show_login_page()
else:
    current_menu = show_sidebar()
    
    if current_menu == "🚀 RUANG PRODUKSI":
        ruang_produksi()
    else:
        st.title(current_menu)
        st.info(f"Modul {current_menu} sedang dalam tahap sinkronisasi data.")

# ==============================================================================
# END OF CODE
# ==============================================================================
