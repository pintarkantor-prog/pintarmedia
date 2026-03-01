import streamlit as st

def halaman_migrasi_total():
    st.set_page_config(
        page_title="Pintar Media | Migration",
        page_icon="🚀",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # --- CSS NUCLEAR: TOTAL TEAL & CENTER LOCK ---
    st.markdown("""
        <style>
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        .main {
            background: radial-gradient(circle at center, rgba(0, 242, 254, 0.2) 0%, #050a0f 100%) !important;
            height: 100vh !important;
            width: 100vw !important;
            overflow: hidden !important;
        }

        .center-lockdown {
            position: fixed;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px;
            z-index: 99999;
            width: 480px; /* Lebar mantap */
        }

        .terminal-box {
            background: rgba(10, 25, 47, 0.95);
            padding: 50px;
            border: 2px solid #00f2fe;
            border-radius: 15px;
            box-shadow: 0 0 40px rgba(0, 242, 254, 0.3);
            text-align: center;
            width: 100%;
            box-sizing: border-box;
        }

        .status-tag {
            color: #00f2fe;
            font-family: 'Courier New', monospace;
            font-size: 0.85rem;
            letter-spacing: 5px;
            text-shadow: 0 0 10px #00f2fe;
            margin-bottom: 20px;
            text-transform: uppercase;
        }

        .main-btn {
            display: block;
            width: 100%;
            padding: 18px 0;
            background: transparent;
            color: #00f2fe !important;
            border: 2px solid #00f2fe;
            border-radius: 10px;
            text-align: center;
            text-decoration: none !important;
            font-family: sans-serif;
            font-weight: bold;
            font-size: 1rem;
            letter-spacing: 2px;
            transition: 0.4s all;
            box-shadow: 0 0 15px rgba(0, 242, 254, 0.2);
        }

        .main-btn:hover {
            background: rgba(0, 242, 254, 0.15);
            box-shadow: 0 0 30px #00f2fe;
            color: white !important;
            transform: translateY(-3px);
        }

        .block-container { padding: 0 !important; }
        </style>

        <div class="center-lockdown">
            <div class="terminal-box">
                <div class="status-tag">[ MIGRATION COMPLETED ]</div>
                <h1 style="color: white; font-family: sans-serif; margin-bottom: 20px; font-size: 2rem;">MIGRASI SISTEM</h1>
                <p style="color: #8b949e; font-size: 1.1rem; line-height: 1.8; margin: 0;">
                    Alamat web ini sudah <b>tidak digunakan lagi</b>.<br> 
                    Mohon gunakan portal utama di bawah untuk mengakses sistem PINTAR MEDIA.
                </p>
            </div>
            
            <a href="https://pintar.streamlit.app/" class="main-btn">
                AKSES WEB UTAMA SEKARANG
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_migrasi_total()
