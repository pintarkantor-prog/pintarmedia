import streamlit as st
import pandas as pd
from modules import database
import time
from datetime import datetime
import pytz
import requests

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
                "Jika stok harian, tanpa perlu kirim tugas ( langsung serahkan hasil ke Admin via FD ).",
                "Jika ada tugas khusus dari owner, wajib setor hasil tugas via Form Tugas Khusus."
            ],
            "sop": [
                "**Kualitas:** Minimal 1080p Full HD.",
                "**Ratio:** Format 9:16 ( Vertical ).",
                "**Durasi:** Disesuaikan kebutuhan.",
                "**Nama file video:** TGL_NAMA_JUDUL.mp4"
            ]
        },
        "UPLOADER": {
            "judul": "UPLOADER", "ikon": "📲",
            "rutinitas": [
                "Upload konten harian sesuai jadwal.",
                "Hapus file video yang sudah di Upload ( termasuk di folder sampah ).",
                "Koordinasi dengan Admin terkait stok video di HP.",
                "Isi daya setiap HP ( Jangan sampai lowbat ).",
                "Hapus pesan di HP, Restart HP, Update Aplikasi YT secara berkala ( 2 hari sekali )."
            ],
            "sop": [
                "Upload tepat waktu sesuai jadwal yang tersedia.",
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
                        st.markdown(f"### 📌 Rutinitas Harian {data['judul']}")
                        for r in data['rutinitas']: st.markdown(f"✅ {r}")
                with c2:
                    with st.container(border=True):
                        st.markdown(f"### 🛠️ Standar Operasional Kerja")
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
                            # ID UNIK (T0331...)
                            new_id_gede = f"T{sekarang.strftime('%m%d%H%M%S')}"
                            database.supabase.table("Tugas").insert({
                                "ID": new_id_gede, "Staf": staf_tujuan, "Instruksi": instr, "Status": "PROSES", "Deadline": sekarang.strftime("%Y-%m-%d")
                            }).execute()
                            kirim_notif_wa(f"🔔 *TUGAS BARU*\n👤 *Untuk:* {staf_tujuan}\n📝 *Detail:* {instr}\n🆔 *ID:* {new_id_gede}")
                            st.success(f"Tugas {new_id_gede} Terkirim!"); time.sleep(1); st.rerun()

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
                                            if status != "WAITING QC":
                                                l_in = st.text_input("Link GDrive", key=f"in_{id_gede}")
                                                if st.button("🚀 SETOR", key=f"btn_{id_gede}", use_container_width=True):
                                                    if "drive.google.com" in l_in:
                                                        database.supabase.table("Tugas").update({
                                                            "Status": "WAITING QC", "Link_Hasil": l_in, "Waktu_Kirim": sekarang.strftime("%d/%m/%Y %H:%M")
                                                        }).eq("ID", id_gede).execute()
                                                        kirim_notif_wa(f"📤 *SETORAN*\n👤 *Dari:* {user_aktif}\n🆔 *ID:* {id_gede}")
                                                        st.rerun()

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
            st.markdown("### 🎬 PANDUAN PRODUKSI & SETOR TUGAS (EDITOR)")
            
            # --- CARD 1: RUTINITAS (FULL WIDTH) ---
            with st.container(border=True):
                st.markdown("#### 1️⃣ Rutinitas & Koordinasi Harian:")
                st.write("- Selalu koordinasi dengan Admin buat tau stok video mana yang mau habis.")
                st.write("- Wajib bikin video harian sesuai kebutuhan stok kantor.")
                st.write("- Dahulukan membuat stok untuk Konten yang stok videonya paling sedikit.")
                st.success(f"📌 **Format Nama Wajib:** `{sekarang.strftime('%d%m')}_JUDUL_FILE.mp4` (Contoh: {sekarang.strftime('%d%m')}_MASJID_NENEK.mp4)")
            
            st.write("") # Spacing sedikit

            # --- HEADER JALUR PENYERAHAN ---
            st.markdown("#### 2️⃣ Alur Penyerahan Hasil Kerja")
            
            col_jalur1, col_jalur2 = st.columns(2)
            
            # --- CARD 2: JALUR A (KIRI) ---
            with col_jalur1:
                with st.container(border=True):
                    st.info("📂 **JALUR A: STOK HARIAN (OFFLINE)**")
                    st.markdown("**Target:** Video rutin harian untuk stok HP.")
                    st.markdown("**Langkah Kerja:**")
                    st.write("- **Tidak perlu** input data ke sistem/web ini.")
                    st.write("- Copy file video langsung dari PC ke **Flashdisk (FD)**.")
                    st.write("- Pastikan file tercopy sempurna sebelum mencabut FD.")
                    st.write("- Serahkan FD ke **Admin** untuk proses QC & pindah ke folder Stok.")

            # --- CARD 3: JALUR B (KANAN) ---
            with col_jalur2:
                with st.container(border=True):
                    st.success("🚀 **JALUR B: TUGAS KHUSUS (ONLINE)**")
                    st.markdown("**Target:** Instruksi khusus dari Owner di Tab Tugas.")
                    st.markdown("**Langkah Kerja:**")
                    st.write("- Upload file ke **Google Drive** (Folder Project).")
                    st.write("- Setting link ke: *'Anyone with the link'*.")
                    st.write("- Buka Tab **TUGAS KERJA** di web ini, cari ID tugasmu.")
                    st.write("- Klik **🔍 Buka Detail**, tempel link G-Drive, lalu klik **SETOR**.")

            # --- FOOTER WARNING ---
            st.write("")
            st.warning("⚠️ Informasi panduan ini bersifat sebagai pengingat, silahkan tanya ke Admin/Owner untuk penjelasan lengkap!")

        # --- FUNGSI MODULAR PANDUAN UPLOADER (MODEL CARD SYSTEM) ---
        def panduan_ritual_upload():
            st.markdown("### 📲 RITUAL UPLOAD & ANTI-SPAM")
            
            # --- CARD 1: RITUAL PEMANASAN ---
            with st.container(border=True):
                st.warning("⚠️ **Pemanasan Akun (Ritual Wajib):**")
                st.write("- **Sebelum Upload:** Buka aplikasi YT, tonton video Shorts orang lain minimal 15 detik (pancing aktivitas manusia).")
                st.write("- **Setelah Upload:** Jangan langsung tutup aplikasi! Tonton lagi 1-2 video orang lain sebentar baru keluar/close aplikasi.")
                st.info("💡 **Tujuan:** Biar akun dianggap 'Manusia' oleh sistem YouTube dan video lebih gampang masuk rekomendasi (FYP).")

            st.write("") # Spacing

            # --- CARD 2: OPTIMASI KONTEN ---
            with st.container(border=True):
                st.markdown("#### 📝 Langkah Optimasi & Jadwal")
                st.write("- Wajib upload tepat waktu sesuai jadwal upload harian.")
                st.write("- Wajib pilih Thumbnail yang paling bikin penasaran, kaget, atau fokus ke karakter utama.")
                st.write("- Judul & Deskripsi wajib mengikuti arahan WA Kerja atau kembangkan secara manual pada konten tertentu.")
                st.write("- Selesai upload, pastikan video sudah muncul di tab 'Your Videos' sebelum berpindah ke HP lain.")

        def panduan_rawat_hp():
            st.markdown("### ⚙️ MAINTENANCE UNIT HP")
            
            col_hp1, col_hp2 = st.columns(2)
            
            # --- CARD 3: KEBERSIHAN DATA (KIRI) ---
            with col_hp1:
                with st.container(border=True):
                    st.markdown("**🧹 Pembersihan Memori:**")
                    st.write("- Segera hapus file video yang sudah sukses di-upload agar memori tidak penuh.")
                    st.write("- Wajib cek folder 'Recently Deleted / Sampah' di galeri dan kosongkan secara berkala.")
                    st.write("- Hapus pesan sms atau chat di HP yang sudah tidak diperlukan.")

            # --- CARD 4: PERFORMA UNIT (KANAN) ---
            with col_hp2:
                with st.container(border=True):
                    st.markdown("**⚡ Performa & Daya:**")
                    st.write("- Wajib **Restart HP** dan Update aplikasi YT secara berkala (minimal 2 hari sekali).")
                    st.write("- Pastikan HP selalu standby dicolok charger. **Jangan sampai Lowbat atau mati total!**")
                    st.write("- Jika ada kendala terkait HP atau Channel, segera laporkan ke Admin/Owner.")

        # --- FUNGSI MODULAR PANDUAN ADMIN (MODEL CARD SYSTEM) ---
        def panduan_kontrol_admin():
            st.markdown("### 📊 MANAJEMEN DATABASE & KONTROL")
            
            # --- CARD 1: PRODUKSI & STOK CHANNEL (PABRIK CHANNEL) ---
            with st.container(border=True):
                st.markdown("#### 🏗️ Produksi & Stok Channel Standby")
                st.info("💡 **Tugas Utama:** Admin adalah penyedia akun agar operasional tidak berhenti.")
                st.write("- **Hunting Akun:** Mencari akun Google fresh/tua untuk bahan channel baru.")
                st.write("- **Ternak Channel:** Membuat channel-channel baru secara berkala untuk stok standby.")
                st.write("- **Quality Control:** Memastikan channel standby sudah siap (setting dasar YT sudah oke).")
                st.write("- **Update Database:** Segera masukkan data channel baru ke sistem agar siap digunakan.")

            st.write("") # Spacing

            # --- CARD 2: KONTROL OPERASIONAL ---
            with st.container(border=True):
                st.markdown("#### 🔄 Rutinitas & Rekap Harian")
                st.write("- **Monitoring Channel:** Memastikan channel standby selalu update statusnya (siap/digunakan).")
                st.write("- **Rekap Unit:** Update dan rekap database HP (Hapus sesi login lama agar aman).")
                st.write("- **Stok Video:** Update stok video di masing-masing HP secara berkala.")
                st.write("- **Efisiensi:** Memastikan seluruh kegiatan kantor berjalan efektif tanpa hambatan teknis.")

            st.write("") # Spacing

            # --- CARD 3: STANDAR OPERASIONAL (SOP) ---
            st.markdown("#### 📝 Standar Operasional Admin")
            col_adm1, col_adm2 = st.columns(2)
            
            with col_adm1:
                with st.container(border=True):
                    st.markdown("🔍 **Pengecekan Logistik**")
                    st.write("- **Cek Fisik:** Rutin cek kuota internet, listrik, dan kondisi unit HP.")
                    st.write("- **Real-Time:** Data Channel wajib di-update secara real-time (No Delay).")
                    st.write("- **Akurasi:** Akurasi data channel wajib 100% (No Error).")

            with col_adm2:
                with st.container(border=True):
                    st.success("💰 **Keuangan & Koordinasi**")
                    st.write("- **Arus Kas:** Mencatat setiap pengeluaran operasional (beli akun, bensin, dll).")
                    st.write("- **Koordinasi Tim:** Wajib cerewet ingetin Editor soal stok dan Uploader soal jadwal.")
                    st.write("- **Akurasi Keuangan:** Data keuangan tidak boleh ada selisih sedikit pun.")

            st.warning("⚠️ Admin adalah jantung data kantor. Kelalaian data Admin berakibat fatal pada performa seluruh tim!")

        # --- LOGIKA PENAMPILAN (OWNER & ADMIN PAKE RADIO) ---
        if user_level in ["OWNER", "ADMIN"]:            
            # --- GANTI KE RADIO HORIZONTAL ---
            pilihan = st.radio(
                "Pilih Panduan Divisi:", 
                ["EDITOR", "UPLOADER", "ADMIN"], 
                horizontal=True,
                label_visibility="collapsed" # Biar lebih rapi, judulnya kita umpetin
            )
            
            st.divider()
            
            # Eksekusi sesuai pilihan radio
            if pilihan == "EDITOR": 
                panduan_setor_tugas() # Pake fungsi detail yang kita buat tadi
            elif pilihan == "UPLOADER": 
                panduan_ritual_upload()
                panduan_rawat_hp()
            elif pilihan == "ADMIN": 
                panduan_kontrol_admin()
            
        # Panduan Keamanan (Wajib buat SEMUA ORANG)
        st.divider()
        with st.expander("🔐 PROSEDUR AMANIN AKUN GOOGLE"):
            c1, c2 = st.columns(2)
            c1.write("- Dilarang login di perangkat pribadi.")
            c1.write("- JANGAN share Prompt AI ke luar Grup WA.")
            c2.error("Jika muncul OTP/Verifikasi: JANGAN ditekan! Segera panggil Owner/Admin.")
                
    # ==============================================================================
    # TAB 3: PERATURAN KERJA
    # ==============================================================================
    with tab_peraturan:
        st.warning("⚠️ Peraturan Kedisiplinan")
        st.markdown("1. Target harian wajib terpenuhi.\n2. Dilarang sebar prompt perusahaan.\n3. Wajib lapor progres.")

    # ==============================================================================
    # TAB 4: KONTRAK KERJA
    # ==============================================================================
    with tab_kontrak:
        st.markdown(f"#### 📜 Kontrak: {user_aktif}")
        if st.button("📄 Lihat Ringkasan Kontrak"):
            st.write("- **Posisi:** Creator AI\n- **Status:** Aktif")
