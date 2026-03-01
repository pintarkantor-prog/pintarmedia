import streamlit as st

def halaman_war_digital():
    st.set_page_config(
        page_title="Pintar Digital | WAR ZONE",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: ANIMASI PERANG DIGITAL KELILING HALAMAN ---
    st.markdown("""
        <style>
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        .main {
            background-color: #020508; /* Gelap total */
            height: 100vh;
            color: #00f2fe;
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
            position: relative;
        }

        /* --- OBJEK PERANG YANG KELILING --- */
        .war-obj {
            position: absolute;
            font-size: 50px;
            z-index: 1;
        }

        /* Roket 1: Keliling Muter */
        .rocket-1 {
            animation: moveAround 10s linear infinite;
            top: 10%; left: 10%;
        }
        
        /* Tank: Jalan Horizontal */
        .tank-1 {
            animation: moveHorizontal 15s linear infinite;
            bottom: 20%; left: -100px;
            font-size: 60px;
        }

        /* Rudal: Kecepatan Tinggi */
        .missile-1 {
            animation: moveDiagonal 5s linear infinite;
            top: -50px; left: -50px;
            font-size: 40px;
        }

        /* Pesawat: Patroli Atas */
        .plane-1 {
            animation: moveHorizontalReverse 12s linear infinite;
            top: 20%; right: -100px;
            font-size: 55px;
        }

        /* --- DEFINISI ANIMASI --- */
        @keyframes moveAround {
            0% { transform: translate(0,0) rotate(0deg); }
            25% { transform: translate(80vw, 20vh) rotate(90deg); }
            50% { transform: translate(50vw, 80vh) rotate(180deg); }
            75% { transform: translate(0vw, 50vh) rotate(270deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }

        @keyframes moveHorizontal {
            from { left: -100px; }
            to { left: 110vw; }
        }

        @keyframes moveHorizontalReverse {
            from { right: -100px; }
            to { right: 110vw; }
        }

        @keyframes moveDiagonal {
            from { top: -50px; left: -50px; transform: rotate(45deg); }
            to { top: 110vh; left: 110vw; transform: rotate(45deg); }
        }

        /* --- CONTAINER TENGAH --- */
        .center-box {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            z-index: 10;
            background: rgba(5, 10, 15, 0.8);
            padding: 40px;
            border-radius: 20px;
            border: 2px solid #00f2fe;
            box-shadow: 0 0 30px #00f2fe;
        }

        .equalizer {
            display: flex;
            justify-content: center;
            gap: 5px;
            margin-bottom: 20px;
        }
        .bar {
            width: 8px; height: 30px;
            background: #00f2fe;
            animation: equalize 0.5s infinite alternate;
        }

        @keyframes equalize {
            from { height: 10px; }
            to { height: 40px; }
        }

        div.stButton > button {
            background: linear-gradient(45deg, #00f2fe, #4facfe);
            color: black !important;
            font-weight: bold;
            border-radius: 50px;
            padding: 10px 30px;
            border: none;
        }
        </style>
        
        <div class="war-obj rocket-1">🚀</div>
        <div class="war-obj tank-1">🚜</div> <div class="war-obj missile-1">🚀</div> <div class="war-obj plane-1">✈️</div>

        <div class="center-box">
            <div class="equalizer">
                <div class="bar"></div><div class="bar"></div><div class="bar"></div>
            </div>
            <h1 style="color:white; font-size: 2rem;">SERVER UNDER ATTACK!</h1>
            <p style="color: #00f2fe;">Lagi maintenance gila-gilaan, Cok! Jangan nangis.</p>
        </div>
    """, unsafe_allow_html=True)

    # Tombol Redirect
    st.link_button("💥 KABUR KE KANTOR PUSAT", "https://pintar.streamlit.app/", use_container_width=True)

    st.stop()

halaman_war_digital()
