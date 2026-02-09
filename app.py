import streamlit as st

# 1. KONFIGURASI HALAMAN (Standard Mewah)
st.set_page_config(
    page_title="PINTAR MEDIA V2",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS SAKTI (Fixed Header, Responsive Padding, & Box Staf)
st.markdown("""
    <style>
    /* Fixed Header agar judul tidak hilang saat scroll */
    header[data-testid="stHeader"] {
        background-color: rgba(255, 75, 75, 0.9);
        color: white;
    }
    
    /* Padding agar tidak nempel ke pinggir layar HP */
    .block-container {
        padding: 1rem 1rem !important;
    }

    /* Styling Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0e1117;
    }

    /* Desain Box Staf / Task agar rapi di HP */
    .st-emotion-cache-1r6slb0 {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        background-color: white;
    }

    /* Tombol Lebar untuk Jempol HP */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5rem;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION (9 Menu Utama Sultan)
with st.sidebar:
    st.title("🎬 PINTAR MEDIA")
    st.write(f"User: **Sultan Prompt** 🛡️")
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
    st.info("Status: Mesin Siap 🟢")

# 4. LOGIKA HALAMAN (Apa yang muncul saat menu diklik)

if menu == "🚀 PRODUCTION HUB":
    st.header("🚀 Production Hub")
    # Sub-menu menggunakan segmented control agar hemat ruang
    submenu = st.radio("Pilih Task:", ["AI Scriptwriter", "Visual Prompter", "Copy-All"], horizontal=True)
    
    if submenu == "AI Scriptwriter":
        st.subheader("Mesin Pembuat 6 Adegan")
        ide = st.text_area("Apa ide hari ini?", placeholder="Misal: Kisah sukses Sultan...")
        if st.button("MULAI GENERATE"):
            st.write("Sedang meracik naskah... (Langkah berikutnya kita sambung ke Gemini)")

elif menu == "🧠 AI LAB":
    st.header("🧠 AI Lab & Validator")
    st.write("Tempat riset video viral dan simulasi netizen.")
    st.text_area("Tempel Link/Transkrip:")
    st.button("Analisis Sekarang")

elif menu == "📋 TEAM TASK":
    st.header("📋 Team Task Manager")
    # Contoh Box Staf yang rapi
    with st.container():
        st.markdown("### 👷 Status Tim")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**Editor 1:** Editing Scene 1")
        with col2:
            st.success("**Admin:** Siap Upload")

elif menu == "🛠️ COMMAND CENTER":
    st.header("🛠️ Pusat Kendali")
    st.text_input("Gemini API Key:", type="password")
    st.button("Simpan Konfigurasi")

else:
    # Untuk menu lainnya yang belum diisi detailnya
    st.header(menu)
    st.info("Fitur ini sedang dalam perjalanan menuju 'Rumah Baru' Sultan.")
    
