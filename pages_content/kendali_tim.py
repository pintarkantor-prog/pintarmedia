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

        # --- 4. SARING DATA (PAKE NAMA KOLOM DI GAMBAR: 'Tanggal') ---
        if not df_kas_raw.empty:
            df_kas_raw['TGL_DT'] = pd.to_datetime(df_kas_raw['Tanggal'], errors='coerce')
            df_k_f = df_kas_raw[(df_kas_raw['TGL_DT'].dt.month == bulan_dipilih) & (df_kas_raw['TGL_DT'].dt.year == tahun_dipilih)].copy()
            
            # Cleaning nominal (Biar Log gak Rp 0)
            df_k_f['NOM_VAL'] = pd.to_numeric(df_k_f['Nominal'].astype(str).replace(r'[^\d.]', '', regex=True), errors='coerce').fillna(0)
        else:
            df_k_f = pd.DataFrame()

        # --- 5. KALKULASI METRIK ---
        inc, bonus_k, ops = 0, 0, 0
        if not df_k_f.empty:
            inc = df_k_f[df_k_f['Tipe'].fillna('').astype(str).str.upper() == 'PENDAPATAN']['NOM_VAL'].sum()
            ops = df_k_f[(df_k_f['Tipe'].fillna('').astype(str).str.upper() == 'PENGELUARAN') & (df_k_f['Kategori'].fillna('').astype(str).str.upper() != 'GAJI TIM')]['NOM_VAL'].sum()
            bonus_k = df_k_f[(df_k_f['Tipe'].fillna('').astype(str).str.upper() == 'PENGELUARAN') & (df_k_f['Kategori'].fillna('').astype(str).str.upper() == 'GAJI TIM')]['NOM_VAL'].sum()

        # HITUNG GAPOK TIM (SESUAI GAMBAR STAFF: 'Gaji_Pokok', 'Tunjangan')
        total_gapok = 0
        df_staff_real = df_staff[df_staff['Level'].fillna('').astype(str).str.upper().isin(['STAFF', 'UPLOADER', 'ADMIN'])]
        for _, s in df_staff_real.iterrows():
            total_gapok += int(str(s.get('Gaji_Pokok', '0')).replace('.', '') or 0) + int(str(s.get('Tunjangan', '0')).replace('.', '') or 0)

        total_out = total_gapok + bonus_k + ops
        saldo = inc - total_out
        margin = (saldo / inc * 100) if inc > 0 else 0

        # ======================================================================
        # --- 6. UI: FINANCIAL DASHBOARD ---
        # ======================================================================
        with st.expander("💰 ANALISIS KEUANGAN & KAS", expanded=True):
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("💰 INCOME", f"Rp {inc:,.0f}")
            m2.metric("💸 OUTCOME", f"Rp {total_out:,.0f}", delta=f"-Rp {total_out:,.0f}" if total_out > 0 else None, delta_color="normal")
            
            status_s = "SURPLUS" if saldo >= 0 else "DEFISIT"
            warna_d = "normal" if saldo >= 0 else "inverse"
            m3.metric("📈 SALDO BERSIH", f"Rp {saldo:,.0f}", delta=status_s, delta_color=warna_d)
            m4.metric("📊 MARGIN", f"{margin:.1f}%")

            st.divider()

            col_in, col_log, col_viz = st.columns([1, 1.2, 1], gap="small")
            with col_in:
                with st.form("form_kas_dian", clear_on_submit=True):
                    f_tipe = st.pills("Tipe", ["PENDAPATAN", "PENGELUARAN"], default="PENGELUARAN", label_visibility="collapsed")
                    f_kat = st.selectbox("Kategori", ["YouTube", "Brand Deal", "Gaji Tim", "Operasional", "Lainnya"], label_visibility="collapsed")
                    f_nom = st.number_input("Nominal", min_value=0, step=50000, label_visibility="collapsed")
                    f_ket = st.text_area("Ket...", height=65, label_visibility="collapsed")
                    if st.form_submit_button("🚀 SIMPAN", use_container_width=True):
                        database.supabase.table("Arus_Kas").insert({"Tanggal": sekarang.strftime('%Y-%m-%d'), "Tipe": f_tipe, "Kategori": f_kat, "Nominal": str(int(f_nom)), "Keterangan": f_ket, "Pencatat": user_sekarang}).execute()
                        st.success("OK!"); time.sleep(0.5); st.rerun()

            with col_log:
                with st.container(height=315):
                    if not df_k_f.empty:
                        # FIX LOG: Gunakan NOM_VAL biar gak Rp 0
                        for _, r in df_k_f.sort_values(by='TGL_DT', ascending=False).head(15).iterrows():
                            warna_log = "#00ba69" if str(r.get('Tipe', '')).upper() == "PENDAPATAN" else "#ff4b4b"
                            st.markdown(f"""
                            <div style='font-size:11px; border-bottom:1px solid #333; padding:4px 0;'>
                                <b>{r.get('Kategori', 'KAS')}</b> 
                                <span style='float:right; color:{warna_log}; font-weight:bold;'>Rp {r.get('NOM_VAL', 0):,.0f}</span><br>
                                <small style='color:#888;'>{r.get('Keterangan', '-')}</small>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.caption("Belum ada data.")

            with col_viz:
                if (inc + total_out) > 0:
                    fig = px.pie(values=[inc, total_out], names=['INC', 'OUT'], hole=0.75, color_discrete_sequence=["#00ba69", "#ff4b4b"])
                    fig.update_layout(showlegend=False, height=200, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
                    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        # ======================================================================
        # --- 7. UI: RINCIAN GAJI & SLIP (ANTI-ERROR 'Keterangan') ---
        # ======================================================================
        st.write(""); st.markdown("### 📄 RINCIAN GAJI & SLIP STAFF")
        kol_v = st.columns(2) 
        df_staff_slip = df_staff_real.reset_index(drop=True)
        
        for idx, s in df_staff_slip.iterrows():
            n_up = str(s.get('Nama', '')).strip().upper()
            if n_up == "" or n_up == "NAN": continue
            
            g_p = int(pd.to_numeric(str(s.get('Gaji_Pokok', '0')).replace('.',''), errors='coerce') or 0)
            t_j = int(pd.to_numeric(str(s.get('Tunjangan', '0')).replace('.',''), errors='coerce') or 0)
            
            # CARI BONUS: Gunakan kolom 'Keterangan' dengan Title Case
            b_c = 0
            if not df_k_f.empty:
                # Cari baris yang Kategori-nya Gaji Tim dan Keterangan-nya ada nama staf
                mask_bonus = (df_k_f['Kategori'].fillna('').astype(str).str.upper() == 'GAJI TIM') & \
                             (df_k_f['Keterangan'].fillna('').astype(str).str.upper().str.contains(n_up, na=False))
                b_c = int(df_k_f[mask_bonus]['NOM_VAL'].sum())
            
            t_n = g_p + t_j + b_c

            with kol_v[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"""<div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;"><div style="background: linear-gradient(135deg, #1d976c, #93f9b9); color: white; width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 18px;">{n_up[0]}</div><div><b>{n_up}</b><br><small>{s.get('Jabatan', 'STAFF')}</small></div></div>""", unsafe_allow_html=True)
                    c1, c2 = st.columns(2)
                    c1.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>ESTIMASI TERIMA</p><h3 style='margin:0; color:#1d976c;'>Rp {t_n:,}</h3>", unsafe_allow_html=True)
                    c2.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>STATUS</p><b style='color:#1d976c;'>AKTIF</b>", unsafe_allow_html=True)
                    
                    if st.button(f"📄 SLIP {n_up}", key=f"slp_{n_up}", use_container_width=True):
                        slip_h = f"""<div style="background: white; padding: 25px; border-radius: 15px; border: 1px solid #eee; font-family: sans-serif; width: 300px; margin: auto; color: #333;"><center><h3 style="color: #1d976c;">PINTAR MEDIA</h3></center><hr><table style="width: 100%; font-size: 12px; line-height: 2;"><tr><td>Nama</td><td align="right"><b>{n_up}</b></td></tr><tr><td>Gapok</td><td align="right">Rp {g_p:,}</td></tr><tr><td>Tunjangan</td><td align="right">Rp {t_j:,}</td></tr><tr style="color: #1d976c;"><td>Bonus</td><td align="right">+{b_c:,}</td></tr><tr style="background: #1a1a1a; color: white;"><td style="padding:10px;">TOTAL</td><td align="right" style="padding:10px;"><b>Rp {t_n:,}</b></td></tr></table></div>"""
                        st.components.v1.html(slip_h, height=450)

    except Exception as e:
        st.error(f"⚠️ Sesuai Referensi, Error di: {e}")
