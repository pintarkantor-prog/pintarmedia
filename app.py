import streamlit as st

def halaman_ramadhan_v2_luxury():
    st.set_page_config(
        page_title="Pintar Media | Ramadhan HQ",
        page_icon="🌙",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: ANIMATED LANTERNS & GLASSMORPHISM ---
    st.markdown("""
        <style>
        /* 1. Sikat habis elemen Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Deep Green & Pattern Mandala */
        .main {
            background-color: #020f06 !important;
            background-image: radial-gradient(circle at center, #062c12 0%, #020f06 100%);
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            overflow: hidden !important;
        }

        /* 3. EFEK LAMPION GANTUNG (LANTERNS) */
        .lantern {
            position: fixed;
            top: -10px;
            font-size: 40px;
            z-index: 1;
            animation: swing 3s ease-in-out infinite;
            transform-origin: top center;
            filter: drop-shadow(0 0 10px #d4af37);
        }
        .l1 { left: 10%; animation-delay: 0s; }
        .l2 { right: 10%; animation-delay: 0.5s; }

        @keyframes swing {
            0%, 100% { transform: rotate(-5deg); }
            50% { transform: rotate(5deg); }
        }

        /* 4. KOTAK GLASSMORPHISM (MEWAH) */
        .glass-box {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 9999;
            width: 500px;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(15px);
            padding: 60px 40px;
            border: 1px solid rgba(212, 175, 55, 0.4);
            border-radius: 30px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(212, 175, 55, 0.1);
            text-align: center;
        }

        /* 5. TEXT STYLING */
        .gold-glow {
            color: #d4af37;
            font-family: 'Times New Roman', serif;
            font-style: italic;
            font-size: 1.1rem;
            letter-spacing: 4px;
            text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
            margin-bottom: 25px;
        }

        .title-ramadhan {
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            font-weight: 900;
            font-size: 2.5rem;
            letter-spacing: -1px;
            margin-bottom: 15px;
            text-transform: uppercase;
        }

        .desc-ramadhan {
            color: #a0c4ab;
            font-size: 1.05rem;
            line-height: 1.8;
            margin-top: 20px;
        }

        /* Sikat paksa padding agar tetap di tengah */
        .block-container { padding: 0 !important; }
        </style>

        <div class="lantern l1">🏮</div>
        <div class="lantern l2">🏮</div>

        <div class="glass-box">
            <div class="gold-glow">— Ramadhan Mubarak —</div>
            <h1 class="title-ramadhan">PINTAR MEDIA<br><span style="color:#d4af37; font-size:1.8rem;">MIGRATION</span></h1>
            <div style="height: 1px; width: 60px; background: #d4af37; margin: 20px auto;"></div>
            <p class="desc-ramadhan">
                Sehubungan dengan pembaruan infrastruktur digital,<br> 
                alamat ini sudah <b>tidak aktif</b>.<br><br>
                Silakan beralih ke portal utama kami di:<br>
                <span style="color: #d4af37; font-weight: bold; font-size: 1.2rem; letter-spacing: 1px;">pintar.streamlit.app</span>
            </p>
            <div style="margin-top: 30px; opacity: 0.6; font-size: 1.5rem;">✨ 🕌 ✨</div>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_ramadhan_v2_luxury()
