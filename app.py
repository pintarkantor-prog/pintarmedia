import streamlit as st

def halaman_cyber_pro():
    st.set_page_config(
        page_title="Pintar Digital | Restricted Access",
        page_icon="🔐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: GRID DIGITAL & CENTER LOCK ---
    st.markdown("""
        <style>
        /* Sikat semua elemen pengganggu dan garis 'njir' */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* Background Grid Digital Pro */
        .main {
            background-color: #050a0f !important;
            background-image: 
                linear-gradient(rgba(100, 255, 218, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(100, 255, 218, 0.05) 1px, transparent 1px);
            background-size: 30px 30px;
            height: 100vh !important;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 !important;
        }

        /* Container Box Tengah */
        .terminal-box {
            position: fixed;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            z-index: 9999;
            background: rgba(10, 25, 47, 0.9);
            padding: 40px;
            border: 1px solid #64ffda;
            border-radius: 4px; /* Sudut tegas biar pro */
            box-shadow: 0 0 30px rgba(100, 255, 218, 0.2);
            text-align: center;
            width: 380px;
        }

        .status-tag {
            color: #64ffda;
            font-family: 'Courier New', monospace;
            font-size: 0.8rem;
            letter-spacing: 3px;
            margin-bottom: 15px;
        }

        /* Tombol Kecil Gacor */
        .btn-container {
            margin-top: 25px;
        }

        div.stButton > button {
            background-color: #64ffda !important;
            color: #0a192f !important;
            border: none !important;
            border-radius: 2px !important;
            padding: 8px 20px !important;
            font-size: 13px !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            letter-spacing: 1px;
            width: auto !important;
            transition: 0.3s;
        }

        div.stButton > button:hover {
            box-shadow: 0 0 15px #64ffda;
            transform: translateY(-2px);
        }
        </style>
        
        <div class="terminal-box">
            <div class="status-tag">[ STATUS: MAINTENANCE ]</div>
            <h2 style="color: white; font-family: sans-serif; margin: 10px 0;">ACCESS RESTRICTED</h2>
            <p style="color: #8892b0; font-size: 0.9rem;">Database sedang disinkronisasi. Silakan kembali ke server utama untuk melanjutkan pekerjaan.</p>
        </div>
    """, unsafe_allow_html=True)

    # --- TOMBOL REDIRECT (TETEP DI TENGAH) ---
    st.markdown('<div style="position: fixed; top: 65%; left: 50%; transform: translate(-50%, -50%); z-index: 10000;">', unsafe_allow_html=True)
    st.link_button("RETURN TO MAIN SERVER", "https://pintar.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

halaman_cyber_pro()
