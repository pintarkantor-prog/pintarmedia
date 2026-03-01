import streamlit as st

def halaman_maintenance_clean():
    st.set_page_config(
        page_title="Pintar Media | Restricted",
        page_icon="🔐",
        layout="centered", 
        initial_sidebar_state="collapsed"
    )

    # --- CSS SNIPER: KUNCI MATI KOTAK DI TENGAH ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen & padding bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Deep Space */
        .main {
            background-color: #0d1117 !important;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }

        /* 3. KUNCI MATI KOTAK DI TENGAH LAYAR (ANTI GESER) */
        .viewport-center {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 99999;
            width: 450px; /* Kunci lebar biar gak melar kayak spanduk */
        }

        /* 4. KOTAK TERMINAL (PROFESSIONAL LOOK) */
        .terminal-box {
            background: rgba(22, 27, 34, 0.98);
            padding: 50px;
            border: 1px solid rgba(100, 255, 218, 0.3);
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7);
            text-align: center;
            width: 100%; 
            box-sizing: border-box;
        }

        /* Sikat paksa padding container agar tidak mojok */
        .block-container { padding: 0 !important; }
        </style>

        <div class="viewport-center">
            <div class="terminal-box">
                <div style="color: #64ffda; font-family: monospace; letter-spacing: 5px; margin-bottom: 25px; font-size: 0.9rem; font-weight: bold;">
                    [ SYSTEM STATUS: ENCRYPTED ]
                </div>
                <h1 style="color: white; font-family: sans-serif; margin-bottom: 20px; font-size: 2.2rem; border: none; font-weight: 800; letter-spacing: 1px;">
                    ACCESS RESTRICTED
                </h1>
                <p style="color: #8b949e; font-size: 1.1rem; line-height: 1.8; margin: 0;">
                    Database sedang dalam sinkronisasi berkala untuk optimasi sistem.<br><br>
                    <span style="color: #64ffda; font-weight: bold;">AKSES DITUTUP SEMENTARA.</span>
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_maintenance_clean()
