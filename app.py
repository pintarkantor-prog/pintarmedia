import streamlit as st
import time
import sqlite3
import json
from streamlit_javascript import st_javascript

# ==============================================
# 1. DATABASE ENGINE (SQLITE + JSON)
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
    # Menggunakan string gabungan untuk menghindari TypeError di Python 3.13
    css = '<style>'
    css += '.stApp { background-color: #000000 !important; color: #FFFFFF !important; }'
    css += '[data-testid="stSidebar"] { background-color: #080808 !important; border-right: 1px solid #1F1F1F !important; }'
    css += '.stTextArea textarea { background-color: #0F0F0F !important; color: #FFFFFF !important; border: 1px solid #262626 !important; border-radius: 10px !important; }'
    css += '.stTextInput input { background-color: #0F0F0F !important; color: #FFFFFF !important; border: 1px solid #262626 !important; }'
    css += 'div.stButton > button { background-color: #FFFFFF !important; color: #000000 !important; border-radius: 25px !important; font-weight: bold !important; width: 100%; border: none !important; transition: 0.3s; }'
    css += 'div.stButton > button:hover { background-color: #CCCCCC !important; transform: scale(1.01); }'
    css += 'header { visibility: hidden; }'
    css += 'footer { visibility: hidden; }'
    css += '.adegan-box { border: 1px solid #1F1F1F; padding: 15px; border-radius: 12px; margin-bottom: 20px; background-color: #050505; }'
    css += 'code { color: #4facfe !important; }'
    css += '</style>'
    st.markdown(css, unsafe_content_html=True)

# ==============================================
# 3. HALAMAN LOGIN
# ==============================================
def render_login():
    st.markdown("<div style='height:100px'></div>", unsafe_content_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h1 style='text-align:center; letter-spacing:2px;'>PINTAR AI LAB</h1>", unsafe_content_html=True)
        st.markdown("<p style='text-align:center; color:#555;'>Production Suite Access</p>", unsafe_content_html=True)
        u = st.text_input("Username", key="login_u")
        p = st.text_input("Password", type="password", key="login_p")
        if st.button("MASUK SISTEM"):
            if u == "admin" and p == "pintar2026":
                st.session_state.logged_in = True
                st.session_state.username = u
                st.session_state.login_time = time.time()
                st.rerun()
            else:
                st.error("Kredensial tidak valid.")

# ==============================================
# 4. COMPONENT RUANG PRODUKSI
# ==============================================
def render_ruang_produksi():
    st.markdown("## 🚀 RUANG PRODUKSI")
    st.caption("Fokus pada Konsistensi Karakter & Alur YouTube Shorts")
    
    # Master Context: Kunci Konsistensi
    st.markdown("### 🧠 MASTER CONTEXT")
    st.session_state.master_ctx = st.text_area(
        "Konteks Karakter & Gaya Visual",
        value=st.session_state.master_ctx,
        placeholder="Contoh: Style Animasi 3D, Udin kepala orange, baju hijau, lighting sinematik...",
        key="master_ctx_input",
        height=100
    )

    st.write("---")
    
    # 10 Adegan Generator
    for i in range(10):
        st.markdown(f"<div class='adegan-box'>", unsafe_content_html=True)
        col_idx, col_text = st.columns([1, 9])
        
        with col_idx:
            st.markdown(f"<h3 style='text-align:center; color:#444; margin-top:10px;'>{i+1}</h3>", unsafe_content_html=True)
            
        with col_text:
            st.session_state.adegan_list[i] = st.text_area(
                f"Deskripsi Adegan {i+1}",
                value=st.session_state.adegan_list[i],
                key=f"scene_{i}",
                height=90,
                label_visibility="collapsed",
                placeholder=f"Apa yang terjadi di adegan ke-{i+1}?"
            )
            
            if st.button(f"Generate Prompt {i+1}", key=f"btn_gen_{i}"):
                final_p = f"### MASTER STYLE:\n{st.session_state.master_ctx}\n\n### SCENE DESCRIPTION:\n{st.session_state.adegan_list[i]}"
                st.code(final_p)
        st.markdown("</div>", unsafe_content_html=True)

# ==============================================
# 5. LOGIKA UTAMA & NAVIGASI
# ==============================================
def main():
    apply_grok_theme()

    # Inisialisasi Session State agar data persisten
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'adegan_list' not in st.session_state:
        st.session_state.adegan_list = [""] * 10
    if 'master_ctx' not in st.session_state:
        st.session_state.master_ctx = ""
    if 'current_menu' not in st.session_state:
        st.session_state.current_menu = "🚀 RUANG PRODUKSI"

    if not st.session_state.logged_in:
        render_login()
    else:
        # Logout otomatis setelah 10 jam (36000 detik)
        if time.time() - st.session_state.login_time > 36000:
            st.session_state.logged_in = False
            st.rerun()

        # Proteksi Akses Mobile
        w = st_javascript("window.innerWidth")
        if w is not None and w < 1024:
            st.warning("⚠️ RUANG PRODUKSI HANYA TERSEDIA DI DESKTOP.")
            st.stop()

        # Sidebar Navigasi
        with st.sidebar:
            st.markdown("<h2 style='letter-spacing:2px; color:white;'>PINTAR MEDIA</h2>", unsafe_content_html=True)
            st.write(f"User: **{st.session_state.username}**")
            st.session_state.current_menu = st.radio("MENU UTAMA", [
                "🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"
            ])
            
            st.write("---")
            if st.button("💾 SIMPAN SEMUA DATA"):
                save_data(st.session_state.username, st.session_state.master_ctx, st.session_state.adegan_list)
                st.success("Data berhasil diamankan!")
            
            if st.button("📂 MUAT DATA LAMA"):
                res = load_data(st.session_state.username)
                if res:
                    st.session_state.master_ctx = res[0]
                    st.session_state.adegan_list = json.loads(res[1])
                    st.rerun()
            
            if st.button("🚪 KELUAR"):
                st.session_state.logged_in = False
                st.rerun()

        # Route Halaman
        if st.session_state.current_menu == "🚀 RUANG PRODUKSI":
            render_ruang_produksi()
        else:
            st.title(st.session_state.current_menu)
            st.info("Ruangan ini sedang dalam tahap dekorasi oleh tim developer.")

# ==============================================
# 6. EKSEKUSI FINAL
# ==============================================
if __name__ == "__main__":
    init_db() # Menjamin Database siap sebelum aplikasi jalan
    main()
