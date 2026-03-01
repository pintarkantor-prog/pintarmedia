import streamlit as st

def halaman_ramadhan_luxury_final():
    st.set_page_config(
        page_title="Pintar Digital | Ramadhan HQ",
        page_icon="🕌",
        layout="centered", # Layout sempit biar gak melar kayak pecel lele
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: DEEP SPACE MOVING + INTEGRATED MOSQUE ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen & padding bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. BACKGROUND: JALAN PELAN KAYAK SHIP NEMBUS GALAKSI */
        .main {
            background-color: #020f06 !important;
            /* Pake gradient deep green & navy buat vibe angkasa */
            background-image: 
                radial-gradient(circle at center, rgba(10, 45, 20, 0.4) 0%, #020f06 100%),
                url('https://www.transparenttextures.com/patterns/stardust.png');
            background-size: cover, auto;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
            /* Animasi jalan pelan */
            animation: move_space 100s linear infinite;
        }

        @keyframes move_space {
            from { background-position: center center, 0 0; }
            to { background-position: center center, -1000px 1000px; }
        }

        /* 3. WRAPPER UTAMA (KUNCI SEMUANYA DI TITIK TENGAH) */
        .ultimate-center {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            z-index: 99999;
            width: 500px; /* Kunci lebar biar gak melar */
        }

        /* 4. KOTAK TERMINAL GLASSMORPHISM (MEWAH) */
        .glass-terminal-box {
            background: rgba(22, 27, 34, 0.9);
            backdrop-filter: blur(10px);
            padding: 55px;
            /* Border Emas Mewah */
            border: 1px solid rgba(212, 175, 55, 0.5);
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(212, 175, 55, 0.1);
            text-align: center;
            width: 100%; /* Ngikutin wrapper 500px */
            box-sizing: border-box;
            position: relative;
        }

        /* 5. INTEGRASI MESJID DI BAWAH KOTAK */
        .mosque-pendant {
            margin-top: -1px; /* Nempel ke kotak */
            width: 150px;
            height: 80px;
            background: linear-gradient(180deg, rgba(212, 175, 55, 0.4) 0%, rgba(212, 175, 55, 0) 100%);
            border-radius: 0 0 100px 100px; /* Bentuk kubah gantung */
            border: 1px solid rgba(212, 175, 55, 0.5);
            border-top: none;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
        }

        /* 6. TEXT STYLING NEON GOLD */
        .neon-gold {
            color: #d4af37;
            font-family: serif;
            font-size: 1.1rem;
            font-style: italic;
            letter-spacing: 3px;
            text-shadow: 0 0 15px rgba(212, 175, 55, 0.6);
            margin-bottom: 25px;
        }

        .main-title {
            color: white;
            font-family: sans-serif;
            font-weight: 800;
            font-size: 2.3rem;
            margin-bottom: 20px;
            letter-spacing: -1px;
        }

        .desc-text {
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

        <div class="ultimate-center">
            <div class="glass-terminal-box">
                <div class="neon-gold">— SELAMAT IDUL FITRI —</div>
                <h1 class="main-title">PORTAL MIGRASI<br><span style="color:#d4af37; font-size:1.9rem;">PINTAR DIGITAL</span></h1>
                <div style="height: 2px; width: 60px; background: #d4af37; margin: 0 auto 25px;"></div>
                <p class="desc-text">
                    Mohon maaf lahir dan batin.<br>
                    Alamat web ini sudah <span class="highlight-gold">tidak digunakan lagi</span>.<br><br>
                    Silakan akses portal utama kami di:<br>
                    <span class="highlight-gold" style="font-size: 1.25rem; letter-spacing: 1px;">pintar.streamlit.app</span>
                </p>
                <div style="margin-top: 30px; color: #d4af37; font-size: 20px;">🕌 ✨</div>
            </div>
            
            <div class="mosque-pendant">
                <div style="font-size: 40px; text-shadow: 0 0 15px #d4af37;">🕌</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_ramadhan_luxury_final()
