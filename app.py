import streamlit as st
from datetime import datetime

# --- 1. CONFIG & SESSION ---
st.set_page_config(page_title="Pintar Media | AI Studio", layout="wide")

if 'login_time' not in st.session_state:
    st.session_state.login_time = datetime.now()

# --- 2. STYLE CSS (Premium Dark Mode) ---
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

    /* Custom Radio Sidebar agar mirip Menu */
    div[data-testid="stSidebarUserContent"] .st-emotion-cache-17l36p9 {
        padding-top: 2rem;
    }
    
    /* Footer Status */
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

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='color: white; letter-spacing: 1px;'>LAB AREA</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Menu dengan Urutan Sesuai Gambar
    menu = st.radio(
        "MENU UTAMA",
        [
            "🚀 RUANG PRODUKSI", 
            "🧠 PINTAR AI LAB", 
            "⚡ QUICK PROMPT", 
            "📋 TUGAS KERJA", 
            "⚡ KENDALI TIM"
        ],
        index=0 # Menjadikan RUANG PRODUKSI sebagai default
    )
    
    # Status Minimalis di Bawah
    uptime = datetime.now() - st.session_state.login_time
    st.markdown(f"""
        <div class="status-footer">
            CONNECTED: {uptime.seconds // 60}M ACTIVE <br>
            STATION: PINTAR_MEDIA_01
        </div>
    """, unsafe_allow_html=True)

# --- 4. MAIN CONTENT ROUTER ---

if "RUANG PRODUKSI" in menu:
    st.markdown("### 📝 Detail Adegan Storyboard")
    
    # --- BAGIAN 1: KARAKTER ---
    with st.expander("👥 Nama Karakter Utama & Penampilan Fisik! (WAJIB ISI)", expanded=True):
        st.markdown("<p style='font-size: 0.9rem; color: #8b949e;'>Total Karakter Utama dalam Project</p>", unsafe_allow_html=True)
        num_chars = st.number_input("Total Karakter", min_value=1, max_value=5, value=2, step=1, label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        char_cols = st.columns(num_chars)
        for i in range(num_chars):
            with char_cols[i]:
                st.markdown(f"👤 **Karakter Utama {i+1}**")
                st.text_input(f"Nama {i+1}", placeholder="Nama Karakter...", key=f"n_{i}", label_visibility="collapsed")
                st.text_area(f"Ciri {i+1}", placeholder="Deskripsi fisik...", key=f"d_{i}", height=120, label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- BAGIAN 2: ADEGAN ---
    # Adegan 1
    with st.expander("🟢 ADEGAN 1", expanded=False):
        col_a1, col_b1 = st.columns([1, 2])
        with col_a1:
            st.text_input("Lokasi / Latar", placeholder="E.g. Ruang Tamu", key="loc1")
        with col_b1:
            st.text_area("Aksi / Kejadian", placeholder="Apa yang dilakukan karakter?", key="act1")

    # Adegan 2
    with st.expander("🎬 ADEGAN 2", expanded=False):
        col_a2, col_b2 = st.columns([1, 2])
        with col_a2:
            st.text_input("Lokasi / Latar ", placeholder="E.g. Hutan", key="loc2")
        with col_b2:
            st.text_area("Aksi / Kejadian ", placeholder="Detail aksi karakter...", key="act2")

    # --- BAGIAN 3: GENERATOR ---
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 COMPILE MASTER PROMPT", use_container_width=True):
        st.toast("Menyusun data...")
        # Tampilkan hasil prompt di sini dengan st.code()

elif "PINTAR AI LAB" in menu:
    st.title("🧠 Pintar AI Lab")
    st.write("Eksperimen model dan riset prompt.")

elif "QUICK PROMPT" in menu:
    st.title("⚡ Quick Prompt")
    st.write("Generator instan untuk kebutuhan cepat.")

else:
    st.title("🚧 Work in Progress")
    st.write(f"Halaman {menu} sedang disiapkan.")
