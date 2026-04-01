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
    """Ambil data: Log dilimit 200 baris, sisanya (Channel/Kas) ambil SEMUA."""
    try:
        query = supabase.table(nama_tabel).select("*")
        
        if nama_tabel == "Log_Aktivitas":
            # Ambil 200 BARIS data terbaru, bukan detik ya Boss!
            res = query.order("Waktu", desc=True).limit(200).execute()
        
        else:
            # Buat Channel_Pintar, Arus_Kas, dll: Ambil SEMUA baris biar akurat
            res = query.execute()
            
        df = pd.DataFrame(res.data)
        
        if not df.empty:
            # JURUS SAKTI: Paksa kolom jadi KAPITAL
            df.columns = [str(c).strip().upper() for c in df.columns]
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
