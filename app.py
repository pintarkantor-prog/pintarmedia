import streamlit as st
import base64

def halaman_offline_horor():
    st.set_page_config(page_title="HIIIIII....", page_icon="👻")

    # 1. LINK MUSIK KUNTI (Cari link .mp3 yang direct)
    # Gue pake contoh link suara horor umum, lo bisa ganti link-nya sendiri
    music_url = "https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Ghost+Laugh&filename=24/244342-8356f91a-7096-419b-a7e8-07e5c6a3f4e1.mp3"

    # 2. INJECT AUDIO AUTO-PLAY (Pake trik Iframe biar auto-start)
    st.markdown(
        f"""
        <iframe src="{music_url}" allow="autoplay" style="display:none" id="iframeAudio">
        </iframe>
        <audio autoplay loop>
            <source src="{music_url}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

    # 3. TAMPILAN MAINTENANCE
    st.markdown("""
        <style>
        .main { background-color: #000000; } /* Maksa item lagi biar serem */
        h1, p { color: #ff0000 !important; text-align: center; } /* Tulisan merah darah */
        </style>
    """, unsafe_allow_html=True)

    st.title("👻 JANGAN BUKA WEB INI MALAM-MALAM...")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJndTRndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LpALgGQzqA0C0/giphy.gif") # GIF Kunti/Hantu
    
    st.warning("Web Pintar Media lagi maintenance, mending lo balik ke kantor pusat sekarang!")
    
    # TOMBOL REDIRECT TETEP ADA BIAR MEREKA BISA KABUR
    st.link_button("🏃 KABUR KE KANTOR PUSAT!", "https://pintar.streamlit.app/", use_container_width=True)

    st.stop()

# Jalankan
halaman_offline_horor()
