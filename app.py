import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="PINTAR MEDIA V2",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. KONFIGURASI MESIN AI (Langsung Menggunakan Key Anda)
API_KEY = "AIzaSyAg9Qpq3HT1UffcvScDvd3C55GX-kJfQwg"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Koneksi AI Terkendala: {e}")

# 3. CSS CUSTOM (Profesional, Clean, & Responsive HP)
st.markdown("""
    <style>
    /* Header Background */
    header[data-testid="stHeader"] {
        background-color: #ff4b4b;
    }
    
    /* Padding utama agar rapi di HP */
    .block-container {
        padding: 1rem 1rem !important;
    }

    /* Styling Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0e1117;
    }

    /* Tombol Utama (Generate) */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.5rem;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border: none;
    }

    /* Input Box */
    .stTextArea textarea {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. SIDEBAR NAVIGATION (9 Menu Utama)
with st.sidebar:
    st.title("🎬 PINTAR MEDIA")
    st.write("Status: **System Authorized** ✅")
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
    st.caption("Version 2.0.2 • Stable")

# 5. LOGIKA MENU UTAMA

# --- MENU: PRODUCTION HUB ---
if menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    
    # Sub-menu profesional
    submenu = st.radio("Pilih Modul:", ["AI Scriptwriter", "Visual Prompter", "Copy-All Center"], horizontal=True)
    
    if submenu == "AI Scriptwriter":
        st.subheader("Content Generator (6 Adegan)")
        
        # Input Ide Konten
        ide_konten = st.text_area(
            "Masukkan Topik atau Ide Konten:", 
            placeholder="Contoh: Tips mengelola waktu untuk kreator pemula...",
            height=150
        )
        
        if st.button("GENERATE SCRIPT"):
            if ide_konten:
                with st.spinner("Sedang memproses naskah terbaik..."):
                    try:
                        # Prompt Instruksi untuk Gemini
                        prompt = f"""
                        Buatkan naskah video pendek (TikTok/Reels/Shorts) 6 adegan berdasarkan ide: {ide_konten}.
                        Format harus jelas:
                        - Adegan 1-6
                        - Visual: Deskripsi visual (dalam Bahasa Inggris untuk AI Image generator)
                        - Narasi: Teks suara (Bahasa Indonesia profesional & menarik)
                        Pastikan pembukaan (Adegan 1) memiliki HOOK yang kuat.
                        """
                        
                        response = model.generate_content(prompt)
                        
                        st.divider()
                        st.subheader("✅ Hasil Naskah")
                        st.markdown(response.text)
                        st.balloons() # Perayaan sukses
                        
                    except Exception as e:
                        st.error(f"Gagal memproses naskah. Pastikan kuota API tersedia. Error: {e}")
            else:
                st.warning("Silakan masukkan ide konten terlebih dahulu.")

# --- MENU: AI LAB ---
elif menu == "🧠 AI LAB":
    st.header("🧠 AI Lab & Validator")
    st.write("Modul analisis referensi video dan validasi konten.")
    st.text_area("Tempel link atau transkrip video referensi:")
    st.button("Mulai Analisis")

# --- MENU: TEAM TASK ---
elif menu == "📋 TEAM TASK":
    st.header("📋 Team Task Manager")
    st.info("Tugas Aktif: Editing Tahap 1 (Scene 1-3)")
    st.success("Tugas Selesai: Riset Keyword & Judul")

# --- MENU: COMMAND CENTER ---
elif menu == "🛠️ COMMAND CENTER":
    st.header("🛠️ System Control")
    st.write("Koneksi Engine: **Connected** ✅")
    st.write(f"Model: **Gemini 1.5 Flash**")
    st.divider()
    st.button("Check System Update")

# --- MENU LAINNYA (Placeholder) ---
else:
    st.header(menu)
    st.info("Modul ini sedang disiapkan untuk rilis berikutnya.")
