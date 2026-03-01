import streamlit as st

def halaman_ramadhan_migration():
    st.set_page_config(
        page_title="Pintar Media | Ramadhan Kareem",
        page_icon="🌙",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # --- CSS NUCLEAR: RAMADHAN VIBE & CENTER LOCK ---
    st.markdown("""
        <style>
        /* 1. Sikat semua elemen bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Malam Ramadhan (Hijau Tua & Gold) */
        .main {
            background: radial-gradient(circle at center, #062c12 0%, #020f06 100%) !important;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }

        /* 3. EFEK BINTANG KELAP-KELIP */
        .stars {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: transparent url('https://www.transparenttextures.com/patterns/stardust.png') repeat;
            z-index: 0;
            opacity: 0.5;
            animation: twinkle 5s infinite linear;
        }

        @keyframes twinkle {
            0% { opacity: 0.3; }
            50% { opacity: 0.7; }
            100% { opacity: 0.3; }
        }

        /* 4. KOTAK TERMINAL RAMADHAN (KUNCI TENGAH) */
        .ramadhan-box {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 99999;
            width: 480px;
            background: rgba(10, 45, 20, 0.95);
            padding: 50px;
            border: 2px solid #d4af37; /* WARNA EMAS (GOLD) */
            border-radius: 25px;
            box-shadow: 0 0 50px rgba(212, 175, 55, 0.3);
            text-align: center;
            box-sizing: border-box;
        }

        /* 5. ORNAMEN ISLAMI (TEKS) */
        .islamic-header {
            color: #d4af37;
            font-family: 'Georgia', serif;
            font-size: 1.2rem;
            letter-spacing: 3px;
            margin-bottom: 20px;
            text-transform: uppercase;
            text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
        }

        .main-title {
            color: #ffffff;
            font-family: sans-serif;
            font-weight: 800;
            font-size: 2.2rem;
            margin-bottom: 15px;
        }

        .sub-text {
            color: #a0c4ab;
            font-size: 1.1rem;
            line-height: 1.8;
            margin: 0;
        }

        .highlight-gold {
            color: #d4af37;
            font-weight: bold;
        }

        /* Sikat paksa padding agar tetap di tengah */
        .block-container { padding: 0 !important; }
        </style>

        <div class="stars"></div>

        <div class="ramadhan-box">
            <div style="font-size: 40px; margin-bottom: 10px;">🌙</div>
            <div class="islamic-header">Ramadhan Kareem</div>
            <h1 class="main-title">MIGRASI SISTEM</h1>
            <p class="sub-text">
                Mohon maaf atas ketidaknyamanannya.<br> 
                Web ini sudah <span class="highlight-gold">tidak digunakan lagi</span>.<br><br>
                Silakan akses portal utama kami di:<br>
                <span class="highlight-gold" style="font-size: 1.2rem;">pintar.streamlit.app</span>
            </p>
            <div style="margin-top: 25px; color: #d4af37; font-size: 20px;">🕌 ✨</div>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_ramadhan_migration()
