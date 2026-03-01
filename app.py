import streamlit as st

def halaman_ramadhan_indonesia():
    st.set_page_config(
        page_title="Pintar Media | Mudik Digital",
        page_icon="🕌",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: KETUPAT & MOSQUE SILHOUETTE ---
    st.markdown("""
        <style>
        /* 1. Sikat habis elemen bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Hijau Janur & Deep Green */
        .main {
            background: radial-gradient(circle at center, #0a3d1a 0%, #020f06 100%) !important;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }

        /* 3. EFEK KETUPAT GANTUNG (KIRI-KANAN) */
        .ketupat {
            position: fixed;
            top: -20px;
            font-size: 50px;
            z-index: 1;
            animation: swing_ketupat 4s ease-in-out infinite;
            transform-origin: top center;
            filter: drop-shadow(0 0 15px #d4af37);
        }
        .k1 { left: 15%; animation-delay: 0s; }
        .k2 { right: 15%; animation-delay: 1s; }

        @keyframes swing_ketupat {
            0%, 100% { transform: rotate(-8deg); }
            50% { transform: rotate(8deg); }
        }

        /* 4. KOTAK INFO (KUNCI TENGAH) */
        .indonesia-box {
            position: fixed;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 9999;
            width: 480px;
            background: rgba(10, 45, 20, 0.95);
            padding: 60px 40px;
            border: 2px solid #d4af37;
            border-radius: 20px;
            box-shadow: 0 0 50px rgba(212, 175, 55, 0.2);
            text-align: center;
        }

        /* 5. SILUET MESJID DI BAWAH KOTAK */
        .mosque-footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            height: 150px;
            background: url('https://www.transparenttextures.com/patterns/black-linen.png'), 
                        linear-gradient(transparent, rgba(212, 175, 55, 0.1));
            text-align: center;
            font-size: 80px;
            opacity: 0.4;
            z-index: 0;
        }

        .gold-text {
            color: #d4af37;
            font-family: serif;
            letter-spacing: 3px;
            text-transform: uppercase;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .title-main {
            color: white;
            font-family: sans-serif;
            font-weight: 800;
            font-size: 2rem;
            margin-bottom: 20px;
        }

        .desc-text {
            color: #a0c4ab;
            line-height: 1.8;
            font-size: 1rem;
        }

        .block-container { padding: 0 !important; }
        </style>

        <div class="ketupat k1">✨🎍</div>
        <div class="ketupat k2">🎍✨</div>

        <div class="indonesia-box">
            <div class="gold-text">Selamat Menyambut Idul Fitri</div>
            <h1 class="title-main">PORTAL MIGRASI<br>PINTAR MEDIA</h1>
            <div style="height: 2px; width: 80px; background: #d4af37; margin: 0 auto 25px;"></div>
            <p class="desc-text">
                Mohon maaf lahir dan batin.<br>
                Alamat web ini sudah <b style="color:#d4af37">tidak digunakan</b>.<br><br>
                Silakan akses portal utama melalui:<br>
                <span style="color: #d4af37; font-weight: bold; font-size: 1.3rem;">pintar.streamlit.app</span>
            </p>
        </div>

        <div class="mosque-footer">🕌🕌🕌</div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_ramadhan_indonesia()
