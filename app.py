import streamlit as st
import time
import sqlite3
from streamlit_javascript import st_javascript

# ==============================================
# 1. DATABASE ENGINE (Simpan & Muat Permanen)
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
    # Hapus data lama user ini, simpan yang baru (Upsert logic)
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
# 2. TEMA GROK (DARK MINIMALIST)
# ==============================================
def apply_grok_theme():
    st.markdown("""
        <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        [data-testid="stSidebar"] { background-color: #080808; border-right: 1px solid #1F1F1F; }
        .stTextArea>div>div>textarea { background-color: #0F0F0F !important; color: #FFFFFF !important; border: 1px solid #262626 !important; border-radius: 12px !important; }
        .stButton>button { background-color: #FFFFFF; color: #000000; border-radius: 25px; font-weight: 600; border: none; height: 45px; }
        .stButton>button:hover { background-color: #E0E0E0; border: 1px solid #FFFFFF; }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        /* Card Style untuk Adegan */
        .adegan-card { background-color: #0A0A0A; padding: 20px; border-radius: 15px; border: 1px solid #1F1F1F; margin-bottom: 10px; }
        </style>
    """, unsafe_content_html=True)

# ==============================================
# 3. RUANG PRODUKSI (MAIN GENERATOR)
# ==============================================
def render_ruang_produksi():
    st.markdown("<h2 style='margin-bottom:0;'>🚀 RUANG PRODUKSI</h2>", unsafe_content_html=True)
    st.caption("Pusat Kendali Prompt YouTube Shorts - Konsistensi Adegan")
    st.write("---")

    # Kolom Master Context (Kunci Konsistensi)
    with st.expander("🧠 MASTER CONTEXT (Karakter, Style, Latar)", expanded=True):
        master_ctx = st.text_area("Jelaskan detail karakter (misal: Udin berkepala orange) dan style visual agar konsisten di semua adegan.", 
                                  value=st.session_state.get('master_ctx', ''), height=100)
        st.session_state.master_ctx = master_ctx

    st.write("### 🎬 Daftar 10 Adegan")
    
    # Grid untuk Adegan
    for i in range(10):
        with st.container():
            st.markdown(f"<div class='adegan-card'>", unsafe_content_html=True)
            col_idx, col_input, col_action = st.columns([0.5, 7, 2])
            
            with col_idx:
                st.markdown(f"<h3 style='color:#444;'>{i+1}</h3>", unsafe_content_html=True)
            
            with col_input:
                st.session_state.adegan_list[i] = st.text_area(
                    f"Deskripsi Visual Adegan {i+1}", 
                    value=st.session_state.adegan_list[i],
                    placeholder="Contoh: Udin sedang berjalan di pasar malam dengan wajah ceria...",
                    key=f"area_{i}", height=80, label_visibility="collapsed"
                )
            
            with col_action:
                if st.button(f"Copy Prompt {i+1}", key=f"btn_{i}"):
                    full_prompt = f"STYLE: {master_ctx} \n\nSCENE: {st.session_state.adegan_list[i]}"
                    st.code(full_prompt) # Menampilkan box copyable
            st.markdown("</div>", unsafe_content_html=True)

    # Floating Action Bar (Simpan & Load)
    st.sidebar.markdown("---")
    st.sidebar.subheader("💾 Database Control")
    if st.sidebar.button("SIMPAN SEMUA DATA"):
        save_data(st.session_state.username, st.session_state.master_ctx, st.session_state.adegan_list)
        st.sidebar.success("Berhasil disimpan ke Database!")
    
    if st.sidebar.button("LOAD DATA TERAKHIR"):
        data = load_data(st.session_state.username)
        if data:
            st.session_state.master_ctx = data[0]
            st.session_state.adegan_list = eval(data[1])
            st.rerun()

# ==============================================
# 4. KONTROL UTAMA & NAVIGASI
# ==============================================
def main():
    apply_grok_theme()
    init_db()

    # Inisialisasi Session State
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'adegan_list' not in st.session_state:
        st.session_state.adegan_list = [""] * 10
    if 'menu' not in st.session_state:
        st.session_state.menu = "🚀 RUANG PRODUKSI"

    # Login Logic
    if not st.session_state.logged_in:
        render_login()
    else:
        # Check PC Only
        width = st_javascript("window.innerWidth")
        if width is not None and width < 1024:
            st.warning("⚠️ Gunakan Desktop untuk mengakses Ruang Produksi.")
            st.stop()
        
        # Sidebar Menu
        with st.sidebar:
            st.markdown("<h2 style='letter-spacing: 2px;'>PINTAR MEDIA</h2>", unsafe_content_html=True)
            st.write(f"User: **{st.session_state.username}**")
            st.session_state.menu = st.radio("NAVIGASI", [
                "🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"
            ])
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()

        # Route Halaman
        if st.session_state.menu == "🚀 RUANG PRODUKSI":
            render_ruang_produksi()
        else:
            st.title(st.session_state.menu)
            st.info("Halaman ini sedang dalam pengembangan.")

def render_login():
    st.markdown("<div style='height:100px'></div>", unsafe_content_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h1 style='text-align:center;'>LOG IN</h1>", unsafe_content_html=True)
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("Masuk Ke Sistem"):
            if user == "admin" and pw == "pintar2026":
                st.session_state.logged_in = True
                st.session_state.username = user
                st.session_state.login_time = time.time()
                st.rerun()
            else:
                st.error("Kredensial Salah")

if __name__ == "__main__":
    main()
