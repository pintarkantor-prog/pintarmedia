import streamlit as st

def halaman_pro_digital():
    st.set_page_config(
        page_title="Pintar Digital | Secure Access",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: PRO DIGITAL, NO FLYING OBJECTS, PURE CENTER ---
    st.markdown("""
        <style>
        /* 1. Hapus SEMUA elemen bawaan Streamlit & Garis-garis 'njir' */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Deep Space dengan Animasi Mesh Tipis */
        .main {
            background: radial-gradient(circle at center, #0a192f 0%, #020c1b 100%) !important;
            height: 100vh !important;
            width: 100vw !important;
            overflow: hidden !important;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* 3. KARTU AKSES TENGAH (PRO LOOK) */
        .command-card {
            position: fixed;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            z-index: 100;
            text-align: center;
            background: rgba(10, 25, 47, 0.7);
            backdrop-filter: blur(15px); /* Efek kaca pro */
            padding: 50px;
            border-radius: 20px;
            border: 1px solid rgba(100, 255, 218, 0.2);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 0 0 20px rgba(100, 255, 218, 0.1);
            width: 400px;
        }

        .title-pro {
            color: #64ffda; /* Warna Teal Digital */
            font-family: 'Inter', sans-serif;
            font-size: 1.8rem;
            font-weight: 800;
            letter-spacing: 4px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }

        .sub-pro {
            color: #8892b0;
            font-size: 0.9rem;
            letter-spacing: 1px;
            margin-bottom: 30px;
        }

        /* 4. TOMBOL MINIMALIS RGB GLOW */
        .btn-glow-container {
            display: inline-block;
            padding: 2px;
            border-radius: 50px;
            background: linear-gradient(90deg, #64ffda, #4facfe, #64ffda);
            background-size: 200%;
            animation: move_gradient 4s linear infinite;
        }

        @keyframes move_gradient {
            0% { background-position: 0% 50%; }
            100% { background-position: 200% 50%; }
        }

        div.stButton > button {
            background-color: #0a192f !important;
            color: #64ffda !important;
            border: none !important;
            border-radius: 50px !important;
            padding: 12px 35px !important;
            font-size: 14px !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            letter-spacing: 2px !important;
            transition: 0.3s ease;
        }

        div.stButton > button:hover {
            background-color: #64ffda !important;
            color: #0a192f !important;
            box-shadow: 0 0 20px rgba(100, 255, 218, 0.5);
        }

        </style>
        
        <div class="command-card">
            <div style="color: #64ffda; font-size: 40px; margin-bottom: 20px;">🔒</div>
            <div class="title-pro">SYSTEM LOCKED</div>
            <div class="sub-pro">PINTAR MEDIA SEDANG DALAM PROSES MAINTENANCE INTERNAL.</div>
        </div>
    """, unsafe_allow_html=True)

    # --- TOMBOL REDIRECT (FIXED CENTER) ---
    st.markdown('<div style="position: fixed; top: 70%; left: 50%; transform: translateX(-50%); z-index: 101;">', unsafe_allow_html=True)
    st.markdown('<div class="btn-glow-container">', unsafe_allow_html=True)
    st.link_button("ACCESS MAIN SERVER", "https://pintar.streamlit.app/")
    st.markdown('</div></div>', unsafe_allow_html=True)

    st.stop()

halaman_pro_digital()
