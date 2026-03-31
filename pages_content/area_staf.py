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
    # TAB 1: TUGAS KERJA (Berdasarkan Level)
    # ==============================================================================
    with tab_tugas:
        st.markdown(f"### 📋 Papan Tugas: {user_aktif}")
        
        # --- A. LOGIKA TUGAS HARIAN BERDASARKAN LEVEL ---
        with st.container(border=True):
            if user_level == "STAFF": # ICHA & NISSA (Staff Editor)
                st.markdown("#### 🎬 Tugas Harian Editor")
                st.write("- [ ] Produksi minimal 3 video AI per hari.")
                st.write("- [ ] Pastikan watermark 'PINTAR DIGITAL' terpasang.")
                st.write("- [ ] Setor link GDrive di kolom 'Tugas Khusus' jika ada instruksi.")
                
            elif user_level == "ADMIN": # INGGI (Admin)
                st.markdown("#### ⚙️ Tugas Harian Admin")
                st.write("- [ ] Kontrol kualitas (QC) video yang disetor Editor.")
                st.write("- [ ] Update status akun di Database Channel.")
                st.write("- [ ] Pastikan slot HP terisi sesuai jadwal.")
                
            elif user_level == "UPLOADER": # LISA (Staff Uploader)
                st.markdown("#### 🚀 Tugas Harian Uploader")
                st.write("- [ ] Upload video ke YouTube/TikTok (Jam 10, 14, 19).")
                st.write("- [ ] Optimasi Judul & Deskripsi sesuai riset Lab.")
                st.write("- [ ] Balas komentar dan bangun interaksi akun.")
            
            elif user_level == "OWNER":
                st.success("👑 Anda Login sebagai Owner. Pantau semua progres tim di bawah.")

        st.divider()

        # --- B. PANEL OWNER (KIRIM TUGAS KHUSUS) ---
        if user_level == "OWNER":
            with st.expander("✨ **KIRIM INSTRUKSI TUGAS KHUSUS**", expanded=False):
                with st.form("form_kirim_tugas", clear_on_submit=True):
                    col_a, col_b = st.columns([2, 1])
                    instruksi = col_a.text_area("Detail Instruksi", placeholder="Tulis tugas tambahan...")
                    staf_tujuan = col_b.selectbox("Pilih Staf", ["ICHA", "LISSA", "INGGI", "NISSA"])
                    
                    if st.form_submit_button("🚀 KIRIM TUGAS", use_container_width=True):
                        if instruksi:
                            t_id = f"T{sekarang.strftime('%m%d%H%M%S')}"
                            database.supabase.table("Tugas").insert({
                                "ID": t_id, "STAF": staf_tujuan, "INSTRUKSI": instruksi, "STATUS": "PROSES", "DEADLINE": sekarang.strftime("%Y-%m-%d")
                            }).execute()
                            kirim_notif_wa(f"🔔 *TUGAS KHUSUS*\n👤 *Untuk:* {staf_tujuan}\n📝 *Detail:* {instruksi}\n🆔 *ID:* {t_id}")
                            st.success(f"Tugas {t_id} terkirim!"); time.sleep(1); st.rerun()

        # --- C. DAFTAR TUGAS KHUSUS & SETORAN ---
        st.markdown("#### ⚡ Progres Tugas Khusus")
        df_raw = database.ambil_data("Tugas")
        
        if not df_raw.empty:
            df_t = df_raw.copy()
            if 'id' in df_t.columns: df_t = df_t.drop(columns=['id'])
            df_t.columns = [str(c).strip().upper() for c in df_t.columns]
            df_t = df_t.loc[:, ~df_t.columns.duplicated()]

            # LEVEL FILTERING: Hanya lihat tugas milik sendiri
            if user_level == "OWNER":
                mask = ~df_t['STATUS'].isin(['FINISH', 'BATAL'])
            else:
                mask = (df_t['STAF'] == user_aktif) & (~df_t['STATUS'].isin(['FINISH', 'BATAL']))
            
            tugas_aktif = df_t[mask].sort_values(by="ID", ascending=False).to_dict('records')

            if not tugas_aktif:
                st.caption("Belum ada tugas khusus tambahan.")
            else:
                for t in tugas_aktif:
                    with st.container(border=True):
                        col_info, col_stat = st.columns([3, 1])
                        col_info.markdown(f"**ID:** `{t['ID']}` | **Instruksi:** {t['INSTRUKSI']}")
                        col_stat.markdown(f"`{t['STATUS']}`")
                        
                        # Aksi buat Staf
                        if user_level != "OWNER":
                            if t['STATUS'] != "WAITING QC":
                                link = st.text_input("Link Hasil Kerja", key=f"url_{t['ID']}")
                                if st.button("🚀 SETOR", key=f"btn_{t['ID']}", use_container_width=True):
                                    if "http" in link:
                                        database.supabase.table("Tugas").update({"STATUS": "WAITING QC", "LINK_HASIL": link}).eq("ID", t['ID']).execute()
                                        kirim_notif_wa(f"📤 *SETORAN*\n👤 *Dari:* {user_aktif}\n🆔 *ID:* {t['ID']}\n🔗 *Link:* {link}")
                                        st.rerun()
                        # Aksi buat Owner/Admin (Inggi bisa QC juga kalau levelnya ADMIN)
                        else:
                            if t.get("LINK_HASIL"):
                                st.link_button("📂 QC VIDEO", t['LINK_HASIL'], use_container_width=True)
                                if st.button("✅ ACC", key=f"acc_{t['ID']}", use_container_width=True):
                                    database.supabase.table("Tugas").update({"STATUS": "FINISH"}).eq("ID", t['ID']).execute()
                                    kirim_notif_wa(f"✅ *TUGAS ACC*\n🆔 *ID:* {t['ID']}\n👤 *Staf:* {t['STAF']}")
                                    st.rerun()

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
