import streamlit as st

def halaman_ramadhan_galaxy_final():
    st.set_page_config(
        page_title="Pintar Digital | Mudik Galaksi",
        page_icon="🕌",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: SLOW MOVING SPACE + REAL KETUPAT + NO BUTTONS ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen sampah & padding bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. BACKGROUND: JALAN PELAN KAYAK SHIP NEMBUS GALAKSI */
        .main {
            background-color: #020f06 !important;
            /* Pake gradient deep green & navy buat vibe angkasa */
            background-image: 
                radial-gradient(circle at center, rgba(10, 60, 30, 0.3) 0%, #020f06 100%),
                url('https://www.transparenttextures.com/patterns/stardust.png');
            background-size: cover;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
            /* Animasi jalan PELAN (120 detik per siklus) */
            animation: move_space_slow 120s linear infinite;
        }

        @keyframes move_space_slow {
            from { background-position: 0 0; }
            to { background-position: -500px 500px; }
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
            width: 500px; /* Kunci lebar biar gak melar kayak image_6c76eb */
        }

        /* 4. KOTAK TERMINAL GLASSMORPHISM MEWAH */
        .glass-terminal-box {
            background: rgba(22, 27, 34, 0.95);
            backdrop-filter: blur(10px);
            padding: 60px 50px;
            /* Border Emas Mewah */
            border: 2px solid rgba(212, 175, 55, 0.6);
            border-radius: 20px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), inset 0 0 20px rgba(212, 175, 55, 0.2);
            text-align: center;
            width: 100%; /* Ngikutin wrapper 500px */
            box-sizing: border-box;
            position: relative;
        }

        /* 5. EFEK KETUPAT CSS MURNI (ANTI BAMBU ANJIR) */
        /* Kita bikin 2 ketupat nangkring di atas kotak */
        .ketupat-wrapper {
            position: absolute;
            top: -45px;
            left: 0;
            width: 100%;
            display: flex;
            justify-content: space-between;
            padding: 0 40px;
            box-sizing: border-box;
        }

        .ketupat {
            width: 60px;
            height: 60px;
            background-color: #d4af37; /* Warna Janur Emas */
            position: relative;
            transform: rotate(45deg);
            border: 2px solid rgba(10, 45, 20, 0.8);
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.5);
            animation: ketupat_sway 5s ease-in-out infinite;
        }

        /* Corak Janur Ketupat */
        .ketupat::after {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: linear-gradient(0deg, transparent 50%, rgba(10, 45, 20, 0.6) 50%),
                              linear-gradient(90deg, transparent 50%, rgba(10, 45, 20, 0.6) 50%);
            background-size: 15px 15px;
        }

        @keyframes ketupat_sway {
            0%, 100% { transform: rotate(45deg) translateY(0); }
            50% { transform: rotate(45deg) translateY(-8px); }
        }

        /* 6. TEXT STYLING NEON GOLD */
        .neon-gold {
            color: #d4af37;
            font-family: serif;
            font-size: 1.15rem;
            font-style: italic;
            letter-spacing: 4px;
            text-shadow: 0 0 15px rgba(212, 175, 55, 0.7);
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
                <div class="ketupat-wrapper">
                    <div class="ketupat"></div>
                    <div class="ketupat"></div>
                </div>

                <div class="neon-gold">— MUDIK DIGITAL 1445H —</div>
                <h1 class="main-title">PORTAL MIGRASI<br><span style="color:#d4af37; font-size:1.9rem;">PINTAR MEDIA</span></h1>
                <div style="height: 2px; width: 60px; background: #d4af37; margin: 0 auto 25px;"></div>
                <p class="desc-text">
                    Mohon maaf lahir dan batin.<br>
                    Alamat web ini sudah <span class="highlight-gold">tidak digunakan lagi</span>.<br><br>
                    Silakan akses portal utama kami di:<br>
                    <span class="highlight-gold" style="font-size: 1.25rem; letter-spacing: 1px;">pintar.streamlit.app</span>
                </p>
                <div style="margin-top: 35px; color: #d4af37; font-size: 25px; text-shadow: 0 0 15px #d4af37;">🕌 ✨</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_ramadhan_galaxy_final()
