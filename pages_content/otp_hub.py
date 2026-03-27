import streamlit as st
import pandas as pd
from modules import database
import time
import re
import requests
from datetime import datetime, timedelta

# --- FUNGSI API OTPNUM ---
def get_otpnum_data(endpoint, params):
    try:
        res = requests.get(endpoint, params=params, timeout=10).json()
        return res if res.get('success') else None
    except:
        return None

def ambil_saldo_otpnum(api_key):
    res = get_otpnum_data("https://otpnum.com/api/get_profile", {"api_key": api_key})
    return res['data']['balance'] if res else 0

def tampilkan_halaman():
    st.title("📩 OTP HUB - PINTAR MEDIA v2.0")
    
    # Ambil API KEY dari Secrets
    API_KEY = st.secrets.get("OTPNUM_API_KEY", "")

    # --- PEMBAGIAN TAB ---
    tab_lokal, tab_online = st.tabs(["📱 SMS LOKAL (ACTIVE)", "🛒 SEWA NOMOR ONLINE"])

    # ==========================================================================
    # TAB 1: SMS LOKAL (60 MENIT TERAKHIR)
    # ==========================================================================
    with tab_lokal:
        # Filter 1 jam terakhir
        waktu_cutoff = (datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            data_otp = database.supabase.table("OTP_Log")\
                .select("*")\
                .gte("created_at", waktu_cutoff)\
                .order("created_at", desc=True)\
                .execute()
            df_otp = pd.DataFrame(data_otp.data)
        except:
            df_otp = pd.DataFrame()

        # Panel Kontrol Minimalis
        with st.container(border=True):
            c_search, c_ref, c_del = st.columns([3, 1, 1])
            search_q = c_search.text_input("Cari SMS...", placeholder="Filter...", label_visibility="collapsed")
            
            if c_ref.button("🔄 REFRESH", use_container_width=True):
                st.rerun()
            
            if c_del.button("🗑️ CLEAR", use_container_width=True):
                if st.session_state.get("user_level") == "OWNER":
                    database.supabase.table("OTP_Log").delete().neq("id", 0).execute()
                    st.rerun()

        # List SMS Card
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
            st.info("Tidak ada Kode OTP masuk dalam 1 jam terakhir.")

        st.caption(f"🔄 Last Sync Lokal: {database.ambil_waktu_sekarang().strftime('%H:%M:%S')} WIB")

    # ==========================================================================
    # TAB 2: SEWA NOMOR ONLINE (SERVER 2 DEFAULT)
    # ==========================================================================
    with tab_online:
        saldo = ambil_saldo_otpnum(API_KEY)
        
        # CARD SALDO
        with st.container(border=True):
            s1, s2 = st.columns([2, 1])
            s1.markdown(f"### 💰 Saldo OTPNUM\n# Rp {saldo:,}")
            if s2.button("🔄 REFRESH SALDO", use_container_width=True):
                st.rerun()

        # PANEL ORDER
        st.markdown("#### 🛒 Sewa Nomor Baru")
        with st.container(border=True):
            c_srv, c_neg = st.columns(2)
            
            # Mapping Server (Server 2 Default)
            dict_server = {
                "Server 2": "https://s2.otpnum.com/api",
                "Server 1": "https://otpnum.com/api",
                "Server 3": "https://s3.otpnum.com/api"
            }
            srv_nama = c_srv.selectbox("Pilih Server", list(dict_server.keys()), index=0)
            url_server = dict_server[srv_nama]
            negara = c_neg.selectbox("Pilih Negara", ["Indonesia", "Vietnam", "Thailand", "India"])

            # Load Services Otomatis
            if "list_services" not in st.session_state or st.session_state.get("last_server") != srv_nama:
                with st.spinner(f"Loading stok {srv_nama}..."):
                    res_serv = get_otpnum_data(f"{url_server}/get_services", {"api_key": API_KEY})
                    if res_serv:
                        st.session_state.list_services = res_serv['data']
                        st.session_state.last_server = srv_nama

            options_serv = {s['name']: s['id'] for s in st.session_state.get("list_services", [])}
            pilih_name = st.selectbox("Pilih Layanan", list(options_serv.keys()) if options_serv else ["Memuat..."])
            id_serv = options_serv.get(pilih_name)

            if st.button("🚀 BELI NOMOR SEKARANG", use_container_width=True, type="primary"):
                if id_serv:
                    with st.spinner("Memesan nomor..."):
                        res_order = get_otpnum_data(f"{url_server}/set_order", {"api_key": API_KEY, "service_id": id_serv})
                        if res_order:
                            st.session_state.active_order = {
                                "id": res_order['data']['order_id'],
                                "number": res_order['data']['number'],
                                "server_url": url_server,
                                "service_name": pilih_name
                            }
                            st.rerun()
                        else:
                            st.error("Stok habis atau saldo tidak cukup.")

        # PANEL MONITORING NOMOR AKTIF
        st.markdown("#### 🕒 Nomor Aktif")
        if "active_order" in st.session_state:
            ord = st.session_state.active_order
            with st.container(border=True):
                st.markdown(f"**NOMOR:** `{ord['number']}` | **SERVICE:** {ord['service_name']}")
                
                c_cek, c_can = st.columns(2)
                if c_cek.button("🔄 CEK SMS", use_container_width=True):
                    res_stat = get_otpnum_data(f"{ord['server_url']}/get_order_status", {"api_key": API_KEY, "order_id": ord['id']})
                    if res_stat and res_stat['data'].get('sms'):
                        st.session_state.otp_online = res_stat['data']['sms']
                        st.balloons()
                    else:
                        st.toast("SMS belum masuk...")

                if c_can.button("❌ SELESAI / CANCEL", use_container_width=True):
                    del st.session_state.active_order
                    if "otp_online" in st.session_state: del st.session_state.otp_online
                    st.rerun()

                if "otp_online" in st.session_state:
                    st.markdown(f"""
                        <div style="background:#262730; padding:15px; border-radius:10px; border:2px solid #50FA7B; text-align:center; margin-top:10px;">
                            <p style="margin:0; color:gray;">KODE OTP:</p>
                            <h1 style="color:#50FA7B; margin:0; letter-spacing:5px;">{st.session_state.otp_online}</h1>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("Belum ada nomor yang disewa.")
