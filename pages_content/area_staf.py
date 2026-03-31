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
    st.title("📘 Pusat Informasi")
    # --- 1. SETUP IDENTITAS ---
    user_aktif = st.session_state.get("user_aktif", "User").upper()
    user_level = st.session_state.get("user_level", "STAFF").upper()
    tz = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz)
    
    foto_staff_default = "https://cdn-icons-png.flaticon.com/512/149/149071.png"

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

        # --- B. PANEL OWNER (KIRIM TUGAS KHUSUS) ---
        if user_level == "OWNER":
            with st.expander("✨ **KIRIM TUGAS KHUSUS BARU**", expanded=False):
                with st.form("form_tugas_baru", clear_on_submit=True):
                    col1, col2 = st.columns([2, 1])
                    instr = col1.text_area("Instruksi Tugas", placeholder="Tulis instruksi di sini...")
                    staf_tujuan = col2.selectbox("Pilih Staf", ["ICHA", "LISSA", "INGGI", "NISSA"])
                    if st.form_submit_button("🚀 KIRIM KE EDITOR", use_container_width=True):
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
            st.markdown("#### ⚡ Progres Tugas Aktif")
            status_aktif = ['PROSES', 'WAITING QC', 'REVISI']
            
            if user_level == "OWNER":
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
                                        if user_level == "OWNER":
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

            # --- E. ARSIP TUGAS ---
            st.divider()
            with st.expander("📂 RIWAYAT & ARSIP TUGAS"):
                status_arsip = ['FINISH', 'CANCELED', 'BATAL']
                mask_arsip = df_t['STATUS'].isin(status_arsip) if user_level == "OWNER" else (df_t['STAF'].str.upper() == user_aktif) & (df_t['STATUS'].isin(status_arsip))
                st.dataframe(df_t[mask_arsip].sort_values(by="ID", ascending=False)[['ID', 'STAF', 'INSTRUKSI', 'STATUS']], hide_index=True)
                    
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
