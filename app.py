import streamlit as st

def halaman_final_pasti_tengah():
    st.set_page_config(
        page_title="Pintar Digital | Secure Access",
        page_icon="🔐",
        layout="centered", # Gue ganti ke centered biar gak maruk layar
        initial_sidebar_state="collapsed"
    )

    # --- JURUS SNIPER: KUNCI MATI SEMUA ELEMEN ---
    st.markdown("""
        <style>
        /* 1. Hapus total semua sampah Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Grid Profesional */
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

        /* 3. WRAPPER ABSOLUT: GAK BAKAL BISA GESER */
        .force-center {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
            z-index: 99999;
            width: 450px; /* KUNCI LEBAR BIAR GAK MELAR KAYAK IMAGE_6C76EB */
        }

        /* 4. KOTAK TERMINAL */
        .terminal-box {
            background: rgba(10, 25, 47, 0.98);
            padding: 40px;
            border: 1px solid #64ffda; /* WARNA TEAL PRO */
            border-radius: 4px;
            box-shadow: 0 0 30px rgba(100, 255, 218, 0.15);
            text-align: center;
            width: 450px; /* HARUS SAMA DENGAN WRAPPER */
            box-sizing: border-box;
        }

        /* 5. TOMBOL CUSTOM HTML (BIAR GAK PAKE ST.BUTTON YANG SUKA MOJOK) */
        .btn-link {
            display: block;
            width: 450px; /* LEBAR PERSIS SAMA DENGAN KOTAK */
            padding: 15px 0;
            background: transparent;
            color: #64ffda !important;
            border: 1px solid #64ffda;
            border-radius: 4px;
            text-align: center;
            text-decoration: none !important;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            font-size: 14px;
            letter-spacing: 2px;
            transition: 0.3s all;
            box-sizing: border-box;
        }

        .btn-link:hover {
            background: rgba(100, 255, 218, 0.1);
            box-shadow: 0 0 20px rgba(100, 255, 218, 0.4);
            color: #fff !important;
            border-color: #fff;
        }

        /* Sikat sisa padding container Streamlit */
        .block-container { padding: 0 !important; }
        </style>

        <div class="force-center">
            <div class="terminal-box">
                <div style="color: #64ffda; font-family: monospace; letter-spacing: 3px; margin-bottom: 15px; font-size: 0.8rem;">
                    [ STATUS: MAINTENANCE ]
                </div>
                <h1 style="color: white; font-family: sans-serif; letter-spacing: 2px; margin-bottom: 15px; font-size: 1.8rem; border:none;">
                    ACCESS RESTRICTED
                </h1>
                <p style="color: #8892b0; font-size: 0.9rem; line-height: 1.6; margin:0;">
                    Sistem sedang dalam sinkronisasi database berkala.<br>
                    Silakan gunakan jalur akses utama di bawah ini.
                </p>
            </div>
            
            <a href="https://pintar.streamlit.app/" class="btn-link">
                RETURN TO MAIN SERVER
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_final_pasti_tengah()
