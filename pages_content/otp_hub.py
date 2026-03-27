import streamlit as st
import pandas as pd
from modules import database
import time
import re
import requests
from datetime import datetime, timedelta

# Matikan peringatan SSL
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- FUNGSI API UNIVERSAL ---
def get_otpnum_api(server_url, endpoint, params):
    try:
        if not server_url: return None
        base = server_url if server_url.endswith("/") else f"{server_url}/"
        full_url = f"{base}{endpoint}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(full_url, params=params, timeout=15, headers=headers, verify=False)
        if response.status_code == 200:
            return response.json()
        return {"success": False, "message": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"success": False, "message": str(e)}

def tampilkan_halaman():
    st.title("📩 OTP HUB - PINTAR MEDIA v2.0")
    API_KEY = st.secrets.get("OTPNUM_API_KEY", "")

    tab_lokal, tab_online = st.tabs(["📱 SMS LOKAL (ACTIVE)", "🛒 SEWA NOMOR ONLINE"])

    # ==========================================================================
    # TAB 1: SMS LOKAL
    # ==========================================================================
    with tab_lokal:
        waktu_cutoff = (datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        try:
            data_otp = database.supabase.table("OTP_Log").select("*").gte("created_at", waktu_cutoff).order("created_at", desc=True).execute()
            df_otp = pd.DataFrame(data_otp.data)
        except: df_otp = pd.DataFrame()

        with st.container(border=True):
            c_search, c_ref, c_del = st.columns([3, 1, 1])
            search_q = c_search.text_input("Cari...", placeholder="Filter...", key="search_lokal")
            if c_ref.button("🔄 REFRESH", use_container_width=True, key="ref_lokal"): st.rerun()
            if c_del.button("🗑️ CLEAR", use_container_width=True, key="clr_lokal"):
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
                    c1.markdown(f"PENGIRIM: **{r['SENDER']}**")
                    c2.markdown(f"<h2 style='margin:0; text-align:right; color:#F1FA8C;'>{otp_code}</h2>", unsafe_allow_html=True)
                    st.markdown(f"<div style='background:#1e1e1e; padding:10px; border-radius:8px; margin-top:5px; color:#CCC; font-size:13px;'>{r['MESSAGE']}</div>", unsafe_allow_html=True)
        else:
            st.info("Belum ada SMS masuk 1 jam terakhir.")

    # ==========================================================================
    # TAB 2: SEWA NOMOR ONLINE (3 KOLOM SEJAJAR)
    # ==========================================================================
    with tab_online:
        dict_server = {
            "Server 2": "https://otpnum.com/api/v2/",
            "Server 1": "https://otpnum.com/api/",
            "Server 3": "https://otpnum.com/api/v3/"
        }
        
        # --- HEADER 3 KOLOM: SERVER | REFRESH | SALDO ---
        with st.container(border=True):
            c_srv, c_ref, c_bal = st.columns([2, 1, 1.5])
            
            # Kolom 1: Pilih Server
            srv_name = c_srv.selectbox("Server", list(dict_server.keys()), index=0, key="sel_server_online", label_visibility="collapsed")
            srv_url = dict_server[srv_name]

            # Kolom 2: Tombol Refresh
            if c_ref.button("🔄 REFRESH", use_container_width=True, key="ref_bal_online"):
                if "list_services_v2" in st.session_state: del st.session_state.list_services_v2
                st.rerun()

            # Ambil Saldo
            res_bal = get_otpnum_api(srv_url, "balance", {"api_key": API_KEY})
            saldo = clean_angka(res_bal['data'].get('balance', 0)) if res_bal and res_bal.get('success') else 0
            
            # Kolom 3: Saldo (Rata Kanan)
            c_bal.markdown(f"<div style='text-align:right;'><p style='margin:0; color:gray; font-size:11px;'>SALDO</p><h3 style='margin:0; color:#50FA7B;'>Rp {saldo:,}</h3></div>", unsafe_allow_html=True)

        # --- PANEL ORDER (GOOGLE ONLY) ---
        st.markdown("#### 🛒 Sewa Nomor Baru")
        with st.container(border=True):
            # Load & Filter Services
            if "list_services_v2" not in st.session_state or st.session_state.get("current_srv") != srv_name:
                res_serv = get_otpnum_api(srv_url, "services", {"api_key": API_KEY, "country_id": 6})
                if res_serv and res_serv.get('success'):
                    st.session_state.list_services_v2 = res_serv['data']['services']
                    st.session_state.current_srv = srv_name

            list_s = st.session_state.get("list_services_v2", [])
            keywords = ['google', 'youtube', 'gmail']
            filtered_s = [s for s in list_s if any(k in s['service_name'].lower() for k in keywords)]
            
            opts = {f"{s['service_name']} - Rp {s['price']}": s['service_id'] for s in filtered_s}
            
            if opts:
                pilih_name = st.selectbox("Pilih Layanan", list(opts.keys()), key="pilih_google_only", label_visibility="collapsed")
                if st.button("🚀 BELI NOMOR SEKARANG", use_container_width=True, type="primary", key="btn_beli_virtual"):
                    sid = opts[pilih_name]
                    res_order = get_otpnum_api(srv_url, "order", {"api_key": API_KEY, "service_id": sid, "operator": "any", "country_id": 6})
                    if res_order and res_order.get('success'):
                        st.session_state.active_order = {"id": res_order['data']['order_id'], "number": res_order['data']['number'], "url": srv_url}
                        st.rerun()
                    else:
                        st.error(f"Gagal: {res_order.get('message') if res_order else 'Stok Habis'}")
            else:
                st.warning("Layanan Google tidak ditemukan.")

        # --- AUTO-POLLING SMS ---
        if "active_order" in st.session_state:
            # (Bagian Auto-Polling tetap sama ya Dian...)
            ord = st.session_state.active_order
            with st.container(border=True):
                st.markdown(f"**NOMOR:** `{ord.get('number')}`")
                msg_area = st.empty()
                res_stat = get_otpnum_api(ord.get('url'), "status", {"api_key": API_KEY, "order_id": ord.get('id')})
                if res_stat and res_stat['data'].get('sms') and res_stat['data']['sms'] != "waiting":
                    st.session_state.otp_online = res_stat['data']['sms']
                    msg_area.success(f"🔥 OTP: {st.session_state.otp_online}")
                    st.balloons()
                else:
                    msg_area.info("⏳ Menunggu SMS... (10s)")
                    time.sleep(10)
                    st.rerun()
                
                if st.button("❌ SELESAI / CANCEL", use_container_width=True, key="btn_cancel_virtual"):
                    get_otpnum_api(ord.get('url'), "cancel", {"api_key": API_KEY, "order_id": ord.get('id')})
                    if "active_order" in st.session_state: del st.session_state.active_order
                    if "otp_online" in st.session_state: del st.session_state.otp_online
                    st.rerun()
