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
    """Mencatat ID Sesi terbaru langsung ke tabel Staff (Single Device)"""
    try:
        data = {
            "Session_ID": session_id,
            "Last_Login": ambil_waktu_sekarang().isoformat()
        }
        # Update kolom Session_ID milik user yang sedang login
        supabase.table("Staff").update(data).eq("Nama", nama).execute()
    except Exception as e:
        print(f"Gagal update sesi: {e}")

def ambil_sesi_terakhir(username):
    """Mengambil ID Sesi terbaru dari tabel Staff untuk divalidasi"""
    try:
        response = supabase.table("Staff").select("Session_ID").eq("Nama", username).execute()
        if response.data and len(response.data) > 0:
            # Pastikan nama kolom di Supabase adalah 'Session_ID' (Case Sensitive)
            return response.data[0].get("Session_ID")
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
