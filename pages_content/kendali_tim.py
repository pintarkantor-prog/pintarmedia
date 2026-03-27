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
            with st.spinner("⏳ Menghubungkan ke Pusat Data..."):
                st.cache_data.clear()
                time.sleep(1.5)
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

        # DETEKSI KOLOM STAFF
        c_gp = next((c for c in df_staff.columns if c.lower() == 'gaji_pokok'), 'Gaji_Pokok')
        c_tj = next((c for c in df_staff.columns if c.lower() == 'tunjangan'), 'Tunjangan')
        c_lv = next((c for c in df_staff.columns if c.lower() == 'level'), 'Level')
        
        df_staff_real = df_staff[df_staff[c_lv].fillna('').astype(str).str.upper().isin(['STAFF', 'UPLOADER', 'ADMIN'])]
        total_gapok = 0
        for _, s in df_staff_real.iterrows():
            total_gapok += int(str(s.get(c_gp, '0')).replace('.', '') or 0) + int(str(s.get(c_tj, '0')).replace('.', '') or 0)

        total_out_riil = total_gapok + bonus_val + ops_val
        saldo_riil = inc_val - total_out_riil
        margin_val = (saldo_riil / inc_val * 100) if inc_val > 0 else 0

        # --- 6. UI: FINANCIAL DASHBOARD ---
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

            with col_logs:
                with st.container(height=315):
                    if not df_k_f.empty:
                        for _, r in df_k_f.sort_values(by='TGL_DT', ascending=False).head(15).iterrows():
                            color = "#00ba69" if str(r.get(col_tipe, '')).upper() == "PENDAPATAN" else "#ff4b4b"
                            tgl_log = r['TGL_DT'].strftime('%d %b') if pd.notnull(r['TGL_DT']) else "-"
                            st.markdown(f"""
                            <div style='font-size:12px; border-bottom:1px solid #333; padding:4px 0;'>
                                <b style='color:#ccc;'>{r.get(col_kat, 'KAS')}</b> 
                                <span style='float:right; color:{color}; font-weight:bold;'>Rp {r['NOM_VAL']:,.0f}</span><br>
                                <small style='color: #888; font-style: italic;'>[{tgl_log}] - {r.get(col_ket, '-')}</small>
                            </div>""", unsafe_allow_html=True)

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

        # ======================================================================
        # --- 7. RINCIAN GAJI & SLIP (STYLE MEWAH - LOGIKA SIMPLE) ---
        # ======================================================================
        with st.expander("💰 RINCIAN GAJI & SLIP", expanded=False):
            try:
                # Ambil kolom secara dinamis biar anti-error
                c_lv = next((c for c in df_staff.columns if c.lower() == 'level'), 'Level')
                c_gp = next((c for c in df_staff.columns if c.lower() == 'gaji_pokok'), 'Gaji_Pokok')
                c_tj = next((c for c in df_staff.columns if c.lower() == 'tunjangan'), 'Tunjangan')
                c_jab = next((c for c in df_staff.columns if c.lower() == 'jabatan'), 'Jabatan')
                
                df_staff_raw_slip = df_staff[df_staff[c_lv].fillna('').astype(str).str.upper().isin(['STAFF', 'UPLOADER', 'ADMIN'])].copy()
                kol_v = st.columns(2) 
                
                for idx, s in df_staff_raw_slip.reset_index(drop=True).iterrows():
                    c_nama = next((c for c in s.index if c.lower() == 'nama'), 'Nama')
                    n_up = str(s.get(c_nama, '')).strip().upper()
                    if n_up == "" or n_up == "NAN": continue
                    
                    # Logika Gaji Simple (Web Baru)
                    v_gapok = int(pd.to_numeric(str(s.get(c_gp, '0')).replace('.','').strip(), errors='coerce') or 0)
                    v_tunjangan = int(pd.to_numeric(str(s.get(c_tj, '0')).replace('.','').strip(), errors='coerce') or 0)
                    jabatan_staf = str(s.get(c_jab, 'STAFF PRODUCTION')).upper() 
                    
                    # Bonus ditarik dari Kas (Gaji Tim)
                    bonus_cair = 0
                    if not df_k_f.empty:
                        mask = (df_k_f[col_kat].fillna('').astype(str).str.upper() == 'GAJI TIM') & \
                               (df_k_f[col_ket].fillna('').astype(str).str.upper().str.contains(n_up, na=False))
                        bonus_cair = int(df_k_f[mask]['NOM_VAL'].sum())
                    
                    v_total = v_gapok + v_tunjangan + bonus_cair

                    with kol_v[idx % 2]:
                        with st.container(border=True):
                            # --- VCARD STYLE LAMA ---
                            st.markdown(f"""
                            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;">
                                <div style="background: linear-gradient(135deg, #1d976c, #93f9b9); color: white; width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 18px;">{n_up[0]}</div>
                                <div><b style="font-size: 15px;">{n_up}</b><br><span style="font-size: 11px; color: #888;">{jabatan_staf}</span></div>
                            </div>""", unsafe_allow_html=True)
                            
                            c1, c2 = st.columns(2)
                            c1.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>ESTIMASI TERIMA</small></p><h3 style='margin:0; color:#1d976c;'>Rp {v_total:,}</h3>", unsafe_allow_html=True)
                            c2.markdown(f"<p style='margin:0; font-size:10px; color:#888;'>STATUS</p><b style='font-size:14px; 'color:#1d976c;'>✅AKTIF</b>", unsafe_allow_html=True)
                            
                            st.divider()

                            # --- SLIP DIGITAL DENGAN LOGO ---
                            if st.button(f"📄 PREVIEW & PRINT SLIP {n_up}", key=f"slp_{n_up}", use_container_width=True):
                                slip_html = f"""
                                <div style="background: white; padding: 30px; border-radius: 20px; border: 1px solid #eee; font-family: sans-serif; width: 350px; margin: auto; color: #333; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                                    <center>
                                        <img src="https://raw.githubusercontent.com/pintarkantor-prog/pintarmedia/main/PINTAR.png" style="width: 200px; margin-bottom: 10px;">
                                        <div style="height: 3px; background: #1d976c; width: 50px; border-radius: 10px; margin: 10px 0;"></div>
                                        <p style="font-size: 10px; letter-spacing: 4px; color: #1d976c; font-weight: 800; text-transform: uppercase;">Slip Gaji Resmi</p>
                                    </center>
                                    <div style="background: #fcfcfc; padding: 15px; border-radius: 12px; border: 1px solid #f0f0f0; margin: 20px 0;">
                                        <table style="width: 100%; font-size: 11px; border-collapse: collapse;">
                                            <tr><td style="color: #999; font-weight: 600;">NAMA</td><td align="right"><b>{n_up}</b></td></tr>
                                            <tr><td style="color: #999; font-weight: 600;">JABATAN</td><td align="right"><b>{jabatan_staf}</b></td></tr>
                                            <tr><td style="color: #999; font-weight: 600;">PERIODE</td><td align="right"><b>{pilihan_nama} {tahun_dipilih}</b></td></tr>
                                        </table>
                                    </div>
                                    <table style="width: 100%; font-size: 13px; line-height: 2.2; border-collapse: collapse;">
                                        <tr><td style="color: #666;">Gaji Pokok</td><td align="right" style="font-weight: 600;">Rp {v_gapok:,}</td></tr>
                                        <tr><td style="color: #666;">Tunjangan</td><td align="right" style="font-weight: 600;">Rp {v_tunjangan:,}</td></tr>
                                        <tr style="color: #1d976c; font-weight: 600;"><td>Bonus Terbayar</td><td align="right">+ {bonus_cair:,}</td></tr>
                                    </table>
                                    <div style="background: #1a1a1a; color: white; padding: 15px; border-radius: 15px; text-align: center; margin-top: 25px;">
                                        <p style="margin: 0; font-size: 9px; color: #55efc4; text-transform: uppercase; letter-spacing: 2px; font-weight: 700;">Total Diterima</p>
                                        <h2 style="margin: 5px 0 0; font-size: 26px; color: #55efc4; font-weight: 800;">Rp {v_total:,}</h2>
                                    </div>
                                    <div style="margin-top: 30px; text-align: center; font-size: 9px; color: #bbb; border-top: 1px solid #f5f5f5; padding-top: 15px;">
                                        <b>Diterbitkan secara digital oleh Sistem PINTAR MEDIA</b><br>
                                        Waktu Cetak: {sekarang.strftime('%d/%m/%Y %H:%M:%S')} WIB
                                    </div>
                                </div>
                                <center><button onclick="window.print()" style="margin-top:20px; padding:10px 20px; background:#1a1a1a; color:#55efc4; border:2px solid #55efc4; border-radius:10px; cursor:pointer; font-weight:bold;">🖨️ CETAK KE PDF</button></center>
                                """
                                st.components.v1.html(slip_html, height=750)
            
            except Exception as e_slip:
                st.error(f"⚠️ Gagal Slip: {e_slip}")

        # ======================================================================
        # --- 8. MANAJEMEN TIM TOTAL (MURNI STREAMLIT) ---
        # ======================================================================
        with st.expander("⚙️ MANAJEMEN TIM & PENGATURAN GAJI", expanded=False):
            
            # --- A. FITUR TAMBAH STAFF BARU ---
            st.markdown("#### ➕ TAMBAH STAFF BARU")
            with st.form("form_tambah_staff", clear_on_submit=True):
                c1, c2, c3 = st.columns(3)
                t_nama = c1.text_input("Nama Lengkap")
                t_jabatan = c2.text_input("Jabatan (Contoh: Staff Editor)")
                t_level = c3.selectbox("Level Akses", ["STAFF", "UPLOADER", "ADMIN", "OWNER"])
                
                c4, c5, c6 = st.columns(3)
                t_gapok = c4.number_input("Gaji Pokok", min_value=0, step=100000)
                t_tunjangan = c5.number_input("Tunjangan", min_value=0, step=50000)
                t_pass = c6.text_input("Password Login", type="password")
                
                if st.form_submit_button("🚀 DAFTARKAN STAFF BARU", use_container_width=True):
                    if t_nama and t_pass:
                        try:
                            database.supabase.table("Staff").insert({
                                "Nama": t_nama.upper(), "Jabatan": t_jabatan, "Level": t_level,
                                "Gaji_Pokok": str(int(t_gapok)), "Tunjangan": str(int(t_tunjangan)), "Password": t_pass
                            }).execute()
                            st.success(f"OK! {t_nama} resmi terdaftar."); time.sleep(1); st.rerun()
                        except Exception as e: st.error(f"Gagal: {e}")

            st.divider()

            # --- B. FITUR EDIT & HAPUS STAFF LAMA ---
            st.markdown("#### 📝 EDIT ATAU BERHENTIKAN STAFF")
            
            # Deteksi Kolom (Antisipasi Case Supabase lo)
            c_nm = next((c for c in df_staff.columns if c.lower() == 'nama'), 'Nama')
            c_jb = next((c for c in df_staff.columns if c.lower() == 'jabatan'), 'Jabatan')
            c_lv = next((c for c in df_staff.columns if c.lower() == 'level'), 'Level')
            c_gp = next((c for c in df_staff.columns if c.lower() == 'gaji_pokok'), 'Gaji_Pokok')
            c_tj = next((c for c in df_staff.columns if c.lower() == 'tunjangan'), 'Tunjangan')
            c_pw = next((c for c in df_staff.columns if c.lower() == 'password'), 'Password')
            c_id = next((c for c in df_staff.columns if c.lower() == 'id'), 'id')

            # Filter selain OWNER
            df_manage = df_staff[df_staff[c_lv].fillna('').astype(str).str.upper() != 'OWNER'].copy()

            for _, s in df_manage.iterrows():
                sid = s.get(c_id)
                with st.container(border=True):
                    # Baris 1: Identitas
                    cols1 = st.columns([2, 2, 1.5, 1.5])
                    u_nama = cols1[0].text_input("Nama Staff", value=str(s.get(c_nm, '')), key=f"unm_{sid}")
                    u_jab = cols1[1].text_input("Jabatan", value=str(s.get(c_jb, '')), key=f"ujb_{sid}")
                    u_lv = cols1[2].selectbox("Level", ["STAFF", "UPLOADER", "ADMIN"], index=["STAFF", "UPLOADER", "ADMIN"].index(str(s.get(c_lv, 'STAFF')).upper()) if str(s.get(c_lv, 'STAFF')).upper() in ["STAFF", "UPLOADER", "ADMIN"] else 0, key=f"ulv_{sid}")
                    u_pw = cols1[3].text_input("Password", value=str(s.get(c_pw, '')), type="password", key=f"upw_{sid}")

                    # Baris 2: Finansial & Tombol
                    cols2 = st.columns([2, 2, 1.5, 1.5])
                    u_gp = cols2[0].text_input("Gaji Pokok", value=str(s.get(c_gp, '0')), key=f"ugp_{sid}")
                    u_tj = cols2[1].text_input("Tunjangan", value=str(s.get(c_tj, '0')), key=f"utj_{sid}")
                    
                    st.write("") # Jeda dikit
                    btn_up = cols2[2].button("💾 UPDATE", key=f"ubtn_{sid}", use_container_width=True)
                    btn_del = cols2[3].button("🗑️ HAPUS", key=f"dbtn_{sid}", use_container_width=True)

                    if btn_up:
                        try:
                            database.supabase.table("Staff").update({
                                c_nm: u_nama.upper(), c_jb: u_jab, c_lv: u_lv,
                                c_gp: u_gp, c_tj: u_tj, c_pw: u_pw
                            }).eq(c_id, sid).execute()
                            st.success("Berhasil Update!"); time.sleep(0.5); st.rerun()
                        except Exception as e: st.error(f"Gagal: {e}")

                    if btn_del:
                        if st.session_state.get('del_confirm') == sid:
                            database.supabase.table("Staff").delete().eq(c_id, sid).execute()
                            st.success("Staff dihapus."); st.session_state.pop('del_confirm'); time.sleep(0.5); st.rerun()
                        else:
                            st.session_state['del_confirm'] = sid
                            st.warning("Klik HAPUS sekali lagi!")
            else:
                st.warning("Tidak ada data staff untuk diedit.")

    except Exception as e:
        st.error(f"⚠️ Sistem Error: {e}")
