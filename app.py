import streamlit as st
from datetime import datetime
import time

# --- CONFIG HALAMAN ---
st.set_page_config(page_title="Storyboard AI Generator", layout="wide")

# --- SESSION STATE UNTUK TIMER ---
if 'login_time' not in st.session_state:
    st.session_state.login_time = datetime.now()

# --- CUSTOM CSS (DARK MODE PREMIUM) ---
st.markdown("""
    <style>
    /* Mengatur Tema Dark Background */
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }

    /* Styling Expander (Adegan) */
    .streamlit-expanderHeader {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        color: #f0f6fc !important;
    }

    /* Input Fields Customization */
    div[data-baseweb="input"] {
        background-color: #0d1117 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }
    
    textarea {
        background-color: #0d1117 !important;
        color: #c9d1d9 !important;
    }

    /* Sidebar User Box */
    .user-card {
        background: #1f2937;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #374151;
        margin-bottom: 20px;
    }

    /* Custom Header Gradient */
    .header-style {
        font-size: 24px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR LOGIC ---
with st.sidebar:
    st.markdown("### 🛠️ Workspace")
    
    # Info Login & Timer
    uptime = datetime.now() - st.session_state.login_time
    st.markdown(f"""
    <div class="user-card">
        <small style='color: #9ca3af;'>USER SESSION</small><br>
        <b>Pintar Media</b><br><br>
        <small style='color: #9ca3af;'>📅 TANGGAL</small><br>
        {st.session_state.login_time.strftime('%d %b %Y')}<br><br>
        <small style='color: #9ca3af;'>⏱️ DURASI AKTIF</small><br>
        {uptime.seconds // 60} Menit {uptime.seconds % 60} Detik
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    menu = st.radio("Menu Utama", ["🎬 Detail Storyboard", "📜 Arsip Project", "⚙️ Settings"])

# --- KONTEN UTAMA ---
if menu == "🎬 Detail Storyboard":
    st.markdown('<div class="header-style">📝 Detail Adegan Storyboard</div>', unsafe_allow_html=True)

    # SEKSI KARAKTER (Mirip Gambar Upload-an)
    with st.expander("👥 Nama Karakter Utama & Penampilan Fisik! (WAJIB ISI)", expanded=True):
        st.write("Total Karakter Utama dalam Project")
        num_chars = st.number_input("", min_value=1, max_value=5, value=2, step=1, label_visibility="collapsed")
        
        cols = st.columns(num_chars)
        char_data = {}
        
        for i in range(num_chars):
            with cols[i]:
                st.markdown(f"👤 **Karakter Utama {i+1}**")
                name = st.text_input(f"Nama Karakter {i+1}", placeholder=f"Nama Karakter Utama {i+1}", label_visibility="collapsed")
                desc = st.text_area(f"Ciri fisik {i+1}", placeholder=f"Ciri fisik Karakter Utama {i+1}...", label_visibility="collapsed", height=100)
                char_data[f"char_{i+1}"] = {"nama": name, "ciri": desc}

    # SEKSI ADEGAN
    with st.expander("🟢 ADEGAN 1"):
        loc_1 = st.text_input("Lokasi / Latar Tempat", placeholder="Contoh: Dapur tua yang gelap")
        act_1 = st.text_area("Aksi/Kejadian", placeholder="Apa yang terjadi di adegan ini?")

    with st.expander("🎬 ADEGAN 2"):
        loc_2 = st.text_input("Lokasi / Latar Tempat ", placeholder="Contoh: Hutan pinus berkabut")
        act_2 = st.text_area("Aksi/Kejadian ", placeholder="Detail aksi karakter...")

    # BUTTON GENERATE
    if st.button("Generate Master Prompt ✨", use_container_width=True):
        st.divider()
        st.subheader("🚀 Hasil Prompt Signifikan")
        
        # Contoh Output Gabungan yang Detail
        full_context = f"Karakter: {char_data['char_1']['nama']} ({char_data['char_1']['ciri']}) dan {char_data['char_2']['nama']} ({char_data['char_2']['ciri']})."
        
        tab_t, tab_i, tab_v = st.tabs(["Teks (Naskah)", "Gambar (Visual)", "Video (Motion)"])
        
        with tab_t:
            st.code(f"Buatkan naskah detail untuk adegan di {loc_1}. {full_context}. Kejadian: {act_1}. Gunakan gaya penceritaan yang emosional.", language="text")
        
        with tab_i:
            st.code(f"Cinematic shot, {loc_1}, {full_context}, hyper-realistic, 8k, --ar 16:9", language="text")
            
        with tab_v:
            st.code(f"Camera movement: Slow zoom into {char_data['char_1']['nama']}. Scene: {act_1}. Realistic lighting, 4k 60fps.", language="text")

else:
    st.write("Halaman dalam pengembangan.")
