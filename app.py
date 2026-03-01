def halaman_offline():
    st.set_page_config(page_title="Web Sedang Maintenance", page_icon="🔧")
    
    # Bikin layout tengah biar estetik
    _, col_tengah, _ = st.columns([1, 2, 1])
    
    with col_tengah:
        st.set_page_config(page_title="Web Sedang Istirahat", page_icon="🌙")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJndTRndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f3iwJFOVOwuy7K6FFw/giphy.gif")
        
        st.warning("Sabar ya, sistem lagi kita rapihin biar makin gacor.")
        st.info("Butuh akses cepat? Klik tombol di bawah buat balik ke web utama.")
        
        # --- INI TOMBOL REDIRECT-NYA ---
        st.link_button("🚀 BALIK KE KANTOR PUSAT", "https://pintar.streamlit.app/", use_container_width=True)
        
        st.divider()
        st.caption("Admin PT Pintar Digital Kreasi")

    st.stop() # Tetap pake ini biar kode bawahnya gak jalan
