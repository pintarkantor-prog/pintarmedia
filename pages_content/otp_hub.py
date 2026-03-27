import streamlit as st
import pandas as pd
from modules import database
import time
import re

def tampilkan_halaman():
    # --- HEADER STANDAR ---
    st.title("📩 OTP HUB SMS")
    st.caption("Monitoring Kode OTP SMS dari unit HP secara real-time.")

    # --- 1. AMBIL DATA DARI SUPABASE ---
    try:
        # Ambil 40 SMS terbaru agar beban database ringan
        data_otp = database.supabase.table("OTP_Log").select("*").order("created_at", desc=True).limit(40).execute()
        df_otp = pd.DataFrame(data_otp.data)
    except Exception as e:
        st.error(f"Gagal narik data OTP: {e}")
        return

    # --- 2. FITUR SEARCH & REFRESH ---
    c1, c2 = st.columns([3, 1])
    search_query = c1.text_input("🔍 Cari Unit / Pengirim / Isi SMS", placeholder="Contoh: HP 01 atau Google")
    
    with c2:
        st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)
        if st.button("🔄 REFRESH", use_container_width=True, type="primary"):
            st.rerun()

    # Tombol Hapus Log (Hanya Muncul untuk Owner)
    if st.session_state.get("user_level") == "OWNER":
        if st.button("🗑️ BERSIHKAN SEMUA LOG OTP", use_container_width=True):
            database.supabase.table("OTP_Log").delete().neq("id", 0).execute()
            st.success("Log OTP dikosongkan.")
            time.sleep(0.5)
            st.rerun()

    st.divider()

    # --- 3. LOGIKA TAMPILAN SMS CARD ---
    if not df_otp.empty:
        # Filter pencarian
        if search_query:
            mask = (
                df_otp['RECEIVER'].astype(str).str.contains(search_query, case=False, na=False) |
                df_otp['SENDER'].astype(str).str.contains(search_query, case=False, na=False) |
                df_otp['MESSAGE'].astype(str).str.contains(search_query, case=False, na=False)
            )
            df_display = df_otp[mask].copy()
        else:
            df_display = df_otp.copy()

        if df_display.empty:
            st.info("Pencarian tidak ditemukan.")
        else:
            # LOOP RENDER CARD (Gaya List Bersih)
            for i, r in df_display.iterrows():
                # Konversi waktu ke WIB
                waktu_indo = pd.to_datetime(r['created_at']).tz_convert('Asia/Jakarta').strftime('%H:%M:%S')
                tgl_indo = pd.to_datetime(r['created_at']).tz_convert('Asia/Jakarta').strftime('%d %b')
                
                # Cari 6 digit OTP
                otp_match = re.findall(r'\b\d{6}\b', str(r['MESSAGE']))
                otp_code = otp_match[0] if otp_match else "---"

                # Tampilan per baris (Card Sederhana)
                with st.container(border=True):
                    col_a, col_b = st.columns([1, 1])
                    col_a.markdown(f"**📱 {r['RECEIVER']}**")
                    col_b.markdown(f"<p style='text-align:right; color:gray; font-size:12px;'>{tgl_indo} | {waktu_indo} WIB</p>", unsafe_allow_html=True)
                    
                    # Info Pengirim & OTP
                    c_p, c_o = st.columns([2, 1])
                    c_p.markdown(f"<p style='margin:0; font-size:11px; color:gray;'>PENGIRIM</p><b>{r['SENDER']}</b>", unsafe_allow_html=True)
                    c_o.markdown(f"<p style='margin:0; font-size:11px; color:gray; text-align:right;'>KODE OTP</p><h3 style='margin:0; text-align:right; color:#FF4B4B;'>{otp_code}</h3>", unsafe_allow_html=True)
                    
                    st.markdown(f"<p style='margin-top:10px; font-size:13px; color:#CCC; font-style:italic;'>\"{r['MESSAGE']}\"</p>", unsafe_allow_html=True)
    else:
        st.info("Belum ada SMS masuk.")

    # --- 4. FOOTER ---
    st.divider()
    st.caption(f"🔄 Terakhir diperbarui: {database.ambil_waktu_sekarang().strftime('%H:%M:%S')} WIB.")
