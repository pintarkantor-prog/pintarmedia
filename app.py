import streamlit as st

def halaman_war_bendera():
    st.set_page_config(
        page_title="Pintar Digital | GLOBAL WAR",
        page_icon="⚔️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: BENDERA & PESAWAT KELILING ---
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
        }

        /* STYLE OBJEK KELILING */
        .obj-war {
            position: absolute;
            width: 80px; /* Ukuran bendera & pesawat */
            z-index: 1;
            filter: drop-shadow(0 0 10px rgba(255,255,255,0.2));
        }

        /* Animasi Berputar-putar Menuhin Layar */
        @keyframes patrol {
            0% { transform: translate(0,0) rotate(0deg); }
            25% { transform: translate(80vw, 20vh) rotate(90deg); }
            50% { transform: translate(40vw, 80vh) rotate(180deg); }
            75% { transform: translate(-10vw, 40vh) rotate(270deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }

        .usa { animation: patrol 12s infinite linear; }
        .israel { animation: patrol 15s infinite linear reverse; }
        .iran { animation: patrol 20s infinite linear; }
        .rocket { animation: patrol 8s infinite linear; font-size: 50px; text-align:center; }

        /* CENTER BOX */
        .center-box {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            z-index: 100;
            background: rgba(0, 0, 0, 0.85);
            padding: 40px;
            border: 2px solid #ff4b2b;
            border-radius: 20px;
            box-shadow: 0 0 30px #ff4b2b;
            color: white;
        }
        </style>
        
        <img src="https://flagcdn.com/w160/us.png" class="obj-war usa" style="top:10%; left:10%;">
        <img src="https://flagcdn.com/w160/il.png" class="obj-war israel" style="top:40%; right:10%;">
        <img src="https://flagcdn.com/w160/ir.png" class="obj-war iran" style="bottom:10%; left:30%;">
        
        <div class="obj-war rocket" style="top:50%; left:50%;">🚀</div>
        <div class="obj-war rocket" style="top:20%; right:30%; animation-delay: 2s;">✈️</div>

        <div class="center-box">
            <h1 style="font-size: 2.5rem; margin-bottom: 0;">GLOBAL MAINTENANCE</h1>
            <p style="color: #ff4b2b; font-weight: bold; letter-spacing: 2px;">WEB LAGI OFF, PINDAH KE PUSAT!</p>
            <p style="color: #4facfe;">Lagi sinkronisasi database antar negara, Cok.</p>
        </div>
    """, unsafe_allow_html=True)

    # Tombol Redirect Gacor
    st.link_button("🔥 MELUNCUR KE KANTOR PUSAT", "https://pintar.streamlit.app/", use_container_width=True)

    st.stop()

halaman_war_bendera()
