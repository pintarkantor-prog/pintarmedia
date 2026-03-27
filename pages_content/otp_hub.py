import streamlit as st
import pandas as pd
from modules import database
import time
import re

def tampilkan_halaman():
    st.title("📩 OTP SMS")

    # --- 1. SETTING REFRESH OTOMATIS ---
    # Gunakan st.empty() dan loop kecil biar kerasa kencang
    if "last_otp_update" not in st.session_state:
        st.session_state.last_otp_update = time.time()

    # --- 2. AMBIL DATA DARI SUPABASE ---
    # Kita ambil 50 SMS terbaru saja biar gak berat
    try:
        data_otp = database.supabase.table("OTP_Log").select("*").order("created_at", desc=True).limit(50).execute()
        df_otp = pd.DataFrame(data_otp.data)
    except Exception as e:
        st.error(f"Gagal narik data OTP: {e}")
        return

    # --- 3. FILTER & SEARCH ---
    c1, c2 = st.columns([2, 1])
    search_query = c1.text_input("🔍 Cari (Nama HP / Pengirim / Isi SMS)", placeholder="Contoh: HP 05 atau Google")
    
    if st.button("🗑️ BERSIHKAN SEMUA OTP", use_container_width=True, type="secondary"):
        # Fitur buat hapus log lama biar gak menumpuk (Hanya untuk Owner)
        if st.session_state.get("user_level") == "OWNER":
            database.supabase.table("OTP_Log").delete().neq("id", 0).execute()
            st.success("Log OTP berhasil dikosongkan!")
            st.rerun()
        else:
            st.warning("Hanya Owner yang bisa menghapus log.")

    # --- 4. LOGIKA TAMPILAN (DATA EDITOR) ---
    if not df_otp.empty:
        # Filter berdasarkan pencarian
        if search_query:
            mask = (
                df_otp['RECEIVER'].str.contains(search_query, case=False, na=False) |
                df_otp['SENDER'].str.contains(search_query, case=False, na=False) |
                df_otp['MESSAGE'].str.contains(search_query, case=False, na=False)
            )
            df_display = df_otp[mask].copy()
        else:
            df_display = df_otp.copy()

        # Format Tanggal agar enak dibaca (WIB)
        df_display['WAKTU'] = pd.to_datetime(df_display['created_at']).dt.tz_convert('Asia/Jakarta').dt.strftime('%d/%m %H:%M:%S')

        # Fungsi highlight 6 angka OTP
        def extract_otp(text):
            otp = re.findall(r'\b\d{6}\b', str(text)) # Cari 6 angka berurutan
            return otp[0] if otp else "-"

        df_display['CODE'] = df_display['MESSAGE'].apply(extract_otp)

        # Render Tabel
        st.dataframe(
            df_display[['WAKTU', 'RECEIVER', 'SENDER', 'CODE', 'MESSAGE']],
            use_container_width=True,
            hide_index=True,
            column_config={
                "WAKTU": st.column_config.TextColumn("⏰ WAKTU", width=120),
                "RECEIVER": st.column_config.TextColumn("📱 DARI HP", width=100),
                "SENDER": st.column_config.TextColumn("👤 PENGIRIM", width=120),
                "CODE": st.column_config.TextColumn("🔑 OTP", width=80),
                "MESSAGE": st.column_config.TextColumn("💬 ISI SMS", width=400),
            }
        )
    else:
        st.info("Belum ada SMS masuk.")

    # --- 5. FOOTER AUTO REFRESH INFO ---
    st.divider()
    st.caption(f"Terakhir diperbarui: {database.ambil_waktu_sekarang().strftime('%H:%M:%S')} WIB. (Data auto-refresh setiap kali halaman dibuka)")
