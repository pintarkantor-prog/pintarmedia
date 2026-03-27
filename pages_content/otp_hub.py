import streamlit as st
import pandas as pd
from modules import database
import time
import re
import requests
from datetime import datetime, timedelta

# Matikan peringatan SSL (biar gak menuhin log)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_otpnum_v2(endpoint, params):
    try:
        # Base URL pastikan pakai HTTPS dan slash di akhir
        base_url = "https://otpnum.com/api/v2/"
        full_url = f"{base_url}{endpoint}"
        
        # Tambahkan verify=False buat bypass blokir SSL
        response = requests.get(full_url, params=params, timeout=15, verify=False)
        
        if response.status_code == 200:
            return response.json()
        return {"success": False, "message": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"success": False, "message": str(e)}

def tampilkan_halaman():
    st.title("📩 OTP HUB - PINTAR MEDIA v2.0")
    
    # Ambil API KEY (Pastikan di Secrets namanya OTPNUM_API_KEY)
    API_KEY = st.secrets.get("OTPNUM_API_KEY", "")

    tab_lokal, tab_online = st.tabs(["📱 SMS LOKAL (ACTIVE)", "🛒 SEWA NOMOR ONLINE"])

    # ==========================================================================
    # TAB 1: SMS LOKAL (Gaya Modern)
    # ==========================================================================
    with tab_lokal:
        waktu_cutoff = (datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        try:
            data_otp = database.supabase.table("OTP_Log").select("*").gte("created_at", waktu_cutoff).order("created_at", desc=True).execute()
            df_otp = pd.DataFrame(data_otp.data)
        except: df_otp = pd.DataFrame()

        with st.container(border=True):
            c_search, c_ref, c_del = st.columns([3, 1, 1])
            search_q = c_search.text_input("Filter...", placeholder="Cari...", label_visibility="collapsed")
            if c_ref.button("🔄 REFRESH", use_container_width=True): st.rerun()
            if c_del.button("🗑️ CLEAR", use_container_width=True):
                if st.session_state.get("user_level") == "OWNER":
                    database.supabase.table("OTP_Log").delete().neq("id", 0).execute()
                    st.rerun()

        if not df_otp.empty:
            df_display = df_otp[df_otp.apply(lambda row: search_q.lower() in str(row).lower(), axis=1)] if search_q else df_otp
            for i, r in df_display.iterrows():
                dt_obj = pd.to_datetime(r['created_at']).tz_convert('Asia/Jakarta')
                otp_code = re.findall(r'\b\d{6}\b', str(r['MESSAGE']))[0] if re.findall(r'\b\d{6}\b', str(r['MESSAGE'])) else "---"
                with st.container(border=True):
                    st.markdown(f"<span style='background:#FF4B4B; color:white; padding:2px 8px; border-radius:5px; font-size:12px;'>📱 {r['RECEIVER']}</span> <small style='float:right; color:gray;'>{dt_obj.strftime('%H:%M:%S')} WIB</small>", unsafe_allow_html=True)
                    c1, c2 = st.columns([2, 1])
                    c1.markdown(f"<p style='margin:5px 0 0 0; color:#888; font-size:11px;'>PENGIRIM</p><b>{r['SENDER']}</b>", unsafe_allow_html=True)
                    c2.markdown(f"<p style='margin:5px 0 0 0; color:#888; font-size:11px; text-align:right;'>KODE</p><h2 style='margin:0; text-align:right; color:#F1FA8C;'>{otp_code}</h2>", unsafe_allow_html=True)
                    st.markdown(f"<div style='background:#1e1e1e; padding:10px; border-radius:8px; margin-top:10px; border-left: 3px solid #444; color:#CCC; font-size:13px;'>{r['MESSAGE']}</div>", unsafe_allow_html=True)
        else:
            st.info("Belum ada SMS lokal 1 jam terakhir.")

    # ==========================================================================
    # TAB 2: SEWA NOMOR ONLINE
    # ==========================================================================
    with tab_online:
        # 1. Cek Saldo
        res_bal = get_otpnum_v2("balance", {"api_key": API_KEY})
        saldo = res_bal['data']['balance'] if res_bal and res_bal.get('success') else 0
        
        with st.container(border=True):
            s1, s2 = st.columns([2, 1])
            s1.markdown(f"### 💰 Saldo: Rp {saldo:,}")
            if s2.button("🔄 REFRESH", use_container_width=True, key="ref_bal"): st.rerun()

        # 2. Panel Order
        st.markdown("#### 🛒 Sewa Nomor (Server 2)")
        with st.container(border=True):
            if "list_services_v2" not in st.session_state:
                res_serv = get_otpnum_v2("services", {"api_key": API_KEY, "country_id": 6})
                if res_serv and res_serv.get('success'):
                    st.session_state.list_services_v2 = res_serv['data']['services']

            services = st.session_state.get("list_services_v2", [])
            opts = {f"{s['service_name']} - Rp {s['price']}": s['service_id'] for s in services}
            pilih = st.selectbox("Layanan", list(opts.keys()) if opts else ["Gagal memuat layanan"])
            
            if st.button("🚀 BELI NOMOR", use_container_width=True, type="primary"):
                sid = opts.get(pilih)
                res_order = get_otpnum_v2("order", {"api_key": API_KEY, "service_id": sid, "operator": "any", "country_id": 6})
                if res_order and res_order.get('success'):
                    st.session_state.active_order = {"id": res_order['data']['order_id'], "number": res_order['data']['number'], "name": pilih}
                    st.rerun()
                else:
                    st.error(f"Gagal: {res_order.get('message') if res_order else 'Stok Habis'}")

        # 3. Monitoring
        if "active_order" in st.session_state:
            ord = st.session_state.active_order
            with st.container(border=True):
                st.write(f"Nomor: **{ord['number']}**")
                if st.button("🔄 CEK SMS"):
                    res_stat = get_otpnum_v2("status", {"api_key": API_KEY, "order_id": ord['id']})
                    if res_stat and res_stat['data'].get('sms') and res_stat['data']['sms'] != "waiting":
                        st.session_state.otp_online = res_stat['data']['sms']
                        st.balloons()
                if st.button("❌ CANCEL"):
                    get_otpnum_v2("cancel", {"api_key": API_KEY, "order_id": ord['id']})
                    del st.session_state.active_order
                    st.rerun()
