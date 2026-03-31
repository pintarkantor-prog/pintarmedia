import streamlit as st
import pandas as pd
from modules import database
import time
from datetime import datetime
import pytz
import requests

# ==============================================================================
# NOTIFIKASI WA (FONNTE)
# ==============================================================================
def kirim_notif_wa(pesan):
    token = "f4CApLBAJDTPrVHHZCDF"
    target = "120363407726656878@g.us"
    url = "https://api.fonnte.com/send"
    payload = {'target': target, 'message': pesan, 'countryCode': '62'}
    headers = {'Authorization': token}
    try: requests.post(url, data=payload, headers=headers, timeout=5)
    except: pass

def tampilkan_area_staf():
    # --- 1. SETUP IDENTITAS ---
    user_aktif = st.session_state.get("user_aktif", "User").upper()
    user_level = st.session_state.get("user_level", "STAFF").upper()
    tz = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz)

    # --- 2. TABS MENU ---
    tab_tugas, tab_panduan, tab_peraturan, tab_kontrak = st.tabs([
        "📝 TUGAS KERJA", "📖 PANDUAN KERJA", "⚖️ PERATURAN KERJA", "📜 KONTRAK KERJA"
    ])

    # ==============================================================================
    # TAB 1: TUGAS KERJA
    # ==============================================================================
    with tab_tugas:
        # --- A. RUTINITAS (CHECKLIST) ---
        st.markdown(f"#### 🕒 Rutinitas Harian: {user_aktif}")
        with st.container(border=True):
            if user_level == "STAFF": # EDITOR
                st.markdown("- [ ] Produksi min. 3 video AI / hari\n- [ ] QC Mandiri Watermark & Subtitle")
            elif user_level == "UPLOADER": # LISA
                st.markdown("- [ ] Upload jadwal Jam 10, 14, 19\n- [ ] Optimasi SEO & Balas Komentar")
            elif user_level == "ADMIN": # INGGI
                st.markdown("- [ ] QC Setoran Editor\n- [ ] Update Data Report Harian")
            else:
                st.write("Sistem Monitoring Owner Aktif.")

        st.divider()

        # --- B. PANEL OWNER (KIRIM TUGAS BARU) ---
        if user_level == "OWNER":
            with st.expander("✨ **KIRIM TUGAS KHUSUS BARU**", expanded=False):
                with st.form("form_tugas_baru", clear_on_submit=True):
                    col1, col2 = st.columns([2, 1])
                    instr = col1.text_area("Instruksi Tugas")
                    staf = col2.selectbox("Pilih Staf", ["ICHA", "LISSA", "INGGI", "NISSA"])
                    if st.form_submit_button("🚀 KIRIM KE EDITOR", use_container_width=True):
                        if instr:
                            # ID UNIK (Misal: T0331...)
                            new_kode = f"T{sekarang.strftime('%m%d%H%M%S')}"
                            database.supabase.table("Tugas").insert({
                                "ID": new_kode, "Staf": staf, "Instruksi": instr, "Status": "PROSES", "Deadline": sekarang.strftime("%Y-%m-%d")
                            }).execute()
                            kirim_notif_wa(f"🔔 *TUGAS BARU*\n👤 *Untuk:* {staf}\n📝 *Detail:* {instr}\n🆔 *ID:* {new_kode}")
                            st.success(f"Tugas {new_kode} Terkirim!"); time.sleep(1); st.rerun()

        # --- C. AMBIL & FIX COLUMN ID (SILET VERSION) ---
        df_raw = database.ambil_data("Tugas")
        if not df_raw.empty:
            df_t = df_raw.copy()
            
            # PAKSA GANTI NAMA: Supaya kolom 'ID' (teks) tidak bentrok dengan 'id' (angka)
            # Kita rename kolom ke-2 (ID besar) menjadi 'KODE_TUGAS' agar UNIK
            if 'ID' in df_t.columns:
                df_t = df_t.rename(columns={'ID': 'KODE_TUGAS'})
            
            # Sekarang standarisasi semua ke UPPER
            df_t.columns = [str(c).strip().upper() for c in df_t.columns]

            # --- D. TUGAS AKTIF (CARD 2 KOLOM) ---
            st.markdown("#### ⚡ Progres Tugas Aktif")
            status_aktif = ['PROSES', 'WAITING QC', 'REVISI']
            
            if user_level == "OWNER":
                mask_aktif = df_t['STATUS'].isin(status_aktif)
            else:
                mask_aktif = (df_t['STAF'].str.upper() == user_aktif) & (df_t['STATUS'].isin(status_aktif))
            
            data_aktif = df_t[mask_aktif].sort_values(by="KODE_TUGAS", ascending=False).to_dict('records')

            if not data_aktif:
                st.caption("Tidak ada tugas khusus yang sedang berjalan.")
            else:
                for i in range(0, len(data_aktif), 2):
                    cols = st.columns(2)
                    for j in range(2):
                        if i + j < len(data_aktif):
                            t = data_aktif[i + j]
                            # GUNAKAN KODE_TUGAS (Hasil rename dari ID besar)
                            k_id = t.get('KODE_TUGAS', 'ERROR')
                            
                            with cols[j]:
                                with st.container(border=True):
                                    c_ava, c_txt = st.columns([1, 4])
                                    c_ava.image("https://cdn-icons-png.flaticon.com/512/149/149071.png", width=50)
                                    with c_txt:
                                        # DI SINI KITA PAKAI K_ID (T0331...)
                                        st.markdown(f"**{t['STAF']}** | <span style='color:#1d976c;'>ID: {k_id}</span>", unsafe_allow_html=True)
                                        icon = "🟡" if t['STATUS'] == "WAITING QC" else "🔴" if t['STATUS'] == "REVISI" else "🟢"
                                        st.markdown(f"{icon} `{t['STATUS']}`")
                                    
                                    olah = st.toggle("🔍 Buka Detail", key=f"tgl_{k_id}")
                                    if olah:
                                        st.divider()
                                        st.markdown(f"**INSTRUKSI:** \n{t['INSTRUKSI']}")
                                        
                                        if user_level != "OWNER":
                                            if t['STATUS'] != "WAITING QC":
                                                link = st.text_input("Link Hasil GDrive", key=f"in_{k_id}")
                                                if st.button("🚀 SETOR", key=f"btn_{k_id}", use_container_width=True):
                                                    if "http" in link:
                                                        database.supabase.table("Tugas").update({"STATUS": "WAITING QC", "LINK_HASIL": link}).eq("ID", k_id).execute()
                                                        kirim_notif_wa(f"📤 *SETORAN*\n👤 *Dari:* {user_aktif}\n🆔 *ID:* {k_id}")
                                                        st.rerun()
                                        else:
                                            if t.get("LINK_HASIL"):
                                                st.link_button("🚀 BUKA VIDEO (QC)", t['LINK_HASIL'], use_container_width=True)
                                                st.divider()
                                                cat_admin = st.text_area("Catatan Admin:", key=f"cat_{k_id}", placeholder="Alasan Revisi/Batal...")
                                                b1, b2, b3 = st.columns(3)
                                                
                                                if b1.button("🟢 ACC", key=f"acc_{k_id}", use_container_width=True):
                                                    database.supabase.table("Tugas").update({"Status": "FINISH"}).eq("ID", k_id).execute()
                                                    kirim_notif_wa(f"✅ *TUGAS ACC*\n🆔 *ID:* {k_id}")
                                                    st.rerun()
                                                
                                                if b2.button("🔴 REV", key=f"rev_{k_id}", use_container_width=True):
                                                    if cat_admin:
                                                        database.supabase.table("Tugas").update({"Status": "REVISI", "CATATAN_REVISI": cat_admin}).eq("ID", k_id).execute()
                                                        kirim_notif_wa(f"⚠️ *REVISI TUGAS*\n👤 *Editor:* {t['STAF']}\n🆔 *ID:* {k_id}\n📝 *Catatan:* {cat_admin}")
                                                        st.rerun()
                                                    else: st.error("Isi alasan revisi!")

                                                if b3.button("🚫 BATAL", key=f"can_{k_id}", use_container_width=True):
                                                    if cat_admin:
                                                        database.supabase.table("Tugas").update({"Status": "CANCELED", "CATATAN_REVISI": cat_admin}).eq("ID", k_id).execute()
                                                        kirim_notif_wa(f"🚫 *TUGAS BATAL*\n🆔 *ID:* {k_id}\n📝 *Alasan:* {cat_admin}")
                                                        st.rerun()
                                                    else: st.error("Isi alasan batal!")

            # --- E. ARSIP TUGAS ---
            st.divider()
            with st.expander("📂 RIWAYAT & ARSIP TUGAS", expanded=False):
                status_arsip = ['FINISH', 'CANCEL', 'CANCELED', 'BATAL']
                mask_arsip = df_t['STATUS'].isin(status_arsip) if user_level == "OWNER" else (df_t['STAF'].str.upper() == user_aktif) & (df_t['STATUS'].isin(status_arsip))
                df_arsip = df_t[mask_arsip].sort_values(by="KODE_TUGAS", ascending=False)
                if df_arsip.empty: st.info("Belum ada riwayat.")
                else:
                    # Menampilkan ID besar (KODE_TUGAS) di tabel arsip
                    st.dataframe(df_arsip[['KODE_TUGAS', 'STAF', 'INSTRUKSI', 'STATUS']], use_container_width=True, hide_index=True)
                    
    # ==============================================================================
    # TAB 2: PANDUAN KERJA
    # ==============================================================================
    with tab_panduan:
        st.markdown("#### 📖 SOP Operasional Produksi")
        with st.expander("1. Cara Login & Amankan Akun"):
            st.write("- Gunakan unit HP sesuai slot.\n- Pastikan IP stabil.\n- Lapor jika verifikasi muncul.")
        with st.expander("2. Alur Produksi Video AI"):
            st.write("- Gunakan prompt PINTAR AI LAB.\n- Pasang watermark.\n- Upload sesuai jadwal.")

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
