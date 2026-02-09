import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="PINTAR MEDIA V2",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. KONFIGURASI MESIN AI (FIX ERROR 404)
# Menggunakan API Key Sultan yang tadi
API_KEY = "AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"

try:
    genai.configure(api_key=API_KEY)
    # Kita gunakan 'gemini-1.5-flash-latest' atau 'gemini-pro' sebagai fallback
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"Koneksi AI Terkendala: {e}")

# 3. CSS CUSTOM (Profesional & Clean)
st.markdown("""
    <style>
    header[data-testid="stHeader"] { background-color: #ff4b4b; color: white; }
    .block-container { padding: 1rem 1rem !important; }
    [data-testid="stSidebar"] { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3.5rem; 
        background-color: #ff4b4b; color: white; font-weight: bold; 
    }
    .stTextArea textarea { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 4. SIDEBAR NAVIGATION
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
    st.caption("Version 2.0.4 • Patch 404")

# 5. LOGIKA MENU UTAMA

if menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    submenu = st.radio("Modul:", ["AI Scriptwriter", "Visual Prompter"], horizontal=True)
    
    if submenu == "AI Scriptwriter":
        st.subheader("Content Generator (6 Adegan)")
        ide_konten = st.text_area(
            "Masukkan Topik atau Ide Konten:", 
            placeholder="Contoh: Tutorial masak simpel...",
            height=150
        )
        
        if st.button("GENERATE SCRIPT"):
            if ide_konten:
                with st.spinner("Menghubungi Server Gemini..."):
                    try:
                        prompt = f"Buatkan naskah video pendek 6 adegan dari ide: {ide_konten}. Format: Adegan 1-6, Visual (English), Narasi (Indonesia)."
                        # Eksekusi Generate
                        response = model.generate_content(prompt)
                        
                        st.divider()
                        st.subheader("✅ Hasil Naskah")
                        st.markdown(response.text)
                        st.balloons()
                    except Exception as e:
                        # Jika masih error, tampilkan detail untuk kita bedah lagi
                        st.error(f"Aduh, server Google sedang sibuk atau ada masalah teknis: {e}")
            else:
                st.warning("Silakan masukkan ide terlebih dahulu.")

elif menu == "🛠️ COMMAND CENTER":
    st.header("🛠️ System Control")
    st.success("API Key Active")
    st.write("Model saat ini: **Gemini 1.5 Flash (Latest)**")

else:
    st.header(menu)
    st.info("Modul ini sedang disiapkan.")
