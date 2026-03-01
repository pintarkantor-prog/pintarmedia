import streamlit as st

def halaman_war_zone_v2():
    st.set_page_config(
        page_title="Pintar Digital | Warzone v2",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: FULL PAGE, BUNDAR, FIXED FOOTER ---
    st.markdown("""
        <style>
        /* Hapus Header & Menu Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        .main {
            background-color: #020508;
            height: 100vh;
            overflow: hidden;
            position: relative;
            margin: 0; padding: 0;
        }

        /* --- STYLE BENDERA BULAT KELILING --- */
        .round-flag {
            position: absolute;
            width: 70px; height: 70px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
            z-index: 2;
        }

        /* --- STYLE UNIT TEMPUR --- */
        .combat-unit {
            position: absolute;
            font-size: 50px;
            z-index: 5;
            filter: drop-shadow(0 0 10px rgba(255, 0, 0, 0.5));
        }

        /* Animasi Keliling Halaman */
        @keyframes patrol {
            0% { transform: translate(0,0) rotate(0deg); }
            25% { transform: translate(85vw, 15vh) rotate(90deg); }
            50% { transform: translate(45vw, 85vh) rotate(180deg); }
            75% { transform: translate(-5vw, 45vh) rotate(270deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }

        /* Mapping Animasi Unit */
        .usa { animation: patrol 12s infinite linear; }
        .isr { animation: patrol 15s infinite linear reverse; }
        .ira { animation: patrol 20s infinite linear; }
        .rus { animation: patrol 18s infinite linear; }
        .nk  { animation: patrol 14s infinite linear reverse; }
        .indo { animation: patrol 16s infinite linear; }
        .chn { animation: patrol 13s infinite linear reverse; }
        .pal { animation: patrol 19s infinite linear; }

        /* Animasi Roket & Rudal Cepat */
        .fast-move { animation: patrol 8s infinite linear; }
        .med-move { animation: patrol 11s infinite linear reverse; }

        /* --- FOOTER PATEN (FIXED) --- */
        .fixed-footer {
            position: fixed;
            bottom: 0; left: 0;
            width: 100%;
            height: 10px;
            background: linear-gradient(90deg, #ff4b2b, #4facfe, #ff4b2b);
            box-shadow: 0 -5px 15px rgba(255, 75, 43, 0.5);
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
        
        <div class="combat-unit fast-move" style="top:50%; left:50%;">🚀</div>
        <div class="combat-unit fast-move" style="top:10%; left:70%; animation-delay: 2s;">✈️</div>
        <div class="combat-unit med-move" style="bottom:30%; left:40%; animation-delay: 1s;">🛸</div>
        <div class="combat-unit fast-move" style="top:80%; right:40%;">🚀</div>
        <div class="combat-unit med-move" style="top:20%; left:10%;">🛩️</div>
        <div class="combat-unit fast-move" style="bottom:10%; left:60%; animation-delay: 4s;">🚀</div>
        <div class="combat-unit med-move" style="top:50%; right:10%;">🛸</div>

        <div class="fixed-footer"></div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_war_zone_v2()
