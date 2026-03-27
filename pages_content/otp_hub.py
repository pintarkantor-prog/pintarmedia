import streamlit as st
import pandas as pd
from modules import database
import time
import re

def tampilkan_halaman():
    st.title("📩 OTP HUB SMS")
    
    # --- AMBIL DATA DARI SUPABASE ---
    try:
        data_otp = database.supabase.table("OTP_Log").select("*").order("created_at", desc=True).limit(40).execute()
        df_otp = pd.DataFrame(data_otp.data)
    except Exception as e:
        st.error(f"Gagal narik data OTP: {e}")
        return

    # --- WRAPPER EXPANDER (BIAR RAPI) ---
    with st.expander("🔍 PANEL KONTROL & FILTER OTP", expanded=True):
        c1, c2 = st.columns([4, 1])
        search_query = c1.text_input("Cari Unit / Pengirim / Isi", placeholder="Contoh: HP 01...", label_visibility="collapsed")
        
        # Tombol Refresh Sejajar
        if c2.button("🔄 REFRESH", use_container_width=True, type="primary"):
            st.rerun()

        # Tombol Hapus (Hanya Owner)
        if st.session_state.get("user_level") == "OWNER":
            st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
            if st.button("🗑️ BERSIHKAN SEMUA LOG OTP", use_container_width=True):
                database.supabase.table("OTP_Log").delete().neq("id", 0).execute()
                st.success("Log dikosongkan.")
                time.sleep(0.5)
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # --- LIST SMS ---
    if not df_otp.empty:
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
            for i, r in df_display.iterrows():
                # Waktu & OTP
                dt_obj = pd.to_datetime(r['created_at']).tz_convert('Asia/Jakarta')
                waktu_str = dt_obj.strftime('%d/%m %H:%M:%S')
                otp_match = re.findall(r'\b\d{6}\b', str(r['MESSAGE']))
                otp_code = otp_match[0] if otp_match else "---"

                # Container Bersih
                with st.container(border=True):
                    # Baris Atas: HP & Waktu
                    ca, cb = st.columns([1, 1])
                    ca.markdown(f"**📱 {r['RECEIVER']}**")
                    cb.markdown(f"<p style='text-align:right; color:gray; font-size:12px;'>{waktu_str} WIB</p>", unsafe_allow_html=True)
                    
                    # Baris Tengah: Pengirim & Kode OTP
                    cp, co = st.columns([2, 1])
                    cp.markdown(f"<p style='margin:0; font-size:11px; color:gray;'>PENGIRIM</p><b>{r['SENDER']}</b>", unsafe_allow_html=True)
                    co.markdown(f"<p style='margin:0; font-size:11px; color:gray; text-align:right;'>KODE</p><h3 style='margin:0; text-align:right; color:#FF4B4B; letter-spacing:2px;'>{otp_code}</h3>", unsafe_allow_html=True)
                    
                    # Baris Bawah: Pesan
                    st.markdown(f"<p style='margin-top:10px; font-size:13px; color:#DDD; background:#1e1e1e; padding:8px; border-radius:5px;'>{r['MESSAGE']}</p>", unsafe_allow_html=True)
    else:
        st.info("Belum ada SMS masuk.")

    st.caption(f"🔄 Auto-update | Last: {database.ambil_waktu_sekarang().strftime('%H:%M:%S')}")
