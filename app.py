# ==============================================================================
# BAGIAN 1: KONFIGURASI DAN DATABASE PENGGUNA
# ==============================================================================
import streamlit as st
from datetime import datetime, timedelta

DAFTAR_USER = {
    "dian": "QWERTY21ab", "icha": "udin99", "nissa": "tung22",
    "inggi": "udin33", "lisa": "tung66", "tamu": "123"
}

st.set_page_config(page_title="PINTAR MEDIA | AI Studio", layout="wide")

# ==============================================================================
# BAGIAN 2: SISTEM KEAMANAN & INISIALISASI DATA (SESSION STATE)
# ==============================================================================
def inisialisasi_keamanan():
    if 'sudah_login' not in st.session_state:
        st.session_state.sudah_login = False
    
    # INISIALISASI LACI PENYIMPANAN DATA (ANTI-HILANG)
    if 'data_produksi' not in st.session_state:
        st.session_state.data_produksi = {
            "jumlah_karakter": 2,
            "karakter": [ {"nama": "", "wear": "", "fisik": ""} for _ in range(4) ],
            "jumlah_adegan": 5,
            "adegan": {} # Tempat menyimpan naskah per adegan
        }

    params = st.query_params
    if "auth" in params and params["auth"] == "true":
        if not st.session_state.sudah_login:
            st.session_state.sudah_login = True
            st.session_state.user_aktif = params.get("user", "User")
            st.session_state.waktu_login = datetime.now()

def proses_login(user, pwd):
    if user in DAFTAR_USER and DAFTAR_USER[user] == pwd:
        st.session_state.sudah_login = True
        st.session_state.user_aktif = user
        st.session_state.waktu_login = datetime.now()
        st.query_params.update({"auth": "true", "user": user})
        st.rerun()
    else:
        st.error("Username atau Password salah.")

def tampilkan_halaman_login():
    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_m, col_r = st.columns([2, 1, 2]) 
    with col_m:
        try:
            st.image("PINTAR.png", use_container_width=True)
        except:
            st.markdown("<h2 style='text-align: center;'>PINTAR MEDIA</h2>", unsafe_allow_html=True)
        with st.form("login_station"):
            u = st.text_input("Username", placeholder="Username...", key="login_user").lower()
            p = st.text_input("Password", type="password", placeholder="Password...", key="login_pass")
            submit = st.form_submit_button("MASUK KE SISTEM 🚀", use_container_width=True)
            if submit: proses_login(u, p)
        st.markdown("<p style='text-align: center; color: #484f58; font-size: 11px; margin-top: 15px;'>Secure Access - PINTAR MEDIA</p>", unsafe_allow_html=True)

def cek_autentikasi():
    if st.session_state.sudah_login:
        if 'waktu_login' in st.session_state:
            durasi = datetime.now() - st.session_state.waktu_login
            if durasi > timedelta(hours=10):
                proses_logout()
                return False
        return True
    return False

def proses_logout():
    st.session_state.clear() # Bersihkan semua memori saat logout
    st.query_params.clear()
    st.rerun()

# ==============================================================================
# BAGIAN 3: PENGATURAN TAMPILAN (CSS)
# ==============================================================================
def pasang_css_kustom():
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; color: #e0e0e0; }
        [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
        
        .small-label {
            font-size: 13px !important;
            font-weight: 600 !important;
            color: #d1d5db !important;
            margin-bottom: 4px !important;
            margin-top: 10px !important;
            display: block;
        }
        
        div[data-testid="stForm"] { border: 1px solid #30363d !important; border-radius: 12px !important; padding: 20px !important; }

        div[data-testid="stFormSubmitButton"] button {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
            color: white !important; border: none !important; height: 50px !important; border-radius: 10px !important;
        }

        div[data-baseweb="input"], div[data-baseweb="textarea"] { background-color: #1d2127 !important; border: 1px solid #30363d !important; border-radius: 8px !important; }
        .status-footer { position: fixed; bottom: 20px; left: 20px; font-size: 10px; color: #484f58; text-transform: uppercase; font-family: monospace; }
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# BAGIAN 4: NAVIGASI SIDEBAR
# ==============================================================================
def tampilkan_navigasi_sidebar():
    with st.sidebar:
        st.markdown("<br>", unsafe_allow_html=True)
        pilihan = st.radio("NAVIGASI WORKSPACE", ["🚀 RUANG PRODUKSI", "🧠 PINTAR AI LAB", "⚡ QUICK PROMPT", "📋 TUGAS KERJA", "⚡ KENDALI TIM"])
        
        # PENGATUR JUMLAH ADEGAN (DEFAULT 5)
        st.markdown("---")
        st.markdown("🎬 **PENGATURAN FILM**")
        st.session_state.data_produksi["jumlah_adegan"] = st.number_input("Jumlah Adegan", 1, 50, st.session_state.data_produksi["jumlah_adegan"])
        
        st.markdown("<br>"*5, unsafe_allow_html=True)
        if st.button("LOGOUT SYSTEM", use_container_width=True):
            proses_logout()
        user = st.session_state.get("user_aktif", "USER").upper()
        st.markdown(f'<div class="status-footer">STATION: {user}_SESSION<br>STATUS: AKTIF</div>', unsafe_allow_html=True)
    return pilihan

# ==============================================================================
# BAGIAN 5: MODUL-MODUL PENDUKUNG
# ==============================================================================
def tampilkan_ai_lab(): st.markdown("### 🧠 Pintar AI Lab"); st.info("Area riset prompt.")
def tampilkan_quick_prompt(): st.markdown("### ⚡ Quick Prompt")
def tampilkan_tugas_kerja(): st.markdown("### 📋 Tugas Kerja")
def tampilkan_kendali_tim(): st.markdown("### ⚡ Kendali Tim")

# ==============================================================================
# BAGIAN 6: MODUL UTAMA - RUANG PRODUKSI (MULTI-SCENE & ANTI-HILANG)
# ==============================================================================
def tampilkan_ruang_produksi():
    st.markdown("### 🚀 Ruang Produksi - Hybrid Engine")
    st.write("---")
    
    data = st.session_state.data_produksi

    # 1. IDENTITY LOCK (GLOBAL UNTUK SEMUA ADEGAN)
    with st.expander("🛡️ IDENTITY LOCK - Referensi Foto", expanded=True):
        data["jumlah_karakter"] = st.number_input("Jumlah Karakter", 1, 4, data["jumlah_karakter"])
        cols_char = st.columns(data["jumlah_karakter"])
        for i in range(data["jumlah_karakter"]):
            with cols_char[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                data["karakter"][i]["nama"] = st.text_input(f"Nama", value=data["karakter"][i]["nama"], key=f"char_nama_{i}")
                data["karakter"][i]["wear"] = st.text_input(f"Pakaian", value=data["karakter"][i]["wear"], key=f"char_wear_{i}")
                data["karakter"][i]["fisik"] = st.text_area(f"Ciri Fisik", value=data["karakter"][i]["fisik"], key=f"char_fix_{i}", height=80)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. GENERASI ADEGAN SECARA DINAMIS
    for s in range(data["jumlah_adegan"]):
        scene_id = s + 1
        # Pastikan data adegan ada di laci
        if scene_id not in data["adegan"]:
            data["adegan"][scene_id] = {"aksi": "", "style": "Realistis", "light": "Studio", "arah": "Normal", "shot": "Setengah Badan", "ratio": "16:9", "cam": "Static", "loc": "", "dialogs": [""]*4}

        with st.expander(f"🟢 ADEGAN {scene_id}", expanded=(scene_id == 1)):
            col_text, col_set = st.columns([1.5, 1])
            
            with col_text:
                st.markdown("### 📸 Naskah Visual & Aksi")
                data["adegan"][scene_id]["aksi"] = st.text_area("Aksi", value=data["adegan"][scene_id]["aksi"], height=335, key=f"act_{scene_id}", label_visibility="collapsed")
            
            with col_set:
                sub1, sub2 = st.columns(2)
                with sub1:
                    st.markdown('<p class="small-label">✨ STYLE</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["style"] = st.selectbox("Style", ["Realistis", "Pixar 3D", "Glossy Asphalt", "Naruto Anime"], index=0, key=f"mood_{scene_id}", label_visibility="collapsed")
                    st.markdown('<p class="small-label" style="margin-top:15px;">💡 LIGHTING</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["light"] = st.selectbox("Lighting", ["Golden Hour", "Studio", "Natural"], key=f"light_{scene_id}", label_visibility="collapsed")
                    st.markdown('<p class="small-label" style="margin-top:15px;">📐 ARAH KAMERA</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["arah"] = st.selectbox("Arah", ["Normal", "Sudut Tinggi", "Samping", "Berhadapan"], key=f"arah_{scene_id}", label_visibility="collapsed")
                with sub2:
                    st.markdown('<p class="small-label">🔍 UKURAN GAMBAR</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["shot"] = st.selectbox("Shot", ["Dekat Wajah", "Setengah Badan", "Seluruh Badan", "Pemandangan Luas"], key=f"shot_{scene_id}", label_visibility="collapsed")
                    st.markdown('<p class="small-label" style="margin-top:15px;">📺 ASPECT RATIO</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["ratio"] = st.selectbox("Ratio", ["16:9", "9:16", "1:1"], key=f"ratio_{scene_id}", label_visibility="collapsed")
                    st.markdown('<p class="small-label" style="margin-top:15px;">🎥 GERAKAN</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["cam"] = st.selectbox("Camera", ["Static", "Zoom In", "Tracking"], key=f"cam_{scene_id}", label_visibility="collapsed")
                
                st.markdown('<p class="small-label" style="margin-top:15px;">📍 LOKASI</p>', unsafe_allow_html=True)
                data["adegan"][scene_id]["loc"] = st.text_input("Lokasi", value=data["adegan"][scene_id]["loc"], key=f"loc_{scene_id}", label_visibility="collapsed")

            # BARIS DIALOG
            st.markdown('<hr style="border:0.5px solid #10b981; opacity:0.3; margin-top:20px; margin-bottom:10px;">', unsafe_allow_html=True)
            cols_d = st.columns(data["jumlah_karakter"])
            for i in range(data["jumlah_karakter"]):
                with cols_d[i]:
                    name = data["karakter"][i]["nama"] if data["karakter"][i]["nama"] else f"Karakter {i+1}"
                    st.markdown(f'<p class="small-label">Dialog {name}</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["dialogs"][i] = st.text_input(f"D_{scene_id}_{i}", value=data["adegan"][scene_id]["dialogs"][i], key=f"d_{scene_id}_{i}", label_visibility="collapsed")

            # TOMBOL GENERATE PER ADEGAN
            if st.button(f"🚀 GENERATE PROMPT ADEGAN {scene_id}", use_container_width=True, key=f"btn_{scene_id}"):
                st.markdown("---")
                char_ids = " AND ".join([f"[[ CHARACTER_{c['nama'].upper()}: \"{c['fisik']}\" maintain 100% exact facial features. ]]" for c in data["karakter"] if c['nama']])
                all_d = " | ".join([f"{data['karakter'][i]['nama']}: '{data['adegan'][scene_id]['dialogs'][i]}'" for i in range(data["jumlah_karakter"])])
                
                img_p = f"CHARACTER DATA: {char_ids}\nVISUAL ACTION: {data['adegan'][scene_id]['aksi']}\nENVIRONMENT: {data['adegan'][scene_id]['loc']}\nTECHNICAL: {data['adegan'][scene_id]['style']}, {data['adegan'][scene_id]['light']}, {data['adegan'][scene_id]['shot']} --ar {data['adegan'][scene_id]['ratio']}"
                vid_p = f"Character Profiles: {char_ids}\nScene: {data['adegan'][scene_id]['aksi']} at {data['adegan'][scene_id]['loc']}\nActing Cue: {all_d}\nTechnical: {data['adegan'][scene_id]['cam']} at {data['adegan'][scene_id]['arah']}, 60fps."

                c1, c2 = st.columns(2)
                with c1: st.code(img_p)
                with c2: st.code(vid_p)

# ==============================================================================
# BAGIAN 7: PENGENDALI UTAMA
# ==============================================================================
def utama():
    inisialisasi_keamanan()
    pasang_css_kustom()
    if not cek_autentikasi():
        tampilkan_halaman_login()
    else:
        menu = tampilkan_navigasi_sidebar()
        if menu == "🚀 RUANG PRODUKSI": tampilkan_ruang_produksi()
        elif menu == "🧠 PINTAR AI LAB": tampilkan_ai_lab()
        elif menu == "⚡ QUICK PROMPT": tampilkan_quick_prompt()
        elif menu == "📋 TUGAS KERJA": tampilkan_tugas_kerja()
        elif menu == "⚡ KENDALI TIM": tampilkan_kendali_tim()

if __name__ == "__main__":
    utama()
