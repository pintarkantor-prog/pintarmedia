import streamlit as st
from datetime import datetime
import time

# --- CONFIG & SESSION ---
st.set_page_config(page_title="Prompt Master Pro", layout="wide")

if 'login_time' not in st.session_state:
    st.session_state.login_time = datetime.now()

# --- CSS UNTUK TAMPILAN PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    /* Style Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f0f2f6;
        border-right: 1px solid #e0e0e0;
        padding: 20px;
    }

    /* Card Styling */
    .prompt-card {
        background: white;
        border: 1px solid #e6e9ef;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        margin-bottom: 20px;
    }

    /* Gradient Title */
    .header-text {
        font-size: 2.5rem;
        font-weight: 600;
        background: linear-gradient(90deg, #1A73E8, #9B72CB);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Badge Login */
    .login-info {
        background: #e8f0fe;
        color: #1967d2;
        padding: 10px;
        border-radius: 10px;
        font-size: 0.8rem;
        border-left: 4px solid #1A73E8;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR LOGIC ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=50)
    st.markdown("### **User Dashboard**")
    
    # Info Waktu Login
    current_time = datetime.now()
    duration = current_time - st.session_state.login_time
    minutes = int(duration.total_seconds() // 60)
    
    st.markdown(f"""
    <div class="login-info">
        <b>Sesi Aktif</b><br>
        📅 {st.session_state.login_time.strftime('%d %b %Y')}<br>
        ⏰ Masuk: {st.session_state.login_time.strftime('%H:%M')}<br>
        ⏳ Durasi: {minutes} menit
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    menu = st.radio("Navigasi", ["Generator Utama", "Riwayat Prompt", "Pengaturan"])

# --- HALAMAN UTAMA ---
if menu == "Generator Utama":
    st.markdown('<h1 class="header-text">AI Command Center</h1>', unsafe_allow_html=True)
    st.write("Rancang instruksi detail untuk ekosistem AI milikmu.")

    # Input Section
    with st.container():
        col_main, col_opt = st.columns([2, 1])
        
        with col_main:
            topik = st.text_input("Topik Cerita/Konten", placeholder="Misal: Udin menemukan mesin waktu di dapur")
            karakter = st.text_area("Deskripsi Karakter & Properti", placeholder="Contoh: Udin (pria kepala oranye), Tung (pria kepala kayu), suasana dapur berantakan.")
        
        with col_opt:
            gaya = st.selectbox("Style Artistik", ["Disney Pixar Style", "Cyberpunk 2077", "Studio Ghibli", "Cinematic Realistic", "Penciler/Sketch"])
            rasio = st.selectbox("Aspek Rasio", ["16:9 (YouTube)", "9:16 (Shorts/TikTok)", "1:1 (Instagram)"])

    if st.button("Generate Comprehensive Suite ✨", use_container_width=True):
        if topik and karakter:
            st.markdown("---")
            
            # --- LOGIKA GENERATOR PROMPT DETAIL ---
            
            # 1. TEXT PROMPT (Gemini)
            text_final = f"Buatkan naskah film pendek tentang '{topik}'. Karakter: {karakter}. Gaya penceritaan: {gaya}. Fokus pada dialog yang natural tapi berkesan, sertakan instruksi emosi karakter di setiap baris."
            
            # 2. IMAGE PROMPT (Midjourney/DALL-E)
            image_final = f"Extreme close-up shot of {karakter} in the middle of {topik}, {gaya}, masterwork, ultra-detailed, depth of field, global illumination, ray tracing, 8k, --ar {rasio.split(' ')[0]}"
            
            # 3. VIDEO PROMPT (Veo/Runway/Luma)
            video_final = f"Cinematic tracking shot, {karakter} is performing action: {topik}. Lighting: {gaya} atmosphere. Camera movement: slow zoom in. High fidelity, fluid motion, 60fps, realistic physics."

            # Tampilan Output dengan Kolom/Cards
            c1, c2, c3 = st.columns(3)
            
            with c1:
                st.markdown("### 📝 Text Prompt")
                st.info(text_final)
                st.button("Copy Text", key="btn_text", on_click=lambda: st.write("Tersalin ke Clipboard (Simulasi)"))
            
            with c2:
                st.markdown("### 🖼️ Image Prompt")
                st.success(image_final)
                st.button("Copy Image Prompt", key="btn_img")

            with c3:
                st.markdown("### 🎬 Video Prompt")
                st.warning(video_final)
                st.button("Copy Video Prompt", key="btn_vid")
            
            st.markdown("---")
            st.caption("Gunakan prompt di atas sesuai dengan platform AI masing-masing.")
        else:
            st.error("Mohon isi topik dan deskripsi karakter agar hasil maksimal.")

else:
    st.info("Halaman ini sedang dalam pengembangan.")

# Auto-refresh sederhana untuk timer
time.sleep(1)
if st.sidebar.button("Update Timer"):
    st.rerun()
