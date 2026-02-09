import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="PINTAR MEDIA V2",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. KONFIGURASI MESIN AI (DETEKSI OTOMATIS JALUR STABIL)
API_KEY = "AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"

@st.cache_resource
def load_stable_model():
    try:
        genai.configure(api_key=API_KEY)
        # Mencari semua model yang aktif di akun kamu
        all_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # Cari yang paling canggih dulu, kalau tidak ada pakai yang paling stabil
        if 'models/gemini-1.5-flash' in all_models:
            target = 'models/gemini-1.5-flash'
        elif 'models/gemini-1.5-pro' in all_models:
            target = 'models/gemini-1.5-pro'
        else:
            target = 'models/gemini-pro'
            
        return genai.GenerativeModel(target)
    except Exception as e:
        return f"Error: {e}"

model_engine = load_stable_model()

# 3. CSS CUSTOM (Kembali ke Desain Mewah & Profesional)
st.markdown("""
    <style>
    header[data-testid="stHeader"] { background-color: #ff4b4b; color: white; }
    .block-container { padding: 1rem 1rem !important; }
    [data-testid="stSidebar"] { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3.5rem; 
        background-color: #ff4b4b; color: white; font-weight: bold; border: none;
    }
    .stTextArea textarea { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 4. SIDEBAR NAVIGATION (9 Menu Utuh Kembali!)
with st.sidebar:
    st.title("🎬 PINTAR MEDIA")
    st.write("User Status: **Authorized** ✅")
    st.divider()
    
    menu = st.radio(
        "NAVIGASI UTAMA:",
        [
            "🚀 PRODUCTION HUB",
            "🧠 AI LAB",
            "🎞️ SCHEDULE",
            "📋 TEAM TASK",
            "📈 TREND ANALYZER",
            "💡 IDEAS BANK",
            "👥 DATABASE LOCKER",
            "📊 MONITORING",
            "🛠️ COMMAND CENTER"
        ]
    )
    st.divider()
    st.caption("Version 2.0.5 • All Systems Normal")

# 5. LOGIKA HALAMAN

if menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    submenu = st.radio("Modul:", ["AI Scriptwriter", "Visual Prompter", "Copy Center"], horizontal=True)
    
    if submenu == "AI Scriptwriter":
        st.subheader("Content Generator (6 Adegan)")
        ide_konten = st.text_area("Topik atau Ide Konten:", placeholder="Masukkan ide di sini...")
        
        if st.button("GENERATE SCRIPT"):
            if isinstance(model_engine, str):
                st.error(f"Sistem gagal memuat model: {model_engine}")
            elif not ide_konten:
                st.warning("Silakan masukkan ide terlebih dahulu.")
            else:
                with st.spinner("Menghubungi AI..."):
                    try:
                        prompt = f"Buatkan naskah video pendek 6 adegan dari ide: {ide_konten}. Format: Adegan 1-6, Visual (English), Narasi (Indonesia)."
                        response = model_engine.generate_content(prompt)
                        st.divider()
                        st.markdown(response.text)
                        st.balloons()
                    except Exception as e:
                        st.error(f"Terjadi kendala teknis pada server Google: {e}")

elif menu == "🧠 AI LAB":
    st.header("🧠 AI Lab & Validator")
    st.info("Modul analisis referensi video sedang dalam sinkronisasi.")

elif menu == "📋 TEAM TASK":
    st.header("📋 Team Task Manager")
    st.info("Tugas Aktif: Editing Tahap 1")

elif menu == "🛠️ COMMAND CENTER":
    st.header("🛠️ System Control")
    if not isinstance(model_engine, str):
        st.success(f"Koneksi Aktif: {model_engine.model_name}")
    else:
        st.error("Sistem AI Offline")

else:
    st.header(menu)
    st.info("Modul ini sedang disiapkan.")
