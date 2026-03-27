import streamlit as st
import pandas as pd
from modules import database
import time
import re
import requests
from datetime import datetime, timedelta

# --- FUNGSI API OTPNUM SESUAI DOKUMEN SERVER 2 ---
def get_otpnum_data(url_lengkap):
    try:
        # Sesuai gambar: GET request langsung ke URL contoh
        res = requests.get(url_lengkap, timeout=10).json()
        return res if res.get('success') else None
    except:
        return None

def tampilkan_halaman():
    st.title("📩 OTP HUB - PINTAR MEDIA v2.0")
    
    # API KEY dari Secrets
    API_KEY = st.secrets.get("OTPNUM_API_KEY", "")

    tab_lokal, tab_online = st.tabs(["📱 SMS LOKAL (ACTIVE)", "🛒 SEWA NOMOR ONLINE"])

    # ==========================================================================
    # TAB 1: SMS LOKAL (60 MENIT TERAKHIR)
    # ==========================================================================
    with tab_lokal:
        waktu_cutoff = (datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        try:
            data_otp = database.supabase.table("OTP_Log").select("*").gte("created_at", waktu_cutoff).order("created_at", desc=True).execute()
            df_otp = pd.DataFrame(data_otp.data)
        except: df_otp = pd.DataFrame()

        with st.container(border=True):
            c_search, c_ref, c_del = st.columns([3, 1, 1])
            search_q = c_search.text_input("Filter...", placeholder="Cari SMS...", label_visibility="collapsed")
            if c_ref.button("🔄 REFRESH", use_container_width=True): st.rerun()
            if c_del.button("🗑️ CLEAR", use_container_width=True):
                if st.session_state.get("user_level") == "OWNER":
                    database.supabase.table("OTP_Log").delete().neq("id", 0).execute()
                    st.rerun()

        if not df_otp.empty:
            df_display = df_otp[df_otp.apply(lambda row: search_q.lower() in str(row).lower(), axis=1)] if search_q else df_otp
            for i, r in df_display.iterrows():
                dt_obj = pd.to_datetime(r['created_at']).tz_convert('Asia/Jakarta')
                otp_match = re.findall(r'\b\d{6}\b', str(r['MESSAGE']))
                otp_code = otp_match[0] if otp_match else "---"
                with st.container(border=True):
                    h1, h2 = st.columns([1, 1])
                    h1.markdown(f"<span style='background:#FF4B4B; color:white; padding:2px 8px; border-radius:5px; font-size:12px;'>📱 {r['RECEIVER']}</span>", unsafe_allow_html=True)
                    h2.markdown(f"<p style='text-align:right; color:gray; font-size:12px; margin:0;'>{dt_obj.strftime('%H:%M:%S')} WIB</p>", unsafe_allow_html=True)
                    b1, b2 = st.columns([2, 1])
                    b1.markdown(f"<p style='margin:5px 0 0 0; color:#888; font-size:11px;'>PENGIRIM</p><b style='font-size:16px;'>{r['SENDER']}</b>", unsafe_allow_html=True)
                    b2.markdown(f"<p style='margin:5px 0 0 0; color:#888; font-size:11px; text-align:right;'>KODE OTP</p><h2 style='margin:0; text-align:right; color:#F1FA8C;'>{otp_code}</h2>", unsafe_allow_html=True)
                    st.markdown(f"<div style='background:#1e1e1e; padding:10px; border-radius:8px; margin-top:10px; border-left: 3px solid #444; color:#CCC; font-size:13px;'>{r['MESSAGE']}</div>", unsafe_allow_html=True)
        else:
            st.info("Tidak ada SMS masuk 1 jam terakhir.")

    # ==========================================================================
    # TAB 2: SEWA NOMOR ONLINE (REVISI SESUAI DOKUMEN SERVER 2)
    # ==========================================================================
    with tab_online:
        # Sesuai Gambar 2: Base URL Server 2 adalah https://otpnum.com/api/v2/
        BASE_URL_S2 = "https://otpnum.com/api/v2"
        
        # 1. CEK SALDO (Endpoint: /balance)
        res_bal = get_otpnum_data(f"{BASE_URL_S2}/balance?api_key={API_KEY}")
        saldo = res_bal['data']['balance'] if res_bal else 0
        
        with st.container(border=True):
            s1, s2 = st.columns([2, 1])
            s1.markdown(f"### 💰 Saldo OTPNUM\n# Rp {saldo:,}")
            if s2.button("🔄 REFRESH SALDO", use_container_width=True): st.rerun()

        # 2. PANEL ORDER (Endpoint: /services & /place_order)
        st.markdown("#### 🛒 Sewa Nomor Baru (Server 2)")
        with st.container(border=True):
            # Load Services
            if "list_services_s2" not in st.session_state:
                with st.spinner("Menarik data stok..."):
                    res_serv = get_otpnum_data(f"{BASE_URL_S2}/services?api_key={API_KEY}")
                    if res_serv: st.session_state.list_services_s2 = res_serv['data']

            list_s = st.session_state.get("list_services_s2", [])
            options_serv = {f"{s['name']} - Rp {s['price']}": s['id'] for s in list_s}
            
            pilih_name = st.selectbox("Pilih Layanan", list(options_serv.keys()) if options_serv else ["Memuat..."])
            id_serv = options_serv.get(pilih_name)

            if st.button("🚀 BELI NOMOR SEKARANG", use_container_width=True, type="primary"):
                if id_serv:
                    with st.spinner("Memesan..."):
                        # Endpoint order: /place_order
                        res_order = get_otpnum_data(f"{BASE_URL_S2}/place_order?api_key={API_KEY}&service_id={id_serv}")
                        if res_order:
                            st.session_state.active_order = {
                                "id": res_order['data']['order_id'],
                                "number": res_order['data']['number'],
                                "name": pilih_name
                            }
                            st.rerun()
                        else: st.error("Gagal order. Stok habis atau saldo kurang.")

        # 3. MONITORING (Endpoint: /status)
        if "active_order" in st.session_state:
            ord = st.session_state.active_order
            with st.container(border=True):
                st.markdown(f"**NOMOR:** `{ord['number']}` | {ord['name']}")
                c_cek, c_can = st.columns(2)
                
                if c_cek.button("🔄 CEK SMS", use_container_width=True):
                    # Endpoint status: /status
                    res_stat = get_otpnum_data(f"{BASE_URL_S2}/status?api_key={API_KEY}&order_id={ord['id']}")
                    if res_stat and res_stat['data'].get('sms'):
                        st.session_state.otp_online = res_stat['data']['sms']
                        st.balloons()
                    else: st.toast("SMS belum masuk...")

                if c_can.button("❌ SELESAI / CANCEL", use_container_width=True):
                    del st.session_state.active_order
                    if "otp_online" in st.session_state: del st.session_state.otp_online
                    st.rerun()

                if "otp_online" in st.session_state:
                    st.markdown(f"<h1 style='text-align:center; color:#50FA7B; letter-spacing:5px;'>{st.session_state.otp_online}</h1>", unsafe_allow_html=True)
        else:
            st.info("Belum ada nomor yang disewa.")
