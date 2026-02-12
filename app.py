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
# 2. TEMA GROK (DARK MINIMALIST) - VERSI ANTI ERROR
# ==============================================
def apply_grok_theme():
    # Kita buat string CSS satu per satu baris agar tidak ada error indentasi
    css = '<style>'
    css += '.stApp { background-color: #000000 !important; color: #FFFFFF !important; }'
    css += '[data-testid="stSidebar"] { background-color: #080808 !important; border-right: 1px solid #1F1F1F !important; }'
    css += '.stTextArea>div>div>textarea { background-color: #0F0F0F !important; color: #FFFFFF !important; border: 1px solid #262626 !important; border-radius: 12px !important; }'
    css += '.stTextInput>div>div>input { background-color: #0F0F0F !important; color: #FFFFFF !important; border: 1px solid #262626 !important; border-radius: 8px !important; }'
    css += '.stButton>button { background-color: #FFFFFF !important; color: #000000 !important; border-radius: 25px !important; font-weight: 600 !important; border: none !important; height: 45px !important; width: 100% !important; }'
    css += 'header {visibility: hidden;}'
    css += 'footer {visibility: hidden;}'
    css += '.adegan-card { background-color: #0A0A0A; padding: 15px; border-radius: 15px; border: 1px solid #1F1F1F; margin-bottom: 15px; }'
    css += '</style>'
    
    st.markdown(css, unsafe_content_html=True)

# ==============================================
# 3. HALAMAN LOGIN
# ==============================================
def render_login():
    st.markdown("<div style='height:80px'></div>", unsafe_content_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h1 style='text-align:center; letter-spacing:3px;'>PINTAR AI LAB</h1>", unsafe_content_html=True)
        user = st.text_input("Username", key="login_user")
        pw = st.text_input("Password", type="password", key="login_pw")
        if st.button("Masuk Ke Sistem"):
            if user == "admin" and pw == "pintar2026":
                st.session_state.logged_in = True
                st.session_state.username = user
                st.session_state.login_time = time.time()
                st.rerun()
            else:
                st.error("Username atau Password salah.")

# ==============================================
# 4. HALAMAN RUANG PRODUKSI
# ==============================================
def render_ruang_produksi():
    st.markdown("## 🚀 RUANG PRODUKSI")
    
    with st.expander("🧠 MASTER CONTEXT", expanded=True):
        st.session_state.master_ctx = st.text_area(
            "Detail Karakter & Style", 
            value=st.session_state.get('master_ctx', ''),
            placeholder="Contoh: Animasi 3D, Karakter Udin kepala orange...",
            height=100
        )

    st.write("---")
    
    for i in range(10):
        st.markdown(f"<div class='adegan-card'>", unsafe_content_html=True)
        col_idx, col_input = st.columns([1, 9])
        with col_idx:
            st.markdown(f"<h3 style='color:#555; text-align:center;'>{i+1}</h3>", unsafe_content_html=True)
        with col_input:
            st.session_state.adegan_list[i] = st.text_area(
                f"Adegan {i+1}", 
                value=st.session_state.adegan_list[i],
                key=f"sc_{i}", height=80, label_visibility="collapsed"
            )
            if st.button(f"Generate Prompt {i+1}", key=f"btn_{i}"):
                full_p = f"STYLE: {st.session_state.master_ctx} \nSCENE: {st.session_state.adegan_list[i]}"
                st.code(full_p)
        st.markdown("</div>", unsafe_content_html=True)

# ==============================================
# 5. KONTROL UTAMA
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
        # Logout otomatis 10 jam
        if time.time() - st.session_state.login_time > 36000:
            st.session_state.logged_in = False
            st.rerun()

        # Sidebar
        with st.sidebar:
            st.markdown("### PINTAR MEDIA")
            menu = st.radio("NAVIGASI", ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"])
            
            st.write("---")
            if st.button("💾 SIMPAN DATABASE"):
                save_data(st.session_state.username, st.session_state.master_ctx, st.session_state.adegan_list)
                st.success("Tersimpan!")
            
            if st.button("📂 MUAT DATA"):
                res = load_data(st.session_state.username)
                if res:
                    st.session_state.master_ctx = res[0]
                    st.session_state.adegan_list = eval(res[1])
                    st.rerun()
            
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()

        if menu == "🚀 RUANG PRODUKSI":
            render_ruang_produksi()
        else:
            st.title(menu)
            st.info("Fitur sedang disiapkan.")

if __name__ == "__main__":
    init_db()
    main()
