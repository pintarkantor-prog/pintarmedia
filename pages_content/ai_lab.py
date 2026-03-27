import streamlit as st

def tampilkan_halaman():
    st.title("🧠 PINTAR AI LAB")
    st.write("Selamat datang di pusat eksperimen AI PINTAR MEDIA.")
    st.divider()
    
    # Contoh konten (Bisa kamu isi dengan kode AI Lab lamamu nanti)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🤖 Prompt Generator")
        st.text_area("Masukkan Ide Konten...", placeholder="Misal: Kisah Nabi Sulaiman...")
        st.button("Generate Script ⚡", use_container_width=True)
        
    with col2:
        st.subheader("📜 Hasil Script")
        st.info("Script AI akan muncul di sini setelah di-generate.")
