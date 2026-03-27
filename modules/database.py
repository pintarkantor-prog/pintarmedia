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
    """Mencatat ID Sesi terbaru ke database (Single Device Login)"""
    data = {
        "nama": nama,
        "session_id": session_id,
        "last_login": ambil_waktu_sekarang().isoformat()
    }
    supabase.table("Sesi_Login").upsert(data).execute()

def cek_sesi_valid(nama, session_id):
    """Memastikan ID sesi di browser masih yang terbaru di Supabase"""
    try:
        res = supabase.table("Sesi_Login").select("session_id").eq("nama", nama).execute()
        if res.data:
            return res.data[0]['session_id'] == session_id
        return False
    except:
        return False

def cek_pc_whitelist(hostname):
    """Mengecek apakah PC terdaftar di kantor (Whitelist)"""
    try:
        res = supabase.table("PC_Whitelist").select("*").eq("hostname", hostname).execute()
        return len(res.data) > 0
    except:
        return False
