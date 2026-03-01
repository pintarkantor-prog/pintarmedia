import streamlit as st

def halaman_ramadhan_galaxy_paten():
    st.set_page_config(
        page_title="Pintar Media | Mudik Galaksi",
        page_icon="🕌",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # --- JURUS SNIPER: CSS MURNI UNTUK KETUPAT & SPACE TRAVEL ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen sampah & padding bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. BACKGROUND: JALAN PELAN KAYAK SHIP NEMBUS GALAKSI */
        .main {
            background-color: #020f06 !important;
            background-image: 
                radial-gradient(circle at center, rgba(10, 60, 30, 0.3) 0%, #020f06 100%),
                url('https://www.transparenttextures.com/patterns/stardust.png');
            background-size: cover;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
            /* Animasi jalan PELAN (150 detik per siklus biar gak pusing) */
            animation: move_space_slow 150s linear infinite;
        }

        @keyframes move_space_slow {
            from { background-position: 0 0; }
            to { background-position: -800px 800px; }
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
            width: 500px;
        }

        /* 4. KOTAK TERMINAL (PROFESSIONAL LOOK) */
        .terminal-box {
            background: rgba(22, 27, 34, 0.95);
            backdrop-filter: blur(10px);
            padding: 55px;
            border: 2px solid #d4af37; /* WARNA EMAS (GOLD) */
            border-radius: 20px;
            box-shadow: 0 0 50px rgba(212, 175, 55, 0.3);
            text-align: center;
            width: 100%; 
            box-sizing: border-box;
            position: relative;
        }

        /* 5. KETUPAT CSS MURNI (NANGKRING DI POJOK BOX) */
        .ketupat-left, .ketupat-right {
            position: absolute;
            top: -30px;
            width: 60px;
            height: 60px;
            background-color: #d4af37;
            transform: rotate(45deg);
            border: 2px solid #062c12;
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.6);
            z-index: 100;
        }
        
        /* Corak Anyaman Ketupat */
        .ketupat-left::after, .ketupat-right::after {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: linear-gradient(0deg, transparent 50%, rgba(10, 45, 20, 0.6) 50%),
                              linear-gradient(90deg, transparent 50%, rgba(10, 45, 20, 0.6) 50%);
            background-size: 15px 15px;
        }

        .ketupat-left { left: 40px; }
        .ketupat-right { right: 40px; }

        .block-container { padding: 0 !important; }
        </style>

        <div class="ultimate-center">
            <div class="terminal-box">
                <div class="ketupat-left"></div>
                <div class="ketupat-right"></div>

                <div style="color: #d4af37; font-family: serif; letter-spacing: 4px; margin-bottom: 25px; font-size: 1.1rem; font-style: italic; text-shadow: 0 0 10px #d4af37;">
                    — MUDIK DIGITAL 1445H —
                </div>
                
                <h1 style="color: white; font-family: sans-serif; font-weight: 800; font-size: 2.3rem; margin-bottom: 20px; border: none;">
                    PORTAL MIGRASI<br><span style="color:#d4af37; font-size:1.9rem;">PINTAR MEDIA</span>
                </h1>
                
                <div style="height: 2px; width: 60px; background: #d4af37; margin: 0 auto 25px;"></div>
                
                <p style="color: #a0c4ab; font-size: 1.1rem; line-height: 1.8; margin: 0;">
                    Mohon maaf lahir dan batin.<br>
                    Alamat web ini sudah <span style="color:#d4af37; font-weight:bold;">tidak digunakan lagi</span>.<br><br>
                    Silakan akses portal utama melalui:<br>
                    <span style="color: #d4af37; font-weight: bold; font-size: 1.3rem;">pintar.streamlit.app</span>
                </p>
                
                <div style="margin-top: 35px; color: #d4af37; font-size: 25px; text-shadow: 0 0 15px #d4af37;">🕌 ✨</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_ramadhan_galaxy_paten()
