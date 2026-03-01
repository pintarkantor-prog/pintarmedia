import streamlit as st

def halaman_pro_digital_v2():
    st.set_page_config(
        page_title="Pintar Digital | Secure Access",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: POSISI TENGAH MUTLAK & NO GHOST ELEMENTS ---
    st.markdown("""
        <style>
        /* Hapus elemen bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* Background Deep Space */
        .main {
            background: radial-gradient(circle at center, #0a192f 0%, #020c1b 100%) !important;
            height: 100vh !important;
            overflow: hidden !important;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* CONTAINER UTAMA TENGAH */
        .command-center {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 30px; /* Jarak antara box dan tombol */
            z-index: 100;
        }

        /* KARTU AKSES TENGAH */
        .command-card {
            background: rgba(10, 25, 47, 0.7);
            backdrop-filter: blur(15px);
            padding: 50px;
            border-radius: 20px;
            border: 1px solid rgba(100, 255, 218, 0.2);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 0 0 20px rgba(100, 255, 218, 0.1);
            width: 450px;
            text-align: center;
        }

        .title-pro {
            color: #64ffda;
            font-family: 'Inter', sans-serif;
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: 5px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }

        /* TOMBOL MINIMALIS RGB CENTER */
        .btn-glow-container {
            padding: 2px;
            border-radius: 50px;
            background: linear-gradient(90deg, #64ffda, #4facfe, #64ffda);
            background-size: 200%;
            animation: move_gradient 4s linear infinite;
            width: 280px; /* Lebar tombol fix */
        }

        @keyframes move_gradient {
            0% { background-position: 0% 50%; }
            100% { background-position: 200% 50%; }
        }

        div.stButton > button {
            background-color: #0a192f !important;
            color: #64ffda !important;
            border: none !important;
            border-radius: 50px !important;
            width: 100% !important;
            padding: 12px 0 !important;
            font-size: 14px !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            letter-spacing: 2px !important;
            transition: 0.3s ease;
        }

        div.stButton > button:hover {
            background-color: #64ffda !important;
            color: #0a192f !important;
            box-shadow: 0 0 20px rgba(100, 255, 218, 0.5);
        }

        </style>
    """, unsafe_allow_html=True)

    # --- STRUKTUR HTML DI TENGAH ---
    st.markdown("""
        <div class="main">
            <div class="command-center">
                <div class="command-card">
                    <div style="color: #64ffda; font-size: 50px; margin-bottom: 20px;">🔒</div>
                    <div class="title-pro">SYSTEM LOCKED</div>
                    <p style="color: #8892b0; letter-spacing: 1px;">PINTAR MEDIA SEDANG DALAM PROSES MAINTENANCE INTERNAL.</p>
                </div>
                """, unsafe_allow_html=True)

    # Inject Tombol Streamlit di tengah bawah Card
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown('<div class="btn-glow-container">', unsafe_allow_html=True)
        st.link_button("ACCESS MAIN SERVER", "https://pintar.streamlit.app/")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)
    st.stop()

halaman_pro_digital_v2()
