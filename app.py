import streamlit as st

def halaman_neon_lockdown():
    st.set_page_config(
        page_title="Pintar Media | Restricted",
        page_icon="🔐",
        layout="centered", # Layout sempit biar gak melar kayak pecel lele
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: POSISI TENGAH MUTLAK & TOTAL TEAL NEON ---
    st.markdown("""
        <style>
        /* 1. Sikat habis semua elemen & padding bawaan Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Deep Space dengan Spotlight Biru Terang */
        .main {
            background: radial-gradient(circle at center, rgba(100, 255, 218, 0.25) 0%, #0d1117 100%) !important;
            height: 100vh !important;
            width: 100vw !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }

        /* 3. WRAPPER UTAMA (KUNCI MATI DI TITIK TENGAH) */
        .ultimate-center {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            z-index: 99999;
            width: 450px; /* Kunci lebar biar gak melar kayak image_6c76eb */
        }

        /* 4. KOTAK TERMINAL DENGAN NEON BREATHING GLOW */
        .terminal-neon-box {
            background: rgba(22, 27, 34, 0.98);
            padding: 50px;
            /* Border Neon Berdenyut */
            border: 2px solid rgba(100, 255, 218, 0.4);
            border-radius: 20px;
            box-shadow: 
                0 0 20px rgba(100, 255, 218, 0.2),
                inset 0 0 10px rgba(100, 255, 218, 0.1);
            text-align: center;
            width: 100%; /* Ngikutin wrapper 450px */
            box-sizing: border-box;
            /* Animasi Breathing Glow */
            animation: neon_breathe 8s ease-in-out infinite;
        }

        @keyframes neon_breathe {
            0%, 100% { 
                border-color: rgba(100, 255, 218, 0.4);
                box-shadow: 0 0 20px rgba(100, 255, 218, 0.2);
            }
            50% { 
                border-color: rgba(100, 255, 218, 0.8);
                box-shadow: 0 0 60px rgba(100, 255, 218, 0.6);
            }
        }

        /* 5. TEKS STATUS NEON (ANTI NORAK) */
        .neon-text-status {
            color: #64ffda;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            font-weight: bold;
            letter-spacing: 5px;
            margin-bottom: 25px;
            text-transform: uppercase;
            /* Neon Glow */
            text-shadow: 0 0 10px rgba(100, 255, 218, 0.8);
            /* Animasi Flicker ala hacker */
            animation: text_flicker 1s linear infinite;
        }

        @keyframes text_flicker {
            0%, 100% { opacity: 1; text-shadow: 0 0 10px rgba(100, 255, 218, 0.8); }
            50% { opacity: 0.8; text-shadow: 0 0 5px rgba(100, 255, 218, 0.4); }
        }

        /* 6. JUDUL NEON GLOW */
        .neon-title {
            color: white;
            font-family: sans-serif;
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: 2px;
            margin-bottom: 20px;
            text-transform: uppercase;
            text-shadow: 0 0 20px rgba(100, 255, 218, 0.6);
        }

        /* 7. DESKRIPSI (BERSIH & PRO) */
        .neon-desc {
            color: #8b949e;
            font-size: 1.1rem;
            line-height: 1.8;
            margin: 0;
            text-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
        }

        /* Sikat paksa padding container agar tidak mojok */
        .block-container { padding: 0 !important; }
        </style>

        <div class="ultimate-center">
            <div class="terminal-neon-box">
                <div class="neon-text-status">[ SYSTEM STATUS: SECURE ]</div>
                <h1 class="neon-title">ACCESS RESTRICTED</h1>
                <p class="neon-desc">
                    Database sedang dalam sinkronisasi berkala untuk optimasi sistem.<br>
                    <span style="color: #64ffda; font-weight: bold;">AKSES DITUTUP SEMENTARA COK.</span>
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_neon_lockdown()
