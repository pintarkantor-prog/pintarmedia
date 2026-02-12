import streamlit as st
from datetime import datetime
import time

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Prompt Generator Pro", layout="wide")

# 2. Logika Penghitung Waktu Login (Sederhana)
if 'login_time' not in st.session_state:
    st.session_state.login_time = time.time()

def get_duration():
    duration = time.time() - st.session_state.login_time
    minutes = int(duration // 60)
    seconds = int(duration % 60)
    return f"{minutes}m {seconds}s"

# 3. Sidebar (Informasi Pengguna & Navigasi)
with st.sidebar:
    st.title("📂 Dashboard")
    st.markdown("---")
    st.subheader("Informasi Sesi")
    st.write(f"📅 **Tanggal:** {datetime.now().strftime('%d %B %Y')}")
    st.write(f"👤 **Status:** Terhubung")
    
    # Placeholder untuk penghitung waktu (akan update setiap refresh)
    st.write(f"⏱️ **Lama Sesi:** {get_duration()}")
    
    st.markdown("---")
    st.info("Gunakan sidebar ini nanti untuk riwayat prompt atau pengaturan lainnya.")

# 4. Custom CSS untuk Tampilan Mewah
st.markdown("""
    <style>
    .main .block-container { max-width: 900px; padding-top: 3rem; }
    .stTextInput input, .stTextArea textarea {
        border-radius: 15px !important;
    }
    .prompt-section {
        background-color: #f8f9fa;
        border-radius: 20px;
        padding: 25px;
        border-left: 5px solid #4285f4;
        margin-bottom: 20px;
    }
    .title-gradient {
        background: linear-gradient(to right, #4285f4, #9b72cb, #d96570);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 40px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 5. Halaman Utama
st.markdown('<h1 class="title-gradient">Prompt Generator Detail</h1>', unsafe_allow_html=True)
st.write("Buat prompt kompleks untuk teks, gambar, dan video dalam satu klik.")

# Input Form
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        topik = st.text_input("Topik Utama", placeholder="Contoh: Petualangan Udin di luar angkasa")
    with col2:
        mood = st.selectbox("Mood/Atmosfer", ["Cinematic", "Lucu", "Horror", "Futuristik", "Professional"])

    detail = st.text_area("Detail Tambahan (Opsional)", placeholder="Tambahkan konteks spesifik, karakter, atau alur...")

if st.button("Generate Master Prompt ✨"):
    if topik:
        # LOGIKA PEMBUATAN PROMPT SIGNIFIKAN
        
        # 1. Prompt Teks (Konteks Dalam)
        text_prompt = f"""Tolong buatkan narasi mendalam tentang {topik}. 
Gunakan gaya {mood}. Detail tambahan: {detail}. 
Struktur cerita harus memiliki pembukaan yang kuat, konflik yang terasa nyata, dan penutup yang berkesan."""

        # 2. Prompt Gambar (Visual Detail)
        image_prompt = f"Hyper-realistic photo of {topik}, {mood} lighting, 8k resolution, highly detailed texture, shot on 35mm lens, masterpiece, --ar 16:9"

        # 3. Prompt Video (Movement & Scene)
        video_prompt = f"Cinematic drone shot moving towards {topik}, {mood} atmosphere, volumetric lighting, high frame rate, smooth motion, professional color grading."

        # Menampilkan Hasil
        st.markdown("---")
        
        st.markdown('<div class="prompt-section">', unsafe_allow_html=True)
        st.subheader("📝 Prompt Teks (Untuk Gemini)")
        st.code(text_prompt, language="text")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="prompt-section" style="border-left-color: #34a853;">', unsafe_allow_html=True)
        st.subheader("🖼️ Prompt Gambar (Midjourney/DALL-E)")
        st.code(image_prompt, language="text")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="prompt-section" style="border-left-color: #fabb05;">', unsafe_allow_html=True)
        st.subheader("🎬 Prompt Video (Runway/Sora)")
        st.code(video_prompt, language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.success("Prompt berhasil dibuat! Silakan salin ke platform yang sesuai.")
    else:
        st.warning("Masukkan topik terlebih dahulu!")

# Footer tipis
st.markdown("<br><hr><center><small>Copy-paste hasil ke Gemini untuk eksekusi</small></center>", unsafe_allow_html=True)
