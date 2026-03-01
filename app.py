import streamlit as st

def halaman_ramadhan_galaxy_final():
    st.set_page_config(
        page_title="Pintar Media | Mudik Galaksi",
        page_icon="🕌",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SNIPER: MOVING SPACE + KETUPAT + NO BUTTONS ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen sampah Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. BACKGROUND LUAR ANGKASA JALAN (ANIMASI) */
        .main {
            background-color: #020f06 !important;
            background-image: 
                radial-gradient(circle at center, rgba(10, 60, 30, 0.4) 0%, #020f06 100%),
                url('https://www.transparenttextures.com/patterns/stardust.png');
            background-size: cover;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            overflow: hidden !important;
            animation: space_travel 60s linear infinite;
        }

        @keyframes space_travel {
            from { background-position: 0 0; }
            to { background-position: 1000px -1000px; }
        }

        /* 3. KETUPAT GANTUNG (KUNCI DI ATAS) */
        .ketupat-wrapper {
            position: fixed;
            top: 20px;
            width: 100%;
            display: flex;
            justify-content: space-between;
            padding: 0 15%;
            z-index: 1000;
        }

        .ketupat-item {
            font-size: 50px;
            filter: drop-shadow(0 0 15px #d4af37);
            animation: swing_ketupat 4s ease-in-out infinite;
            transform-origin: top center;
        }

        @keyframes swing_ketupat {
            0%, 100% { transform: rotate(-10deg); }
            50% { transform: rotate(10deg); }
        }

        /* 4. KOTAK TENGAH (FIXED NO MELAR) */
        .center-box {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 480px;
            background: rgba(10, 45, 20, 0.95);
            padding: 50px;
            border: 2px solid #d4af37;
            border-radius: 20px;
            box-shadow: 0 0 50px rgba(212, 175, 55, 0.3);
            text-align: center;
            z-index: 9999;
        }

        .gold-glow {
            color: #d4af37;
            font-family: serif;
            letter-spacing: 4px;
            text-shadow: 0 0 10px #d4af37;
            margin-bottom: 20px;
        }

        .block-container { padding: 0 !important; }
        </style>

        <div class="ketupat-wrapper">
            <div class="ketupat-item">🎍</div>
            <div class="ketupat-item">🎍</div>
        </div>

        <div class="center-box">
            <div style="font-size: 50px; margin-bottom: 10px;">🕌</div>
            <div class="gold-glow">RAMADHAN MUBARAK</div>
            <h1 style="color: white; font-family: sans-serif; font-weight: 800; font-size: 2.2rem; margin-bottom: 20px;">
                MIGRASI SISTEM
            </h1>
            <div style="height: 2px; width: 60px; background: #d4af37; margin: 0 auto 25px;"></div>
            <p style="color: #a0c4ab; font-size: 1.1rem; line-height: 1.8;">
                Mohon maaf lahir dan batin.<br>
                Web ini sudah <span style="color: #d4af37; font-weight: bold;">tidak digunakan lagi</span>.<br><br>
                Silakan akses portal utama melalui:<br>
                <span style="color: #d4af37; font-weight: bold; font-size: 1.3rem; letter-spacing: 1px;">pintar.streamlit.app</span>
            </p>
            <div style="margin-top: 25px; color: #d4af37; font-size: 20px;">✨ 🌙 ✨</div>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_ramadhan_galaxy_final()
