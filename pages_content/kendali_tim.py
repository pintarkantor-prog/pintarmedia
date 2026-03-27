import streamlit as st
import pandas as pd
from modules import database  # Panggil modul database lo
import plotly.express as px
from datetime import datetime
import pytz
import time

def tampilkan_kendali_tim():    
    # --- 1. SETUP AUTH & WAKTU ---
    user_sekarang = st.session_state.get("user_aktif", "User").upper()
    user_level = st.session_state.get("user_level", "STAFF").upper()

    if user_level not in ["OWNER", "ADMIN"]:
        st.error("🚫 Area Terbatas!")
        st.stop()

    tz = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz)
    
    # --- 2. HEADER & FILTER ---
    col_h1, col_h2 = st.columns([3, 1])
    with col_h1:
        st.title("⚡ PUSAT KENDALI TIM")
    with col_h2:
        if st.button("🔄 REFRESH DATA", use_container_width=True):
            st.cache_data.clear()
            st.rerun()

    c_bln, c_thn = st.columns([2, 2])
    daftar_bulan = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
    pilihan_nama = c_bln.selectbox("📅 Pilih Bulan Laporan:", list(daftar_bulan.values()), index=sekarang.month - 1)
    bulan_dipilih = [k for k, v in daftar_bulan.items() if v == pilihan_nama][0]
    tahun_dipilih = c_thn.number_input("📅 Tahun:", value=sekarang.year, min_value=2024, max_value=2030)

    st.divider()

    try:
        # --- 3. AMBIL DATA ---
        df_staff = database.ambil_data("Staff")
        df_kas_raw = database.ambil_data("Arus_Kas")

        # --- 4. LOGIKA SARING TANGGAL (FIX CASE-SENSITIVE) ---
        if not df_kas_raw.empty:
            # Trik Aman: Cari kolom yang namanya mirip 'Tanggal'
            col_tgl = next((c for c in df_kas_raw.columns if c.lower() == 'tanggal'), None)
            
            if col_tgl:
                df_kas_raw['TGL_DT'] = pd.to_datetime(df_kas_raw[col_tgl], errors='coerce')
                df_k_f = df_kas_raw[(df_kas_raw['TGL_DT'].dt.month == bulan_dipilih) & (df_kas_raw['TGL_DT'].dt.year == tahun_dipilih)].copy()
                
                # Cleaning nominal (Regex lo) - Cari kolom 'Nominal'
                col_nom = next((c for c in df_kas_raw.columns if c.lower() == 'nominal'), 'Nominal')
                df_k_f['NOMINAL_VAL'] = pd.to_numeric(df_k_f[col_nom].astype(str).replace(r'[^\d.]', '', regex=True), errors='coerce').fillna(0)
            else:
                st.error("⚠️ Kolom 'Tanggal' tidak ditemukan di database Arus_Kas!")
                df_k_f = pd.DataFrame()
        else:
            df_k_f = pd.DataFrame()

        # --- 5. KALKULASI FINANSIAL (Pake .get() biar aman) ---
        inc_val, ops_val, bonus_val = 0, 0, 0
        if not df_k_f.empty:
            # Pastikan kolom Tipe & Kategori juga ketemu
            col_tipe = next((c for c in df_k_f.columns if c.lower() == 'tipe'), 'Tipe')
            col_kat = next((c for c in df_k_f.columns if c.lower() == 'kategori'), 'Kategori')

            inc_val = df_k_f[df_k_f[col_tipe].str.upper() == 'PENDAPATAN']['NOMINAL_VAL'].sum()
            ops_val = df_k_f[(df_k_f[col_tipe].str.upper() == 'PENGELUARAN') & (df_k_f[col_kat].str.upper() != 'GAJI TIM')]['NOMINAL_VAL'].sum()
            bonus_val = df_k_f[(df_k_f[col_tipe].str.upper() == 'PENGELUARAN') & (df_k_f[col_kat].str.upper() == 'GAJI TIM')]['NOMINAL_VAL'].sum()
        # Hitung Gapok Tim dari Staff
        total_gapok = 0
        df_staff_real = df_staff[df_staff['LEVEL'].isin(['STAFF', 'UPLOADER', 'ADMIN'])]
        for _, s in df_staff_real.iterrows():
            total_gapok += int(str(s.get('GAJI_POKOK', '0')).replace('.', '') or 0) + int(str(s.get('TUNJANGAN', '0')).replace('.', '') or 0)

        total_out_riil = total_gapok + bonus_val + ops_val
        saldo_riil = inc_val - total_out_riil
        margin_val = (saldo_riil / inc_val * 100) if inc_val > 0 else 0

        # ======================================================================
        # --- 6. UI: FINANCIAL DASHBOARD (METRIK LO BANGET!) ---
        # ======================================================================
        with st.expander("💰 ANALISIS KEUANGAN & KAS", expanded=True):
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("💰 INCOME", f"Rp {inc_val:,.0f}")
            m2.metric("💸 OUTCOME", f"Rp {total_out_riil:,.0f}", delta=f("-Rp {total_out_riil:,.0f}") if total_out_riil > 0 else None, delta_color="normal")
            
            status_saldo = "SURPLUS" if saldo_riil >= 0 else "DEFISIT"
            warna_delta = "normal" if saldo_riil >= 0 else "inverse"
            m3.metric("📈 SALDO BERSIH", f"Rp {saldo_riil:,.0f}", delta=status_saldo, delta_color=warna_delta)
            m4.metric("📊 MARGIN", f"{margin_val:.1f}%")

            st.divider()

            # Formasi 3 Kolom: Input - Logs - Viz
            col_input, col_logs, col_viz = st.columns([1, 1.2, 1], gap="small")
            
            with col_input:
                with st.form("form_kas_dian", clear_on_submit=True):
                    f_tipe = st.pills("Tipe", ["PENDAPATAN", "PENGELUARAN"], default="PENGELUARAN", label_visibility="collapsed")
                    f_kat = st.selectbox("Kategori", ["YouTube", "Brand Deal", "Gaji Tim", "Operasional", "Lainnya"], label_visibility="collapsed")
                    f_nom = st.number_input("Nominal", min_value=0, step=50000, label_visibility="collapsed", placeholder="Rp...")
                    f_ket = st.text_area("Ket...", height=65, label_visibility="collapsed", placeholder="Catatan...")
                    if st.form_submit_button("🚀 SIMPAN", use_container_width=True):
                        database.supabase.table("Arus_Kas").insert({"Tanggal": sekarang.strftime('%Y-%m-%d'), "Tipe": f_tipe, "Kategori": f_kat, "Nominal": str(int(f_nom)), "Keterangan": f_ket, "Pencatat": user_sekarang}).execute()
                        st.success("Tersimpan!"); time.sleep(0.5); st.rerun()

            with col_logs:
                with st.container(height=315):
                    if not df_k_f.empty:
                        for _, r in df_k_f.sort_values(by='TGL_DT', ascending=False).head(15).iterrows():
                            c_text = "#00ba69" if r['Tipe'] == "PENDAPATAN" else "#ff4b4b"
                            st.markdown(f"<div style='font-size:11px; border-bottom:1px solid #333; padding:4px 0;'><b>{r['Kategori']}</b> <span style='float:right; color:{c_text};'>Rp {float(r['Nominal']):,.0f}</span><br><small>{r['Keterangan']}</small></div>", unsafe_allow_html=True)

            with col_viz:
                if (inc_val + total_out_riil) > 0:
                    fig = px.pie(values=[inc_val, total_out_riil], names=['INC', 'OUT'], hole=0.75, color_discrete_sequence=["#00ba69", "#ff4b4b"])
                    fig.update_layout(showlegend=False, height=200, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
                    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        # ======================================================================
        # --- 7. UI: SLIP GAJI MEWAH (TANPA SP/BONUS VIDEO/ABSEN) ---
        # ======================================================================
        st.write(""); st.markdown("### 📄 RINCIAN GAJI & SLIP STAFF")
        kol_v = st.columns(2) 
        for idx, s in df_staff_real.reset_index().iterrows():
            n_up = str(s.get('NAMA', '')).strip().upper()
            if n_up == "" or n_up == "NAN": continue
            
            gapok = int(pd.to_numeric(str(s.get('GAJI_POKOK', '0')).replace('.',''), errors='coerce') or 0)
            tunj = int(pd.to_numeric(str(s.get('TUNJANGAN', '0')).replace('.',''), errors='coerce') or 0)
            
            bonus_cair = 0
            if not df_k_f.empty:
                mask = (df_k_f['Kategori'] == 'Gaji Tim') & (df_k_f['Keterangan'].str.upper().str.contains(n_up, na=False))
                bonus_cair = int(df_k_f[mask]['NOMINAL_VAL'].sum())

            total_nett = gapok + tunj + bonus_cair

            with kol_v[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"""<div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;"><div style="background: linear-gradient(135deg, #1d976c, #93f9b9); color: white; width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 18px;">{n_up[0]}</div><div><b style="font-size: 15px;">{n_up}</b><br><span style="font-size: 11px; color: #888;">{s.get('LEVEL', 'STAFF')}</span></div></div>""", unsafe_allow_html=True)
                    c1, c2 = st.columns(2)
                    c1.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>ESTIMASI TERIMA</p><h3 style='margin:0; color:#1d976c;'>Rp {total_nett:,}</h3>", unsafe_allow_html=True)
                    c2.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>STATUS</p><b style='font-size:14px; color:#1d976c;'>AKTIF</b>", unsafe_allow_html=True)
                    
                    if st.button(f"📄 PRINT SLIP {n_up}", key=f"slp_{n_up}", use_container_width=True):
                        slip_html = f"""<div style="background: white; padding: 30px; border-radius: 20px; border: 1px solid #eee; font-family: sans-serif; width: 320px; margin: auto; color: #333; box-shadow: 0 10px 30px rgba(0,0,0,0.05);"><center><h2 style="color: #1d976c; margin-bottom: 0;">PINTAR MEDIA</h2><p style="font-size: 10px; letter-spacing: 4px; color: #1d976c; font-weight: 800; text-transform: uppercase;">Slip Gaji Digital</p></center><div style="background: #fcfcfc; padding: 15px; border-radius: 12px; border: 1px solid #f0f0f0; margin: 20px 0;"><table style="width: 100%; font-size: 11px;"><tr><td style="color: #999;">NAMA</td><td align="right"><b>{n_up}</b></td></tr><tr><td style="color: #999;">PERIODE</td><td align="right"><b>{pilihan_nama} {tahun_dipilih}</b></td></tr></table></div><table style="width: 100%; font-size: 13px; line-height: 2.5;"><tr><td>Gaji Pokok</td><td align="right">Rp {gapok:,}</td></tr><tr><td>Tunjangan</td><td align="right">Rp {tunj:,}</td></tr><tr style="color: #1d976c;"><td>Bonus Cair</td><td align="right">+ {bonus_cair:,}</td></tr></table><div style="background: #1a1a1a; color: white; padding: 15px; border-radius: 15px; text-align: center; margin-top: 25px;"><p style="margin:0; font-size: 9px; color: #55efc4; letter-spacing: 2px;">TOTAL DITERIMA</p><h2 style="margin: 5px 0 0; color: #55efc4;">Rp {total_nett:,}</h2></div></div><center><button onclick="window.print()" style="margin-top:20px; cursor:pointer;">🖨️ PRINT</button></center>"""
                        st.components.v1.html(slip_html, height=750)

    except Exception as e:
        st.error(f"⚠️ Sesuai Referensi, Error di: {e}")
