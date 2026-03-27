import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import time
import socket
from modules import database  # Memastikan koneksi ke database.py

def tampilkan_database_channel():
    # --- 1. PROTEKSI LEVEL AKSES (HANYA OWNER & ADMIN) ---
    level_aktif = st.session_state.get("user_level", "STAFF")
    user_aktif = st.session_state.get("user_aktif", "User").upper()
    
    # Cek apakah user punya otoritas
    if level_aktif not in ["OWNER", "ADMIN"]:
        st.error("🚫 AKSES DITOLAK!")
        st.info("Halaman ini hanya dapat diakses oleh Owner dan Admin. Silakan hubungi Boss Dian jika ini adalah kesalahan.")
        st.stop() # Menghentikan seluruh proses render ke bawah

    # --- 2. HEADER & SETUP ---
    st.title("📱 DATABASE MASTER CHANNEL")
    tz = pytz.timezone('Asia/Jakarta')
    
    # Penanda Otoritas
    st.caption(f"Logged in as: {user_aktif} | Role: {level_aktif} | System: Murni Supabase (No GSheet)")

    # --- 3. PENARIKAN DATA REAL-TIME ---
    with st.spinner("Sinkronisasi Radar Supabase..."):
        df = database.ambil_data("Channel_Pintar")
        df_hp = database.ambil_data("Data_HP")

    if df.empty:
        st.warning("Gagal memuat data. Pastikan tabel 'Channel_Pintar' ada di Supabase.")
        return

    # --- 4. PEMBUATAN TAB ---
    tab_st, tab_pr, tab_jd, tab_hp, tab_sd, tab_ar = st.tabs([
        "📦 STOK STANDBY", "🚀 CHANNEL PROSES", "📅 JADWAL UPLOAD", 
        "📱 MONITOR HP", "💰 SOLD CHANNEL", "📂 ARSIP"
    ])

    # ==============================================================================
    # TAB 1: STOK STANDBY
    # ==============================================================================
    with tab_st:
        total_st = len(df[df['STATUS'] == 'STANDBY'])
        total_pr = len(df[df['STATUS'] == 'PROSES'])
        
        # Dashboard Metrik
        with st.container(border=True):
            m1, m2, m3 = st.columns(3)
            m1.metric("📦 STOK READY", f"{total_st}")
            m2.metric("🚀 SEDANG PROSES", f"{total_pr}")
            m3.metric("📱 UNIT HP", f"{len(df_hp)}")

        # --- FORM INPUT AKUN BARU ---
        with st.expander("➕ TAMBAH AKUN BARU KE SUPABASE", expanded=False):
            with st.form("input_akun_v2", clear_on_submit=True):
                f1, f2, f3 = st.columns(3)
                v_mail = f1.text_input("📧 Email Login")
                v_pass = f2.text_input("🔑 Password")
                v_nama = f3.text_input("📺 Nama Channel")
                
                f4, f5 = st.columns([1, 2])
                v_subs = f4.text_input("📊 Subs")
                v_link = f5.text_input("🔗 Link Channel")
                
                if st.form_submit_button("🚀 SIMPAN SEKARANG", use_container_width=True):
                    if v_nama and v_mail:
                        tgl_now = datetime.now(tz).strftime("%d/%m/%Y %H:%M")
                        data_insert = {
                            "TANGGAL": tgl_now, "EMAIL": v_mail.strip().lower(),
                            "PASSWORD": v_pass, "NAMA_CHANNEL": v_nama,
                            "SUBSCRIBE": v_subs, "LINK_CHANNEL": v_link,
                            "STATUS": "STANDBY", "PENCATAT": user_aktif,
                            "EDITED": f"New: {user_aktif} ({tgl_now})"
                        }
                        database.supabase.table("Channel_Pintar").insert(data_insert).execute()
                        st.success(f"✅ Akun {v_mail} Berhasil Masuk!")
                        time.sleep(1)
                        st.rerun()

        # --- DATA EDITOR STANDBY ---
        df_st = df[df['STATUS'] == 'STANDBY'].copy()
        if not df_st.empty:
            df_st['REAL_IDX'] = df_st.index
            edited_st = st.data_editor(
                df_st[["EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "STATUS", "REAL_IDX"]],
                use_container_width=True, hide_index=True, key="edit_stok",
                column_config={
                    "STATUS": st.column_config.SelectboxColumn("STATUS", options=["STANDBY", "PROSES", "SOLD", "BUSUK", "SUSPEND"]),
                    "REAL_IDX": None
                }
            )
            
            # Logika Simpan Perubahan (Batch Upsert)
            if st.button("💾 SIMPAN PERUBAHAN STOK", type="primary", use_container_width=True):
                batch_data = []
                for _, row in edited_st.iterrows():
                    idx = int(row['REAL_IDX'])
                    old = df.iloc[idx]
                    # Hanya ambil yang berubah
                    if row['STATUS'] != old['STATUS']:
                        tgl_now = datetime.now(tz).strftime("%d/%m/%Y %H:%M")
                        batch_data.append({
                            "EMAIL": row['EMAIL'], "STATUS": row['STATUS'],
                            "EDITED": f"Up: {user_aktif} ({tgl_now})"
                        })
                if batch_data:
                    database.simpan_perubahan_channel(batch_data)
                    st.success(f"✅ {len(batch_data)} Akun Berhasil Diupdate!")
                    time.sleep(1)
                    st.rerun()

    # ==============================================================================
    # TAB 2: CHANNEL PROSES
    # ==============================================================================
    with tab_pr:
        df_pr = df[df['STATUS'] == 'PROSES'].copy()
        if not df_pr.empty:
            df_pr['HP_N'] = pd.to_numeric(df_pr['HP'], errors='coerce').fillna(999)
            df_pr = df_pr.sort_values('HP_N')
            
            st.dataframe(
                df_pr[["HP", "EMAIL", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL"]],
                use_container_width=True, hide_index=True,
                column_config={"LINK_CHANNEL": st.column_config.LinkColumn("🔗 URL")}
            )
        else:
            st.info("Belum ada akun yang sedang diproses di HP.")

    # ==============================================================================
    # TAB 3: JADWAL UPLOAD
    # ==============================================================================
    with tab_jd:
        df_jd = df[df['STATUS'] == 'PROSES'].copy()
        if not df_jd.empty:
            # Monitoring Jam Sederhana
            st.dataframe(
                df_jd[["HP", "NAMA_CHANNEL", "PAGI", "SIANG", "SORE"]].sort_values("HP"),
                use_container_width=True, hide_index=True
            )
        else:
            st.info("Jadwal kosong (Pindahkan akun ke status PROSES dulu).")

    # ==============================================================================
    # TAB 4: MONITOR HP
    # ==============================================================================
    with tab_hp:
        if not df_hp.empty:
            # Tampilan Grid HP sesuai kodemu yang lama
            cols = st.columns(4)
            for i, (idx, r) in enumerate(df_hp.iterrows()):
                with cols[i % 4]:
                    with st.container(border=True):
                        st.markdown(f"**{r['NAMA_HP']}**")
                        st.caption(f"{r['PROVIDER']} | {r['NOMOR_HP']}")
                        st.code(f"Exp: {r['MASA_AKTIF']}")
        else:
            st.warning("Data HP belum didaftarkan.")

    # ==============================================================================
    # TAB 5 & 6: SOLD & ARSIP (Satu Jalur)
    # ==============================================================================
    with tab_sd:
        st.dataframe(df[df['STATUS'] == 'SOLD'], use_container_width=True, hide_index=True)
        
    with tab_ar:
        st.dataframe(df[df['STATUS'].isin(['BUSUK', 'SUSPEND'])], use_container_width=True, hide_index=True)
