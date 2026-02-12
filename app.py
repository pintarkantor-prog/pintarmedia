import streamlit as st
from datetime import datetime

# --- 1. DATA USER & KONFIGURASI ---
users = {
    "dian": "QWERTY21ab",
    "icha": "udin99",
    "nissa": "tung22",
    "inggi": "udin33",
    "lisa": "tung66",
    "tamu": "123"
}

st.set_page_config(page_title="Pintar Media | AI Studio", layout="wide")

# --- 2. SESSION STATE ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'login_time' not in st.session_state:
    st.session_state.login_time = None

# --- 3. CUSTOM CSS (DARK THEME PREMIUM) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] { 
        background-color: #161b22 !important; 
        border-right: 1px solid #30363d; 
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }
    .streamlit-expanderContent {
        background-color: #0d1117 !important;
        border: 1px solid #30363d !important;
        border-top: none !important;
    }

    /* Input Fields */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }

    /* Status Footer */
    .status-footer {
        position: fixed;
        bottom: 20px;
        left: 20px;
        font-size: 10px;
        color: #484f58;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. FUNGSI HALAMAN LOGIN ---
def show_login():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h2 style='text-align: center; color: white;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #8b949e;'>AI Production Studio Access</p>", unsafe_allow_html=True)
        
        username = st.text_input("Username", key="login_user").lower()
        password = st.text_input("Password", type="password", key="login_pass")
        
        if st.button("LOGIN", use_container_width=True):
            if username in users and users[username] == password:
                st.session_state.logged_in = True
                st.session_state.user_name = username
                st.session_state.login_time = datetime.now()
                st.rerun()
            else:
                st.error("Credential tidak valid.")

# --- 5. FUNGSI APLIKASI UTAMA ---
def show_main():
    # --- SIDEBAR ---
    with st.sidebar:
        st.markdown("<h2 style='color: white; letter-spacing: 1px;'>LAB AREA</h2>", unsafe_allow_html=True)
        st.markdown(f"👤 User: **{st.session_state.user_name.upper()}**")
        st.markdown("---")
        
        menu = st.radio(
            "MENU UTAMA",
            ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"]
        )
        
        st.markdown("<br>"*5, unsafe_allow_html=True)
        if st.button("LOGOUT", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

        # Footer Status Minimalis
        uptime = datetime.now() - st.session_state.login_time
        st.markdown(f"""
            <div class="status-footer">
                STATION: PINTAR_MEDIA_01 <br>
                ACTIVE: {uptime.seconds // 60}M — {datetime.now().strftime('%d.%m.%y')}
            </div>
        """, unsafe_allow_html=True)

    # --- CONTENT ROUTER ---
    if "RUANG PRODUKSI" in menu:
        st.markdown("### 📝 Detail Adegan Storyboard")
        
        # Karakter Utama
        with st.expander("👥 Nama Karakter Utama & Penampilan Fisik! (WAJIB ISI)", expanded=True):
            st.write("Total Karakter Utama dalam Project")
            num_chars = st.number_input("", min_value=1, max_value=5, value=2, step=1, label_visibility="collapsed")
            
            char_cols = st.columns(num_chars)
            for i in range(num_chars):
                with char_cols[i]:
                    st.markdown(f"👤 **Karakter Utama {i+1}**")
                    st.text_input(f"Nama {i+1}", key=f"n_{i}", label_visibility="collapsed", placeholder="Nama...")
                    st.text_area(f"Ciri {i+1}", key=f"d_{i}", height=120, label_visibility="collapsed", placeholder="Deskripsi fisik...")

        st.markdown("<br>", unsafe_allow_html=True)

        # Adegan
        with st.expander("🟢 ADEGAN 1"):
            col_a1, col_b1 = st.columns([1, 2])
            with col_a1: st.text_input("Lokasi", key="loc1", placeholder="Lokasi...")
            with col_b1: st.text_area("Aksi", key="act1", placeholder="Kejadian...")

        with st.expander("🎬 ADEGAN 2"):
            col_a2, col_b2 = st.columns([1, 2])
            with col_a2: st.text_input("Lokasi ", key="loc2", placeholder="Lokasi...")
            with col_b2: st.text_area("Aksi ", key="act2", placeholder="Kejadian...")

        if st.button("🚀 COMPILE MASTER PROMPT", use_container_width=True):
            st.success("Data berhasil dikompilasi!")

    else:
        st.title(menu)
        st.info(f"Halaman {menu} sedang dalam pengembangan.")

# --- 6. ROUTER ---
if not st.session_state.logged_in:
    show_login()
else:
    show_main()
