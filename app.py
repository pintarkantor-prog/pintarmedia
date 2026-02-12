import streamlit as st

# 1. Konfigurasi Halaman & Sembunyikan Sidebar Secara Paksa
st.set_page_config(page_title="Gemini Style Generator", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS Magic untuk meniru Interface Gemini
st.markdown("""
    <style>
    /* Sembunyikan Sidebar dan Tombol Menu */
    [data-testid="stSidebar"], .st-emotion-cache-16ids0d, .st-emotion-cache-10o10d2 {
        display: none;
    }
    
    /* Atur Background Utama */
    .stApp {
        background-color: #ffffff;
    }

    /* Pusatkan konten di tengah layar */
    .main .block-container {
        max-width: 800px;
        margin: auto;
        padding-top: 10% !important;
    }

    /* Gradasi Judul Khas Gemini */
    .gemini-title {
        font-size: 44px;
        font-weight: 600;
        background: linear-gradient(to right, #4285f4, #9b72cb, #d96570);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    .sub-title {
        color: #5f6368;
        font-size: 24px;
        margin-bottom: 40px;
    }

    /* Styling Kotak Input agar mirip Chat Box */
    .stTextInput input {
        border-radius: 28px !important;
        padding: 15px 25px !important;
        border: 1px solid #dfe1e5 !important;
        background-color: #f8f9fa !important;
        font-size: 16px !important;
    }

    /* Hasil Prompt dalam Kotak yang Bersih */
    .result-container {
        background-color: #f0f4f9;
        border-radius: 24px;
        padding: 25px;
        margin-top: 30px;
        border: none;
        color: #1f1f1f;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Konten Utama
st.markdown('<h1 class="gemini-title">Halo, Kreator</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Apa yang ingin kita buat hari ini?</p>', unsafe_allow_html=True)

# Input Utama (Seperti Chat Box Gemini)
user_input = st.text_input("", placeholder="Masukkan ide atau topik di sini...", key="main_input")

if user_input:
    # Logika Template Prompt (Bisa kamu kembangkan sendiri)
    final_prompt = f"Buatkan skrip detail tentang {user_input}. Pastikan karakter seperti Udin dan Tung mendapatkan dialog yang lucu dan unik."
    
    st.markdown('<div class="result-container">', unsafe_allow_html=True)
    st.markdown("### ✨ Hasil Prompt:")
    st.code(final_prompt, language="text")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.caption("Salin teks di atas dan tempelkan ke kolom chat Gemini.")
