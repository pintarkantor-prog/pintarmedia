import streamlit as st
import pandas as pd
from modules import database  # Import mesin database lo
import time

def tampilkan_area_staf():
    # 1. SETUP IDENTITAS
    user_aktif = st.session_state.get("user_aktif", "User").upper()
    
    st.markdown(f"### 📘 AREA STAF - PT PINTAR DIGITAL KREASI")
    st.write(f"Selamat bertugas, **{user_aktif}**! Pantau tugas dan lapor progres di sini.")

    # 2. TARIK DATA DARI SUPABASE (Tanpa Cache biar Real-time)
    df_ch = database.load_data_channel()
    df_hp = database.load_data_hp()

    if df_ch.empty:
        st.warning("Data channel kosong atau gagal load.")
        return

    # 3. DASHBOARD MONITORING (Gaya Radar)
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    total_standby = len(df_ch[df_ch['STATUS'] == 'STANDBY'])
    total_proses = len(df_ch[df_ch['STATUS'] == 'PROSES'])
    hp_live = len(df_hp[df_hp['STATUS'] == 'LIVE'])

    col1.metric("📦 TUGAS STANDBY", f"{total_standby} Akun")
    col2.metric("🚀 SEDANG PROSES", f"{total_proses} Akun")
    col3.metric("📱 UNIT HP READY", f"{hp_live} Unit")

    # 4. AREA KERJA (TABS)
    tab_list, tab_update, tab_perangkat = st.tabs(["📋 DAFTAR TUGAS", "⚡ UPDATE PROGRES", "📲 CEK HP"])

    with tab_list:
        st.markdown("#### Akun Status STANDBY")
        # Tampilkan data yang perlu dikerjakan saja
        df_tugas = df_ch[df_ch['STATUS'] == 'STANDBY'][['EMAIL', 'PASSWORD', 'NAMA_CHANNEL', 'SUBSCRIBE']]
        st.dataframe(df_tugas, use_container_width=True, hide_index=True)

    with tab_update:
        st.markdown("#### Form Laporan Kerja")
        with st.form("form_lapor", clear_on_submit=True):
            # List email yang statusnya masih STANDBY
            list_email = df_ch[df_ch['STATUS'] == 'STANDBY']['EMAIL'].tolist()
            
            sel_email = st.selectbox("Pilih Email yang Selesai Dikerjakan", list_email if list_email else ["Semua Beres!"])
            sel_status = st.selectbox("Update Menjadi", ["PROSES", "SUSPEND", "BUSUK"])
            catatan = st.text_input("Catatan (Misal: Slot HP 5)")

            if st.form_submit_button("🚀 KIRIM LAPORAN", use_container_width=True):
                if sel_email == "Semua Beres!":
                    st.error("Gak ada email yang bisa di-update, Coy!")
                else:
                    try:
                        # Panggil koneksi supabase dari module database lo
                        database.supabase.table("Channel_Pintar").update({
                            "STATUS": sel_status,
                            "EDITED": f"Update by {user_aktif}: {catatan}"
                        }).eq("EMAIL", sel_email).execute()

                        # Catat Log
                        database.tambah_log(user_aktif, f"Lapor {sel_email} -> {sel_status}")
                        
                        st.success(f"Daging! {sel_email} berhasil di-update ke {sel_status}.")
                        st.cache_data.clear() # Reset cache biar data langsung berubah
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Gagal Simpan: {e}")

    with tab_perangkat:
        st.markdown("#### Monitoring Unit HP")
        st.dataframe(df_hp[['UNIT', 'STATUS', 'PROVIDER']], use_container_width=True, hide_index=True)
