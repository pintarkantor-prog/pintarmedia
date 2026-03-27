import streamlit as st
import pandas as pd
from modules import database
import re
import requests
from datetime import datetime, timedelta
import pytz
import time

def tampilkan_kendali_tim():
    # --- 1. PROTEKSI AKSES ---
    user_level = st.session_state.get("user_level", "STAFF").upper()
    user_aktif = st.session_state.get("user_aktif", "User").upper()

    if user_level not in ["OWNER", "ADMIN"]:
        st.error("🚫 Maaf, Area ini hanya untuk jajaran Manajemen.")
        st.stop()

    # --- 2. SETUP WAKTU & FILTER ---
    tz = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz)
    
    st.title("💰 KENDALI KEUANGAN TIM")
    
    c_bln, c_thn, c_ref = st.columns([2, 1, 1], vertical_alignment="bottom")
    daftar_bulan = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
    pilihan_nama = c_bln.selectbox("📅 Pilih Bulan Laporan:", list(daftar_bulan.values()), index=sekarang.month - 1)
    bulan_dipilih = [k for k, v in daftar_bulan.items() if v == pilihan_nama][0]
    tahun_dipilih = c_thn.number_input("Tahun:", value=sekarang.year, min_value=2024, max_value=2030)
    
    if c_ref.button("🔄 REFRESH DATA", use_container_width=True):
        st.rerun()

    st.divider()

    try:
        # --- 3. AMBIL DATA DARI SUPABASE ---
        with st.spinner("Sinkronisasi Data Keuangan..."):
            df_staff = database.ambil_data("Staff")
            df_kas = database.ambil_data("Arus_Kas")
            # Data pendukung untuk hitung bonus/potongan (Absen & Tugas)
            df_absen = database.ambil_data("Absensi")
            df_tugas = database.ambil_data("Tugas")

        # --- 4. FUNGSI FILTER BULANAN ---
        def filter_bulanan(df, kolom_tgl):
            if df.empty: return pd.DataFrame()
            df['TGL_TEMP'] = pd.to_datetime(df[kolom_tgl], errors='coerce')
            mask = (df['TGL_TEMP'].dt.month == bulan_dipilih) & (df['TGL_TEMP'].dt.year == tahun_dipilih)
            return df[mask].copy()

        df_k_f = filter_bulanan(df_kas, 'Tanggal')
        df_a_f = filter_bulanan(df_absen, 'Tanggal')
        df_t_f = filter_bulanan(df_tugas, 'Deadline')

        # ======================================================================
        # --- 5. ANALISIS KEUANGAN & KAS ---
        # ======================================================================
        st.markdown("### 📊 ANALISIS KEUANGAN")
        
        inc = 0
        ops = 0
        bonus_terbayar_kas = 0
        
        if not df_k_f.empty:
            # Bersihkan nominal (hilangkan Rp, titik, koma)
            df_k_f['NOMINAL_VAL'] = pd.to_numeric(df_k_f['Nominal'].astype(str).replace(r'[^\d.]', '', regex=True), errors='coerce').fillna(0)
            inc = df_k_f[df_k_f['Tipe'] == 'PENDAPATAN']['NOMINAL_VAL'].sum()
            ops = df_k_f[(df_k_f['Tipe'] == 'PENGELUARAN') & (df_k_f['Kategori'] != 'Gaji Tim')]['NOMINAL_VAL'].sum()
            bonus_terbayar_kas = df_k_f[(df_k_f['Tipe'] == 'PENGELUARAN') & (df_k_f['Kategori'] == 'Gaji Tim')]['NOMINAL_VAL'].sum()

        # Hitung Estimasi Gaji Pokok Tim (Bukan Owner)
        total_gaji_pokok_tim = 0
        df_staff_real = df_staff[df_staff['LEVEL'].isin(['STAFF', 'UPLOADER', 'ADMIN'])]
        
        for _, s in df_staff_real.iterrows():
            g_pokok = int(str(s.get('GAJI_POKOK', '0')).replace('.', '') or 0)
            t_tunj = int(str(s.get('TUNJANGAN', '0')).replace('.', '') or 0)
            total_gaji_pokok_tim += (g_pokok + t_tunj)

        total_out = total_gaji_pokok_tim + bonus_terbayar_kas + ops
        saldo_bersih = inc - total_out

        # Tampilan Metrik
        with st.container(border=True):
            m1, m2, m3 = st.columns(3)
            m1.metric("💰 INCOME", f"Rp {inc:,.0f}")
            m2.metric("💸 OUTCOME (TOTAL)", f"Rp {total_out:,.0f}", delta=f"- {total_out:,.0f}", delta_color="inverse")
            m3.metric("📈 SALDO BERSIH", f"Rp {saldo_bersih:,.0f}", delta="SURPLUS" if saldo_bersih >= 0 else "DEFISIT")

        # ======================================================================
        # --- 6. RINCIAN GAJI & SLIP ---
        # ======================================================================
        st.markdown("### 📄 RINCIAN GAJI & SLIP STAFF")
        
        kol_v = st.columns(2)
        for idx, s in df_staff_real.reset_index().iterrows():
            n_up = str(s.get('NAMA', '')).strip().upper()
            v_gapok = int(str(s.get('GAJI_POKOK', '0')).replace('.', '') or 0)
            v_tunj = int(str(s.get('TUNJANGAN', '0')).replace('.', '') or 0)
            
            # Hitung Bonus Riil dari Kas (Jika ada catatan khusus di keterangan kas)
            bonus_staf = 0
            if not df_k_f.empty:
                mask_bonus = (df_k_f['Kategori'] == 'Gaji Tim') & (df_k_f['Keterangan'].str.contains(n_up, na=False, case=False))
                bonus_staf = df_k_f[mask_bonus]['NOMINAL_VAL'].sum()

            total_terima = v_gapok + v_tunj + bonus_staf

            with kol_v[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"**👤 {n_up}**")
                    c1, c2 = st.columns(2)
                    c1.markdown(f"<small>GAPOK + TUNJ</small><br><b>Rp {v_gapok+v_tunj:,}</b>", unsafe_allow_html=True)
                    c2.markdown(f"<small>BONUS CAIR</small><br><b style='color:#50FA7B;'>Rp {bonus_staf:,}</b>", unsafe_allow_html=True)
                    
                    st.markdown(f"#### Rp {total_terima:,}")
                    
                    if st.button(f"📄 CETAK SLIP {n_up}", key=f"slip_{n_up}", use_container_width=True):
                        # Slip HTML (Gaya Dian)
                        slip_html = f"""
                        <div style="background: white; padding: 20px; border: 1px solid #ddd; border-radius: 10px; color: #333; font-family: sans-serif; width: 300px; margin: auto;">
                            <center><b>PINTAR MEDIA</b><br><small>SLIP GAJI DIGITAL</small></center>
                            <hr>
                            <small>Nama:</small> <b>{n_up}</b><br>
                            <small>Periode:</small> <b>{pilihan_nama} {tahun_dipilih}</b><br>
                            <hr>
                            <table style="width:100%; font-size: 12px;">
                                <tr><td>Gaji Pokok</td><td align="right">{v_gapok:,}</td></tr>
                                <tr><td>Tunjangan</td><td align="right">{v_tunj:,}</td></tr>
                                <tr><td>Bonus</td><td align="right">{bonus_staf:,}</td></tr>
                                <tr style="font-weight:bold; border-top: 1px solid #eee;"><td>TOTAL</td><td align="right">Rp {total_terima:,}</td></tr>
                            </table>
                            <hr>
                            <center><small>Dicetak pada {sekarang.strftime('%d/%m/%Y')}</small></center>
                        </div>
                        <center><button onclick="window.print()" style="margin-top:10px;">🖨️ PRINT</button></center>
                        """
                        st.components.v1.html(slip_html, height=450)

    except Exception as e:
        st.error(f"⚠️ Gagal memuat laporan keuangan: {e}")
