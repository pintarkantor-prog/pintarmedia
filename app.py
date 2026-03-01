import streamlit as st

def halaman_global_digital():
    st.set_page_config(
        page_title="Pintar Digital | Global Access",
        page_icon="🌐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: BENDERA MELAYANG KELILING ---
    st.markdown("""
        <style>
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        .main {
            background-color: #0a0e17; /* Dark Blue Digital */
            height: 100vh;
            overflow: hidden;
            position: relative;
        }

        /* --- STYLE BENDERA MELAYANG --- */
        .flag-obj {
            position: absolute;
            font-size: 50px;
            filter: drop-shadow(0 0 10px rgba(255,255,255,0.3));
            z-index: 1;
        }

        /* Animasi Keliling Halaman */
        @keyframes floatAround {
            0% { transform: translate(0, 0) rotate(0deg); }
            25% { transform: translate(70vw, 20vh) rotate(10deg); }
            50% { transform: translate(40vw, 70vh) rotate(-10deg); }
            75% { transform: translate(-10vw, 40vh) rotate(5deg); }
            100% { transform: translate(0, 0) rotate(0deg); }
        }

        .flag-us { animation: floatAround 15s infinite linear; top: 10%; left: 10%; }
        .flag-il { animation: floatAround 18s infinite linear reverse; top: 50%; left: 80%; }
        .flag-ir { animation: floatAround 20s infinite linear; bottom: 10%; left: 30%; }

        /* CENTER BOX */
        .center-box {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            z-index: 10;
            background: rgba(15, 23, 42, 0.9);
            padding: 40px;
            border-radius: 25px;
            border: 1px solid #00f2fe;
            box-shadow: 0 0 50px rgba(0, 242, 254, 0.2);
        }

        .status-text {
            color: #00f2fe;
            font-family: 'Courier New', monospace;
            letter-spacing: 3px;
            font-weight: bold;
        }

        div.stButton > button {
            background: linear-gradient(45deg, #00c6ff, #0072ff);
            color: white !important;
            border-radius: 50px;
            padding: 10px 40px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 20px #00f2fe;
        }
        </style>
        
        <div class="flag-obj flag-us">🇺🇸</div>
        <div class="flag-obj flag-il">🇮🇱</div>
        <div class="flag-obj flag-ir">🇮🇷</div>

        <div class="center-box">
            <h1 style="color:white; margin-bottom:10px;">GLOBAL MAINTENANCE</h1>
            <p class="status-text">SYNCING INTERNATIONAL SERVERS...</p>
            <p style="color:#64748b; margin-bottom:30px;">Web ini lagi istirahat, Cok. Pindah ke pusat dulu!</p>
        </div>
    """, unsafe_allow_html=True)

    # Tombol Redirect
    st.link_button("🚀 PINDAH KE PINTAR.APP", "https://pintar.streamlit.app/", use_container_width=True)

    st.stop()

halaman_global_digital()
