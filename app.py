def halaman_offline():
    st.set_page_config(page_title="Maintenance Mode", page_icon="🔧", layout="centered")

    # --- CSS SAKTI BUAT NGILANGIN ITEM ---
    st.markdown("""
        <style>
        .main {
            background-color: #ffffff; /* Maksa latar jadi putih */
        }
        h1, p, span {
            color: #1f1f1f !important; /* Maksa tulisan jadi item biar kebaca di layar putih */
        }
        div.stButton > button {
            background-color: #ff4b4b; /* Warna tombol redirect biar mencolok */
            color: white !important;
        }
        </style>
    """, unsafe_allow_value=True)
    
    _, col_tengah, _ = st.columns([1, 2, 1])
    
    with col_tengah:
        st.title("🔧 Web Lagi Maintenance, Cok!")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJndTRndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f3iwJFOVOwuy7K6FFw/giphy.gif")
        
        st.warning("Lagi ada perbaikan database Supabase & GSheet bentar ya!")
        
        # TOMBOL REDIRECT
        st.link_button("🚀 BALIK KE KANTOR PUSAT", "https://pintar.streamlit.app/", use_container_width=True)
        
        st.info("Pindah ke kantor pusat aja dulu kalau buru-buru.")

    st.stop()
