import streamlit as st

def halaman_warzone_final_v3():
    st.set_page_config(
        page_title="Pintar Digital | Elite",
        page_icon="⚔️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: HAPUS SEMUA GARIS & KUNCI TOMBOL DI TENGAH ---
    st.markdown("""
        <style>
        /* 1. Hapus Header, Footer, & Garis Bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        /* 2. Background Full Gelap */
        .main {
            background-color: #010409 !important;
            height: 100vh !important;
            width: 100vw !important;
            overflow: hidden !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* 3. BENDERA BULAT KELILING */
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
        .id  { animation: patrol 16s infinite linear; }
        .cn  { animation: patrol 13s infinite linear reverse; }
        .ps  { animation: patrol 19s infinite linear; }

        /* 4. UNIT TEMPUR */
        .combat-unit { position: absolute; font-size: 50px; z-index: 2; animation: patrol 10s infinite linear; }

        /* 5. TOMBOL KECIL RGB - KUNCI MATI DI TENGAH */
        .absolute-center {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%); /* Rumus Tengah Mutlak */
            z-index: 9999;
            padding: 4px;
            border-radius: 50px;
            background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
            background-size: 400%;
            animation: rainbow_move 8s linear infinite;
            width: 220px; /* Lebar kecil sesuai request */
            display: flex;
            justify-content: center;
            align-items: center;
        }

        @keyframes rainbow_move {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }

        /* Styling Button Asli */
        .absolute-center div.stButton > button {
            background-color: #050a0f !important;
            color: #ffffff !important;
            border: none !important;
            width: 210px !important;
            border-radius: 50px !important;
            font-weight: bold !important;
            padding: 8px 0 !important;
            font-size: 14px !important;
            transition: 0.3s;
        }
        
        .absolute-center div.stButton > button:hover {
            color: #4facfe !important;
            transform: scale(1.05);
        }

        /* HAPUS SEMUA GARIS BAWAH (NO BORDER) */
        hr { display: none !important; }
        .stMarkdownContainer { border: none !important; }

        </style>
        
        <img src="https://flagcdn.com/w160/us.png" class="round-flag usa" style="top:5%; left:5%;">
        <img src="https://flagcdn.com/w160/il.png" class="round-flag isr" style="top:40%; right:5%;">
        <img src="https://flagcdn.com/w160/ir.png" class="round-flag ira" style="bottom:20%; left:15%;">
        <img src="https://flagcdn.com/w160/ru.png" class="round-flag rus" style="top:25%; right:20%;">
        <img src="https://flagcdn.com/w160/kp.png" class="round-flag nk" style="bottom:10%; right:15%;">
        <img src="https://flagcdn.com/w160/id.png" class="round-flag id" style="top:15%; left:40%;">
        <img src="https://flagcdn.com/w160/cn.png" class="round-flag cn" style="bottom:40%; right:30%;">
        <img src="https://flagcdn.com/w160/ps.png" class="round-flag ps" style="top:60%; left:10%;">
        
        <div class="combat-unit" style="top:30%; left:30%;">🚀</div>
        <div class="combat-unit" style="top:10%; left:70%; animation-delay: 2s%;">✈️</div>
        <div class="combat-unit" style="bottom:20%; right:20%; animation-delay: 4s;">🚀</div>
    """, unsafe_allow_html=True)

    # --- TOMBOL LOGIN (CENTRED ABSOLUTE) ---
    st.markdown('<div class="absolute-center">', unsafe_allow_html=True)
    st.link_button("🚀 LOGIN UTAMA", "https://pintar.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

halaman_warzone_final_v3()
