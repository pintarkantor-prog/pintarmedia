import streamlit as st
import pandas as pd
from modules import database
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

    tz_wib = pytz.timezone('Asia/Jakarta')
    sekarang = datetime.now(tz_wib)
    
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

        # --- 4. SARING DATA (PAKE PENANGKAL ERROR KOLOM) ---
        if not df_kas_raw.empty:
            col_tgl = next((c for c in df_kas_raw.columns if c.lower() == 'tanggal'), 'Tanggal')
            col_nom = next((c for c in df_kas_raw.columns if c.lower() == 'nominal'), 'Nominal')
            col_tipe = next((c for c in df_kas_raw.columns if c.lower() == 'tipe'), 'Tipe')
            col_kat = next((c for c in df_kas_raw.columns if c.lower() == 'kategori'), 'Kategori')
            col_ket = next((c for c in df_kas_raw.columns if c.lower() == 'keterangan'), 'Keterangan')

            df_kas_raw['TGL_DT'] = pd.to_datetime(df_kas_raw[col_tgl], errors='coerce')
            df_k_f = df_kas_raw[(df_kas_raw['TGL_DT'].dt.month == bulan_dipilih) & (df_kas_raw['TGL_DT'].dt.year == tahun_dipilih)].copy()
            df_k_f['NOM_VAL'] = pd.to_numeric(df_k_f[col_nom].astype(str).replace(r'[^\d.]', '', regex=True), errors='coerce').fillna(0)
        else:
            df_k_f = pd.DataFrame()
            col_tipe, col_kat, col_ket = 'Tipe', 'Kategori', 'Keterangan'

        # --- 5. KALKULASI FINANSIAL ---
        inc_val = df_k_f[df_k_f[col_tipe].fillna('').astype(str).str.upper() == 'PENDAPATAN']['NOM_VAL'].sum() if not df_k_f.empty else 0
        ops_val = df_k_f[(df_k_f[col_tipe].fillna('').astype(str).str.upper() == 'PENGELUARAN') & (df_k_f[col_kat].fillna('').astype(str).str.upper() != 'GAJI TIM')]['NOM_VAL'].sum() if not df_k_f.empty else 0
        bonus_val = df_k_f[(df_k_f[col_tipe].fillna('').astype(str).str.upper() == 'PENGELUARAN') & (df_k_f[col_kat].fillna('').astype(str).str.upper() == 'GAJI TIM')]['NOM_VAL'].sum() if not df_k_f.empty else 0

        # DETEKSI KOLOM STAFF (Gaji_Pokok, Tunjangan, Level)
        c_gp = next((c for c in df_staff.columns if c.lower() == 'gaji_pokok'), 'Gaji_Pokok')
        c_tj = next((c for c in df_staff.columns if c.lower() == 'tunjangan'), 'Tunjangan')
        c_lv = next((c for c in df_staff.columns if c.lower() == 'level'), 'Level')
        
        # Hitung Gapok Tim
        df_staff_real = df_staff[df_staff[c_lv].fillna('').astype(str).str.upper().isin(['STAFF', 'UPLOADER', 'ADMIN'])]
        total_gapok = 0
        for _, s in df_staff_real.iterrows():
            total_gapok += int(str(s.get(c_gp, '0')).replace('.', '') or 0) + int(str(s.get(c_tj, '0')).replace('.', '') or 0)

        total_out_riil = total_gapok + bonus_val + ops_val
        saldo_riil = inc_val - total_out_riil
        margin_val = (saldo_riil / inc_val * 100) if inc_val > 0 else 0

        # ======================================================================
        # --- 6. UI: FINANCIAL DASHBOARD ---
        # ======================================================================
        with st.expander("💰 ANALISIS KEUANGAN & KAS", expanded=True):
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("💰 INCOME", f"Rp {inc_val:,.0f}")
            m2.metric("💸 OUTCOME", f"Rp {total_out_riil:,.0f}", delta=f"-Rp {total_out_riil:,.0f}" if total_out_riil > 0 else None, delta_color="normal")
            
            status_s = "SURPLUS" if saldo_riil >= 0 else "DEFISIT"
            warna_d = "normal" if saldo_riil >= 0 else "inverse"
            m3.metric("📈 SALDO BERSIH", f"Rp {saldo_riil:,.0f}", delta=status_s, delta_color=warna_d)
            m4.metric("📊 MARGIN", f"{margin_val:.1f}%")

            st.divider()

            col_in, col_logs, col_viz = st.columns([1, 1.2, 1], gap="small")
            
            with col_in:
                with st.form("form_kas_dian", clear_on_submit=True):
                    f_tipe = st.pills("Tipe", ["PENDAPATAN", "PENGELUARAN"], default="PENGELUARAN", label_visibility="collapsed")
                    f_kat = st.selectbox("Kategori", ["YouTube", "Brand Deal", "Gaji Tim", "Operasional", "Lainnya"], label_visibility="collapsed")
                    f_nom = st.number_input("Nominal", min_value=0, step=50000, label_visibility="collapsed")
                    f_ket = st.text_area("Ket...", height=65, label_visibility="collapsed")
                    if st.form_submit_button("🚀 SIMPAN", use_container_width=True):
                        database.supabase.table("Arus_Kas").insert({"Tanggal": sekarang.strftime('%Y-%m-%d'), "Tipe": f_tipe, "Kategori": f_kat, "Nominal": str(int(f_nom)), "Keterangan": f_ket, "Pencatat": user_sekarang}).execute()
                        st.success("OK!"); time.sleep(0.5); st.rerun()

            # --- LOG TRANSAKSI (GAYA SAKTI DIAN: TANGGAL + ABU MIRING) ---
            with col_logs:
                with st.container(height=315):
                    if not df_k_f.empty:
                        for _, r in df_k_f.sort_values(by='TGL_DT', ascending=False).head(15).iterrows():
                            v_tipe = str(r.get(col_tipe, '')).upper()
                            color = "#00ba69" if v_tipe == "PENDAPATAN" else "#ff4b4b"
                            tgl_log = r['TGL_DT'].strftime('%d %b') if pd.notnull(r['TGL_DT']) else "-"
                            
                            st.markdown(f"""
                            <div style='font-size:11px; border-bottom:1px solid #333; padding:5px 0;'>
                                <b style='color:#ccc;'>{r.get(col_kat, 'KAS')}</b> 
                                <span style='float:right; color:{color}; font-weight:bold;'>Rp {r['NOM_VAL']:,.0f}</span><br>
                                <small style='color: #888; font-style: italic;'>[{tgl_log}] - {r.get(col_ket, '-')}</small>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.caption("Belum ada data transaksi.")

            with col_viz:
                st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
                if (inc_val + total_out_riil) > 0:
                    fig = px.pie(values=[inc_val, total_out_riil], names=['INCOME', 'OUTCOME'], hole=0.75, color_discrete_sequence=["#00ba69", "#ff4b4b"])
                    fig.update_layout(
                        showlegend=True,
                        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5, font=dict(size=10)),
                        height=200, margin=dict(t=0, b=0, l=0, r=0),
                        paper_bgcolor='rgba(0,0,0,0)',
                        annotations=[dict(text=f"{margin_val:.1f}%", x=0.5, y=0.5, font_size=20, showarrow=False, font_color="#ccc")]
                    )
                    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        # --- 7. RINCIAN GAJI & SLIP (FIX ERROR 'Level') ---
        st.write(""); st.markdown("### 📄 RINCIAN GAJI & SLIP STAFF")
        kol_v = st.columns(2) 
        df_staff_slip = df_staff_real.reset_index(drop=True)
        for idx, s in df_staff_slip.iterrows():
            c_nama = next((c for c in s.index if c.lower() == 'nama'), 'Nama')
            n_up = str(s.get(c_nama, '')).strip().upper()
            if n_up == "" or n_up == "NAN": continue
            
            g_p = int(pd.to_numeric(str(s.get(c_gp, '0')).replace('.',''), errors='coerce') or 0)
            t_j = int(pd.to_numeric(str(s.get(c_tj, '0')).replace('.',''), errors='coerce') or 0)
            
            b_c = 0
            if not df_k_f.empty:
                mask = (df_k_f[col_kat].fillna('').astype(str).str.upper() == 'GAJI TIM') & \
                       (df_k_f[col_ket].fillna('').astype(str).str.upper().str.contains(n_up, na=False))
                b_c = int(df_k_f[mask]['NOM_VAL'].sum())
            
            t_n = g_p + t_j + b_c

            with kol_v[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"**👤 {n_up}**")
                    st.markdown(f"#### Rp {t_n:,}")
                    if st.button(f"📄 SLIP {n_up}", key=f"slp_{n_up}", use_container_width=True):
                        slip_h = f"""<div style="background: white; padding: 25px; border-radius: 15px; border: 1px solid #eee; font-family: sans-serif; width: 300px; margin: auto; color: #333;"><center><h3 style="color: #1d976c;">PINTAR MEDIA</h3></center><hr><table style="width: 100%; font-size: 12px; line-height: 2;"><tr><td>Nama</td><td align="right"><b>{n_up}</b></td></tr><tr><td>Gapok</td><td align="right">{g_p:,}</td></tr><tr><td>Tunjangan</td><td align="right">{t_j:,}</td></tr><tr style="color: #1d976c;"><td>Bonus</td><td align="right">+{b_c:,}</td></tr><tr style="background: #1a1a1a; color: white;"><td>TOTAL</td><td align="right"><b>{t_n:,}</b></td></tr></table></div>"""
                        st.components.v1.html(slip_h, height=450)

    except Exception as e:
        st.error(f"⚠️ Sesuai Referensi, Error di: {e}")
