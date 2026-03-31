import streamlit as st
import pandas as pd
from modules import database
import time

def tampilkan_area_staf():
    # 1. SETUP IDENTITAS & HEADER
    user_aktif = st.session_state.get("user_aktif", "User").upper()
    st.markdown(f"### 📘 AREA STAF - PT PINTAR DIGITAL KREASI")
    st.write(f"Selamat bertugas, **{user_aktif}**!")

    # 2. PEMBUATAN SUB-MENU (TAB)
    tab_tugas, tab_panduan, tab_peraturan, tab_kontrak = st.tabs([
        "📝 TUGAS KERJA", 
        "📖 PANDUAN KERJA", 
        "⚖️ PERATURAN KERJA", 
        "📜 KONTRAK KERJA"
    ])

    # --- TAB 1: TUGAS KERJA (DINAMIS DARI SUPABASE) ---
    with tab_tugas:
        st.markdown("#### ⚡ Update Progres Akun")
        df_ch = database.load_data_channel()
        
        # Dashboard Mini
        total_standby = len(df_ch[df_ch['STATUS'] == 'STANDBY'])
        st.info(f"Ada **{total_standby}** akun berstatus STANDBY yang menunggu dieksekusi.")

        with st.form("form_lapor_staf", clear_on_submit=True):
            list_standby = df_ch[df_ch['STATUS'] == 'STANDBY']['EMAIL'].tolist()
            sel_email = st.selectbox("Pilih Akun yang Dikerjakan", list_standby if list_standby else ["Semua Beres!"])
            sel_status = st.selectbox("Update Status", ["PROSES", "SUSPEND", "BUSUK"])
            catatan = st.text_area("Catatan Kerja (Misal: Kendala login / Slot HP)")
            
            if st.form_submit_button("🚀 KIRIM LAPORAN", use_container_width=True):
                if sel_email != "Semua Beres!":
                    try:
                        database.supabase.table("Channel_Pintar").update({
                            "STATUS": sel_status,
                            "EDITED": f"Update by {user_aktif}: {catatan}"
                        }).eq("EMAIL", sel_email).execute()
                        
                        database.tambah_log(user_aktif, f"Lapor {sel_email} -> {sel_status}")
                        st.success(f"Daging! Status {sel_email} berhasil diperbarui.")
                        st.cache_data.clear()
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Gagal update: {e}")
                else:
                    st.warning("Tidak ada akun untuk di-update.")

    # --- TAB 2: PANDUAN KERJA (SOP OPERASIONAL) ---
    with tab_panduan:
        st.markdown("#### 📖 SOP Operasional Produksi")
        with st.expander("1. Cara Login & Amankan Akun"):
            st.write("""
            - Gunakan perangkat yang sudah ditentukan (Unit HP sesuai slot).
            - Pastikan IP stabil sebelum login.
            - Segera lapor di sistem jika akun meminta verifikasi nomor HP.
            """)
        with st.expander("2. Alur Produksi Video AI"):
            st.write("""
            - Gunakan prompt yang sudah diuji di PINTAR AI LAB.
            - Pastikan watermark brand terpasang dengan benar.
            - Upload pada jam prime time sesuai jadwal masing-masing channel.
            """)

    # --- TAB 3: PERATURAN KERJA (KEDISIPLINAN) ---
    with tab_peraturan:
        st.warning("⚠️ Harap dipatuhi demi kenyamanan bersama.")
        st.markdown("""
        1. **Jam Operasional:** Fleksibel namun target harian wajib terpenuhi.
        2. **Kerahasiaan:** Dilarang menyebarkan prompt eksklusif atau struktur database perusahaan.
        3. **Laporan:** Wajib mengisi update status di Tab 'Tugas Kerja' segera setelah pengerjaan selesai.
        4. **Alat:** Menjaga kebersihan dan keamanan unit HP yang dipinjamkan.
        """)

    # --- TAB 4: KONTRAK KERJA (ARSIP PRIBADI) ---
    with tab_kontrak:
        st.markdown(f"#### 📜 Dokumen Kontrak: {user_aktif}")
        st.info("Dokumen kontrak Anda tersimpan secara aman di database.")
        # Opsi: Bisa lo kasih tombol download PDF kontrak asli di sini
        if st.button("📄 Lihat Ringkasan Kontrak"):
            st.write(f"- **Posisi:** Creator AI & Data Operator")
            st.write(f"- **Masa Berlaku:** Sesuai kesepakatan tertulis di PT Pintar Digital Kreasi.")
            st.write(f"- **Status Penandatanganan:** ✅ Terverifikasi")
