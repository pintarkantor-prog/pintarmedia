import streamlit as st
import pandas as pd
from modules import database
import time
import re
import requests

def ambil_saldo_otpnum(api_key):
    try:
        url = f"https://otpnum.com/api/get_profile?api_key={api_key}"
        res = requests.get(url).json()
        return res['data']['balance'] if res.get('success') else 0
    except: return 0

def tampilkan_halaman():
    st.title("📩 OTP HUB - PINTAR MEDIA v2.0")
    API_KEY_OTPNUM = st.secrets.get("OTPNUM_API_KEY", "")

    tab_lokal, tab_online = st.tabs(["📱 SMS LOKAL (25 HP)", "🛒 SEWA NOMOR ONLINE"])

    # ==========================================================================
    # TAB 1: SMS LOKAL (EXPANDER + CARD)
    # ==========================================================================
    with tab_lokal:
        try:
            data_otp = database.supabase.table("OTP_Log").select("*").order("created_at", desc=True).limit(50).execute()
            df_otp = pd.DataFrame(data_otp.data)
        except: df_otp = pd.DataFrame()

        with st.expander("🛠️ PANEL KONTROL & DAFTAR SMS", expanded=True):
            search_query = st.text_input("Cari SMS...", placeholder="Ketik Unit, Pengirim, atau Kode...", label_visibility="collapsed")
            c1, c2 = st.columns(2)
            if c1.button("🔄 REFRESH SMS", use_container_width=True): st.rerun()
            if c2.button("🗑️ BERSIHKAN LOG", use_container_width=True):
                if st.session_state.get("user_level") == "OWNER":
                    database.supabase.table("OTP_Log").delete().neq("id", 0).execute()
                    st.rerun()

            st.markdown("<hr style='margin:15px 0; border-color:#444;'>", unsafe_allow_html=True)

            if not df_otp.empty:
                # Filter pencarian
                df_display = df_otp[df_otp.apply(lambda row: search_query.lower() in str(row).lower(), axis=1)] if search_query else df_otp
                
                for i, r in df_display.iterrows():
                    dt_obj = pd.to_datetime(r['created_at']).tz_convert('Asia/Jakarta')
                    otp_match = re.findall(r'\b\d{6}\b', str(r['MESSAGE']))
                    otp_code = otp_match[0] if otp_match else "---"
                    
                    # CARD DALAM EXPANDER
                    with st.container(border=True):
                        ca, cb = st.columns([1, 1])
                        ca.markdown(f"**📱 {r['RECEIVER']}**")
                        cb.markdown(f"<p style='text-align:right; color:gray; font-size:12px;'>{dt_obj.strftime('%d/%m %H:%M:%S')}</p>", unsafe_allow_html=True)
                        cp, co = st.columns([2, 1])
                        cp.markdown(f"PENGIRIM: **{r['SENDER']}**")
                        co.markdown(f"<h3 style='margin:0; text-align:right; color:#FF4B4B;'>{otp_code}</h3>", unsafe_allow_html=True)
                        st.markdown(f"<p style='background:#1e1e1e; padding:8px; border-radius:5px; font-size:13px;'>{r['MESSAGE']}</p>", unsafe_allow_html=True)
            else:
                st.info("Belum ada SMS masuk.")
        
        st.caption(f"🔄 Last Update SMS Lokal: {database.ambil_waktu_sekarang().strftime('%H:%M:%S')} WIB")

    # ==========================================================================
    # TAB 2: SEWA NOMOR ONLINE (MODERN CARD)
    # ==========================================================================
    with tab_online:
        saldo = ambil_saldo_otpnum(API_KEY_OTPNUM)
        
        # CARD SALDO (Pakai Container Border biar kyk Card)
        with st.container(border=True):
            col_s1, col_s2 = st.columns([2, 1])
            col_s1.markdown(f"### 💰 Saldo OTPNUM\n**Rp {saldo:,}**")
            if col_s2.button("➕ TOP UP", use_container_width=True):
                st.info("Silakan top up di web otpnum.com")

        st.markdown("#### 🛒 Sewa Nomor Baru")
        with st.container(border=True):
            c_lay, c_neg = st.columns(2)
            layanan = c_lay.selectbox("Layanan", ["Google", "Telegram", "WhatsApp", "Facebook"], label_visibility="collapsed")
            negara = c_neg.selectbox("Negara", ["Indonesia", "Vietnam", "Thailand"], label_visibility="collapsed")
            if st.button("🚀 BELI NOMOR SEKARANG", use_container_width=True, type="primary"):
                st.toast("Menghubungkan ke API OTPNUM...")

        st.markdown("#### 🕒 Nomor Aktif")
        # CARD HASIL BELI (Contoh Tampilan kalau sudah dapet nomor)
        with st.container(border=True):
            st.warning("Belum ada nomor yang sedang disewa. Silakan klik tombol Beli di atas.")
