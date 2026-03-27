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
        st.error("🚫 Maaf, Area ini hanya untuk jajaran Manajemen.")
        st.stop()

    # --- 2. SETUP WAKTU & HEADER ---
    tz = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz)
    
    col_h1, col_h2 = st.columns([3, 1])
    with col_h1:
        st.title("⚡ PUSAT KENDALI TIM")
    with col_h2:
        if st.button("🔄 REFRESH DATA", use_container_width=True):
            st.cache_data.clear()
            st.rerun()

    # --- 3. FILTER PERIODE ---
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

        if not df_kas_raw.empty:
            # Sesuaikan dengan screenshot: kolomnya 'Tanggal'
            df_kas_raw['TGL_TEMP'] = pd.to_datetime(df_kas_raw['Tanggal'], errors='coerce')
            mask = (df_kas_raw['TGL_TEMP'].dt.month == bulan_dipilih) & (df_kas_raw['TGL_TEMP'].dt.year == tahun_dipilih)
            df_k_f = df_kas_raw[mask].copy()
        else:
            df_k_f = pd.DataFrame()

        # --- 4. KALKULASI FINANSIAL (Sesuaikan Nama Kolom di Gambar) ---
        inc, ops, bonus_cair = 0, 0, 0
        if not df_k_f.empty:
            # Sesuai gambar: 'Nominal'
            df_k_f['NOMINAL_VAL'] = pd.to_numeric(df_k_f['Nominal'].astype(str).replace(r'[^\d.]', '', regex=True), errors='coerce').fillna(0)
            
            # Sesuai gambar: 'Tipe' & 'Kategori' (Huruf depan besar)
            inc = df_k_f[df_k_f['Tipe'] == 'PENDAPATAN']['NOMINAL_VAL'].sum()
            ops = df_k_f[(df_k_f['Tipe'] == 'PENGELUARAN') & (df_k_f['Kategori'] != 'Gaji Tim')]['NOMINAL_VAL'].sum()
            bonus_cair = df_k_f[(df_k_f['Tipe'] == 'PENGELUARAN') & (df_k_f['Kategori'] == 'Gaji Tim')]['NOMINAL_VAL'].sum()

        # Hitung Gapok Tim dari Tabel Staff
        total_gapok_tim = 0
        df_staff_real = df_staff[df_staff['LEVEL'].isin(['STAFF', 'UPLOADER', 'ADMIN'])]
        for _, s in df_staff_real.iterrows():
            total_gapok_tim += int(str(s.get('GAJI_POKOK', '0')).replace('.', '') or 0) + int(str(s.get('TUNJANGAN', '0')).replace('.', '') or 0)

        total_out = total_gapok_tim + bonus_cair + ops
        saldo_bersih = inc - total_out
        margin = (saldo_bersih / inc * 100) if inc > 0 else 0

        # ======================================================================
        # --- UI: FINANCIAL COMMAND CENTER (SULTAN LOOK) ---
        # ======================================================================
        with st.expander("💰 ANALISIS KEUANGAN & KAS", expanded=True):
            # Baris Metrik
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("💰 INCOME", f"Rp {inc:,.0f}")
            
            # Outcome Merah (Delta negatif)
            m2.metric("💸 OUTCOME", f"Rp {total_out:,.0f}", delta=f"-Rp {total_out:,.0f}" if total_out > 0 else None, delta_color="inverse")
            
            # Saldo Bersih (Positif Hijau, Negatif Merah)
            status_txt = "🟢 SURPLUS" if saldo_bersih >= 0 else "🔴 DEFISIT"
            m3.metric("📈 SALDO BERSIH", f"Rp {saldo_bersih:,.0f}", delta=status_txt, delta_color="normal")
            
            m4.metric("📊 MARGIN", f"{margin:.1f}%")

            st.divider()

            # Formasi: Input (1) - Logs (1.2) - Viz (1)
            col_input, col_logs, col_viz = st.columns([1, 1.2, 1], gap="small")

            with col_input:
                with st.form("form_kas_new", clear_on_submit=True):
                    f_tipe = st.pills("Tipe", ["PENDAPATAN", "PENGELUARAN"], default="PENGELUARAN", label_visibility="collapsed")
                    f_kat = st.selectbox("Kategori", ["YouTube", "Brand Deal", "Gaji Tim", "Operasional", "Lainnya"], label_visibility="collapsed")
                    f_nom = st.number_input("Nominal", min_value=0, step=50000, label_visibility="collapsed", placeholder="Nominal Rp...")
                    f_ket = st.text_area("Keterangan", height=65, label_visibility="collapsed", placeholder="Catatan...")
                    if st.form_submit_button("🚀 SIMPAN", use_container_width=True):
                        if f_nom > 0:
                            # SINKRON MURNI SUPABASE
                            database.supabase.table("Arus_Kas").insert({
                                "Tanggal": sekarang.strftime('%Y-%m-%d'),
                                "Tipe": f_tipe,
                                "Kategori": f_kat,
                                "Nominal": str(int(f_nom)),
                                "Keterangan": f_ket,
                                "Pencatat": user_sekarang.upper()
                            }).execute()
                            st.success("Tersimpan!"); time.sleep(0.5); st.rerun()

            with col_logs:
                with st.container(height=315):
                    if not df_k_f.empty:
                        df_logs_display = df_k_f.sort_values(by='TGL_TEMP', ascending=False).head(15)
                        for _, r in df_logs_display.iterrows():
                            color = "#00ba69" if r['Tipe'] == "PENDAPATAN" else "#ff4b4b"
                            st.markdown(f"""
                            <div style='font-size:11px; border-bottom:1px solid #333; padding:4px 0;'>
                                <b style='color:#ccc;'>{r['Kategori']}</b> 
                                <span style='float:right; color:{color}; font-weight:bold;'>Rp {float(r['Nominal']):,.0f}</span><br>
                                <span style='color:#666; font-style:italic;'>{r['Keterangan']}</span>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.caption("Belum ada data transaksi.")

            with col_viz:
                st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
                if inc > 0 or total_out > 0:
                    fig = px.pie(values=[inc, total_out], names=['INCOME', 'OUTCOME'], hole=0.75, color_discrete_sequence=["#00ba69", "#ff4b4b"])
                    fig.update_layout(showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5, font=dict(size=10)),
                                      height=200, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
                else:
                    st.markdown("<p style='text-align:center; color:#666; font-size:12px; margin-top:50px;'>No Viz Data.</p>", unsafe_allow_html=True)

        # --- 7. RINCIAN GAJI & SLIP ---
        st.write("")
        st.markdown("### 📄 RINCIAN GAJI & SLIP STAFF")
        kol_v = st.columns(2)
        for idx, s in df_staff_real.reset_index().iterrows():
            n_up = str(s.get('NAMA', '')).strip().upper()
            v_gapok = int(str(s.get('GAJI_POKOK', '0')).replace('.', '') or 0)
            v_tunj = int(str(s.get('TUNJANGAN', '0')).replace('.', '') or 0)
            
            bonus_staf = 0
            if not df_k_f.empty:
                mask = (df_k_f['Kategori'] == 'Gaji Tim') & (df_k_f['Keterangan'].str.contains(n_up, na=False, case=False))
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
                        <div style="background:white; padding:20px; color:#333; font-family:sans-serif; border:1px solid #ddd; width:300px; margin:auto; border-radius:10px;">
                            <center><b style="font-size:18px; color:#1d976c;">PINTAR MEDIA</b><br><small>SLIP GAJI DIGITAL</small></center>
                            <hr>
                            <table style="width:100%; font-size:11px;">
                                <tr><td>Nama</td><td align="right"><b>{n_up}</b></td></tr>
                                <tr><td>Periode</td><td align="right">{pilihan_nama} {tahun_dipilih}</td></tr>
                            </table>
                            <hr>
                            <table style="width:100%; font-size:12px; line-height:1.8;">
                                <tr><td>Gaji Pokok</td><td align="right">{v_gapok:,}</td></tr>
                                <tr><td>Tunjangan</td><td align="right">{v_tunj:,}</td></tr>
                                <tr style="color:#1d976c;"><td>Bonus Cair</td><td align="right">+{bonus_staf:,}</td></tr>
                                <tr style="font-weight:bold; font-size:14px; border-top:2px solid #eee;">
                                    <td style="padding-top:10px;">TOTAL</td><td align="right" style="padding-top:10px;">Rp {total_terima:,}</td>
                                </tr>
                            </table>
                            <hr>
                            <center><small>ID Sesi: {st.session_state.get('browser_session_id', 'N/A')[:8]}</small></center>
                        </div>
                        <center><button onclick="window.print()" style="margin-top:10px; cursor:pointer;">🖨️ Cetak PDF</button></center>
                        """
                        st.components.v1.html(slip_html, height=450)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
