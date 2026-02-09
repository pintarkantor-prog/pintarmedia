import streamlit as st
import google.generativeai as genai
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="PINTAR MEDIA V2",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. KONFIGURASI MESIN AI (FIX 404 - STABLE VERSION)
API_KEY = "AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"

try:
    # Menginisialisasi library dengan konfigurasi terbaru
    genai.configure(api_key=API_KEY)
    
    # Kita gunakan 'gemini-1.5-flash' tanpa tambahan 'latest' atau 'beta'
    # Ini adalah jalur paling stabil untuk produksi sekarang
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    
except Exception as e:
    st.error(f"Koneksi AI Terkendala: {e}")

# 3. CSS CUSTOM (Profesional)
st.markdown("""
    <style>
    header[data-testid="stHeader"] { background-color: #ff4b4b; color: white; }
    .block-container { padding: 1rem 1rem !important; }
    [data-testid="stSidebar"] { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3.5rem; 
        background-color: #ff4b4b; color: white; font-weight: bold; 
    }
    </style>
    """, unsafe_allow_html=True)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.title("🎬 PINTAR MEDIA")
    st.write("Status: **System Authorized** ✅")
    st.divider()
    menu = st.radio("NAVIGASI UTAMA:", ["🚀 PRODUCTION HUB", "🧠 AI LAB", "📋 TEAM TASK", "🛠️ COMMAND CENTER"])

# 5. LOGIKA PRODUCTION HUB
if menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    submenu = st.radio("Modul:", ["AI Scriptwriter", "Visual Prompter"], horizontal=True)
    
    if submenu == "AI Scriptwriter":
        st.subheader("Content Generator (6 Adegan)")
        ide_konten = st.text_area("Topik atau Ide Konten:", placeholder="Masukkan ide di sini...")
        
        if st.button("GENERATE SCRIPT"):
            if ide_konten:
                with st.spinner("Sedang menghubungi otak AI..."):
                    try:
                        # Prompt Instruksi
                        prompt = f"Buatkan naskah video pendek viral 6 adegan dari ide: {ide_konten}. Format: Adegan 1-6, Visual (English), Narasi (Indonesia)."
                        
                        # Eksekusi dengan penanganan error yang lebih spesifik
                        response = model.generate_content(prompt)
                        
                        st.divider()
                        st.subheader("✅ Hasil Naskah")
                        st.markdown(response.text)
                        st.balloons()
                    except Exception as e:
                        # Jika masih gagal, kita akan tampilkan saran spesifik
                        st.error(f"Maaf, terjadi kendala teknis. Silakan coba klik tombol sekali lagi. Detail: {e}")
            else:
                st.warning("Silakan masukkan ide terlebih dahulu.")

elif menu == "🛠️ COMMAND CENTER":
    st.header("🛠️ System Control")
    st.success("API Key Active")
    st.write("Model: **Gemini 1.5 Flash (Production Mode)**")

else:
    st.header(menu)
    st.info("Fitur ini sedang dalam pengembangan.")
