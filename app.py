import streamlit as st
import time
import sqlite3
import json
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
    adegan_json = json.dumps(adegans)
    c.execute("DELETE FROM produksi WHERE user=?", (user,))
    c.execute("INSERT INTO produksi (user, master_context, adegan_data) VALUES (?, ?, ?)", 
              (user, context, adegan_json))
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
# 2. TEMA GROK (DARK MINIMALIST) - MENGGUNAKAN ST.HTML
# ==============================================
def apply_grok_theme():
    # st.html adalah cara paling aman di versi terbaru untuk injeksi CSS
    st.html("""
        <style>
            .stApp { background-color: #000000 !important; color: #FFFFFF !important; }
            [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 1px solid #1F1F1F !important; }
            .stTextArea textarea { background-color: #0F0F0F !important; color: #FFFFFF !important; border: 1px solid #262626 !important; border-radius: 10px !important; }
            .stTextInput input { background-color: #0F0F0F !important; color: #FFFFFF !important; border: 1px solid #262626 !important; }
            div.stButton > button { background-color: #FFFFFF !important; color: #000000 !important; border-radius: 25px !important; font-weight: bold !important; width: 100%; border: none !important; }
            header { visibility: hidden; }
            footer { visibility: hidden; }
            .adegan-box { border: 1px solid #1F1F1F; padding: 15px; border-radius: 12px; margin-bottom: 20px; background-color: #050505; }
        </style>
    """)

# ==============================================
# 3. COMPONENT RUANG PRODUKSI
# ==============================================
def render_ruang_produksi():
    st.title("🚀 RUANG PRODUKSI")
    st.write("Kelola 10 Adegan YouTube Shorts Anda")
    
    # Master Context
    st.subheader("🧠 MASTER CONTEXT")
    st.session_state.master_ctx = st.text_area(
        "Konteks Karakter & Gaya Visual",
        value=st.session_state.get('master_ctx', ''),
        placeholder="Contoh: Style Animasi 3D, Udin kepala orange...",
        key="master_ctx_input",
        height=100
    )

    st.write("---")
    
    # 10 Adegan Generator
    for i in range(10):
        # Menggunakan container bawaan agar lebih stabil
        with st.container():
            st.write(f"### Adegan {i+1}")
            st.session_state.adegan_list[i] = st.text_area(
                f"Deskripsi Adegan {i+1}",
                value=st.session_state.adegan_list[i],
                key=f"scene_{i}",
                height=90,
                label_visibility="collapsed"
            )
            
            if st.button(f"Generate Prompt {i+1}", key=f"btn_gen_{i}"):
                final_p = f"MASTER STYLE: {st.session_state.master_ctx}\n\nSCENE DESCRIPTION: {st.session_state.adegan_list[i]}"
                st.code(final_p)
            st.write("---")

# ==============================================
# 4. SISTEM LOGIN & UTAMA
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

    if not st.session_state.logged_in:
        # Menghindari markdown HTML untuk judul login
        st.title("🧠 PINTAR AI LAB")
        u = st.text_input("Username", key="login_u")
        p = st.text_input("Password", type="password", key="login_p")
        
        if st.button("MASUK SISTEM"):
            if u == "admin" and p == "pintar2026":
                st.session_state.logged_in = True
                st.session_state.username = u
                st.session_state.login_time = time.time()
                st.rerun()
            else:
                st.error("Username atau Password salah")
    else:
        # Logout otomatis 10 jam
        if time.time() - st.session_state.login_time > 36000:
            st.session_state.logged_in = False
            st.rerun()

        # Proteksi Layar (Dijalankan hanya setelah login)
        width = st_javascript("window.innerWidth")
        if width is not None and width < 1024:
            st.warning("⚠️ RUANG PRODUKSI HANYA TERSEDIA DI DESKTOP.")
            st.stop()

        # Sidebar Navigasi
        with st.sidebar:
            st.title("PINTAR MEDIA")
            st.write(f"User: **{st.session_state.username}**")
            menu = st.radio("MENU", [
                "🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"
            ])
            
            st.write("---")
            if st.button("💾 SIMPAN DATA"):
                save_data(st.session_state.username, st.session_state.master_ctx, st.session_state.adegan_list)
                st.success("Tersimpan!")
            
            if st.button("📂 MUAT DATA"):
                res = load_data(st.session_state.username)
                if res:
                    st.session_state.master_ctx = res[0]
                    st.session_state.adegan_list = json.loads(res[1])
                    st.rerun()
            
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()

        # Route Halaman
        if menu == "🚀 RUANG PRODUKSI":
            render_ruang_produksi()
        else:
            st.title(menu)
            st.info("Fitur dalam pengembangan...")

# ==============================================
# 5. EKSEKUSI FINAL
# ==============================================
if __name__ == "__main__":
    init_db()
    main()
