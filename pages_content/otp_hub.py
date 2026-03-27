import streamlit as st
import pandas as pd
from modules import database
import time
import re
import requests
from datetime import datetime, timedelta

def ambil_saldo_otpnum(api_key):
    try:
        url = f"https://otpnum.com/api/get_profile?api_key={api_key}"
        res = requests.get(url).json()
        return res['data']['balance'] if res.get('success') else 0
    except: return 0

def tampilkan_halaman():
    st.title("📩 OTP HUB - PINTAR MEDIA v2.0")
    API_KEY_OTPNUM = st.secrets.get("OTPNUM_API_KEY", "")

    tab_lokal, tab_online = st.tabs(["📱 SMS LOKAL (ACTIVE NOW)", "🛒 SEWA NOMOR ONLINE"])

    # ==========================================================================
    # TAB 1: SMS LOKAL (MODERN CARD & 1 HOUR FILTER)
    # ==========================================================================
    with tab_lokal:
        # Filter: Hanya ambil data 1 jam terakhir dari sekarang
        waktu_cutoff = (datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            # Kita filter langsung di query Supabase biar kencang
            data_otp = database.supabase.table("OTP_Log")\
                .select("*")\
                .gte("created_at", waktu_cutoff)\
                .order("created_at", desc=True)\
                .execute()
            df_otp = pd.DataFrame(data_otp.data)
        except: df_otp = pd.DataFrame()

        # Panel Kontrol Minimalis
        c_search, c_ref, c_del = st.columns([3, 1, 1])
        search_q = c_search.text_input("Cari...", placeholder="Filter SMS...", label_visibility="collapsed")
        
        if c_ref.button("🔄 REFRESH", use_container_width=True): st.rerun()
        
        if c_del.button("🗑️ CLEAR", use_container_width=True):
            if st.session_state.get("user_level") == "OWNER":
                database.supabase.table("OTP_Log").delete().neq("id", 0).execute()
                st.rerun()

        st.markdown(f"<p style='color:gray; font-size:12px; margin-top:5px;'>🔥 Menampilkan SMS 60 menit terakhir</p>", unsafe_allow_html=True)

        # RENDER CARD MODERN
        if not df_otp.empty:
            df_display = df_otp[df_otp.apply(lambda row: search_q.lower() in str(row).lower(), axis=1)] if search_q else df_otp
            
            for i, r in df_display.iterrows():
                dt_obj = pd.to_datetime(r['created_at']).tz_convert('Asia/Jakarta')
                otp_match = re.findall(r'\b\d{6}\b', str(r['MESSAGE']))
                otp_code = otp_match[0] if otp_match else "---"
                
                # DESIGN CARD TANPA EXPANDER (MODERN LOOK)
                with st.container(border=True):
                    # Header Card
                    h1, h2 = st.columns([1, 1])
                    h1.markdown(f"<span style='background:#FF4B4B; color:white; padding:2px 8px; border-radius:5px; font-size:12px;'>📱 {r['RECEIVER']}</span>", unsafe_allow_html=True)
                    h2.markdown(f"<p style='text-align:right; color:gray; font-size:12px; margin:0;'>{dt_obj.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)
                    
                    # Body Card
                    b1, b2 = st.columns([2, 1])
                    b1.markdown(f"<p style='margin:5px 0 0 0; color:#888; font-size:11px;'>PENGIRIM</p><b style='font-size:16px;'>{r['SENDER']}</b>", unsafe_allow_html=True)
                    b2.markdown(f"<p style='margin:5px 0 0 0; color:#888; font-size:11px; text-align:right;'>KODE OTP</p><h2 style='margin:0; text-align:right; color:#F1FA8C;'>{otp_code}</h2>", unsafe_allow_html=True)
                    
                    # Message Area
                    st.markdown(f"<div style='background:#1e1e1e; padding:10px; border-radius:8px; margin-top:10px; border-left: 3px solid #444; color:#CCC; font-size:13px;'>{r['MESSAGE']}</div>", unsafe_allow_html=True)
        else:
            st.info("Tidak ada SMS dalam 1 jam terakhir.")

        st.caption(f"🔄 Last Sync: {database.ambil_waktu_sekarang().strftime('%H:%M:%S')} WIB")

    # ==========================================================================
    # TAB 2: SEWA NOMOR ONLINE (MODERN CARD)
    # ==========================================================================
    with tab_online:
        saldo = ambil_saldo_otpnum(API_KEY_OTPNUM)
        
        # CARD SALDO
        with st.container(border=True):
            s1, s2 = st.columns([2, 1])
            s1.markdown(f"### 💰 Saldo OTPNUM\n# Rp {saldo:,}")
            if s2.button("➕ TOP UP", use_container_width=True):
                st.info("Top up di web OTPNUM ya!")

        st.markdown("#### 🛒 Sewa Nomor Baru")
        with st.container(border=True):
            layanan = st.selectbox("Pilih Layanan", ["Google/Youtube", "Telegram", "WhatsApp", "Facebook", "TikTok"])
            if st.button("🚀 BELI NOMOR SEKARANG", use_container_width=True, type="primary"):
                st.toast("Menghubungkan ke API...")

        st.markdown("#### 🕒 Riwayat Sewa (Aktif)")
        with st.container(border=True):
            st.write("Belum ada transaksi aktif.")
