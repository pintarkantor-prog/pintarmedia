import streamlit as st

def halaman_final_ramadhan_paten():
    st.set_page_config(
        page_title="Pintar Media | Mudik Galaksi",
        page_icon="🕌",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # --- SATU BLOK SAKTI: SEMUA CSS & HTML NYATU DI SINI ---
    st.markdown("""
        <style>
        /* SIKAT SEMUA SAMPAH STREAMLIT */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* BACKGROUND JALAN PELAN */
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
            animation: move_space_slow 180s linear infinite;
        }

        @keyframes move_space_slow {
            from { background-position: 0 0; }
            to { background-position: -1000px 1000px; }
        }

        /* KUNCI MATI DI TENGAH LAYAR */
        .viewport-center {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            z-index: 99999;
            width: 480px;
        }

        /* KOTAK TERMINAL RAMADHAN */
        .ramadhan-card {
            background: rgba(13, 17, 23, 0.95);
            backdrop-filter: blur(10px);
            padding: 50px 40px;
            border: 2px solid #d4af37; /* EMAS MEWAH */
            border-radius: 25px;
            box-shadow: 0 0 50px rgba(212, 175, 55, 0.3);
            text-align: center;
            width: 100%;
            position: relative;
        }

        /* KETUPAT CSS MURNI DI POJOK ATAS KOTAK */
        .ketupat {
            position: absolute;
            top: -30px;
            width: 50px;
            height: 50px;
            background-color: #d4af37;
            transform: rotate(45deg);
            border: 2px solid #062c12;
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
            z-index: 100;
        }
        .ketupat::after {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: linear-gradient(0deg, transparent 50%, rgba(10, 45, 20, 0.5) 50%),
                              linear-gradient(90deg, transparent 50%, rgba(10, 45, 20, 0.5) 50%);
            background-size: 12px 12px;
        }
        .k-left { left: 40px; }
        .k-right { right: 40px; }

        .block-container { padding: 0 !important; }
        </style>

        <div class="viewport-center">
            <div class="ramadhan-card">
                <div class="ketupat k-left"></div>
                <div class="ketupat k-right"></div>

                <div style="color: #d4af37; font-family: serif; letter-spacing: 4px; margin-bottom: 20px; font-size: 1rem; font-style: italic; text-shadow: 0 0 10px #d4af37;">
                    — MUDIK DIGITAL 1445H —
                </div>
                
                <h1 style="color: white; font-family: sans-serif; font-weight: 800; font-size: 2.1rem; margin-bottom: 20px; border: none;">
                    PORTAL MIGRASI<br><span style="color:#d4af37; font-size:1.8rem;">PINTAR MEDIA</span>
                </h1>
                
                <div style="height: 2px; width: 60px; background: #d4af37; margin: 0 auto 25px;"></div>
                
                <p style="color: #a0c4ab; font-size: 1rem; line-height: 1.8; margin: 0;">
                    Mohon maaf lahir dan batin.<br>
                    Alamat web ini sudah <span style="color:#d4af37; font-weight:bold;">tidak digunakan lagi</span>.<br><br>
                    Silakan akses portal utama melalui:<br>
                    <span style="color: #d4af37; font-weight: bold; font-size: 1.2rem; letter-spacing: 1px;">pintar.streamlit.app</span>
                </p>
                
                <div style="margin-top: 30px; color: #d4af37; font-size: 30px; text-shadow: 0 0 15px #d4af37;">🕌 ✨</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_final_ramadhan_paten()
