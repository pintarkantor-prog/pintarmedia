import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="PINTAR MEDIA V2",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. KONEKSI MESIN GEMINI (Membaca dari Secrets)
try:
    genai.configure(api_key=st.secrets["AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ Koneksi API belum terdeteksi. Silakan periksa konfigurasi Secrets.")

# 3. CSS CUSTOM (Profesional & Responsive)
st.markdown("""
    <style>
    header[data-testid="stHeader"] { background-color: rgba(255, 75, 75, 0.9); color: white; }
    .block-container { padding: 1rem 1rem !important; }
    [data-testid="stSidebar"] { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; 
        border-radius: 10px; 
        height: 3.5rem; 
        background-color: #ff4b4b; 
        color: white; 
        font-weight: 600;
        border: none;
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
        ["🚀 PRODUCTION HUB", "🧠 AI LAB", "🎞️ SCHEDULE", "📋 TEAM TASK", "📈 TREND ANALYZER", "💡 IDEAS BANK", "👥 DATABASE LOCKER", "📊 MONITORING", "🛠️ COMMAND CENTER"]
    )
    st.divider()
    st.caption("Version 2.0.1")

# 5. LOGIKA HALAMAN

# --- MENU: PRODUCTION HUB ---
if menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    submenu = st.radio("Task:", ["Scriptwriter", "Visual Prompter", "Copy Center"], horizontal=True)
    
    if submenu == "Scriptwriter":
        st.subheader("AI Content Generator")
        ide = st.text_area("Topik atau Ide Konten:", placeholder="Contoh: Edukasi tentang manajemen keuangan untuk anak muda...")
        
        if st.button("GENERATE SCRIPT"):
            if ide:
                with st.spinner("Sedang memproses naskah..."):
                    try:
                        prompt = f"Buatkan naskah video pendek 6 adegan yang menarik dan potensial viral berdasarkan ide: {ide}. Sertakan visual deskripsi dan narasi untuk setiap adegan."
                        response = model.generate_content(prompt)
                        st.divider()
                        st.subheader("Hasil Naskah:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Gagal memproses permintaan: {e}")
            else:
                st.warning("Silakan masukkan ide konten terlebih dahulu.")

# --- MENU: AI LAB ---
elif menu == "🧠 AI LAB":
    st.header("🧠 AI Lab & Validator")
    st.write("Analisis referensi konten dan validasi naskah.")
    st.text_area("Masukkan link atau teks referensi:")
    st.button("Mulai Analisis")

# --- MENU: TEAM TASK ---
elif menu == "📋 TEAM TASK":
    st.header("📋 Team Task Manager")
    st.info("Task Active: Content Editing - Scene 1-3")
    st.success("Task Completed: Keyword Research")

# --- MENU: COMMAND CENTER ---
elif menu == "🛠️ COMMAND CENTER":
    st.header("🛠️ System Settings")
    st.write("Status API: **Connected**")
    st.selectbox("Model Engine:", ["Gemini 1.5 Flash", "Gemini 1.5 Pro"])

# --- MENU LAINNYA ---
else:
    st.header(menu)
    st.info("Modul ini sedang dalam tahap pengembangan.")
