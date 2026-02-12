import streamlit as st
from datetime import datetime
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Aura Prompt Lab", layout="wide", initial_sidebar_state="expanded")

# --- LOGIKA SESI ---
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()

# --- CUSTOM CSS (THE ELEGANCE LAYER) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        color: #2D3436;
    }

    /* Background Utama */
    .stApp {
        background: radial-gradient(circle at top right, #f8faff, #ffffff);
    }

    /* Sidebar Refinement */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.6) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(0,0,0,0.05);
    }

    /* Container Hasil Prompt */
    .prompt-card {
        background: #ffffff;
        border-radius: 24px;
        padding: 30px;
        border: 1px solid #f1f3f5;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        margin-top: 20px;
    }

    /* Judul Elegan */
    .main-title {
        font-size: 3.5rem;
        font-weight: 600;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    /* Sidebar Info */
    .user-info-box {
        padding: 1.5rem;
        background: #1e293b;
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
    }

    /* Input Styling */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #f8fafd !important;
        border-radius: 16px !important;
        border: 1px solid #e2e8f0 !important;
        padding: 15px !important;
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent !important;
        border: none !important;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="user-info-box">
        <p style="opacity: 0.8; margin-bottom: 5px; font-size: 0.8rem;">SESI AKTIF</p>
        <h4 style="margin: 0;">Pintar Media</h4>
        <p style="font-size: 0.85rem; margin-top: 10px;">
            📅 {st.session_state.start_time.strftime('%d %B %Y')}<br>
            🕒 Masuk: {st.session_state.start_time.strftime('%H:%M')}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Penghitung waktu login sederhana
    duration = datetime.now() - st.session_state.start_time
    st.write(f"⏱️ **Lama Bekerja:** {duration.seconds // 60} menit")
    
    st.markdown("---")
    st.markdown("### Navigasi")
    st.caption("Eksplorasi Ide & Produksi")

# --- HALAMAN UTAMA ---
st.markdown('<h1 class="main-title">Aura Generator</h1>', unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.2rem; color: #64748b;'>Rancang instruksi visual dan naratif yang mendalam secara instan.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Area Input
with st.container():
    topik = st.text_input("Fokus Utama Ide", placeholder="Contoh: Pertemuan Udin dan Tung di dimensi kayu")
    detail_konteks = st.text_area("Detail Visual & Karakter", placeholder="Gambarkan suasana, emosi, dan detail fisik karakter secara spesifik...")

if st.button("Generate Master Suite", use_container_width=True):
    if topik:
        st.markdown("---")
        
        # PROMPT ENGINEERING YANG SIGNIFIKAN
        tab1, tab2, tab3 = st.tabs(["📄 Narasi Teks", "🖼️ Visual Gambar", "🎬 Produksi Video"])
        
        with tab1:
            st.markdown('<div class="prompt-card">', unsafe_allow_html=True)
            text_p = f"""[Identity: Expert Storyteller]
Tolong buatkan skrip mendalam dengan fokus pada: {topik}.
Konteks: {detail_konteks}.
Gunakan struktur narasi tiga babak. Sertakan instruksi blocking kamera dan nada bicara untuk karakter Udin dan Tung agar terasa hidup."""
            st.code(text_p, language="markdown")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab2:
            st.markdown('<div class="prompt-card">', unsafe_allow_html=True)
            img_p = f"Cinematic wide shot, {topik}, {detail_konteks}, hyper-realistic, photorealistic, shot on ARRI Alexa, 85mm lens, f/1.8, cinematic lighting, volumetric fog, unreal engine 5 render, highly detailed, 8k, --ar 16:9 --v 6.0"
            st.code(img_p, language="text")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab3:
            st.markdown('<div class="prompt-card">', unsafe_allow_html=True)
            vid_p = f"Camera move: Slow drone orbit around {topik}. Lighting transitions from golden hour to dusk. Character {detail_konteks} moving in slow motion. High dynamic range, fluid motion, professional color grade, 4k 60fps."
            st.code(vid_p, language="text")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Silakan masukkan topik untuk memulai.")

# Footer
st.markdown("<br><p style='text-align: center; color: #cbd5e1;'>Aura Generator | Powered by Gemini Context</p>", unsafe_allow_html=True)
