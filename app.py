import streamlit as st

def halaman_migrasi_final_clean():
    st.set_page_config(
        page_title="Pintar Media | Migration",
        page_icon="🔐",
        layout="centered", 
        initial_sidebar_state="collapsed"
    )

    # --- CSS NUCLEAR: TOTAL TEAL NEON & ABSOLUTE CENTER ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen & padding bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Deep Space dengan Spotlight Biru Terang */
        .main {
            background: radial-gradient(circle at center, rgba(0, 242, 254, 0.25) 0%, #050a0f 100%) !important;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }

        /* 3. KUNCI MATI KOTAK DI TENGAH LAYAR (ANTI GESER) */
        .viewport-center {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 99999;
            width: 480px; /* Kunci lebar biar gak melar */
        }

        /* 4. KOTAK TERMINAL DENGAN NEON BREATHING GLOW KUAT */
        .terminal-neon-box {
            background: rgba(10, 25, 47, 0.98);
            padding: 55px;
            /* Border Neon Biru Cyan */
            border: 2px solid #00f2fe;
            border-radius: 20px;
            box-shadow: 
                0 0 30px rgba(0, 242, 254, 0.3),
                inset 0 0 15px rgba(0, 242, 254, 0.1);
            text-align: center;
            width: 100%; 
            box-sizing: border-box;
            /* Animasi Berdenyut */
            animation: neon_pulse 6s ease-in-out infinite;
        }

        @keyframes neon_pulse {
            0%, 100% { 
                box-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
                border-color: rgba(0, 242, 254, 0.5);
            }
            50% { 
                box-shadow: 0 0 70px rgba(0, 242, 254, 0.7);
                border-color: rgba(0, 242, 254, 1);
            }
        }

        /* 5. TEKS STATUS NEON FLICKER */
        .status-tag {
            color: #00f2fe;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            font-weight: bold;
            letter-spacing: 5px;
            margin-bottom: 25px;
            text-transform: uppercase;
            text-shadow: 0 0 15px #00f2fe;
        }

        /* Sikat paksa padding container agar tidak mojok */
        .block-container { padding: 0 !important; }
        </style>

        <div class="viewport-center">
            <div class="terminal-neon-box">
                <div class="status-tag">[ MIGRATION COMPLETED ]</div>
                <h1 style="color: white; font-family: sans-serif; margin-bottom: 20px; font-size: 2.2rem; font-weight: 800;">MIGRASI SISTEM</h1>
                <p style="color: #8b949e; font-size: 1.1rem; line-height: 1.8; margin: 0;">
                    Alamat web ini sudah <b style="color: #00f2fe;">tidak digunakan lagi</b>.<br><br>
                    Mohon gunakan portal utama <b style="color: #00f2fe;">pintar.streamlit.app</b> untuk mengakses sistem PINTAR MEDIA.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_migrasi_final_clean()
