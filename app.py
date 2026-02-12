import streamlit as st
import time
import sqlite3
import json

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
# 2. TEMA GROK (DARK MINIMALIST)
# ==============================================
def apply_grok_theme():
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
    st.write("Sistem Pembuatan 10 Adegan YouTube Shorts")
    
    st.subheader("🧠 MASTER CONTEXT")
    st.session_state.master_ctx = st.text_area(
        "Konteks Karakter & Gaya Visual",
        value=st.session_state.get('master_ctx', ''),
        placeholder="Contoh: Style Animasi 3D, Udin kepala orange...",
        key="master_ctx_input",
        height=100,
        label_visibility="collapsed"
    )

    st.write("---")
    
    for i in range(10):
        with st.container():
            st.write(f"### Adegan {i+1}")
            st.session_state.adegan_list[i] = st.text_area(
                f"Input Adegan {i+1}",
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
# 4. SISTEM LOGIN & DATA USER
# ==============================================
def render_login():
    # Daftar User & Password sesuai permintaan
    users_db = {
        "dian": "QWERTY21ab",  
        "icha": "udin99",
        "nissa": "tung22",
        "inggi": "udin33",
        "lisa": "tung66",
        "tamu": "123"
    }

    st.markdown("<div style='height:100px'></div>", unsafe_content_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("🧠 PINTAR AI LAB")
        u = st.text_input("Username", key="login_u")
        p = st.text_input("Password", type="password", key="login_p")
        
        if st.button("MASUK SISTEM"):
            if u in users_db and users_db[u] == p:
                st.session_state.logged_in = True
                st.session_state.username = u
                st.session_state.login_time = time.time()
                st.rerun()
            else:
                st.error("Username atau Password salah")

# ==============================================
# 5. LOGIKA UTAMA & NAVIGASI
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
        render_login()
    else:
        # Logout otomatis 10 jam (36000 detik)
        if time.time() - st.session_state.login_time > 36000:
            st.session_state.logged_in = False
            st.rerun()

        # Sidebar Navigasi
        with st.sidebar:
            st.title("PINTAR MEDIA")
            st.write(f"Logged in as: **{st.session_state.username}**")
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

if __name__ == "__main__":
    init_db()
    main()
