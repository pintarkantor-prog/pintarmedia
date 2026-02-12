import streamlit as st
import time
import sqlite3
import json
from streamlit_javascript import st_javascript

# ==============================================
# 1. DATABASE ENGINE
# ==============================================
def init_db():
    try:
        conn = sqlite3.connect('pintar_media.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS produksi 
                     (id INTEGER PRIMARY KEY, user TEXT, master_context TEXT, adegan_data TEXT)''')
        conn.commit()
        conn.close()
    except Exception:
        pass

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
# 2. TEMA GROK (DARK MINIMALIST) - ANTI TYPEERROR
# ==============================================
def apply_grok_theme():
    # Menggunakan st.html untuk menghindari bug markdown pada Python 3.13
    st.html("""
        <style>
            html, body, [data-testid="stAppViewContainer"] {
                background-color: #000000 !important;
                color: #FFFFFF !important;
            }
            [data-testid="stSidebar"] {
                background-color: #080808 !important;
                border-right: 1px solid #1F1F1F !important;
            }
            .stTextArea textarea {
                background-color: #0F0F0F !important;
                color: #FFFFFF !important;
                border: 1px solid #262626 !important;
                border-radius: 10px !important;
            }
            .stTextInput input {
                background-color: #0F0F0F !important;
                color: #FFFFFF !important;
                border: 1px solid #262626 !important;
            }
            div.stButton > button {
                background-color: #FFFFFF !important;
                color: #000000 !important;
                border-radius: 25px !important;
                font-weight: bold !important;
                width: 100%;
                border: none !important;
            }
            header, footer { visibility: hidden !important; }
            .adegan-box {
                border: 1px solid #1F1F1F;
                padding: 15px;
                border-radius: 12px;
                margin-bottom: 20px;
                background-color: #050505;
            }
        </style>
    """)

# ==============================================
# 3. COMPONENT RUANG PRODUKSI
# ==============================================
def render_ruang_produksi():
    st.title("🚀 RUANG PRODUKSI")
    
    # Master Context
    st.subheader("🧠 MASTER CONTEXT")
    st.session_state.master_ctx = st.text_area(
        "Konteks Karakter & Gaya Visual",
        value=st.session_state.get('master_ctx', ''),
        key="master_ctx_input",
        height=100,
        label_visibility="collapsed"
    )

    st.write("---")
    
    # Adegan Loop
    for i in range(10):
        st.markdown(f"**Adegan {i+1}**")
        st.session_state.adegan_list[i] = st.text_area(
            f"Input Adegan {i+1}",
            value=st.session_state.adegan_list[i],
            key=f"scene_{i}",
            height=90,
            label_visibility="collapsed"
        )
        
        if st.button(f"Generate Prompt {i+1}", key=f"btn_gen_{i}"):
            res = f"GAYA: {st.session_state.master_ctx}\n\nADEGAN: {st.session_state.adegan_list[i]}"
            st.code(res)
        st.write("")

# ==============================================
# 4. SISTEM LOGIN & UTAMA
# ==============================================
def main():
    apply_grok_theme()

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'adegan_list' not in st.session_state:
        st.session_state.adegan_list = [""] * 10
    if 'master_ctx' not in st.session_state:
        st.session_state.master_ctx = ""

    if not st.session_state.logged_in:
        st.markdown("<h2 style='text-align:center;'>PINTAR AI LAB</h2>", unsafe_content_html=True)
        u = st.text_input("User", key="u_login")
        p = st.text_input("Pass", type="password", key="p_login")
        if st.button("LOGIN"):
            if u == "admin" and p == "pintar2026":
                st.session_state.logged_in = True
                st.session_state.username = u
                st.session_state.login_time = time.time()
                st.rerun()
            else:
                st.error("Gagal.")
    else:
        # Check PC Only
        w = st_javascript("window.innerWidth")
        if w is not None and w < 1024:
            st.warning("Gunakan PC.")
            st.stop()

        # Sidebar
        with st.sidebar:
            st.title("PINTAR MEDIA")
            menu = st.radio("Menu", ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"])
            
            if st.button("💾 SIMPAN"):
                save_data(st.session_state.username, st.session_state.master_ctx, st.session_state.adegan_list)
                st.success("OK")
            
            if st.button("📂 MUAT"):
                res = load_data(st.session_state.username)
                if res:
                    st.session_state.master_ctx = res[0]
                    st.session_state.adegan_list = json.loads(res[1])
                    st.rerun()

            if st.button("LOGOUT"):
                st.session_state.logged_in = False
                st.rerun()

        if menu == "🚀 RUANG PRODUKSI":
            render_ruang_produksi()
        else:
            st.info(f"Halaman {menu}")

# ==============================================
# 5. EKSEKUSI
# ==============================================
if __name__ == "__main__":
    init_db()
    main()
