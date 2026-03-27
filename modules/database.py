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
    """Mengambil data & Memaksa semua kolom jadi KAPITAL (Anti-Error Case Sensitive)"""
    try:
        res = supabase.table(nama_tabel).select("*").execute()
        df = pd.DataFrame(res.data)
        
        if not df.empty:
            # --- JURUS SAKTI: Paksa semua nama kolom jadi KAPITAL & Hapus Spasi ---
            df.columns = [str(c).strip().upper() for c in df.columns]
            
            # Bersihkan isi data dari NaN agar tidak crash saat diolah
            df = df.fillna('')
            return df
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Gagal ambil data {nama_tabel}: {e}")
        return pd.DataFrame()

# ==============================================================================
# 3. FUNGSI OPERASIONAL CHANNEL (PINDAHAN DARI WEB LAMA)
# ==============================================================================
def load_data_channel():
    """Khusus narik data akun YouTube (Real-time)"""
    return ambil_data("Channel_Pintar")

def load_data_hp():
    """Khusus narik data unit HP (Real-time)"""
    return ambil_data("Data_HP")

def simpan_perubahan_channel(data_batch):
    """Update status masal langsung ke Supabase (Instan)"""
    try:
        if data_batch:
            supabase.table("Channel_Pintar").upsert(data_batch, on_conflict="EMAIL").execute()
            return True
        return False
    except Exception as e:
        st.error(f"Gagal Simpan: {e}")
        return False

def tambah_log(user, aksi):
    """Mencatat aktivitas ke Supabase (Dian tidak dicatat)"""
    if str(user).upper() == "DIAN": return
    try:
        waktu_log = ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M:%S")
        supabase.table("Log_Aktivitas").insert({
            "Waktu": waktu_log,
            "User": str(user).upper(),
            "Aksi": aksi
        }).execute()
    except: pass

# ==============================================================================
# 4. FUNGSI KEAMANAN (SESI & WHITELIST)
# ==============================================================================
def update_sesi(nama, session_id):
    """Mencatat sesi login terakhir - Fix Error Nama"""
    try:
        # Kita pakai huruf kecil semua untuk KEY di dictionary 
        # SAAT input ke Supabase, pastikan kolom di tabel 'Sesi_Login' 
        # juga huruf kecil semua: 'nama', 'session_id', 'last_login'
        data = {
            "nama": str(nama).upper(), # Isinya kita paksa besar biar seragam
            "session_id": session_id,
            "last_login": ambil_waktu_sekarang().isoformat()
        }
        
        # Eksekusi Upsert
        supabase.table("Sesi_Login").upsert(data, on_conflict="nama").execute()
    except Exception as e:
        # Print error ke terminal buat kita debug kalau masih bandel
        print(f"❌ Catatan sesi gagal: {e}")
