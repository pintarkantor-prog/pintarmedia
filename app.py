import streamlit as st

def halaman_digital_warfare():
    st.set_page_config(
        page_title="Pintar Digital | WAR ZONE",
        page_icon="💥",
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
            background-color: #020508;
            height: 100vh;
            color: #00f2fe;
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
            position: relative;
        }

        /* --- OBJEK PERANG YANG KELILING (RAME-RAME) --- */
        .war-obj {
            position: absolute;
            font-size: 60px;
            z-index: 1;
        }

        /* Roket 1: Keliling Muter */
        .rocket-1 { animation: moveAround 8s linear infinite; top: 10%; left: 10%; }
        /* Tank: Jalan Horizontal */
        .tank-1 { animation: moveHorizontal 12s linear infinite; bottom: 20%; left: -100px; }
        /* Rudal Cepat */
        .missile-1 { animation: moveDiagonal 4s linear infinite; top: -50px; left: -50px; font-size: 40px; }
        /* Pesawat Patroli */
        .plane-1 { animation: moveHorizontalReverse 10s linear infinite; top: 15%; right: -100px; font-size: 65px; }

        /* --- DEFINISI ANIMASI --- */
        @keyframes moveAround {
            0% { transform: translate(0,0) rotate(0deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }
        @keyframes moveHorizontal {
            from { left: -100px; } to { left: 110vw; }
        }
        @keyframes moveHorizontalReverse {
            from { right: -100px; } to { right: 110vw; }
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
            background: rgba(5, 10, 15, 0.9);
            padding: 50px;
            border-radius: 20px;
            border: 2px solid #ff4b2b;
            box-shadow: 0 0 30px #ff4b2b;
        }

        div.stButton > button {
            background: linear-gradient(45deg, #ff4b2b, #ff416c);
            color: white !important;
            font-weight: bold;
            border-radius: 50px;
            padding: 12px 40px;
            border: none;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(255, 75, 43, 0.8);
        }
        </style>
        
        <div class="war-obj rocket-1">🚀</div>
        <div class="war-obj tank-1">🚜</div>
        <div class="war-obj missile-1">🚀</div>
        <div class="war-obj plane-1">✈️</div>

        <div class="center-box">
            <h1 style="color:white; font-size: 2.5rem;">🚨 SYSTEM BOMBARDIER!</h1>
            <p style="color: #ff416c; font-size: 1.2rem;">Lagi perbaikan database Supabase & GSheet, Cok!</p>
            <p style="color: #4facfe;">Harap tenang, roket lagi meluncur menuhin semua sudut.</p>
        </div>
    """, unsafe_allow_html=True)

    # Tombol Redirect
    st.link_button("🔥 KABUR KE KANTOR PUSAT", "https://pintar.streamlit.app/", use_container_width=True)

    st.stop()

halaman_digital_warfare()
