import streamlit as st

def halaman_void_minimalis():
    st.set_page_config(
        page_title="Pintar Digital | Redirect",
        page_icon="🕶️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: HAPUS SEMUA & KUNCI TOMBOL DI TENGAH ---
    st.markdown("""
        <style>
        /* 1. Sikat semua elemen bawaan, garis, dan footer */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Hitam Pekat */
        .main {
            background-color: #000000 !important;
            height: 100vh !important;
            width: 100vw !important;
            overflow: hidden !important;
            margin: 0 !important;
            padding: 0 !important;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* 3. Kunci Tombol di Tengah Layar (Absolute Center) */
        .void-container {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 9999;
            text-align: center;
        }

        /* 4. Styling Tombol Kecil Profesional */
        div.stButton > button {
            background-color: transparent !important;
            color: #64ffda !important; /* Warna Teal Pro */
            border: 1px solid #64ffda !important;
            border-radius: 5px !important;
            padding: 10px 25px !important;
            font-size: 14px !important;
            font-family: 'Courier New', monospace;
            letter-spacing: 2px;
            transition: 0.4s all;
            width: auto !important;
        }

        div.stButton > button:hover {
            background-color: rgba(100, 255, 218, 0.1) !important;
            box-shadow: 0 0 20px rgba(100, 255, 218, 0.4);
            transform: scale(1.05);
        }

        /* Hapus garis biru atau hijau yang suka muncul di bawah elemen */
        .stMarkdownContainer { border: none !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- INJECT TOMBOL KE TITIK TENGAH ---
    st.markdown('<div class="void-container">', unsafe_allow_html=True)
    st.link_button("CONNECT TO MAIN SERVER", "https://pintar.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

halaman_void_minimalis()
