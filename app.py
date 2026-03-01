import streamlit as st

# --- KONFIGURASI SAKLAR ---
# Lo bisa ganti ini jadi False kalau mau web-nya ON lagi
web_sedang_perbaikan = True 

def halaman_offline():
    st.set_page_config(page_title="Web Sedang Istirahat", page_icon="🌙")
    
    # Bikin tampilan tengah (Centered)
    empty1, col_tengah, empty2 = st.columns([1, 2, 1])
    
    with col_tengah:
        st.title("🌙 Web Lagi Off, Cok!")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndTRndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndXJndSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f3iwJFOVOwuy7K6FFw/giphy.gif") # GIF lucu biar gak pada nangis
        st.warning("Gue lagi benerin sesuatu di dalem. Sabar ya, jangan nangis dulu!")
        st.info("Estimasi kelar: Bentar lagi, kalau nggak ketiduran.")
        
        if st.button("Coba Cek Lagi"):
            st.rerun()
    
    st.stop() # PAKSA SISTEM BERHENTI DI SINI

# --- EKSEKUSI SAKLAR ---
if web_sedang_perbaikan:
    halaman_offline()

# --- KODE ASLI WEB LO DI BAWAH SINI ---
st.title("Web Utama Lo")
st.write("Kalau lo liat ini, berarti saklarnya lagi OFF.")
