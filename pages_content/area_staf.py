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
    # TAB 2: PANDUAN KERJA (BERDASARKAN AKTIVITAS / CARA KERJA)
    # ==============================================================================
    with tab_panduan:
        st.markdown(f"#### 📖 Pusat Panduan Kerja: PINTAR MEDIA")
        st.info("💡 **INFO:** Klik setiap judul panduan di bawah ini untuk melihat langkah-langkah teknisnya secara lengkap.")

        # --- 1. PANDUAN SETOR TUGAS ---
        with st.expander("📝 1. PANDUAN SETOR & PENYERAHAN TUGAS", expanded=True):
            col_s1, col_s2 = st.columns(2)
            with col_s1:
                st.markdown("**📽️ Penyerahan Stok Harian (Offline):**")
                st.write("1. Pastikan video sudah sesuai **SOP Kualitas** (1080p, 9:16).")
                st.write("2. Nama file wajib: `TGL_NAMA_JUDUL.mp4`.")
                st.write("3. Masukkan file ke **Flashdisk (FD)** yang tersedia di kantor.")
                st.write("4. Serahkan FD ke **Admin** untuk proses pemindahan ke unit HP.")
            with col_s2:
                st.markdown("**🚀 Penyerahan Tugas Khusus (Online):**")
                st.write("1. Upload file video ke **Google Drive** kantor.")
                st.write("2. Pastikan akses link sudah **'Anyone with the link'** (Bisa diakses siapa saja).")
                st.write("3. Buka **Tab TUGAS KERJA** di aplikasi ini.")
                st.write("4. Cari ID Tugas Anda, klik **🔍 Buka Detail**, tempel link GDrive, lalu klik **SETOR**.")

        # --- 2. PANDUAN AMANIN AKUN & UNIT ---
        with st.expander("🔐 2. PANDUAN KEAMANAN AKUN GOOGLE & UNIT HP"):
            c_sec1, c_sec2 = st.columns(2)
            with c_safe1:
                st.markdown("**🛡️ Proteksi Akun:**")
                st.write("- **Dilarang Keras** login akun YouTube kantor di perangkat pribadi (Laptop/HP Sendiri).")
                st.write("- Jika muncul notifikasi 'Perangkat Tidak Dikenal', segera ambil screenshot dan lapor Admin.")
                st.write("- Jangan pernah membagikan **Prompt AI** rahasia perusahaan ke luar grup WA Kerja.")
            with c_safe2:
                st.error("**⚠️ Kasus Verifikasi 2 Langkah:**")
                st.write("Jika HP meminta kode OTP atau menekan angka verifikasi:")
                st.write("1. **JANGAN** asal tekan angka.")
                st.write("2. **JANGAN** isi kode sembarangan.")
                st.write("3. Langsung teriak atau panggil Owner/Admin untuk verifikasi fisik.")

        # --- 3. PANDUAN UPLOAD & RITUAL ALGORITMA ---
        with st.expander("📲 3. PANDUAN UPLOAD & RITUAL ALGORITMA (ANTI-SPAM)"):
            st.markdown("**⏰ Jadwal Upload:** `10:00` | `14:00` | `19:00` (Wajib Tepat Waktu!)")
            st.divider()
            st.markdown("**🔄 Ritual 'Pemanasan' YouTube:**")
            st.write("1. **Sebelum Upload:** Buka aplikasi YT, tonton minimal 2-3 video Shorts orang lain (pancing aktivitas manusia).")
            st.write("2. **Proses Upload:** Pilih Thumbnail yang paling kontras/fokus ke karakter. Judul & Deskripsi unik.")
            st.write("3. **Setelah Upload:** Jangan langsung tutup aplikasi! Tonton 1-2 video lagi, baru kembali ke menu utama HP.")
            st.write("4. **Maintenance:** Hapus file video di galeri **DAN** di folder sampah/trash HP setelah upload sukses.")

        # --- 4. PANDUAN PERAWATAN PERANGKAT ---
        with st.expander("⚙️ 4. PANDUAN PERAWATAN PERANGKAT (DEVICE MAINTENANCE)"):
            c_dev1, c_dev2 = st.columns(2)
            with c_dev1:
                st.markdown("**🧹 Pembersihan Sistem (2 Hari Sekali):**")
                st.write("- **Restart HP:** Biar sistem segar dan tidak berat.")
                st.write("- **Clear Chat:** Hapus pesan-pesan tidak penting di WA/Pesan HP.")
                st.write("- **Update App:** Cek Playstore, pastikan YouTube versi terbaru.")
            with col_dev2:
                st.markdown("**⚡ Manajemen Daya & Data:**")
                st.write("- Pastikan HP selalu tercolok charger (Dilarang mati karena lowbat).")
                st.write("- Cek sisa kuota di HP secara berkala via aplikasi provider.")
                st.write("- Lapor Admin jika unit HP terasa panas berlebih.")
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
