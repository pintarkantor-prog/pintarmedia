import streamlit as st

def halaman_maintenance_ultimate():
    st.set_page_config(
        page_title="Pintar Media | Restricted",
        page_icon="🔐",
        layout="centered", 
        initial_sidebar_state="collapsed"
    )

    # --- THE NUCLEAR OPTION: RAW CSS & HTML ONLY ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen & padding bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Deep Space Tanpa Celah */
        .main {
            background-color: #0d1117 !important;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }

        /* 3. KUNCI MATI SEMUA DI TENGAH LAYAR (FIXED POSITION) */
        .viewport-center {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px; /* Jarak rapi antara kotak dan tombol */
            z-index: 99999;
            width: 450px; /* Kunci lebar biar gak melar */
        }

        /* 4. KOTAK TERMINAL (PROFESSIONAL LOOK) */
        .terminal-box {
            background: rgba(22, 27, 34, 0.98);
            padding: 45px;
            border: 1px solid rgba(100, 255, 218, 0.3);
            border-radius: 12px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
            text-align: center;
            width: 100%; 
            box-sizing: border-box;
        }

        /* 5. TOMBOL HTML MURNI (PANJANG SAMA 450px & SEWARNA LOGO) */
        .btn-redirect {
            display: block;
            width: 100%; /* Panjang persis sama dengan kotak */
            padding: 16px 0;
            /* Gradasi sewarna logo PINTAR MEDIA */
            background: linear-gradient(90deg, #1e3a8a, #3b82f6, #ef4444); 
            color: white !important;
            border: none;
            border-radius: 8px;
            text-align: center;
            text-decoration: none !important;
            font-family: sans-serif;
            font-weight: 800;
            font-size: 14px;
            letter-spacing: 2px;
            text-transform: uppercase;
            transition: 0.3s all ease;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
        }

        .btn-redirect:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(59, 130, 246, 0.5);
            filter: brightness(1.2);
        }

        /* Sikat paksa padding container agar tidak mojok */
        .block-container { padding: 0 !important; }
        </style>

        <div class="viewport-center">
            <div class="terminal-box">
                <div style="color: #64ffda; font-family: monospace; letter-spacing: 4px; margin-bottom: 20px; font-size: 0.85rem; font-weight: bold;">
                    [ SYSTEM STATUS: ENCRYPTED ]
                </div>
                <h1 style="color: white; font-family: sans-serif; margin-bottom: 15px; font-size: 2.1rem; border: none; font-weight: 800; letter-spacing: 1px;">
                    ACCESS RESTRICTED
                </h1>
                <p style="color: #8b949e; font-size: 1rem; line-height: 1.6; margin: 0;">
                    Database sedang dalam sinkronisasi berkala.<br>
                    Silakan gunakan jalur akses utama di bawah.
                </p>
            </div>
            
            <a href="https://pintar.streamlit.app/" class="btn-redirect">
                RETURN TO MAIN SERVER
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_maintenance_ultimate()
