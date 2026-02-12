import streamlit as st

# Pengaturan halaman agar terlihat bersih
st.set_page_config(page_title="Prompt Generator", layout="centered")

st.title("✨ My Prompt Generator")
st.caption("Rancang prompt di sini, lalu tempelkan ke Gemini.")

# Sidebar untuk parameter (opsional)
with st.sidebar:
    st.header("Pengaturan")
    gaya_bahasa = st.selectbox("Gaya Bahasa", ["Formal", "Santai", "Kreatif"])

# Area Input Utama
topik = st.text_input("Apa yang ingin kamu buat?", placeholder="Contoh: Skrip film pendek Udin & Tung")

if topik:
    # Logika Penggabungan Prompt (Template)
    prompt_hasil = f"Halo Gemini, tolong buatkan {topik} dengan gaya bahasa {gaya_bahasa}. Pastikan hasilnya detail dan kreatif."
    
    # Menampilkan hasil dengan gaya chat
    st.markdown("### 📝 Hasil Prompt:")
    st.code(prompt_hasil, language="text")
    
    st.info("Klik ikon di pojok kanan atas kotak teks di atas untuk menyalin!")
