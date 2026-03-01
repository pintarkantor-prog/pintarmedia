import streamlit as st

def halaman_maintenance_ramadhan_estetik():
    st.set_page_config(page_title="Menyambut Ramadhan", page_icon="🌙", layout="centered")

    # --- CSS SAKTI BUAT TAMPILAN MODERN ---
    st.markdown("""
        <style>
        /* 1. Latar Belakang Gradasi biar Gak Polos */
        .main {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
        }
        
        /* 2. Style Judul Teal Modern */
        h1 {
            color: #008080 !important;
            text-align: center;
            font-family: 'Poppins', sans-serif; /* Pake font modern */
            font-weight: 700;
            margin-bottom: 30px;
        }
        
        /* 3. Style Gambar Pake Efek Card */
        div.stImage > img {
            border-radius: 20px; /* Sudut melengkung */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* Bayangan estetik */
            transition: transform 0.3s ease; /* Efek hover */
        }
        div.stImage > img:hover {
            transform: scale(1.02); /* Sedikit membesar pas di-hover */
        }
        
        /* 4. Style Peringatan (Warning) biar Gak Kaku */
        div.stAlert {
            border-radius: 15px;
            border: 1px solid #00acc1;
            background-color: white;
            color: #006064;
        }
        
        /* 5. Style Tombol Redirect Bulat Modern */
        stlinkbutton > a {
            background-color: #008080 !important;
            color: white !important;
            border-radius: 30px !important; /* Tombol bulat */
            padding: 10px 20px;
            font-weight: bold;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        stlinkbutton > a:hover {
            background-color: #006064 !important;
            transform: translateY(-3px); /* Tombol naik dikit pas di-hover */
        }
        
        </style>
        
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)
    
    # Bikin layout tengah (3 kolom, tengah paling lebar)
    _, col_tengah, _ = st.columns([1, 2, 1])
    
    with col_tengah:
        st.title("🌙 MARHABAN YA RAMADHAN")
        
        # Gambar Ramadhan Estetik (Cari link gambar yang resolusinya bagus)
        st.image("GANTI_Pake_LINK_GAMBAR_RAMADHAN_ESTETIK_LO_DI_SINI.jpg", caption="Semoga keberkahan menyertai kita semua.", use_container_width=True)
        
        st.warning("Mohon maaf, web Pintar Media lagi maintenance bentar!")
        
        st.info("Butuh akses cepat? Lo bisa akses kantor pusat dulu.")

        # Tombol Redirect Bulat (Capsule)
        st.link_button("🚀 BALIK KE KANTOR PUSAT", "https://pintar.streamlit.app/", use_container_width=True)
        
        st.divider()
        st.caption("Admin PT Pintar Digital Kreasi")

    st.stop() # Tetap pake ini biar kode bawahnya gak jalan

# Jalankan
halaman_maintenance_ramadhan_estetik()
