import streamlit as st

def halaman_maintenance_ramadhan():
    st.set_page_config(page_title="Menyambut Ramadhan", page_icon="🌙", layout="centered")

    # 1. CSS SAKTI BUAT LATAR BELAKANG (Biar adem)
    st.markdown("""
        <style>
        .main {
            background-color: #f0f8ff; /* Warna biru muda adem */
        }
        h1 {
            color: #008080 !important; /* Warna teal buat judul */
            text-align: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stButton>button {
            background-color: #008080; /* Warna tombol redirect biar seragam */
            color: white;
            border-radius: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    _, col_tengah, _ = st.columns([1, 2, 1])
    
    with col_tengah:
        st.title("🌙 MARHABAN YA RAMADHAN")
        
        # 2. GAMBAR RAMADHAN (Gue cariin yang estetik)
        # Lo bisa ganti link gambar ini pakai gambar lo sendiri kalau punya
        st.image("https://images.unsplash.com/photo-1596791697204-71239c065f97?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80", caption="Semoga keberkahan menyertai kita semua.", use_container_width=True)
        
        st.warning("Mohon maaf, web Pintar Media lagi maintenance bentar!")
        
        st.info("Sambil nunggu perbaikan, lo bisa akses kantor pusat dulu.")

        # 3. TOMBOL REDIRECT
        st.link_button("🚀 BALIK KE KANTOR PUSAT", "https://pintar.streamlit.app/", use_container_width=True)
        
        st.divider()
        st.caption("Admin PT Pintar Digital Kreasi")

    st.stop() # Tetap pake ini biar kode bawahnya gak jalan

halaman_maintenance_ramadhan()
