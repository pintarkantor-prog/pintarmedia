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
        st.info("Halaman ini hanya dapat diakses oleh Owner dan Admin.")
        st.stop() # Menghentikan seluruh proses render ke bawah

    # --- 2. HEADER & SETUP ---
    st.title("📱 DATABASE MASTER CHANNEL")
    tz = pytz.timezone('Asia/Jakarta') 

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
    # TAB 1: STOK STANDBY (GAYA RADAR UI v2.0 - FULL SUPABASE)
    # ==============================================================================
    with tab_st: # Sesuaikan nama variabel tab di atas
        # --- 1. LOGIKA HITUNG DATA (Real-time) ---
        total_st = len(df[df['STATUS'] == 'STANDBY'])
        total_pr = len(df[df['STATUS'] == 'PROSES'])
        
        # Hitung HP Aktif (Cek kolom HP yang tidak kosong)
        hp_aktif = len(df[df['HP'].notna() & (df['HP'].astype(str).str.strip() != "")]['HP'].unique())
        
        # --- LOGIKA STATUS VITAL ---
        selisih_vital = total_st - (total_pr + 10)
        status_stok = f"AMAN (+{selisih_vital})" if selisih_vital >= 0 else f"KRITIS ({selisih_vital})"
        warna_stok = "normal" if selisih_vital >= 0 else "inverse"
        
        # --- LOGIKA SOLD (Bulan Ini) ---
        now_indo = database.ambil_waktu_sekarang()
        bln_ini = now_indo.strftime("%m/%Y") 
        
        # Filter SOLD bulan ini berdasarkan kolom EDITED
        mask_ini = (df['STATUS'] == 'SOLD') & (df['EDITED'].astype(str).str.contains(bln_ini, na=False))
        sold_ini = len(df[mask_ini])
        
        # HITUNG ARSIP (SUSPEND + BUSUK)
        total_arsip = len(df[df['STATUS'].isin(['SUSPEND', 'BUSUK'])])

        # --- 2. RENDER DASHBOARD UI ---
        with st.container(border=True):
            c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1.2, 2.2])
            c1.metric("📦 CH STANDBY", f"{total_st}", delta=status_stok, delta_color=warna_stok)
            c2.metric("🚀 CH PROSES", f"{total_pr}", delta="ON PROCESS")
            c3.metric("📱 UNIT HP", f"{hp_aktif}", delta="LIVE")
            c4.metric("💰 SOLD (BLN)", f"{sold_ini}", delta="Bulan Ini")
            
            with c5:
                st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
                st.write(f"📢 **INFO SISTEM:**")
                st.write(f"Terdapat **{total_arsip}** akun di arsip (Suspend/Busuk).")

        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- 3. HEADER DATABASE & TOMBOL TAMBAH ---
        hc1, hc2 = st.columns([3, 1])
        hc1.markdown("#### 🔐 DATABASE STOK STANDBY")
        
        if hc2.button("➕ TAMBAH AKUN", use_container_width=True, type="primary"):
            st.session_state.form_baru = not st.session_state.get('form_baru', False)

        # --- 4. FORM INPUT AKUN BARU ---
        if st.session_state.get('form_baru', False):
            with st.container(border=True):
                with st.form("input_v6_icon", clear_on_submit=True):
                    f1, f2, f3 = st.columns(3)
                    v_mail = f1.text_input("📧 Email Login")
                    v_pass = f2.text_input("🔑 Password")
                    v_nama = f3.text_input("📺 Nama Channel")
                    
                    f4, f5 = st.columns([1, 2])
                    v_subs = f4.text_input("📊 Jumlah Subs")
                    v_link = f5.text_input("🔗 Link Channel")
                    
                    if st.form_submit_button("🚀 SIMPAN KE DATABASE", use_container_width=True):
                        if v_nama and v_mail:
                            tgl_now = now_indo.strftime("%d/%m/%Y %H:%M")
                            v_mail = v_mail.strip().lower() 
                            
                            try:
                                with st.spinner("Mendaftarkan akun..."):
                                    database.supabase.table("Channel_Pintar").insert({
                                        "TANGGAL": tgl_now, 
                                        "EMAIL": v_mail,
                                        "PASSWORD": v_pass,
                                        "NAMA_CHANNEL": v_nama,
                                        "SUBSCRIBE": v_subs,
                                        "LINK_CHANNEL": v_link,
                                        "STATUS": "STANDBY",
                                        "PENCATAT": user_aktif,
                                        "EDITED": f"New: {user_aktif} ({tgl_now})"
                                    }).execute()
                                
                                st.success(f"✅ MANTAP! Akun {v_mail} masuk Supabase.")
                                time.sleep(0.5)
                                st.rerun()
                            except Exception as e:
                                if "23505" in str(e):
                                    st.warning(f"⚠️ Email **{v_mail}** sudah terdaftar!")
                                else:
                                    st.error(f"❌ Masalah: {e}")
                        else:
                            st.error("⚠️ Email dan Nama Channel wajib diisi!")
                            
        # --- 5. GRID EDITOR STANDBY ---
        df_st = df[df['STATUS'] == 'STANDBY'].copy()
        if df_st.empty:
            st.info("Belum ada stok standby.")
        else:
            df_st['NO'] = range(1, len(df_st) + 1)
            df_st['REAL_IDX'] = df_st.index 
            df_st['SUBSCRIBE'] = df_st['SUBSCRIBE'].astype(str)

            config_st = {
                "NO": st.column_config.TextColumn("#️⃣ NO", width=30, disabled=True),
                "EMAIL": st.column_config.TextColumn("📧 EMAIL", width=200),
                "PASSWORD": st.column_config.TextColumn("🔑 PASS", width=130),
                "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=130),
                "SUBSCRIBE": st.column_config.TextColumn("📊 SUBS", width=50), 
                "LINK_CHANNEL": st.column_config.LinkColumn("🔗 URL", width=300),
                "PENCATAT": st.column_config.TextColumn("👤 OLEH", width=50, disabled=True),
                "STATUS": st.column_config.SelectboxColumn("⚙️ STATUS", width=80, options=["STANDBY", "PROSES", "SOLD", "BUSUK", "SUSPEND"]),
                "REAL_IDX": None 
            }

            edited_st = st.data_editor(
                df_st[["NO", "EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "PENCATAT", "STATUS", "REAL_IDX"]],
                column_config=config_st, use_container_width=True, hide_index=True, key="grid_st_pro_v2"
            )

            # --- 6. LOGIKA UPDATE MODERN (BATCH UPSERT) ---
            kolom_cek = ["NO", "EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "PENCATAT", "STATUS", "REAL_IDX"]
            if not edited_st.equals(df_st[kolom_cek]):
                if st.button("💾 KONFIRMASI PERUBAHAN", use_container_width=True, type="primary"):
                    try:
                        with st.spinner("Sinkronisasi Radar ke Supabase..."):
                            tgl_now = now_indo.strftime("%d/%m/%Y %H:%M")
                            data_batch = []
                            
                            for i, row in edited_st.iterrows():
                                idx_asli = int(row['REAL_IDX'])
                                old_val = df.iloc[idx_asli]
                                
                                # Cek jika ada perubahan status atau data lain
                                if row['STATUS'] != old_val['STATUS'] or row['EMAIL'] != old_val['EMAIL']:
                                    target_email = row['EMAIL'].strip().lower()
                                    target_hp = str(old_val['HP'])
                                    
                                    # LOGIKA AUTO-ASSIGN HP (SLOT DINAMIS)
                                    if row['STATUS'] == 'PROSES' and old_val['STATUS'] == 'STANDBY':
                                        df_p_now = df[df['STATUS'] == 'PROSES'].copy()
                                        hp_counts = df_p_now['HP'].astype(str).value_counts().to_dict()
                                        
                                        target_hp = "1"
                                        for h in range(1, 101):
                                            count_sekarang = hp_counts.get(str(h), 0)
                                            # Jatah Slot: HP 1-8 (3 Channel), Lainnya (4 Channel)
                                            max_slot = 3 if h in [1, 2, 3, 4, 5, 6, 7, 8] else 4
                                            
                                            if count_sekarang < max_slot:
                                                target_hp = str(h)
                                                break

                                    elif row['STATUS'] in ['SOLD', 'BUSUK', 'SUSPEND'] and old_val['STATUS'] == 'PROSES':
                                        target_hp = ""

                                    data_batch.append({
                                        "EMAIL": target_email,
                                        "PASSWORD": row['PASSWORD'],
                                        "NAMA_CHANNEL": row['NAMA_CHANNEL'],
                                        "SUBSCRIBE": str(row['SUBSCRIBE']),
                                        "LINK_CHANNEL": row['LINK_CHANNEL'],
                                        "STATUS": row['STATUS'],
                                        "HP": target_hp,
                                        "EDITED": f"Up: {user_aktif} ({tgl_now})"
                                    })

                            if data_batch:
                                database.supabase.table("Channel_Pintar").upsert(data_batch, on_conflict="EMAIL").execute()
                                st.success(f"✅ Mantap! {len(data_batch)} Akun Berhasil Diupdate!")
                                time.sleep(1)
                                st.rerun()
                                
                    except Exception as e:
                        st.error(f"❌ Error Global: {e}")

    # ==============================================================================
    # TAB 2: MONITORING PROSES (RADAR SYNC & SLOT HP PROTECTION v2.0)
    # ==============================================================================
    with tab_pr:
        st.markdown("#### 🚀 MONITORING PROSES")
        
        # --- INFO INSTRUKSI STAFF ---
        st.info("""
            💡 **PENGINGAT KHUSUS:**
            1. HP 1-8 Konten Sakura (Max 3 Channel)
            2. HP 9-23 Konten Masjid (Max 4 Channel)
            3. Pastikan login/hapus stock video disesuaikan.
        """)

        # Filter data yang statusnya PROSES
        df_p = df[df['STATUS'] == 'PROSES'].copy()

        if df_p.empty:
            st.info("Semua unit HP kosong (Belum ada akun di Tab Proses).")
        else:
            # --- FIX SORTING (Agar HP 1, 2... 10 urut lurus) ---
            df_p['HP_NUM'] = df_p['HP'].astype(str).str.extract('(\d+)').astype(float).fillna(999)
            df_p = df_p.sort_values(by=['HP_NUM', 'EMAIL'])

            display_list = []
            # Groupby untuk membuat tampilan "Group per HP"
            for hp_id, group in df_p.groupby('HP', sort=False):
                for i, (idx, r) in enumerate(group.iterrows()):
                    display_list.append({
                        "REAL_IDX": idx,
                        "HP": f"📱 HP {hp_id}" if i == 0 else "", 
                        "EMAIL": r['EMAIL'],
                        "PASSWORD": r['PASSWORD'],
                        "NAMA_CHANNEL": r['NAMA_CHANNEL'],
                        "SUBSCRIBE": str(r['SUBSCRIBE']),
                        "LINK_CHANNEL": r['LINK_CHANNEL'],
                        "STATUS": r['STATUS']
                    })

            df_display = pd.DataFrame(display_list)
            
            # Konfigurasi Kolom Editor
            config_p = {
                "HP": st.column_config.TextColumn("📱 UNIT", width=80, disabled=True),
                "EMAIL": st.column_config.TextColumn("📧 EMAIL", width=200, disabled=True),
                "PASSWORD": st.column_config.TextColumn("🔑 PASS", width=130, disabled=True),
                "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=150, disabled=True),
                "SUBSCRIBE": st.column_config.TextColumn("📊 SUBS", width=60), 
                "LINK_CHANNEL": st.column_config.LinkColumn("🔗 URL", width=100, disabled=True),
                "STATUS": st.column_config.SelectboxColumn(
                    "⚙️ STATUS", width=100, 
                    options=["PROSES", "SOLD", "STANDBY", "BUSUK", "SUSPEND"]
                ),
                "REAL_IDX": None 
            }

            edited_p = st.data_editor(
                df_display, 
                column_config=config_p, 
                use_container_width=True, 
                hide_index=True, 
                key="grid_p_pro_v2"
            )

            # --- LOGIKA SAVE (MURNI SUPABASE - BATCH) ---
            if not edited_p.equals(df_display):
                if st.button("💾 UPDATE STATUS MONITORING", use_container_width=True, type="primary"):
                    try:
                        with st.spinner("Sinkronisasi ke Supabase..."):
                            tgl_now = database.ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M")
                            data_batch = []
                            
                            for i, row in edited_p.iterrows():
                                idx_asli = int(row['REAL_IDX'])
                                old_val = df.iloc[idx_asli]
                                
                                # Cek perubahan Status atau Subscribe
                                if (row['STATUS'] != old_val['STATUS'] or str(row['SUBSCRIBE']) != str(old_val['SUBSCRIBE'])):
                                    target_hp = str(old_val['HP'])
                                    # Jika dilepas dari proses, kosongkan HP-nya
                                    if row['STATUS'] != 'PROSES':
                                        target_hp = "" 

                                    data_batch.append({
                                        "EMAIL": row['EMAIL'].strip().lower(),
                                        "STATUS": row['STATUS'],
                                        "SUBSCRIBE": str(row['SUBSCRIBE']),
                                        "HP": target_hp,
                                        "EDITED": f"Up: {user_aktif} ({tgl_now})"
                                    })

                            if data_batch:
                                database.supabase.table("Channel_Pintar").upsert(data_batch, on_conflict="EMAIL").execute()
                                st.success(f"✅ Berhasil! {len(data_batch)} Akun terupdate.")
                                time.sleep(1)
                                st.rerun()
                                
                    except Exception as e:
                        st.error(f"❌ Gagal update: {e}")

    # ==============================================================================
    # TAB 3: JADWAL UPLOAD (FULL MANUAL - SLOT HP VERSION v2.0)
    # ==============================================================================
    with tab_jd:
        df_j = df[df['STATUS'] == 'PROSES'].copy()

        if df_j.empty:
            st.info("Belum ada akun di Tab Proses untuk dijadwalkan.")
        else:
            now_indo = database.ambil_waktu_sekarang()
            
            # --- Map Bulan Indo ---
            nama_bulan = {
                1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni",
                7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"
            }
            tgl_str = f"{now_indo.day} {nama_bulan[now_indo.month]} {now_indo.year}"

            # --- 1. FITUR EDIT JAM (FULL SUPABASE - KENCENG SILET) ---
            with st.expander("🛠️ EDIT JAM UPLOAD (SLOT HP)", expanded=False):
                df_j['REAL_IDX'] = df_j.index
                df_j['HP_N'] = pd.to_numeric(df_j['HP'], errors='coerce').fillna(999)
                
                # Sort biar rapi per HP dan waktu
                df_j_sorted = df_j.sort_values(['HP_N', 'PAGI'])

                kolom_edit = ["HP", "NAMA_CHANNEL", "PAGI", "SIANG", "SORE", "EMAIL", "REAL_IDX"]
                
                edited_j = st.data_editor(
                    df_j_sorted[kolom_edit],
                    column_config={
                        "HP": st.column_config.TextColumn("📱 HP", width=50, disabled=True),
                        "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=250, disabled=True),
                        "PAGI": st.column_config.TextColumn("🌅 PAGI"),
                        "SIANG": st.column_config.TextColumn("☀️ SIANG"),
                        "SORE": st.column_config.TextColumn("🌆 SORE"),
                        "EMAIL": None, 
                        "REAL_IDX": None
                    },
                    use_container_width=True, hide_index=True, key="editor_manual_v2"
                )

                if st.button("💾 SIMPAN SEMUA JADWAL", use_container_width=True, type="primary"):
                    try:
                        with st.spinner("Sinkronisasi Jadwal ke Supabase..."):
                            jam_log = now_indo.strftime('%H:%M')
                            data_supabase = []

                            for _, row in edited_j.iterrows():
                                data_supabase.append({
                                    "EMAIL": row['EMAIL'].strip().lower(),
                                    "PAGI": str(row['PAGI']) if row['PAGI'] else "",
                                    "SIANG": str(row['SIANG']) if row['SIANG'] else "",
                                    "SORE": str(row['SORE']) if row['SORE'] else "",
                                    "EDITED": f"Up: {user_aktif} (Jadwal {jam_log})"
                                })

                            if data_supabase:
                                database.supabase.table("Channel_Pintar").upsert(
                                    data_supabase, on_conflict="EMAIL"
                                ).execute()

                            st.success(f"✅ Mantap! {len(data_supabase)} Jadwal Berhasil Sinkron.")
                            time.sleep(1)
                            st.rerun()
                            
                    except Exception as e:
                        st.error(f"❌ Terjadi Kesalahan: {e}")

            st.divider()

            # --- 2. LOGIKA GENERATE TABEL PRINT (TIM BREAK) ---
            df_j['HP_NUM'] = pd.to_numeric(df_j['HP'], errors='coerce').fillna(999)
            df_display = df_j.sort_values(['HP_NUM', 'PAGI'])
            
            # PISAHKAN LIST HP JADI 2 KELOMPOK (Sesuai Tim Staf Kamu)
            list_hp_tim1 = [h for h in df_display['HP'].unique() if pd.to_numeric(h, errors='coerce') <= 11]
            list_hp_tim2 = [h for h in df_display['HP'].unique() if pd.to_numeric(h, errors='coerce') > 11]
            
            kelompok_tim = [
                {"nama": "ICHA / NISSA (HP 1-11)", "list": list_hp_tim1},
                {"nama": "LISA (HP 12-23)", "list": list_hp_tim2}
            ]

            html_all_pages = "" 

            for tim in kelompok_tim:
                list_hp_unik = tim["list"]
                if not list_hp_unik: continue
                
                # Loop per 6 HP per halaman agar tidak sesak saat di-print
                for start_idx in range(0, len(list_hp_unik), 6):
                    hp_halaman_ini = list_hp_unik[start_idx : start_idx + 6]
                    df_page = df_display[df_display['HP'].isin(hp_halaman_ini)]
                    
                    html_all_pages += f"""
                    <div class="print-container page-break">
                        <div class="header-box">
                            <h2>📋 JADWAL UPLOAD PINTAR MEDIA</h2>
                            <p class="sub">Unit: <b>{tim['nama']}</b> | Periode: <b>{tgl_str}</b></p>
                        </div>
                        <table>
                            <thead>
                                <tr>
                                    <th style="width: 10%;">📱 HP</th>
                                    <th style="width: 45%;">📺 CHANNEL YOUTUBE</th>
                                    <th style="width: 15%;">🌅 PAGI</th>
                                    <th style="width: 15%;">☀️ SIANG</th>
                                    <th style="width: 15%;">🌆 SORE</th>
                                </tr>
                            </thead>
                            <tbody>
                    """
                    
                    for i, r in enumerate(df_page.itertuples()):
                        p = r.PAGI if pd.notna(r.PAGI) and str(r.PAGI).strip() != "" else "-"
                        s = r.SIANG if pd.notna(r.SIANG) and str(r.SIANG).strip() != "" else "-"
                        o = r.SORE if pd.notna(r.SORE) and str(r.SORE).strip() != "" else "-"
                        
                        # Hanya tampilkan nomor HP di baris pertama tiap unit HP
                        hp_view = str(r.HP) if i == 0 or str(r.HP) != str(df_page.iloc[i-1]['HP']) else ""
                        bg_color = "#FFFFFF" if i % 2 == 0 else "#F4F4F4"
                        
                        html_all_pages += f"""
                            <tr style="background-color: {bg_color} !important;">
                                <td class="col-hp">{hp_view}</td>
                                <td class="col-ch">{r.NAMA_CHANNEL}</td>
                                <td class="col-jam">{p}</td>
                                <td class="col-jam">{s}</td>
                                <td class="col-jam">{o}</td>
                            </tr>
                        """
                    html_all_pages += "</tbody></table></div>"

            # --- 3. MONITORING VIEW (WEB) ---
            st.markdown("#### 📱 MONITORING JADWAL UPLOAD")
            st.dataframe(
                df_display[["HP", "NAMA_CHANNEL", "PAGI", "SIANG", "SORE"]],
                column_config={
                    "HP": st.column_config.TextColumn("📱 HP", width=50),
                    "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=250),
                    "PAGI": st.column_config.TextColumn("🌅 PAGI", width=120),
                    "SIANG": st.column_config.TextColumn("☀️ SIANG", width=120),
                    "SORE": st.column_config.TextColumn("🌆 SORE", width=120),
                }, hide_index=True, use_container_width=True
            )

            # --- 4. RENDER TOMBOL PRINT ---
            html_masterpiece = f"""
            <style>
                @media print {{
                    @page {{ size: A4 portrait; margin: 1cm; }}
                    body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: white; }}
                    .print-container {{ width: 100%; margin: 0 auto; }}
                    .page-break {{ page-break-after: always; }}
                    .header-box {{ text-align: center; border-bottom: 2px solid #333; margin-bottom: 15px; padding-bottom: 5px; }}
                    h2 {{ font-size: 20px; margin: 5px 0; color: #000; }}
                    .sub {{ font-size: 12px; color: #666; }}
                    table {{ width: 100%; border-collapse: collapse; border: 1px solid #CCC; table-layout: fixed; }}
                    th {{ background-color: #FFFFFF !important; color: #1E3A8A !important; padding: 10px; border: 1px solid #CCC; font-size: 12px; font-weight: bold; -webkit-print-color-adjust: exact; }}
                    td {{ border: 1px solid #CCC; padding: 8px 10px; font-size: 14px; color: #111; }}
                    .col-hp {{ width: 10%; text-align: center; font-weight: bold; background-color: #F8F8F8 !important; }}
                    .col-jam {{ text-align: center; font-weight: bold; color: #C00 !important; }}
                }}
            </style>
            {html_all_pages}
            """
            
            if st.button("📄 PRINT JADWAL", use_container_width=True, type="primary"):
                st.components.v1.html(html_masterpiece + "<script>window.print();</script>", height=0)

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
