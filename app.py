import streamlit as st

def halaman_final_lockdown():
    st.set_page_config(
        page_title="Pintar Digital | Secure Access",
        page_icon="🔐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: POSISI MATI DI TITIK TENGAH ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen sampah & garis sisa */
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

        /* 3. WRAPPER UTAMA (KUNCI MATI DI TENGAH LAYAR) */
        .absolute-center-wrapper {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px; /* JARAK SPASI ANTARA BOX DAN TOMBOL */
            z-index: 99999;
            width: 450px; /* LEBAR FIX PENYELARAS */
        }

        /* 4. KOTAK TERMINAL (Lebar Fix 450px) */
        .terminal-box {
            background: rgba(10, 25, 47, 0.95);
            padding: 45px;
            border: 1px solid #64ffda; /* WARNA SEWARNA LOGO */
            border-radius: 4px;
            box-shadow: 0 0 40px rgba(100, 255, 218, 0.15);
            text-align: center;
            width: 100%; /* Ngikutin wrapper 450px */
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
            transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        div.stButton > button:hover {
            background-color: rgba(100, 255, 218, 0.1) !important;
            box-shadow: 0 0 25px #64ffda;
            color: #ffffff !important;
            border-color: #ffffff !important;
            transform: translateY(-3px);
        }

        /* Hapus semua padding bawaan Streamlit yang bikin geser */
        .block-container { padding: 0 !important; }
        .stMarkdownContainer { border: none !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- RENDER SEMUA DALAM SATU WRAPPER ABSOLUT ---
    st.markdown('<div class="absolute-center-wrapper">', unsafe_allow_html=True)
    
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

halaman_final_lockdown()
