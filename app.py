import streamlit as st

def halaman_offline_kunti():
    st.set_page_config(page_title="HIIIIII....", page_icon="👻")

    # Link suara kunti/horor (Pastikan link mp3 ini aktif)
    music_url = "https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Ghost+Laugh&filename=24/244342-8356f91a-7096-419b-a7e8-07e5c6a3f4e1.mp3"

    st.markdown("""
        <style>
        .main { background-color: #000000; }
        h1 { color: #ff0000 !important; text-align: center; font-family: 'Courier New', Courier, monospace; }
        </style>
    """, unsafe_allow_html=True)

    st.title("👻 WEB LAGI OFF, COK!")
    
    # --- TRIK BARU: TOMBOL PANCINGAN ---
    st.write("### ⚠️ Klik tombol di bawah buat cek status server...")
    
    if st.button("🔴 CEK STATUS SERVER (KLIK DI SINI)"):
        # Begitu diklik, musik baru bisa muter
        st.markdown(
            f"""
            <audio autoplay loop>
                <source src="{music_url}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True
        )
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJndTRndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LpALgGQzqA0C0/giphy.gif")
        st.error("MAU KEMANA LO?! BALIK KE KANTOR PUSAT SANA!")
        
        st.link_button("🏃 KABUR KE KANTOR PUSAT!", "https://pintar.streamlit.app/", use_container_width=True)

    st.stop()

halaman_offline_kunti()
