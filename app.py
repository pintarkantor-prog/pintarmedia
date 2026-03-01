import streamlit as st

def halaman_cyber_integrated():
    st.set_page_config(
        page_title="Pintar Digital | Restricted Access",
        page_icon="🔐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: INTEGRATED UI & CENTER LOCK ---
    st.markdown("""
        <style>
        /* Sikat semua elemen pengganggu Streamlit */
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
            width: 100vw !important;
            display: flex;
            flex-direction: column; /* Flow ke bawah */
            justify-content: center;
            align-items: center;
            margin: 0 !important;
        }

        /* Container Utama buat Box + Tombol */
        .ui-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px; /* Jarak rapi antara box dan tombol */
            z-index: 9999;
        }

        /* Box Terminal Central */
        .terminal-card {
            background: rgba(10, 25, 47, 0.95);
            padding: 40px;
            border: 1px solid #64ffda;
            border-radius: 4px;
            box-shadow: 0 0 40px rgba(100, 255, 218, 0.15);
            text-align: center;
            width: 420px;
        }

        .status-header {
            color: #64ffda;
            font-family: 'Courier New', monospace;
            font-size: 0.8rem;
            letter-spacing: 4px;
            margin-bottom: 20px;
        }

        /* Custom Button Style: Samain Nuansa */
        div.stButton > button {
            background-color: transparent !important;
            color: #64ffda !important;
            border: 1px solid #64ffda !important;
            border-radius: 4px !important;
            padding: 12px 30px !important;
            font-size: 13px !important;
            font-family: 'Courier New', monospace !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            letter-spacing: 2px !important;
            width: 300px !important; /* Buat tombol agak lebar biar gagah */
            transition: 0.4s ease;
        }

        div.stButton > button:hover {
            background-color: rgba(100, 255, 218, 0.1) !important;
            box-shadow: 0 0 20px rgba(100, 255, 218, 0.4);
            transform: translateY(-3px);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- RENDER UI DALAM SATU WRAPPER ---
    st.markdown('<div class="ui-wrapper">', unsafe_allow_html=True)
    
    # Bagian Box
    st.markdown("""
        <div class="terminal-card">
            <div class="status-header">[ STATUS: MAINTENANCE ]</div>
            <h1 style="color: white; font-family: sans-serif; letter-spacing: 2px; margin-bottom: 15px;">ACCESS RESTRICTED</h1>
            <p style="color: #8892b0; font-size: 0.9rem; line-height: 1.6;">
                Database sedang disinkronisasi untuk optimasi sistem.<br>
                Silakan kembali ke server utama.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Bagian Tombol (Persis di bawah)
    st.link_button("RETURN TO MAIN SERVER", "https://pintar.streamlit.app/")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

halaman_cyber_integrated()
