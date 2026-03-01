import streamlit as st

def halaman_perang_bulat_asli():
    st.set_page_config(
        page_title="Pintar Digital | Cyber Warfare Round",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: HAPUS HEADER & BIKIN FULL PAGE ---
    st.markdown("""
        <style>
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
            width: 80px; height: 80px; /* Ukuran pas buat icon bulatan */
            z-index: 1;
            /* Tambah glow dikit biar keren di background gelap */
            filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.3));
        }

        /* Animasi Keliling Halaman (Random Path) */
        @keyframes patrol {
            0% { transform: translate(0,0) rotate(0deg); }
            25% { transform: translate(80vw, 15vh) rotate(90deg); }
            50% { transform: translate(45vw, 85vh) rotate(180deg); }
            75% { transform: translate(-5vw, 45vh) rotate(270deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }

        /* Set animasi beda-beda biar gak barengan */
        .usa-round { animation: patrol 10s infinite linear; top: 10%; left: 5%; }
        .isr-round { animation: patrol 14s infinite linear reverse; top: 40%; right: 10%; }
        .ira-round { animation: patrol 18s infinite linear; bottom: 10%; left: 20%; }
        .rus-round { animation: patrol 16s infinite linear; top: 20%; right: 30%; }
        .nk-round  { animation: patrol 12s infinite linear reverse; bottom: 20%; right: 20%; }
        
        .rocket-obj { position: absolute; font-size: 55px; animation: patrol 8s infinite linear; z-index: 2; }
        
        /* FOOTER PATEN (FIXED) DI BAWAH */
        .fixed-footer {
            position: fixed;
            bottom: 0; left: 0;
            width: 100%;
            height: 12px;
            background: linear-gradient(90deg, #ff4b2b, #4facfe, #ff4b2b);
            border-top: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 -5px 20px rgba(0, 242, 254, 0.4);
            z-index: 999;
        }
        </style>
        
        <img src="https://img.icons8.com/?size=100&id=16301&format=png&color=000000" class="round-flag usa-round"> <img src="https://img.icons8.com/?size=100&id=16279&format=png&color=000000" class="round-flag isr-round"> <img src="https://img.icons8.com/?size=100&id=16278&format=png&color=000000" class="round-flag ira-round"> <img src="https://img.icons8.com/?size=100&id=16300&format=png&color=000000" class="round-flag rus-round"> <img src="https://img.icons8.com/?size=100&id=t74F8fXU0u4S&format=png&color=000000" class="round-flag nk-round">  <div class="rocket-obj" style="top:50%; left:50%;">🚀</div>
        <div class="rocket-obj" style="top:25%; right:25%; animation-delay: 3s;">✈️</div>

        <div class="fixed-footer"></div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_perang_bulat_asli()
