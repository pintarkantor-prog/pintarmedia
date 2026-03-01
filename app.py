import streamlit as st

def halaman_warzone_final_bersih():
    st.set_page_config(
        page_title="Pintar Digital | Warzone",
        page_icon="⚔️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: PURE CENTER, NO LINES, RGB GLOW ---
    st.markdown("""
        <style>
        /* Sembunyiin Header & Menu Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        /* Bikin background full gelap dan tombol di tengah */
        .main {
            background-color: #010409;
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0; padding: 0;
            position: relative;
        }

        /* --- BENDERA BULAT KELILING (EFEK GLOW) --- */
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

        /* Mapping Animasi Bendera */
        .usa { animation: patrol 12s infinite linear; }
        .isr { animation: patrol 15s infinite linear reverse; }
        .ira { animation: patrol 20s infinite linear; }
        .rus { animation: patrol 18s infinite linear; }
        .nk  { animation: patrol 14s infinite linear reverse; }
        .id  { animation: patrol 16s infinite linear; }
        .cn  { animation: patrol 13s infinite linear reverse; }
        .ps  { animation: patrol 19s infinite linear; }

        /* --- UNIT TEMPUR --- */
        .combat-unit { position: absolute; font-size: 50px; z-index: 2; animation: patrol 10s infinite linear; }

        /* --- CONTAINER TOMBOL LOGIN RGB (FIXED CENTER) --- */
        .login-box-center {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 9999;
            padding: 5px;
            border-radius: 50px;
            /* Efek Pelangi Muter */
            background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
            background-size: 400%;
            animation: rainbow_move 10s linear infinite;
            box-shadow: 0 0 30px rgba(0, 242, 254, 0.6);
            width: 230px; /* Ukuran tombol kecil */
            display: flex;
            justify-content: center;
        }

        @keyframes rainbow_move {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }

        /* Styling Button Asli Streamlit */
        .login-box-center div.stButton > button {
            background-color: #050a0f !important;
            color: #ffffff !important;
            border: none !important;
            width: 220px !important;
            border-radius: 50px !important;
            font-weight: bold !important;
            padding: 10px 0 !important;
            font-size: 14px !important;
            letter-spacing: 1px;
            transition: 0.3s;
        }
        
        .login-box-center div.stButton > button:hover {
            color: #4facfe !important;
            transform: scale(1.05);
        }

        /* --- HAPUS GARIS BAWAH (NO FOOTER) --- */
        </style>
        
        <img src="https://flagcdn.com/w160/us.png" class="round-flag usa" style="top:5%; left:5%;">
        <img src="https://flagcdn.com/w160/il.png" class="round-flag isr" style="top:40%; right:5%;">
        <img src="https://flagcdn.com/w160/ir.png" class="round-flag ira" style="bottom:20%; left:15%;">
        <img src="https://flagcdn.com/w160/ru.png" class="round-flag rus" style="top:25%; right:20%;">
        <img src="https://flagcdn.com/w160/kp.png" class="round-flag nk" style="bottom:10%; right:15%;">
        <img src="https://flagcdn.com/w160/id.png" class="round-flag id" style="top:15%; left:40%;">
        <img src="https://flagcdn.com/w160/cn.png" class="round-flag cn" style="bottom:40%; right:30%;">
        <img src="https://flagcdn.com/w160/ps.png" class="round-flag ps" style="top:60%; left:10%;">
        
        <div class="combat-unit" style="top:50%; left:50%;">🚀</div>
        <div class="combat-unit" style="top:10%; left:70%; animation-delay: 2s;">✈️</div>
    """, unsafe_allow_html=True)

    # --- TOMBOL LOGIN KERAMAT (CENTERED) ---
    st.markdown('<div class="login-box-center">', unsafe_allow_html=True)
    st.link_button("🚀 LOGIN UTAMA", "https://pintar.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

halaman_warzone_final_bersih()
