import time as t_delay
import streamlit as st
import pandas as pd
from modules import database
from datetime import datetime
import pytz
import requests
from modules.database import supabase

def kirim_notif_wa(pesan):
    token = "f4CApLBAJDTPrVHHZCDF"
    target = "120363407726656878@g.us"
    url = "https://api.fonnte.com/send"
    payload = {'target': target, 'message': pesan, 'countryCode': '62'}
    headers = {'Authorization': token}
    try: requests.post(url, data=payload, headers=headers, timeout=5)
    except: pass

def tampilkan_area_staf():
    st.title("📘 Pusat Informasi")
    
    # --- 1. SETUP IDENTITAS ---
    user_aktif = st.session_state.get("user_aktif", "User").upper()
    user_level = st.session_state.get("user_level", "STAFF").upper()
    tz = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz)
    
    # --- 2. AMBIL DATA STAFF (DINAMIS DARI SUPABASE) ---
    res_staff = database.supabase.table("Staff").select("Nama, Level").execute()
    df_staff_db = pd.DataFrame(res_staff.data)
    
    # Ambil list nama & level unik (Kecuali Owner)
    list_staff_tujuan = df_staff_db[df_staff_db['Level'] != 'OWNER']['Nama'].unique().tolist()
    list_level_aktif = [l.upper() for l in df_staff_db['Level'].unique() if l.upper() != "OWNER"]
    
    foto_staff_default = "https://cdn-icons-png.flaticon.com/512/149/149071.png"

    # --- 3. DATABASE KETENTUAN (EDIT MANUAL DI SINI COK!) ---
    data_kerja = {
        "STAFF": { 
            "judul": "EDITOR", "ikon": "🎬",
            "rutinitas": [
                "Produksi video harian sesuai kebutuhan Kantor.",
                "Koordinasi dengan Admin terkait Stok Harian.",
                "Jika stok harian, tanpa perlu kirim tugas *(langsung serahkan hasil ke Admin via FD)*.",
                "Jika ada tugas khusus dari owner, wajib setor hasil tugas via Form Tugas Khusus."
            ],
            "sop": [
                "**Kualitas:** Minimal 1080p Full HD.",
                "**Ratio:** Format 9:16 ( Vertical ).",
                "Manipulasi Metadata & Produksi Konten *(detail cek panduan kerja)*.",
                "Aturan Dialog & Alur Penyerahan File *(detail cek panduan kerja)*."
            ]
        },
        "UPLOADER": {
            "judul": "UPLOADER", "ikon": "📲",
            "rutinitas": [
                "Upload tepat waktu sesuai jadwal yang tersedia",
                "Hapus file video yang sudah di Upload ( termasuk di folder sampah ).",
                "Koordinasi dengan Admin terkait stok video di HP.",
                "Isi daya setiap HP ( Jangan sampai lowbat ).",
                "Hapus pesan di HP, Restart HP, Update Aplikasi YT secara berkala ( 2 hari sekali )."
            ],
            "sop": [
                "**DILARANG** menautkan wifi kantor ke HP kerja.",
                "Judul & Deskripsi mengikuti WA Kerja, atau isi manual pada konten-konten tertentu.",
                "Pilih thumbnail yang jelas! utamakan kejadian atau fokus ke karakter.",
                "Sebelum upload, wajib tonton video Youtube orang lain beberapa detik.",
                "Selesai upload, tonton dulu video Youtube orang lain, baru close YT nya."
            ]
        },
        "ADMIN": {
            "judul": "ADMIN", "ikon": "📊",
            "rutinitas": [
                "Memastikan channel standby selalu update.",
                "Update dan Rekap database channel & HP ( Hapus Login ).",
                "Update stok video di masing-masing HP.",
                "Memastikan kegiatan operasional kantor berjalan efektif dan efisien.",
                "Tugas lain disesuaikan kebutuhan kantor."
            ],
            "sop": [
                "Cek stok channel, video, kuota, listrik, dll.",
                "Data Channel wajib selalu update ( real-time ).",
                "Mencatat arus kas operasional kantor.",
                "Akurasi data channel dan keuangan 100% (No Error).",
                "Selalu koordinasi dengan staff lain terkait stok video, jadwal, channel, dll."
            ]
        }
    }

    tab_tugas, tab_panduan, tab_peraturan, tab_kontrak = st.tabs([
        "📝 TUGAS KERJA", "📖 PANDUAN KERJA", "⚖️ PERATURAN KERJA", "📜 KONTRAK KERJA"
    ])

    # ==============================================================================
    # TAB 1: TUGAS KERJA
    # ==============================================================================
    with tab_tugas:        
        # --- A. TAMPILAN DINAMIS (2 CARD MODEL) ---
        if user_level in ["OWNER"]:
            st.markdown("#### 🕒 Monitoring Standar Tim")
            
            target_monitor = st.radio(
                "Pilih Divisi:", list_level_aktif, horizontal=True, label_visibility="collapsed"
            )
            
            # Kita mapping STAFF ke label EDITOR biar gak bingung
            data = data_kerja.get(target_monitor)
            if data:
                c1, c2 = st.columns(2)
                with c1:
                    with st.container(border=True):
                        st.info(f"📌 **Rutinitas Harian {data['judul']}**")
                        for r in data['rutinitas']: st.markdown(f"✅ {r}")
                with c2:
                    with st.container(border=True):
                        st.success(f"🛠️ **Standar Operasional Kerja {data['judul']}**")
                        for s in data['sop']: st.markdown(f"⭐ {s}")
        
        else:
            # --- B. TAMPILAN STAFF (OTOMATIS) ---
            st.markdown(f"#### 🕒 Tugas & Standar Kerja {user_aktif}")
            data = data_kerja.get(user_level)
            if data:
                c1, c2 = st.columns(2)
                with c1:
                    with st.container(border=True):
                        st.markdown(f"#### 📌 Rutinitas Harian {data['judul']}")
                        for r in data['rutinitas']: st.markdown(f"✅ {r}")
                with c2:
                    with st.container(border=True):
                        st.markdown(f"#### 🛠️ Standar Operasional Kerja")
                        for s in data['sop']: st.markdown(f"⭐ {s}")

        st.divider()
        # --- B. PANEL OWNER (KIRIM TUGAS KHUSUS) ---
        if user_level in ["OWNER", "ADMIN"]:
            with st.expander("✨ **KIRIM TUGAS KHUSUS BARU**", expanded=False):
                with st.form("form_tugas_baru", clear_on_submit=True):
                    col1, col2 = st.columns([2, 1])
                    instr = col1.text_area("Instruksi Tugas", placeholder="Tulis instruksi di sini...")
                    staf_tujuan = col2.selectbox("Pilih Staf", list_staff_tujuan)
                    
                    if st.form_submit_button("🚀 KIRIM TUGAS SEKARANG", use_container_width=True):
                        if instr:
                            # 1. Generate ID Unik
                            new_id_gede = f"T{sekarang.strftime('%m%d%H%M%S')}"
                            
                            # 2. Potong Detail Instruksi (Maks 50 Huruf)
                            instr_wa = (instr[:50] + '...') if len(instr) > 50 else instr
                            
                            # 3. Simpan ke Database Supabase
                            database.supabase.table("Tugas").insert({
                                "ID": new_id_gede, 
                                "Staf": staf_tujuan, 
                                "Instruksi": instr, 
                                "Status": "PROSES", 
                                "Deadline": sekarang.strftime("%Y-%m-%d")
                            }).execute()
                            
                            # 4. Kirim Notifikasi WA (ID di bawah Tugas Baru)
                            kirim_notif_wa(
                                f"🔔 *TUGAS BARU*\n"
                                f"🆔 *ID:* {new_id_gede}\n"
                                f"👤 *Untuk:* {staf_tujuan}\n"
                                f"📝 *Detail:* {instr_wa}"
                            )
                            
                            st.success(f"✅ Tugas {new_id_gede} Terkirim!")
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.warning("⚠️ Isi instruksinya dulu!")

        # --- C. PROSES DATA (TEKNIK SELECTIVE SUPABASE) ---
        # Kita panggil kolomnya SATU-SATU biar 'id' kecil gak ikut campur!
        try:
            res = database.supabase.table("Tugas").select("ID, Staf, Instruksi, Status, Link_Hasil, Catatan_Revisi, Deadline").execute()
            df_t = pd.DataFrame(res.data)
        except:
            df_t = pd.DataFrame()

        if not df_t.empty:
            # Standarisasi Header biar kodingan di bawah gak bingung
            df_t.columns = [str(c).strip().upper() for c in df_t.columns]

            # --- D. TUGAS AKTIF (CARD 2 KOLOM) ---
            st.markdown("#### ⚡ Progres Tugas Khusus")
            status_aktif = ['PROSES', 'WAITING QC', 'REVISI']
            
            if user_level in ["OWNER", "ADMIN"]:
                mask = df_t['STATUS'].isin(status_aktif)
            else:
                mask = (df_t['STAF'].str.upper() == user_aktif) & (df_t['STATUS'].isin(status_aktif))
            
            # Kita pake List Reversed kayak web lama lo biar yang terbaru di atas
            data_list = list(reversed(df_t[mask].to_dict('records')))

            if not data_list:
                st.caption("Tidak ada tugas khusus aktif.")
            else:
                for i in range(0, len(data_list), 2):
                    cols = st.columns(2)
                    for j in range(2):
                        if i + j < len(data_list):
                            t = data_list[i + j]
                            # INI KUNCI SAKTI LO: Ambil ID GEDE dari kolom ID
                            id_gede = str(t.get('ID', 'N/A'))
                            staf_nama = str(t.get('STAF', '')).upper()
                            status = str(t.get('STATUS', 'PROSES')).upper()
                            
                            with cols[j]:
                                with st.container(border=True):
                                    # Header Kartu
                                    c_ava, c_txt = st.columns([1, 4])
                                    c_ava.image(foto_staff_default, width=50)
                                    with c_txt:
                                        st.markdown(f"**{staf_nama}** | <span style='color:#1d976c;'>ID: {id_gede}</span>", unsafe_allow_html=True)
                                        icon = "🟡" if status == "WAITING QC" else "🔴" if status == "REVISI" else "🟢"
                                        st.markdown(f"{icon} `{status}`")
                                    
                                    olah = st.toggle("🔍 Buka Detail", key=f"tgl_{id_gede}")
                                    if olah:
                                        st.divider()
                                        if t.get("CATATAN_REVISI"):
                                            st.warning(f"⚠️ **REVISI:** {t['CATATAN_REVISI']}")
                                        st.write(f"📝 {t.get('INSTRUKSI', '-')}")
                                        
                                        # PANEL QC (OWNER)
                                        if user_level in ["OWNER", "ADMIN"]:
                                            if t.get("LINK_HASIL") and t["LINK_HASIL"] != "-":
                                                st.link_button("🚀 BUKA VIDEO (QC)", t['LINK_HASIL'], use_container_width=True)
                                            
                                            st.divider()
                                            cat_admin = st.text_area("Catatan:", key=f"cat_{id_gede}")
                                            b1, b2, b3 = st.columns(3)
                                            
                                            if b1.button("✅ ACC", key=f"acc_{id_gede}", use_container_width=True):
                                                database.supabase.table("Tugas").update({"Status": "FINISH"}).eq("ID", id_gede).execute()
                                                kirim_notif_wa(f"✅ *TUGAS ACC*\n🆔 *ID:* {id_gede}")
                                                st.rerun()
                                            if b2.button("🔴 REV", key=f"rev_{id_gede}", use_container_width=True):
                                                database.supabase.table("Tugas").update({"Status": "REVISI", "Catatan_Revisi": cat_admin}).eq("ID", id_gede).execute()
                                                kirim_notif_wa(f"⚠️ *REVISI*\n🆔 *ID:* {id_gede}\n📝: {cat_admin}")
                                                st.rerun()
                                            if b3.button("🚫 BATAL", key=f"can_{id_gede}", use_container_width=True):
                                                database.supabase.table("Tugas").update({"Status": "CANCELED"}).eq("ID", id_gede).execute()
                                                st.rerun()

                                        # PANEL SETOR (STAFF)
                                        else:
                                            # Cek apakah sudah ada link yang pernah ditempel
                                            link_lama = t.get("LINK_HASIL", "-")
                                            
                                            if status == "WAITING QC":
                                                st.info(f"✅ Sudah disetor. Link: {link_lama}")
                                                st.caption("Tunggu proses checking ya...")
                                            else:
                                                # Staff bisa paste link di sini
                                                l_in = st.text_input("Tempel (Paste) Link GDrive:", key=f"in_{id_gede}")
                                                if st.button("🚀 SETOR SEKARANG", key=f"btn_{id_gede}", use_container_width=True):
                                                    if "drive.google.com" in l_in:
                                                        database.supabase.table("Tugas").update({
                                                            "Status": "WAITING QC", 
                                                            "Link_Hasil": l_in, 
                                                            "Waktu_Kirim": sekarang.strftime("%d/%m/%Y %H:%M")
                                                        }).eq("ID", id_gede).execute()
                                                        
                                                        kirim_notif_wa(f"📤 *SETORAN*\n👤 *Dari:* {user_aktif}\n🆔 *ID:* {id_gede}")
                                                        st.success("✅ Berhasil Disetor!"); t_delay.sleep(1); st.rerun()
                                                    else:
                                                        st.warning("⚠️ Pastikan yang ditempel adalah link GDrive!")

        # ==============================================================================
        # E. ARSIP TUGAS (VERSI CLEAN - NO DOUBLE IF)
        # ==============================================================================
        with st.expander("📜 RIWAYAT & ARSIP TUGAS", expanded=False):
            c_arsip1, c_arsip2 = st.columns([2, 1])
            daftar_bulan = {
                1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni", 
                7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"
            }
            
            bln_arsip_nama = c_arsip1.selectbox("📅 Pilih Bulan Riwayat:", list(daftar_bulan.values()), index=sekarang.month - 1, key="sel_bln_arsip")
            bln_arsip_angka = [k for k, v in daftar_bulan.items() if v == bln_arsip_nama][0]
            thn_arsip = c_arsip2.number_input("📅 Tahun:", value=sekarang.year, min_value=2024, max_value=2030, key="sel_thn_arsip")

            # --- 1. PROSES FILTERING (SATU ALUR) ---
            df_laci = df_t.copy()
            
            if not df_laci.empty:
                # Konversi Deadline & Filter Waktu/Status
                df_laci['DEADLINE_DT'] = pd.to_datetime(df_laci['DEADLINE'], errors='coerce')
                mask_waktu = (df_laci['DEADLINE_DT'].dt.month == bln_arsip_angka) & (df_laci['DEADLINE_DT'].dt.year == thn_arsip)
                mask_status = df_laci['STATUS'].isin(['FINISH', 'CANCELED', 'BATAL', 'DONE'])
                
                df_laci = df_laci[mask_waktu & mask_status]
                
                # Filter Level Staff
                if user_level in ["STAFF", "UPLOADER"]:
                    df_laci = df_laci[df_laci['STAF'].str.upper() == user_aktif]

            # --- 2. LOGIKA TAMPILAN (Hanya satu pengecekan hasil akhir) ---
            if not df_laci.empty:
                # Statistik
                total_f = len(df_laci[df_laci['STATUS'] == "FINISH"])
                total_c = len(df_laci[df_laci['STATUS'].isin(['CANCELED', 'BATAL'])])
                
                st.markdown(f"📊 **Laporan {bln_arsip_nama}:** <span style='color:#1d976c;'>✅ {total_f} Selesai</span> | <span style='color:#e74c3c;'>🚫 {total_c} Dibatalkan</span>", unsafe_allow_html=True)
                
                # Bersihkan None/NaN & Formatting
                df_final = df_laci.copy()
                df_final = df_final.fillna("").astype(str).replace(['None', 'nan'], '', regex=True)
                
                kolom_fix = ['ID', 'STAF', 'INSTRUKSI', 'DEADLINE', 'STATUS', 'CATATAN_REVISI']
                
                st.dataframe(
                    df_final.sort_values(by=['DEADLINE', 'ID'], ascending=[False, False])[kolom_fix],
                    column_config={
                        "ID": st.column_config.TextColumn("🆔 ID"),
                        "STAF": st.column_config.TextColumn("👤 STAF"),
                        "INSTRUKSI": st.column_config.TextColumn("📝 JUDUL KONTEN"),
                        "DEADLINE": st.column_config.TextColumn("📅 TGL"),
                        "STATUS": st.column_config.TextColumn("🚩 STATUS"),
                        "CATATAN_REVISI": st.column_config.TextColumn("📋 KETERANGAN")
                    },
                    hide_index=True,
                    use_container_width=True
                )
            else:
                # Ini muncul kalau setelah di-filter datanya emang gak ada
                st.info(f"📭 Tidak ada riwayat tugas pada {bln_arsip_nama} {thn_arsip}.")
                    
    # ==============================================================================
    # TAB 2: PANDUAN KERJA (FILTERED BY LEVEL)
    # ==============================================================================
    with tab_panduan:        
        # --- FUNGSI MODULAR PANDUAN EDITOR (MODEL CARD SYSTEM) ---
        def panduan_setor_tugas():            
            # --- CARD 1: RUTINITAS (FULL WIDTH) ---
            with st.container(border=True):
                st.markdown("#### 1️⃣ Rutinitas & Koordinasi Harian:")
                st.write("- Selalu koordinasi dengan Admin buat tau stok video mana yang mau habis.")
                st.write("- Wajib bikin video harian sesuai kebutuhan stok kantor.")
                st.write("- Dahulukan membuat stok untuk Konten yang stok videonya paling sedikit.")            
            st.write("") # Spacing

            # --- CARD 2: MANIPULASI METADATA & BYPASS DNA (NEW!) ---
            with st.container(border=True):
                st.markdown("#### 2️⃣ Manipulasi Metadata & Produksi Konten")
                st.warning("🚨 Jangan kirim **file mentah** langsung dari hasil web AI / software editing.")
                
                col_meta1, col_meta2 = st.columns(2)
                with col_meta1:
                    st.markdown("**🛡️ Cara Manipulasi Metadata:**")
                    st.write("- Masukkan semua video ke folder `FILE MENTAH`.")
                    st.write("- Jalankan **`METADATA.bat`** (Wajib jalankan ini untuk buang sidik jari AI).")
                    st.write("- Tool otomatis menghapus jejak software (Filmora/Capcut) & Device PC.")
                    st.write("- **Metadata identik di banyak HP** = *Resiko akun kena suspend massal*!")
                
                with col_meta2:
                    st.markdown("**🆔 Variasi Nama File & Caption:**")
                    st.write("- Nama file sudah otomatis dibuat acak ala rekaman HP asli.")
                    st.write("- Pastikan posisi subtitle atau elemen penting tidak terlalu mepet ke pinggir frame.")
                    # --- TAMPILAN FORMAT YANG LO MAU ---
                    st.info(f"📌 **Format Manual:** `VID_tahun-bulan-tanggal_jam-menit-detik.mp4` ")
                    st.caption("💡 **Misalnya:** `VID_20260412_053015.mp4` berarti Tahun 2026, Bulan 04, Tgl 12, Jam 05:30:15")
                    
            st.write("") # Spacing

            # --- CARD 3: ATURAN DIALOG ---
            with st.container(border=True):
                st.markdown("#### 3️⃣ Alat Pendukung & Aturan Dialog Masjid")
                
                # Samakan pembagian kolom 50:50 biar lurus sama Card 2
                col_kiri, col_kanan = st.columns(2)

                with col_kiri:
                    st.markdown("**📥 Alat Tempur Editor:**")
                    
                    # 1. Link Google Docs/Drive untuk Dialog
                    url_dialog = "https://docs.google.com/document/d/1itFxRuNkQSgZHQq1MZ9fEo-MCj876MlC4Uw60Ksa7as/edit?usp=sharing"
                    st.link_button(
                        label="📖 DOWNLOAD FORMAT DIALOG NENEK",
                        url=url_dialog,
                        use_container_width=True
                    ) 
                    
                    st.write("") # Spacing biar gak nempel

                    # 2. Link Direct Download File Bypass (.bat) dari Drive
                    url_bypass = "https://drive.google.com/file/d/1z0bGr2HsT60V-vlryPaAiQxg_W7sxAg0/view?usp=sharing"
                    st.link_button(
                        label="🛡️ DOWNLOAD BYPASS METADATA.bat",
                        url=url_bypass,
                        use_container_width=True
                    )
                    st.caption("💡 Klik tombol di atas untuk membuka/mengunduh file dari GDrive.")

                with col_kanan:
                    st.markdown("**📢 INFO PENTING PENYESUAIAN DIALOG:**")
                    st.write("- Jika masjid dari **Strawberry**, isi dialog wajib menyebut **Strawberry**.")
                    st.write("- Jika masjid dari **Barang Bekas**, isi dialog sesuai bahan (Koran/Kaleng/dll).")
                    st.write("- Jika visual **Ka'bah/Mekah**, Hanya gunakan dialog tentang **Ka'bah/Mekah**.")
                    st.caption("💡 Boleh menambahkan dialog dengan kreativitas sendiri (asal sesuai konteks).")

            # --- HEADER JALUR PENYERAHAN ---
            st.markdown("#### 4️⃣ Alur Penyerahan Hasil Kerja")
            
            col_jalur1, col_jalur2 = st.columns(2)
            
            # --- CARD 4: JALUR A (KIRI) ---
            with col_jalur1:
                with st.container(border=True):
                    st.info("📂 **JALUR A: STOK HARIAN (OFFLINE)**")
                    st.markdown("**Target:** Video rutin harian untuk stok HP.")
                    st.markdown("**Langkah Kerja:**")
                    st.write("- **Tidak perlu** input data ke sistem/web ini.")
                    st.write("- Pastikan audio & visual sudah OKE, **SYNC PAS**.")
                    st.write("- Copy file dari folder `SIAP TEMPUR` ke **Flashdisk (FD)**.")
                    st.write("- Serahkan ke **Admin** untuk QC & pindah ke folder Stok.")

            # --- CARD 5: JALUR B (KANAN) ---
            with col_jalur2:
                with st.container(border=True):
                    st.success("🚀 **JALUR B: TUGAS KHUSUS (ONLINE)**")
                    st.markdown("**Target:** Instruksi khusus di Tab Tugas.")
                    st.markdown("**Langkah Kerja:**")
                    st.write("- Upload `FILE VIDEO` ke **Google Drive**.")
                    st.write("- Setting link ke: *`Anyone with the link`*.")
                    st.write("- Buka Tab **TUGAS KERJA**, cari ID tugasmu.")
                    st.write("- Klik **🔍 Buka Detail**, tempel link G-Drive, lalu klik **SETOR**.")

        # --- FUNGSI MODULAR PANDUAN UPLOADER (SOP SISTEMATIS) ---
        def panduan_ritual_upload():            
            # --- FASE 1: NETWORK & DEVICE SANITIZATION (MENIT 0-2) ---
            with st.container(border=True):
                st.markdown("#### 1️⃣ Ritual Sterilisasi HP")
                st.caption("💡 **Tujuan:** Menghapus jejak `Device Fingerprint`, agar HP dianggap `Baru` oleh server Google.")
                st.write("- **Wajib Restart HP** setiap pagi sebelum upload pertama kali.")
                st.write("- **Hapus Cache & Data:** setiap pagi setelah restart HP. Masuk ke **`Settingan HP > Aplikasi > YouTube & Google Play Services`**.")
                st.write("- Matikan Data Seluler *(`Mode Pesawat`)* selama 15 - 20 detik, agar `Dynamic IP` benar-benar baru, **setiap akan upload**.")
                st.write("- Pastikan GPS Lokasi dalam keadaan **Mati/OFF** (*Jangan biarkan Google merekam lokasi setiap HP Kerja*).")
                st.write("- **Dilarang keras** menggunakan WiFi Kantor! Wajib 100% menggunakan Data Seluler per unit HP.") 
            st.write("") # Spacing

            # --- FASE 2: RITUAL PEMANASAN AKUN (LEBUR 2 KOLOM) ---
            with st.container(border=True):
                st.markdown("#### 2️⃣ Ritual Pemanasan (Pancingan Alogritma)")
                st.warning("💡 Dilakukan **SEBELUM** masuk ke menu upload, agar tidak dianggap Bot Uploader.")
            
                col_warm1, col_warm2 = st.columns(2)
            
                with col_warm1:
                    st.write("**🔍 1. Interaksi Organik (Aktivitas)**")
                    st.write("- Ketik manual kata kunci sesuai tema (**Contoh:** `Miniatur Masjid, Masjid Nenek, Drama Sakura`).")
                    st.write("- Klik salah satu video dari hasil cari, lalu tonton sampai selesai.")
                    st.write("- Balik ke tab Shorts, tonton lagi 2 video orang lain *20-30 detik* dan kasih **1 Like Acak**.")          

                with col_warm2:
                    st.write("**📱 2. Langkah Transisi ke Upload**")
                    st.write("- Lakukan scroll pelan (skip tonton) pada beberapa video berikutnya untuk **meniru perilaku manusia**.")
                    st.write("- Setelah selesai scroll, diamkan aplikasi di beranda selama **10 detik** (jangan langsung klik upload!).")
                    st.write("- Baru kemudian klik ikon **[+]** atau **tombol upload video**.")
            
            st.write("") # Spacing

            # --- FASE 3: EKSEKUSI PUBLIKASI & OPTIMASI ---
            with st.container(border=True):
                st.markdown("#### 3️⃣ Prosedur Upload dan Optimasi Metadata")            
                # --- BARIS ATAS: PROSEDUR TEKNIS (2 KOLOM) ---
                col_up1, col_up2 = st.columns(2)
            
                with col_up1:
                    st.write("**📱 Langkah Eksekusi (Proses Upload):**")
                    st.write("1. Tekan ikon **`[+] > Unggah Video >`** Pilih file yang ada di HP.")
                    st.write("2. Pilih Thumbnail yang jelas, tidak blur, dan objek atau karakter utama menonjol.")
                    st.write("3. Masukkan judul dari daftar referensi di bawah (*Pastikan judul sinkron dengan isi video*).")
                    st.write("4. Wajib pilih opsi **`Bukan untuk anak-anak`** dan **`Konten Modifikasi > Ya`**.")

                with col_up2:
                    st.write("**🛡️ Protokol Keamanan (Anti-Bot System):**")
                    st.write("- Tunggu status *'Processing'* 100%. Ini memastikan resolusi video maksimal (HD).")
                    st.write("- Pastikan visibilitas sudah benar-benar set ke **Publik**, bukan 'Tidak Publik' atau 'Pribadi'.")
                    st.write("- **Jangan langsung klik Publish!**. Berikan jeda **30-60 detik** di halaman Upload.")
                    st.write("- Klik **'Publish'** HANYA jika status durasi tunggu (loading) selesai.")

                # --- BARIS BAWAH: REFERENSI JUDUL (DENGAN LOGIKA MODIFIKASI) ---
                st.write("---")
                st.markdown("#### 📌 Daftar Referensi Judul, Hastag & Aturan Modifikasi")
                
                # Blok Aturan Modifikasi (Abu-abu & Jelas)
                with st.container(border=True):
                    st.markdown(":violet-badge[:material/star: Favorite] :orange-badge[⚙️ Aturan Modifikasi Judul Video dan Hastag:] :gray-badge[Deprecated]")
                    st.markdown(" * Jika karakter video adalah *'Kakek'*, ubah kata *'Nenek'* menjadi *'Kakek'*.")
                    st.markdown(" * Bagian **[ XXXX ]** wajib diganti dengan bahan masjid (**Contoh:** *Kardus Bekas, Buah Melon, Daun Pisang, Dll*).")
                    st.markdown(" * Bagian **+ Emoji** wajib diganti dengan emoji asli (**Contoh:** 🕌, ✨, 😍, 🔥, *Dll*).")
                    st.markdown(" * Wajib ditambahkan 3 hastag (*pilih secara acak*), **Contoh:** `Nenek Buat Masjid Miniatur Dari Strawberry🕌 #shorts #masyaallah #aivideo`")

                # Daftar Judul dengan 3 Kolom agar Padat & Rapi
                col_j1, col_j2, col_j3 = st.columns(3)
                
                with col_j1:
                    st.markdown("🔹 <kbd>:grey[Miniatur Masjid Buatan Nenek + Emoji]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Masjid Buatan Nenek Dari [ *XXXX* ] Emoji]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Miniatur Masjid Dari [ *XXXX* ] Buatan Nenek]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Masjid Miniatur Nenek Dari [ *XXXX* ]]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Nenek Membuat Masjid Miniatur Dari [ *XXXX* ]]</kbd>", unsafe_allow_html=True)
                
                with col_j2:
                    st.markdown("🔹 <kbd>:grey[Masjid Indah Dari [ *XXXX* ] Buatan Nenek]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Miniatur Masjid Indah Buatan Nenek [ *XXXX* ]]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Masjid Indah Dari [ *XXXX* ] Bikinan Nenek]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Nenek Bikin Miniatur Masjid Dari [ *XXXX* ]]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Masya Allah! Miniatur Masjid Buatan Nenek] + Emoji</kbd>", unsafe_allow_html=True)
                
                with col_j3:
                    st.markdown("🔹 <kbd>:grey[Nenek Buat Miniatur Masjid Dari [ *XXXX* ]]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Masjid Miniatur Buatan Nenek + Emoji]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Masjid Miniatur Dibuat Nenek dari [ *XXXX* ]]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Nenek Buat Masjid Miniatur Dari [ *XXXX* ] + Emoji]</kbd>", unsafe_allow_html=True)
                    st.markdown("🔹 <kbd>:grey[Nenek Bikin Masjid Miniatur + Emoji]</kbd>", unsafe_allow_html=True)
                    
                st.write("---")
                col_hastag1, col_hastag2, col_hastag3, col_hastag4, col_hastag5, col_hastag6 = st.columns(6)

                with col_hastag1:
                    st.markdown("<kbd>:grey[*#miniaturmasjid*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#masjid*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#shorts*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#shortsviral*]</kbd>", unsafe_allow_html=True)
                
                with col_hastag2:
                    st.markdown("<kbd>:grey[*#trending*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#foryou*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#fyp*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#miniature*]</kbd>", unsafe_allow_html=True)
                
                with col_hastag3:
                    st.markdown("<kbd>:grey[*#diycrafts*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#kerajinantangan*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#storytelling*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#masyaallah*]</kbd>", unsafe_allow_html=True)

                with col_hastag4:
                    st.markdown("<kbd>:grey[*#nenekkreatif*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#aivideo*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#handmade*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#masjidindah*]</kbd>", unsafe_allow_html=True)
                
                with col_hastag5:
                    st.markdown("<kbd>:grey[*#islamicart*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#satisfying*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#liriklagu*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#jumpstyle*]</kbd>", unsafe_allow_html=True)
                
                with col_hastag6:
                    st.markdown("<kbd>:grey[*#bome*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#fyptiktok*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#relatable*]</kbd>", unsafe_allow_html=True)
                    st.markdown("<kbd>:grey[*#shortsvideo*]</kbd>", unsafe_allow_html=True)

                st.warning("⚠️ **Perhatian:** Gunakan judul, emoji, hastag yang berbeda untuk tiap Channel di unit HP yang sama!")
            st.write("") # Spacing

        def panduan_rawat_hp():
            st.markdown("#### ⚙️ 4️⃣ **MAINTENANCE UNIT HP (DAILY CHECK)**")
            
            col_hp1, col_hp2 = st.columns(2)
            
            # --- CARD 3: KEBERSIHAN DATA (KIRI) ---
            with col_hp1:
                with st.container(border=True):
                    st.info("**🧹 Pembersihan Memori:**")
                    st.write("- Segera hapus file video yang sudah sukses di-upload agar memori tidak penuh.")
                    st.write("- Wajib cek folder `Recently Deleted / Sampah` di galeri dan kosongkan secara berkala.")
                    st.write("- Hapus pesan sms atau chat di HP yang sudah tidak diperlukan.")

            # --- CARD 4: PERFORMA UNIT (KANAN) ---
            with col_hp2:
                with st.container(border=True):
                    st.success("**⚡ Performa & Daya:**")
                    st.write("- Update aplikasi YT dan Google secara berkala ( *minimal 3 hari sekali* ).")
                    st.write("- Pastikan HP selalu standby dicolok charger. **Jangan sampai Lowbat atau mati total!**")
                    st.write("- Jika ada kendala terkait HP atau Channel, segera laporkan ke Admin/Owner.")

        # --- FUNGSI MODULAR PANDUAN ADMIN (MODEL CARD SYSTEM) ---
        def panduan_kontrol_admin():            
            # --- CARD 1: PRODUKSI & STOK CHANNEL (PABRIK CHANNEL) ---
            with st.container(border=True):
                st.markdown("#### 🏗️ Produksi & Stok Channel Standby")
                st.info("💡 **Tugas Utama:** Admin adalah penyedia akun agar operasional tidak berhenti.")
                st.write("- Mencari akun Google fresh/tua untuk bahan channel baru.")
                st.write("- Membuat channel-channel baru secara berkala untuk stok standby.")
                st.write("- Memastikan channel standby sudah siap (setting dasar YT sudah oke).")
                st.write("- Segera masukkan data channel baru ke sistem agar siap digunakan.")

            st.write("") # Spacing

            # --- CARD 2: KONTROL OPERASIONAL ---
            with st.container(border=True):
                st.markdown("#### 🔄 Rutinitas & Rekap Harian")
                # --- POIN REQUEST DIAN ---
                st.write("- Wajib mengganti channel yang sudah **Busuk** atau **Tembus** dengan channel baru dari stok standby *(umur channel pengganti minimal 4 hari)*.")
                st.write("- Memastikan channel standby selalu update statusnya (siap/digunakan).")
                st.write("- Update jadwal harian untuk uploader setiap sore.")
                st.write("- Update stok video di masing-masing HP secara berkala.")
                st.write("- Memastikan seluruh kegiatan kantor berjalan efektif tanpa hambatan teknis.")

            st.write("") # Spacing

            # --- CARD 3: STANDAR OPERASIONAL (SOP) ---
            st.markdown("#### 📝 Standar Operasional Admin")
            col_adm1, col_adm2 = st.columns(2)
            
            with col_adm1:
                with st.container(border=True):
                    st.info("🔍 **Pengecekan Logistik**")
                    st.write("- Rutin cek kuota internet, listrik, dan kondisi unit HP.")
                    st.write("- Data Channel wajib di-update secara real-time (No Delay).")
                    st.write("- Akurasi data channel wajib 99% (No Error).")

            with col_adm2:
                with st.container(border=True):
                    st.success("💰 **Keuangan & Koordinasi**")
                    st.write("- Mencatat setiap pengeluaran operasional (beli akun, kuota, dll).")
                    st.write("- Wajib cerewet ingetin Editor soal stok dan Uploader soal jadwal.")
                    st.write("- Data keuangan tidak boleh ada selisih sedikit pun.")

            st.warning("⚠️ Admin adalah jantung data kantor. Kelalaian data Admin berakibat fatal pada performa seluruh tim!")

        def panduan_keamanan_akun():
            st.markdown("#### 🔐 PROSEDUR KEAMANAN AKUN GOOGLE")
            with st.container(border=True):
                col_sec1, col_sec2 = st.columns(2)
                
                with col_sec1:
                    st.success("**🛡️ Aturan Penggunaan Akun:**")
                    st.write("- **Dilarang Keras** login akun Google kantor di perangkat pribadi (Laptop/HP sendiri).")
                    st.write("- Wajib pasang Nomor HP yang aktif di semua Akun Google.")
                    st.write("- Pastikan semua akun google telah diganti password saat pembelian.")
                    st.write("- Pastikan semua data akun google ter-input dengan benar di Sistem.")
                
                with col_sec2:
                    st.error("**🚨 JIKA MUNCUL VERIFIKASI (OTP):**")
                    st.write("Jika HP tiba-tiba minta klik angka atau masukkan kode verifikasi:")
                    st.write("1. **JANGAN** asal tekan angka/tombol 'YES'.")
                    st.write("2. **JANGAN** isi kode sembarangan.")
                    st.write("3. **WAJIB** hubungi Admin atau Owner untuk konfirmasi.")
                
        # --- LOGIKA PENAMPILAN (THE GATEKEEPER) ---
        if user_level in ["OWNER", "ADMIN"]:
            pilihan = st.radio("Pilih Panduan Divisi:", ["EDITOR", "UPLOADER", "ADMIN"], horizontal=True)
            
            if pilihan == "EDITOR": 
                panduan_setor_tugas()
            elif pilihan == "UPLOADER": 
                panduan_ritual_upload()
                panduan_rawat_hp()
                panduan_keamanan_akun() # <-- Muncul di monitoring Owner/Admin
            elif pilihan == "ADMIN": 
                panduan_kontrol_admin()
                panduan_keamanan_akun() # <-- Muncul di monitoring Owner/Admin
            
        elif user_level == "UPLOADER":
            panduan_ritual_upload()
            panduan_rawat_hp()
            panduan_keamanan_akun() # <-- MUNCUL DI LAYAR UPLOADER        
        elif user_level == "STAFF": # Editor
            panduan_setor_tugas() 
            # Editor gak perlu liat keamanan akun karena gak pegang HP/Akun
                
    # ==============================================================================
    # TAB 3: PERATURAN KERJA (MODEL CARD - FULL POLICY)
    # ==============================================================================
    with tab_peraturan:        
        # --- CARD 1: KETENTUAN WAKTU & DISIPLIN (SYSTEM SHIFT) ---
        with st.container(border=True):
            st.markdown("#### 📜 KETENTUAN WAKTU KERJA")
            
            col_shift1, col_shift2 = st.columns(2)
            
            with col_shift1:
                st.info("☀️ **SHIFT 1 (Pagi - Sore)**")
                st.write("**⏰ Jam Kerja:** 08:00 s/d 16:00 WIB")
                st.write("**🕒 Istirahat:** 11:30 – 12:30 WIB")

            with col_shift2:
                st.success("🌤️ **SHIFT 2 (Siang - Sore)**")
                st.write("**⏰ Jam Kerja:** 10:00 s/d 18:00 WIB (**Fleksibel**)")
                st.write("**🕒 Istirahat:** 11:30 – 12:30 WIB (**Fleksibel**)")

            st.divider()
            st.write("**📅 Hari Kerja:** Senin – Sabtu (Minggu & Libur Nasional Tutup).")
            st.write("**💡 Info:** Cuti Bersama, Operasional kantor tetap berjalan normal kecuali ditentukan lain oleh Owner.")

        st.write("") 

        # --- CARD 2: PENGGAJIAN & APRESIASI (KOMPLIT) ---
        with st.container(border=True):
            st.markdown("#### 💰 SISTEM PENGGAJIAN & APRESIASI KINERJA")
            
            # --- LOGIKA PENENTUAN GAJI (Sesuai Level) ---
            if user_level == "STAFF":
                gapok_display = "Rp 2.000.000"
            elif user_level == "UPLOADER":
                gapok_display = "Rp 1.500.000"
            elif user_level == "ADMIN":
                gapok_display = "Rp 2.500.000"
            else:
                gapok_display = "Rp -, -"

            col_gaji1, col_gaji2 = st.columns(2)
            
            with col_gaji1:
                st.success(f"💵 **Penghasilan Bulanan ({user_level}):**")
                st.markdown(f"**Gaji Pokok:** {gapok_display}")
                st.markdown(f"**Tunjangan Kerja:** Rp 250.000 - Rp 500.000")
                
                st.divider()
                st.markdown("**🌟 Bonus Kinerja:**")
                st.write("- Disesuaikan dengan performa kerja individu.")
                st.write("- Tergantung tercapainya target perusahaan bulan ini.")

            with col_gaji2:
                st.info("⏲️ **Bonus Lembur & Pembayaran:**")
                st.write("**• Senin - Sabtu:** Rp 25.000 / Jam")
                st.write("**• Minggu / Tgl Merah:** Rp 100.000 / hari")
                
                st.divider()
                st.write("**📅 Periode Pembayaran:**")
                st.write("Hak upah, tunjangan, dan bonus disalurkan pada **Tanggal 2 s/d 5** setiap bulannya.")
                st.write("**📊 Struktur:** Gaji Pokok + Tunjangan + Bonus + Lembur.")

            st.warning("⚠️ **Catatan:** Pembayaran dilakukan secara transparan berdasarkan rekap data performa di sistem.")

        st.write("")

        # --- CARD 3: OPERASIONAL & KEAMANAN ASSET (GABUNGAN) ---
        with st.container(border=True):
            st.markdown("#### 🛠️ OPERASIONAL, ALAT KERJA & KEAMANAN ASSET")
            
            c_sop, c_alat = st.columns(2)
            
            with c_sop:
                st.markdown("**📑 Standar Operasional (SOP):**")
                st.write("- SOP kerja berdasarkan posisi (Editor, Uploader, Admin) wajib dilihat di halaman **Area Staff**.")
                st.write("- Seluruh staff wajib mengikuti instruksi teknis yang sudah ditentukan.")
                
                st.markdown("**📱 Penggunaan Smartphone:**")
                st.write("- Diperbolehkan terbatas hanya untuk riset tren, ide cerita, dan koordinasi internal.")
                st.write("- **Batasan Etika:** Dilarang untuk hiburan pribadi (Game/WA Personal) yang mengganggu produktivitas.")

            with c_alat:
                st.error("**🔐 Kerahasiaan & Integritas Data:**")
                st.write("- **Dilarang Keras** menyebarkan rahasia atau data perusahaan ke pihak luar.")
                st.write("- Membagikan akses akun kepada pihak ketiga tanpa izin adalah pelanggaran berat.")
                
                st.markdown("**📉 Efisiensi Resource:**")
                st.write("- Gunakan kuota produksi secara bijak dan terukur guna menghindari pemborosan.")

        with st.container(border=True):
            st.markdown("#### 🧹 PEMELIHARAAN ASET & ETIKA LINGKUNGAN")
            
            c_aset1, c_aset2 = st.columns(2)
            
            with c_aset1:
                st.markdown("**📱 Penanganan Alat Kantor:**")
                st.write("- Letakkan HP di area yang aman, jangan di pinggir meja yang rawan jatuh.")
                st.write("- Rapikan kabel setelah digunakan, dilarang menarik paksa kabel charger dari unit.")
                st.write("- Jika HP/PC terasa panas berlebih (Overheat), wajib diistirahatkan atau hubungi Admin/Owner.")
                st.write("- Kerusakan akibat kelalaian (jatuh/kena air) menjadi tanggung jawab penuh staf yang memegang.")

            with c_aset2:
                st.markdown("**✨ Kebersihan Area Kerja:**")
                st.write("- Wajib bersih dari sampah plastik, sisa makanan, atau kertas yang tidak terpakai.")
                st.write("- Dilarang membawa makanan berat/berkuah ke dekat perangkat elektronik.")
                st.write("- Rapikan kursi dan matikan AC, PC, kipas setelah jam kerja selesai.")
                st.success("💡 **Filosofi:** Kebersihan sebagian dari Iman.")

        with st.container(border=True):
            st.markdown("#### 🤝 Komitmen Bersama")
            st.write("1. Owner berhak melakukan penyesuaian kebijakan operasional kapan saja demi kebaikan tim.")
            st.write("2. Setiap Staff wajib menjaga etika, keamananan dan kebersihan lingkungan.")
            st.write("3. Segala bentuk kendala pekerjaan wajib dikomunikasikan dengan Admin/Owner.")
            
            # Gimmick biar mereka merasa terikat
            st.checkbox("Saya telah membaca, memahami, dan siap mematuhi seluruh peraturan PINTAR MEDIA.", value=True)

        st.caption(f"Terakhir diperbarui: 31 Maret 2026")

    # ==============================================================================
    # TAB 4: KONTRAK KERJA (PINTAR MEDIA - VERSI LEGAL MUTLAK)
    # ==============================================================================
    with tab_kontrak:
        # --- 1. MAPPING & DATABASE LOGIC ---
        staff_mapping = {
            "nissa": "Nisaul Mukaromah Alfiyaeni",
            "lisa": "Salisatu Rohmatus Saodah",
            "icha": "Nissa Pangestuningrum",
            "inggi": "Rizki Retno Inggiani",
            "hani": "Nur Hanifah",
            "dian": "Dian Setya Wardana"
        }
        
        nama_lengkap_staf = staff_mapping.get(user_aktif.lower(), user_aktif.upper())
        periode_skrg = sekarang.strftime('%m-%Y')
        nomor_ahu = "AHU-011181.AH.01.31.2025"
        
        try:
            res_staff = supabase.table("Staff").select("*").eq("Nama", user_aktif.upper()).execute()
            if res_staff.data:
                s_data = res_staff.data[0]
                gaji_pokok = s_data.get("Gaji_Pokok", 0)
                jabatan_db = s_data.get("Jabatan", user_level)
            else:
                gaji_pokok, jabatan_db = 0, user_level
        except:
            gaji_pokok, jabatan_db = 0, user_level

        # --- 2. CEK STATUS TTD BULAN INI ---
        res_ttd = supabase.table("kontrak_staff").select("*").eq("username", user_aktif).eq("periode", periode_skrg).execute()
        
        # --- 3. KONSTRUKSI HTML UNTUK PRINT (FULL TEXT TANPA EDIT) ---
        html_kontrak_full = f"""
        <style>
            @media print {{
                @page {{ size: A4; margin: 15mm; }}
                body {{ margin: 0; padding: 0; background: white; }}
                .a4-container {{ border: none !important; box-shadow: none !important; width: 100% !important; margin: 0 !important; padding: 0 !important; }}
            }}
            .a4-container {{
                background: white; width: 210mm; padding: 20mm; margin: auto; 
                font-family: Arial, sans-serif; color: black; line-height: 1.6; 
                border: 1px solid #eee; box-sizing: border-box;
            }}
        </style>
        <div class="a4-container">
            <table style="width: 100%; border-bottom: 3px solid #000; padding-bottom: 15px; margin-bottom: 30px;">
                <tr>
                    <td style="width: 30%; vertical-align: middle;">
                        <img src="https://raw.githubusercontent.com/pintarkantor-prog/pintarmedia/main/PINTAR.png" style="width: 180px;">
                    </td>
                    <td style="width: 70%; text-align: right; vertical-align: middle;">
                        <h1 style="margin: 0; font-size: 22px; font-weight: bold; text-transform: uppercase;">PT Pintar Digital Kreasi</h1>
                        <p style="margin: 0; font-size: 12px; color: #333;">Creative Content & Digital Media Production</p>
                        <p style="margin: 0; font-size: 10px; color: #666;">SK KEMENKUMHAM: {nomor_ahu}</p>
                    </td>
                </tr>
            </table>

            <h3 style="text-align: center; text-decoration: underline;">SURAT PERJANJIAN KEMITRAAN KERJA</h3>
            <p style="text-align: center; margin-top: -10px; font-size: 14px;">Nomor: {periode_skrg}/PM/KONTRAK/{user_aktif.upper()}</p>

            <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                <tr>
                    <td style="width: 50%; border: 1px solid black; padding: 10px; vertical-align: top; font-size: 13px;">
                        <b>PIHAK KEDUA (MITRA):</b><br>
                        Nama Lengkap: {nama_lengkap_staf}<br>
                        Jabatan: {jabatan_db}<br>
                        <i>Selanjutnya disebut sebagai Penerima Kerja.</i>
                    </td>
                    <td style="width: 50%; border: 1px solid black; padding: 10px; vertical-align: top; font-size: 13px;">
                        <b>PIHAK PERTAMA (OWNER):</b><br>
                        Nama Lengkap: Dian Setya Wardana<br>
                        Perusahaan: PT. PINTAR DIGITAL KREASI<br>
                        <i>Selanjutnya disebut sebagai Pemberi Kerja.</i>
                    </td>
                </tr>
            </table>

            <h4 style="margin-top: 25px; border-bottom: 1px solid #000;">I. PENGHASILAN & PENGGAJIAN</h4>
            <div style="font-size: 13px;">
                1. <b>Gaji Pokok:</b> Rp {int(gaji_pokok):,}<br>
                2. <b>Tunjangan Kerja:</b> Rp 250.000 - Rp 500.000 (Disesuaikan kondisi perusahaan)<br>
                3. <b>Bonus Kinerja:</b> Berdasarkan pencapaian target<br>
                4. <b>Lembur:</b> Hari Normal (25rb/Jam) | Minggu (100rb/7 Jam)<br><br>
                *) Seluruh hak upah, tunjangan, dan bonus disalurkan setiap tanggal 2 s/d 5 melalui sistem transfer bank/e-wallet.
            </div>

            <h4 style="margin-top: 20px; border-bottom: 1px solid #000;">II. PASAL-PASAL KESEPAKATAN KEMITRAAN</h4>
            <div style="font-size: 13px; text-align: justify;">
                <p><b>PASAL 1: STATUS HUBUNGAN KERJA</b><br>
                1. Hubungan hukum antara Pihak Pertama dan Pihak Kedua adalah hubungan <b>Kemitraan Lepas (Freelance/Project-Based)</b>.<br>
                2. Pihak Kedua tidak memiliki status sebagai karyawan tetap, sehingga Pihak Pertama tidak berkewajiban memberikan tunjangan pesangon, atau jaminan sosial di luar kesepakatan tertulis.<br>
                3. Perjanjian ini berlaku selama proyek <b>PINTAR MEDIA</b> berjalan dan performa Pihak Kedua memenuhi standar evaluasi bulanan.</p>

                <p><b>PASAL 2: KLAUSUL REM DARURAT & FORCE MAJEURE</b><br>
                1. Mengingat jenis pekerjaan ini sangat bergantung pada kebijakan platform pihak ketiga (YouTube), Pihak Pertama berhak <b>menghentikan, menunda, atau mengakhiri</b> kemitraan secara sepihak jika terjadi perubahan algoritma atau penurunan tren pasar.<br>
                2. Dalam hal terjadi penghentian proyek sebagaimana dimaksud pada ayat (1), maka Pihak Kedua setuju bahwa pembayaran upah akan dilakukan secara <b>PRO-RATA</b> (Hanya membayar sesuai jumlah hari hingga hari penghentian).<br>
                3. Pihak Kedua membebaskan Pihak Pertama dari segala tuntutan ganti rugi atau pesangon jika proyek dihentikan karena faktor-faktor tersebut di atas.</p>

                <p><b>PASAL 3: KERAHASIAAN & KEKAYAAN INTELEKTUAL</b><br>
                1. Pihak Kedua wajib menjaga kerahasiaan seluruh metode kerja, alur produksi, dan terutama <b>PROMPT AI</b> yang digunakan oleh PINTAR MEDIA.<br>
                2. Pihak Kedua <b>DILARANG KERAS</b> menyebarkan, menjual, atau membocorkan Prompt AI tersebut kepada pihak manapun, baik selama masa kontrak maupun setelah kontrak berakhir.<br>
                3. Seluruh hasil karya berupa Video, Script, Voiceover, dan Aset Digital lainnya adalah milik sah Pihak Pertama.<br>
                4. Pelanggaran terhadap pasal ini akan ditindaklanjuti melalui jalur hukum pidana/perdata dan dikenakan denda materiil sebesar kerugian yang dialami perusahaan.</p>

                <p><b>PASAL 4: TANGGUNG JAWAB ASSET INVENTARIS</b><br>
                1. Pihak Kedua bertanggung jawab penuh atas pemeliharaan Smartphone, PC, atau peralatan kantor lainnya yang dipinjamkan.<br>
                2. Segala bentuk kerusakan fisik (Layar pecah, terkena air, hilang) akibat kelalaian Pihak Kedua wajib diganti rugi secara penuh oleh Pihak Kedua.<br>
                3. Pihak Kedua <b>Dilarang Keras</b> mengubah kredensial akun (Email/Password/Profile) pada akun-akun premium (Google, Gemini, Grok, dll) tanpa izin Admin.<br>
                4. Saat hubungan kemitraan berakhir, Pihak Kedua wajib mengembalikan aset inventaris dalam waktu maksimal <b>2x24 Jam</b> dalam kondisi fungsional.</p>

                <p><b>PASAL 5: ETIKA KERJA & EVALUASI</b><br>
                1. Pihak Kedua wajib mematuhi Jam Operasional yang telah ditentukan (Shift 1 / Shift 2).<br>
                2. Pihak Kedua wajib menjaga peforma pekerjaan sesuai dengan standar yang ditetapkan Admin.<br>
                3. Pihak Kedua dilarang menggunakan perangkat kantor untuk kepentingan pribadi yang dapat menurunkan ritme produktivitas tim.<br>
                4. Pihak Pertama berhak memutuskan kontrak secara sepihak jika Pihak Kedua melanggar etika kerja atau tidak mencapai target minimal selama 6 hari berturut-turut.</p>
            </div>
            <div style="margin-top: 30px; padding: 15px; border: 2px solid green; text-align: center; background-color: #f9fff9;">
                <b style="color: green;">✔ DOKUMEN DISAHKAN SECARA DIGITAL</b><br>
                Nama: {nama_lengkap_staf} | Tanggal: {res_ttd.data[0]['tgl_tanda_tangan'] if len(res_ttd.data)>0 else ''} | Jam: {res_ttd.data[0]['waktu_presisi'] if len(res_ttd.data)>0 else ''}
            </div>
        </div>
        """

        # --- LOGIKA TAMPILAN ---
        if len(res_ttd.data) > 0:
            st.success(f"✔️ **DOKUMEN DISAHKAN DIGITAL - PERIODE {periode_skrg}**")
            if st.button("📄 CETAK KONTRAK KERJA", use_container_width=True, type="primary"):
                st.components.v1.html(f"""
                    <div id="hidden-print" style="display:none;">{html_kontrak_full}</div>
                    <script>
                        var content = document.getElementById('hidden-print').innerHTML;
                        var win = window.open('', '', 'height=700,width=900');
                        win.document.write('<html><head><title>KONTRAK_{user_aktif.upper()}</title></head><body>');
                        win.document.write(content);
                        win.document.write('</body></html>');
                        win.document.close();
                        setTimeout(function(){{ win.print(); win.close(); }}, 500);
                    </script>
                """, height=0)
        else:
            st.warning(f"🚨 **ADMINISTRASI WAJIB:** Anda belum menyetujui kontrak kemitraan periode **{periode_skrg}**.")
            
            # --- TAMPILAN LAYAR (VERSI BERSIH & RAPI) ---
            st.markdown("<h2 style='text-align: center;'>📜 PERJANJIAN KEMITRAAN KERJA</h2>", unsafe_allow_html=True)
            
            st.write("### 🤝 PARA PIHAK")
            c1, c2 = st.columns(2)
            
            with c1:
                # Pihak Kedua pake warna biru (Info)
                st.info("👤 **PIHAK KEDUA (MITRA)**")
                with st.container(border=True):
                    st.write(f"**Nama Lengkap:** \n{nama_lengkap_staf}")
                    st.write(f"**Jabatan:** \n{jabatan_db}")
                    st.caption("Selanjutnya disebut sebagai Penerima Kerja.")

            with c2:
                # Pihak Pertama pake warna hijau (Success)
                st.success("🏢 **PIHAK PERTAMA (OWNER)**")
                with st.container(border=True):
                    st.write(f"**Nama Lengkap:** \nDian Setya Wardana")
                    st.write(f"**Perusahaan:** \nPT. PINTAR DIGITAL KREASI")
                    st.caption("Selanjutnya disebut sebagai Pemberi Kerja.")

            st.write("---")

            # --- CARD 2: PENGHASILAN & PENGGAJIAN (REBORN) ---
            with st.container(border=True):
                st.markdown("### 💰 I. PENGHASILAN & PENGGAJIAN")
                
                # Kita bagi 3 kolom biar gak numpuk ke bawah
                col_angka, col_detail = st.columns([1.2, 2])
                
                with col_angka:
                    # Kotak Gaji Pokok yang Mencolok
                    st.metric(label="💵 GAJI POKOK (NETT)", value=f"Rp {int(gaji_pokok):,}")
                    st.caption("*) Belum termasuk tunjangan & bonus")
                
                with col_detail:
                    # Detail Poin pake Bullet Points asli Streamlit biar simetris
                    st.markdown("**DETAIL KOMPONEN LAINNYA:**")
                    st.write(f"🔹 **Tunjangan Kerja:** Rp 250k - Rp 500k")
                    st.write(f"🔹 **Bonus Kinerja:** Sesuai Pencapaian Target")
                    st.write(f"🔹 **Lembur:** Normal (25rb/Jam) | Minggu (100rb/7 Jam)")
                
                # Footer Penggajian pake info box kecil biar ditekankan
                st.info(f"📅 **JADWAL PAYDAY:** Seluruh upah disalurkan setiap tanggal **2 s/d 5** via Transfer Bank/E-Wallet.")


            # --- CARD 3: PASAL-PASAL KESEPAKATAN (BRUTAL & CLEAN) ---
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center;'>⚖️ PASAL-PASAL KESEPAKATAN KEMITRAAN</h3>", unsafe_allow_html=True)
                st.divider()

                # PASAL 1
                st.info("📜 **PASAL 1: STATUS HUBUNGAN KERJA**")
                st.markdown("""
                1. Hubungan hukum antara Pihak Pertama dan Pihak Kedua adalah hubungan **Kemitraan Lepas (Freelance/Project-Based)**.
                2. Pihak Kedua tidak memiliki status sebagai karyawan tetap, sehingga Pihak Pertama tidak berkewajiban memberikan tunjangan pesangon, atau jaminan sosial di luar kesepakatan tertulis.
                3. Perjanjian ini berlaku selama proyek **PINTAR MEDIA** berjalan dan performa Pihak Kedua memenuhi standar evaluasi bulanan.
                """)
                st.write("")

                # PASAL 2
                st.info("📜 **PASAL 2: KLAUSUL REM DARURAT & FORCE MAJEURE**")
                st.markdown("""
                1. Mengingat jenis pekerjaan ini sangat bergantung pada kebijakan platform pihak ketiga (YouTube), Pihak Pertama berhak **menghentikan, menunda, atau mengakhiri** kemitraan secara sepihak jika terjadi perubahan algoritma atau penurunan tren pasar.
                2. Dalam hal terjadi penghentian proyek sebagaimana dimaksud pada ayat (1), maka Pihak Kedua setuju bahwa pembayaran upah akan dilakukan secara **PRO-RATA** (Hanya membayar sesuai jumlah hari hingga hari penghentian).
                3. Pihak Kedua membebaskan Pihak Pertama dari segala tuntutan ganti rugi atau pesangon jika proyek dihentikan karena faktor-faktor tersebut di atas.
                """)
                st.write("")

                # PASAL 3 - INI YANG PALING GALAK
                st.info("🚨 **PASAL 3: KERAHASIAAN & KEKAYAAN INTELEKTUAL**")
                st.markdown("""
                1. Pihak Kedua wajib menjaga kerahasiaan seluruh metode kerja, alur produksi, dan terutama **PROMPT AI** yang digunakan oleh PINTAR MEDIA.
                2. Pihak Kedua **DILARANG KERAS** menyebarkan, menjual, atau membocorkan Prompt AI tersebut kepada pihak manapun, baik selama masa kontrak maupun setelah kontrak berakhir.
                3. Seluruh hasil karya berupa Video, Script, Voiceover, dan Aset Digital lainnya adalah milik sah Pihak Pertama.
                4. Pelanggaran terhadap pasal ini akan ditindaklanjuti melalui jalur hukum pidana/perdata dan dikenakan denda materiil sebesar kerugian yang dialami perusahaan.
                """)
                st.write("")

                # PASAL 4
                st.info("📜 **PASAL 4: TANGGUNG JAWAB ASSET INVENTARIS**")
                st.markdown("""
                1. Pihak Kedua bertanggung jawab penuh atas pemeliharaan Smartphone, PC, atau peralatan kantor lainnya yang dipinjamkan.
                2. Segala bentuk kerusakan fisik (Layar pecah, terkena air, hilang) akibat kelalaian Pihak Kedua wajib diganti rugi secara penuh oleh Pihak Kedua.
                3. Pihak Kedua **Dilarang Keras** mengubah kredensial akun (Email/Password/Profile) pada akun-akun premium (Google, Gemini, Grok, dll) tanpa izin Admin.
                4. Saat hubungan kemitraan berakhir, Pihak Kedua wajib mengembalikan aset inventaris dalam waktu maksimal **2x24 Jam** dalam kondisi fungsional.
                """)
                st.write("")

                # PASAL 5
                st.info("📜 **PASAL 5: ETIKA KERJA & EVALUASI**")
                st.markdown("""
                1. Pihak Kedua wajib mematuhi Jam Operasional yang telah ditentukan (Shift 1 / Shift 2).
                2. Pihak Kedua wajib menjaga peforma pekerjaan sesuai dengan standar yang ditetapkan Admin.
                3. Pihak Kedua dilarang menggunakan perangkat kantor untuk kepentingan pribadi yang dapat menurunkan ritme produktivitas tim.
                4. Pihak Pertama berhak memutuskan kontrak secara sepihak jika Pihak Kedua melanggar etika kerja atau tidak mencapai target minimal selama 6 hari berturut-turut.
                """)

            # --- CARD 4: DIGITAL SIGNATURE AREA (SANGAR) ---
            with st.container(border=True):
                st.markdown("### 🖋️ PENGESAHAN DIGITAL")
                st.write(f"Saya yang bertanda tangan di bawah ini, menyatakan telah membaca, memahami, dan menyetujui seluruh ketentuan kemitraan **PINTAR MEDIA** untuk periode **{periode_skrg}**.")
                
                # Kita bikin checkbox-nya lebih mencolok
                st.divider()
                setuju = st.checkbox(f"**SAYA, {nama_lengkap_staf.upper()}, MENYATAKAN SETUJU TANPA PAKSAAN.**")
                
                # Tombol tanda tangan dengan logika proteksi
                if st.button("🖋️ TANDA TANGANI KONTRAK SEKARANG", 
                             disabled=not setuju, 
                             use_container_width=True, 
                             type="primary"): # Pakai type="primary" biar warnanya beda sendiri
                    
                    with st.status("Sedang mengesahkan dokumen digital...", expanded=True) as status:
                        try:
                            # 1. Siapkan Payload
                            payload = {
                                "username": user_aktif, 
                                "nama_staff": nama_lengkap_staf, 
                                "periode": periode_skrg,
                                "tgl_tanda_tangan": sekarang.strftime('%d %B %Y'), 
                                "waktu_presisi": sekarang.strftime('%H:%M:%S')
                            }
                            
                            # 2. Tembak ke Database
                            st.write("📝 Mencatat rekam jejak digital ke database...")
                            supabase.table("kontrak_staff").insert(payload).execute()
                            
                            # 3. Kirim Notif WA (Fonnte)
                            st.write("📲 Mengirimkan notifikasi pengesahan ke grup...")
                            pesan_legal = (
                                f"✅ *KONTRAK DISAHKAN DIGITAL*\n\n"
                                f"Staff: *{nama_lengkap_staf}*\n"
                                f"Periode: *{periode_skrg}*\n"
                                f"Waktu: {sekarang.strftime('%H:%M:%S')} WIB\n\n"
                                f"Status: _Telah menyetujui seluruh draf kontrak PINTAR MEDIA tanpa paksaan._"
                            )
                            kirim_notif_wa(pesan_legal)
                            
                            status.update(label="✅ Pengesahan Berhasil! Memuat ulang...", state="complete", expanded=False)
                            st.toast("Kontrak Berhasil Disahkan!", icon="🚀")
                            
                            # Kasih jeda dikit biar staf lo liat suksesnya
                            import time
                            time.sleep(2)
                            st.rerun()
                            
                        except Exception as e:
                            status.update(label="❌ Gagal mengesahkan!", state="error")
                            st.error(f"Terjadi kesalahan sistem: {e}")

        # --- 4. KHUSUS OWNER: MONITORING ADMINISTRASI (CLEAN & PROFESSIONAL) ---
        if user_level == "OWNER":
            st.divider()
            st.markdown(f"### 📊 MONITORING ADMINISTRASI ({periode_skrg})")
            
            # 1. Data Retrieval
            res_all = supabase.table("kontrak_staff").select("username").eq("periode", periode_skrg).execute()
            sudah_ttd = [x['username'].lower() for x in res_all.data]
            staf_wajib = ["nissa", "lisa", "icha", "inggi", "hani"]
            belum_ttd = [s for s in staf_wajib if s not in sudah_ttd]
            
            # 2. Stats Summary
            total_staf = len(staf_wajib)
            jumlah_sudah = len(sudah_ttd)
            progres_persen = jumlah_sudah / total_staf
            
            c_stats1, c_stats2 = st.columns([3, 1])
            with c_stats1:
                st.write(f"**Status Kepatuhan: {jumlah_sudah} dari {total_staf} Staf**")
                st.progress(progres_persen)
            with c_stats2:
                st.metric("Kepatuhan", f"{int(progres_persen * 100)}%")

            st.write("")

            # 3. Kondisi Tampilan (NO EFEK LAYAR)
            if belum_ttd:
                c_list, c_tagih = st.columns([2, 1])
                with c_list:
                    st.error(f"⚠️ **BELUM TANDA TANGAN:**\n\n" + "\n".join([f"- {s.upper()} ({staff_mapping.get(s, s)})" for s in belum_ttd]))
                
                with c_tagih:
                    if st.button("📣 TAGIH WA GRUP", use_container_width=True, type="primary"):
                        nama_tagihan = ", ".join([staff_mapping.get(s, s) for s in belum_ttd])
                        pesan_tagihan = (
                            f"📢 *REMINDER ADMINISTRASI PINTAR MEDIA*\n\n"
                            f"Kepada: *{nama_tagihan.upper()}*\n\n"
                            f"Anda terdeteksi BELUM menandatangani kontrak periode *{periode_skrg}*.\n"
                            f"Segera sahkan dokumen di Dashboard PINTAR MEDIA. Terima kasih."
                        )
                        kirim_notif_wa(pesan_tagihan)
                        st.info("Pesan tagihan terkirim.")
            else:
                # VERSI BERSIH: TANPA BALON, TANPA SALJU, TANPA TOAST
                with st.container(border=True):
                    st.markdown("""
                    <div style="text-align: center; padding: 20px;">
                        <h2 style="color: #10b981; margin: 0;">✅ STATUS: ADMINISTRASI CLEAN</h2>
                        <p style="color: #888; font-size: 14px;">Seluruh staf telah melengkapi tanda tangan kontrak periode ini.</p>
                    </div>
                    """, unsafe_allow_html=True)
