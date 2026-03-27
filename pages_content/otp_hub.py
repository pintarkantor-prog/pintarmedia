import streamlit as st
import pandas as pd
from modules import database
import time
import re

def tampilkan_halaman():
    # --- HEADER GAYA RADAR ---
    st.markdown("""
        <div style="background-color:#1E1E2E; padding:20px; border-radius:10px; border-left: 5px solid #FF4B4B; margin-bottom:20px;">
            <h2 style="color:white; margin:0;">📩 RADAR OTP HUB</h2>
            <p style="color:#888; margin:0;">Kode OTP Real-time dari Unit HP Kerja</p>
        </div>
    """, unsafe_allow_html=True)

    # --- 1. AMBIL DATA DARI SUPABASE ---
    try:
        data_otp = database.supabase.table("OTP_Log").select("*").order("created_at", desc=True).limit(40).execute()
        df_otp = pd.DataFrame(data_otp.data)
    except Exception as e:
        st.error(f"Gagal narik data OTP: {e}")
        return

    # --- 2. FITUR SEARCH & COMMAND ---
    c1, c2 = st.columns([3, 1])
    search_query = c1.text_input("🔍 Filter Unit / Pengirim / Kode", placeholder="Contoh: HP 01 atau Google")
    
    with c2:
        st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)
        if st.button("🗑️ CLEAR LOG", use_container_width=True, type="secondary"):
            if st.session_state.get("user_level") == "OWNER":
                database.supabase.table("OTP_Log").delete().neq("id", 0).execute()
                st.rerun()
            else:
                st.warning("Akses Ditolak!")

    # --- 3. LOGIKA TAMPILAN CARD ---
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

        if df_display.empty:
            st.info("Pencarian tidak ditemukan.")
        else:
            # LOOP UNTUK RENDER CARD SMS
            for i, r in df_display.iterrows():
                # Format Waktu
                waktu_indo = pd.to_datetime(r['created_at']).tz_convert('Asia/Jakarta').strftime('%H:%M:%S')
                tgl_indo = pd.to_datetime(r['created_at']).tz_convert('Asia/Jakarta').strftime('%d %b')
                
                # Ekstrak 6 Digit OTP (Kuning Terang)
                otp_match = re.findall(r'\b\d{6}\b', str(r['MESSAGE']))
                otp_code = otp_match[0] if otp_match else "---"

                # DESIGN CARD AESTHETIC
                st.markdown(f"""
                    <div style="background:#262730; padding:15px; border-radius:10px; border:1px solid #444; margin-bottom:10px;">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="background:#FF4B4B; color:white; padding:2px 10px; border-radius:15px; font-size:12px; font-weight:bold;">
                                📱 {r['RECEIVER']}
                            </span>
                            <span style="color:#888; font-size:12px;">⏰ {tgl_indo} | {waktu_indo} WIB</span>
                        </div>
                        <div style="display:flex; margin-top:10px; align-items:center;">
                            <div style="flex:1;">
                                <p style="margin:0; color:#888; font-size:11px;">PENGIRIM</p>
                                <b style="font-size:16px; color:#50FA7B;">{r['SENDER']}</b>
                            </div>
                            <div style="flex:1; text-align:right;">
                                <p style="margin:0; color:#888; font-size:11px;">KODE OTP</p>
                                <b style="font-size:24px; color:#F1FA8C; letter-spacing:3px;">{otp_code}</b>
                            </div>
                        </div>
                        <hr style="border:0.5px solid #333; margin:10px 0;">
                        <p style="margin:0; color:#DDD; font-size:13px; font-style:italic;">"{r['MESSAGE']}"</p>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Belum ada SMS masuk.")

    # --- 4. AUTO REFRESH INFO ---
    st.divider()
    st.caption(f"🔄 Terakhir diperbarui: {database.ambil_waktu_sekarang().strftime('%H:%M:%S')} WIB.")
