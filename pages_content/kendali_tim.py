import streamlit as st
import pandas as pd
from modules import database
import plotly.express as px
from datetime import datetime
import pytz
import time

def tampilkan_kendali_tim():
    # --- 1. PROTEKSI AKSES ---
    user_level = st.session_state.get("user_level", "STAFF").upper()
    user_sekarang = st.session_state.get("user_aktif", "User").upper()

    if user_level not in ["OWNER", "ADMIN"]:
        st.error("🚫 Akses Dibatasi!")
        st.stop()

    # --- 2. SETUP WAKTU & HEADER ---
    tz = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz)
    
    st.title("⚡ PUSAT KENDALI TIM")
    
    c_bln, c_thn, c_ref = st.columns([3, 2, 1.2], vertical_alignment="bottom")
    daftar_bulan = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
    pilihan_nama = c_bln.selectbox("📅 Pilih Bulan Laporan:", list(daftar_bulan.values()), index=sekarang.month - 1)
    bulan_dipilih = [k for k, v in daftar_bulan.items() if v == pilihan_nama][0]
    tahun_dipilih = c_thn.number_input("Tahun:", value=sekarang.year)
    
    if c_ref.button("🔄 REFRESH DATA", use_container_width=True):
        st.rerun()

    st.divider()

    try:
        # --- 3. AMBIL DATA & FILTER ---
        df_staff = database.ambil_data("Staff")
        df_kas = database.ambil_data("Arus_Kas")
        
        # Standarisasi Kolom Kapital
        if not df_kas.empty:
            df_kas.columns = [c.upper() for c in df_kas.columns]
            df_kas['TGL_DT'] = pd.to_datetime(df_kas['TANGGAL'], errors='coerce')
            df_k_f = df_kas[(df_kas['TGL_DT'].dt.month == bulan_dipilih) & (df_kas['TGL_DT'].dt.year == tahun_dipilih)].copy()
        else:
            df_k_f = pd.DataFrame()

        # --- 4. KALKULASI FINANSIAL ---
        inc, ops, bonus_cair = 0, 0, 0
        if not df_k_f.empty:
            df_k_f['NOMINAL_VAL'] = pd.to_numeric(df_k_f['NOMINAL'].astype(str).replace(r'[^\d.]', '', regex=True), errors='coerce').fillna(0)
            inc = df_k_f[df_k_f['TIPE'] == 'PENDAPATAN']['NOMINAL_VAL'].sum()
            ops = df_k_f[(df_k_f['TIPE'] == 'PENGELUARAN') & (df_k_f['KATEGORI'] != 'GAJI TIM')]['NOMINAL_VAL'].sum()
            bonus_cair = df_k_f[(df_k_f['TIPE'] == 'PENGELUARAN') & (df_k_f['KATEGORI'] == 'GAJI TIM')]['NOMINAL_VAL'].sum()

        total_gapok = 0
        df_staff_real = df_staff[df_staff['LEVEL'].isin(['STAFF', 'UPLOADER', 'ADMIN'])]
        for _, s in df_staff_real.iterrows():
            total_gapok += int(str(s.get('GAJI_POKOK', '0')).replace('.', '') or 0) + int(str(s.get('TUNJANGAN', '0')).replace('.', '') or 0)

        total_out = total_gapok + bonus_cair + ops
        saldo_bersih = inc - total_out
        margin = (saldo_bersih / inc * 100) if inc > 0 else 0

        # ======================================================================
        # --- UI: FINANCIAL COMMAND CENTER (SESUAI GAMBAR) ---
        # ======================================================================
        with st.expander("💰 ANALISIS KEUANGAN & KAS", expanded=True):
            # Baris Metrik
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("💰 INCOME", f"Rp {inc:,.0f}")
            m2.metric("💸 OUTCOME", f"Rp {total_out:,.0f}", delta=f"-Rp {total_out:,.0f}", delta_color="inverse")
            m3.metric("📈 SALDO BERSIH", f"Rp {saldo_bersih:,.0f}", delta="SURPLUS" if saldo_bersih >= 0 else "DEFISIT")
            m4.metric("📊 MARGIN", f"{margin:.1f}%")

            st.divider()

            # Layout 3 Kolom: Input | Log | Chart
            col_input, col_logs, col_viz = st.columns([1.2, 1.5, 1], gap="medium")

            with col_input:
                with st.form("form_kas_v2", clear_on_submit=True):
                    f_tipe = st.radio("Tipe", ["PENDAPATAN", "PENGELUARAN"], horizontal=True, label_visibility="collapsed")
                    f_kat = st.selectbox("Kategori", ["YouTube", "Brand Deal", "Gaji Tim", "Operasional", "Lainnya"], label_visibility="collapsed")
                    f_nom = st.number_input("Nominal", min_value=0, step=50000, placeholder="Nominal Rp...")
                    f_ket = st.text_area("Catatan...", height=80, placeholder="Keterangan transaksi...")
                    if st.form_submit_button("🚀 SIMPAN", use_container_width=True):
                        if f_nom > 0:
                            database.supabase.table("Arus_Kas").insert({
                                "TANGGAL": sekarang.strftime('%Y-%m-%d'), "TIPE": f_tipe,
                                "KATEGORI": f_kat, "NOMINAL": str(int(f_nom)),
                                "KETERANGAN": f_ket, "PENCATAT": user_sekarang
                            }).execute()
                            st.success("Tersimpan!"); time.sleep(0.5); st.rerun()

            with col_logs:
                # Log Transaksi (Scrollable Container)
                with st.container(height=300, border=True):
                    if not df_k_f.empty:
                        df_display = df_k_f.sort_values(by='TGL_DT', ascending=False)
                        for _, r in df_display.iterrows():
                            c_text = "#50FA7B" if r['TIPE'] == "PENDAPATAN" else "#FF5555"
                            st.markdown(f"""
                            <div style='font-size:11px; border-bottom:1px solid #333; padding:5px 0;'>
                                <span style='color:#888;'>{r['KATEGORI']}</span>
                                <span style='float:right; color:{c_text}; font-weight:bold;'>Rp {float(r['NOMINAL']):,.0f}</span><br>
                                <i style='color:#ccc;'>{r['KETERANGAN']}</i>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.caption("Belum ada data.")

            with col_viz:
                # Donut Chart
                if inc > 0 or total_out > 0:
                    fig = px.pie(values=[inc, total_out], names=['INCOME', 'OUTCOME'], 
                                 hole=0.7, color_discrete_sequence=["#50FA7B", "#FF5555"])
                    fig.update_layout(showlegend=False, height=200, margin=dict(t=0,b=0,l=0,r=0),
                                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
                    st.markdown(f"<center><small>{margin:.1f}% Margin</small></center>", unsafe_allow_html=True)

        # ======================================================================
        # --- MENU 2: RINCIAN GAJI & SLIP ---
        # ======================================================================
        st.write("")
        st.markdown("### 📄 RINCIAN GAJI & SLIP STAFF")
        
        kol_v = st.columns(2)
        for idx, s in df_staff_real.reset_index().iterrows():
            n_up = str(s.get('NAMA', '')).strip().upper()
            v_gapok = int(str(s.get('GAJI_POKOK', '0')).replace('.', '') or 0)
            v_tunj = int(str(s.get('TUNJANGAN', '0')).replace('.', '') or 0)
            
            # Cari Bonus yang sudah di-input di Arus_Kas (Kategori: Gaji Tim, Ket: Nama Staff)
            bonus_staf = 0
            if not df_k_f.empty:
                mask = (df_k_f['KATEGORI'] == 'GAJI TIM') & (df_k_f['KETERANGAN'].str.contains(n_up, na=False, case=False))
                bonus_staf = df_k_f[mask]['NOMINAL_VAL'].sum()

            total_terima = v_gapok + v_tunj + bonus_staf

            with kol_v[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"**👤 {n_up}**")
                    c1, c2 = st.columns(2)
                    c1.markdown(f"<small>GAPOK+TUNJ</small><br><b>Rp {v_gapok+v_tunj:,}</b>", unsafe_allow_html=True)
                    c2.markdown(f"<small>BONUS CAIR</small><br><b style='color:#50FA7B;'>Rp {bonus_staf:,}</b>", unsafe_allow_html=True)
                    st.markdown(f"#### Total: Rp {total_terima:,}")
                    
                    if st.button(f"📄 PRINT SLIP {n_up}", key=f"slip_{n_up}", use_container_width=True):
                        slip_html = f"""
                        <div style="background:white; padding:20px; color:#333; font-family:sans-serif; border:1px solid #ddd; width:300px; margin:auto; border-radius:10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
                            <center><b style="font-size:18px; color:#1d976c;">PINTAR MEDIA</b><br><small>SLIP GAJI DIGITAL</small></center>
                            <hr>
                            <table style="width:100%; font-size:12px;">
                                <tr><td>Nama</td><td align="right"><b>{n_up}</b></td></tr>
                                <tr><td>Jabatan</td><td align="right">{s.get('LEVEL', 'STAFF')}</td></tr>
                                <tr><td>Periode</td><td align="right">{pilihan_nama} {tahun_dipilih}</td></tr>
                            </table>
                            <hr>
                            <table style="width:100%; font-size:12px; line-height:1.8;">
                                <tr><td>Gaji Pokok</td><td align="right">{v_gapok:,}</td></tr>
                                <tr><td>Tunjangan</td><td align="right">{v_tunj:,}</td></tr>
                                <tr style="color:#1d976c;"><td>Bonus Cair</td><td align="right">+{bonus_staf:,}</td></tr>
                                <tr style="font-weight:bold; font-size:15px; border-top:2px solid #eee;">
                                    <td style="padding-top:10px;">TOTAL</td><td align="right" style="padding-top:10px; color:#1d976c;">Rp {total_terima:,}</td>
                                </tr>
                            </table>
                            <hr>
                            <center><small>Cetak: {sekarang.strftime('%d/%m/%Y %H:%M')}</small></center>
                        </div>
                        <center><button onclick="window.print()" style="margin-top:15px; padding:8px 20px; background:#1d976c; color:white; border:none; border-radius:5px; cursor:pointer;">🖨️ Cetak ke PDF</button></center>
                        """
                        st.components.v1.html(slip_html, height=450)

    except Exception as e:
        st.error(f"⚠️ Error Keuangan: {e}")
