import streamlit as st
import pandas as pd
from modules import database
import time
import re

def tampilkan_halaman():
    st.title("📩 OTP HUB SMS")
    
    # --- 1. AMBIL DATA DARI SUPABASE (URUTAN TERBARU DI ATAS) ---
    try:
        # Perintah .order("created_at", desc=True) memastikan SMS paling baru muncul pertama
        data_otp = database.supabase.table("OTP_Log").select("*").order("created_at", desc=True).limit(50).execute()
        df_otp = pd.DataFrame(data_otp.data)
    except Exception as e:
        st.error(f"Gagal narik data OTP: {e}")
        return

    # --- 2. SINGLE EXPANDER UNTUK SEMUA ---
    with st.expander("🛠️ PANEL KONTROL & DAFTAR SMS", expanded=True):
        
        # --- BARIS 1: PENCARIAN ---
        search_query = st.text_input("Cari...", placeholder="Ketik Unit HP, Pengirim, atau Kode...", label_visibility="collapsed")
        
        # --- BARIS 2: TOMBOL AKSI (SEJAJAR & WARNA NETRAL) ---
        c1, c2 = st.columns(2)
        
        if c1.button("🔄 REFRESH DATA", use_container_width=True):
            st.rerun()

        if c2.button("🗑️ BERSIHKAN LOG", use_container_width=True):
            if st.session_state.get("user_level") == "OWNER":
                database.supabase.table("OTP_Log").delete().neq("id", 0).execute()
                st.success("Log dikosongkan.")
                time.sleep(0.5)
                st.rerun()
            else:
                st.warning("Akses Ditolak!")

        st.markdown("<hr style='margin:15px 0; border-color:#444;'>", unsafe_allow_html=True)

        # --- BARIS 3: LIST SMS ---
        if not df_otp.empty:
            if search_query:
                # Filter pencarian tetap mempertahankan urutan terbaru di atas
                mask = (
                    df_otp['RECEIVER'].astype(str).str.contains(search_query, case=False, na=False) |
                    df_otp['SENDER'].astype(str).str.contains(search_query, case=False, na=False) |
                    df_otp['MESSAGE'].astype(str).str.contains(search_query, case=False, na=False)
                )
                df_display = df_otp[mask].copy()
            else:
                df_display = df_otp.copy()

            if df_display.empty:
                st.info("Pencarian tidak ditemukan.")
            else:
                # Loop render card
                for i, r in df_display.iterrows():
                    # Konversi Waktu ke WIB
                    dt_obj = pd.to_datetime(r['created_at']).tz_convert('Asia/Jakarta')
                    waktu_str = dt_obj.strftime('%d/%m %H:%M:%S')
                    
                    # Cari 6 digit OTP
                    otp_match = re.findall(r'\b\d{6}\b', str(r['MESSAGE']))
                    otp_code = otp_match[0] if otp_match else "---"

                    with st.container(border=True):
                        col_a, col_b = st.columns([1, 1])
                        col_a.markdown(f"**📱 {r['RECEIVER']}**")
                        col_b.markdown(f"<p style='text-align:right; color:gray; font-size:12px;'>{waktu_str} WIB</p>", unsafe_allow_html=True)
                        
                        cp, co = st.columns([2, 1])
                        cp.markdown(f"<p style='margin:0; font-size:11px; color:gray;'>PENGIRIM</p><b>{r['SENDER']}</b>", unsafe_allow_html=True)
                        co.markdown(f"<p style='margin:0; font-size:11px; color:gray; text-align:right;'>KODE</p><h3 style='margin:0; text-align:right; color:#FF4B4B;'>{otp_code}</h3>", unsafe_allow_html=True)
                        
                        st.markdown(f"<p style='margin-top:10px; font-size:13px; color:#DDD; background:#1e1e1e; padding:10px; border-radius:5px;'>{r['MESSAGE']}</p>", unsafe_allow_html=True)
        else:
            st.info("Belum ada SMS masuk.")

    st.caption(f"🔄 Last Update: {database.ambil_waktu_sekarang().strftime('%H:%M:%S')} WIB")
