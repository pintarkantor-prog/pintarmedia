import streamlit as st
from datetime import datetime
import time

# --- CONFIG HALAMAN ---
st.set_page_config(page_title="Pintar Media | AI Studio", layout="wide")

# --- SESSION STATE ---
if 'login_time' not in st.session_state:
    st.session_state.login_time = datetime.now()

# --- CUSTOM CSS (HIGH-END DARK MINIMALIST) ---
st.markdown("""
    <style>
    /* Background Utama & Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    .stApp {
        background-color: #0b0e11;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Minimalis */
    [data-testid="stSidebar"] {
        background-color: #0b0e11 !important;
        border-right: 1px solid #1e2329;
    }
    
    /* Menghilangkan border default expander */
    .streamlit-expanderHeader {
        background-color: #1e2329 !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        color: #ffffff !important;
    }
    .streamlit-expanderContent {
        border: 1px solid #1e2329 !important;
        border-top: none !important;
        border-bottom-left-radius: 12px;
        border-bottom-right-radius: 12px;
        background-color: #161b22;
    }

    /* Status Info (Minimalist Text) */
    .status-text {
        font-size: 0.75rem;
        color: #484f58;
        letter-spacing: 0.05rem;
        text-transform: uppercase;
    }

    /* Input & TextArea Styling */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: #0b0e11 !important;
        border: 1px solid #30363d !important;
        border-radius: 10px !important;
    }

    /* Button Gradient */
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
        border: none !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.6rem 2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (CLEAN VERSION) ---
with st.sidebar:
    st.markdown("<h2 style='color: white; font-weight: 600;'>Studio</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Navigasi tanpa ikon berlebihan
    menu = st.radio("WORKSPACE", ["Project Baru", "Riwayat", "Aset Karakter"])
    
    st.markdown("<br>"*15, unsafe_allow_html=True) # Jarak ke bawah
    
    # Info Session yang jauh lebih elegan (Hanya teks kecil di pojok bawah sidebar)
    uptime = datetime.now() - st.session_state.login_time
    st.markdown(f"""
    <div style='border-top: 1px solid #1e2329; padding-top: 20px;'>
        <p class="status-text">SYSTEM ACTIVE</p>
        <p style='color: #8b949e; font-size: 0.8rem;'>
            {datetime.now().strftime('%d.%m.%y')} — {uptime.seconds // 60}m active
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN CONTENT ---
st.markdown("<h3 style='color: white;'>Detail Adegan Storyboard</h3>", unsafe_allow_html=True)

# Container Karakter Utama
with st.expander("👥 Karakter Utama & Penampilan Fisik", expanded=True):
    # Kolom untuk jumlah karakter
    col_qty = st.columns([1, 4])
    with col_qty[0]:
        num_chars = st.number_input("Total", min_value=1, max_value=4, value=2)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    char_cols = st.columns(num_chars)
    char_data = {}
    
    for i in range(num_chars):
        with char_cols[i]:
            st.markdown(f"<p style='color: #8b949e; font-size: 0.9rem;'>KARAKTER {i+1}</p>", unsafe_allow_html=True)
            name = st.text_input(f"Nama {i+1}", key=f"n{i}", label_visibility="collapsed", placeholder="Nama...")
            desc = st.text_area(f"Ciri {i+1}", key=f"d{i}", label_visibility="collapsed", placeholder="Ciri fisik & atribut...", height=120)
            char_data[i] = {"nama": name, "ciri": desc}

# Container Adegan
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("🎬 ADEGAN 1", expanded=False):
    loc_1 = st.text_input("Lokasi", placeholder="Tempat adegan berlangsung...")
    act_1 = st.text_area("Aksi", placeholder="Deskripsikan tindakan karakter secara detail...")

with st.expander("🎬 ADEGAN 2", expanded=False):
    loc_2 = st.text_input("Lokasi ", placeholder="Tempat adegan berlangsung...")
    act_2 = st.text_area("Aksi ", placeholder="Deskripsikan tindakan karakter secara detail...")

# Action Button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("GENERATE MASTER PROMPT"):
    st.success("Prompt telah dikompilasi. Silakan cek hasil di bawah.")
    # Hasil Prompt detail di sini (seperti versi sebelumnya)
