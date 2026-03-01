import streamlit as st

def halaman_warzone_final_paten():
    st.set_page_config(
        page_title="Pintar Digital | Secure Access",
        page_icon="🔐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: FORCE CENTER & NO GHOST ELEMENTS ---
    st.markdown("""
        <style>
        /* 1. Hapus SEMUA elemen sampah Streamlit & garis-garis sisa */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Grid Pro tanpa margin */
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
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* 3. WRAPPER UTAMA (KUNCI SEMUA DI TITIK TENGAH) */
        .master-center-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 25px; /* JARAK SPASI ANTARA BOX DAN TOMBOL */
            z-index: 9999;
        }

        /* 4. KOTAK TERMINAL (Lebar Fix 450px) */
        .terminal-box {
            background: rgba(10, 25, 47, 0.95);
            padding: 45px;
            border: 1px solid #64ffda; /* WARNA SEWARNA LOGO */
            border-radius: 4px;
            box-shadow: 0 0 40px rgba(100, 255, 218, 0.2);
            text-align: center;
            width: 450px; /* LEBAR PATEN */
        }

        /* 5. TOMBOL PANJANG (WAJIB 450px & SENADA) */
        div.stButton > button {
            background-color: transparent !important;
            color: #64ffda !important; /* WARNA SEWARNA LOGO */
            border: 1px solid #64ffda !important;
            border-radius: 4px !important;
            width: 450px !important; /* PANJANGNYA WAJIB SAMA DENGAN KOTAK */
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
            box-shadow: 0 0 25px #64ffda;
            color: #ffffff !important;
            border-color: #ffffff !important;
        }

        /* Hapus border container Streamlit yang bikin geser */
        .stMarkdownContainer { border: none !important; }
        [data-testid="stVerticalBlock"] { gap: 0 !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- RENDER UI (Satu Wrapper agar Presisi Mati di Tengah) ---
    st.markdown('<div class="master-center-wrapper">', unsafe_allow_html=True)
    
    # Render Kotak Pesan
    st.markdown("""
        <div class="terminal-box">
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

    # Render Tombol Persis di Bawah (Wajib Tengah & 450px)
    st.link_button("RETURN TO MAIN SERVER", "https://pintar.streamlit.app/")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

halaman_warzone_final_paten()
