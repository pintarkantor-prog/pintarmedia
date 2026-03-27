import streamlit as st
from supabase import create_client, Client
import pandas as pd
from datetime import datetime
import pytz

# 1. SETUP KONEKSI & WAKTU
url: str = st.secrets["supabase"]["url"]
key: str = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)
tz = pytz.timezone('Asia/Jakarta')

def ambil_waktu_sekarang():
    """Mengambil waktu saat ini dalam zona Asia/Jakarta"""
    return datetime.now(tz)

# 2. FUNGSI AMBIL DATA
def ambil_data(nama_tabel):
    try:
        res = supabase.table(nama_tabel).select("*").execute()
        return pd.DataFrame(res.data)
    except Exception as e:
        st.error(f"Gagal ambil data {nama_tabel}: {e}")
        return pd.DataFrame()

# 3. FUNGSI KEAMANAN SESI & PC
def update_sesi(nama, session_id):
    """Mencatat ID Sesi ke tabel khusus Sesi_Login (Biar Gaji aman)"""
    try:
        data = {
            "nama": nama,
            "session_id": session_id,
            "last_login": ambil_waktu_sekarang().isoformat()
        }
        # Pake upsert: kalo nama udah ada dia update, kalo belum dia nambah baru
        supabase.table("Sesi_Login").upsert(data, on_conflict="nama").execute()
    except Exception as e:
        print(f"Gagal update sesi: {e}")

def ambil_sesi_terakhir(username):
    """Ambil ID sesi terbaru dari tabel Sesi_Login"""
    try:
        res = supabase.table("Sesi_Login").select("session_id").eq("nama", username).execute()
        if res.data and len(res.data) > 0:
            return res.data[0].get("session_id")
        return None
    except Exception as e:
        print(f"Error ambil_sesi_terakhir: {e}")
        return None

def cek_sesi_valid(nama, session_id):
    """Fungsi pembantu untuk cek apakah sesi masih valid"""
    sesi_db = ambil_sesi_terakhir(nama)
    return sesi_db == session_id

def cek_pc_whitelist(hostname):
    """Mengecek apakah PC terdaftar di kantor (Whitelist)"""
    try:
        # Pastikan di Supabase nama tabelnya 'PC_Whitelist' dan kolomnya 'hostname'
        res = supabase.table("PC_Whitelist").select("*").eq("hostname", hostname).execute()
        return len(res.data) > 0
    except:
        return False
