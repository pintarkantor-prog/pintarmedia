import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import pytz
import time
import socket
import re
import requests
from modules import database 

def tampilkan_database_channel():
    # --- 1. PROTEKSI LEVEL AKSES ---
    level_aktif = str(st.session_state.get("user_level", "STAFF")).upper().strip()
    user_aktif = st.session_state.get("user_aktif", "User").upper()
    
    if level_aktif not in ["OWNER", "ADMIN", "STAFF", "UPLOADER"]:
        st.error(f"🚫 AKSES DITOLAK, {user_aktif}!")
        st.stop() 

    # --- 2. HEADER & SETUP ---
    st.title("📱 DATABASE CHANNEL")
    if st.sidebar.button("🔄 REFRESH DATA", type="secondary"):
        st.cache_data.clear()
        st.cache_resource.clear()
        st.rerun()

    # --- 3. PENARIKAN DATA REAL-TIME ---
    df = database.ambil_data("Channel_Pintar")
    df_hp = database.ambil_data("Data_HP")
    
    if df.empty:
        st.warning("⚠️ Gagal memuat data atau tabel kosong.")
        return

    # =====================================================================
    # FIX GLOBAL: Normalisasi STATUS & HP setelah ambil data
    # Paksa strip SEMUA whitespace termasuk \t, \n, \r, spasi ganda
    # =====================================================================
    df['STATUS'] = df['STATUS'].astype(str).str.strip().str.upper()
    df['HP']     = df['HP'].astype(str).str.strip()
    # Ganti semua varian "kosong": nan, None, null, whitespace only → ''
    df['HP']     = df['HP'].replace({'nan': '', 'None': '', 'null': '', 'NULL': ''})
    df['HP']     = df['HP'].apply(lambda x: '' if str(x).strip() == '' else str(x).strip())

    # =====================================================================
    # FIX KRITIS: Definisikan nowww DI SINI (scope global fungsi),
    # bukan di dalam blok if level_aktif, agar semua tab bisa mengaksesnya
    # =====================================================================
    now_indo = database.ambil_waktu_sekarang()
    nowww = now_indo

    # --- 4. PEMBUATAN TAB ---
    tab_st, tab_pr, tab_jd, tab_hp, tab_sd, tab_ar = st.tabs([
        "📦 STOK STANDBY", "🚀 CHANNEL PROSES", "📅 JADWAL UPLOAD", 
        "📱 MONITOR HP", "💰 SOLD CHANNEL", "📂 ARSIP"
    ])

    # ==============================================================================
    # TAB 1: STOK STANDBY
    # ==============================================================================
    with tab_st:
        if level_aktif in ["OWNER", "ADMIN"]:
            # --- 1. LOGIKA HITUNG DATA ---
            total_st = len(df[df['STATUS'] == 'STANDBY'])
            total_pr = len(df[df['STATUS'] == 'PROSES'])
            df_proses = df[df['STATUS'] == 'PROSES']
            hp_aktif = len(df_proses[df_proses['HP'].notna() & (df_proses['HP'] != "")]['HP'].unique())
        
            selisih_vital = total_st - (total_pr + 10)
            status_stok = f"AMAN (+{selisih_vital})" if selisih_vital >= 0 else f"KRITIS ({selisih_vital})"
            warna_stok = "normal" if selisih_vital >= 0 else "inverse"
        
            bln_ini = nowww.strftime("%m/%Y") 
        
            mask_ini = (df['STATUS'] == 'SOLD') & (df['EDITED'].astype(str).str.contains(bln_ini, na=False))
            sold_ini = len(df[mask_ini])
        
            total_arsip = len(df[df['STATUS'].isin(['SUSPEND', 'BUSUK'])])

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

            # --- REPORT HARIAN ---
            hari_ini_filter = nowww.strftime("%d/%m/%Y")
            kemarin_filter = (nowww - timedelta(days=1)).strftime("%d/%m/%Y")
            
            df_today = df[df['TANGGAL'].astype(str).str.contains(hari_ini_filter, na=False)]
            df_yesterday = df[df['TANGGAL'].astype(str).str.contains(kemarin_filter, na=False)]
            
            total_today = len(df_today)
            selisih = total_today - len(df_yesterday)
            
            rekap_pencatat = df_today['PENCATAT'].value_counts().reset_index()
            rekap_pencatat.columns = ['NAMA', 'JUMLAH']

            with st.expander(f"📊 REKAP INPUT HARIAN", expanded=False):
                cols = st.columns(4)
                with cols[0]:
                    with st.container(border=True):
                        st.metric(label="📈 TOTAL HARI INI", value=f"{total_today}", delta=f"{selisih} vs Kemarin")
                for i in range(3):
                    with cols[i+1]:
                        if i < len(rekap_pencatat):
                            nama_staff = rekap_pencatat.iloc[i]['NAMA']
                            jml_staff = rekap_pencatat.iloc[i]['JUMLAH']
                            with st.container(border=True):
                                st.metric(label=f"👤 {nama_staff.upper()}", value=f"{jml_staff}", delta="Akun Terinput")
                        else:
                            st.write("") 

            st.markdown("<br>", unsafe_allow_html=True)
            
            hc1, hc2 = st.columns([3, 1])
            hc1.markdown("#### 🔐 DATABASE STOK STANDBY")
            
            if hc2.button("➕ TAMBAH AKUN", use_container_width=True, type="primary"):
                st.session_state.form_baru = not st.session_state.get('form_baru', False)

            if st.session_state.get('form_baru', False):
                with st.container(border=True):
                    with st.form(key=f"form_input_{len(df)}", clear_on_submit=True):
                        f1, f2, f3 = st.columns(3)
                        v_mail = f1.text_input("📧 Email Login")
                        v_pass = f2.text_input("🔑 Password")
                        v_nama = f3.text_input("📺 Nama Channel")
                        f4, f5 = st.columns([1, 2])
                        v_subs = f4.text_input("📊 Jumlah Subs")
                        v_link = f5.text_input("🔗 Link Channel")
                        
                        if st.form_submit_button("🚀 SIMPAN KE DATABASE", use_container_width=True):
                            if v_nama and v_mail:
                                tgl_now = database.ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M")
                                v_mail = v_mail.strip().lower()
                                v_nama = v_nama.strip()
                                try:
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
                                    st.cache_data.clear()
                                    st.toast(f"✅ Berhasil Masuk: {v_mail}", icon="🚀")
                                    time.sleep(1)
                                    st.rerun()
                                except Exception as e:
                                    if "23505" in str(e):
                                        st.warning(f"⚠️ Email **{v_mail}** sudah ada!")
                                    else:
                                        st.error(f"❌ Masalah: {e}")
                            else:
                                st.error("⚠️ Email dan Nama Channel wajib diisi!")
                                
            # --- 5. GRID EDITOR STANDBY ---
            df_st = df[df['STATUS'] == 'STANDBY'].copy()
            if df_st.empty:
                st.info("Belum ada stok standby.")
            else:
                df_st = df_st.sort_values(by='ID', ascending=False)
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
                    "STATUS": st.column_config.SelectboxColumn("⚙️ STATUS", width=100, options=["STANDBY", "PROSES", "SOLD", "BUSUK", "SUSPEND"]),
                    "REAL_IDX": None,
                    "ID": None
                }

                kolom_tampil = ["NO", "EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "PENCATAT", "STATUS", "REAL_IDX", "ID"]

                edited_st = st.data_editor(
                    df_st[kolom_tampil],
                    column_config=config_st, 
                    use_container_width=True, 
                    hide_index=True, 
                    key=f"grid_st_{len(df_st)}"
                )

                # --- 6. LOGIKA UPDATE ---
                if not edited_st.equals(df_st[kolom_tampil]):
                    if st.button("💾 KONFIRMASI PERUBAHAN", use_container_width=True, type="primary"):
                        try:
                            with st.spinner("Lagi nyimpen ke database, sabaar..."):
                                tgl_now = database.ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M")
                                data_batch = []
                            
                                for i, row in edited_st.iterrows():
                                    match_df = df[df['ID'] == row['ID']]
                                
                                    if not match_df.empty:
                                        old_val = match_df.iloc[0]
                                    
                                        is_changed = (
                                            str(row['STATUS']).strip().upper() != str(old_val['STATUS']).strip().upper() or 
                                            str(row['EMAIL']).strip().lower() != str(old_val['EMAIL']).strip().lower() or
                                            str(row['PASSWORD']).strip() != str(old_val['PASSWORD']).strip() or 
                                            str(row['NAMA_CHANNEL']).strip() != str(old_val['NAMA_CHANNEL']).strip() or
                                            str(row['SUBSCRIBE']).strip() != str(old_val['SUBSCRIBE']).strip()
                                        )

                                        if is_changed:
                                            target_hp = old_val.get('HP') or ''
                                        
                                            if row['STATUS'] == 'PROSES' and old_val['STATUS'] == 'STANDBY':
                                                df_p_now = df[df['STATUS'] == 'PROSES'].copy()
                                                hp_counts = df_p_now['HP'].astype(str).value_counts().to_dict()
                                                target_hp = "1"
                                                for h in range(1, 101):
                                                    count_sekarang = hp_counts.get(str(h), 0)
                                                    max_slot = 3 if h in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] else 4
                                                    if count_sekarang < max_slot:
                                                        target_hp = str(h)
                                                        break
                                            elif row['STATUS'] in ['SOLD', 'BUSUK', 'SUSPEND'] and old_val['STATUS'] == 'PROSES':
                                                target_hp = ""

                                            data_batch.append({
                                                "id": row['ID'],
                                                "EMAIL": str(row['EMAIL']).strip().lower(),
                                                "TANGGAL": row.get('TANGGAL', old_val['TANGGAL']),
                                                "PASSWORD": str(row['PASSWORD']).strip(),
                                                "NAMA_CHANNEL": str(row['NAMA_CHANNEL']).strip(),
                                                "SUBSCRIBE": str(row['SUBSCRIBE']).strip(),
                                                "LINK_CHANNEL": row['LINK_CHANNEL'],
                                                "STATUS": row['STATUS'],
                                                "HP": target_hp,
                                                "PENCATAT": row['PENCATAT'],
                                                "EDITED": f"Up: {user_aktif} ({tgl_now})"
                                            })

                                if data_batch:
                                    database.supabase.table("Channel_Pintar").upsert(data_batch, on_conflict="id").execute()
                                    st.cache_data.clear()
                                    st.success(f"✅ Mantap! {len(data_batch)} Akun Diupdate!")
                                    time.sleep(1)
                                    st.rerun()
                                else:
                                    st.info("Tidak ada perubahan spesifik yang terdeteksi.")
                                    
                        except Exception as e:
                            st.error(f"❌ Error Global: {e}")

                    st.divider() 

        else:
            st.error(f"🛡️ **AKSES TERBATAS: {level_aktif}**")
            st.write(f"Maaf **{user_aktif}**, area ini hanya untuk Admin.")

    # ==============================================================================
    # TAB 2: MONITORING PROSES
    # ==============================================================================
    with tab_pr:
        if level_aktif in ["OWNER", "ADMIN"]:
            st.markdown("#### 🚀 MONITORING PROSES")

            with st.container(border=True):
                c1, c2, c3, c4 = st.columns(4)
                with c1:
                    st.write("📱 **HP 1 - 18**")
                    st.markdown("##### :green[3 Channel] :gray[/hp]") 
                with c2:
                    st.write("🕌 **MASJID NENEK BUAH**")
                    st.markdown("##### :orange[HP 1 sampai 13]")
                with c3:
                    st.write("🕌 **MASJID KAKEK BUAH**")
                    st.markdown("##### :red[HP 14 sampai 18]")
                with c4:
                    st.write("🌸 **XXXX**")
                    st.markdown("##### :blue[HP XXXX]")

            # ================================================================
            # Filter PROSES hanya ambil baris yang HP-nya terisi & valid
            # ================================================================
            df_p = df[
                (df['STATUS'] == 'PROSES') &
                (df['HP'] != '') &
                (df['HP'] != 'nan')
            ].copy()

            if df_p.empty:
                st.info("Semua unit HP kosong (Belum ada akun di Tab Proses).")
            else:
                df_p['HP_NUM'] = pd.to_numeric(df_p['HP'], errors='coerce')
                df_p = df_p[df_p['HP_NUM'].notna()].copy()
                df_p = df_p.sort_values(by=['HP_NUM', 'ID'], ascending=[True, True])

                display_list = []
                for hp_num in sorted(df_p['HP_NUM'].unique()):
                    group = df_p[df_p['HP_NUM'] == hp_num]
                    hp_id = str(int(hp_num))
                    for i, (idx, r) in enumerate(group.iterrows()):
                        display_list.append({
                            "ID": r['ID'],
                            "HP": f"📱 HP {hp_id}" if i == 0 else "", 
                            "EMAIL": r['EMAIL'],
                            "PASSWORD": r['PASSWORD'],
                            "NAMA_CHANNEL": r['NAMA_CHANNEL'],
                            "SUBSCRIBE": str(r['SUBSCRIBE']),
                            "LINK_CHANNEL": r['LINK_CHANNEL'],
                            "STATUS": r['STATUS']
                        })

                df_display = pd.DataFrame(display_list)
            
                config_p = {
                    "ID": None,
                    "HP": st.column_config.TextColumn("📱 UNIT", width=80, disabled=True),
                    "EMAIL": st.column_config.TextColumn("📧 EMAIL", width=200), 
                    "PASSWORD": st.column_config.TextColumn("🔑 PASS", width=130), 
                    "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=150), 
                    "SUBSCRIBE": st.column_config.TextColumn("📊 SUBS", width=60), 
                    "LINK_CHANNEL": st.column_config.LinkColumn("🔗 URL", width=150), 
                    "STATUS": st.column_config.SelectboxColumn(
                        "⚙️ STATUS", width=100, 
                        options=["PROSES", "SOLD", "STANDBY", "BUSUK", "SUSPEND"]
                    )
                }

                edited_p = st.data_editor(
                    df_display, 
                    column_config=config_p, 
                    use_container_width=True, 
                    hide_index=True, 
                    key="grid_p_pro_v2"
                )

                if not edited_p.equals(df_display):
                    if st.button("💾 UPDATE DATA MONITORING", use_container_width=True, type="primary"):
                        try:
                            st.cache_data.clear() 
                            with st.spinner("Sinkronisasi ke Supabase..."):
                                tgl_now = database.ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M")
                                data_batch = []
                            
                                for i, row in edited_p.iterrows():
                                    match_df = df[df['ID'] == row['ID']]
                                    if not match_df.empty:
                                        old_val = match_df.iloc[0]
                                    
                                        is_changed = (
                                            str(row['STATUS']).strip().upper() != str(old_val['STATUS']).strip().upper() or 
                                            str(row['SUBSCRIBE']).strip() != str(old_val['SUBSCRIBE']).strip() or
                                            str(row['PASSWORD']).strip() != str(old_val['PASSWORD']).strip() or
                                            str(row['NAMA_CHANNEL']).strip() != str(old_val['NAMA_CHANNEL']).strip() or
                                            str(row['LINK_CHANNEL']).strip() != str(old_val['LINK_CHANNEL']).strip() or
                                            str(row['EMAIL']).strip().lower() != str(old_val['EMAIL']).strip().lower()
                                        )

                                        if is_changed:
                                            target_hp = old_val.get('HP') or ''
                                            if row['STATUS'] != 'PROSES':
                                                target_hp = "" 

                                            data_batch.append({
                                                "id": row['ID'],
                                                "EMAIL": row['EMAIL'].strip().lower(),
                                                "PASSWORD": row['PASSWORD'],
                                                "NAMA_CHANNEL": row['NAMA_CHANNEL'],
                                                "SUBSCRIBE": str(row['SUBSCRIBE']),
                                                "LINK_CHANNEL": row['LINK_CHANNEL'],
                                                "STATUS": row['STATUS'],
                                                "HP": target_hp,
                                                "EDITED": f"Up: {user_aktif} ({tgl_now})"
                                            })

                                if data_batch:
                                    database.supabase.table("Channel_Pintar").upsert(data_batch, on_conflict="id").execute()
                                    st.cache_data.clear() 
                                    st.success(f"✅ Mantap! {len(data_batch)} Akun terupdate.")
                                    time.sleep(1) 
                                    st.rerun()
                                else:
                                    st.info("Tidak ada perubahan data.")
                                
                        except Exception as e:
                            st.error(f"❌ Gagal update: {e}")

                    st.divider() 

        else:
            st.error(f"🛡️ **AKSES TERBATAS: {level_aktif}**")
            st.write(f"Maaf **{user_aktif}**, area ini hanya untuk Admin.")

    # ==============================================================================
    # TAB 3: JADWAL UPLOAD
    # ==============================================================================
    with tab_jd:
        df_j = df[
            (df['STATUS'] == 'PROSES') &
            (df['HP'] != '') &
            (df['HP'] != 'nan')
        ].copy()
        
        df_j['HP_N'] = pd.to_numeric(df_j['HP'], errors='coerce')
        df_j = df_j[df_j['HP_N'].notna()].copy()
        df_j_sorted = df_j.sort_values(['HP_N'], kind='mergesort').copy()

        if df_j_sorted.empty:
            st.info("Belum ada akun di Tab Proses untuk dijadwalkan.")
        else:
            nama_bulan = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
            tgl_str = f"{nowww.day} {nama_bulan[nowww.month]} {nowww.year}"
            
            list_hp_tim1 = [str(int(h)) for h in sorted(df_j_sorted['HP_N'].unique()) if 1 <= h <= 9]
            list_hp_tim2 = [str(int(h)) for h in sorted(df_j_sorted['HP_N'].unique()) if 10 <= h <= 18]
            kelompok_tim = [
                {"nama": "INGGI (HP 1-9)", "list": list_hp_tim1},
                {"nama": "HANI (HP 10-18)", "list": list_hp_tim2}
            ]

            with st.container(border=True):
                c_start, c_btn = st.columns([1, 1])
                start_time = c_start.text_input("🕒 Jam Mulai Upload", value="08:15", key="start_estafet")
                
                if c_btn.button("🚀 GENERATE JADWAL OTOMATIS", use_container_width=True, type="primary"):
                    try:
                        with st.status("Sedang membuat jadwal otomatis...", expanded=False) as status:
                            data_update = []
                            base_pagi = datetime.strptime(start_time, "%H:%M")

                            def geser_jam_silet(waktu_mulai, urutan_total):
                                target = waktu_mulai + timedelta(minutes=(urutan_total - 1) * 15)
                                menit_target = target.hour * 60 + target.minute
                                if menit_target >= (11 * 60 + 30):
                                    target = target + timedelta(minutes=60)
                                return target

                            for tim_idx in [1, 2]:
                                if tim_idx == 1:
                                    df_tim = df_j_sorted[df_j_sorted['HP_N'] <= 9].copy()
                                else:
                                    df_tim = df_j_sorted[df_j_sorted['HP_N'] >= 10].copy()
                                
                                if df_tim.empty: continue

                                # FIX: Sort by HP_N lalu ID agar urutan konsisten
                                # groupby HP_N (numerik), bukan HP (string) agar tidak salah urut
                                df_tim = df_tim.sort_values(['HP_N', 'ID'], ascending=[True, True])
                                df_tim['urutan_di_hp'] = df_tim.groupby('HP_N').cumcount() + 1

                                # Iterasi per HP, hitung jam per slot secara independen
                                counter_jam = 1
                                for hp_num in sorted(df_tim['HP_N'].unique()):
                                    group_hp = df_tim[df_tim['HP_N'] == hp_num].sort_values('ID')
                                    for _, row in group_hp.iterrows():
                                        urutan = int(row['urutan_di_hp'])
                                        jam_final = geser_jam_silet(base_pagi, counter_jam)
                                        counter_jam += 1
                                        data_update.append({
                                            "id": row['ID'],
                                            "PAGI":  jam_final.strftime("%H:%M") if urutan == 1 else "EMPTY",
                                            "SIANG": jam_final.strftime("%H:%M") if urutan == 2 else "EMPTY",
                                            "SORE":  jam_final.strftime("%H:%M") if urutan == 3 else "EMPTY",
                                            "EDITED": f"Estafet: {user_aktif}"
                                        })

                            if data_update:
                                database.supabase.table("Channel_Pintar").upsert(data_update, on_conflict="id").execute()
                                st.cache_data.clear()
                                st.rerun()
                    except Exception as e:
                        st.error(f"Error generate jadwal: {e}")

            with st.expander("🛠️ EDIT MANUAL JADWAL", expanded=False):
                kolom_edit = ["HP", "NAMA_CHANNEL", "PAGI", "SIANG", "SORE", "ID"]
                editor_key = "editor_manual_sultan_v4"

                # FIX: Simpan mapping EMPTY → "" hanya untuk tampilan editor
                # Nilai asli (EMPTY/jam) tetap disimpan di df_j_sorted untuk referensi save
                df_editor_view = df_j_sorted[kolom_edit].copy()
                df_editor_view['PAGI']  = df_editor_view['PAGI'].replace("EMPTY", "")
                df_editor_view['SIANG'] = df_editor_view['SIANG'].replace("EMPTY", "")
                df_editor_view['SORE']  = df_editor_view['SORE'].replace("EMPTY", "")

                edited_df = st.data_editor(
                    df_editor_view,
                    column_config={
                        "HP": st.column_config.TextColumn("📱 HP", disabled=True),
                        "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", disabled=True),
                        "PAGI": st.column_config.TextColumn("🌅 PAGI"),
                        "SIANG": st.column_config.TextColumn("☀️ SIANG"),
                        "SORE": st.column_config.TextColumn("🌆 SORE"),
                        "ID": None
                    },
                    use_container_width=True, hide_index=True, key=editor_key
                )
                
                if st.button("💾 SIMPAN PERUBAHAN MANUAL", use_container_width=True, type="primary"):
                    if editor_key in st.session_state:
                        edits = st.session_state[editor_key].get("edited_rows", {})
                        if edits:
                            try:
                                data_save = []
                                for row_idx, changes in edits.items():
                                    orig = df_j_sorted.iloc[int(row_idx)]

                                    # FIX: Ambil nilai dari editor_view (sudah "" bukan "EMPTY")
                                    # bukan dari orig (yang masih "EMPTY") agar tidak tertimpa
                                    orig_display = df_editor_view.iloc[int(row_idx)]
                                    p_val = changes.get("PAGI",  orig_display['PAGI'])
                                    s_val = changes.get("SIANG", orig_display['SIANG'])
                                    o_val = changes.get("SORE",  orig_display['SORE'])

                                    # Konversi None/kosong → "EMPTY", sisanya simpan apa adanya
                                    def bersihkan_jam(val):
                                        if val is None or str(val).strip() == "" or str(val).strip() == "None":
                                            return "EMPTY"
                                        return str(val).strip()

                                    data_save.append({
                                        "id": orig['ID'],
                                        "PAGI":  bersihkan_jam(p_val),
                                        "SIANG": bersihkan_jam(s_val),
                                        "SORE":  bersihkan_jam(o_val),
                                        "EDITED": f"Manual: {user_aktif}"
                                    })

                                if data_save:
                                    database.supabase.table("Channel_Pintar").upsert(data_save, on_conflict="id").execute()
                                    st.success("✅ Berhasil Simpan!")
                                    st.cache_data.clear()
                                    st.rerun()
                            except Exception as e:
                                st.error(f"Gagal simpan manual: {e}")

            st.divider()

            st.markdown("#### 📱 MONITORING JADWAL HARI INI")

            # FIX: Tampilkan semua akun PROSES (termasuk yang belum punya jadwal)
            # Akun tanpa jadwal akan tampil dengan kolom jam kosong — jangan disembunyikan
            df_monitor = df_j_sorted[["HP", "NAMA_CHANNEL", "PAGI", "SIANG", "SORE"]].copy()
            df_monitor['PAGI']  = df_monitor['PAGI'].replace({"EMPTY": "", "nan": "", "None": ""}).fillna("")
            df_monitor['SIANG'] = df_monitor['SIANG'].replace({"EMPTY": "", "nan": "", "None": ""}).fillna("")
            df_monitor['SORE']  = df_monitor['SORE'].replace({"EMPTY": "", "nan": "", "None": ""}).fillna("")

            # Tandai baris yang belum punya jadwal sama sekali
            belum_dijadwal = df_monitor[
                (df_monitor['PAGI'] == '') & 
                (df_monitor['SIANG'] == '') & 
                (df_monitor['SORE'] == '')
            ]
            if not belum_dijadwal.empty:
                st.warning(f"⚠️ **{len(belum_dijadwal)} akun belum dijadwalkan** — silakan Generate Jadwal Otomatis atau Edit Manual.")

            st.dataframe(
                df_monitor,
                column_config={
                    "HP": st.column_config.TextColumn("📱 HP", width=50),
                    "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=250),
                    "PAGI": st.column_config.TextColumn("🌅 PAGI", width=120),
                    "SIANG": st.column_config.TextColumn("☀️ SIANG", width=120),
                    "SORE": st.column_config.TextColumn("🌆 SORE", width=120),
                },
                hide_index=True, use_container_width=True
            )

            if st.button("📄 PRINT JADWAL", use_container_width=True, type="primary"):
                with st.spinner("Merakit jadwal..."):
                    df_display = df_j_sorted.copy()
                    html_all_pages = "" 
                    
                    for tim in kelompok_tim:
                        list_hp_unik = tim["list"]
                        if not list_hp_unik: continue
                        
                        for start_idx in range(0, len(list_hp_unik), 9):
                            hp_halaman_ini = list_hp_unik[start_idx : start_idx + 9]
                            df_page = df_display[df_display['HP'].isin(hp_halaman_ini)]
                            
                            html_all_pages += f"""
                            <div class="print-container page-break">
                                <div class="header-box">
                                    <h2 style="margin:0; font-size:22px;">📋 JADWAL UPLOAD PINTAR MEDIA</h2>
                                    <p class="sub" style="margin:2px 0; font-size:13px;">Unit: <b>{tim['nama']}</b> | Periode: <b>{tgl_str}</b></p>
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
                                p = r.PAGI if pd.notna(r.PAGI) and str(r.PAGI).strip() not in ["", "EMPTY"] else "-"
                                s = r.SIANG if pd.notna(r.SIANG) and str(r.SIANG).strip() not in ["", "EMPTY"] else "-"
                                o = r.SORE if pd.notna(r.SORE) and str(r.SORE).strip() not in ["", "EMPTY"] else "-"
                                hp_view = str(r.HP) if i == 0 or str(r.HP) != str(df_page.iloc[i-1]['HP']) else ""
                                bg_color = "#FFFFFF" if i % 2 == 0 else "#F4F4F4"
                                border_top = "border-top: 1px solid #000 !important;" if hp_view and i != 0 else ""
                                
                                html_all_pages += f"""
                                    <tr style="background-color: {bg_color} !important; {border_top}">
                                        <td class="col-hp">{hp_view}</td>
                                        <td class="col-ch">{r.NAMA_CHANNEL}</td>
                                        <td class="col-jam">{p}</td>
                                        <td class="col-jam">{s}</td>
                                        <td class="col-jam">{o}</td>
                                    </tr>
                                """
                            html_all_pages += "</tbody></table></div>"

                    html_masterpiece = f"""
                    <style>
                        @media print {{
                            @page {{ size: A4 portrait; margin: 0.8cm 0.8cm 0.3cm 0.8cm; }} 
                            * {{ box-sizing: border-box; }}
                            body {{ font-family: 'Segoe UI', Tahoma, sans-serif; margin: 0; padding: 0; background: white; }}
                            .print-container {{ width: 100%; max-width: 750px; margin: 0 auto; padding-top: 10px; }}
                            .page-break {{ page-break-after: always; }}
                            .header-box {{ text-align: center; border-bottom: 2px solid #333; margin-bottom: 8px; padding-bottom: 5px; }}
                            h2 {{ font-size: 20px; margin: 0; color: #000; }}
                            .sub {{ font-size: 12px; color: #666; margin: 0; }}
                            table {{ width: 100%; border-collapse: collapse; border: 1px solid #CCC; table-layout: fixed; }}
                            th {{ background-color: #FFFFFF !important; color: #1E3A8A !important; padding: 10px; border: 1px solid #CCC; font-size: 13px; font-weight: bold; -webkit-print-color-adjust: exact; }}
                            td {{ border: 1px solid #CCC; padding: 8.5px 10px; font-size: 13.5px; color: #111; line-height: 1.1; }}
                            .col-hp {{ width: 10%; text-align: center; font-weight: bold; background-color: #F8F8F8 !important; font-size: 15px; }}
                            .col-ch {{ text-align: left; font-weight: 500; padding-left: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
                            .col-jam {{ text-align: center; font-weight: bold; color: #C00 !important; }}
                        }}
                    </style>
                    {html_all_pages}
                    """
                    st.components.v1.html(html_masterpiece + "<script>window.print();</script>", height=0)
                
    # ==============================================================================
    # TAB 4: MONITOR HP
    # ==============================================================================
    with tab_hp:
        with st.expander("➕ DAFTARKAN UNIT HP BARU", expanded=False):
            with st.form("form_hp_supabase", clear_on_submit=True):
                st.markdown("### 📝 Input Data Unit")
                c1, c2 = st.columns(2)
                v_nama = c1.text_input("Nama Unit (Contoh: HP 01)").strip().upper()
                v_no = c2.text_input("Nomor HP (Contoh: 0812...)").strip()
                c3, c4 = st.columns(2)
                v_prov = c3.selectbox("Provider", ["TELKOMSEL", "XL", "AXIS", "INDOSAT", "TRI", "SMARTFREN"])
                v_tgl = c4.date_input("Masa Aktif Kartu")
                
                if st.form_submit_button("🚀 SIMPAN UNIT", use_container_width=True):
                    if v_nama and v_no:
                        try:
                            tgl_fix = v_tgl.strftime("%d/%m/%Y")
                            database.supabase.table("Data_HP").insert({
                                "NAMA_HP": v_nama,
                                "NOMOR_HP": v_no,
                                "PROVIDER": v_prov,
                                "MASA_AKTIF": tgl_fix
                            }).execute()
                            st.cache_data.clear()
                            st.success(f"✅ {v_nama} Berhasil Didaftarkan!")
                            time.sleep(1)
                            st.rerun() 
                        except Exception as e:
                            st.error(f"Error Supabase: {e}")
                    else:
                        st.error("Nama & Nomor wajib diisi!")

        st.divider()

        if df_hp.empty:
            st.info("Radar unit HP masih kosong. Silakan daftarkan unit baru.")
        else:
            now_indo_date = database.ambil_waktu_sekarang().date()
            df_hp['HP_NUM'] = df_hp['NAMA_HP'].astype(str).str.extract(r'(\d+)').astype(float).fillna(999)
            df_view = df_hp[df_hp['NAMA_HP'].str.strip() != ""].sort_values('HP_NUM').copy()
            
            grid = st.columns(4) 
            for i, (idx, r) in enumerate(df_view.iterrows()):
                id_target = r.get('id') if 'id' in r else r.get('ID')

                with grid[i % 4]:
                    try:
                        t_exp = pd.to_datetime(r['MASA_AKTIF'], dayfirst=True).date()
                        sisa = (t_exp - now_indo_date).days
                        if sisa > 5: color_code = "#2D5A47" 
                        elif 3 <= sisa <= 5: color_code = "#B8860B" 
                        else: color_code = "#962D2D" 
                    except:
                        color_code = "#444"; sisa = "?"

                    with st.container(border=True):
                        st.markdown(f'''
                            <div style="background:{color_code}; padding:5px; border-radius:5px; text-align:center; margin-bottom:12px;">
                                <b style="color:white; font-size:18px;">{r["NAMA_HP"]}</b>
                            </div>
                        ''', unsafe_allow_html=True)
                        
                        ic1, ic2 = st.columns(2)
                        ic1.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>📞 NOMOR</p><b style='font-size:14px;'>{r['NOMOR_HP']}</b>", unsafe_allow_html=True)
                        ic2.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>📡 PROVIDER</p><b style='font-size:11px;'>{r['PROVIDER']}</b>", unsafe_allow_html=True)
                        
                        st.divider()
                        sc1, sc2 = st.columns(2)
                        sc1.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>📅 EXPIRED</p><code style='font-size:11px;'>{r['MASA_AKTIF']}</code>", unsafe_allow_html=True)
                        sisa_color = "#ff4b4b" if isinstance(sisa, int) and sisa <= 2 else "#ffffff"
                        sc2.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>⏳ SISA</p><b style='font-size:14px; color:{sisa_color};'>{sisa} Hari</b>", unsafe_allow_html=True)

                        with st.popover("✏️ Edit", use_container_width=True):
                            st.markdown(f"#### 🛠️ EDIT: {r['NAMA_HP']}")
                            e_nama = st.text_input("📱 Nama Unit", value=str(r['NAMA_HP']), key=f"en_{id_target}").strip().upper()
                            e_no = st.text_input("📞 Nomor HP", value=str(r['NOMOR_HP']), key=f"eno_{id_target}").strip()
                            provider_list = ["TELKOMSEL", "XL", "AXIS", "INDOSAT", "TRI", "SMARTFREN"]
                            curr_prov = r['PROVIDER'] if r['PROVIDER'] in provider_list else "TELKOMSEL"
                            e_prov = st.selectbox("📡 Provider", provider_list, index=provider_list.index(curr_prov), key=f"ep_{id_target}")
                            e_tgl = st.text_input("📅 Exp (DD/MM/YYYY)", value=str(r['MASA_AKTIF']), key=f"et_{id_target}").strip()
                            
                            if st.button("💾 SIMPAN", key=f"btn_e_{id_target}", use_container_width=True, type="primary"):
                                if e_nama and e_no:
                                    try:
                                        database.supabase.table("Data_HP").update({
                                            "NAMA_HP": e_nama, 
                                            "NOMOR_HP": e_no, 
                                            "PROVIDER": e_prov, 
                                            "MASA_AKTIF": e_tgl
                                        }).eq("id", id_target).execute() 
                                        st.cache_data.clear()
                                        st.success(f"✅ {e_nama} Berhasil Diupdate!")
                                        time.sleep(1)
                                        st.rerun()
                                    except Exception as e:
                                        st.error(f"❌ Gagal Update: {e}")
                                else:
                                    st.error("⚠️ Nama & Nomor HP wajib diisi!")

    # ==============================================================================
    # TAB 5: SOLD CHANNEL
    # ==============================================================================
    with tab_sd: 
        if level_aktif == "OWNER":
            col_f1, col_f2 = st.columns([1, 1])
            with col_f1:
                list_bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
                sel_bln_nama = st.selectbox("📅 Pilih Bulan Audit", list(list_bulan.values()), index=nowww.month - 1, key="tab_sold_bln")
                sel_bln_code = [k for k, v in list_bulan.items() if v == sel_bln_nama][0]
            with col_f2:
                sel_thn = st.selectbox("📆 Pilih Tahun", ["2024", "2025", "2026"], index=2, key="tab_sold_thn")

            filter_periode = f"{sel_bln_code}/{sel_thn}"
            
            df_sold_all = df[df['STATUS'] == 'SOLD'].copy()
            total_ever = len(df_sold_all)
            
            mask_periode = df_sold_all['EDITED'].astype(str).str.contains(filter_periode, na=False, case=False)
            df_selected = df_sold_all[mask_periode].copy()
            total_selected = len(df_selected)
            
            try:
                date_selected = datetime.strptime(f"01/{filter_periode}", "%d/%m/%Y")
                date_prev = (date_selected - timedelta(days=1))
                filter_prev = date_prev.strftime("%m/%Y")
                total_prev = len(df_sold_all[df_sold_all['EDITED'].astype(str).str.contains(filter_prev, na=False)])
            except:
                total_prev = 0
                filter_prev = "N/A"

            with st.container(border=True):
                m1, m2, m3 = st.columns(3)
                m1.metric("💰 TOTAL SOLD (ALL TIME)", f"{total_ever}", delta="Unit Laku")
                m2.metric(f"📅 {sel_bln_nama.upper()} {sel_thn}", f"{total_selected}", delta=f"Laku Bulan Ini")
                m3.metric(f"🕒 BULAN LALU ({filter_prev})", f"{total_prev}", delta=f"{total_selected - total_prev} dari bulan lalu", delta_color="normal")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"##### 📊 DAFTAR PENJUALAN PERIODE {sel_bln_nama.upper()} {sel_thn}")

            if df_selected.empty:
                st.info(f"Belum ada data periode {filter_periode}")
            else:
                df_selected['TGL_LAST'] = df_selected['EDITED']
                df_selected = df_selected.sort_values('TGL_LAST', ascending=False)
                
                config_sold = {
                    "TGL_LAST": st.column_config.TextColumn("⏰ TGL SOLD", width=180, disabled=True),
                    "EMAIL": st.column_config.TextColumn("📧 EMAIL", width=200),
                    "PASSWORD": st.column_config.TextColumn("🔑 PASS", width=120),
                    "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=150),
                    "SUBSCRIBE": st.column_config.TextColumn("📊 SUBS", width=80),
                    "LINK_CHANNEL": st.column_config.LinkColumn("🔗 LINK", width=100),
                    "STATUS": st.column_config.SelectboxColumn("⚙️ STATUS", width=100, options=["SOLD", "STANDBY", "PROSES", "BUSUK", "SUSPEND"]),
                    "ID": None
                }

                edited_sold = st.data_editor(
                    df_selected[["TGL_LAST", "EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "STATUS", "ID"]], 
                    use_container_width=True, 
                    hide_index=True, 
                    column_config=config_sold, 
                    key=f"grid_sold_{filter_periode}"
                )

                if not edited_sold.equals(df_selected[["TGL_LAST", "EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "STATUS", "ID"]]):
                    if st.button("💾 KONFIRMASI PERUBAHAN SOLD", type="primary", use_container_width=True):
                        try:
                            with st.spinner("Sinkronisasi data penjualan..."):
                                tgl_now = database.ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M")
                                data_batch = []
                                
                                for i, row in edited_sold.iterrows():
                                    match_df = df[df['ID'] == row['ID']]
                                    if not match_df.empty:
                                        old_val = match_df.iloc[0]
                                        
                                        is_changed = (
                                            str(row['STATUS']).strip().upper() != str(old_val['STATUS']).strip().upper() or 
                                            str(row['EMAIL']).strip().lower() != str(old_val['EMAIL']).strip().lower() or
                                            str(row['PASSWORD']).strip() != str(old_val['PASSWORD']).strip() or
                                            str(row['NAMA_CHANNEL']).strip() != str(old_val['NAMA_CHANNEL']).strip() or
                                            str(row['SUBSCRIBE']).strip() != str(old_val['SUBSCRIBE']).strip()
                                        )

                                        if is_changed:
                                            data_batch.append({
                                                "id": row['ID'],
                                                "EMAIL": row['EMAIL'].strip().lower(),
                                                "PASSWORD": row['PASSWORD'],
                                                "NAMA_CHANNEL": row['NAMA_CHANNEL'],
                                                "SUBSCRIBE": str(row['SUBSCRIBE']),
                                                "LINK_CHANNEL": row['LINK_CHANNEL'],
                                                "STATUS": row['STATUS'],
                                                "EDITED": f"Audit: {user_aktif} ({tgl_now})"
                                            })

                                if data_batch:
                                    database.supabase.table("Channel_Pintar").upsert(data_batch, on_conflict="id").execute()
                                    st.cache_data.clear()
                                    st.success(f"✅ Mantap Bos! {len(data_batch)} Akun SOLD Diperbarui!")
                                    time.sleep(1)
                                    st.rerun()
                                else:
                                    st.info("Tidak ada perubahan data.")

                        except Exception as e:
                            st.error(f"❌ Gagal Simpan Audit: {e}")

                    st.divider() 

        else:
            st.error(f"🛡️ **AKSES TERBATAS: {level_aktif}**")
            st.write(f"Maaf **{user_aktif}**, area ini hanya untuk Owner.")

    # ==============================================================================
    # TAB 6: ARSIP CHANNEL
    # ==============================================================================
    with tab_ar:
        if level_aktif in ["OWNER", "ADMIN"]:
            df_a = df[df['STATUS'].isin(['BUSUK', 'SUSPEND'])].copy()
        
            total_arsip = len(df_a)
            total_busuk = len(df_a[df_a['STATUS'] == 'BUSUK'])
            total_suspend = len(df_a[df_a['STATUS'] == 'SUSPEND'])

            with st.container(border=True):
                ca1, ca2, ca3 = st.columns(3)
                ca1.metric("💀 TOTAL ARSIP", f"{total_arsip}", delta="Akun Rusak", delta_color="inverse")
                ca2.metric("📉 TOTAL BUSUK", f"{total_busuk}", delta="Teknis/Kartu", delta_color="inverse")
                ca3.metric("🚫 TOTAL SUSPEND", f"{total_suspend}", delta="Banned YT", delta_color="inverse")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("##### 📂 DAFTAR AKUN ARSIP")

            if df_a.empty:
                st.success("✨ Arsip masih kosong!")
            else:
                df_a = df_a.sort_values(by='ID', ascending=False)
                df_a['TGL_KEJADIAN'] = df_a['EDITED']
            
                config_arsip = {
                    "ID": None,
                    "TGL_KEJADIAN": st.column_config.TextColumn("⏰ TGL KEJADIAN", width=180, disabled=True),
                    "EMAIL": st.column_config.TextColumn("📧 EMAIL", width=200), 
                    "PASSWORD": st.column_config.TextColumn("🔑 PASS", width=120), 
                    "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=150), 
                    "SUBSCRIBE": st.column_config.TextColumn("📊 SUBS", width=80), 
                    "LINK_CHANNEL": st.column_config.LinkColumn("🔗 LINK", width=100), 
                    "STATUS": st.column_config.SelectboxColumn(
                        "⚙️ STATUS", width=100,
                        options=["STANDBY", "PROSES", "SOLD", "BUSUK", "SUSPEND"],
                        help="Ubah ke STANDBY jika ingin mendaur ulang akun ini."
                    )
                }
            
                kolom_tampil_a = ["TGL_KEJADIAN", "EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "STATUS", "ID"]

                edited_a = st.data_editor(
                    df_a[kolom_tampil_a], 
                    use_container_width=True, 
                    hide_index=True, 
                    column_config=config_arsip, 
                    key="grid_arsip_daur_ulang_v4"
                )
                
                if not edited_a.equals(df_a[kolom_tampil_a]):
                    if st.button("💾 KONFIRMASI PERUBAHAN ARSIP", type="primary", use_container_width=True):
                        try:
                            with st.spinner("Sinkronisasi data..."):
                                tgl_now = database.ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M")
                                data_batch = []
                            
                                for i, row in edited_a.iterrows():
                                    match_df = df[df['ID'] == row['ID']]
                                
                                    if not match_df.empty:
                                        old_val = match_df.iloc[0]
                                    
                                        is_changed = (
                                            str(row['STATUS']).strip().upper() != str(old_val['STATUS']).strip().upper() or 
                                            str(row['EMAIL']).strip().lower() != str(old_val['EMAIL']).strip().lower() or
                                            str(row['PASSWORD']).strip() != str(old_val['PASSWORD']).strip() or 
                                            str(row['NAMA_CHANNEL']).strip() != str(old_val['NAMA_CHANNEL']).strip() or
                                            str(row['SUBSCRIBE']).strip() != str(old_val['SUBSCRIBE']).strip()
                                        )

                                        if is_changed:
                                            data_batch.append({
                                                "id": row['ID'],
                                                "EMAIL": row['EMAIL'].strip().lower(),
                                                "PASSWORD": row['PASSWORD'],
                                                "NAMA_CHANNEL": row['NAMA_CHANNEL'],
                                                "SUBSCRIBE": str(row['SUBSCRIBE']),
                                                "LINK_CHANNEL": row['LINK_CHANNEL'],
                                                "STATUS": row['STATUS'],
                                                "HP": None,
                                                "EDITED": f"Recycle: {user_aktif} ({tgl_now})"
                                            })

                                if data_batch:
                                    database.supabase.table("Channel_Pintar").upsert(data_batch, on_conflict="id").execute()
                                    st.cache_data.clear()
                                    st.success(f"✅ Mantap! {len(data_batch)} Akun Arsip Diperbarui!")
                                    time.sleep(1)
                                    st.rerun()
                                
                        except Exception as e:
                            st.error(f"❌ Gagal Diperbarui: {e}")

                    st.divider() 

        else:
            st.error(f"🛡️ **AKSES TERBATAS: {level_aktif}**")
            st.write(f"Maaf **{user_aktif}**, area ini hanya untuk Admin.")
