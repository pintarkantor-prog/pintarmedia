import streamlit as st
import pandas as pd
from modules import database
import time
import re
import requests
from datetime import datetime, timedelta

# Matikan peringatan SSL buat jaga-jaga
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- FUNGSI API UNIVERSAL ---
def get_otpnum_api(server_url, endpoint, params):
    try:
        # Pastikan URL diakhiri slash sebelum endpoint
        base = server_url if server_url.endswith("/") else f"{server_url}/"
        full_url = f"{base}{endpoint}"
        headers = {"User-Agent": "Mozilla/5.0"}
        # Pakai verify=False dan headers buat tembus blokir IP/SSL
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
    # TAB 1: SMS LOKAL (GAYA MODERN - 1 JAM TERAKHIR)
    # ==========================================================================
    with tab_lokal:
        waktu_cutoff = (datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        try:
            data_otp = database.supabase.table("OTP_Log").select("*").gte("created_at", waktu_cutoff).order("created_at", desc=True).execute()
            df_otp = pd.DataFrame(data_otp.data)
        except: df_otp = pd.DataFrame()

        with st.container(border=True):
            c_search, c_ref, c_del = st.columns([3, 1, 1])
            search_q = c_search.text_input("Filter SMS...", placeholder="Cari...", key="search_lokal")
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
            st.info("Belum ada SMS masuk dalam 1 jam terakhir.")

    # ==========================================================================
    # TAB 2: SEWA NOMOR ONLINE (SERVER 1, 2, 3)
    # ==========================================================================
    with tab_online:
        # Konfigurasi URL sesuai permintaan Dian
        dict_server = {
            "Server 2": "https://otpnum.com/api/v2/",
            "Server 1": "https://otpnum.com/api/",
            "Server 3": "https://otpnum.com/api/v3/"
        }
        
        col_srv, col_bal = st.columns([1, 1])
        srv_name = col_srv.selectbox("Pilih Server", list(dict_server.keys()), index=0, key="sel_server_online")
        srv_url = dict_server[srv_name]

        # Cek Saldo
        res_bal = get_otpnum_api(srv_url, "balance", {"api_key": API_KEY})
        saldo = res_bal['data']['balance'] if res_bal and res_bal.get('success') else 0
        col_bal.markdown(f"### 💰 Rp {saldo:,}")

        st.markdown("#### 🛒 Sewa Nomor (Filter: Google Only)")
        with st.container(border=True):
            # Load & Filter Services
            res_serv = get_otpnum_api(srv_url, "services", {"api_key": API_KEY, "country_id": 6})
            
            if res_serv and res_serv.get('success'):
                keywords = ['google', 'youtube', 'gmail']
                all_s = res_serv['data']['services']
                # Hanya tampilkan yang mengandung kata kunci biar gak usah scroll
                filtered_s = [s for s in all_s if any(k in s['service_name'].lower() for k in keywords)]
                
                opts = {f"{s['service_name']} - Rp {s['price']}": s['service_id'] for s in filtered_s}
                
                if opts:
                    pilih_layanan = st.selectbox("Layanan Tersedia", list(opts.keys()), key="pilih_google_only")
                    if st.button("🚀 BELI NOMOR SEKARANG", use_container_width=True, type="primary", key="btn_beli_virtual"):
                        sid = opts[pilih_layanan]
                        res_order = get_otpnum_api(srv_url, "order", {"api_key": API_KEY, "service_id": sid, "operator": "any", "country_id": 6})
                        if res_order and res_order.get('success'):
                            st.session_state.active_order = {"id": res_order['data']['order_id'], "number": res_order['data']['number'], "url": srv_url}
                            st.rerun()
                else:
                    st.warning("Layanan Google tidak ditemukan di server ini.")
            else:
                st.error("Gagal memuat layanan. Cek koneksi API.")

        # --- AUTO-CHECK SMS (NON-STOP SAMPAI KODE MUNCUL) ---
        if "active_order" in st.session_state:
            ord = st.session_state.active_order
            with st.container(border=True):
                st.markdown(f"**NOMOR AKTIF:** `{ord['number']}`")
                
                # Placeholder buat status (biar gak numpuk)
                msg_area = st.empty()
                
                # Hitung mundur atau status
                res_stat = get_otpnum_api(ord['url'], "status", {"api_key": API_KEY, "order_id": ord['id']})
                
                if res_stat and res_stat['data'].get('sms') and res_stat['data']['sms'] != "waiting":
                    st.session_state.otp_online = res_stat['data']['sms']
                    msg_area.success(f"🔥 OTP DITEMUKAN: {st.session_state.otp_online}")
                    st.balloons()
                else:
                    msg_area.info("⏳ Menunggu SMS... (Web akan cek otomatis tiap 10 detik)")
                    time.sleep(10)
                    st.rerun()
                
                if st.button("❌ SELESAI / CANCEL", use_container_width=True, key="btn_cancel_virtual"):
                    get_otpnum_api(ord['url'], "cancel", {"api_key": API_KEY, "order_id": ord['id']})
                    del st.session_state.active_order
                    if "otp_online" in st.session_state: del st.session_state.otp_online
                    st.rerun()
