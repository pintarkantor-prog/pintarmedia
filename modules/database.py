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
# 2. FUNGSI AMBIL DATA (MESIN UTAMA)
# ==============================================================================
def ambil_data(nama_tabel):
    """Mengambil semua data dari tabel Supabase tertentu"""
    try:
        res = supabase.table(nama_tabel).select("*").execute()
        return pd.DataFrame(res.data)
    except Exception as e:
        st.error(f"Gagal ambil data {nama_tabel}: {e}")
        return pd.DataFrame()

# ==============================================================================
# 3. FUNGSI KEAMANAN (VERSI SIMPEL & STABIL)
# ==============================================================================
def update_sesi(nama, session_id):
    """Hanya mencatat kapan terakhir login (Biar Gaji di tabel Staff Aman)"""
    try:
        data = {
            "nama": nama,
            "session_id": session_id,
            "last_login": ambil_waktu_sekarang().isoformat()
        }
        # Menggunakan tabel Sesi_Login agar tidak mengganggu tabel Staff
        supabase.table("Sesi_Login").upsert(data, on_conflict="nama").execute()
    except Exception as e:
        # Silent error agar tidak mengganggu proses login utama
        print(f"Catatan sesi gagal: {e}")

def cek_pc_whitelist(hostname):
    """Mengecek apakah PC terdaftar di kantor (Whitelist)"""
    try:
        # Mencari hostname di tabel PC_Whitelist
        res = supabase.table("PC_Whitelist").select("*").eq("hostname", hostname).execute()
        return len(res.data) > 0
    except:
        # Jika tabel tidak ada atau error, anggap tidak terdaftar
        return False

# Fitur 'tendang otomatis' dihapus agar aplikasi lebih stabil dan ringan.
