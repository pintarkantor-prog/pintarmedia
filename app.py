import streamlit as st

def halaman_war_bersih():
    st.set_page_config(
        page_title="Pintar Digital | Global",
        page_icon="🌍",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: BERSIHIN TOTAL & TOMBOL KECIL ---
    st.markdown("""
        <style>
        /* Hapus Header & Footer Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        .main {
            background-color: #050a0f;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            position: relative;
        }

        /* --- OBJEK BENDERA KELILING --- */
        .obj-war {
            position: absolute;
            width: 70px;
            z-index: 1;
            filter: drop-shadow(0 0 8px rgba(255,255,255,0.2));
            animation: patrol 15s infinite linear;
        }

        @keyframes patrol {
            0% { transform: translate(0,0) rotate(0deg); }
            50% { transform: translate(70vw, 50vh) rotate(180deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }

        /* --- BOX TENGAH --- */
        .center-box {
            text-align: center;
            z-index: 100;
            background: rgba(0, 0, 0, 0.9);
            padding: 30px;
            border: 2px solid #ff4b2b;
            border-radius: 20px;
            box-shadow: 0 0 25px rgba(255, 75, 43, 0.5);
            width: 400px; /* Ukuran box fix biar nggak meler */
        }

        h1 { color: white; font-size: 2rem !important; margin-bottom: 5px !important; }
        .sub-text { color: #ff4b2b; font-weight: bold; margin-bottom: 20px; }

        /* --- TOMBOL KECIL DI TENGAH --- */
        .stElementContainer div.stButton {
            display: flex;
            justify-content: center;
        }
        
        div.stButton > button {
            background: #ff4b2b !important;
            color: white !important;
            border-radius: 10px !important;
            padding: 5px 20px !important; /* Perkecil ukuran */
            font-size: 14px !important;
            width: auto !important; /* Nggak usah panjang-panjang */
            border: none !important;
        }
        </style>
        
        <img src="https://flagcdn.com/w160/us.png" class="obj-war" style="top:10%; left:10%; animation-duration: 12s;">
        <img src="https://flagcdn.com/w160/il.png" class="obj-war" style="top:40%; right:10%; animation-duration: 18s;">
        <img src="https://flagcdn.com/w160/ir.png" class="obj-war" style="bottom:10%; left:30%; animation-duration: 15s;">
        <div class="obj-war" style="top:70%; right:20%; font-size: 40px;">🚀</div>

        <div class="center-box">
            <h1>GLOBAL MAINTENANCE</h1>
            <div class="sub-text">WEB OFF - SINKRONISASI DATABASE</div>
        </div>
    """, unsafe_allow_html=True)

    # Tombol kecil di tengah
    st.link_button("🚀 Balik Ke Pusat", "https://pintar.streamlit.app/")

    st.stop()

halaman_war_bersih()
