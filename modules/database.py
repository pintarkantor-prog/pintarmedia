import streamlit as st
from supabase import create_client, Client
import pandas as pd
from datetime import datetime
import pytz

# ==============================================================================
# 1. SETUP KONEKSI & WAKTU
# ==============================================================================
url: str = st.secrets["supabase"]["url"]
key: str = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)
tz = pytz.timezone('Asia/Jakarta')

def ambil_waktu_sekarang():
    """Mengambil waktu saat ini dalam zona Asia/Jakarta"""
    return datetime.now(tz)

# ==============================================================================
# 2. FUNGSI AMBIL DATA (MESIN UTAMA - NO CACHE)
# ==============================================================================
def ambil_data(nama_tabel):
    try:
        # 1. Setup Waktu buat Saringan (Biar enteng kayak web lama)
        now = ambil_waktu_sekarang()
        tgl_awal_bulan = now.replace(day=1).strftime("%Y-%m-%d")
        
        query = supabase.table(nama_tabel).select("*")
        
        # 2. JURUS SARINGAN (Kunci Biar Gak Mbayang Kelamaan)
        if nama_tabel == "Log_Aktivitas":
            res = query.order("Waktu", desc=True).limit(200).execute()
        elif nama_tabel == "Arus_Kas":
            # Cuma tarik data bulan ini (Biar laporannya cepet)
            res = query.gte("Tanggal", tgl_awal_bulan).order("id", desc=True).execute()
        else:
            # Untuk Channel_Pintar, tarik semua tapi tetep real-time
            res = query.execute()
            
        df = pd.DataFrame(res.data)
        return bersihkan_data(df) # Pake fungsi pembersih sakti lo
    except Exception as e:
        st.error(f"Gagal tarik {nama_tabel}: {e}")
        return pd.DataFrame()

# ==============================================================================
# 3. FUNGSI OPERASIONAL CHANNEL (PINDAHAN DARI WEB LAMA)
# ==============================================================================
def bersihkan_data(df):
    """Jurus sakti biar data seragam, gak ada spasi liar & huruf kecil"""
    if df.empty: return df
    df.columns = [str(c).strip().upper() for c in df.columns]
    df = df.fillna('')
    kolom_krusial = ['EMAIL', 'STATUS', 'NAMA_CHANNEL', 'PENCATAT', 'HP']
    for col in df.columns:
        if col in kolom_krusial:
            df[col] = df[col].astype(str).str.strip().str.upper()
    return df

def load_data_channel():
    """Narik data murni (Real-time tanpa Cache)"""
    try:
        res = supabase.table("Channel_Pintar").select("*").execute()
        if res.data:
            df = pd.DataFrame(res.data)
            return bersihkan_data(df) # Sekarang aman karena fungsi udah ada di atas
        return pd.DataFrame(columns=["TANGGAL", "EMAIL", "STATUS", "HP"])
    except Exception as e:
        st.error(f"❌ Supabase Error: {e}")
        return pd.DataFrame()

@st.cache_data(ttl=600) # <--- GANTI JADI 600 (10 Menit) BIAR HP GAK NARIK TERUS
def load_data_hp():
    try:
        res = supabase.table("Data_HP").select("*").execute()
        df = pd.DataFrame(res.data)
        if not df.empty:
            df.columns = [str(c).strip().upper() for c in df.columns]
        return df
    except:
        return pd.DataFrame()

def simpan_perubahan_channel(data_batch):
    try:
        if data_batch:
            with st.spinner("Mengirim data ke pusat..."): # Opsional: tambah spinner
                supabase.table("Channel_Pintar").upsert(data_batch, on_conflict="EMAIL").execute()
                st.cache_data.clear()
                st.toast("✅ Data Berhasil Disinkron!", icon="🚀") # Tambahan biar mantap
                return True
        return False
    except Exception as e:
        st.error(f"Gagal Simpan: {e}")
        return False

def tambah_log(user, aksi):
    """Mencatat aktivitas ke Supabase (Dian tidak dicatat)"""
    # 1. Standarisasi Nama (Biar gak ada "Icha", "icha", "ICHA")
    user_fix = str(user).strip().upper()
    
    # 2. Proteksi Owner (Sesuai request lo, Dian gak dicatat)
    if user_fix == "DIAN": 
        return
        
    try:
        # 3. Format Waktu Indonesia (Sesuai mesin baru lo)
        waktu_log = ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M:%S")
        
        # 4. Kirim ke Supabase
        supabase.table("Log_Aktivitas").insert({
            "Waktu": waktu_log,
            "User": user_fix,
            "Aksi": str(aksi).strip()
        }).execute()
        
    except Exception as e:
        # Minimal print ke console biar lo tau kalau ada masalah koneksi
        print(f"❌ Log Error: {e}")

# ==============================================================================
# 4. FUNGSI KEAMANAN (HANYA SESI LOGIN - WHITELIST HAPUS)
# ==============================================================================

def update_sesi(nama, session_id):
    """Mencatat sesi login terakhir ke tabel Sesi_Login (Whitelist dihapus)"""
    try:
        # Data tetap masuk ke Supabase buat monitoring Owner
        data = {
            "nama": str(nama).upper(), 
            "session_id": session_id,
            "last_login": ambil_waktu_sekarang().isoformat()
        }
        
        # Eksekusi Upsert (Update data kalau nama sudah ada)
        supabase.table("Sesi_Login").upsert(data, on_conflict="nama").execute()
    except Exception as e:
        # Hanya muncul di log terminal/console
        print(f"❌ Catatan sesi gagal: {e}")
