import streamlit as st

def halaman_digital_rocket():
    st.set_page_config(
        page_title="Pintar Digital | Launching",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: FULL DIGITAL + ROKET ANIMASI ---
    st.markdown("""
        <style>
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        .main {
            background-color: #050a0f; /* Hitam luar angkasa */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #00f2fe;
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
        }
        
        .digital-container {
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* --- ANIMASI ROKET GETAR --- */
        .rocket-box {
            font-size: 80px;
            margin-bottom: 10px;
            animation: shake 0.5s infinite;
            display: inline-block;
        }
        
        @keyframes shake {
            0% { transform: translate(1px, 1px) rotate(0deg); }
            10% { transform: translate(-1px, -2px) rotate(-1deg); }
            20% { transform: translate(-3px, 0px) rotate(1deg); }
            30% { transform: translate(3px, 2px) rotate(0deg); }
            40% { transform: translate(1px, -1px) rotate(1deg); }
            50% { transform: translate(-1px, 2px) rotate(-1deg); }
            100% { transform: translate(1px, -2px) rotate(0deg); }
        }

        /* --- EQUALIZER DIGITAL --- */
        .equalizer {
            display: flex;
            justify-content: space-between;
            width: 80px;
            height: 40px;
            margin: 20px 0;
        }
        .bar {
            width: 10px;
            height: 100%;
            background: #00f2fe;
            animation: equalize 0.8s ease-in-out infinite;
        }
        .bar:nth-child(1) { animation-delay: 0.0s; }
        .bar:nth-child(2) { animation-delay: 0.2s; }
        .bar:nth-child(3) { animation-delay: 0.4s; }
        
        @keyframes equalize {
            0%, 100% { transform: scaleY(1); }
            50% { transform: scaleY(0.3); }
        }

        .status-text {
            font-size: 1.2rem;
            font-weight: bold;
            letter-spacing: 3px;
            color: #ffffff;
            text-shadow: 0 0 10px #00f2fe;
        }

        /* --- TOMBOL PINDAH GACOR --- */
        div.stButton > button {
            background: linear-gradient(45deg, #ff4b2b, #ff416c); /* Warna api roket */
            color: white !important;
            border-radius: 50px !important;
            padding: 15px 40px;
            font-weight: bold;
            border: none;
            box-shadow: 0 0 20px rgba(255, 75, 43, 0.5);
            transition: 0.3s;
        }
        div.stButton > button:hover {
            transform: scale(1.1);
            box-shadow: 0 0 30px rgba(255, 75, 43, 0.8);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- HTML STRUCTURE ---
    st.markdown("""
        <div class="digital-container">
            <div class="rocket-box">🚀</div>
            <div class="equalizer">
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
            </div>
            <div class="status-text">SYSTEM UPGRADING...</div>
            <p style="color: #4facfe;">Harap tenang, roket lagi dipanasin buat ke Web Utama.</p>
        </div>
    """, unsafe_allow_html=True)

    # Tombol Redirect Langsung ke Web Utama lo
    st.link_button("🔥 MELUNCUR KE KANTOR PUSAT", "https://pintar.streamlit.app/", use_container_width=True)

    st.stop()

halaman_digital_rocket()
