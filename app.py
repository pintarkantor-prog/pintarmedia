import streamlit as st

def halaman_maintenance_pro_final_banget():
    st.set_page_config(
        page_title="Pintar Media | Restricted",
        page_icon="🔐",
        layout="centered", 
        initial_sidebar_state="collapsed"
    )

    # --- CSS SNIPER: KUNCI MATI SEMUA DI TITIK TENGAH ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen sampah & garis sisa Streamlit */
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

        /* 3. WRAPPER UTAMA: POSISI TITIK TENGAH MUTLAK */
        .ultimate-center {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px; /* Jarak rapi antara kotak dan tombol */
            z-index: 99999;
            width: 450px; /* Kunci lebar biar gak melar kayak image_6c76eb */
        }

        /* 4. KOTAK TERMINAL (PROFESSIONAL LOOK) */
        .terminal-box {
            background: rgba(22, 27, 34, 0.95);
            padding: 45px;
            border: 1px solid rgba(100, 255, 218, 0.3);
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            text-align: center;
            width: 100%; 
            box-sizing: border-box;
        }

        /* 5. TOMBOL CUSTOM (SEWARNA LOGO PINTAR MEDIA - ANTI TEKS KODE) */
        .btn-main {
            display: block;
            width: 100%; /* Panjang persis sama dengan kotak (450px) */
            padding: 16px 0;
            /* Gradasi sewarna logo lo di image_6c73c2 */
            background: linear-gradient(90deg, #1e3a8a, #3b82f6, #ef4444); 
            color: white !important;
            border: none;
            border-radius: 8px;
            text-align: center;
            text-decoration: none !important;
            font-family: sans-serif;
            font-weight: bold;
            font-size: 14px;
            letter-spacing: 2px;
            text-transform: uppercase;
            transition: 0.3s all ease;
            cursor: pointer;
        }

        .btn-main:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5);
            filter: brightness(1.2);
        }

        /* Hapus sisa padding Streamlit yang bikin mojok */
        .block-container { padding: 0 !important; }
        </style>

        <div class="ultimate-center">
            <div class="terminal-box">
                <div style="color: #64ffda; font-family: monospace; letter-spacing: 3px; margin-bottom: 20px; font-size: 0.85rem; font-weight: bold;">
                    [ SYSTEM STATUS: ENCRYPTED ]
                </div>
                <h1 style="color: white; font-family: sans-serif; margin-bottom: 15px; font-size: 2rem; border: none; font-weight: 800;">
                    ACCESS RESTRICTED
                </h1>
                <p style="color: #8b949e; font-size: 1rem; line-height: 1.6; margin: 0;">
                    Database sedang dalam sinkronisasi berkala.<br>
                    Silakan gunakan jalur akses utama di bawah.
                </p>
            </div>
            
            <a href="https://pintar.streamlit.app/" style="text-decoration: none; width: 100%;">
                <div class="btn-main">RETURN TO MAIN SERVER</div>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_maintenance_pro_final_banget()
