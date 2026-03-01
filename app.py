import streamlit as st

def halaman_warzone_final_kecil():
    st.set_page_config(
        page_title="Pintar Digital | Warzone",
        page_icon="⚔️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: FULL PAGE, BUNDAR, TOMBOL KECIL RGB ---
    st.markdown("""
        <style>
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        .main {
            background-color: #010409;
            height: 100vh;
            overflow: hidden;
            position: relative;
            margin: 0; padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* --- BENDERA BULAT KELILING --- */
        .round-flag {
            position: absolute;
            width: 70px; height: 70px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
            z-index: 1;
        }

        @keyframes patrol {
            0% { transform: translate(0,0) rotate(0deg); }
            25% { transform: translate(80vw, 20vh) rotate(90deg); }
            50% { transform: translate(40vw, 80vh) rotate(180deg); }
            75% { transform: translate(-5vw, 40vh) rotate(270deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }

        .usa { animation: patrol 12s infinite linear; }
        .isr { animation: patrol 15s infinite linear reverse; }
        .ira { animation: patrol 20s infinite linear; }
        .rus { animation: patrol 18s infinite linear; }
        .nk  { animation: patrol 14s infinite linear reverse; }
        .indo { animation: patrol 16s infinite linear; }
        .chn { animation: patrol 13s infinite linear reverse; }
        .pal { animation: patrol 19s infinite linear; }

        /* --- UNIT TEMPUR --- */
        .combat-unit { position: absolute; font-size: 50px; z-index: 2; }
        .fast { animation: patrol 8s infinite linear; }

        /* --- CONTAINER TOMBOL KECIL RGB --- */
        .login-wrapper {
            z-index: 100;
            width: 260px; /* KITA KUNCI LEBARNYA DI SINI COK */
            padding: 4px;
            border-radius: 50px; /* Biar bentuknya kapsul */
            background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
            background-size: 400%;
            animation: rainbow_move 10s linear infinite;
            box-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
        }

        @keyframes rainbow_move {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }

        /* Bikin Tombol Streamlit-nya jadi Transparan di dalem Container RGB */
        div.stButton > button {
            background-color: #050a0f !important;
            color: #ffffff !important;
            border: none !important;
            width: 100% !important;
            border-radius: 50px !important;
            font-weight: bold !important;
            padding: 10px 20px !important;
            letter-spacing: 1px;
        }

        div.stButton > button:hover {
            color: #4facfe !important;
            transform: scale(1.02);
        }

        /* --- FOOTER PATEN --- */
        .fixed-footer {
            position: fixed;
            bottom: 0; left: 0;
            width: 100%;
            height: 10px;
            background: linear-gradient(90deg, #ff4b2b, #4facfe, #ff4b2b);
            z-index: 999;
        }
        </style>
        
        <img src="https://flagcdn.com/w160/us.png" class="round-flag usa" style="top:5%; left:5%;">
        <img src="https://flagcdn.com/w160/il.png" class="round-flag isr" style="top:40%; right:5%;">
        <img src="https://flagcdn.com/w160/ir.png" class="round-flag ira" style="bottom:20%; left:15%;">
        <img src="https://flagcdn.com/w160/ru.png" class="round-flag rus" style="top:25%; right:20%;">
        <img src="https://flagcdn.com/w160/kp.png" class="round-flag nk" style="bottom:10%; right:15%;">
        <img src="https://flagcdn.com/w160/id.png" class="round-flag indo" style="top:15%; left:40%;">
        <img src="https://flagcdn.com/w160/cn.png" class="round-flag chn" style="bottom:40%; right:30%;">
        <img src="https://flagcdn.com/w160/ps.png" class="round-flag pal" style="top:60%; left:10%;">
        
        <div class="combat-unit fast" style="top:50%; left:50%;">🚀</div>
        <div class="combat-unit fast" style="top:10%; left:70%; animation-delay: 2s;">✈️</div>

        <div class="fixed-footer"></div>
    """, unsafe_allow_html=True)

    # --- TOMBOL LOGIN KECIL DI TENGAH ---
    _, col_tengah, _ = st.columns([1, 1, 1]) # Pake kolom biar makin mantap di tengah
    with col_tengah:
        st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
        st.link_button("🚀 LOGIN UTAMA", "https://pintar.streamlit.app/")
        st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

halaman_warzone_final_kecil()
