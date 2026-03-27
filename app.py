import streamlit as st

# 1. Konfigurasi Awal
st.set_page_config(page_title="PINTAR MEDIA v2.0", page_icon="🖼️", layout="centered")

# 2. Fungsi Cek Login (Simpel dulu, nanti kita sambung ke Supabase)
def login():
    st.image("PINTAR.png", width=200)
    st.title("🔐 Login PINTAR MEDIA")
    
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    
    if st.button("Masuk Sekarang"):
        # Kita buat password sementara dulu ya biar kamu bisa ngetes
        if user == "admin" and pw == "pintar2026":
            st.session_state["authenticated"] = True
            st.success("Login Berhasil! Silakan pilih menu di samping.")
            st.rerun()
        else:
            st.error("Username atau Password Salah, Dian!")

# 3. Logika Tampilan
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
    # Bagian ini penting: Kita hentikan proses di sini kalau belum login
    st.stop() 

# 4. Kalau sudah login, tampilkan Dashboard Utama
st.sidebar.success("Logged in as Admin")
st.title("🏠 Dashboard Utama PINTAR MEDIA")
st.write(f"Selamat datang kembali, Bos Dian! Semua sistem siap dijalankan.")

# Kasih ringkasan singkat di sini
col1, col2 = st.columns(2)
col1.metric("Status Server", "Online", "Stable")
col2.metric("Total HP", "25 Units", "Connected")
