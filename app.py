import streamlit as st

def halaman_offline_kunti():
    st.set_page_config(page_title="HIIIIII....", page_icon="👻")

    # LINK BARU (Gue cariin yang direct link MP3)
    # Ini link suara tertawa horor
    music_url = "https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Ghost+Laugh&filename=24/244342-8356f91a-7096-419b-a7e8-07e5c6a3f4e1.mp3" # <- Link ini tadi mati
    
    # Pake link alternatif dari koleksi open source (Horror Ambience)
    alt_music_url = "https://www.soundjay.com/misc/sounds/horror-ambience-1.mp3"

    st.markdown("""
        <style>
        .main { background-color: #000000; }
        h1 { color: #ff0000 !important; text-align: center; }
        .stButton>button { background-color: #4b0082; color: white; border-radius: 20px; }
        </style>
    """, unsafe_allow_html=True)

    st.title("👻 WEB LAGI MAINTENANCE, COK!")
    
    st.write("### ⚠️ Klik tombol di bawah buat cek status server...")
    
    # Tombol pancingan buat izin browser
    if st.button("🔴 CEK KONEKSI DATABASE"):
        # Play music
        st.markdown(
            f"""
            <audio autoplay loop>
                <source src="{alt_music_url}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True
        )
        
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJndTRndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LpALgGQzqA0C0/giphy.gif")
        st.error("DATABASE LAGI DIHUNI KUNTI, COK! BALIK KE KANTOR PUSAT AJA!")
        
        st.link_button("🏃 KABUR KE KANTOR PUSAT!", "https://pintar.streamlit.app/", use_container_width=True)
    else:
        st.info("Jangan kaget kalau ada suara aneh ya...")

    st.stop()

halaman_offline_kunti()
