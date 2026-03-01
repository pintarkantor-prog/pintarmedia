import streamlit as st

def halaman_visual_only():
    st.set_page_config(
        page_title="Pintar Digital | Visual Mode",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: HAPUS SEMUA TEKS/TOMBOL & BIKIN FULL ANIMASI ---
    st.markdown("""
        <style>
        /* Hapus elemen bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        .main {
            background-color: #020508;
            height: 100vh;
            overflow: hidden;
            position: relative;
            margin: 0;
            padding: 0;
        }

        /* --- STYLE OBJEK KELILING --- */
        .obj-war {
            position: absolute;
            width: 80px;
            z-index: 1;
            filter: drop-shadow(0 0 15px rgba(255,255,255,0.3));
        }

        /* Animasi Keliling Halaman (Random Path) */
        @keyframes patrol {
            0% { transform: translate(0,0) rotate(0deg); }
            25% { transform: translate(85vw, 15vh) rotate(90deg); }
            50% { transform: translate(45vw, 85vh) rotate(180deg); }
            75% { transform: translate(-5vw, 45vh) rotate(270deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }

        /* Variasi Kecepatan & Delay biar Rame */
        .usa { animation: patrol 12s infinite linear; top: 5%; left: 5%; }
        .israel { animation: patrol 18s infinite linear reverse; top: 50%; right: 10%; }
        .iran { animation: patrol 22s infinite linear; bottom: 5%; left: 30%; }
        .rocket { animation: patrol 9s infinite linear; font-size: 60px; top: 40%; left: 45%; }
        .plane { animation: patrol 14s infinite linear reverse; font-size: 55px; top: 70%; right: 30%; }

        </style>
        
        <img src="https://flagcdn.com/w160/us.png" class="obj-war usa">
        <img src="https://flagcdn.com/w160/il.png" class="obj-war israel">
        <img src="https://flagcdn.com/w160/ir.png" class="obj-war iran">
        
        <div class="obj-war rocket">🚀</div>
        <div class="obj-war plane">✈️</div>
        <div class="obj-war rocket" style="animation-delay: 3s; top: 20%; right: 20%;">🚀</div>
        <div class="obj-war plane" style="animation-delay: 5s; bottom: 20%; left: 10%;">✈️</div>
    """, unsafe_allow_html=True)

    # Berhenti di sini, tidak ada st.title atau st.link_button
    st.stop()

halaman_visual_only()
