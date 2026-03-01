import streamlit as st

def halaman_equalizer_digital():
    # 1. Set Page Config biar Full Page & Title Keren
    st.set_page_config(
        page_title="Pintar Digital | Toning Proses",
        page_icon="⚡",
        layout="wide", # Pake wide biar full
        initial_sidebar_state="collapsed" # Sembunyiin sidebar
    )

    # 2. CSS SAKTI: Hancurin Header Streamlit, Bikin Equalizer & Full Background
    st.markdown("""
        <style>
        /* Sembunyiin elemen bawaan Streamlit biar Full Page */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        .embedded-container {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Latar Belakang Digital Dark */
        .main {
            background-color: #0a0e17; /* Biru tua gelap banget ala server */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #00f2fe; /* Warna teks cyan digital */
            font-family: 'Courier New', Courier, monospace; /* Font kode */
            overflow: hidden;
        }
        
        /* Container Utama Tengah */
        .digital-container {
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* --- ANIMASI EQUALIZER CSS --- */
        .equalizer {
            display: flex;
            justify-content: space-between;
            width: 100px;
            height: 60px;
            margin-bottom: 30px;
        }
        .bar {
            width: 15px;
            height: 100%;
            background: linear-gradient(to top, #00c6ff, #00f2fe);
            border-radius: 3px;
            animation: equalize 1s ease-in-out infinite;
        }
        /* Variasi animasi tiap bar biar dinamis */
        .bar:nth-child(1) { animation-delay: 0.0s; }
        .bar:nth-child(2) { animation-delay: 0.1s; }
        .bar:nth-child(3) { animation-delay: 0.2s; }
        .bar:nth-child(4) { animation-delay: 0.3s; }
        
        @keyframes equalize {
            0%, 100% { transform: scaleY(1); }
            50% { transform: scaleY(0.4); }
        }

        /* Style Teks Modern ala Hacker */
        .status-text {
            font-size: 1.5rem;
            margin-bottom: 10px;
            letter-spacing: 2px;
        }
        .sub-text {
            font-size: 1rem;
            color: #4facfe;
            margin-bottom: 30px;
        }

        /* Style Tombol Redirect Bulat Gacor */
        div.stButton > button {
            background: linear-gradient(45deg, #00c6ff, #4facfe);
            color: white !important;
            border-radius: 30px !important;
            padding: 12px 30px;
            font-weight: bold;
            border: none;
            transition: all 0.3s ease;
            letter-spacing: 1px;
            box-shadow: 0 5px 15px rgba(0, 242, 254, 0.4);
        }
        div.stButton > button:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 8px 20px rgba(0, 242, 254, 0.6);
        }

        </style>
    """, unsafe_allow_html=True)

    # 3. Struktur HTML & Teks Digital (Inject langsung pake markdown)
    st.markdown("""
        <div class="digital-container">
            <div class="equalizer">
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
            </div>
            
            <div class="status-text">SYSTEM STATUS: MAINTENANCE</div>
            <div class="sub-text">WEB SEDANG DI-TUNING ULANG, COK! BENTAR YAA..</div>
        </div>
    """, unsafe_allow_html=True)

    # 4. Tombol Redirect Tetap Pake Streamlit (Biar Gampang)
    st.link_button("🚀 PINDAH KE WEB UTAMA", "https://pintar.streamlit.app/", use_container_width=True)

    # 5. Pasang Stoper biar kode bawah gak jalan
    st.stop()

halaman_equalizer_digital()
