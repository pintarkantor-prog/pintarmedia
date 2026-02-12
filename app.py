import streamlit as st
import streamlit_authenticator as stauth
import datetime
import sqlite3
import pandas as pd
import random
import time
from streamlit.components.v1 import html

# --- Tema Elegan seperti Grok (CSS Custom) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #1e1e1e;  /* Dark background */
        color: #ffffff;  /* White text */
    }
    .sidebar .sidebar-content {
        background-color: #2a2a2a;  /* Dark sidebar */
    }
    button {
        background-color: #4CAF50;  /* Green button */
        color: white;
    }
    input, textarea {
        background-color: #333333;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #333333;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- Deteksi User-Agent untuk Batasi Mobile ---
user_agent = st.experimental_get_query_params().get("user_agent", [""])[0]  # Ini aproksimasi; untuk akurat, gunakan JS
if "Mobile" in user_agent or "Android" in user_agent or "iPhone" in user_agent:
    st.error("Akses dibatasi: Hanya bisa diakses menggunakan PC/Komputer.")
    st.stop()

# --- Setup Database SQLite ---
conn = sqlite3.connect('prompt_db.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS scenes (user TEXT, data TEXT)''')  # Untuk save adegan
c.execute('''CREATE TABLE IF NOT EXISTS tasks (task TEXT)''')  # Contoh untuk TUGAS KERJA
conn.commit()

# --- Setup Autentikasi (Tambah user default: admin/password) ---
# Ganti dengan user/password mu. Hash password untuk aman.
credentials = {
    "credentials": {
        "usernames": {
            "admin": {
                "name": "Admin",
                "password": stauth.Hasher(['password']).generate()[0]  # Hash 'password'
            }
        }
    }
}
authenticator = stauth.Authenticate(credentials, "app_cookie", "random_key", cookie_expiry_days=0)

# --- Halaman Login ---
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    # --- Auto-Logout setelah 10 jam ---
    if 'login_time' not in st.session_state:
        st.session_state['login_time'] = datetime.datetime.now()
    
    delta = datetime.datetime.now() - st.session_state['login_time']
    if delta > datetime.timedelta(hours=10):
        st.session_state['authentication_status'] = False
        st.session_state['name'] = None
        st.session_state['username'] = None
        st.experimental_rerun()  # Force logout

    # --- Sidebar Menu ---
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Pilih Menu", [
        "🚀 RUANG PRODUKSI",
        "🧠 PINTAR AI LAB",
        "⚡ QUICK PROMPT",
        "📋 TUGAS KERJA",
        "⚡ KENDALI TIM"
    ])
    authenticator.logout('Logout', 'sidebar')

    # --- Fungsi Save/Load Data (untuk RUANG PRODUKSI) ---
    def save_scenes(user, scenes):
        scenes_str = ','.join(scenes)  # Simpan sebagai string
        c.execute("INSERT OR REPLACE INTO scenes (user, data) VALUES (?, ?)", (user, scenes_str))
        conn.commit()

    def load_scenes(user):
        c.execute("SELECT data FROM scenes WHERE user=?", (user,))
        result = c.fetchone()
        return result[0].split(',') if result else []

    # --- Menu Implementation ---
    if menu == "🚀 RUANG PRODUKSI":
        st.title("🚀 RUANG PRODUKSI")
        st.write("Generate 10 adegan konsisten. Tambah manual, save/load.")
        
        # Load data jika ada
        if 'scenes' not in st.session_state:
            st.session_state['scenes'] = load_scenes(username)
        
        # Generate 10 adegan
        if st.button("Generate 10 Adegan"):
            themes = ["petualangan", "misteri", "romansa", "sci-fi"]  # Contoh template
            st.session_state['scenes'] = [f"Adegan {i+1}: {random.choice(themes)} dengan detail kompleks." for i in range(10)]
        
        # Tampilkan adegan
        for i, scene in enumerate(st.session_state['scenes']):
            st.text_area(f"Adegan {i+1}", value=scene, key=f"scene_{i}")
        
        # Tambah manual
        new_scene = st.text_input("Tambah Adegan Manual")
        if st.button("Tambah"):
            st.session_state['scenes'].append(new_scene)
        
        # Save/Load
        if st.button("Save Data"):
            save_scenes(username, st.session_state['scenes'])
            st.success("Data disimpan!")
        
        if st.button("Load Data"):
            st.session_state['scenes'] = load_scenes(username)
            st.success("Data dimuat!")

    elif menu == "🧠 PINTAR AI LAB":
        st.title("🧠 PINTAR AI LAB")
        premis = st.text_area("Masukkan Premis atau Alur Cerita")
        if st.button("Generate Ide Cerita"):
            # Logic sederhana; bisa expand ke AI API
            st.write(f"Ide berdasarkan '{premis}': Cerita tentang pahlawan yang {premis.lower()} dengan twist akhir.")

    elif menu == "⚡ QUICK PROMPT":
        st.title("⚡ QUICK PROMPT")
        type_prompt = st.selectbox("Pilih Tipe", ["Gambar", "Video"])
        desc = st.text_input("Deskripsi")
        if st.button("Generate Prompt"):
            st.write(f"Prompt {type_prompt}: Gambar/Video tentang {desc} dengan detail tinggi.")

    elif menu == "📋 TUGAS KERJA":
        st.title("📋 TUGAS KERJA")
        # Contoh list tugas dari DB
        new_task = st.text_input("Tambah Tugas")
        if st.button("Tambah Tugas"):
            c.execute("INSERT INTO tasks (task) VALUES (?)", (new_task,))
            conn.commit()
        
        tasks = pd.read_sql_query("SELECT * FROM tasks", conn)
        st.table(tasks)

    elif menu == "⚡ KENDALI TIM":
        st.title("⚡ KENDALI TIM")
        st.write("Monitor kinerja staff. (Contoh dashboard sederhana)")
        # Tambah metric dummy
        st.metric("Kinerja Staff 1", "90%", "5%")
        st.metric("Kinerja Staff 2", "85%", "-2%")

elif authentication_status == False:
    st.error('Username/password salah')
elif authentication_status == None:
    st.warning('Silakan login dengan username dan password')
