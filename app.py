import streamlit as st
import requests  
import pandas as pd
import gspread 
import time
import pytz
import json
import re
from datetime import datetime, timedelta
from google.oauth2.service_account import Credentials

def bersihkan_data(df):
    if df.empty: return df
    df.columns = [str(c).strip().upper() for c in df.columns]
    # Tambahkan TANGGAL dan WAKTU_KIRIM ke daftar kolom yang dibersihkan
    kolom_krusial = ['NAMA', 'STAF', 'STATUS', 'USERNAME', 'TANGGAL', 'WAKTU_KIRIM']
    for col in kolom_krusial:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.upper()
    return df

# ==============================================================================
# BAGIAN 1: PUSAT KENDALI OPSI (VERSI KLIMIS - NO REDUNDANCY)
# ==============================================================================
OPTS_STYLE = ["Sangat Nyata", "Animasi 3D Pixar", "Gaya Cyberpunk", "Anime Jepang"]
OPTS_LIGHT = ["Senja Cerah (Golden)", "Studio Bersih", "Neon Cyberpunk", "Malam Indigo", "Siang Alami"]
OPTS_ARAH  = ["Sejajar Mata", "Dari Atas", "Dari Bawah", "Dari Samping", "Berhadapan"]
OPTS_SHOT  = ["Sangat Dekat", "Wajah & Bahu", "Setengah Badan", "Seluruh Badan", "Drone (Jauh)"]
OPTS_CAM   = ["Diam (Tetap Napas)", "Maju Perlahan", "Ikuti Karakter", "Memutar", "Goyang (Handheld)"]
OPTS_RATIO = ["9:16", "16:9", "1:1"]

def rakit_prompt_sakral(aksi, style, light, arah, shot, cam):
    style_map = {
        "Sangat Nyata": "Cinematic RAW shot, PBR surfaces, 8k textures, macro-detail fidelity, f/1.8 lens focus, depth map rendering.",
        "Animasi 3D Pixar": "Disney style 3D, Octane render, ray-traced global illumination, premium subsurface scattering.",
        "Gaya Cyberpunk": "Futuristic neon aesthetic, volumetric fog, sharp reflections, high contrast.",
        "Anime Jepang": "Studio Ghibli style, hand-painted watercolor textures, soft cel shading, lush aesthetic."
    }
    
    light_map = {
        "Senja Cerah (Golden)": "4 PM golden hour, warm amber highlights, dramatic long shadows, high local contrast.",
        "Studio Bersih": "Professional studio setup, rim lighting, clean shadows, commercial photography look.",
        "Neon Cyberpunk": "Vibrant pink and blue rim light, deep noir shadows, cinematic volumetric lighting.",
        "Malam Indigo": "Cinematic night, moonlight shading, deep indigo tones, clean silhouettes.",
        "Siang Alami": "Daylight balanced exposure, neutral color temperature, crystal clear atmosphere."
    }

    s_cmd = style_map.get(style, "Cinematic optical clarity.")
    l_cmd = light_map.get(light, "Balanced exposure.")
    
    # --- PERBAIKAN: Hapus label "Technical:" agar lebih clean ---
    tech_logic = f"{shot} framing, {arah} angle, {cam} motion, cinematic optical rendering."

    return f"{s_cmd} {tech_logic} {l_cmd}"
    
DAFTAR_USER = {
    "dian": "QWERTY21ab", "icha": "udin99", "nissa": "tung22",
    "inggi": "udin33", "lisa": "tung66", "tamu": "123"
}
MASTER_CHAR = {
    "Custom": {"fisik": "", "versi_pakaian": {"Manual": ""}}, 
    
    "Udin": {
        "fisik": "",
        "versi_pakaian": {
            "Keseharian": "Black cotton t-shirt with the word 'UDIN' printed in bold white letters in the center, premium branded short denim jeans, and black rubber flip-flops.",
            "Kemeja": "Open-buttoned red and black plaid flannel shirt, plain white crewneck t-shirt underneath, black denim shorts, and white high-top sneakers. STRICTLY NO HAT, no headwear.",
            "Casual": "High-end designer oversized white t-shirt in heavy-weight premium cotton, paired with luxury light-wash distressed denim jeans. Limited-edition hypebeast sneakers. Accessorized with a diamond-encrusted watch, a solid gold bracelet, and a thick gold link chain necklace.",
            "Versi Gaul": "Vibrant pink short-sleeve button-up shirt with large tropical floral patterns, open over a white premium cotton tank top. Tailored white linen shorts. Thick gold link chain, wide gold bracelet, diamond-encrusted watch. White luxury designer sneakers.",
            "Versi Kaya": "Premium navy blue polo shirt, beige chino shorts. Sleek luxury gold watch. Brown suede boat shoes with white rubber soles.",
            "Versi Sultan": "Charcoal three-piece suit, metallic gold brocade patterns, fully buttoned. Black silk shirt, black bow tie. Thick gold link chain, large diamond-encrusted dollar pendant, gemstone rings. Black velvet loafers with shimmering micro-diamonds. Gold-rimmed sunglasses. No color bleeding; isolated gold and diamond textures.",
            "Versi Raja": "Royal crimson velvet tunic, heavy gold-threaded embroidery, high standing collar. Detailed gold metallic fibers woven throughout the fabric. Massive gemstone rings on fingers. Polished gold-tipped leather boots.",
            "Versi Miskin": "Stretched-out grey cotton t-shirt, faded fabric, visible stains. Short trousers with frayed hems. Thin blue rubber flip-flops. All fabrics feature rough, damaged, and pitted textures.",
            "Versi Gembel": "Tattered oversized undershirt, multiple irregular holes, heavy dark grime. Patchwork shorts held by a frayed rope. Mismatched worn-out sandals. Extremely distressed and soiled fabric textures with layered dirt. Surface of the orange head looks dusty and dull.",
            "Anak SD": "White short-sleeve button-up shirt, red embroidered school logo on the chest pocket. Red short trousers, elastic waistband. Red and white striped tie. Low-cut black canvas sneakers, white rubber soles. High-contrast red and white fabric textures.",
            "Anak SMA": "Short-sleeved white button-up shirt, embroidered school logo on chest pocket. Gray trousers, Slim black synthetic belt, silver buckle. Gray tie. Low-cut black canvas sneakers, white rubber sole. High contrast gray and white fabric texture."
        }
    },

    "Tung": {
        "fisik": "",
        "versi_pakaian": {
            "Keseharian 1": "Forest green cotton T-shirt. Charcoal grey long trousers. Brown rubber flip-flops. zero accessories.",
            "Keseharian 2": "A worn blue polo shirt, worn gray sweatpants and rubber flip-flops.",            
            "Kemeja": "Open-buttoned blue and white plaid flannel shirt, plain white crewneck t-shirt underneath, long blue denim jeans, and brown leather boots. STRICTLY NO HAT, no headwear.",
            "Casual": "dark gray polo shirt with honeycomb motif, dark gray twill shorts. shiny brown belt. shiny brown shoes.",
            "Versi Gaul": "Pink polo shirt, monogram pattern, silk-pique blend, shiny gold-rimmed buttons. Dark royal pink chino shorts, satin stitching, high-gloss finish. Chocolate brown crocodile leather belt, oversized gold 'T' logo buckle. Diamond-encrusted gold watch, heavy metallic link strap. White crocodile leather loafers, gold horsebit hardware. No sunglasses, zero headwear. Extravagant, high-contrast, and reflective material textures.",
            "Versi Kaya": "Electric orange silk-satin blazer, open front design, wide notched lapels. Matching orange silk waistcoat, tonal button details. Bright royal purple tailored long trousers, high-gloss satin finish. Chocolate brown crocodile-skin belt, oversized gold 'T' metallic buckle. Oversized gold-framed aviator sunglasses, dark gradient lenses. Solid gold wristwatch, fully iced diamond dial. Holographic silver leather footwear, translucent chunky soles. Multi-layered gold chain necklace with a small solid gold 'TUNG' pendant. Luminous, hyper-reflective, and extravagant material textures.",
            "Versi Sultan": "Iridescent silver silk textile, reflective glass-bead embroidery. Metallic gold-threaded denim fabric, deep indigo base, straight-cut long trousers. Chocolate brown crocodile-skin texture belt, oversized gold 'T' metallic buckle. Solid white-gold timekeeper, baguette-cut sapphire bezel, fully iced dial. High-gloss holographic leather footwear, translucent chunky soles. Horizontal solid 24k gold pendant spelling 'TUNG', high-mirror polish finish, encrusted with micro-diamond accents, attached to a fine gold micro-link chain. Hyper-reflective, multifaceted, and luminous material textures.",
            "Versi Miskin": "faded yellowish white t-shirt. The corduroy trousers are brown, the bottom edge is frayed, and there are sewn-on patches. Weathered rubber flip flops.",
            "Anak SD": "White short-sleeve button-up shirt, red embroidered school logo on the chest pocket. Red short trousers, elastic waistband. Red and white striped tie. Low-cut black canvas sneakers, white rubber soles. High-contrast red and white fabric textures.",
            "Anak SMA": "Short-sleeved white button-up shirt, embroidered school logo on chest pocket. Gray trousers, Slim black synthetic belt, silver buckle. Gray tie. Low-cut black canvas sneakers, white rubber sole. High contrast gray and white fabric texture."
        }
    },
    
    "Balerina": {
        "fisik": "",
        "versi_pakaian": {
            "Keseharian": "Dark brown linen dress, straight cut, knee length. Textile with a simple matte finish. Plain black leather flat shoes, thin rubber soles. No accessories. The surface of the material is smooth and opaque.",
            "Daster": "Loose-fit cotton rayon daster, vibrant purple and blue batik floral patterns. Wide-cut arm openings. Red rubber flip-flops, thinned soles, worn-out surface texture.",
            "Versi Gaul": "Soft pink cotton t-shirt, bright floral pattern print. Dark brown cotton skirt, flared A-line cut, no ruffles. White platform leather sneakers, thick see-through sole, colorful lace details.",
            "Wanita Karir": "Tailored charcoal gray striped wool blazer, sharp padded shoulders. Striped slim-fit trousers with pressed pleats. Black silk sleeveless turtleneck inner lining. Gold layered necklace with geometric pendant. Shiny black pointed stiletto heels.",
            "Versi Miskin": "Oversized faded brown cotton dress, stretched neckline, visible coarse hand-stitched repairs. The texture of the fabric is piled and thinned. Worn rubber flip flops.",
            "Anak SD": "Short-sleeved white button-up shirt, red embroidered school logo on chest pocket. Red skirt, elastic waist. Red and white striped tie. Low-cut black canvas sneakers, white rubber sole. High contrast red and white fabric texture.",
            "Anak SMA": "Short-sleeved white button-up shirt, embroidered school logo on the chest pocket. gray skirt, slim black synthetic belt, silver buckle. Gray tie. Low-cut black canvas sneakers, white rubber sole. High contrast gray and white fabric texture."
        }
    },

    "Emak": {
        "fisik": "",
        "versi_pakaian": {
            "Keseharian": "Long negligee in loose rayon cotton fabric, bright brown and pink batik floral motif. Wide cut sleeve openings. Green rubber flip flops, thin soles, worn surface texture.",
            "Daster Kerudung": "Long negligee made from loose rayon cotton, bright blue and red floral batik motifs combined with 'Bergo' (instant jersey hijab with white foam edges). Green rubber flip flops, thin sole, worn surface texture.",
            "Versi Miskin": "Long negligee made from loose rayon cotton with floral batik motifs in faded pink and shabby green. Red rubber flip flops. Two small white medicine patches are attached symmetrically to the right and left sides of the forehead.",
            "Versi Sultan": "remium Silk Kaftan with elegant gold embroidery, carrying a luxury designer handbag, wearing a large diamond ring and gold jewelry, with oversized designer sunglasses. shiny brown sandals, gold lines that look sharp and shiny."
        }
    },

    "Bapak": {
        "fisik": "",
        "versi_pakaian": {
            "Keseharian": "Plain white t-shirt, loose ends not tucked in, covering the waist. Long checkered cotton sarong, red and calm colors, straight vertical curtains. Blue rubber flip flops.",
            "Versi Kades": "Formal khaki-colored PDH (Indonesian civil servant uniform) with shoulder epaulets. On the right chest, there is a clear black name tag with white text that reads: 'KADES KONOHA'. Wearing black leather shoes and a leather belt.",
            "Versi Pak RT": "Short-sleeved batik shirt tucked into black trousers. holding a clip-on folder.",
            "Versi Batik": "Exclusive silk batik shirt with expensive intricate motifs. Wearing a large 'batu akik' gemstone ring, a gold watch, luxury sunglasses, and polished shiny leather shoes."
        }
    },

    "Rumi": {
        "fisik": "",
        "versi_pakaian": {
            "Keseharian": "Modern Cotton Batik Daster (house dress) with minimalist motifs. Her signature purple braided ponytail was tied a little lower. Wearing pink rubber flip-flops.",
            "Casual": "An oversized cream-colored knit sweater tucked into light blue high-waisted jeans. Wearing clean white minimalist sneakers.",
            "Versi Miskin": "A worn pink t-shirt and worn gray long jeans. wearing black flip flops.",
            "Versi Gaul": "Yellow cropped leather bomber jacket with floral embroidery, white crop top underneath, denim hot pants with a fuchsia pink belt, and high black boots.",
            "Wanita Karir": "A sharply designed white blazer over a soft light brown silk blouse, paired with charcoal gray trousers and black pointy heels.",
            "Versi Kaya": "Deep purple silk-satin midi dress, tailored wrap-around design, clean-cut V-neckline. A delicate string of brilliant-cut diamonds, set in white gold, resting on the fabric's neckline. Smooth high-luster textile. Black pointed-toe leather pumps, slim high heels, polished finish. Small structured gold metallic handbag, minimalist geometric shape.",
            "Anak SD": "Short-sleeved white button-up shirt, red embroidered school logo on chest pocket. Red skirt, elastic waist. Red and white striped tie. Low-cut black canvas sneakers, white rubber sole. High contrast red and white fabric texture.",
            "Anak SMA": "Short-sleeved white button-up shirt, embroidered school logo on the chest pocket. gray skirt, slim black synthetic belt, silver buckle. Gray tie. Low-cut black canvas sneakers, white rubber sole. High contrast gray and white fabric texture."
        }
    },

    "Dindin": {
        "fisik": "",
        "versi_pakaian": {
            "Keseharian ": "Bright yellow cotton T-shirt, featuring a large colorful cartoon dinosaur print on the center chest. Short navy blue denim overalls, small metallic buckle fastenings. Wears colorful sneakers with glowing LED lights.",
            "Versi Miskin": "The faded gray cotton T-shirt is oversized, the collar is stretchy, and the cartoon print is cracked and peeling. Worn brown corduroy shorts. black flip flops.",
            "Versi Gaul": "Mini cat-ear hoodie, denim jogger pants, glowing LED roller shoes, and bright neon plastic sunglasses.",
            "Versi Sultan": "Mini white silk tuxedo, tiny diamond-encrusted toy watch, holding a gold-plated smartphone, expensive designer sneakers.",
            "Anak SD": "White short-sleeve button-up shirt, red embroidered school logo on the chest pocket. Red short trousers, elastic waistband. Red and white striped tie. Low-cut black canvas sneakers, white rubber soles. High-contrast red and white fabric textures.",
            "Anak SMA": "Short-sleeved white button-up shirt, embroidered school logo on chest pocket. Gray trousers, Slim black synthetic belt, silver buckle. Gray tie. Low-cut black canvas sneakers, white rubber sole. High contrast gray and white fabric texture."
        }
    },

    "Tingting": {
        "fisik": "",
        "versi_pakaian": {
            "Keseharian ": "Blue polo shirt, dark blue sweatpants, and brown velcro strap sneakers.",
            "Casual": "A cool mini bomber jacket in olive green over a grey t-shirt, paired with khaki cargo jogger pants and small tactical boots.",
            "Versi Miskin": "Tunic made from a tattered flour sack with visible branding (karung terigu), scrap cloth shorts, carrying an old inner tube (ban dalam) as a toy.",
            "Versi Gaul": "Flannel shirt tied around the waist, multi-pocket cargo pants, backwards snapback hat, and large headphones around neck.",
            "Versi Sultan": "A crimson royal velvet robe, a small gold crown perched on his head. premium leather boots, holding a solid gold toy car.",
            "Anak SD": "White short-sleeve button-up shirt, red embroidered school logo on the chest pocket. Red short trousers, elastic waistband. Red and white striped tie. Low-cut black canvas sneakers, white rubber soles. High-contrast red and white fabric textures.",
            "Anak SMA": "Short-sleeved white button-up shirt, embroidered school logo on chest pocket. Gray trousers, Slim black synthetic belt, silver buckle. Gray tie. Low-cut black canvas sneakers, white rubber sole. High contrast gray and white fabric texture."
        }
    }
}

st.set_page_config(page_title="PINTAR MEDIA | Studio", layout="wide")

# ==============================================================================
# FUNGSI ABSENSI OTOMATIS (MESIN ABSEN)
# ==============================================================================
def log_absen_otomatis(nama_user):
    if nama_user.lower() in ["dian", "tamu"]: return
    
    url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
    tz_wib = pytz.timezone('Asia/Jakarta')
    waktu_skrg = datetime.now(tz_wib)
    
    jam = waktu_skrg.hour
    tgl_skrg = waktu_skrg.strftime("%Y-%m-%d")
    jam_skrg = waktu_skrg.strftime("%H:%M")

    if 8 <= jam < 10: 
        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
            client = gspread.authorize(creds)
            sheet_absen = client.open_by_url(url_gsheet).worksheet("Absensi")
            
            # AMBIL DATA & BERSIHKAN
            data_mentah = sheet_absen.get_all_records()
            df_absen = bersihkan_data(pd.DataFrame(data_mentah))
            
            nama_up = nama_user.upper()
            
            # CEK APAKAH SUDAH ADA (Tanpa bingung Huruf Besar/Kecil)
            sudah_absen = False
            if not df_absen.empty:
                sudah_absen = any((df_absen['TANGGAL'].astype(str) == tgl_skrg) & (df_absen['NAMA'] == nama_up))
            
            if not sudah_absen:
                sheet_absen.append_row([nama_up, tgl_skrg, jam_skrg, "HADIR"])
                st.toast(f"⏰ Absen Berhasil (Jam {jam_skrg})", icon="✅")
        except:
            pass

# ==============================================================================
# BAGIAN 2: SISTEM KEAMANAN & INISIALISASI DATA (SESSION STATE)
# ==============================================================================
def inisialisasi_keamanan():
    if 'sudah_login' not in st.session_state:
        st.session_state.sudah_login = False
    
    # INISIALISASI MASTER DATA (VERSI CLEAN)
    if 'data_produksi' not in st.session_state:
        st.session_state.data_produksi = {
            "jumlah_karakter": 2,
            "karakter": [ {"nama": "", "wear": "", "fisik": ""} for _ in range(4) ],
            "jumlah_adegan": 5,
            "adegan": {i: {
                "aksi": "", 
                "style": OPTS_STYLE[0], 
                "light": OPTS_LIGHT[0], 
                "arah": OPTS_ARAH[0], 
                "shot": OPTS_SHOT[0], 
                "cam": OPTS_CAM[0], 
                "loc": "", 
                "dialogs": [""]*4
            } for i in range(1, 51)}, 
            "form_version": 0
        }

    params = st.query_params
    if "auth" in params and params["auth"] == "true":
        if not st.session_state.sudah_login:
            st.session_state.sudah_login = True
            st.session_state.user_aktif = params.get("user", "User").lower()
            st.session_state.waktu_login = datetime.now()

def proses_login(user, pwd):
    if user in DAFTAR_USER and DAFTAR_USER[user] == pwd:
        st.session_state.sudah_login = True
        st.session_state.user_aktif = user.lower()
        st.session_state.waktu_login = datetime.now()
        
        # AKTIVASI ABSEN
        log_absen_otomatis(user)
        
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
            if submit: 
                proses_login(u, p)
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
    st.session_state.clear()
    st.query_params.clear()
    st.rerun()

# FUNGSI BACKUP (SINKRON UPPERCASE)
def simpan_ke_gsheet():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
        client = gspread.authorize(creds)
        
        url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
        sheet = client.open_by_url(url_gsheet).sheet1
        
        tz_wib = pytz.timezone('Asia/Jakarta')
        waktu = datetime.now(tz_wib).strftime("%d/%m/%Y %H:%M:%S")
        
        # PENTING: Paksa User jadi UPPER agar sinkron dengan Restore
        user = st.session_state.get("user_aktif", "STAFF").upper()
        data_json = json.dumps(st.session_state.data_produksi)
        
        sheet.append_row([user, waktu, data_json])
        st.toast("🚀 Berhasil disimpan ke Cloud!", icon="☁️")
    except Exception as e:
        st.error(f"Gagal Simpan Cloud: {e}")

# FUNGSI RESTORE (SINKRON HEADER & USER)
def muat_dari_gsheet():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
        client = gspread.authorize(creds)
        
        url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
        sheet = client.open_by_url(url_gsheet).sheet1
        
        # 1. Ambil data dan paksa UPPERCASE lewat bersihkan_data
        semua_data = sheet.get_all_records()
        df_temp = pd.DataFrame(semua_data)
        df_temp = bersihkan_data(df_temp) 
        
        # 2. Ambil username aktif dan paksa ke UPPERCASE
        user_up = st.session_state.get("user_aktif", "").upper()
        
        # 3. Bersihkan kolom USERNAME agar pencarian akurat
        if 'USERNAME' in df_temp.columns:
            df_temp['USERNAME'] = df_temp['USERNAME'].astype(str).str.strip().str.upper()
        
        user_rows = df_temp[df_temp['USERNAME'] == user_up].to_dict('records')
        
        if user_rows:
            # PENTING: Cari kolom naskah secara fleksibel (karena bersihkan_data merubah ke UPPER)
            target_col = 'DATA_NASKAH' if 'DATA_NASKAH' in user_rows[-1] else 'Data_Naskah'
            naskah_mentah = user_rows[-1].get(target_col)
            
            if naskah_mentah:
                data_termuat = json.loads(naskah_mentah)
                
                # --- PROSES PERBAIKAN STRUKTUR (VERSI KLIMIS) ---
                if "adegan" in data_termuat:
                    adegan_baru = {}
                    for k, v in data_termuat["adegan"].items():
                        # Buang sampah & Bersihkan spasi dropdown (Agar Bug UI Poin 3 hilang)
                        for field in ["style", "shot", "light", "arah", "cam"]:
                            if field in v:
                                v[field] = str(v[field]).strip()
                        
                        v.pop("ekspresi", None)
                        v.pop("cuaca", None)
                        v.pop("vibe", None)
                        v.pop("ratio", None)
                        
                        adegan_baru[int(k)] = v 
                    data_termuat["adegan"] = adegan_baru
                
                st.session_state.data_produksi = data_termuat
                st.session_state.form_version = st.session_state.get("form_version", 0) + 1
                
                st.success(f"🔄 Naskah {user_up} Berhasil Dipulihkan!")
                st.rerun()
            else:
                st.error("⚠️ Kolom data naskah tidak ditemukan!")
        else:
            st.warning(f"⚠️ Data untuk {user_up} tidak ditemukan di Cloud.")
    except Exception as e:
        st.error(f"Gagal memuat: {e}")
        
# ==============================================================================
# BAGIAN 3: PENGATURAN TAMPILAN (CSS) - TOTAL BORDERLESS & STATIC
# ==============================================================================
def pasang_css_kustom():
    st.markdown("""
        <style>
        /* 1. DASAR APLIKASI & SCROLLBAR */
        .stApp { background-color: #0b0e14; color: #e0e0e0; }
        [data-testid="stSidebar"] { 
            background-color: #1a1c24 !important; 
            border-right: 1px solid rgba(29, 151, 108, 0.1) !important; 
        }
        
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #0e1117; }
        ::-webkit-scrollbar-thumb { background: #31333f; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #1d976c; }

        /* 2. FIXED HEADER (STATION & JAM) */
        [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) {
            position: fixed; top: 0; left: 310px; right: 0; z-index: 99999;
            background-color: #0e1117; padding: 10px 2rem; border-bottom: 2px solid #31333f;
        }
        @media (max-width: 768px) {
            [data-testid="stMainViewContainer"] section.main div.block-container > div:nth-child(1) { left: 0; }
        }

        /* 3. HANYA TOMBOL GENERATE YANG HIJAU (PRIMARY) */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(to right, #1d976c, #11998e) !important;
            color: white !important; 
            border: none !important; 
            border-radius: 8px !important;
            padding: 10px 20px !important;
            margin-top: 15px !important;
            margin-bottom: 10px !important;
            font-weight: bold !important;
            font-size: 14px !important;
            width: 100%; 
            box-shadow: 0 4px 12px rgba(29, 151, 108, 0.2) !important;
        }

        /* 4. MODE TANPA GARIS (BORDERLESS) PADA SEMUA INPUT */
        .stTextArea textarea, 
        .stTextInput input, 
        div[data-testid="stNumberInput"], 
        div[data-baseweb="input"],
        div[data-baseweb="textarea"],
        [data-baseweb="base-input"] {
            border: none !important;
            box-shadow: none !important;
            outline: none !important;
            background-color: #0d1117 !important;
            border-radius: 10px !important;
            color: #ffffff !important;
        }
        
        .stTextArea textarea:focus, 
        .stTextInput input:focus, 
        div[data-testid="stNumberInput"]:focus-within,
        div[data-baseweb="input"]:focus-within,
        [data-baseweb="base-input"]:focus-within {
            border: none !important;
            box-shadow: none !important;
            outline: none !important;
        }

        /* 5. STAFF HEADER & LABEL */
        .staff-header-premium {
            background: rgba(29, 151, 108, 0.2) !important;
            border: 2px solid #1d976c !important;
            border-radius: 10px !important;
            padding: 15px 20px !important; margin-bottom: 25px !important;
            display: flex !important; align-items: center !important; gap: 12px !important;
        }
        .staff-header-premium b { color: #1d976c !important; font-size: 1.15em !important; }
        
        .small-label {
            color: #1d976c !important; font-size: 10px !important;
            font-weight: 800 !important; letter-spacing: 1px; text-transform: uppercase;
            margin-bottom: 5px !important; display: block;
        }

        /* 6. KOMPONEN LAIN - KETEBALAN STANDAR WARNA DEFAULT */
        .stExpander {
            /* 1px adalah ukuran standar yang paling pas, warna abu-abu gelap */
            border: 1px solid #30363d !important; 
            border-radius: 12px !important; 
            background-color: #161922 !important;
            margin-bottom: 10px !important;
        }
        
        .status-footer { font-size: 11px !important; color: #8b949e !important; font-family: monospace; }
        
        /* Garis pemisah (hr) tipis warna default */
        hr { 
            border: none !important;
            border-top: 1px solid #30363d !important; 
            opacity: 0.3 !important; /* Dibuat samar agar dashboard terlihat bersih */
            margin: 15px 0 !important;
        }

        /* 7. PENGATURAN INPUT HALAMAN LOGIN */
        .stForm div[data-baseweb="input"] {
            background-color: #1a1f26 !important;
            border: 1px solid #30363d !important;
        }
        .stForm input {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }
        .stForm label p {
            color: #e0e0e0 !important;
            font-weight: 600 !important;
            font-size: 14px !important;
        }
        /* 8. COPY TO CLIPBOARD - BUTTON STYLING */
        /* Kotak kodenya kita buat lebih tegas */
        .stCodeBlock {
            border: 1px solid #30363d !important;
            border-radius: 10px !important;
            background-color: #0d1117 !important;
            padding: 10px !important;
        }
        
        /* Tombol copy bawaan Streamlit dibuat besar & berwarna hijau */
        button[title="Copy to clipboard"] {
            background-color: #238636 !important;
            color: white !important;
            transform: scale(1.6); /* Memperbesar ukuran ikon */
            margin-right: 15px !important;
            margin-top: 15px !important;
            border-radius: 6px !important;
            border: none !important;
            transition: all 0.2s ease-in-out !important;
        }
        
        /* Efek saat kursor menempel (Hover) */
        button[title="Copy to clipboard"]:hover {
            background-color: #2ea043 !important;
            transform: scale(1.8) !important;
            cursor: pointer !important;
        }

        /* Menghilangkan background bawaan agar warna hijau kita solid */
        button[title="Copy to clipboard"]:active {
            background-color: #3fb950 !important;
        }

        /* 9. PROTEKSI LAYAR (PC ONLY) - DI POSISI PALING BAWAH */
        @media (max-width: 1024px) {
            [data-testid="stAppViewContainer"], [data-testid="stSidebar"], .main { display: none !important; }
            body::before {
                content: "⚠️ Akses Diblokir!";
                display: flex; justify-content: center; align-items: center;
                height: 100vh; width: 100vw; background: #0e1117; color: white;
                position: fixed; top: 0; left: 0; z-index: 9999; text-align: center; padding: 20px;
                font-family: sans-serif; font-weight: bold;
            }
        }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# BAGIAN 4: NAVIGASI SIDEBAR (VERSI CLOUD ONLY)
# ==============================================================================
def tampilkan_navigasi_sidebar():
    with st.sidebar:
        # 1. JUDUL DENGAN IKON (Sesuai Gambar)
        st.markdown("""
            <div style='display: flex; align-items: center; margin-bottom: 10px; margin-top: 10px;'>
                <span style='font-size: 20px; margin-right: 10px;'>🖥️</span>
                <span style='font-size: 14px; color: white; font-weight: bold; letter-spacing: 1px;'>
                    MAIN COMMAND
                </span>
            </div>
        """, unsafe_allow_html=True)
        
        # 2. MENU RADIO (Daftar Pilihan)
        pilihan = st.radio(
            "COMMAND_MENU",
            [
                "🚀 RUANG PRODUKSI", 
                "🧠 PINTAR AI LAB", 
                "⚡ QUICK PROMPT", 
                "📋 TUGAS KERJA", 
                "⚡ KENDALI TIM"
            ],
            label_visibility="collapsed"
        )
        
        # 3. GARIS PEMISAH & SPASI KE BAWAH
        st.markdown("<hr style='margin: 20px 0; border-color: #30363d;'>", unsafe_allow_html=True)
        
        # 1. KOTAK DURASI FILM
        st.markdown("<p class='small-label'>🎬 DURASI FILM (ADEGAN)</p>", unsafe_allow_html=True)
        st.session_state.data_produksi["jumlah_adegan"] = st.number_input(
            "Jumlah Adegan", 1, 50, 
            value=st.session_state.data_produksi["jumlah_adegan"],
            label_visibility="collapsed"
        )
        
        # 2. SISTEM DATABASE CLOUD (GSHEET)
        st.markdown("<p class='small-label'>☁️ CLOUD DATABASE (GSHEET)</p>", unsafe_allow_html=True)
        
        # Tombol Backup & Restore Berdampingan dengan tampilan default
        col1, col2 = st.columns(2)
        with col1:
            # type="primary" dihapus agar warnanya default (abu-abu)
            if st.button("📤 BACKUP", use_container_width=True): 
                simpan_ke_gsheet()
        with col2:
            if st.button("🔄 RESTORE", use_container_width=True):
                muat_dari_gsheet()
                
        st.markdown('<div style="margin-top: 50px;"></div>', unsafe_allow_html=True)   
        
        if st.button("⚡ KELUAR SISTEM", use_container_width=True):
            proses_logout()
        
        user = st.session_state.get("user_aktif", "USER").upper()
        st.markdown(f'''
            <div style="border-top: 1px solid #30363d; padding-top: 15px; margin-top: 10px;">
                <p class="status-footer">
                    🛰️ STATION: {user}_SESSION<br>
                    🟢 STATUS: AKTIF
                </p>
            </div>
        ''', unsafe_allow_html=True)
        
    return pilihan

# ==============================================================================
# BAGIAN 5: PINTAR AI LAB - PRO EDITION (SYNCHRONIZED MANTRA)
# ==============================================================================

def tampilkan_ai_lab():
    st.title("🧠 PINTAR AI LAB")
    st.info("🚀 **Gaskeun!** Ide cerita di mode **Manual**, atau langsung jadi naskah di mode **Otomatis**!")
    
    # --- 1. KONFIGURASI & SESSION STATE ---
    if 'lab_hasil_otomatis' not in st.session_state: st.session_state.lab_hasil_otomatis = ""
    if 'jumlah_karakter' not in st.session_state: st.session_state.jumlah_karakter = 2
    if 'memori_n' not in st.session_state: st.session_state.memori_n = {}
    if 'memori_s' not in st.session_state: st.session_state.memori_s = {}
    
    # 4 NICHE UTAMA
    opsi_pola = [
        "Revenge (Direndahkan -> Balas Dendam)",
        "Empathy (Iba -> Pesan Moral)",
        "Absurd Race (Lomba Konyol -> Interaktif CTA)",
        "Knowledge (Fakta Harian -> Edukasi)"
    ]
    opsi_visual = ["Sangat Nyata", "Gaya Cyberpunk", "3D Pixar Style", "Anime Style"]

    try:
        api_key_groq = st.secrets["GROQ_API_KEY"]
    except:
        api_key_groq = None

    # --- 2. AREA PENGATURAN KARAKTER ---
    st.subheader("👤 Pengaturan Karakter")
    c_add, c_rem, c_spacer = st.columns([0.25, 0.25, 0.5])
    with c_add:
        if st.button("➕ Tambah Karakter", use_container_width=True) and st.session_state.jumlah_karakter < 4:
            st.session_state.jumlah_karakter += 1
            st.rerun()
    with c_rem:
        if st.button("➖ Kurang Karakter", use_container_width=True) and st.session_state.jumlah_karakter > 1:
            st.session_state.jumlah_karakter -= 1
            st.rerun()

    list_karakter = []
    with st.expander("👥 DETAIL KARAKTER", expanded=True):
        char_cols = st.columns(2)
        for i in range(st.session_state.jumlah_karakter):
            if i not in st.session_state.memori_n: st.session_state.memori_n[i] = ""
            if i not in st.session_state.memori_s: st.session_state.memori_s[i] = ""
            with char_cols[i % 2]:
                with st.container(border=True):
                    label_k = "Karakter Utama" if i == 0 else f"Karakter {i+1}"
                    st.markdown(f"**{label_k}**")
                    st.session_state.memori_n[i] = st.text_input(f"N{i}", value=st.session_state.memori_n[i], key=f"inp_n_{i}", placeholder="Nama...", label_visibility="collapsed")
                    st.session_state.memori_s[i] = st.text_input(f"S{i}", value=st.session_state.memori_s[i], key=f"inp_s_{i}", placeholder="Detail sifat/fisik...", label_visibility="collapsed")
                    n_f = st.session_state.memori_n[i] if st.session_state.memori_n[i] else label_k
                    list_karakter.append(f"{i+1}. {n_f.upper()}: {st.session_state.memori_s[i]}")

    st.write("---")

    # --- 3. TAB MENU (MANUAL & OTOMATIS) ---
    tab_manual, tab_otomatis = st.tabs(["🛠️ Mode Manual", "⚡ Mode Otomatis"])

    # MODE MANUAL
    with tab_manual:
        with st.expander("📝 KONFIGURASI MANUAL", expanded=True):
            col_m1, col_m2 = st.columns([2, 1])
            with col_m1:
                st.markdown("**📝 Topik Utama**")
                topik_m = st.text_area("T", placeholder="Ketik ide ceritanya di sini...", height=245, key="m_topik", label_visibility="collapsed")
            with col_m2:
                st.markdown("**🎭 Pola & Style**")
                pola_m = st.selectbox("Pola", opsi_pola, key="m_pola")
                visual_m = st.selectbox("Visual", opsi_visual, key="m_visual")
                adegan_m = st.number_input("Jumlah Adegan", 3, 15, 12, key="m_adegan")

            if st.button("✨ GENERATE NASKAH CERITA", use_container_width=True, type="primary"):
                if topik_m:
                    str_k = "\n".join(list_karakter)
                    mantra_sakti = f"""Kamu adalah Scriptwriter Pro Pintar Media. 
Buatkan naskah YouTube Shorts VIRAL dalam format TABEL MARKDOWN (Siap Copy-Paste ke GSheet).

--- DAFTAR KARAKTER & DETAIL FISIK ---
{str_k}

--- KONSEP UTAMA ---
Topik: {topik_m}
Pola: {pola_m}
Total Adegan: {adegan_m} (WAJIB {adegan_m} ADEGAN)

--- LOGIKA ALUR PER POLA (DIBAGI DALAM {adegan_m} ADEGAN) ---
{f''' - ALUR REVENGE: Adegan 1-5 (Protagonis dihina/hartanya dirusak Antagonis), Adegan 6 (CTA Like/Subs via Dialog), Adegan 7-10 (Balas Dendam Savage/Anomali secara realistis), Adegan 11-12 (Ending Kepuasan Penonton).''' if pola_m == opsi_pola[0] else ''}
{f''' - ALUR EMPATHY: Adegan 1-5 (Hook masalah nyesek/iba), Adegan 6 (CTA Like/Subs via Dialog), Adegan 7-10 (Perjuangan emosional karakter), Adegan 11-12 (Ending Haru).''' if pola_m == opsi_pola[1] else ''}
{f''' - ALUR ABSURD RACE: Adegan 1-4 (Lomba konyol dimulai), Adegan 5-8 (Lomba chaos/lucu), Adegan 9-10 (Momen kritis), Adegan 11-12 (Hasil lomba & WAJIB CTA penonton tentukan pemenang via Like/Subs).''' if pola_m == opsi_pola[2] else ''}
{f''' - ALUR KNOWLEDGE: Adegan 1-3 (Fakta unik awal), Adegan 4-6 (Dampak jangka pendek), Adegan 7-10 (Dampak jangka panjang/1 tahun kemudian), Adegan 11-12 (Edukasi penutup).''' if pola_m == opsi_pola[3] else ''}

--- STANDAR PRODUKSI (WAJIB PATUH) ---
1. LOKASI: Wajib DESKRIPTIF & DETAIL (Minimal 10-15 kata, gambarkan suasana lingkungan, benda sekitar, dan cuaca).
2. NO MORAL: Jangan ada pesan moral atau nasihat bijak di akhir cerita.
3. NO TEXT: Tanpa teks di layar, semua pesan disampaikan lewat visual dan dialog.
4. BAHASA: Sehari hari (mudah dimengerti oleh penonton).

--- FORMAT TABEL (KOLOM GSHEET) ---
ID_IDE | JUDUL | STATUS | NASKAH_VISUAL | DIALOG_ACTOR_1 | DIALOG_ACTOR_2 | STYLE | UKURAN_GAMBAR | LIGHTING | ARAH_KAMERA | GERAKAN | LOKASI

--- DROPDOWN VALID ---
- STYLE: [{visual_m}]
- UKURAN_GAMBAR: [Seluruh Badan / Setengah Badan / Sangat Dekat / Wajah & Bahu]
- LIGHTING: [Siang Alami / Malam Indigo / Senja Cerah / Neon Cyberpunk / Fajar]
- ARAH_KAMERA: [Sejajar Mata / Dari Atas / Dari Bawah / Dari Samping / Dari Belakang]
- GERAKAN: [Diam (Tetap Napas) / Maju Perlahan / Ikuti Karakter / Goyang (Handheld)]

Balas HANYA tabel Markdown.
"""
                    st.divider()
                    st.success("✨ **Mantra ide cerita Siap!**")
                    st.code(mantra_sakti, language="text")

    # MODE OTOMATIS
    with tab_otomatis:
        with st.expander("⚡ KONFIGURASI OTOMATIS", expanded=True):
            col_o1, col_o2 = st.columns([2, 1])
            with col_o1:
                st.markdown("**📝 Topik Utama**")
                topik_o = st.text_area("O", placeholder="Ketik ide ceritanya di sini...", height=245, key="o_topik", label_visibility="collapsed")
            with col_o2:
                st.markdown("**⚙️ Konfigurasi Otomatis**")
                pola_o = st.selectbox("Pola Cerita", opsi_pola, key="o_pola")
                adegan_o = st.number_input("Jumlah Adegan", 3, 15, 12, key="o_adegan_api")

            if st.button("🔥 GENERATE NASKAH CERITA", use_container_width=True, type="primary"):
                if api_key_groq and topik_o:
                    with st.spinner("lagi ngetik naskah..."):
                        try:
                            import requests
                            headers = {"Authorization": f"Bearer {api_key_groq}", "Content-Type": "application/json"}
                            str_k = "\n".join(list_karakter)
                            
                            prompt_otomatis = f"""Kamu adalah Creative Director & Scriptwriter Pro Pintar Media. 
Buatkan naskah YouTube Shorts VIRAL dalam format TABEL MARKDOWN.

--- DAFTAR KARAKTER & DETAIL FISIK ---
{str_k}

KONSEP:
Topik: {topik_o}
Pola: {pola_o}
Total Adegan: {adegan_o} (WAJIB {adegan_o} ADEGAN)

--- ATURAN MAIN (STRICT PRODUKSI) ---
1. NASKAH_VISUAL: WAJIB DESKRIPTIF & PANJANG (Minimal 30-40 kata per adegan) Jelaskan aksi karakter, ekspresi wajah secara detail, dan interaksi dengan benda di sekitarnya.
2. LOKASI: Harus Detail (Minimal 15 kata) Gambarkan suasana lingkungan, dan tumpukan benda/detail latar belakang agar terlihat nyata.
3. DIALOG: Buat dialog yang natural, emosional. Gunakan bahasa sehari-hari yang luwes.
4. NO MORAL & NO TEXT: Tanpa pesan moral dan tanpa teks di layar.
5. STRUKTUR: Bagi {adegan_o} adegan menjadi fase Awal (Konflik), Tengah (Puncak/CTA Like & Subs), dan Akhir (Pembalasan Savage/Anomali).

--- FORMAT TABEL (WAJIB 5 KOLOM) ---
JUDUL | NASKAH_VISUAL | DIALOG_ACTOR_1 | DIALOG_ACTOR_2 | LOKASI

Balas HANYA tabel Markdown tanpa penjelasan apa pun.
"""
                            payload = {
                                "model": "llama-3.3-70b-versatile", 
                                "messages": [{"role": "user", "content": prompt_otomatis}],
                                "temperature": 0.7
                            }
                            res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
                            st.session_state.lab_hasil_otomatis = res.json()['choices'][0]['message']['content']
                            st.toast("Naskah Berhasil Dibuat!", icon="✅")
                        except Exception as e:
                            st.error(f"Error: {e}")

        if st.session_state.lab_hasil_otomatis:
            with st.expander("🎬 NASKAH JADI (OTOMATIS)", expanded=True):
                st.markdown(st.session_state.lab_hasil_otomatis)
                st.divider()
                btn_col1, btn_col2, btn_col3 = st.columns(3)
                with btn_col1:
                    if st.button("🚀 KIRIM KE RUANG PRODUKSI", use_container_width=True):
                        if 'data_produksi' not in st.session_state: st.session_state.data_produksi = {}
                        st.session_state.naskah_siap_produksi = st.session_state.lab_hasil_otomatis
                        st.toast("Naskah sukses terkirim!", icon="🚀")
                with btn_col2:
                    if st.button("🗑️ BERSIHKAN NASKAH", use_container_width=True):
                        st.session_state.lab_hasil_otomatis = ""
                        st.rerun()
                with btn_col3:
                    st.download_button("📥 DOWNLOAD (.txt)", st.session_state.lab_hasil_otomatis, file_name="naskah.txt", use_container_width=True)
                
def tampilkan_quick_prompt():
    st.title("⚡ QUICK PROMPT")
    st.info(f"💡 **INFO :** Pada bagian ini, tidak bisa simpan atau restore data.")

    # --- A. SETTINGAN LOKAL ---
    QB_IMG_LOKAL = (
        "8k RAW optical clarity, cinematic depth of field, f/1.8 aperture, "
        "bokeh background, razor-sharp focus on subject detail, "
        "high-index lens glass look, CPL filter, sub-surface scattering, "
        "physically-based rendering, hyper-detailed surface micro-textures, "
        "anisotropic filtering, ray-traced ambient occlusion"
    )

    QB_VID_LOKAL = (
        "Unreal Engine 5.4, 24fps cinematic motion, ultra-clear, 8k UHD, high dynamic range, "
        "professional color grading, ray-traced reflections, hyper-detailed textures, "
        "temporal anti-aliasing, zero digital noise, clean pixels, "
        "smooth motion interpolation, high-fidelity physical interaction"
    )

    NEG_LOKAL = (
        "muscular, bodybuilder, shredded, male anatomy, human skin, human anatomy, "
        "realistic flesh, skin pores, blurry, distorted surface, "
        "STRICTLY NO text, NO typography, NO watermark, NO letters, NO subtitles, "
        "NO captions, NO speech bubbles, NO dialogue boxes, NO labels, NO black bars"
    )

    # --- B. BRANKAS DATA (DIPERBARUI) ---
    if "qp_data" not in st.session_state:
        st.session_state.qp_data = {
            "name_a": "", "det_a": "", "name_b": "", "det_b": "",
            "loc": "", "act": "", "dial_a": "", "dial_b": "", "spk": []
        }
    
    # PENGAMAN TAMBAHAN: Mencegah KeyError
    if "dial_a" not in st.session_state.qp_data:
        st.session_state.qp_data["dial_a"] = ""
    if "dial_b" not in st.session_state.qp_data:
        st.session_state.qp_data["dial_b"] = ""

    # --- C. FORMULIR ---
    with st.expander("📝 FORMULIR PROMPT SINGKAT", expanded=True):
        col_a, col_b = st.columns(2)
        with col_a:
            q_char_a = st.text_input("Nama Karakter 1", value=st.session_state.qp_data["name_a"], placeholder="Contoh: Rumi")
            st.session_state.qp_data["name_a"] = q_char_a
            q_detail_a = st.text_area("Fisik & Baju (1)", value=st.session_state.qp_data["det_a"], height=80)
            st.session_state.qp_data["det_a"] = q_detail_a
        with col_b:
            q_char_b = st.text_input("Nama Karakter 2", value=st.session_state.qp_data["name_b"], placeholder="Contoh: Tung")
            st.session_state.qp_data["name_b"] = q_char_b
            q_detail_b = st.text_area("Fisik & Baju (2)", value=st.session_state.qp_data["det_b"], height=80)
            st.session_state.qp_data["det_b"] = q_detail_b
        
        q_lokasi = st.text_input("📍 Lokasi", value=st.session_state.qp_data["loc"])
        st.session_state.qp_data["loc"] = q_lokasi
        
        # Pintar AI Logic
        if st.button("🪄 Pintar AI (Perjelas Adegan)", use_container_width=True):
            api_key = st.secrets.get("GROQ_API_KEY")
            if api_key and st.session_state.qp_data["act"]:
                with st.spinner("Memoles adegan..."):
                    try:
                        headers = {"Authorization": f"Bearer {api_key}"}
                        p_ai = f"Ubah aksi ini jadi deskripsi visual sinematik 2 kalimat: {st.session_state.qp_data['act']}"
                        res = requests.post("https://api.groq.com/openai/v1/chat/completions", 
                                            headers=headers, 
                                            json={"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": p_ai}]})
                        if res.status_code == 200:
                            st.session_state.qp_data["act"] = res.json()['choices'][0]['message']['content'].strip()
                            st.rerun()
                    except: st.error("AI Error")

        q_aksi = st.text_area("🏃 Apa yang terjadi?", value=st.session_state.qp_data["act"])
        st.session_state.qp_data["act"] = q_aksi

        c1, c2, c3, c4 = st.columns(4)
        with c1: q_shot = st.selectbox("📸 Shot Size", ["Lanskap", "Seluruh Badan", "Setengah Badan", "Close Up", "Extreme Close Up"], index=2)
        with c2: q_arah = st.selectbox("🎥 Arah Kamera", ["Sejajar Mata", "Dari Bawah", "Dari Atas", "Dari Samping", "Belakang Karakter"], index=0)
        with c3: q_style = st.selectbox("🎨 Visual Style", ["Sangat Nyata", "Animasi 3D Pixar", "Gaya Cyberpunk", "Anime Jepang"], index=0)
        with c4: q_light = st.selectbox("💡 Lighting", ["Sinar Senja", "Siang Alami", "Neon Cyberpunk", "Malam Indigo", "Malam Hari"], index=1)

        st.divider()
        st.markdown("💬 **DIALOG (Obrolan)**")
        d_col1, d_col2 = st.columns(2)
        with d_col1:
            q_dial_a = st.text_area(f"Dialog {q_char_a if q_char_a else 'Karakter 1'}", value=st.session_state.qp_data["dial_a"], height=80, key="q_dial_a_input")
            st.session_state.qp_data["dial_a"] = q_dial_a
        with d_col2:
            q_dial_b = st.text_area(f"Dialog {q_char_b if q_char_b else 'Karakter 2'}", value=st.session_state.qp_data["dial_b"], height=80, key="q_dial_b_input")
            st.session_state.qp_data["dial_b"] = q_dial_b

    # --- E. LOGIKA RAKIT PROMPT (SMART FILTER + PHYSICS + DIALOG REFORM) ---
    if q_aksi and q_lokasi:
        aksi_lower = q_aksi.lower()
        active_characters = []
        
        # 1. SCANNER IDENTITAS
        if q_char_a and q_char_a.lower() in aksi_lower:
            active_characters.append(f"[[ ACTOR_1_SKS ({q_char_a.upper()}): refer to PHOTO #1 ONLY. WEAR: {q_detail_a} ]]")
        if q_char_b and q_char_b.lower() in aksi_lower:
            active_characters.append(f"[[ ACTOR_2_SKS ({q_char_b.upper()}): refer to PHOTO #2 ONLY. WEAR: {q_detail_b} ]]")

        if active_characters:
            char_identity_string = " AND ".join(active_characters)
            final_identity_rule = f"IMAGE REFERENCE RULE: Use uploaded photos for each character. Interaction required. {char_identity_string}"
        else:
            final_identity_rule = f"[[ ACTOR_1_SKS ({q_char_a.upper() if q_char_a else 'CHAR1'}): {q_detail_a} ]]"

        # 2. DIALOG REFORMER (Sesuai Form Terpisah)
        raw_dialogs = []
        if q_dial_a.strip():
            raw_dialogs.append(f"[{q_char_a.upper() if q_char_a else 'CHAR1'}_DIALOG]: '{q_dial_a.strip()}'")
        if q_dial_b.strip():
            raw_dialogs.append(f"[{q_char_b.upper() if q_char_b else 'CHAR2'}_DIALOG]: '{q_dial_b.strip()}'")

        if raw_dialogs:
            emotional_ref = " | ".join(raw_dialogs)
            acting_cue_final = (
                f"Use these individual dialogue cues for emotional reference only: {emotional_ref}. "
                f"STRICTLY focus mouth movement and lip-sync ONLY on the active speaker. Others must remain silent."
            )
        else:
            acting_cue_final = "Neutral Interaction"

        # 3. PHYSICS & VISUAL MAPPING (Penerjemah Bahasa AI Pro)
        q_style_map = {
            "Sangat Nyata": "Cinematic RAW shot, high-fidelity textures, 8k UHD, ray-traced lighting",
            "Animasi 3D Pixar": "Stylized 3D render, expressive character design, global illumination",
            "Gaya Cyberpunk": "Cyberpunk aesthetic, neon-drenched atmosphere, futuristic noir",
            "Anime Jepang": "High-quality 2D cel-shaded, Studio Ghibli aesthetic, hand-drawn textures"
        }
        
        q_shot_map = {
            "Lanskap": "Wide-angle cinematic vista",
            "Seluruh Badan": "Full-length portrait, wide framing",
            "Setengah Badan": "Waist-up medium shot",
            "Close Up": "Tight portrait, facial detail focus",
            "Extreme Close Up": "Extreme macro lens focus"
        }

        q_arah_map = {
            "Sejajar Mata": "Eye-level perspective, neutral camera angle",
            "Dari Bawah": "Low-angle heroic shot, looking upward",
            "Dari Atas": "High-angle perspective, bird's-eye view",
            "Dari Samping": "Profile view, 90-degree lateral angle",
            "Belakang Karakter": "Over-the-shoulder perspective, rear-view framing"
        }
        
        q_light_map = {
            "Sinar Senja": "Golden hour glow, amber warmth, long shadows",
            "Siang Alami": "Organic daylight, soft diffusion, bright atmosphere",
            "Neon Cyberpunk": "Vivid neon highlights, purple and cyan color-grading",
            "Malam Indigo": "Deep twilight tones, blue-hour ambiance",
            "Malam Hari": "Low-light cinematic contrast, moody shadows"
        }

        # Menjalankan Mapping Lokal
        v_style = q_style_map.get(q_style, q_style)
        v_shot = q_shot_map.get(q_shot, q_shot)
        v_arah = q_arah_map.get(q_arah, q_arah)
        v_light = q_light_map.get(q_light, q_light)

        physics_guard = "PHYSICS RULE: Strict object permanence. All handheld items stay firmly attached. No clipping."
        
        # 4. RAKIT OUTPUT FINAL
        p_img = (
            f"{final_identity_rule}\n\n"
            f"SCENE: {q_aksi} at {q_lokasi}. {physics_guard}\n"
            f"VISUAL: {v_style}, {v_shot}, {v_arah}, {v_light}.\n"
            f"QUALITY: {QB_IMG_LOKAL}\n"
            f"NEGATIVE: {NEG_LOKAL}"
        )

        p_vid = (
            f"{final_identity_rule}\n\n"
            f"SCENE: {q_aksi} with {v_shot} framing at {v_arah} perspective at {q_lokasi}. {physics_guard}\n"
            f"ACTING CUE (STRICTLY NO TEXT ON SCREEN): {acting_cue_final}\n"
            f"QUALITY: {QB_VID_LOKAL}, fluid mouth movement, consistent facial features\n"
            f"NEGATIVE: {NEG_LOKAL}"
        )

        # --- TAMPILKAN HASIL ---
        st.divider()
        res_img, res_vid = st.columns(2)
        with res_img:
            st.markdown("##### 📷 PROMPT GAMBAR")
            st.code(p_img, language="text")
        with res_vid:
            st.markdown("##### 🎥 PROMPT VIDEO")
            st.code(p_vid, language="text")
                        
        st.success("✅ Quick Prompt Berhasil! Silahkan langsung copy ke grok atau gemini flow veo.")
            
def kirim_notif_wa(pesan):
    """Fungsi otomatis untuk kirim laporan ke Grup WA YT YT 🔥"""
    token = "f4CApLBAJDTPrVHHZCDF"
    target = "120363407726656878@g.us"
    url = "https://api.fonnte.com/send"
    payload = {'target': target, 'message': pesan, 'countryCode': '62'}
    headers = {'Authorization': token}
    try:
        requests.post(url, data=payload, headers=headers, timeout=10)
    except:
        pass

def hitung_logika_performa_dan_bonus(df_arsip_user, df_absen_user):
    # 1. Pastikan Header Konsisten (UPPERCASE)
    df_arsip_user = bersihkan_data(df_arsip_user)
    df_absen_user = bersihkan_data(df_absen_user)

    tz_wib = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz_wib)
    
    uang_absen_total = 0
    bonus_video_total = 0
    pot_sp = 0
    level_sp = "NORMAL"

    # --- A. HITUNG UANG ABSEN DARI DATA GSHEET ABSENSI ---
    # Ini kuncinya biar Inggi ngga 0 lagi
    if not df_absen_user.empty:
        # Bersihkan spasi di kolom NAMA dan TANGGAL sebelum dihitung
        df_absen_user['NAMA'] = df_absen_user['NAMA'].astype(str).str.strip()
        total_hari_hadir = len(df_absen_user['TANGGAL'].unique())
        uang_absen_total = total_hari_hadir * 30000
    else:
        uang_absen_total = 0

    # --- B. JIKA BELUM ADA VIDEO SELESAI ---
    if df_arsip_user.empty:
        if sekarang.day >= 7:
            return 0, uang_absen_total, 300000, "SP 1 (BELUM ADA KARYA)"
        else:
            return 0, uang_absen_total, 0, "NORMAL (MASA PENILAIAN)"

    # --- C. HITUNG BONUS VIDEO & HARI MALAS ---
    df_arsip_user['Tgl_Setor'] = pd.to_datetime(df_arsip_user['WAKTU_KIRIM'], dayfirst=True, errors='coerce').dt.strftime('%Y-%m-%d')
    rekap_harian = df_arsip_user['Tgl_Setor'].value_counts().to_dict()
    
    total_hari_malas = 0
    for tgl, jml in rekap_harian.items():
        if jml >= 4:
            bonus_video_total += (jml - 3) * 25000 # Bonus mulai video ke-4
        if jml <= 1:
            total_hari_malas += 1

    # --- D. LOGIKA POTONGAN SP ---
    if sekarang.day < 7:
        level_sp = "NORMAL (MASA PENILAIAN)"
        pot_sp = 0
    else:
        if total_hari_malas >= 21:
            level_sp = "SP 3 (CUT OFF)"; pot_sp = 1000000
        elif total_hari_malas >= 14:
            level_sp = "SP 2 (PERINGATAN KERAS)"; pot_sp = 700000
        elif total_hari_malas >= 7:
            level_sp = "SP 1 (PERFORMA BURUK)"; pot_sp = 300000
        
    return bonus_video_total, uang_absen_total, pot_sp, level_sp

def tampilkan_tugas_kerja():
    st.title("🚀 PINTAR INTEGRATED SYSTEM")
    
    url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
    user_sekarang = st.session_state.get("user_aktif", "tamu").lower()
    tz_wib = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz_wib)
    
    foto_staff_default = "https://cdn-icons-png.flaticon.com/512/847/847969.png"
    foto_staff = {
        "icha": "https://cdn-icons-png.flaticon.com/512/6997/6997662.png", 
        "nissa": "https://cdn-icons-png.flaticon.com/512/6997/6997674.png",
        "inggi": "https://cdn-icons-png.flaticon.com/512/6997/6997662.png",
        "lisa": "https://cdn-icons-png.flaticon.com/512/6997/6997674.png"
    }
    
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
        client = gspread.authorize(creds)
        
        # Buka file utama
        sh = client.open_by_url(url_gsheet) 
        
        # Hubungkan ke semua sheet
        sheet_tugas = sh.worksheet("Tugas")
        sheet_log = sh.worksheet("Log_Aktivitas")
        sheet_staff = sh.worksheet("Staff")
        sheet_absensi = sh.worksheet("Absensi")
        sheet_gudang = sh.worksheet("Gudang_Ide") 
        
        data_tugas = sheet_tugas.get_all_records()
        df_all_tugas = pd.DataFrame(data_tugas)
        df_all_tugas = bersihkan_data(df_all_tugas)
        
        if not df_all_tugas.empty:
            df_all_tugas['DEADLINE_DT'] = pd.to_datetime(df_all_tugas['DEADLINE'], errors='coerce')
        
        df_staff_raw = pd.DataFrame(sheet_staff.get_all_records())
        staf_options = df_staff_raw['Nama'].unique().tolist()

        def catat_log(aksi):
            waktu_log = datetime.now(tz_wib).strftime("%d/%m/%Y %H:%M:%S")
            sheet_log.append_row([waktu_log, user_sekarang.upper(), aksi])

    except Exception as e:
        st.error(f"❌ Database Offline: {e}")
        return

    # --- 1. LEADERBOARD ---
    if not df_all_tugas.empty:
        mask_l = (df_all_tugas['DEADLINE_DT'].dt.month == sekarang.month) & \
                 (df_all_tugas['DEADLINE_DT'].dt.year == sekarang.year) & \
                 (df_all_tugas['STATUS'] == "FINISH")
        
        df_finish_l = df_all_tugas[mask_l].copy()
        if not df_finish_l.empty:
            skor = df_finish_l['STAF'].astype(str).str.strip().str.upper().value_counts().reset_index()
            skor.columns = ['Nama', 'Video']
            ranks = skor.values.tolist()
            c1, c2, c3 = st.columns(3)
            with c1: 
                if len(ranks) > 0: st.metric("🥇 JUARA 1", ranks[0][0], f"{ranks[0][1]} Video")
            with c2: 
                if len(ranks) > 1: st.metric("🥈 JUARA 2", ranks[1][0], f"{ranks[1][1]} Video")
            with c3: 
                if len(ranks) > 2: st.metric("🥉 JUARA 3", ranks[2][0], f"{ranks[2][1]} Video")

    st.divider()

    # --- 2. PANEL ADMIN (DEPLOY TUGAS) ---
    if user_sekarang == "dian":
        with st.expander("✨ **KIRIM TUGAS BARU**", expanded=False):
            c2, c1 = st.columns([2, 1]) 
            with c2:
                isi_tugas = st.text_area("Instruksi Tugas", height=150)
            with c1:
                staf_tujuan = st.selectbox("Pilih Editor", staf_options)
                pake_wa = st.checkbox("Kirim Notif WA?", value=True) 

            if st.button("🚀 KIRIM KE EDITOR", use_container_width=True):
                if isi_tugas:
                    t_id = f"ID{datetime.now(tz_wib).strftime('%m%d%H%M%S')}"
                    tgl_deploy = datetime.now(tz_wib).strftime("%Y-%m-%d") 
                    sheet_tugas.append_row([t_id, staf_tujuan, tgl_deploy, isi_tugas, "PROSES", "-", "", ""])
                    catat_log(f"Kirim Tugas Baru {t_id} ke {staf_tujuan}")
                    if pake_wa:
                        kirim_notif_wa(f"✨ *INFO TUGAS BARU*\n\n👤 *Untuk:* {staf_tujuan.upper()}\n🆔 *ID:* {t_id}\n📝 *Detail:* {isi_tugas[:100]}...\n\n_Silakan cek dashboard untuk pengerjaan._ 🚀")
                    st.success("✅ Berhasil terkirim!"); time.sleep(1); st.rerun()

    ### --- 🟢 SISTEM GUDANG BLUEPRINT (VERSI DROPDOWN MASTER) --- ###
    st.subheader("📦 GUDANG IDE PINTAR")
    try:
        data_gudang = sheet_gudang.get_all_records()
        df_gudang = pd.DataFrame(data_gudang)
        
        if not df_gudang.empty:
            # 1. Pastikan list judul unik dan tersedia
            list_judul = df_gudang[df_gudang['STATUS'].astype(str).str.upper() == 'TERSEDIA']['JUDUL'].unique().tolist()
            pilihan_judul = st.selectbox("🎯 Pilih Ide Konten Hari Ini:", ["-- Pilih Judul Cerita --"] + list_judul)

            # 2. LOGIKA INI HANYA JALAN JIKA JUDUL SUDAH DIPILIH
            if pilihan_judul != "-- Pilih Judul Cerita --":
                # Definisi 'row' dilakukan di sini agar aman
                row = df_gudang[df_gudang['JUDUL'] == pilihan_judul].iloc[0]
                
                st.success(f"Kamu memilih: **{row['JUDUL']}**")
                
                # Sekarang Python tahu siapa itu 'row', jadi tombol tidak akan error lagi
                if st.button(f"🚀 AMBIL IDE: {row['ID_IDE']}", use_container_width=True):
                    with st.spinner("⏳ Menyinkronkan Blueprint ke Ruang Produksi..."):
                        # 1. Gunakan Batch Update agar tidak terkena Rate Limit
                        cells = sheet_gudang.findall(str(row['ID_IDE']))
                        if cells:
                            # Ambil baris pertama dan terakhir untuk range update
                            min_row = min(cell.row for cell in cells)
                            max_row = max(cell.row for cell in cells)
                            
                            # Update status untuk seluruh adegan sekaligus dalam satu perintah
                            # Kita asumsikan Kolom 3 adalah kolom STATUS di GSheet Gudang Ide
                            status_baru = [[f"DIAMBIL ({user_sekarang.upper()})"]] * (max_row - min_row + 1)
                            sheet_gudang.update(f'C{min_row}:C{max_row}', status_baru)
                        
                        # 2. Filter data adegan dari dataframe yang sudah ada (lebih cepat drpd panggil GSheet lagi)
                        adegan_rows = df_gudang[df_gudang['ID_IDE'] == row['ID_IDE']]
                        st.session_state.data_produksi["jumlah_adegan"] = len(adegan_rows)
                        
                        # 3. Reset & Isi Adegan Baru
                        rangkuman_naskah = f"### 🎬 ALUR CERITA: {row['JUDUL']}\n\n"
                        
                        for i, (_, a_row) in enumerate(adegan_rows.iterrows(), 1):
                            st.session_state.data_produksi["adegan"][i] = {
                                "aksi": a_row.get('NASKAH_VISUAL', ''),
                                "dialogs": [a_row.get('DIALOG_ACTOR_1', ''), a_row.get('DIALOG_ACTOR_2', ''), "", ""],
                                "style": a_row.get('STYLE', OPTS_STYLE[0]),
                                "shot": a_row.get('UKURAN_GAMBAR', OPTS_SHOT[0]),
                                "light": a_row.get('LIGHTING', OPTS_LIGHT[0]),
                                "arah": a_row.get('ARAH_KAMERA', OPTS_ARAH[0]),
                                "cam": a_row.get('GERAKAN', OPTS_CAM[0]),
                                "loc": a_row.get('LOKASI', '')
                            }
                            rangkuman_naskah += f"**Adegan {i}:** {a_row.get('NASKAH_VISUAL', '')}\n\n"
                        
                        # 4. Finalisasi
                        st.session_state.naskah_siap_produksi = rangkuman_naskah
                        st.session_state.form_version = st.session_state.get("form_version", 0) + 1
                        catat_log(f"Mengambil Blueprint {row['ID_IDE']}")
                        
                        st.toast("✅ Ide Berhasil Dipindahkan!", icon="🚀")
                        time.sleep(1)
                        st.rerun()
    except Exception as e:
        st.warning(f"⚠️ Gagal memuat database ide: {e}")
                    
    # --- 3. DAFTAR TUGAS AKTIF ---
    st.subheader("📑 Tugas On-Progress")

    if user_sekarang != "dian" and user_sekarang != "tamu":
        with st.expander("➕ STAFF: SETOR TUGAS MANDIRI", expanded=False):
            with st.form("form_mandiri", clear_on_submit=True):
                judul_m = st.text_input("Apa yang kamu kerjakan?")
                link_m = st.text_input("Link GDrive Hasil:")
                submit_m = st.form_submit_button("🚀 SETOR SEKARANG", use_container_width=True)
                if submit_m and judul_m and link_m:
                    t_id_m = f"M{datetime.now(tz_wib).strftime('%m%d%H%M%S')}"
                    tgl_m = datetime.now(tz_wib).strftime("%Y-%m-%d")
                    waktu_m = datetime.now(tz_wib).strftime("%d/%m/%Y %H:%M")
                    sheet_tugas.append_row([t_id_m, user_sekarang, tgl_m, judul_m, "WAITING QC", waktu_m, link_m, ""])
                    catat_log(f"Menyetor Tugas Mandiri {t_id_m}")
                    kirim_notif_wa(f"⚡ *SETORAN TUGAS MANDIRI*\n\n👤 *Nama:* {user_sekarang.upper()}\n🆔 *ID:* {t_id_m}\n📝 *Pekerjaan:* {judul_m}\n🔗 *Link:* {link_m}")
                    st.success("✅ Berhasil disetor!"); time.sleep(1); st.rerun()

    tugas_terfilter = []
    if not df_all_tugas.empty:
        if user_sekarang == "dian":
            tugas_terfilter = [t for t in data_tugas if str(t["Status"]).upper() != "FINISH"]
        else:
            tugas_terfilter = [t for t in data_tugas if str(t["Staf"]).lower() == user_sekarang and str(t["Status"]).upper() != "FINISH"]

    if not tugas_terfilter:
        st.info(f"☕ Belum ada tugas aktif.")
    else:
        for t in reversed(tugas_terfilter):
            status = str(t["Status"]).upper()
            nama_key = str(t["Staf"]).lower()
            url_foto = foto_staff.get(nama_key, foto_staff_default)
            
            try: selisih = (sekarang.date() - pd.to_datetime(t['Deadline']).date()).days
            except: selisih = 0
            is_telat = status in ["PROSES", "REVISI"] and selisih >= 2
            
            st.markdown(f'<div style="border: 2px solid {"#ff4b4b" if is_telat else "rgba(255,255,255,0.1)"}; padding: 15px; border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">', unsafe_allow_html=True)
            c1, c2, c3, c4, c5 = st.columns([0.8, 1.5, 1.5, 1.5, 2])
            with c1: st.image(url_foto, width=90)
            with c2: 
                st.write(f"**{str(t['Staf']).upper()}**")
                st.caption(f"{status} {'⚠️ DEADLINE!' if is_telat else ''}")
            with c3: st.caption("🆔 ID"); st.write(t['ID'])
            with c4: st.caption("📅 DEADLINE"); st.write(t['Deadline'])
            with c5: st.caption("⏰ SETOR"); st.write(t['Waktu_Kirim'])

            with st.expander("🔍 CEK TUGAS KERJA HARIAN"):
                st.code(t["Instruksi"])
                if t.get("Link_Hasil") and t["Link_Hasil"] != "-":
                    links = str(t["Link_Hasil"]).split(",")
                    for i, link in enumerate(links):
                        if "http" in link: st.write(f"🔗 [LINK {i+1}]({link.strip()})")
                
                if t.get("Catatan_Revisi"): st.warning(f"⚠️ {t['Catatan_Revisi']}")
                st.divider()
                
                if user_sekarang != "dian" and user_sekarang != "tamu":
                    if status in ["PROSES", "REVISI"]:
                        l_in = st.text_input("Link GDrive:", value=t.get("Link_Hasil", ""), key=f"l_{t['ID']}")
                        if st.button("🚩 SETOR HASIL", key=f"b_{t['ID']}", use_container_width=True):
                            cell = sheet_tugas.find(str(t['ID']).strip())
                            sheet_tugas.update_cell(cell.row, 5, "WAITING QC")
                            sheet_tugas.update_cell(cell.row, 7, l_in)
                            sheet_tugas.update_cell(cell.row, 6, sekarang.strftime("%d/%m/%Y %H:%M"))
                            catat_log(f"Menyetor tugas {t['ID']}")
                            kirim_notif_wa(f"📤 *UPDATE SETORAN TUGAS*\n\n👤 *Nama:* {user_sekarang.upper()}\n🆔 *ID:* {t['ID']}\n🔗 *Link:* {l_in}")
                            st.success("✅ Berhasil terkirim!"); time.sleep(1); st.rerun()
                elif user_sekarang == "dian" and status != "FINISH":
                    cat = st.text_area("Catatan Revisi:", key=f"cat_{t['ID']}")
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("🟢 VALIDASI (FINISH)", key=f"f_{t['ID']}", use_container_width=True):
                            cell = sheet_tugas.find(str(t['ID']).strip())
                            sheet_tugas.update_cell(cell.row, 5, "FINISH")
                            catat_log(f"Finish tugas {t['ID']}")
                            kirim_notif_wa(f"✅ *TUGAS SELESAI*\n\nTugas Nama *{t['Staf'].upper()}* (ID: {t['ID']}) telah divalidasi.\n✨ Hasil kerja sudah masuk rekapan bulanan.")
                            st.success("✅ Validasi Selesai!"); time.sleep(1); st.rerun()
                    with col2:
                        if st.button("🔴 MINTA REVISI", key=f"r_{t['ID']}", use_container_width=True):
                            cell = sheet_tugas.find(str(t['ID']).strip())
                            sheet_tugas.update_cell(cell.row, 5, "REVISI")
                            sheet_tugas.update_cell(cell.row, 8, cat)
                            catat_log(f"Revisi tugas {t['ID']}")
                            kirim_notif_wa(f"⚠️ *NOTIFIKASI REVISI*\n\n👤 *Nama:* {t['Staf'].upper()}\n🆔 *ID:* {t['ID']}\n📝 *Catatan:* {cat}\n\n_Mohon untuk diperbaiki kembali._ 🛠️")
                            st.success("✅ Permintaan revisi dikirim!"); time.sleep(1); st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    # --- 4. LACI ARSIP ---
    st.divider()
    df_arsip = pd.DataFrame()
    with st.expander("📜 Riwayat Tugas Selesai"):
        if not df_all_tugas.empty:
            # 1. Gunakan filter UPPERCASE untuk Status dan Staf
            mask_s = (df_all_tugas['STATUS'] == "FINISH")
            if user_sekarang != "dian": 
                mask_s &= (df_all_tugas['STAF'] == user_sekarang.upper())
            
            df_arsip = df_all_tugas[mask_s].copy()
            
            if not df_arsip.empty: 
                # 2. Pastikan pemanggilan kolom menggunakan HURUF BESAR
                kolom_tampil = ['ID', 'STAF', 'DEADLINE', 'STATUS']
                # Filter hanya kolom yang benar-benar ada untuk menghindari error
                kolom_ada = [c for c in kolom_tampil if c in df_arsip.columns]
                
                st.dataframe(df_arsip[kolom_ada], hide_index=True, use_container_width=True)
            else: 
                st.write("Belum ada riwayat.")
                
    # --- 5. GAJIAN (VERSI UPGRADE SAKTI) ---
    if user_sekarang != "dian" and user_sekarang != "tamu":
        # A. AMBIL DATA ABSENSI DULU (VERSI FIX ANTI-NOL)
        try:
            data_absensi = sheet_absensi.get_all_records()
            df_absensi = pd.DataFrame(data_absensi)
            
            if not df_absensi.empty:
                df_absensi = bersihkan_data(df_absensi) # Paksa Header & Isi jadi UPPER
                
                # Gunakan strip() untuk buang spasi di belakang nama "INGGI "
                user_up = user_sekarang.upper().strip()
                mask_ab = (df_absensi['NAMA'].astype(str).str.strip() == user_up)
                df_absen_user = df_absensi[mask_ab].copy()
            else:
                df_absen_user = pd.DataFrame()
        except Exception as e:
            st.error(f"Error Absensi: {e}")
            df_absen_user = pd.DataFrame()

        # B. HITUNG LOGIKA (Bonus, Hadir, SP)
        b_video, b_absen, pot_sp, level_sp = hitung_logika_performa_dan_bonus(df_arsip, df_absen_user)

        # --- TAMPILAN ATURAN GAJI (VERSI RAPI) ---
        with st.expander("ℹ️ INFO PENTING: ATURAN & CARA HITUNG GAJI"):
            st.markdown("""
            #### 📢 Aturan Main Pintar Media ( Berlaku per 1 Maret 2026 )
            
            Biar gajian kamu lancar dan nggak bingung, perhatikan poin-poin di bawah ini:
            
            * 🛡️ Masa Proteksi: Tanggal 1 sampai 6 tiap bulan aman dari potongan (Masa Penilaian).
            * ⏰ Bonus Absen (Rp 30.000): Bakal cair kalau kamu setor minimal 3 video di hari yang sama.
            * 🎬 Bonus Video: Mulai video ke-4 dan seterusnya di hari yang sama, kamu dapet tambahan +Rp 25.000/video.
            * ⚠️ Penalti SP: Setor <= 1 video sehari dihitung "Hari Malas". Jika akumulasi mencapai 7, 14, atau 21 hari, maka akan dikenakan SP 1, SP 2, atau SP 3.

            ---

            #### ❓ Gimana Kalau Hasil Per Hari Beda-beda?
            
            * ***Setor 1 Video:*** Dihitung "Hari Malas". Bonus Absen Rp 30rb TIDAK cair. (Akumulasi hari malas memicu potongan SP).
            * ***Setor 2 Video:*** Status kamu "Aman" (nggak dihitung hari malas), tapi Bonus Absen Rp 30rb BELUM cair.
            * ***Setor 3 Video:*** Bonus Absen Rp 30.000 CAIR. (Ini target minimal harian kamu).
            * ***Setor 4 Video:*** Bonus Absen Rp 30.000 CAIR + Bonus Video ke-4 Rp 25.000. Total tambahan hari itu = Rp 55.000.
            * ***Setor 5 Video:*** Bonus Absen Rp 30.000 CAIR + Bonus 2 Video (2 x 25rb). Total tambahan hari itu = Rp 80.000.

            ---          

            #### 🧮 Rumus Gaji:
            [ Gaji Pokok ] + [ Total Bonus Absen ] + [ Total Bonus Video ] - [ Potongan SP ] = 💰 TOTAL GAJI BERSIH

            ---

            #### 💡 PERBANDINGAN SIMULASI (25 Hari Kerja)
            *JIKA Gaji Pokok Rp 2.000.000*

            **1. Simulasi Super Rajin (5 Video/Hari)**
            * Bonus Absen: 25 hari x 30rb = Rp 750.000
            * Bonus Video: 50 video x 25rb = Rp 1.250.000
            * **Total Gaji: Rp 4.000.000**

            **2. Simulasi Rajin (4 Video/Hari)**
            * Bonus Absen: 25 hari x 30rb = Rp 750.000
            * Bonus Video: 25 video x 25rb = Rp 625.000
            * **Total Gaji: Rp 3.375.000**

            **3. Simulasi Target (3 Video/Hari)**
            * Bonus Absen: 25 hari x 30rb = Rp 750.000
            * Bonus Video: Rp 0
            * **Total Gaji: Rp 2.750.000**

            **4. Simulasi Pas-pasan (2 Video/Hari)**
            * Bonus Absen: Rp 0
            * Bonus Video: Rp 0
            * **Total Gaji: Rp 2.000.000** (Hanya Gaji Pokok)

            **5. Simulasi Malas (1 Video/Hari)**
            * Bonus Absen: Rp 0
            * Bonus Video: Rp 0
            * Potongan: Dikenakan SP 1 = Rp 300.000 | SP 2 = Rp 700.000 | SP 3 = Rp 1.000.000 + CUT OFF
            * **Total Gaji: Terpotong sesuai ketentuan SP** *(Misal SP 1: Gaji Pokok + Bonus - 300.000)*

            ---

            #### ⚠️ CATATAN PENTING:
            Semua hitungan hanya berlaku jika video sudah berstatus "FINISH" (Lolos QC Admin). Video berstatus PROSES, WAITING QC, atau REVISI tidak masuk hitungan harian.
            
            ---
            *Cuma beda 1 video per hari bisa ngefek ratusan ribu ke gaji kamu. Yuk, maksimalin hasilnya!* 🚀
            """)
    
        # C. --- RADAR PERFORMA (DI LUAR SLIP) ---
        st.divider()
        if pot_sp > 0:
            st.error(f"⚠️ **STATUS KEDISIPLINAN: {level_sp}**")
            st.write(f"Sistem mendeteksi setoran video kamu di bawah standar (≤ 1 video/hari).")
            # Baris denda sudah dihapus dari sini sesuai permintaanmu
            if level_sp == "SP 2 (PERINGATAN KERAS)":
                st.warning("❗ **PERINGATAN:** Segera kejar setoran 3 video/hari sebelum masuk ke SP 3 (Pecat)!")
        else:             
            st.info("🌟 **STATUS PERFORMA: TERJAGA**")
            st.write("Pertahankan ritme kerja kamu untuk mendapatkan uang absen penuh dan bonus video!")


        # D. --- SLIP GAJI (DIKUNCI TANGGAL 28) ---
        if sekarang.day >= 28:
            with st.expander("💰 **KLAIM SLIP GAJI BULAN INI**", expanded=True):
                try:
                    # 1. Ambil Data Gaji Pokok dari GSheet (Sheet Staff)
                    # Pastikan nama kolom di GSheet adalah 'Nama' dan 'GAJI_POKOK'
                    row_s = df_staff_raw[df_staff_raw['Nama'].str.lower() == user_sekarang.lower()]
                    
                    if not row_s.empty:
                        gapok = int(row_s['GAJI_POKOK'].values[0])
                    else:
                        gapok = 2000000  # Default jika data tidak ditemukan
                    
                    # 2. Kalkulasi Total Akhir
                    total_gaji = (gapok + b_video + b_absen) - pot_sp
                    
                    st.markdown(f"### 📄 Rincian Slip Gaji: {sekarang.strftime('%B %Y')}")
                    st.caption(f"Nama Staf: {user_sekarang.upper()}")
                    
                    # 3. Tampilan Metric (Ringkasan Cepat)
                    col_m1, col_m2, col_m3 = st.columns(3)
                    col_m1.metric("GAJI BERSIH", f"Rp {total_gaji:,}")
                    col_m2.metric("BONUS ABSEN", f"Rp {b_absen:,}")
                    col_m3.metric("BONUS VIDEO", f"Rp {b_video:,}")

                    st.divider()

                    # 4. Tabel Rincian Detail
                    data_rincian = {
                        "Deskripsi": ["Gaji Pokok", "Total Bonus Absen", "Total Bonus Video", "Potongan Penalti (SP)"],
                        "Jumlah": [
                            f"Rp {gapok:,}",
                            f"Rp {b_absen:,}",
                            f"Rp {b_video:,}",
                            f"- Rp {pot_sp:,}" if pot_sp > 0 else "Rp 0"
                        ]
                    }
                    df_rincian = pd.DataFrame(data_rincian)
                    st.table(df_rincian)

                    # 5. Tombol Konfirmasi Final
                    if st.button("🧧 KONFIRMASI & TERIMA GAJI", use_container_width=True):
                        # Catat ke Log Aktivitas
                        catat_log(f"Klaim Gaji: Rp {total_gaji:,} (SP: {level_sp})")
                        
                        # Kirim Laporan ke WA Grup
                        pesan_wa = (
                            f"🧧 *KONFIRMASI PENERIMAAN GAJI*\n\n"
                            f"👤 *Nama Staf:* {user_sekarang.upper()}\n"
                            f"💰 *Total Gaji:* Rp {total_gaji:,}\n"
                            f"--- \n"
                            f"📅 *Bonus Absen:* Rp {b_absen:,} ({int(b_absen/30000)} hari tembus)\n"
                            f"🎬 *Bonus Video:* Rp {b_video:,}\n"
                            f"⚠️ *Status Akhir:* {level_sp}\n\n"
                            f"_Laporan otomatis sistem Pintar Media._ ✅"
                        )
                        kirim_notif_wa(pesan_wa)
                        st.success("✅ Konfirmasi gaji berhasil dikirim ke Admin!")
                        st.balloons()
                        
                except Exception as e: 
                    st.error(f"❌ Gagal memproses rincian slip: {e}")
        else:
            # Tampilan jika belum tanggal 28
            st.info(f"🔒 **Menu Klaim Gaji** akan terbuka otomatis pada tanggal 28 (Sisa {28 - sekarang.day} hari lagi).")
                
def tampilkan_kendali_tim():
    user_sekarang = st.session_state.get("user_aktif", "tamu").lower()
    
    # 1. PROTEKSI AKSES (Hanya Dian)
    if user_sekarang != "dian":
        st.title("⚡ KENDALI TIM")
        st.divider()
        st.warning("🔒 **AREA TERBATAS**")
        return

    # 2. HALAMAN KHUSUS ADMIN
    st.title("⚡ PUSAT KENDALI TIM (ADMIN)")
    
    url_gsheet = "https://docs.google.com/spreadsheets/d/16xcIqG2z78yH_OxY5RC2oQmLwcJpTs637kPY-hewTTY/edit?usp=sharing"
    tz_wib = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz_wib)
    
    c_bln, c_thn = st.columns([2, 2])
    daftar_bulan = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
    pilihan_nama = c_bln.selectbox("📅 Pilih Bulan Laporan:", list(daftar_bulan.values()), index=sekarang.month - 1)
    bulan_dipilih = [k for k, v in daftar_bulan.items() if v == pilihan_nama][0]
    tahun_dipilih = c_thn.number_input("📅 Tahun:", value=sekarang.year, min_value=2024, max_value=2030)

    st.divider()

    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["service_account"], scopes=scope)
        client = gspread.authorize(creds)
        sh = client.open_by_url(url_gsheet)
        
        # --- AMBIL DATA DASAR & NORMALISASI HEADER ---
        def ambil_data(nama_sheet):
            ws = sh.worksheet(nama_sheet)
            data = ws.get_all_records()
            df = pd.DataFrame(data)
            df.columns = [str(c).strip().upper() for c in df.columns]
            return df

        df_staff = ambil_data("Staff")
        df_absen = ambil_data("Absensi")
        df_kas = ambil_data("Arus_Kas")
        ws_tugas = sh.worksheet("Tugas")

        # Ambil Data Tugas Manual
        raw_t = ws_tugas.get_all_values()
        if len(raw_t) > 1:
            h_t = [str(h).strip().upper() for h in raw_t[0]]
            df_tugas = pd.DataFrame(raw_t[1:], columns=h_t)
            if len(df_tugas.columns) >= 5:
                df_tugas.columns.values[4] = "STATUS"
        else:
            df_tugas = pd.DataFrame(columns=['STAF', 'DEADLINE', 'INSTRUKSI', 'STATUS'])

        # --- FUNGSI FILTER TANGGAL AMAN ---
        def saring_tgl(df, kolom, bln, thn):
            if df.empty or kolom.upper() not in df.columns: 
                return pd.DataFrame()
            # Gunakan errors='coerce' dan pastikan konversi ke format YYYY-MM-DD
            df['TGL_TEMP'] = pd.to_datetime(df[kolom.upper()], errors='coerce')
            # Buang data yang gagal dikonversi (NaT)
            df = df.dropna(subset=['TGL_TEMP'])
            mask = (df['TGL_TEMP'].dt.month == bln) & (df['TGL_TEMP'].dt.year == thn)
            return df[mask].copy()
    
        df_t_bln = saring_tgl(df_tugas, 'DEADLINE', bulan_dipilih, tahun_dipilih)
        df_a_f = saring_tgl(df_absen, 'TANGGAL', bulan_dipilih, tahun_dipilih)
        df_k_f = saring_tgl(df_kas, 'TANGGAL', bulan_dipilih, tahun_dipilih)

        # --- LOGIKA HITUNG KEUANGAN (SINKRON DENGAN ATURAN BARU) ---
        df_f_f = df_t_bln[df_t_bln['STATUS'].astype(str).str.upper() == "FINISH"] if not df_t_bln.empty else pd.DataFrame()
        
        # Rekap Video per Nama per Tanggal (untuk hitung uang absen)
        # Kita pakai 'TGL_TEMP' yang sudah di-saring di fungsi saring_tgl
        rekap_harian_tim = {}
        if not df_f_f.empty:
            df_f_f['TGL_STR'] = df_f_f['TGL_TEMP'].dt.strftime('%Y-%m-%d')
            # Grouping: Nama -> Tanggal -> Jumlah Video
            rekap_harian_tim = df_f_f.groupby(['STAF', 'TGL_STR']).size().unstack(fill_value=0).to_dict('index')

        # Total Video per Nama (untuk bonus 4+)
        rekap_total_video = df_f_f['STAF'].str.upper().value_counts().to_dict() if not df_f_f.empty else {}
        
        inc = pd.to_numeric(df_k_f[df_k_f['TIPE'] == 'PENDAPATAN']['NOMINAL'], errors='coerce').sum() if not df_k_f.empty else 0
        ops = pd.to_numeric(df_k_f[df_k_f['TIPE'] == 'PENGELUARAN']['NOMINAL'], errors='coerce').sum() if not df_k_f.empty else 0
        
        # --- LOGIKA HITUNG KEUANGAN (SINKRON TOTAL) ---
        total_pengeluaran_gaji = 0
        for _, s in df_staff.iterrows():
            n_up = str(s['NAMA']).upper()
            
            # 1. Hitung Bonus Absen (30rb jika hari itu setor >= 3 video)
            b_absen_admin = 0
            hari_malas_admin = 0
            
            if n_up in rekap_harian_tim:
                for tgl, jml in rekap_harian_tim[n_up].items():
                    if jml >= 3:
                        b_absen_admin += 30000
                    elif jml <= 1:
                        hari_malas_admin += 1
            
            # 2. Hitung Bonus Video (25rb mulai dari video ke-4 per hari)
            # Di sini kita hitung akumulasi bonus video harian
            b_video_admin = 0
            if n_up in rekap_harian_tim:
                for tgl, jml in rekap_harian_tim[n_up].items():
                    if jml >= 4:
                        b_video_admin += (jml - 3) * 25000

            # 3. Logika Potongan SP (Sesuai Aturan Hari Malas)
            pot_sp_admin = 0
            # Proteksi: Anggap admin melihat setelah lewat masa proteksi (tgl 7+)
            if hari_malas_admin >= 21:
                pot_sp_admin = 1000000
            elif hari_malas_admin >= 14:
                pot_sp_admin = 700000
            elif hari_malas_admin >= 7:
                pot_sp_admin = 300000
            
            # 4. Ambil Gaji Pokok & Tunjangan (Nihilkan tunjangan jika memang kosong)
            v_gapok = int(pd.to_numeric(s.get('GAJI_POKOK'), errors='coerce') or 0)
            v_tunj = int(pd.to_numeric(s.get('TUNJANGAN'), errors='coerce') or 0)
            
            # Kalkulasi Gaji per Orang (Sinkron dengan Slip Gaji Staf)
            gaji_orang_ini = (v_gapok + v_tunj + b_absen_admin + b_video_admin) - pot_sp_admin
            total_pengeluaran_gaji += max(0, gaji_orang_ini)

        # Update tampilan metrik
        st.subheader("💰 LAPORAN KEUANGAN")
        m1, m2, m3 = st.columns(3)
        m1.metric("💰 PENDAPATAN", f"Rp {inc:,}")
        m2.metric("💸 PENGELUARAN", f"Rp {(total_pengeluaran_gaji + ops):,}")
        m3.metric("💎 BERSIH", f"Rp {inc - (total_pengeluaran_gaji + ops):,}")

        # --- TAMPILAN 2: INPUT TRANSAKSI (POSISI KEDUA) ---
        with st.expander("📝 **INPUT TRANSAKSI KEUANGAN**", expanded=False):
            with st.form("form_kas", clear_on_submit=True):
                c_tipe, c_kat, c_nom = st.columns(3)
                f_tipe = c_tipe.selectbox("Jenis:", ["PENDAPATAN", "PENGELUARAN"])
                f_kat = c_kat.selectbox("Kategori:", ["YouTube", "Brand Deal", "Tool AI", "Internet", "Listrik", "Lainnya"])
                f_nom = c_nom.number_input("Nominal (Rp):", min_value=0, step=10000)
                f_ket = st.text_input("Keterangan:")
                
                if st.form_submit_button("Simpan Transaksi"):
                    # AMBIL USER AKTIF (Dian atau Admin lain yang login)
                    pencatat = st.session_state.get("user_aktif", "UNKNOWN").upper()
                    
                    # Simpan ke GSheet dengan nama pencatat yang dinamis
                    sh.worksheet("Arus_Kas").append_row([
                        sekarang.strftime('%Y-%m-%d'), 
                        f_tipe, 
                        f_kat, 
                        int(f_nom), 
                        f_ket, 
                        pencatat # <--- Ganti "Dian" jadi variabel pencatat
                    ])
                    
                    st.success(f"Tersimpan oleh {pencatat}!"); time.sleep(1); st.rerun()

        st.divider()

        # --- TAMPILAN 3: RUANG QC (VERSI AMAN & CEPAT) ---
        with st.expander("🔍 RUANG PEMERIKSAAN (QC)", expanded=False):
            # 1. Ambil data mentah dengan index agar tahu nomor baris asli
            # Header di baris 1, data mulai baris 2. Jadi index df + 2 = baris GSheet.
            df_qc_raw = df_tugas.copy()
            df_qc_raw['BARIS_GSHEET'] = df_qc_raw.index + 2 
            
            df_qc = df_qc_raw[df_qc_raw['STATUS'].astype(str).str.upper() == "WAITING QC"].copy()
            
            if not df_qc.empty:
                for i, r in df_qc.iterrows():
                    t_id_qc = str(r.get('ID', ''))
                    no_baris = int(r.get('BARIS_GSHEET')) # Alamat langsung ke GSheet
                    
                    with st.container(border=True):
                        c1, c2, c3 = st.columns([3, 1, 1])
                        c1.write(f"🎬 **{r.get('INSTRUKSI', 'Tanpa Judul')}**")
                        c1.caption(f"Editor: {r.get('STAF', 'Anonim')} | 🆔 ID: {t_id_qc}")
                        
                        # Tombol ACC - Langsung tembak nomor baris
                        if c2.button("✅ ACC", key=f"acc_safe_{t_id_qc}", use_container_width=True):
                            # Update kolom 5 (Status) di baris spesifik
                            ws_tugas.update_cell(no_baris, 5, "FINISH")
                            st.toast(f"Tugas {t_id_qc} FINISH!", icon="✅")
                            time.sleep(0.5)
                            st.rerun()
                            
                        # Tombol REV - Langsung tembak nomor baris
                        if c3.button("❌ REV", key=f"rev_safe_{t_id_qc}", use_container_width=True):
                            # Update kolom 5 (Status) di baris spesifik
                            ws_tugas.update_cell(no_baris, 5, "REVISI")
                            st.toast(f"Tugas {t_id_qc} dikirim ke REVISI", icon="🔴")
                            time.sleep(0.5)
                            st.rerun()
            else:
                st.info("Antrean QC kosong. ✨ Semua tugas tim sudah diperiksa.")

        # --- TAMPILAN 4: JADWAL PRODUKSI (VERSI EXPANDER) ---
        with st.expander("📅 JADWAL PRODUKSI", expanded=False):
            if not df_t_bln.empty:
                for _, t in df_t_bln.sort_values('TGL_TEMP').iterrows():
                    # Format tampilan lebih ringkas: Ikon - Tanggal - Instruksi - Staf
                    ikon = {"FINISH": "🟢", "WAITING QC": "🔵", "PROSES": "🟡", "REVISI": "🔴"}.get(str(t['STATUS']).upper(), "⚪")
                    st.write(f"{ikon} **{t['TGL_TEMP'].strftime('%d %b')}** — {t.get('INSTRUKSI')} — `{t.get('STAF')}`")
            else:
                st.caption("Tidak ada jadwal untuk periode ini.")

        # --- TAMPILAN 5: GRAFIK PRODUKTIVITAS ---
        with st.expander("📊 GRAFIK PRODUKTIVITAS"):
            if rekap_total_video:
                st.bar_chart(pd.Series(rekap_total_video))
            else:
                st.info("Belum ada video selesai bulan ini.")

# --- TAMPILAN 6: SLIP GAJI (SINKRON TOTAL) ---
        with st.expander("💰 RINCIAN GAJI & SLIP", expanded=False):
            try:
                # 1. Ambil data dasar dulu agar df_arsip dan df_absen tersedia
                sheet_tugas = client.open_by_url(url_gsheet).worksheet("Tugas")
                data_tugas = sheet_tugas.get_all_records()
                df_tugas_all = bersihkan_data(pd.DataFrame(data_tugas))
                df_arsip = df_tugas_all[df_tugas_all['STATUS'] == 'FINISH'] 
                
                sheet_absensi = client.open_by_url(url_gsheet).worksheet("Absensi")
                df_absen = bersihkan_data(pd.DataFrame(sheet_absensi.get_all_records()))
                
                ada_kerja = False

                # 2. MULAI LOOP STAFF (Ini yang bikin Inggi Muncul)
                for _, s in df_staff.iterrows():
                    n_up = str(s['NAMA']).upper().strip()
                    
                    # Hitung Absen Hadir Asli dari GSheet
                    absen_hadir_asli = 0
                    df_absen_staf = pd.DataFrame()
                    if not df_absen.empty:
                        df_absen_staf = df_absen[df_absen['NAMA'].astype(str).str.strip() == n_up]
                        absen_hadir_asli = len(df_absen_staf['TANGGAL'].unique())

                    # Hitung Logika Bonus & Video
                    b_video_view, b_absen_view, pot_sp_view, level_sp_view = hitung_logika_performa_dan_bonus(df_arsip, df_absen_staf)
                    
                    # Ambil total video finish
                    jml_v_total = rekap_total_video.get(n_up, 0)
                    ada_kerja = True

                    # 3. TAMPILKAN CONTAINER (Sekarang di dalam Loop Staff)
                    with st.container(border=True):
                        c1, c2, c3 = st.columns([2, 1, 1])
                        c1.write(f"👤 **{n_up}**")
                        c1.caption(f"💼 {s.get('JABATAN', 'Editor')} | {level_sp_view}")
                        
                        c2.write(f"📅 Hadir: {absen_hadir_asli} Hari")
                        c2.caption(f"✨ Cair: {int(b_absen_view/30000)} Hari")
                        
                        c3.write(f"🎬 {jml_v_total} Video")
                        
                        if st.button(f"🧾 LIHAT SLIP {n_up}", key=f"btn_adm_final_{n_up}"):
                            v_gapok = int(pd.to_numeric(s.get('GAJI_POKOK'), errors='coerce') or 0)
                            v_tunj = int(pd.to_numeric(s.get('TUNJANGAN'), errors='coerce') or 0)
                            v_total = (v_gapok + v_tunj + b_absen_view + b_video_view) - pot_sp_view
                            
                            # SLIP HTML ASLI (Sesuai permintaan lo: TANPA DIHAPUS/SEDERHANAKAN)
                            slip_html = f"""
                            <div style="background-color: white; color: black; padding: 25px; border-radius: 12px; border: 4px solid #1d976c; font-family: sans-serif; width: 320px; margin: auto; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
                                <div style="text-align: center; margin-bottom: 15px;">
                                    <img src="https://raw.githubusercontent.com/pintarkantor-prog/pintarmedia/main/PINTAR.png" width="130" style="margin-bottom: 5px;">
                                    <div style="font-size: 10px; color: #666;">Creative AI Studio & Production</div>
                                    <hr style="border: 0.5px dashed #1d976c; margin: 12px 0;">
                                    <div style="background-color: #1d976c; color: white; display: inline-block; padding: 5px 15px; border-radius: 6px; font-weight: bold; font-size: 12px;">SLIP GAJI (ADMIN VIEW)</div>
                                </div>
                                <table style="width: 100%; font-size: 13px; border-collapse: collapse; color: black;">
                                    <tr><td>Staf</td><td align="right"><b>{n_up}</b></td></tr>
                                    <tr><td>Periode</td><td align="right">{pilihan_nama} {tahun_dipilih}</td></tr>
                                    <tr><td colspan="2"><hr style="border: 0.5px solid #eee; margin: 8px 0;"></td></tr>
                                    <tr><td>Gaji Pokok</td><td align="right">Rp {v_gapok:,}</td></tr>
                                    <tr><td>Bonus Absen (3+)</td><td align="right">Rp {b_absen_view:,}</td></tr>
                                    <tr><td>Bonus Video (4+)</td><td align="right">Rp {b_video_view:,}</td></tr>
                                    <tr style="color: #ff4b4b;"><td>Potongan SP ({hari_malas_view if 'hari_malas_view' in locals() else 0} Hari Malas)</td><td align="right">- Rp {pot_sp_view:,}</td></tr>
                                    <tr><td colspan="2"><hr style="border: 1px dashed black; margin: 15px 0;"></td></tr>
                                    <tr style="font-weight: bold; font-size: 16px; color: #1d976c;">
                                        <td>TOTAL TRANSFER</td><td align="right">Rp {max(0, v_total):,}</td></tr>
                                </table>
                                <div style="margin-top: 25px; text-align: center; border-top: 1px solid #eee; padding-top: 10px;">
                                    <div style="font-size: 9px; color: #999;">Diterbitkan otomatis oleh</div>
                                    <div style="font-size: 11px; font-weight: bold; color: #1d976c;">PINTAR MEDIA SYSTEM</div>
                                    <div style="font-size: 8px; color: #ccc; margin-top: 5px;">{datetime.now(tz_wib).strftime('%d/%m/%Y %H:%M')} WIB</div>
                                </div>
                            </div>
                            """
                            st.components.v1.html(slip_html, height=520)
                
                # 4. Tutup Blok Try dengan Except yang Benar
                if not ada_kerja:
                    st.info("Belum ada aktivitas tim untuk periode ini.")

            except Exception as e:
                st.error(f"⚠️ Terjadi Kendala Sistem: {e}")
        
    # --- TAMPILAN 7: PENGELOLA AKUN AI (VERSI SEJAJAR SEMPURNA) ---    
    with st.expander("🔐 DATABASE AKUN AI", expanded=False):
        try:
            # 1. AMBIL DATA
            ws_akun = sh.worksheet("Akun_AI")
            data_akun_raw = ws_akun.get_all_records()
            df_ai = pd.DataFrame(data_akun_raw)
            
            # 2. TOMBOL TAMBAH DATA (Toggle Form)
            if st.button("➕ Tambah Akun Baru", use_container_width=True):
                st.session_state.buka_form = not st.session_state.get('buka_form', False)
            
            if st.session_state.get('buka_form', False):
                with st.form("form_ai_simple", clear_on_submit=True):
                    c1, c2 = st.columns(2)
                    f_ai = c1.text_input("Nama AI")
                    f_mail = c2.text_input("Email")
                    f_pass = c1.text_input("Password")
                    f_exp = c2.date_input("Tanggal Expired")
                    if st.form_submit_button("Simpan Ke Cloud"):
                        ws_akun.append_row([f_ai, f_mail, f_pass, str(f_exp)])
                        st.success("Data Tersimpan!")
                        time.sleep(1)
                        st.rerun()

            st.write("") # Jarak

            # 3. DAFTAR AKUN (LOGIKA AUTO-HIDE H+1)
            if not df_ai.empty:
                df_ai['EXPIRED'] = pd.to_datetime(df_ai['EXPIRED']).dt.date
                hari_ini = sekarang.date()
                df_tampil = df_ai[df_ai['EXPIRED'] + timedelta(days=1) >= hari_ini]

                for _, row in df_tampil.iterrows():
                    sisa = (row['EXPIRED'] - hari_ini).days
                    
                    if sisa > 7:
                        label = "🟢 Aman"
                    elif 0 <= sisa <= 3:
                        label = "🟠 Segera Habis"
                    elif sisa < 0:
                        label = "🔴 Expired"
                    else:
                        label = "⚪ Standby"

                    # Box Tiap Akun - SEMUA SEJAJAR
                    with st.container(border=True):
                        col1, col2 = st.columns([2.5, 1.5])
                        with col1:
                            # Sisi Kiri: Nama AI, Email, dan Password sejajar
                            st.write(f"**{row['AI']}** — `{row['EMAIL']}` — Pass: `{row['PASSWORD']}`")
                        with col2:
                            # Sisi Kanan: Label Status dan Tanggal sejajar dalam satu baris
                            st.write(f"**{label}** — `{row['EXPIRED'].strftime('%d %b %Y')}`")
            else:
                st.caption("Belum ada data akun.")

        except Exception as e:
            st.info("💡 Pastikan tab 'Akun_AI' sudah ada di Google Sheets.")
        
# ==============================================================================
# BAGIAN 6: MODUL UTAMA - RUANG PRODUKSI (VERSI TOTAL FULL - NO CUT)
# ==============================================================================
def simpan_ke_memori():
    st.session_state.data_produksi = st.session_state.data_produksi
def tampilkan_ruang_produksi():
    # 1. PENGATURAN WAKTU & USER
    sekarang = datetime.utcnow() + timedelta(hours=7) 
    hari_id = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    bulan_id = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    nama_hari = hari_id[sekarang.weekday()]
    tgl = sekarang.day
    nama_bulan = bulan_id[sekarang.month - 1]
    user_aktif = st.session_state.get("user_aktif", "User").upper()

    # 2. KUNCI DATA DARI SESSION STATE (SUMBER UTAMA)
    # Kita ambil data di baris paling atas agar tidak tertimpa/reset
    data = st.session_state.data_produksi
    ver = st.session_state.get("form_version", 0)

    # --- QUALITY BOOSTER & NEGATIVE CONFIG (VERSI FINAL KLIMIS) ---
    QB_IMG = (
        "8k RAW optical clarity, cinematic depth of field, f/1.8 aperture, "
        "bokeh background, razor-sharp focus on subject detail, "
        "high-index lens glass look, CPL filter, sub-surface scattering, "
        "physically-based rendering, hyper-detailed surface micro-textures, "
        "anisotropic filtering, ray-traced ambient occlusion"
    )

    QB_VID = (
        "Unreal Engine 5.4, 24fps cinematic motion, ultra-clear, 8k UHD, high dynamic range, "
        "professional color grading, ray-traced reflections, hyper-detailed textures, "
        "temporal anti-aliasing, zero digital noise, clean pixels, "
        "smooth motion interpolation, high-fidelity physical interaction"
    )

    # --- INI DIA YANG KURANG: NEGATIVE BASE ---
    negative_base = (
        "muscular, bodybuilder, shredded, male anatomy, human skin, human anatomy, "
        "realistic flesh, skin pores, blurry, distorted surface, "
    )
    
    no_text_strict = (
        "STRICTLY NO text, NO typography, NO watermark, NO letters, NO subtitles, "
        "NO captions, NO speech bubbles, NO dialogue boxes, NO labels, NO black bars, "
        "NO burned-in text, NO characters speaking with visible words, "
        "the image must be a CLEAN cinematic shot without any written characters."
    )
    
    negative_motion_strict = (
        "STRICTLY NO morphing, NO extra limbs, NO distorted faces, NO teleporting objects, "
        "NO flickering textures, NO sudden lighting jumps, NO floating hair artifacts."
    )

    # HEADER UI
    c1, c_kosong, c2 = st.columns([2, 0.5, 1.5]) 
    with c1:
        st.markdown("# 🚀 RUANG PRODUKSI")
    with c2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(f"🛰️ {nama_hari}, {tgl} {nama_bulan} | Staf: {user_aktif}")
    
    data = st.session_state.data_produksi
    ver = st.session_state.get("form_version", 0)

    # 1. INTEGRASI REFERENSI NASKAH (KLIMIS - TANPA TOMBOL TANAM)
    if 'naskah_siap_produksi' in st.session_state and st.session_state.naskah_siap_produksi:
        with st.expander("📖 NASKAH REFERENSI PINTAR AI LAB", expanded=True):
            st.markdown(st.session_state.naskah_siap_produksi)
            
            # Cukup tombol bersihkan saja, karena proses tanam sudah otomatis di Gudang Ide
            if st.button("🗑️ Bersihkan Naskah Referensi", use_container_width=True):
                st.session_state.naskah_siap_produksi = ""
                st.rerun()
                
    # 2. IDENTITY LOCK
    with st.expander("🛡️ IDENTITY LOCK - Detail Karakter", expanded=False):
        data["jumlah_karakter"] = st.number_input("Jumlah Karakter", 1, 4, data["jumlah_karakter"], label_visibility="collapsed", key=f"num_char_{ver}")
        cols_char = st.columns(data["jumlah_karakter"])
        
        for i in range(data["jumlah_karakter"]):
            with cols_char[i]:
                st.markdown(f"👤 **Karakter {i+1}**")
                
                # --- LOGIKA AUTO-FILL ---
                nama_pilihan = st.selectbox("Pilih Karakter", list(MASTER_CHAR.keys()), key=f"sel_nama_{i}_{ver}", label_visibility="collapsed")
                pilih_versi = "Manual" 
                current_char = MASTER_CHAR[nama_pilihan]
                
                if nama_pilihan != "Custom":
                    list_versi = list(current_char["versi_pakaian"].keys())
                    pilih_versi = st.selectbox("Versi", list_versi, key=f"sel_ver_{i}_{ver}", label_visibility="collapsed")
                    
                    def_wear = current_char["versi_pakaian"][pilih_versi]
                    def_fisik = current_char["fisik"]
                    nama_final = nama_pilihan
                else:
                    def_wear = data["karakter"][i]["wear"]
                    def_fisik = data["karakter"][i]["fisik"]
                    nama_final = data["karakter"][i]["nama"]

                # --- INPUT WIDGET DENGAN ON_CHANGE (PENGUNCI DATA) ---
                data["karakter"][i]["nama"] = st.text_input(
                    "Nama", value=nama_final, 
                    key=f"char_nama_{i}_{ver}_{nama_pilihan}", 
                    on_change=simpan_ke_memori,
                    placeholder="Nama...", label_visibility="collapsed"
                )
                data["karakter"][i]["wear"] = st.text_input(
                    "Pakaian", value=def_wear, 
                    key=f"char_wear_{i}_{ver}_{nama_pilihan}_{pilih_versi}", 
                    on_change=simpan_ke_memori,
                    placeholder="Pakaian...", label_visibility="collapsed"
                )
                data["karakter"][i]["fisik"] = st.text_area(
                    "Ciri Fisik", value=def_fisik, 
                    key=f"char_fix_{i}_{ver}_{nama_pilihan}", 
                    on_change=simpan_ke_memori,
                    height=80, placeholder="Diisi detail fisik, jika tidak ada referensi gambar...", label_visibility="collapsed"
                )
    # 3. INPUT ADEGAN (LENGKAP: LIGHTING, RATIO, DLL)
    for s in range(data["jumlah_adegan"]):
        scene_id = s + 1
        if scene_id not in data["adegan"]:
            data["adegan"][scene_id] = {
                "aksi": "", "style": OPTS_STYLE[0], "light": OPTS_LIGHT[0], 
                "arah": OPTS_ARAH[0], "shot": OPTS_SHOT[0], "ratio": OPTS_RATIO[0], 
                "cam": OPTS_CAM[0], "loc": "", "dialogs": [""]*4
            }

        with st.expander(f"🎬 ADEGAN {scene_id}", expanded=(scene_id == 1)):
            col_text, col_set = st.columns([1.5, 1])
            with col_text:
                st.markdown('<p class="small-label">📸 NASKAH VISUAL & AKSI</p>', unsafe_allow_html=True)
                # Formatnya dibuat menurun supaya rapi dan tidak bingung
                data["adegan"][scene_id]["aksi"] = st.text_area(
                    f"Aksi_{scene_id}", 
                    value=data["adegan"][scene_id]["aksi"], 
                    height=230, 
                    key=f"act_{scene_id}_{ver}", 
                    label_visibility="collapsed",
                    on_change=simpan_ke_memori # <--- Cukup tempel ini di akhir
                )
            
            with col_set:
                # --- LOGIKA PENGAMAN INDEX (Mencegah ValueError) ---
                def get_index(option_list, current_val):
                    try:
                        return option_list.index(current_val)
                    except ValueError:
                        return 0 # Kembali ke pilihan pertama jika data lama tidak cocok

                # BARIS 1: STYLE & SHOT
                sub1, sub2 = st.columns(2)
                with sub1:
                    st.markdown('<p class="small-label">✨ STYLE</p>', unsafe_allow_html=True)
                    curr_s = data["adegan"][scene_id].get("style", OPTS_STYLE[0])
                    data["adegan"][scene_id]["style"] = st.selectbox(
                        f"S_{scene_id}", OPTS_STYLE, 
                        index=get_index(OPTS_STYLE, curr_s), 
                        key=f"mood_{scene_id}_{ver}", label_visibility="collapsed"
                    )
                with sub2:
                    st.markdown('<p class="small-label">🔍 UKURAN GAMBAR</p>', unsafe_allow_html=True)
                    curr_sh = data["adegan"][scene_id].get("shot", OPTS_SHOT[0])
                    data["adegan"][scene_id]["shot"] = st.selectbox(
                        f"Sh_{scene_id}", OPTS_SHOT, 
                        index=get_index(OPTS_SHOT, curr_sh), 
                        key=f"shot_{scene_id}_{ver}", label_visibility="collapsed"
                    )

                # BARIS 2: LIGHTING & ARAH KAMERA
                sub3, sub4 = st.columns(2)
                with sub3:
                    st.markdown('<p class="small-label">💡 LIGHTING & ATMOSPHERE</p>', unsafe_allow_html=True)
                    curr_l = data["adegan"][scene_id].get("light", OPTS_LIGHT[0])
                    data["adegan"][scene_id]["light"] = st.selectbox(
                        f"L_{scene_id}", OPTS_LIGHT, 
                        index=get_index(OPTS_LIGHT, curr_l), 
                        key=f"light_{scene_id}_{ver}", label_visibility="collapsed"
                    )
                with sub4:
                    st.markdown('<p class="small-label">📐 ARAH KAMERA</p>', unsafe_allow_html=True)
                    curr_a = data["adegan"][scene_id].get("arah", OPTS_ARAH[0])
                    data["adegan"][scene_id]["arah"] = st.selectbox(
                        f"A_{scene_id}", OPTS_ARAH, 
                        index=get_index(OPTS_ARAH, curr_a), 
                        key=f"arah_{scene_id}_{ver}", label_visibility="collapsed"
                    )

                # BARIS 3: GERAKAN & LOKASI
                sub5, sub6 = st.columns([1, 1.5])
                with sub5:
                    st.markdown('<p class="small-label">🎥 GERAKAN</p>', unsafe_allow_html=True)
                    curr_c = data["adegan"][scene_id].get("cam", OPTS_CAM[0])
                    data["adegan"][scene_id]["cam"] = st.selectbox(
                        f"C_{scene_id}", OPTS_CAM, 
                        index=get_index(OPTS_CAM, curr_c), 
                        key=f"cam_{scene_id}_{ver}", label_visibility="collapsed"
                    )
                with sub6:
                    st.markdown('<p class="small-label">📍 LOKASI</p>', unsafe_allow_html=True)
                    data["adegan"][scene_id]["loc"] = st.text_input(
                        f"Loc_{scene_id}", value=data["adegan"][scene_id]["loc"], 
                        key=f"loc_{scene_id}_{ver}", label_visibility="collapsed", 
                        placeholder="Lokasi...", on_change=simpan_ke_memori
                    )

            # --- DIALOG SECTION (SINKRONISASI IDENTITAS) ---
            cols_d = st.columns(data["jumlah_karakter"])
            for i in range(data["jumlah_karakter"]):
                with cols_d[i]:
                    # Ambil nama dan paksa jadi Kapital agar sinkron dengan Scan Karakter
                    raw_nama = data["karakter"][i]["nama"] or f"Karakter {i+1}"
                    char_n = raw_nama.upper()
                    
                    # Beri label Token agar kamu tahu ini akan jadi ACTOR_1, ACTOR_2, dst.
                    st.markdown(f'<p class="small-label" style="color:#FFA500;">🎭 {char_n} (ACTOR_{i+1})</p>', unsafe_allow_html=True)
                    
                    data["adegan"][scene_id]["dialogs"][i] = st.text_input(
                        f"D_{scene_id}_{i}", 
                        value=data["adegan"][scene_id]["dialogs"][i], 
                        key=f"d_{scene_id}_{i}_{ver}", 
                        label_visibility="collapsed",
                        placeholder=f"Ketik dialog {char_n}...",
                        on_change=simpan_ke_memori
                    )

# --- 4. GLOBAL COMPILER LOGIC ---
    st.markdown("---")
    if st.button("🚀 GENERATE SEMUA PROMPT", use_container_width=True, type="primary"):
        adegan_terisi = [s_id for s_id, isi in data["adegan"].items() if isi["aksi"].strip() != ""]
        if not adegan_terisi:
            st.error("⚠️ Isi NASKAH dulu!")
        else:
            user_nama = st.session_state.get("user_aktif", "User").capitalize()
            st.markdown(f"## 🎬 Hasil Prompt: {user_nama} ❤️")
            
            for scene_id in adegan_terisi:
                sc = data["adegan"][scene_id]
                v_text_low = sc["aksi"].lower()
                
                # A. SCAN KARAKTER
                found = []
                jml_kar = data.get("jumlah_karakter", 2)
                for i in range(jml_kar):
                    c = data["karakter"][i]
                    if c['nama'] and re.search(rf'\b{re.escape(c["nama"].lower())}\b', v_text_low):
                        found.append({"id": i+1, "nama": c['nama'].upper(), "wear": c['wear']})

                # B. RAKIT IDENTITAS & CUE (SOLUSI NAMEERROR)
                clean_parts = [f"[[ ACTOR_{m['id']}_SKS ({m['nama']}): refer to PHOTO #{m['id']} ONLY. WEAR: {m['wear']} ]]" for m in found]
                final_identity = " AND ".join(clean_parts) if clean_parts else "[[ IDENTITY: UNKNOWN ]]"
                
                # Logika Acting Cue Otomatis
                cue_parts = [f"[{m['nama']}]: Memberikan ekspresi akting yang mendalam dan emosional sesuai narasi adegan." for m in found]
                acting_cue_text = "\n".join(cue_parts) if cue_parts else "Neutral cinematic expression."

                # Dialog Sync
                list_dialog = [f"[ACTOR_{f['id']}_SKS ({f['nama']}) SPEAKING]: '{sc['dialogs'][f['id']-1]}'" for f in found if sc["dialogs"][f['id']-1].strip()]
                dialog_text = " | ".join(list_dialog) if list_dialog else "Silent interaction."

                # C. MASTER COMPILER (SINKRONISASI TOTAL: MINIMALIS & SAKTI)
                with st.expander(f"💎 MASTERPIECE RESULT | ADEGAN {scene_id}", expanded=True):
                    
                    # 1. Mantra VIDEO (Suntikan Brutal Sharpness f/11)
                    mantra_video = rakit_prompt_sakral(sc['aksi'], sc['style'], sc['light'], sc['arah'], sc['shot'], sc['cam'])
                    
                    # 2. Mantra IMAGE (Infinte Depth of Field)
                    style_map_img = {
                        "Sangat Nyata": "Cinematic RAW shot, PBR surfaces, 8k textures, tactile micro-textures, f/11 aperture, infinite depth of field.",
                        "Animasi 3D Pixar": "Disney style 3D, Octane render, ray-traced global illumination, premium subsurface scattering.",
                        "Gaya Cyberpunk": "Futuristic neon aesthetic, volumetric fog, sharp reflections, high contrast.",
                        "Anime Jepang": "Studio Ghibli style, hand-painted watercolor textures, soft cel shading, lush aesthetic."
                    }
                    s_img = style_map_img.get(sc['style'], "Cinematic optical clarity.")
                    mantra_statis = f"{s_img} {sc['shot']} framing, {sc['arah']} angle, razor-sharp optical focus, {sc['light']}."

                    # 3. Logika Acting Cue Gaya Web Lama (ANTI-DIALOG DOBEL)
                    raw_dialogs = [f"[{data['karakter'][i]['nama'].upper()}_DIALOG]: '{sc['dialogs'][i].strip()}'" for i in range(data["jumlah_karakter"]) if sc['dialogs'][i].strip()]
                    
                    emotional_ref = " | ".join(raw_dialogs) if raw_dialogs else "Neutral Interaction"
                    
                    acting_cue_custom = f"Use these individual dialogue cues for emotional reference only: {emotional_ref}. FOCUS mouth movement and lip-sync ONLY on the active speaker. Others must remain silent."


                    # RAKIT PROMPT GAMBAR
                    img_p = (
                        f"IMAGE REFERENCE RULE: Use uploaded photos for each character. Interaction required.\n"
                        f"{final_identity}\n"
                        f"SCENE: {sc['aksi']}\n"
                        f"LOCATION: {sc['loc']}\n"
                        f"VISUAL: {mantra_statis} NO SOFTENING, extreme edge-enhancement.\n"
                        f"QUALITY: {QB_IMG}\n"
                        f"NEGATIVE: {negative_base} {no_text_strict}\n"
                        f"FORMAT: 9:16 Vertical Framing"
                    )


                    # RAKIT PROMPT VIDEO (DIBERSIHKAN DARI DIALOG DOBEL)
                    vid_p = (
                        f"IMAGE REFERENCE RULE: Use uploaded photos for each character. Interaction required.\n"
                        f"{final_identity}\n"
                        f"SCENE & KINETICS: {sc['aksi']} with {sc['cam']} motion. Character must move naturally with fluid cinematic motion, no robotic movement, no stiffness.\n"
                        f"ACTING CUE (STRICTLY NO TEXT ON SCREEN): {acting_cue_custom}\n"            
                        f"VISUAL: {mantra_video}\n\n"
                        f"QUALITY: {QB_VID}, Maintain 100% facial identity consistency, look exactly like the reference, natural mouth movement\n"
                        f"NEGATIVE: {negative_base} {no_text_strict} {negative_motion_strict}, static, robotic\n"
                        f"FORMAT: 9:16 Vertical Video"
                    )

                    c1, c2 = st.columns(2)
                    with c1: 
                        st.markdown("📷 **PROMPT GEMINI**")
                        st.code(img_p, language="text")
                    with c2: 
                        st.markdown("🎥 **PROMPT VEO**")
                        st.code(vid_p, language="text")

                st.markdown('<div style="margin-bottom: -15px;"></div>', unsafe_allow_html=True)
                
# ==============================================================================
# BAGIAN 7: PENGENDALI UTAMA
# ==============================================================================
def utama():
    inisialisasi_keamanan() 
    pasang_css_kustom() # Tambahkan ini agar CSS kamu langsung aktif saat login
    
    if not cek_autentikasi():
        tampilkan_halaman_login()
    else:
        # Panggil Sidebar & Menu setelah login berhasil
        menu = tampilkan_navigasi_sidebar()
        
        # Logika Menu
        if menu == "🚀 RUANG PRODUKSI": tampilkan_ruang_produksi()
        elif menu == "🧠 PINTAR AI LAB": tampilkan_ai_lab()
        elif menu == "⚡ QUICK PROMPT": tampilkan_quick_prompt()
        elif menu == "📋 TUGAS KERJA": tampilkan_tugas_kerja()
        elif menu == "⚡ KENDALI TIM": tampilkan_kendali_tim()

# --- BAGIAN PALING BAWAH ---
if __name__ == "__main__":
    utama()




