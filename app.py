import streamlit as st

def halaman_kocak_interogasi():
    st.set_page_config(
        page_title="Pintar Digital | OY KERJA!",
        page_icon="👮",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: CLEAN, NO LINES, CENTER LOCK ---
    st.markdown("""
        <style>
        /* Hapus elemen sampah Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        .main {
            background-color: #050505 !important;
            height: 100vh !important;
            overflow: hidden !important;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* --- BENDERA & ROKET PATROLI --- */
        .round-flag {
            position: absolute;
            width: 60px; height: 60px;
            border-radius: 50%;
            object-fit: cover;
            z-index: 1;
            filter: grayscale(80%) blur(1px); /* Efek dramatis */
            animation: patrol 20s infinite linear;
        }

        @keyframes patrol {
            0% { transform: translate(0,0) rotate(0deg); }
            50% { transform: translate(80vw, 50vh) rotate(180deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }

        /* --- KOTAK INTEROGASI (CENTER) --- */
        .interrogation-box {
            position: fixed;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            z-index: 9999;
            text-align: center;
            background: rgba(20, 20, 20, 0.95);
            padding: 40px;
            border-radius: 20px;
            border: 2px solid #ff4b2b;
            box-shadow: 0 0 50px rgba(255, 75, 43, 0.4);
            width: 350px;
        }

        .warn-text {
            color: #ff4b2b;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 20px;
            text-transform: uppercase;
        }

        /* --- TOMBOL KECIL RGB --- */
        .btn-wrapper {
            background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
            background-size: 400%;
            animation: rainbow_move 10s linear infinite;
            padding: 3px;
            border-radius: 50px;
            display: inline-block;
            margin-top: 10px;
        }

        @keyframes rainbow_move {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }

        div.stButton > button {
            background-color: #000 !important;
            color: #fff !important;
            border: none !important;
            border-radius: 50px !important;
            padding: 8px 25px !important;
            font-size: 14px !important;
            font-weight: bold !important;
        }
        </style>
        
        <img src="https://flagcdn.com/w160/id.png" class="round-flag" style="top:10%; left:10%;">
        <img src="https://flagcdn.com/w160/us.png" class="round-flag" style="top:40%; right:20%; animation-delay: -5s;">
        <img src="https://flagcdn.com/w160/ru.png" class="round-flag" style="bottom:10%; left:30%; animation-delay: -10s;">

        <div class="interrogation-box">
            <div style="font-size: 50px; margin-bottom: 10px;">🚔</div>
            <div class="warn-text">MAU NGAPAIN LO DI SINI, COK?!</div>
            <p style="color: #888; font-size: 0.9rem;">Halaman ini lagi disita negara. <br> Balik kerja sana ke web utama!</p>
        </div>
    """, unsafe_allow_html=True)

    # --- TOMBOL REDIRECT ---
    _, col_tengah, _ = st.columns([1, 2, 1])
    with col_tengah:
        st.markdown('<div style="text-align: center;"><div class="btn-wrapper">', unsafe_allow_html=True)
        st.link_button("🏃 KABUR KE WEB UTAMA", "https://pintar.streamlit.app/")
        st.markdown('</div></div>', unsafe_allow_html=True)

    st.stop()

halaman_kocak_interogasi()
