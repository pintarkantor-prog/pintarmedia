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

# Konfigurasi Halaman Utama
st.set_page_config(page_title="Pintar Media | AI Studio", layout="wide")

# --- 2. SESSION STATE (Agar tidak logout saat refresh) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'login_time' not in st.session_state:
    st.session_state.login_time = None

# --- 3. CUSTOM CSS (Dark Theme + Proteksi Mobile) ---
st.markdown("""
    <style>
    /* Dark Theme Base */
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

    /* Status Footer Sidebar */
    .status-footer {
        position: fixed;
        bottom: 20px;
        left: 20px;
        font-size: 10px;
        color: #484f58;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* PROTEKSI PC ONLY: Menyembunyikan konten jika lebar layar < 1024px */
    @media (max-width: 1024px) {
        .main { display: none !important; }
        [data-testid="stSidebar"] { display: none !important; }
        .stApp::before {
            content: '⚠️ AKSES TERBATAS: Sistem Ruang Produksi hanya dapat diakses melalui perangkat PC / Desktop demi kenyamanan tata letak storyboard.';
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
            font-weight: bold;
            text-align: center;
            padding: 40px;
            background-color: #0e1117;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. FUNGSI HALAMAN LOGIN ---
def show_login():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<h2 style='text-align: center;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #8b949e;'>AI Production Studio Login</p>", unsafe_allow_html=True)
        
        username = st.text_input("Username").lower()
        password = st.text_input("Password", type="password")
        
        if st.button("LOG IN", use_container_width=True):
            if username in users and users[username] == password:
                st.session_state.logged_in = True
                st.session_state.user_name = username
                st.session_state.login_time = datetime.now()
                st.rerun()
            else:
                st.error("Credential tidak valid.")

# --- 5. FUNGSI APLIKASI UTAMA (Ruang Produksi) ---
def show_main():
    # SIDEBAR NAVIGATION
    with st.sidebar:
        st.markdown("<h2 style='color: white; letter-spacing: 1px;'>LAB AREA</h2>", unsafe_allow_html=True)
        st.markdown(f"👤 Aktif: **{st.session_state.user_name.upper()}**")
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

    # ROUTER MENU
    if "RUANG PRODUKSI" in menu:
        st.markdown("### 📝 Detail Adegan Storyboard")
        
        # --- SEKSI KARAKTER ---
        with st.expander("👥 Nama Karakter Utama & Penampilan Fisik! (WAJIB ISI)", expanded=True):
            st.write("Total Karakter Utama dalam Project")
            num_chars = st.number_input("", min_value=1, max_value=5, value=2, step=1, label_visibility="collapsed")
            
            st.markdown("<br>", unsafe_allow_html=True)
            char_cols = st.columns(num_chars)
            char_info = {}
            
            for i in range(num_chars):
                with char_cols[i]:
                    st.markdown(f"👤 **Karakter Utama {i+1}**")
                    c_name = st.text_input(f"Nama {i+1}", key=f"name_{i}", placeholder="Nama...", label_visibility="collapsed")
                    c_desc = st.text_area(f"Ciri {i+1}", key=f"desc_{i}", placeholder="Ciri fisik...", height=100, label_visibility="collapsed")
                    char_info[i] = {"nama": c_name, "ciri": c_desc}

        st.markdown("<br>", unsafe_allow_html=True)

        # --- SEKSI ADEGAN ---
        with st.expander("🟢 ADEGAN 1", expanded=False):
            c1a, c1b = st.columns([1, 2])
            with c1a: loc1 = st.text_input("Lokasi Adegan 1", placeholder="Lokasi...", key="l1")
            with c1b: act1 = st.text_area("Aksi Adegan 1", placeholder="Kejadian...", key="a1")

        with st.expander("🎬 ADEGAN 2", expanded=False):
            c2a, c2b = st.columns([1, 2])
            with c2a: loc2 = st.text_input("Lokasi Adegan 2", placeholder="Lokasi...", key="l2")
            with c2b: act2 = st.text_area("Aksi Adegan 2", placeholder="Kejadian...", key="a2")

        # --- TOMBOL GENERATE ---
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 COMPILE MASTER PROMPT", use_container_width=True):
            st.success("Prompt berhasil disusun! (Tempelkan hasilnya ke Gemini)")
            # Logika penggabungan teks prompt bisa ditambahkan di sini

    elif "PINTAR AI LAB" in menu:
        st.title("🧠 Pintar AI Lab")
        st.info("Halaman eksperimen riset AI.")

    else:
        st.title(menu)
        st.write(f"Halaman {menu} sedang dalam tahap pengembangan.")

# --- 6. ROUTER UTAMA ---
if not st.session_state.logged_in:
    show_login()
else:
    show_main()
