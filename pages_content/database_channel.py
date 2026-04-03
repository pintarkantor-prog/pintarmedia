import streamlit as st
import pandas as pd
from datetime import datetime, timedelta # Tambahin timedelta buat cutoff waktu kalau perlu
import pytz
import time
import socket
import re        # <--- WAJIB (Buat fungsi clean_angka)
import requests  # <--- WAJIB (Buat nembak API OTPNUM)
from modules import database 

# Tambahin ini juga biar gak muncul warning SSL merah-merah di terminal
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- FUNGSI OTP HUB (COPY DARI OTP_HUB.PY) ---
def clean_angka(data):
    try:
        if data is None: return 0
        angka_bersih = re.sub(r'[^\d.]', '', str(data))
        if not angka_bersih: return 0
        return int(float(angka_bersih))
    except: return 0

def get_otpnum_api(server_url, endpoint, params):
    try:
        if not server_url: return None
        base = server_url if server_url.endswith("/") else f"{server_url}/"
        full_url = f"{base}{endpoint}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        
        # Gue naikin timeout jadi 25 biar gak gampang baper (timeout)
        response = requests.get(full_url, params=params, timeout=25, headers=headers, verify=False)
        
        if response.status_code == 200: 
            return response.json()
        
        return {"success": False, "message": "SERVER LAGI ERROR / UNDER MAINTENANCE!"}
        
    except Exception: 
        # DI SINI KUNCINYA, COK! 
        # Kita abaikan pesan 'str(e)' yang ribet itu, ganti pake teks sultan:
        return {"success": False, "message": "SERVER LAGI LEMOT / TIMEOUT!"}

def tampilkan_database_channel():
    # --- 1. PROTEKSI LEVEL AKSES (Udah Mantap!) ---
    level_aktif = str(st.session_state.get("user_level", "STAFF")).upper().strip()
    user_aktif = st.session_state.get("user_aktif", "User").upper()
    
    if level_aktif not in ["OWNER", "ADMIN", "STAFF", "UPLOADER"]:
        st.error(f"🚫 AKSES DITOLAK, {user_aktif}!")
        st.stop() 

    # --- 2. HEADER & SETUP ---
    st.title("📱 DATABASE CHANNEL")

    # --- 3. PENARIKAN DATA REAL-TIME (VERSI SENYAP - ANTI KEDIP) ---
    # Kita hapus spinner-nya, biar narik data di balik layar aja
    df = database.ambil_data("Channel_Pintar")
    df_hp = database.ambil_data("Data_HP")
    
    if df.empty:
        st.warning("⚠️ Gagal memuat data atau tabel kosong.")
        return

    # --- 4. PEMBUATAN TAB ---
    tab_st, tab_pr, tab_jd, tab_hp, tab_sd, tab_ar, tab_buy = st.tabs([
        "📦 STOK STANDBY", "🚀 CHANNEL PROSES", "📅 JADWAL UPLOAD", 
        "📱 MONITOR HP", "💰 SOLD CHANNEL", "📂 ARSIP", "🛒 BELI NOMOR OTP"
    ])

    # ==============================================================================
    # TAB 1: STOK STANDBY (GAYA RADAR UI v2.0 - FULL SUPABASE)
    # ==============================================================================
    with tab_st: # Sesuaikan nama variabel tab di atas
        if level_aktif in ["OWNER", "ADMIN", "STAFF"]:
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

            # --- 2. RENDER DASHBOARD UI (BALIK KE GAYA st.write) ---
            with st.container(border=True):
                c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1.2, 2.2])
                c1.metric("📦 CH STANDBY", f"{total_st}", delta=status_stok, delta_color=warna_stok)
                c2.metric("🚀 CH PROSES", f"{total_pr}", delta="ON PROCESS")
                c3.metric("📱 UNIT HP", f"{hp_aktif}", delta="LIVE")
                c4.metric("💰 SOLD (BLN)", f"{sold_ini}", delta="Bulan Ini")
                
                # INI YANG LO MAU: Pake gaya st.write di Kolom 5
                with c5:
                    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
                    st.write(f"📢 **INFO SISTEM:**")
                    st.write(f"Terdapat **{total_arsip}** akun di arsip (Suspend/Busuk).")
            # ==============================================================================
            # RENDER DASHBOARD UI: GAYA METRIC TOTAL & STAFF (CLEAN)
            # ==============================================================================
            
            # --- 1. Persiapan Data ---
            nowww = database.ambil_waktu_sekarang()
            hari_ini_filter = nowww.strftime("%d/%m/%Y")
            from datetime import timedelta
            kemarin_filter = (nowww - timedelta(days=1)).strftime("%d/%m/%Y")
            
            df_today = df[df['TANGGAL'].astype(str).str.contains(hari_ini_filter, na=False)]
            df_yesterday = df[df['TANGGAL'].astype(str).str.contains(kemarin_filter, na=False)]
            
            total_today = len(df_today)
            selisih = total_today - len(df_yesterday)
            
            # Rekap Staff Hari Ini
            rekap_pencatat = df_today['PENCATAT'].value_counts().reset_index()
            rekap_pencatat.columns = ['NAMA', 'JUMLAH']

            # --- 2. Render UI (Satu Baris Lurus) ---
            with st.container(border=True):
                # Kita pake 6 kolom biar pas (1 Total + 5 Space Staff)
                cols = st.columns([1.2, 1, 1, 1, 1, 1])
                
                # KOLOM 1: TOTAL INPUT HARI INI
                cols[0].metric(
                    label="📈 TOTAL HARI INI", 
                    value=f"{total_today}", 
                    delta=f"{selisih} vs Kemarin"
                )
                
                # KOLOM 2 s/d 6: NAMA STAFF & INPUTNYA
                # Looping otomatis sesuai jumlah staff yang input hari ini
                for i in range(len(rekap_pencatat)):
                    if i < 5: # Batasin maksimal 5 staff biar gak overflow ke samping
                        nama_staff = rekap_pencatat.iloc[i]['NAMA']
                        jml_staff = rekap_pencatat.iloc[i]['JUMLAH']
                        
                        # Render langsung: Nama Staff sebagai Label, Jumlah sebagai Value
                        cols[i+1].metric(
                            label=f"👤 {nama_staff.upper()}", 
                            value=f"{jml_staff}",
                            delta="Akun"
                        )

            st.markdown("<br>", unsafe_allow_html=True)
            
            # --- 3. HEADER DATABASE & TOMBOL TAMBAH ---
            hc1, hc2 = st.columns([3, 1])
            hc1.markdown("#### 🔐 DATABASE STOK STANDBY")
            
            if hc2.button("➕ TAMBAH AKUN", use_container_width=True, type="primary"):
                st.session_state.form_baru = not st.session_state.get('form_baru', False)

            # --- 4. FORM INPUT AKUN BARU (GAYA LAMA - NOTIF TOAST) ---
            if st.session_state.get('form_baru', False):
                with st.container(border=True):
                    # Gue kasih key dinamis biar gak error "Duplicate Form" lagi
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
                # Penomoran visual
                df_st['NO'] = range(1, len(df_st) + 1)
                # REAL_IDX tetep ada buat navigasi visual lo
                df_st['REAL_IDX'] = df_st.index 
                df_st['SUBSCRIBE'] = df_st['SUBSCRIBE'].astype(str)

                # Konfigurasi Kolom
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
                    "ID": None # SEMBUNYIKAN ID ASLI (Kunci Supabase)
                }

                # Ambil kolom ID juga (Hasil .upper() dari database.py)
                kolom_tampil = ["NO", "EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "PENCATAT", "STATUS", "REAL_IDX", "ID"]

                edited_st = st.data_editor(
                    df_st[kolom_tampil],
                    column_config=config_st, 
                    use_container_width=True, 
                    hide_index=True, 
                    key=f"grid_st_{len(df_st)}" # Biar gak ngebayang datanya
                )

            # --- 6. LOGIKA UPDATE MODERN (BATCH VERSION - ID ANCHOR) ---
            # Cek apakah ada perubahan di data editor dibanding df_st
            if not edited_st.equals(df_st[kolom_tampil]):
                if st.button("💾 KONFIRMASI PERUBAHAN", use_container_width=True, type="primary"):
                    try:
                        with st.spinner("Lagi nyimpen ke database, sabaar..."):
                            tgl_now = database.ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M")
                            data_batch = []
                        
                            for i, row in edited_st.iterrows():
                                # Cari baris asli di master DF pake ID (Bukan REAL_IDX atau EMAIL)
                                match_df = df[df['ID'] == row['ID']]
                            
                                if not match_df.empty:
                                    old_val = match_df.iloc[0]
                                
                                    # FILTER PERUBAHAN: Cek data murni
                                    is_changed = (
                                        str(row['STATUS']).strip() != str(old_val['STATUS']).strip() or 
                                        str(row['EMAIL']).strip().lower() != str(old_val['EMAIL']).strip().lower() or
                                        str(row['PASSWORD']).strip() != str(old_val['PASSWORD']).strip() or 
                                        str(row['NAMA_CHANNEL']).strip() != str(old_val['NAMA_CHANNEL']).strip() or
                                        str(row['SUBSCRIBE']).strip() != str(old_val['SUBSCRIBE']).strip()
                                    )

                                    if is_changed:
                                        target_hp = str(old_val.get('HP', ''))
                                    
                                        # Logika Auto-Slot lo tetep jalan
                                        if row['STATUS'] == 'PROSES' and old_val['STATUS'] == 'STANDBY':
                                            df_p_now = df[df['STATUS'] == 'PROSES'].copy()
                                            hp_counts = df_p_now['HP'].astype(str).value_counts().to_dict()
                                        
                                            # Scan HP Kosong
                                            target_hp = "1"
                                            for h in range(1, 101):
                                                count_sekarang = hp_counts.get(str(h), 0)
                                                max_slot = 3 if h in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] else 4
                                                if count_sekarang < max_slot:
                                                    target_hp = str(h)
                                                    break
                                        elif row['STATUS'] in ['SOLD', 'BUSUK', 'SUSPEND'] and old_val['STATUS'] == 'PROSES':
                                            target_hp = ""

                                        # Masukkan ke keranjang batch
                                        data_batch.append({
                                            "id": row['ID'], # KUNCI UTAMA (Gunakan huruf kecil 'id' sesuai Supabase)
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
                                # UPSERT PAKE on_conflict="id" (Anti-Duplikat!)
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
            # --- TAMPILAN SINGKAT & PADAT ---
            st.error(f"🛡️ **AKSES TERBATAS: {level_aktif}**")
            st.write(f"Maaf **{user_aktif}**, area ini hanya untuk Admin.")
    # ==============================================================================
    # TAB 2: MONITORING PROSES (GAYA COMMAND CENTER)
    # ==============================================================================
    with tab_pr:
        if level_aktif in ["OWNER", "ADMIN"]:
            st.markdown("#### 🚀 MONITORING PROSES")

            # --- 1. DASHBOARD INFO UNIT (MODEL 4 KOLOM PROPORTIONAL) ---
            with st.container(border=True):
                c1, c2, c3, c4 = st.columns(4)
            
                with c1:
                    st.write("📱 **HP 1 - 3**")
                    st.markdown("##### 3 Channel") # Pake H5 biar pas ukurannya

                with c2:
                    st.write("📱 **HP 4 - 23**")
                    st.markdown("##### 3 Channel")

                with c3:
                    st.write("🌸 **SAKURA**")
                    st.markdown("##### HP 1 - 3")

                with c4:
                    st.write("🕌 **MASJID AI**")
                    st.markdown("##### HP 4 - 23")

            # Filter data PROSES
            df_p = df[df['STATUS'] == 'PROSES'].copy()

            if df_p.empty:
                st.info("Semua unit HP kosong (Belum ada akun di Tab Proses).")
            else:
                # Sorting HP biar rapi (1, 2, 3...)
                df_p['HP_NUM'] = df_p['HP'].astype(str).str.extract('(\d+)').astype(float).fillna(999)
                df_p = df_p.sort_values(by=['HP_NUM', 'EMAIL'])

                display_list = []
                for hp_id, group in df_p.groupby('HP', sort=False):
                    for i, (idx, r) in enumerate(group.iterrows()):
                        display_list.append({
                            "ID": r['ID'], # <--- AMBIL ID ASLI DATABASE
                            "HP": f"📱 HP {hp_id}" if i == 0 else "", 
                            "EMAIL": r['EMAIL'],
                            "PASSWORD": r['PASSWORD'],
                            "NAMA_CHANNEL": r['NAMA_CHANNEL'],
                            "SUBSCRIBE": str(r['SUBSCRIBE']),
                            "LINK_CHANNEL": r['LINK_CHANNEL'],
                            "STATUS": r['STATUS']
                        })

                df_display = pd.DataFrame(display_list)
            
                # --- CONFIG: SEMUA GEMBOK DIBUKA ---
                config_p = {
                    "ID": None, # Sembunyiin KTP asli
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

                # --- LOGIKA SAVE (PAKE ID SEBAGAI JANGKAR) ---
                if not edited_p.equals(df_display):
                    if st.button("💾 UPDATE DATA MONITORING", use_container_width=True, type="primary"):
                        try:
                            st.cache_data.clear() 

                            with st.spinner("Sinkronisasi ke Supabase..."):
                                tgl_now = database.ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M")
                                data_batch = []
                            
                                for i, row in edited_p.iterrows():
                                    # Cari data lama pake ID (Bukan Index!)
                                    match_df = df[df['ID'] == row['ID']]
                                    if not match_df.empty:
                                        old_val = match_df.iloc[0]
                                    
                                        # Cek perubahan murni
                                        is_changed = (
                                            str(row['STATUS']) != str(old_val['STATUS']) or 
                                            str(row['SUBSCRIBE']) != str(old_val['SUBSCRIBE']) or
                                            str(row['PASSWORD']) != str(old_val['PASSWORD']) or
                                            str(row['NAMA_CHANNEL']) != str(old_val['NAMA_CHANNEL']) or
                                            str(row['LINK_CHANNEL']) != str(old_val['LINK_CHANNEL']) or
                                            str(row['EMAIL']).strip().lower() != str(old_val['EMAIL']).strip().lower()
                                        )

                                        if is_changed:
                                            # HP dilepas kalau status bukan PROSES
                                            target_hp = str(old_val['HP'])
                                            if row['STATUS'] != 'PROSES':
                                                target_hp = "" 

                                            data_batch.append({
                                                "id": row['ID'], # <--- JANGKAR UTAMA
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
                                    # UPSERT PAKE on_conflict="id"
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
            # --- TAMPILAN SINGKAT & PADAT ---
            st.error(f"🛡️ **AKSES TERBATAS: {level_aktif}**")
            st.write(f"Maaf **{user_aktif}**, area ini hanya untuk Admin.")

    # ==============================================================================
    # TAB 3: JADWAL UPLOAD (FULL ESTAFET SULTAN v4.0 - ANTI-NUMPUK & PARALLEL)
    # ==============================================================================
    with tab_jd:
        df_j = df[df['STATUS'] == 'PROSES'].copy()
        
        df_j_kocok = df_j.sample(frac=1).reset_index(drop=True)
        df_j_kocok['HP_N'] = pd.to_numeric(df_j_kocok['HP'], errors='coerce').fillna(999)
        df_j_sorted = df_j_kocok.sort_values(['HP_N'], kind='mergesort').copy()

        if df_j_sorted.empty:
            st.info("Belum ada akun di Tab Proses untuk dijadwalkan.")
        else:
            now_indo = database.ambil_waktu_sekarang()
            nama_bulan = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
            tgl_str = f"{now_indo.day} {nama_bulan[now_indo.month]} {now_indo.year}"
            
            # --- DEFINISI KELOMPOK TIM ---
            list_hp_tim1 = [str(int(h)) for h in sorted(df_j_sorted['HP_N'].unique()) if 1 <= h <= 11]
            list_hp_tim2 = [str(int(h)) for h in sorted(df_j_sorted['HP_N'].unique()) if 12 <= h <= 23]
            kelompok_tim = [
                {"nama": "INGGI (HP 1-11)", "list": list_hp_tim1},
                {"nama": "LISA (HP 12-23)", "list": list_hp_tim2}
            ]

            # --- A. GENERATOR JADWAL (AUTO-ESTAFET SILET) ---
            with st.container(border=True):
                c_start, c_btn = st.columns([1, 1])
                start_time = c_start.text_input("🕒 Jam Mulai Upload", value="08:15", key="start_estafet")
                
                if c_btn.button("🚀 GENERATE JADWAL OTOMATIS", use_container_width=True, type="primary"):
                    try:
                        from datetime import datetime, timedelta
                        with st.status("Sedang membuat jadwal otomatis...", expanded=False) as status:
                            data_update = []
                            base_pagi = datetime.strptime(start_time, "%H:%M")

                            def geser_jam_silet(waktu_mulai, urutan_total):
                                # 1. Itung jam asli berdasarkan antrean (10 mnt per akun)
                                target = waktu_mulai + timedelta(minutes=(urutan_total - 1) * 10)
                                
                                # 2. Cek apakah jam target masuk/melewati batas awal istirahat (11:30)
                                # 11:30 itu sama dengan 690 menit dari jam 00:00
                                menit_target = target.hour * 60 + target.minute
                                
                                if menit_target >= (11 * 60 + 30):
                                    # Kalo kena istirahat, kita lempar ke 12:40.
                                    # Selisih dari 11:30 ke 12:40 adalah 70 menit.
                                    target = target + timedelta(minutes=70)
                                    
                                return target

                            # Kita proses per Tim (Tim 1: HP 1-11, Tim 2: HP 12-23)
                            for tim_idx in [1, 2]:
                                if tim_idx == 1:
                                    df_tim = df_j_sorted[df_j_sorted['HP_N'] <= 11].copy()
                                else:
                                    df_tim = df_j_sorted[df_j_sorted['HP_N'] >= 12].copy()
                                
                                if df_tim.empty: continue

                                # --- LOGIKA ROUND ROBIN DIAN ---
                                # 1. Kelompokkan akun berdasarkan 'urutan ke-berapa' di tiap HP
                                # Kloter 1: Semua akun pertama di tiap HP
                                # Kloter 2: Semua akun kedua di tiap HP, dst.
                                df_tim['urutan_di_hp'] = df_tim.groupby('HP').cumcount() + 1
                                
                                # 2. Urutkan berdasarkan Kloter dulu (1, 2, 3), baru nomor HP
                                df_resorted = df_tim.sort_values(['urutan_di_hp', 'HP_N'])
                                
                                # 3. Kasih jam estafet berurutan
                                for i, (idx_row, row) in enumerate(df_resorted.iterrows(), 1):
                                    jam_final = geser_jam_silet(base_pagi, i)
                                    
                                    # Simpan ke kolom sesuai kloternya
                                    data_update.append({
                                        "id": row['ID'],
                                        "PAGI": jam_final.strftime("%H:%M") if row['urutan_di_hp'] == 1 else "",
                                        "SIANG": jam_final.strftime("%H:%M") if row['urutan_di_hp'] == 2 else "",
                                        "SORE": jam_final.strftime("%H:%M") if row['urutan_di_hp'] == 3 else "",
                                        "EDITED": f"Round-Robin: {user_aktif}"
                                    })

                            if data_update:
                                database.supabase.table("Channel_Pintar").upsert(data_update, on_conflict="id").execute()
                                st.cache_data.clear()
                                st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")

            # --- B. EDIT MANUAL JADWAL ---
            with st.expander("🛠️ EDIT MANUAL JADWAL", expanded=False):
                kolom_edit = ["HP", "NAMA_CHANNEL", "PAGI", "SIANG", "SORE", "ID"]
                edited_j = st.data_editor(
                    df_j_sorted[kolom_edit],
                    column_config={
                        "HP": st.column_config.TextColumn("📱 HP", width=50, disabled=True),
                        "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=250, disabled=True),
                        "PAGI": st.column_config.TextColumn("🌅 PAGI"),
                        "SIANG": st.column_config.TextColumn("☀️ SIANG"),
                        "SORE": st.column_config.TextColumn("🌆 SORE"),
                        "ID": None
                    },
                    use_container_width=True, hide_index=True, key="editor_v4_final"
                )
                if st.button("💾 SIMPAN PERUBAHAN MANUAL", use_container_width=True):
                    try:
                        data_save = [{"id": r['ID'], "PAGI": r['PAGI'], "SIANG": r['SIANG'], "SORE": r['SORE']} for _, r in edited_j.iterrows()]
                        database.supabase.table("Channel_Pintar").upsert(data_save, on_conflict="id").execute()
                        st.cache_data.clear(); st.rerun()
                    except Exception as e: st.error(f"Gagal simpan: {e}")

            st.divider()

            # --- 3. MONITORING VIEW ---
            st.markdown("#### 📱 MONITORING JADWAL HARI INI")
            st.dataframe(
                df_j_sorted[["HP", "NAMA_CHANNEL", "PAGI", "SIANG", "SORE"]], 
                column_config={
                    "HP": st.column_config.TextColumn("📱 HP", width=50),
                    "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=250),
                    "PAGI": st.column_config.TextColumn("🌅 PAGI", width=120),
                    "SIANG": st.column_config.TextColumn("☀️ SIANG", width=120),
                    "SORE": st.column_config.TextColumn("🌆 SORE", width=120),
                },
                hide_index=True, use_container_width=True
            )

            # --- 4. LOGIKA PRINT (1000000% STYLE ASLI DIAN) ---
            if st.button("📄 PRINT JADWAL", use_container_width=True, type="primary"):
                with st.spinner("Merakit jadwal..."):
                    # Pastikan data print terurut HP
                    df_display = df_j_sorted.copy()
                    html_all_pages = "" 
                    for tim in kelompok_tim:
                        list_hp_unik = tim["list"]
                        if not list_hp_unik: continue
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

                    html_masterpiece = f"""
                    <style>
                        @media print {{
                            @page {{ size: A4 portrait; margin: 1cm; }}
                            * {{ box-sizing: border-box; }}
                            body {{ font-family: 'Segoe UI', Tahoma, sans-serif; margin: 0; padding: 0; background: white; }}
                            .print-container {{ width: 100%; max-width: 690px; margin: 0 auto; }}
                            .page-break {{ page-break-after: always; }}
                            .header-box {{ text-align: center; border-bottom: 2px solid #333; margin-bottom: 15px; padding-bottom: 5px; }}
                            h2 {{ font-size: 20px; margin: 5px 0; color: #000; }}
                            .sub {{ font-size: 12px; color: #666; }}
                            table {{ width: 100%; border-collapse: collapse; border: 1px solid #CCC; table-layout: fixed; }}
                            th {{ background-color: #FFFFFF !important; color: #1E3A8A !important; padding: 10px; border: 1px solid #CCC; font-size: 12px; font-weight: bold; -webkit-print-color-adjust: exact; }}
                            td {{ border: 1px solid #CCC; padding: 8px 10px; font-size: 14px; color: #111; line-height: 1.3; }}
                            .col-hp {{ width: 10%; text-align: center; font-weight: bold; background-color: #F8F8F8 !important; }}
                            .col-ch {{ text-align: left; font-weight: 500; padding-left: 12px; }}
                            .col-jam {{ text-align: center; font-weight: bold; color: #C00 !important; }}
                        }}
                    </style>
                    {html_all_pages}
                    """
                    st.components.v1.html(html_masterpiece + "<script>window.print();</script>", height=0)
                
    # ======================================================================
    # --- TAB 4: MONITOR HP (ANTI-CRASH & SUPABASE SYNC v2.0) ---
    # ======================================================================
    with tab_hp:
        # --- 1. EXPANDER INPUT UNIT BARU ---
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

        # --- 2. DISPLAY RADAR CARD ---
        if df_hp.empty:
            st.info("Radar unit HP masih kosong. Silakan daftarkan unit baru.")
        else:
            now_indo = database.ambil_waktu_sekarang().date()
            
            # --- FIX URUTAN HP ---
            df_hp['HP_NUM'] = df_hp['NAMA_HP'].astype(str).str.extract('(\d+)').astype(float).fillna(999)
            df_view = df_hp[df_hp['NAMA_HP'].str.strip() != ""].sort_values('HP_NUM').copy()
            
            # Tampilan Grid 4 Kolom
            grid = st.columns(4) 
            for i, (idx, r) in enumerate(df_view.iterrows()):
                # Ambil ID unik database sebagai jangkar utama
                id_target = r.get('id') if 'id' in r else r.get('ID')

                with grid[i % 4]:
                    try:
                        t_exp = pd.to_datetime(r['MASA_AKTIF'], dayfirst=True).date()
                        sisa = (t_exp - now_indo).days
                        
                        if sisa > 10: color_code = "#2D5A47" 
                        elif 4 <= sisa <= 10: color_code = "#B8860B" 
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
                        
                        sisa_color = "#ff4b4b" if isinstance(sisa, int) and sisa < 4 else "#ffffff"
                        sc2.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>⏳ SISA</p><b style='font-size:14px; color:{sisa_color};'>{sisa} Hari</b>", unsafe_allow_html=True)

                        # --- FITUR EDIT (Pake id_target biar gak salah alamat) ---
                        with st.popover("✏️ Edit", use_container_width=True):
                            st.markdown(f"#### 🛠️ EDIT: {r['NAMA_HP']}")
                            
                            # KUNCI UTAMA: Key harus pake ID Unik Database, bukan index dataframe!
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
    # TAB 5: SOLD CHANNEL (SINKRON SUPABASE - FULL EDITABLE v2.0)
    # ==============================================================================
    with tab_sd: 
        # --- PROTEKSI AKSES OWNER ---
        if level_aktif == "OWNER":

            # --- 1. SETUP FILTER PERIODE ---
            now_indo = database.ambil_waktu_sekarang()
            col_f1, col_f2 = st.columns([1, 1])
            with col_f1:
                list_bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
                sel_bln_nama = st.selectbox("📅 Pilih Bulan Audit", list(list_bulan.values()), index=now_indo.month - 1, key="tab_sold_bln")
                sel_bln_code = [k for k, v in list_bulan.items() if v == sel_bln_nama][0]
            with col_f2:
                sel_thn = st.selectbox("📆 Pilih Tahun", ["2024", "2025", "2026"], index=2, key="tab_sold_thn")

            filter_periode = f"{sel_bln_code}/{sel_thn}"
            
            # --- 2. LOGIKA HITUNG DATA (SUPABASE DATA) ---
            df_sold_all = df[df['STATUS'] == 'SOLD'].copy()
            total_ever = len(df_sold_all)
            
            # Filter berdasarkan kolom EDITED (jejak digital transaksi)
            mask_periode = df_sold_all['EDITED'].astype(str).str.contains(filter_periode, na=False)
            df_selected = df_sold_all[mask_periode].copy()
            total_selected = len(df_selected)
            
            # --- LOGIKA DELTA BULAN LALU (Silet Analisis) ---
            try:
                from datetime import timedelta, datetime
                date_selected = datetime.strptime(f"01/{filter_periode}", "%d/%m/%Y")
                date_prev = (date_selected - timedelta(days=1))
                filter_prev = date_prev.strftime("%m/%Y")
                total_prev = len(df_sold_all[df_sold_all['EDITED'].astype(str).str.contains(filter_prev, na=False)])
            except:
                total_prev = 0
                filter_prev = "N/A"

            # --- 3. RENDER 3 METRIK UTAMA ---
            with st.container(border=True):
                m1, m2, m3 = st.columns(3)
                m1.metric("💰 TOTAL SOLD (ALL TIME)", f"{total_ever}", delta="Unit Laku")
                m2.metric(f"📅 {sel_bln_nama.upper()} {sel_thn}", f"{total_selected}", delta=f"Laku Bulan Ini")
                m3.metric(f"🕒 BULAN LALU ({filter_prev})", f"{total_prev}", delta=f"{total_selected - total_prev} dari bulan lalu", delta_color="normal")

            st.markdown("<br>", unsafe_allow_html=True)

            # --- 4. DATABASE TABEL (Pake Jangkar ID) ---
            st.markdown(f"##### 📊 DAFTAR PENJUALAN PERIODE {sel_bln_nama.upper()} {sel_thn}")
            if df_selected.empty:
                st.info(f"Belum ada data periode {filter_periode}")
            else:
                # Pastikan kolom ID ditarik
                df_selected['TGL_LAST'] = df_selected['EDITED']
                df_selected = df_selected.sort_values('TGL_LAST', ascending=False)
                
                config_sold = {
                    "TGL_LAST": st.column_config.TextColumn("⏰ TGL SOLD", width=180, disabled=True),
                    "EMAIL": st.column_config.TextColumn("📧 EMAIL", width=200),
                    "PASSWORD": st.column_config.TextColumn("🔑 PASS", width=120),
                    "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=150),
                    "SUBSCRIBE": st.column_config.TextColumn("📊 SUBS", width=80),
                    "LINK_CHANNEL": st.column_config.LinkColumn("🔗 LINK", width=100),
                    "STATUS": st.column_config.SelectboxColumn(
                        "⚙️ STATUS", width=100, 
                        options=["SOLD", "STANDBY", "PROSES", "BUSUK", "SUSPEND"]
                    ),
                    "ID": None # SEMBUNYIKAN KTP ASLI
                }

                # Tampilkan kolom ID di belakang layar buat jangkar update
                edited_sold = st.data_editor(
                    df_selected[["TGL_LAST", "EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "STATUS", "ID"]], 
                    use_container_width=True, 
                    hide_index=True, 
                    column_config=config_sold, 
                    key=f"grid_sold_{filter_periode}" # Key dinamis biar refresh tiap ganti bulan
                )

                # --- 5. LOGIKA SAVE (ANTI-DUPLIKAT PAKE ID) ---
                # Cek perubahan antara hasil edit dan data awal
                if not edited_sold.equals(df_selected[["TGL_LAST", "EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "STATUS", "ID"]]):
                    if st.button("💾 KONFIRMASI PERUBAHAN SOLD", type="primary", use_container_width=True):
                        try:
                            with st.spinner("Sinkronisasi data penjualan..."):
                                tgl_now = database.ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M")
                                data_batch = []
                                
                                for i, row in edited_sold.iterrows():
                                    # Cari baris asli pake ID (Bukan Index!)
                                    match_df = df[df['ID'] == row['ID']]
                                    if not match_df.empty:
                                        old_val = match_df.iloc[0]
                                        
                                        # Cek perubahan murni di kolom-kolom penting
                                        is_changed = (
                                            str(row['STATUS']) != str(old_val['STATUS']) or 
                                            str(row['EMAIL']).strip().lower() != str(old_val['EMAIL']).strip().lower() or
                                            str(row['PASSWORD']) != str(old_val['PASSWORD']) or
                                            str(row['NAMA_CHANNEL']) != str(old_val['NAMA_CHANNEL']) or
                                            str(row['SUBSCRIBE']) != str(old_val['SUBSCRIBE'])
                                        )

                                        if is_changed:
                                            data_batch.append({
                                                "id": row['ID'], # <--- JANGKAR UTAMA
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
            # --- TAMPILAN SINGKAT & PADAT ---
            st.error(f"🛡️ **AKSES TERBATAS: {level_aktif}**")
            st.write(f"Maaf **{user_aktif}**, area ini hanya untuk Owner.")

    # ==============================================================================
    # TAB 6: ARSIP CHANNEL (SINKRON SUPABASE - FULL EDITABLE v2.0)
    # ==============================================================================
    with tab_ar:
        if level_aktif in ["OWNER", "ADMIN"]:
            # --- 1. LOGIKA DASHBOARD ARSIP ---
            df_a = df[df['STATUS'].isin(['BUSUK', 'SUSPEND'])].copy()
        
            total_arsip = len(df_a)
            total_busuk = len(df_a[df_a['STATUS'] == 'BUSUK'])
            total_suspend = len(df_a[df_a['STATUS'] == 'SUSPEND'])

            # --- 2. RENDER METRIK ---
            with st.container(border=True):
                ca1, ca2, ca3 = st.columns(3)
                ca1.metric("💀 TOTAL ARSIP", f"{total_arsip}", delta="Akun Rusak", delta_color="inverse")
                ca2.metric("📉 TOTAL BUSUK", f"{total_busuk}", delta="Teknis/Kartu", delta_color="inverse")
                ca3.metric("🚫 TOTAL SUSPEND", f"{total_suspend}", delta="Banned YT", delta_color="inverse")

            st.markdown("<br>", unsafe_allow_html=True)

            # --- 3. DATABASE ARSIP (FULL EDITABLE & ID ANCHOR) ---
            st.markdown("##### 📂 DAFTAR AKUN ARSIP")
            if df_a.empty:
                st.success("✨ Arsip masih kosong!")
            else:
                df_a['TGL_KEJADIAN'] = df_a['EDITED']
                df_a = df_a.sort_values(by=['TGL_KEJADIAN'], ascending=False)
            
                # --- CONFIG: SEMUA GEMBOK DIBUKA & PAKAI ID ---
                config_arsip = {
                    "ID": None, # SEMBUNYIIN KTP ASLI
                    "TGL_KEJADIAN": st.column_config.TextColumn("⏰ TGL KEJADIAN", width=150, disabled=True),
                    "EMAIL": st.column_config.TextColumn("📧 EMAIL", width=200), 
                    "PASSWORD": st.column_config.TextColumn("🔑 PASS", width=120), 
                    "NAMA_CHANNEL": st.column_config.TextColumn("📺 CHANNEL", width=150), 
                    "SUBSCRIBE": st.column_config.TextColumn("📊 SUBS", width=80), 
                    "LINK_CHANNEL": st.column_config.LinkColumn("🔗 LINK", width=100), 
                    "STATUS": st.column_config.SelectboxColumn(
                        "⚙️ STATUS", 
                        width=100,
                        options=["STANDBY", "PROSES", "SOLD", "BUSUK", "SUSPEND"],
                        help="Ubah ke STANDBY jika ingin mendaur ulang akun ini."
                    )
                }
            
                # Tambahkan ID ke dalam list kolom yang ditarik
                kolom_tampil_a = ["TGL_KEJADIAN", "EMAIL", "PASSWORD", "NAMA_CHANNEL", "SUBSCRIBE", "LINK_CHANNEL", "STATUS", "ID"]

                edited_a = st.data_editor(
                    df_a[kolom_tampil_a], 
                    use_container_width=True, 
                    hide_index=True, 
                    column_config=config_arsip, 
                    key="grid_arsip_daur_ulang_v3"
                )

                # --- 4. LOGIKA SAVE (PAKE ID - ANTI DUPLIKAT) ---
                if not edited_a.equals(df_a[kolom_tampil_a]):
                    if st.button("💾 KONFIRMASI PERUBAHAN ARSIP", type="primary", use_container_width=True):
                        try:
                            with st.spinner("Sinkronisasi data..."):
                                tgl_now = database.ambil_waktu_sekarang().strftime("%d/%m/%Y %H:%M")
                                data_batch = []
                            
                                for i, row in edited_a.iterrows():
                                    # Cari baris asli di master DF pake ID
                                    match_df = df[df['ID'] == row['ID']]
                                
                                    if not match_df.empty:
                                        old_val = match_df.iloc[0]
                                    
                                        # Cek perubahan murni
                                        is_changed = (
                                            str(row['STATUS']) != str(old_val['STATUS']) or 
                                            str(row['EMAIL']).strip().lower() != str(old_val['EMAIL']).strip().lower() or
                                            str(row['PASSWORD']) != str(old_val['PASSWORD']) or 
                                            str(row['NAMA_CHANNEL']) != str(old_val['NAMA_CHANNEL']) or
                                            str(row['SUBSCRIBE']) != str(old_val['SUBSCRIBE'])
                                        )

                                        if is_changed:
                                            data_batch.append({
                                                "id": row['ID'], # <--- JANGKAR UTAMA
                                                "EMAIL": row['EMAIL'].strip().lower(),
                                                "PASSWORD": row['PASSWORD'],
                                                "NAMA_CHANNEL": row['NAMA_CHANNEL'],
                                                "SUBSCRIBE": str(row['SUBSCRIBE']),
                                                "LINK_CHANNEL": row['LINK_CHANNEL'],
                                                "STATUS": row['STATUS'],
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
            # --- TAMPILAN SINGKAT & PADAT ---
            st.error(f"🛡️ **AKSES TERBATAS: {level_aktif}**")
            st.write(f"Maaf **{user_aktif}**, area ini hanya untuk Admin.")
                        
    # ==========================================================================
    # TAB 7: SEWA NOMOR ONLINE (VERSI FIX LAYOUT & SALDO HIJAU)
    # ==========================================================================
    with tab_buy:
        API_KEY = st.secrets.get("OTPNUM_API_KEY", "")
        dict_server = {
            "Server 2 (Primary)": "https://otpnum.com/api/v2/",
            "Server 1 (Backup)": "https://otpnum.com/api/"
        }
        
        # --- HEADER: SERVER | REFRESH | SALDO (HIJAU + BESAR) ---
        with st.container(border=True):
            # Kita bagi kolom dengan rasio [3, 1, 1.5]
            # Dropdown Server (Kiri), Tombol Refresh (Tengah), Saldo (Kanan)
            c_srv, c_btn, c_bal = st.columns([3, 1, 1.5])
            
            # 1. Pilih Server (Kolom Kiri)
            srv_name = c_srv.selectbox("Pilih Server", list(dict_server.keys()), index=0, key="sel_server_online", label_visibility="collapsed")
            srv_url = dict_server[srv_name]

            # 2. Ambil Saldo
            res_bal = get_otpnum_api(srv_url, "balance", {"api_key": API_KEY})
            saldo = clean_angka(res_bal['data'].get('balance', 0)) if res_bal and res_bal.get('success') else 0

            # 3. Tombol Refresh (Kolom Tengah)
            if c_btn.button("🔄 REFRESH", use_container_width=True, key="ref_bal_online"):
                if "list_services_v2" in st.session_state: del st.session_state.list_services_v2
                st.rerun()
            
            # 4. Tampilan Saldo (Kolom Kanan - Tanpa CSS, Pakai Markdown Standar)
            c_bal.markdown(f"""
                #### <span style='color: #50FA7B; font-size: 20px;'>💰 SALDO Rp {saldo:,}</span>
            """, unsafe_allow_html=True)

        # --- PANEL ORDER (GOOGLE ONLY) ---
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
                    with st.spinner("Sabar, sedang memesan nomer..."):
                        try:
                            # Eksekusi beli nomor
                            sid = opts[pilih_name]
                            res_order = get_otpnum_api(srv_url, "order", {"api_key": API_KEY, "service_id": sid, "operator": "any", "country_id": 6})
                            
                            if res_order and res_order.get('success'):
                                st.session_state.active_order = {
                                    "id": res_order['data']['order_id'], 
                                    "number": res_order['data']['number'], 
                                    "url": srv_url
                                }
                                st.success(f"Nomor Berhasil Dipesan: {res_order['data']['number']}")
                                st.rerun()
                            else:
                                # Ini kalau API jawab tapi gagal (misal saldo kurang)
                                msg = res_order.get('message', 'Server lagi pening') if res_order else "Server gak respon"
                                st.error(f"❌ GAGAL: {msg}")

                        except Exception:
                            # --- INI KUNCI NYA: SEMUA ERROR TEKNIS DIBUANG ---
                            # Ganti tulisan HTTPSConnectionPool dll jadi pesan simpel:
                            st.error("❌ SERVER LAGI LEMOT / TIMEOUT!")
                            st.warning("Coba ganti Server atau tunggu 1 menit lagi!")
            else:
                st.warning("Layanan Google tidak ditemukan.")

        # --- AUTO-POLLING SMS (VERSI FIX TOMBOL CANCEL) ---
        if "active_order" in st.session_state:
            ord = st.session_state.active_order
            current_url = ord.get('url')
            
            with st.container(border=True):
                st.markdown(f"# 📱 `{ord.get('number')}`")
                st.caption("Salin nomor di atas untuk verifikasi Google")
                
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
                        msg_area.success(f"# 🔥 {st.session_state.otp_online}")
                        # Jika sudah ada OTP, kita stop auto-refresh-nya
                        st.info("OTP sudah muncul. Klik 'SELESAI' jika sudah selesai menyalin.")
                    else:
                        msg_area.info("⏳ Menunggu SMS Masuk...")
                        time.sleep(10)
                        st.rerun()
