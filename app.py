import streamlit as st

def halaman_cyber_war():
    st.set_page_config(
        page_title="CYBER WARFARE | PINTAR DIGITAL",
        page_icon="⚔️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS: ANIMASI PERANG CYBER ---
    st.markdown("""
        <style>
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        .main {
            background-color: #050505;
            height: 100vh;
            overflow: hidden;
            position: relative;
        }

        /* OBJEK PERANG KELILING */
        .cyber-unit {
            position: absolute;
            font-size: 50px;
            filter: drop-shadow(0 0 10px currentColor);
        }

        /* Fraksi Cyan (Cyber Defender) */
        .cyan-unit { color: #00f2fe; animation: moveRight 8s linear infinite; top: 10%; }
        /* Fraksi Magenta (System Breaker) */
        .magenta-unit { color: #ff00ff; animation: moveLeft 12s linear infinite; bottom: 15%; }
        /* Rudal antar Fraksi */
        .bolt { font-size: 30px; animation: moveDiagonal 4s linear infinite; }

        @keyframes moveRight {
            from { left: -100px; } to { left: 110vw; }
        }
        @keyframes moveLeft {
            from { right: -100px; } to { right: 110vw; }
        }
        @keyframes moveDiagonal {
            from { top: -50px; left: -50px; transform: rotate(45deg); }
            to { top: 110vh; left: 110vw; transform: rotate(45deg); }
        }

        /* CENTER BOX GACOR */
        .status-box {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            z-index: 100;
            background: rgba(0, 0, 0, 0.8);
            padding: 40px;
            border: 2px solid #00f2fe;
            border-radius: 20px;
            box-shadow: 0 0 40px #00f2fe;
        }

        .glitch {
            color: white;
            font-size: 2.5rem;
            font-weight: bold;
            text-transform: uppercase;
            position: relative;
            display: inline-block;
        }

        div.stButton > button {
            background: linear-gradient(45deg, #00f2fe, #ff00ff);
            color: white !important;
            font-weight: bold;
            border-radius: 50px;
            border: none;
            padding: 15px 40px;
        }
        </style>
        
        <div class="cyber-unit cyan-unit">🛸</div>
        <div class="cyber-unit cyan-unit" style="top:40%; animation-delay: 2s;">📡</div>
        <div class="cyber-unit magenta-unit">👾</div>
        <div class="cyber-unit bolt" style="color:red;">⚡</div>

        <div class="status-box">
            <div class="glitch">SYSTEM UNDER REPAIR</div>
            <p style="color: #00f2fe; margin-top: 15px;">Lagi "perang" benerin database Supabase, Cok!</p>
            <p style="color: #888;">Data sedang dire-organisasi agar tidak double lagi.</p>
        </div>
    """, unsafe_allow_html=True)

    # Tombol Redirect
    st.link_button("🔥 KABUR KE WEB UTAMA", "https://pintar.streamlit.app/", use_container_width=True)

    st.stop()

halaman_cyber_war()
