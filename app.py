import streamlit as st

def halaman_perang_kota_paten():
    st.set_page_config(
        page_title="Pintar Digital | City Defense",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: BENDERA BULAT + FOOTER KOTA FULL ---
    st.markdown("""
        <style>
        /* Hapus Header & Menu Streamlit biar Full Screen */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        .main {
            background-color: #020508; /* Langit Malam Gelap */
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
            z-index: 1;
        }

        /* Animasi Keliling Halaman */
        @keyframes patrol {
            0% { transform: translate(0,0) rotate(0deg); }
            25% { transform: translate(80vw, 15vh) rotate(90deg); }
            50% { transform: translate(40vw, 60vh) rotate(180deg); }
            75% { transform: translate(-5vw, 40vh) rotate(270deg); }
            100% { transform: translate(0,0) rotate(360deg); }
        }

        .usa { animation: patrol 12s infinite linear; }
        .isr { animation: patrol 15s infinite linear reverse; }
        .ira { animation: patrol 20s infinite linear; }
        .rus { animation: patrol 18s infinite linear; }
        .nk  { animation: patrol 14s infinite linear reverse; }
        .rocket { position: absolute; font-size: 50px; animation: patrol 10s infinite linear; z-index: 2; }

        /* --- FOOTER KOTA PATEN (FIXED) --- */
        .city-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 250px; /* Tinggi gambar kota */
            /* Menggunakan gambar siluet kota digital */
            background-image: url('https://www.transparenttextures.com/patterns/carbon-fibre.png'), 
                              linear-gradient(to top, rgba(2, 5, 8, 1) 10%, rgba(2, 5, 8, 0) 100%),
                              url('https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=1600&auto=format&fit=crop');
            background-size: cover;
            background-position: bottom;
            background-repeat: no-repeat;
            z-index: 5;
            border-top: 2px solid #4facfe;
            box-shadow: 0 -10px 30px rgba(79, 172, 254, 0.5);
            opacity: 0.8; /* Biar benderanya tetep kelihatan pas di belakang gedung */
        }
        </style>
        
        <img src="https://flagcdn.com/w160/us.png" class="round-flag usa" style="top:10%; left:5%;">
        <img src="https://flagcdn.com/w160/il.png" class="round-flag isr" style="top:30%; right:10%;">
        <img src="https://flagcdn.com/w160/ir.png" class="round-flag ira" style="top:20%; left:20%;">
        <img src="https://flagcdn.com/w160/ru.png" class="round-flag rus" style="top:15%; right:30%;">
        <img src="https://flagcdn.com/w160/kp.png" class="round-flag nk" style="top:40%; right:15%;">
        
        <div class="rocket" style="top:25%; left:50%;">🚀</div>
        <div class="rocket" style="top:10%; left:70%; animation-delay: 3s;">✈️</div>

        <div class="city-footer"></div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_perang_kota_paten()
