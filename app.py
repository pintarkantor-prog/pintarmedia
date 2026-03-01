import streamlit as st

def halaman_warzone_final_paten():
    st.set_page_config(
        page_title="Pintar Digital | Secure Access",
        page_icon="🔐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: POSISI MATI DI TENGAH ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen sampah Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Grid Pro */
        .main {
            background-color: #050a0f !important;
            background-image: 
                linear-gradient(rgba(100, 255, 218, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(100, 255, 218, 0.05) 1px, transparent 1px);
            background-size: 30px 30px;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }

        /* 3. KOTAK TERMINAL (KUNCI MATI DI TENGAH) */
        .terminal-lock {
            position: fixed;
            top: 45%; /* Naik dikit biar tombol di bawahnya pas di tengah */
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 999;
            background: rgba(10, 25, 47, 0.95);
            padding: 45px;
            border: 1px solid #64ffda;
            border-radius: 4px;
            box-shadow: 0 0 40px rgba(100, 255, 218, 0.2);
            text-align: center;
            width: 450px; /* Lebar Paten */
        }

        /* 4. TOMBOL (KUNCI MATI DI BAWAH KOTAK) */
        .button-lock {
            position: fixed;
            top: calc(45% + 185px); /* Posisi tepat di bawah kotak (45% + setengah tinggi kotak + spasi) */
            left: 50%;
            transform: translate(-50%, 0);
            z-index: 1000;
            width: 450px; /* LEBAR WAJIB SAMA DENGAN KOTAK */
        }

        /* Styling Button agar sewarna dan rapi */
        div.stButton > button {
            background-color: transparent !important;
            color: #64ffda !important;
            border: 1px solid #64ffda !important;
            border-radius: 4px !important;
            width: 100% !important; /* Ngikutin container 450px */
            padding: 15px 0 !important;
            font-size: 14px !important;
            font-family: 'Courier New', monospace !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            letter-spacing: 3px !important;
            transition: 0.3s;
        }

        div.stButton > button:hover {
            background-color: rgba(100, 255, 218, 0.1) !important;
            box-shadow: 0 0 20px #64ffda;
            color: #fff !important;
        }

        /* Hapus border container Streamlit */
        .stMarkdownContainer { border: none !important; }
        </style>
        
        <div class="terminal-lock">
            <div style="color: #64ffda; font-family: monospace; letter-spacing: 4px; margin-bottom: 20px; font-size: 0.85rem;">
                [ STATUS: MAINTENANCE ]
            </div>
            <h1 style="color: white; font-family: sans-serif; letter-spacing: 2px; margin-bottom: 15px; font-size: 2rem;">
                ACCESS RESTRICTED
            </h1>
            <p style="color: #8892b0; font-size: 0.95rem; line-height: 1.6;">
                Sistem sedang dalam sinkronisasi database berkala.<br>
                Silakan gunakan jalur akses utama di bawah ini.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- RENDER TOMBOL (DIPAKSA KE POSISI LOCK) ---
    st.markdown('<div class="button-lock">', unsafe_allow_html=True)
    st.link_button("RETURN TO MAIN SERVER", "https://pintar.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

halaman_warzone_final_paten()
