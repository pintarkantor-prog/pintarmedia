import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="PINTAR MEDIA V2",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. KONEKSI & DETEKSI MODEL OTOMATIS
API_KEY = "AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"

@st.cache_resource
def get_working_model():
    try:
        genai.configure(api_key=API_KEY)
        # Mencari semua model yang mendukung generateContent di akun Sultan
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                # Kita pilih yang paling baru/stabil yang ketemu pertama kali
                return genai.GenerativeModel(m.name)
    except Exception as e:
        return None

model = get_working_model()

# 3. CSS CUSTOM (Profesional & Anti-Penyok)
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

# 4. SIDEBAR NAVIGATION (9 MENU LENGKAP)
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
    st.caption("Version 2.0.8 • Auto-Detector")

# 5. LOGIKA PRODUCTION HUB
if menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    submenu = st.radio("Modul:", ["AI Scriptwriter", "Visual Prompter"], horizontal=True)
    
    if submenu == "AI Scriptwriter":
        st.subheader("Content Generator")
        ide_konten = st.text_area("Topik Konten:", placeholder="Ketik ide konten di sini...")
        
        if st.button("GENERATE SCRIPT"):
            if not model:
                st.error("Gagal mendeteksi model AI. Periksa API Key Anda di Google AI Studio.")
            elif not ide_konten:
                st.warning("Silakan masukkan ide terlebih dahulu.")
            else:
                with st.spinner("Sistem sedang mencari jalur AI yang tersedia..."):
                    try:
                        prompt = f"Buatkan naskah video pendek viral 6 adegan dari ide: {ide_konten}. Format: Adegan 1-6, Visual (English), Narasi (Indonesia)."
                        response = model.generate_content(prompt)
                        st.divider()
                        st.subheader("✅ Hasil Naskah")
                        st.markdown(response.text)
                        st.balloons()
                    except Exception as e:
                        st.error(f"Upaya gagal. Google API merespons: {e}")

elif menu == "🛠️ COMMAND CENTER":
    st.header("🛠️ System Control")
    if model:
        st.success(f"Model Aktif: {model.model_name}")
    else:
        st.error("Mesin AI Offline")

else:
    st.header(menu)
    st.info("Fitur ini sedang dalam proses sinkronisasi.")
