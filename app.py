import streamlit as st

def halaman_perang_bulat_paten():
    st.set_page_config(
        page_title="Pintar Digital | Elite Zone",
        page_icon="🎖️",
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
            border-radius: 50%; /* Bikin bulet sempurna */
            object-fit: cover;
            border: 2px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
            z-index: 1;
        }

        /* Animasi Keliling Halaman */
        @keyframes patrol {
            0% { transform: translate(0,0) rotate(0deg); }
            25% { transform: translate(80vw, 20vh) rotate(90deg); }
            50% { transform: translate(40vw, 80vh) rotate(180deg); }
            75% { transform: translate(-5vw, 40vh) rotate(270deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }

        /* Set animasi beda-beda biar gak barengan */
        .usa { animation: patrol 12s infinite linear; }
        .isr { animation: patrol 15s infinite linear reverse; }
        .ira { animation: patrol 20s infinite linear; }
        .rus { animation: patrol 18s infinite linear; }
        .nk  { animation: patrol 14s infinite linear reverse; }
        .rocket { position: absolute; font-size: 50px; animation: patrol 10s infinite linear; z-index: 2; }

        /* --- FOOTER PATEN (FIXED) --- */
        .fixed-footer {
            position: fixed;
            bottom: 0; left: 0;
            width: 100%;
            height: 10px;
            background: linear-gradient(90deg, #ff4b2b, #4facfe, #ff4b2b);
            border-top: 1px solid rgba(255,255,255,0.3);
            box-shadow: 0 -5px 15px rgba(255, 75, 43, 0.5);
            z-index: 999;
        }
        </style>
        
        <img src="https://i.pinimg.com/1200x/d0/3f/c4/d03fc4bdc00b3ae0495ef44b7a2314f8.jpg" class="round-flag usa" style="top:10%; left:5%;">
        <img src="https://i.pinimg.com/1200x/b3/88/56/b38856c8ca883b56acb40df11beb562e.jpg" style="top:40%; right:10%;">
        <img src="https://flagcdn.com/w160/ir.png" class="round-flag ira" style="bottom:20%; left:20%;">
        <img src="https://i.pinimg.com/736x/1f/3a/04/1f3a04018de63ce5e03526571aaa6f5d.jpg" style="top:20%; right:30%;">
        <img src="https://flagcdn.com/w160/kp.png" class="round-flag nk" style="bottom:10%; right:15%;">
        
        <div class="rocket" style="top:50%; left:50%;">🚀</div>
        <div class="rocket" style="top:20%; left:70%; animation-delay: 3s;">✈️</div>

        <div class="fixed-footer"></div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_perang_bulat_paten()


