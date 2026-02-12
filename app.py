import streamlit as st
import time
import sqlite3
from streamlit_javascript import st_javascript

# ==============================================
# 1. DATABASE ENGINE
# ==============================================
def init_db():
    conn = sqlite3.connect('pintar_media.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS produksi 
                 (id INTEGER PRIMARY KEY, user TEXT, master_context TEXT, adegan_data TEXT)''')
    conn.commit()
    conn.close()

def save_data(user, context, adegans):
    conn = sqlite3.connect('pintar_media.db')
    c = conn.cursor()
    c.execute("DELETE FROM produksi WHERE user=?", (user,))
    c.execute("INSERT INTO produksi (user, master_context, adegan_data) VALUES (?, ?, ?)", 
              (user, context, str(adegans)))
    conn.commit()
    conn.close()

def load_data(user):
    conn = sqlite3.connect('pintar_media.db')
    c = conn.cursor()
    c.execute("SELECT master_context, adegan_data FROM produksi WHERE user=?", (user,))
    data = c.fetchone()
    conn.close()
    return data

# ==============================================
# 2. TEMA GROK (DARK MINIMALIST) - FIXED VERSION
# ==============================================
def apply_grok_theme():
    st.markdown("""
<style>
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 1px solid #1F1F1F !important; }
    .stTextArea>div>div>textarea { background-color: #0F0F0F !important; color: #FFFFFF !important; border: 1px solid #262626 !important; border-radius: 12px !important; }
    .stTextInput>div>div>input { background-color: #0F0F0F !important; color: #FFFFFF !important; border: 1px solid #262626 !important; border-radius: 8px !important; }
    .stButton>button { background-color: #FFFFFF !important; color: #000000 !important; border-radius: 25px !important; font-weight: 600 !important; border: none !important; height: 45px !important; width: 100% !important; }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stExpander"] { background-color: #0A0A0A !important; border: 1px solid #1F1F1F !important; border-radius: 15px !important; }
    .adegan-card { background-color: #0A0A0A; padding: 15px; border-radius: 15px; border: 1px solid #1F1F1F; margin-bottom: 15px; }
</style>
""", unsafe_content_html=True)

# ==============================================
# 3. HALAMAN LOGIN
# ==============================================
def render_login():
    st.markdown("<div style='height:80px'></div>", unsafe_content_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h1 style='text-align:center; letter-spacing:3px;'>PINTAR AI LAB</h1>", unsafe_content_html=True)
        st.markdown("<p style='text-align:center; color:#888;'>Silakan login untuk mengakses Ruang Produksi</p>", unsafe_content_html=True)
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("Masuk Ke Sistem"):
            if user == "admin" and pw == "pintar2026":
                st.session_state.logged_in = True
                st.session_state.username = user
                st.session_state.login_time = time.time()
                st.rerun()
            else:
                st.error("Username atau Password salah.")

# ==============================================
# 4. HALAMAN RUANG PRODUKSI (DEFAULT)
# ==============================================
def render_ruang_produksi():
    st.markdown("## 🚀 RUANG PRODUKSI")
    st.caption("Fokus pada 10 Adegan Konsisten untuk YouTube Shorts")
    
    # Master Context
    with st.expander("🧠 MASTER CONTEXT (Definisikan Karakter & Gaya Visual)", expanded=True):
        st.session_state.master_ctx = st.text_area(
            "Detail Karakter & Style", 
            value=st.session_state.get('master_ctx', ''),
            placeholder="Contoh: Style Animasi 3D Pixar, Karakter Udin kepala orange, baju hijau, lighting sinematik...",
            height=100
        )

    st.write("---")
    
    # Daftar 10 Adegan
    for i in range(10):
        st.markdown(f"<div class='adegan-card'>", unsafe_content_html=True)
        col_idx, col_input = st.columns([1, 9])
        
        with col_idx:
            st.markdown(f"<h3 style='color:#555; text-align:center;'>{i+1}</h3>", unsafe_content_html=True)
        
        with col_input:
            st.session_state.adegan_list[i] = st.text_area(
                f"Deskripsi Adegan {i+1}", 
                value=st.session_state.adegan_list[i],
                key=f"sc_{i}", height=90, label_visibility="collapsed",
                placeholder=f"Tulis alur cerita adegan {i+1} di sini..."
            )
            
            if st.button(f"Generate Prompt {i+1}", key=f"btn_{i}"):
                full_p = f"**MASTER STYLE:** {st.session_state.master_ctx}\n\n**SCENE DESCRIPTION:** {st.session_state.adegan_list[i]}"
                st.code(full_p)
        st.markdown("</div>", unsafe_content_html=True)

# ==============================================
# 5. KONTROL UTAMA
# ==============================================
def main():
    apply_grok_theme()
    
    # Inisialisasi Session State
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'adegan_list' not in st.session_state:
        st.session_state.adegan_list = [""] * 10
    if 'master_ctx' not in st.session_state:
        st.session_state.master_ctx = ""

    # Cek Login
    if not st.session_state.logged_in:
        render_login()
    else:
        # Cek Durasi Login 10 Jam
        if time.time() - st.session_state.login_time > 36000:
            st.session_state.logged_in = False
            st.rerun()

        # Proteksi Layar HP
        width = st_javascript("window.innerWidth")
        if width is not None and width < 1024:
            st.warning("⚠️ RUANG PRODUKSI HANYA UNTUK DESKTOP.")
            st.stop()

        # Sidebar Navigasi
        with st.sidebar:
            st.markdown("<h2 style='letter-spacing: 2px;'>PINTAR MEDIA</h2>", unsafe_content_html=True)
            st.write(f"User: **{st.session_state.username}**")
            menu = st.radio("NAVIGASI", [
                "🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"
            ])
            
            st.write("---")
            if st.button("💾 SIMPAN KE DATABASE"):
                save_data(st.session_state.username, st.session_state.master_ctx, st.session_state.adegan_list)
                st.success("Tersimpan!")
                
            if st.button("📂 MUAT DATA LAMA"):
                res = load_data(st.session_state.username)
                if res:
                    st.session_state.master_ctx = res[0]
                    st.session_state.adegan_list = eval(res[1])
                    st.rerun()
            
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()

        # Tampilkan Menu
        if menu == "🚀 RUANG PRODUKSI":
            render_ruang_produksi()
        else:
            st.title(menu)
            st.info("Fitur dalam pengembangan...")

if __name__ == "__main__":
    init_db()
    main()
