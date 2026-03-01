import streamlit as st

def halaman_pro_fix_total():
    st.set_page_config(
        page_title="Pintar Digital | Secure Access",
        page_icon="🔐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS SAKTI: CENTER LOCK, EQUAL WIDTH, & MATCHING COLOR ---
    st.markdown("""
        <style>
        /* 1. Hapus SEMUA elemen pengganggu & garis sisa */
        [data-testid="stHeader"], [data-testid="stSidebar"], footer, hr {
            display: none !important;
        }
        
        /* 2. Background Full Screen dengan Grid Tipis */
        .main {
            background-color: #050a0f !important;
            background-image: 
                linear-gradient(rgba(100, 255, 218, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(100, 255, 218, 0.05) 1px, transparent 1px);
            background-size: 30px 30px;
            height: 100vh !important;
            width: 100vw !important;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* 3. Container Utama (Box + Tombol) */
        .master-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px; /* Spasi jarak antara kotak dan tombol */
            z-index: 9999;
        }

        /* 4. Kotak Terminal (Ukuran Fix 450px) */
        .terminal-box {
            background: rgba(10, 25, 47, 0.95);
            padding: 45px;
            border: 1px solid #64ffda; /* Warna senada gambar */
            border-radius: 4px;
            box-shadow: 0 0 40px rgba(100, 255, 218, 0.15);
            text-align: center;
            width: 450px; /* Lebar Kotak */
        }

        .status-tag {
            color: #64ffda;
            font-family: 'Courier New', monospace;
            font-size: 0.85rem;
            letter-spacing: 4px;
            margin-bottom: 20px;
        }

        /* 5. Tombol Panjang Senada (Matching Width & Color) */
        div.stButton > button {
            background-color: transparent !important;
            color: #64ffda !important; /* Warna senada teks gambar */
            border: 1px solid #64ffda !important;
            border-radius: 4px !important;
            padding: 15px 0 !important;
            font-size: 14px !important;
            font-family: 'Courier New', monospace !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            letter-spacing: 3px !important;
            width: 450px !important; /* PANJANGNYA SAMA DENGAN KOTAK */
            transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        div.stButton > button:hover {
            background-color: rgba(100, 255, 218, 0.1) !important;
            box-shadow: 0 0 25px rgba(100, 255, 218, 0.4);
            transform: translateY(-3px);
            color: #ffffff !important;
            border-color: #ffffff !important;
        }

        /* Hilangkan Border Container Streamlit */
        .stMarkdownContainer { border: none !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- RENDER UI (Satu Wrapper agar Presisi) ---
    st.markdown('<div class="master-wrapper">', unsafe_allow_html=True)
    
    # Kotak Pesan
    st.markdown("""
        <div class="terminal-box">
            <div class="status-tag">[ STATUS: MAINTENANCE ]</div>
            <h1 style="color: white; font-family: sans-serif; letter-spacing: 2px; margin-bottom: 15px; font-size: 2rem;">ACCESS RESTRICTED</h1>
            <p style="color: #8892b0; font-size: 0.95rem; line-height: 1.6;">
                Sistem sedang dalam sinkronisasi database berkala.<br>
                Silakan gunakan jalur akses utama di bawah ini.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Tombol Persis di Bawah (Lebar Sama)
    st.link_button("RETURN TO MAIN SERVER", "https://pintar.streamlit.app/")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

halaman_pro_fix_total()
