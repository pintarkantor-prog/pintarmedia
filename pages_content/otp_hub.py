import streamlit as st
import pandas as pd
from modules import database
import time
import re
import requests
from datetime import datetime, timedelta

# --- FUNGSI API (DEBUG MODE) ---
def get_otpnum_v2(endpoint, params):
    try:
        base_url = "https://otpnum.com/api/v2"
        # Kita print ke terminal buat jaga-jaga
        response = requests.get(f"{base_url}/{endpoint}", params=params, timeout=15)
        if response.status_code == 200:
            return response.json()
        else:
            return {"success": False, "message": f"Server Error {response.status_code}"}
    except Exception as e:
        return {"success": False, "message": str(e)}

def tampilkan_halaman():
    st.title("📩 OTP HUB - PINTAR MEDIA v2.0")
    
    # AMBIL API KEY DARI SECRETS (PASTIKAN NAMANYA SAMA)
    # Jika di secrets.toml kamu tulis [otpnum] api_key = "..." maka ganti kodenya
    API_KEY = st.secrets.get("OTPNUM_API_KEY", "")

    # --- PANEL DEBUG (HANYA MUNCUL KALO BELUM KONEK) ---
    if not API_KEY:
        st.error("❌ API KEY TIDAK DITEMUKAN DI SECRETS!")
    
    tab_lokal, tab_online = st.tabs(["📱 SMS LOKAL", "🛒 SEWA NOMOR ONLINE"])

    # --- TAB 1: SMS LOKAL ---
    with tab_lokal:
        # (Kode Tab Lokal tetep sama kayak sebelumnya ya Dian...)
        st.info("SMS Lokal Aktif.")

    # --- TAB 2: SEWA NOMOR ---
    with tab_online:
        # TOMBOL TES KONEKSI (BIAR KETAHUAN SALAHNYA DIMANA)
        if st.button("🔍 CEK KONEKSI API"):
            with st.status("Mencoba hubungi OTPNUM Server 2..."):
                res = get_otpnum_v2("balance", {"api_key": API_KEY})
                st.write("Respon Server:", res)

        # 1. CEK SALDO
        res_bal = get_otpnum_v2("balance", {"api_key": API_KEY})
        saldo = res_bal['data']['balance'] if res_bal and res_bal.get('success') else 0
        
        with st.container(border=True):
            s1, s2 = st.columns([2, 1])
            s1.markdown(f"### 💰 Saldo OTPNUM\n# Rp {saldo:,}")
            if s2.button("🔄 REFRESH SALDO", use_container_width=True): st.rerun()

        # 2. PANEL ORDER
        st.markdown("#### 🛒 Sewa Nomor Baru")
        with st.container(border=True):
            # Indonesia ID = 6
            country_id = 6 
            
            # Reset cache jika ganti server
            if "list_services_v2" not in st.session_state:
                res_serv = get_otpnum_v2("services", {"api_key": API_KEY, "country_id": country_id})
                if res_serv and res_serv.get('success'):
                    st.session_state.list_services_v2 = res_serv['data']['services']
                else:
                    st.warning(f"Gagal muat layanan: {res_serv.get('message') if res_serv else 'Timeout'}")

            list_s = st.session_state.get("list_services_v2", [])
            options_serv = {f"{s['service_name']} - Rp {s['price']}": s['service_id'] for s in list_s}
            
            pilih_name = st.selectbox("Pilih Layanan", list(options_serv.keys()) if options_serv else ["Belum terkoneksi..."])
            service_id = options_serv.get(pilih_name)

            if st.button("🚀 BELI NOMOR SEKARANG", use_container_width=True, type="primary"):
                if service_id:
                    res_order = get_otpnum_v2("order", {
                        "api_key": API_KEY, "service_id": service_id, "operator": "any", "country_id": country_id
                    })
                    if res_order and res_order.get('success'):
                        st.session_state.active_order = {"id": res_order['data']['order_id'], "number": res_order['data']['number'], "name": pilih_name}
                        st.rerun()
                    else: st.error("Gagal Order!")

        # 3. MONITORING AKTIF
        if "active_order" in st.session_state:
            ord = st.session_state.active_order
            with st.container(border=True):
                st.write(f"Nomor: **{ord['number']}**")
                if st.button("🔄 CEK SMS", use_container_width=True):
                    res_stat = get_otpnum_v2("status", {"api_key": API_KEY, "order_id": ord['id']})
                    if res_stat and res_stat['data'].get('sms') and res_stat['data']['sms'] != "waiting":
                        st.session_state.otp_online = res_stat['data']['sms']
                        st.balloons()
                
                if st.button("❌ CANCEL", use_container_width=True):
                    del st.session_state.active_order
                    st.rerun()

                if "otp_online" in st.session_state:
                    st.success(f"OTP: {st.session_state.otp_online}")
