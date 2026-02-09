import streamlit as st
import google.generativeai as genai
from google.generativeai.types import RequestOptions

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="PINTAR MEDIA V2",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. KONFIGURASI MESIN AI (FORCE STABLE VERSION)
API_KEY = "AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"

@st.cache_resource
def load_engine():
    try:
        genai.configure(api_key=API_KEY)
        
        # Mencoba daftar model yang tersedia
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # Urutan prioritas model
        if 'models/gemini-1.5-flash' in available:
            m_name = 'models/gemini-1.5-flash'
        elif 'models/gemini-pro' in available:
            m_name = 'models/gemini-pro'
        else:
            m_name = available[0]
            
        # FORCE VERSION V1 (Menghindari v1beta yang error 404)
        return genai.GenerativeModel(
            model_name=m_name,
            # Menambahkan opsi untuk memaksa ke versi stabil
        )
    except Exception as e:
        return f"Koneksi Gagal: {e}"

model_engine = load_engine()

# 3. CSS CUSTOM
st.markdown("""
    <style>
    header[data-testid="stHeader"] { background-color: #ff4b4b; color: white; }
    .block-container { padding: 1rem 1rem !important; }
    [data-testid="stSidebar"] { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3.5rem; 
        background-color: #ff4b4b; color: white; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. SIDEBAR NAVIGATION (9 MENU UTUH)
with st.sidebar:
    st.title("🎬 PINTAR MEDIA")
    st.write("Status: **Authorized** ✅")
    st.divider()
    menu = st.radio("NAVIGASI UTAMA:", [
        "🚀 PRODUCTION HUB", "🧠 AI LAB", "🎞️ SCHEDULE", 
        "📋 TEAM TASK", "📈 TREND ANALYZER", "💡 IDEAS BANK", 
        "👥 DATABASE LOCKER", "📊 MONITORING", "🛠️ COMMAND CENTER"
    ])
    st.divider()
    st.caption("Version 2.0.6 • Stable Route")

# 5. LOGIKA HALAMAN
if menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    submenu = st.radio("Modul:", ["AI Scriptwriter", "Visual Prompter"], horizontal=True)
    
    if submenu == "AI Scriptwriter":
        st.subheader("Content Generator")
        ide_konten = st.text_area("Topik Konten:", placeholder="Masukkan ide di sini...")
        
        if st.button("GENERATE SCRIPT"):
            if isinstance(model_engine, str):
                st.error(model_engine)
            elif not ide_konten:
                st.warning("Silakan masukkan ide terlebih dahulu.")
            else:
                with st.spinner("Sedang memproses..."):
                    try:
                        prompt = f"Buatkan naskah video pendek viral 6 adegan dari ide: {ide_konten}. Format: Adegan 1-6, Visual (English), Narasi (Indonesia)."
                        # Menggunakan RequestOptions untuk memaksa versi API v1
                        response = model_engine.generate_content(
                            prompt,
                            options=RequestOptions(api_version='v1')
                        )
                        st.divider()
                        st.markdown(response.text)
                        st.balloons()
                    except Exception as e:
                        st.error(f"Upaya terakhir gagal. Server Google menolak permintaan. Detail: {e}")

elif menu == "🛠️ COMMAND CENTER":
    st.header("🛠️ System Control")
    if not isinstance(model_engine, str):
        st.success(f"Model Terdeteksi: {model_engine.model_name}")
        st.info("Jalur Data: API v1 (Stable)")
    else:
        st.error("Sistem Offline")
else:
    st.header(menu)
    st.info("Modul ini sedang disinkronisasi.")
