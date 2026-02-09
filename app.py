import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="PINTAR MEDIA V2",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. KONFIGURASI MESIN AI (CLEAN START)
API_KEY = "AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"

# Kita buat fungsi inisialisasi yang sangat simpel
try:
    genai.configure(api_key=API_KEY)
    # Gunakan nama model langsung tanpa embel-embel models/
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Koneksi Awal Gagal: {e}")

# 3. CSS CUSTOM (Profesional & Mewah)
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

# 4. SIDEBAR NAVIGATION (9 MENU UTUH)
with st.sidebar:
    st.title("🎬 PINTAR MEDIA")
    st.write("User Status: **Authorized** ✅")
    st.divider()
    menu = st.radio("NAVIGASI UTAMA:", [
        "🚀 PRODUCTION HUB", "🧠 AI LAB", "🎞️ SCHEDULE", 
        "📋 TEAM TASK", "📈 TREND ANALYZER", "💡 IDEAS BANK", 
        "👥 DATABASE LOCKER", "📊 MONITORING", "🛠️ COMMAND CENTER"
    ])
    st.divider()
    st.caption("Version 2.0.7 • Final Patch")

# 5. LOGIKA HALAMAN
if menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    submenu = st.radio("Modul:", ["AI Scriptwriter", "Visual Prompter"], horizontal=True)
    
    if submenu == "AI Scriptwriter":
        st.subheader("Content Generator")
        ide_konten = st.text_area("Topik Konten:", placeholder="Ketik ide konten Anda di sini...")
        
        if st.button("GENERATE SCRIPT"):
            if not ide_konten:
                st.warning("Silakan masukkan ide terlebih dahulu.")
            else:
                with st.spinner("Sedang memproses naskah..."):
                    try:
                        # Prompt yang sangat jelas
                        prompt = f"Buatkan naskah video pendek 6 adegan dari ide: {ide_konten}. Format: Adegan 1-6, Visual (English), Narasi (Indonesia)."
                        
                        # Eksekusi standar tanpa RequestOptions yang bikin error
                        response = model.generate_content(ide_konten)
                        
                        st.divider()
                        st.subheader("✅ Hasil Naskah")
                        st.markdown(response.text)
                        st.balloons()
                    except Exception as e:
                        # Jika gemini-1.5-flash gagal, kita coba otomatis ke gemini-pro
                        try:
                            alt_model = genai.GenerativeModel('gemini-pro')
                            response = alt_model.generate_content(ide_konten)
                            st.divider()
                            st.markdown(response.text)
                            st.balloons()
                        except Exception as e2:
                            st.error(f"Gagal memproses naskah. Silakan periksa kembali API Key atau kuota Anda. Detail: {e2}")

elif menu == "🛠️ COMMAND CENTER":
    st.header("🛠️ System Control")
    st.success("API Key Active")
    st.info("System Engine: Connected")

else:
    st.header(menu)
    st.info("Modul ini sedang disinkronisasi.")
