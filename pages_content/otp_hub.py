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

# --- 1. FUNGSI MEMBERSIHKAN SALDO ---
def clean_angka(data):
    try:
        if data is None: return 0
        angka_bersih = re.sub(r'[^\d.]', '', str(data))
        if not angka_bersih: return 0
        return int(float(angka_bersih))
    except: return 0

# --- 2. FUNGSI API UNIVERSAL ---
def get_otpnum_api(server_url, endpoint, params):
    try:
        if not server_url: return None
        base = server_url if server_url.endswith("/") else f"{server_url}/"
        full_url = f"{base}{endpoint}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(full_url, params=params, timeout=15, headers=headers, verify=False)
        if response.status_code == 200: return response.json()
        return {"success": False, "message": f"HTTP {response.status_code}"}
    except Exception as e: return {"success": False, "message": str(e)}

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
            search_q = c_search.text_input("Cari SMS...", placeholder="Filter...", key="search_lokal")
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
                    st.markdown(f"<div style='display: flex; justify-content: space-between;'><span style='background:#FF4B4B; color:white; padding:2px 8px; border-radius:5px; font-size:12px;'>📱 {r['RECEIVER']}</span><small style='color:gray;'>{dt_obj.strftime('%H:%M:%S')} WIB</small></div>", unsafe_allow_html=True)
                    c1, c2 = st.columns([2, 1])
                    c1.markdown(f"<p style='margin:10px 0 0 0; color:#888; font-size:11px;'>PENGIRIM</p><b>{r['SENDER']}</b>", unsafe_allow_html=True)
                    c2.markdown(f"<p style='margin:10px 0 0 0; color:#888; font-size:11px; text-align:right;'>KODE OTP</p><h2 style='margin:0; text-align:right; color:#F1FA8C;'>{otp_code}</h2>", unsafe_allow_html=True)
                    st.markdown(f"<div style='background:#1e1e1e; padding:12px; border-radius:8px; margin-top:10px; border-left: 3px solid #444; color:#CCC; font-size:13px; line-height:1.4;'>{r['MESSAGE']}</div>", unsafe_allow_html=True)
        else:
            st.info("Belum ada SMS masuk.")

    # ==========================================================================
    # TAB 2: SEWA NOMOR ONLINE (SIMPLE 3 KOLOM)
    # ==========================================================================
    with tab_online:
        dict_server = {
            "Server 2 (Primary)": "https://otpnum.com/api/v2/",
            "Server 1 (Backup)": "https://otpnum.com/api/"
        }
        
        # --- HEADER 3 KOLOM: SERVER | SALDO | REFRESH ---
        with st.container(border=True):
            c_srv, c_bal, c_btn = st.columns([2, 1, 1])
            
            # 1. Pilih Server
            srv_name = c_srv.selectbox("Pilih Server", list(dict_server.keys()), index=0, key="sel_server_online", label_visibility="collapsed")
            srv_url = dict_server[srv_name]

            # 2. Ambil Saldo
            res_bal = get_otpnum_api(srv_url, "balance", {"api_key": API_KEY})
            saldo = clean_angka(res_bal['data'].get('balance', 0)) if res_bal and res_bal.get('success') else 0
            
            # Tampilan Saldo di Kolom Tengah/Kanan (Tanpa CSS)
            c_bal.markdown(f"**Saldo:**\nRp {saldo:,}")

            # 3. Tombol Refresh di Ujung Kanan
            if c_btn.button("🔄 REFRESH", use_container_width=True, key="ref_bal_online"):
                if "list_services_v2" in st.session_state: del st.session_state.list_services_v2
                st.rerun()

        # --- PANEL ORDER (GOOGLE ONLY) ---
        st.markdown("#### 🛒 Sewa Nomor Baru")
        with st.container(border=True):
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
                pilih_name = st.selectbox("Layanan Tersedia", list(opts.keys()), key="pilih_google_only")
                if st.button("🚀 BELI NOMOR SEKARANG", use_container_width=True, type="primary", key="btn_beli_virtual"):
                    sid = opts[pilih_name]
                    res_order = get_otpnum_api(srv_url, "order", {"api_key": API_KEY, "service_id": sid, "operator": "any", "country_id": 6})
                    if res_order and res_order.get('success'):
                        st.session_state.active_order = {"id": res_order['data']['order_id'], "number": res_order['data']['number'], "url": srv_url}
                        st.rerun()
            else: st.warning("Layanan Google tidak ditemukan.")

        # --- AUTO-POLLING SMS (VERSI FIX TOMBOL CANCEL) ---
        if "active_order" in st.session_state:
            ord = st.session_state.active_order
            current_url = ord.get('url')
            
            with st.container(border=True):
                st.markdown(f"**NOMOR AKTIF:** `{ord.get('number')}`")
                
                # PINDAHKAN TOMBOL CANCEL KE ATAS BIAR GAMPANG DIKLIK
                if st.button("❌ SELESAI / CANCEL NOMOR INI", use_container_width=True, key="btn_cancel_virtual", type="secondary"):
                    with st.spinner("Membatalkan/Menyelesaikan..."):
                        if current_url:
                            get_otpnum_api(current_url, "cancel", {"api_key": API_KEY, "order_id": ord.get('id')})
                        # Bersihkan semua session terkait order ini
                        if "active_order" in st.session_state: del st.session_state.active_order
                        if "otp_online" in st.session_state: del st.session_state.otp_online
                        st.rerun()

                st.divider()
                msg_area = st.empty()
                
                # Cek Status SMS
                if current_url:
                    res_stat = get_otpnum_api(current_url, "status", {"api_key": API_KEY, "order_id": ord.get('id')})
                    
                    if res_stat and res_stat.get('success') and res_stat['data'].get('sms') and res_stat['data']['sms'] != "waiting":
                        st.session_state.otp_online = res_stat['data']['sms']
                        msg_area.success(f"🔥 OTP DITEMUKAN: {st.session_state.otp_online}")
                        st.balloons()
                        # Jika sudah ada OTP, kita stop auto-refresh-nya
                        st.info("OTP sudah muncul. Klik 'SELESAI' jika sudah selesai menyalin.")
                    else:
                        msg_area.info("⏳ Menunggu SMS... (Web cek otomatis tiap 10 detik)")
                        time.sleep(10)
                        st.rerun()
