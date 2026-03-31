import streamlit as st
import pandas as pd
from modules import database
import time
from datetime import datetime
import pytz

def tampilkan_area_staf():
    # --- 1. SETUP IDENTITAS & KONEKSI ---
    user_aktif = st.session_state.get("user_aktif", "User").upper()
    user_level = st.session_state.get("user_level", "STAFF")
    tz = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz)

    # --- 2. PEMBUATAN SUB-MENU (TAB) ---
    tab_tugas, tab_panduan, tab_peraturan, tab_kontrak = st.tabs([
        "📝 TUGAS KERJA", 
        "📖 PANDUAN KERJA", 
        "⚖️ PERATURAN KERJA", 
        "📜 KONTRAK KERJA"
    ])

    # ==============================================================================
    # TAB 1: TUGAS KERJA (Kirim Instruksi & Setor Hasil URL)
    # ==============================================================================
    with tab_tugas:
        # --- A. PANEL OWNER (KIRIM TUGAS) ---
        if user_level == "OWNER":
            with st.expander("✨ **KIRIM INSTRUKSI TUGAS BARU**", expanded=False):
                with st.form("form_kirim_tugas", clear_on_submit=True):
                    col_a, col_b = st.columns([2, 1])
                    instruksi = col_a.text_area("Detail Instruksi", placeholder="Contoh: Buat video Beruang Episode 10...")
                    staf_tujuan = col_b.selectbox("Pilih Staf", ["ICHA", "LISSA", "INGGI", "NISSA"])
                    
                    if st.form_submit_button("🚀 KIRIM TUGAS", use_container_width=True):
                        if instruksi:
                            t_id = f"T{sekarang.strftime('%m%d%H%M%S')}"
                            try:
                                database.supabase.table("Tugas").insert({
                                    "ID": t_id,
                                    "STAF": staf_tujuan,
                                    "INSTRUKSI": instruksi,
                                    "STATUS": "PROSES",
                                    "DEADLINE": sekarang.strftime("%Y-%m-%d")
                                }).execute()
                                st.success(f"Tugas {t_id} berhasil dikirim ke {staf_tujuan}!")
                                time.sleep(1)
                                st.rerun()
                            except Exception as e:
                                st.error(f"Gagal kirim: {e}")

        st.divider()

        # --- B. RENDER DAFTAR TUGAS (GAYA KARTU) ---
        df_tugas = database.ambil_data("Tugas")
        
        if df_tugas.empty:
            st.info("📭 Belum ada tugas aktif.")
        else:
            # Filter: Staf cuma liat tugas mereka, Owner liat semua yang belum FINISH
            if user_level == "OWNER":
                mask = ~df_tugas['STATUS'].isin(['FINISH', 'BATAL'])
            else:
                mask = (df_tugas['STAF'].str.upper() == user_aktif) & (~df_tugas['STATUS'].isin(['FINISH', 'BATAL']))
            
            tugas_aktif = df_tugas[mask].sort_values(by="ID", ascending=False).to_dict('records')

            if not tugas_aktif:
                st.write("✅ Semua tugas sudah beres!")
            else:
                # Tampilan Grid 2 Kolom
                for i in range(0, len(tugas_aktif), 2):
                    cols = st.columns(2)
                    for j in range(2):
                        if i + j < len(tugas_aktif):
                            t = tugas_aktif[i + j]
                            with cols[j]:
                                with st.container(border=True):
                                    st.markdown(f"**{t['STAF']}** | `ID: {t['ID']}`")
                                    status = t['STATUS']
                                    icon = "🟢" if status == "PROSES" else "🟡" if status == "WAITING QC" else "🔴"
                                    st.markdown(f"{icon} `{status}`")
                                    st.info(f"📝 **Instruksi:**\n{t['INSTRUKSI']}")
                                    
                                    # Form Setor (Untuk Staf) atau Tombol ACC (Untuk Owner)
                                    if user_level != "OWNER":
                                        if status != "WAITING QC":
                                            url_hasil = st.text_input("Link Hasil (Drive/Terabox)", key=f"url_{t['ID']}")
                                            if st.button("🚀 SETOR HASIL", key=f"btn_{t['ID']}", use_container_width=True):
                                                if "http" in url_hasil:
                                                    database.supabase.table("Tugas").update({
                                                        "STATUS": "WAITING QC",
                                                        "LINK_HASIL": url_hasil
                                                    }).eq("ID", t['ID']).execute()
                                                    st.success("Tugas terkirim! Menunggu QC.")
                                                    time.sleep(1)
                                                    st.rerun()
                                        else:
                                            st.warning("Menunggu pengecekan Owner...")
                                    
                                    else: # Tombol Owner
                                        if t.get("LINK_HASIL"):
                                            st.link_button("📂 CEK HASIL VIDEO", t['LINK_HASIL'], use_container_width=True)
                                            c_acc, c_rev = st.columns(2)
                                            if c_acc.button("✅ ACC", key=f"acc_{t['ID']}", use_container_width=True):
                                                database.supabase.table("Tugas").update({"STATUS": "FINISH"}).eq("ID", t['ID']).execute()
                                                st.success("Tugas Selesai!")
                                                time.sleep(1)
                                                st.rerun()
                                            if c_rev.button("↩️ REVISI", key=f"rev_{t['ID']}", use_container_width=True):
                                                database.supabase.table("Tugas").update({"STATUS": "REVISI"}).eq("ID", t['ID']).execute()
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
