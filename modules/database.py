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
@st.cache_data(ttl=60)
def ambil_data(nama_tabel):
    """Ambil data: Paksa panggil dua kali biar tembus limit 1000 Supabase."""
    try:
        query = supabase.table(nama_tabel).select("*")
        
        if nama_tabel == "Log_Aktivitas":
            # Truk tunggal buat Log (200 data cukup)
            res_log = query.order("Waktu", desc=True).limit(200).execute()
            data_final = res_log.data
        else:
            # --- TRUK 1 (0-1000) ---
            res1 = query.range(0, 1000).execute()
            data_final = res1.data if res1.data else []
            
            # --- TRUK 2 (1001-2000) ---
            # Kita panggil lagi buat ambil sisanya (35 data lo ada di sini)
            try:
                res2 = query.range(1001, 2000).execute()
                if res2.data:
                    data_final.extend(res2.data)
            except:
                pass # Kalau data gak sampe 1000, truk 2 abaikan aja

        # SEKARANG KITA PAKE data_final, BUKAN res.data LAGI
        df = pd.DataFrame(data_final)    
        
        if not df.empty:
            df.columns = [str(c).strip().upper() for c in df.columns]
            if 'ID' in df.columns:
                df['ID'] = pd.to_numeric(df['ID'], errors='coerce')

            df = df.fillna("") 
            df = df.astype(str)
            df = df.replace(["NONE", "NAN", "NAN.0", "<NA>"], "")
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
            with st.spinner("Mengirim data ke pusat..."):
                # Kita tetep pake EMAIL sebagai jangkar (On Conflict)
                # Biar kalau emailnya sama, dia otomatis UPDATE bukan INSERT
                supabase.table("Channel_Pintar").upsert(data_batch, on_conflict="EMAIL").execute()
                
                # Clear Cache biar angka 395 tadi langsung update jadi 1035+
                st.cache_data.clear()
                st.toast("✅ Sinkronisasi Berhasil!", icon="🚀")
                return True
        return False
    except Exception as e:
        # Jika email duplikat tapi ID beda, Supabase bakal nolak dan masuk ke sini
        if "duplicate key" in str(e).lower():
            st.error("⚠️ Gagal: Email sudah terdaftar!")
        else:
            st.error(f"❌ Gagal Simpan: {e}")
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
