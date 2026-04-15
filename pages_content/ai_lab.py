import streamlit as st
from datetime import datetime, timedelta

def tampilkan_halaman():
    # --- 1. PINTU UTAMA: CEK IZIN AKSES ---
    sekarang = datetime.utcnow() + timedelta(hours=7) 
    hari_id = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    bulan_id = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    nama_hari = hari_id[sekarang.weekday()]
    nama_bulan = bulan_id[sekarang.month - 1]
    tgl = sekarang.day
    tahun = sekarang.year
    
    user_aktif = st.session_state.get("user_aktif", "USER").upper()
    user_level = st.session_state.get("user_level", "STAFF").upper()

    # Cek apakah level user ada di daftar yang diizinkan
    izin_akses = ["OWNER", "ADMIN", "UPLOADER", "STAFF"]
    
    if user_level not in izin_akses:
        st.error(f"🚫 Maaf {user_aktif}, Area ini terbatas untuk tim internal.")
        st.stop()

    # --- 2. TAMPILAN UTAMA ---
    st.title("🧠 PINTAR AI LAB")
    st.markdown(f"**{user_aktif}** | 📅 {nama_hari}, {tgl} {nama_bulan} {tahun}")

    # --- 3. TABS MENU (Dian's New Menu) ---
    t_masjid_v1, t_masjid_v2, t_roblox, t_minecraft, t_random = st.tabs([
        "🕌 MINIATUR MASJID", 
        "🎋 MASJID VERSI BARU", 
        "🎮 ROBLOX", 
        "⛏️ MINECRAFT", 
        "🎲 RANDOM"
    ])
                
    # ==========================================================================
    # TAB 1: MINIATUR MASJID
    # ==========================================================================
    with t_masjid_v1:
        with st.container(border=True):
            
            col_meta1, col_meta2 = st.columns(2)
            with col_meta1:
                st.info("**💡 SOP PENGGUNAAN GENERATOR PROMPT**")
                st.write("- **WAJIB** Selalu acak pilihan `Karakter`, `Bahan Masjid`, `Pakaian` dan `Lokasi`.")
                st.write("- Pada `ACTING & PERFORMANCE` juga di acak pilihan `Logat`, `Mood` dan `Gerakan Tubuh`.")
                st.write("- Bagian `DIALOG` juga diacak, disesuaikan dengan update dialog terbaru.")
                
            with col_meta2:
                st.success("**🛡️ QUALITY CONTROL ( WAJIB CEK )**")
                st.write("- Cek hasil video, Apakah ada `Penampakan Aneh` ( *masjidnya, suaranya, tangan, jari, dll* ).")
                st.write("- Download gambar di `GEMINI FLOW` pilih yang ukuran 2K, boleh pilih 1K *jika akun limit*.")
                st.write("- Download hasil video di `GROK` wajib ukuran minimal `720p` ( *Tidak boleh 480p* ).")
        
        st.warning("💡 **Saat setor ke Admin**, Pisahkan hasil video kakek dan nenek ( *jangan dijadikan satu folder* )")           
        st.write("") # Spacing
		
		# --- 1. MASTER DNA MANUSIA ASLI (FULL BODY & NATURAL SKIN) ---
        MASTER_FAMILY_SOUL = {
            # === NENEK ===
            "Nenek Aminah": (
                "IDENTITY: Frail 88-year-old Javanese grandmother. "
                "FACE: Long narrow face with high cheekbones, deep vertical wrinkles on the cheeks, heavy sagging skin along the jawline, warm sawo matang skin with golden undertone and scattered dark liver spots. "
                "EYES: Deeply sunken eyes with heavy drooping upper eyelids and soft lower eye bags. "
                "BODY: Tall but severely shrunken and thin frame, slightly hunched shoulders, thin neck with visible tendons. "
                "MOUTH: Thin lips with gentle downward sagging at the corners."
            ),
            "Nenek Siti": (
                "IDENTITY: Frail 73-year-old petite Javanese grandmother. "
                "FACE: Small round plump face with full soft cheeks that sag due to age, warm langsat skin with yellowish undertone and natural glow. "
                "EYES: Large round eyes with heavy eyelid droop and mild under-eye puffiness. "
                "BODY: Tiny delicate frame with short neck and still some remaining softness. "
                "MOUTH: Plump lower lip that sags softly with loose skin at the corners."
            ),
            "Nenek Marsi": (
                "IDENTITY: Frail 94-year-old Javanese grandmother. "
                "FACE: Wide square face with prominent cheekbones, deep horizontal forehead wrinkles, loose skin under the chin, deep warm sawo matang skin with many age spots and golden undertone. "
                "EYES: Narrow eyes mostly covered by thick heavy upper lids. "
                "BODY: Broad shoulders but very thin arms and chest, frail hunched posture. "
                "MOUTH: Wide mouth with deep folds from nose to chin."
            ),
            "Nenek Ponirah": (
                "IDENTITY: Frail 80-year-old Javanese grandmother. "
                "FACE: Round full face with heavy sagging cheeks and soft jawline, warm brownish skin with natural sun-kissed tone. "
                "EYES: Almond-shaped eyes with noticeable lower eye bags. "
                "BODY: Sedang plump but shrunken frame with loose skin on arms and neck. "
                "MOUTH: Naturally curved lips surrounded by fine radiating wrinkles."
            ),
            "Nenek Juminah": (
                "IDENTITY: Frail 91-year-old very thin Javanese grandmother. "
                "FACE: Sharp angular tirus face with sunken temples, high forehead, warm tan skin with golden undertone stretched over bones. "
                "EYES: Deep-set eyes with thin eyelids and soft dark circles. "
                "BODY: Extremely thin bony frame with long thin neck and visible shoulder bones. "
                "MOUTH: Very thin lips with fine vertical wrinkles."
            ),
            "Nenek Sikem": (
                "IDENTITY: Frail 76-year-old Javanese grandmother. "
                "FACE: Very round plump face with heavy lower cheeks and multiple soft folds under the chin, warm sawo matang skin with golden undertone. "
                "EYES: Small eyes almost hidden under thick puffy eyelids. "
                "BODY: Short rounded frame with remaining softness but clear frailty. "
                "MOUTH: Wide loose mouth with noticeable sagging of the lower lip."
            ),
            "Nenek Dulah": (
                "IDENTITY: Frail 68-year-old Sundanese grandmother. "
                "FACE: Soft oval face with naturally full cheeks that sag gently, bright warm langsat skin with yellowish golden undertone. "
                "EYES: Gentle almond eyes with soft under-eye hollows. "
                "BODY: Soft fragile frame with rounded shoulders and thin arms. "
                "MOUTH: Full lips that sag softly at the corners."
            ),
            "Nenek Sartini": (
                "IDENTITY: Frail 84-year-old Sundanese grandmother. "
                "FACE: Wide round face with heavy sagging cheeks and deep gentle folds from nose to mouth on warm brownish skin with golden undertone. "
                "EYES: Wide-set eyes with heavy upper lids and calm tired expression. "
                "BODY: Plump but frail frame with loose skin on upper arms. "
                "MOUTH: Broad mouth with loose corners and soft wrinkles."
            ),
            "Nenek Tinah": (
                "IDENTITY: Frail 93-year-old thin Javanese grandmother. "
                "FACE: Long oval tirus face with deeply sunken cheeks and sharp jawline on warm tan skin with golden undertone. "
                "EYES: Deep sunken eyes with heavy lids and minimal surrounding fat. "
                "BODY: Very thin elongated shrunken frame with prominent bones. "
                "MOUTH: Thin lips with many fine vertical wrinkles."
            ),
            "Nenek Wati": (
                "IDENTITY: Frail 64-year-old small Sundanese grandmother. "
                "FACE: Small delicate round face with soft heavy sagging skin on the cheeks and warm langsat tone with golden undertone. "
                "EYES: Large gentle eyes with heavy drooping lids and soft under-eye bags. "
                "BODY: Very small delicate frame with thin wrists, still has some youthful roundness. "
                "MOUTH: Small mouth with subtle sagging of the lower lip."
            ),

            # === KAKEK ===
            "Kakek Marto": (
                "IDENTITY: Frail 87-year-old Javanese grandfather. "
                "FACE: Long rectangular face with strong jawline, deep forehead wrinkles, rough warm sawo matang skin with golden undertone. "
                "EYES: Deep-set eyes with thick brows and heavy lower lids. "
                "BODY: Lean bony frame with slightly hunched shoulders and thin arms. "
                "MOUTH: Wide mouth with thick aged lips."
            ),
            "Kakek Somo": (
                "IDENTITY: Frail 79-year-old Javanese grandfather. "
                "FACE: Round soft face with heavy jowls and multiple soft folds under the chin on warm brownish skin with golden undertone. "
                "EYES: Small tired eyes almost hidden under puffy eyelids. "
                "BODY: Short rounded fragile frame with loose skin on the neck. "
                "MOUTH: Full sagging lips."
            ),
            "Kakek Joyo": (
                "IDENTITY: Frail 90-year-old Javanese grandfather. "
                "FACE: Square face with prominent brow ridge, deep wrinkles, leathery rough warm sun-exposed skin with golden undertone. "
                "EYES: Narrow eyes with heavy lids. "
                "BODY: Once sturdy but now shrunken frame with visible shoulder bones. "
                "MOUTH: Wide firm mouth with deep wrinkles."
            ),
            "Kakek Hardi": (
                "IDENTITY: Extremely frail 95-year-old Javanese grandfather. "
                "FACE: Extremely shrunken face with hollow cheeks, thin translucent warm tan skin with golden undertone. "
                "EYES: Deep sunken cloudy eyes with thin eyelids. "
                "BODY: Very thin delicate frame with prominent collarbones. "
                "MOUTH: Thin stretched lips."
            ),
            "Kakek Sableng": (
                "IDENTITY: Frail 83-year-old Javanese grandfather. "
                "FACE: Broad face with high cheekbones and heavy fatigue lines on warm tan skin with golden undertone. "
                "EYES: Tired eyes with heavy lower lids. "
                "BODY: Lean frame with slightly hunched posture. "
                "MOUTH: Wide mouth with noticeable sagging."
            ),
            "Kakek Sinto": (
                "IDENTITY: Extremely frail 94-year-old Javanese grandfather. "
                "FACE: Deeply sunken skeletal face with hollow cheeks and thin warm tan skin with golden undertone. "
                "EYES: Deep sunken cloudy eyes with thin eyelids. "
                "BODY: Very thin delicate frame with bony hands. "
                "MOUTH: Thin stretched lips."
            ),
            "Kakek Wiryo": (
                "IDENTITY: Frail 74-year-old Javanese grandfather. "
                "FACE: Broad labor-worn face with high cheekbones, deep pores, rough warm sawo matang skin with golden undertone. "
                "EYES: Tired eyes with heavy lower lids. "
                "BODY: Lean weathered frame with slightly hunched shoulders. "
                "MOUTH: Wide mouth with thick aged lips."
            ),
            "Kakek Usman": (
                "IDENTITY: Frail 86-year-old Indonesian grandfather. "
                "FACE: Deeply wrinkled face with prominent fatigue lines and sunken cheeks on warm brownish skin with golden undertone. "
                "EYES: Heavy-lidded eyes with weary appearance. "
                "BODY: Thin frame with slow movements and slightly rounded shoulders. "
                "MOUTH: Relaxed mouth with natural aged lip texture."
            )
        }
		# --- 2. MASTER WARDROBE (6 VARIAN PER KARAKTER - DAILY & NEAT HIJAB) ---
        MASTER_FAMILY_WARDROBE = {
            # --- KELOMPOK NENEK ---
            "Nenek Aminah": {
                "Daster Rayon Motif Floral Lembut": "Wearing a loose soft rayon daster with delicate faded floral pattern in gentle natural tones. Lightweight breathable fabric with soft drape. Paired with a simple matching instant bergo hijab.",
                "Daster Kaos Motif Batik Parang": "Wearing an oversized soft cotton daster with subtle faded parang batik pattern. Comfortable daily fabric. Paired with a simple neutral jersey hijab.",
                "Daster Polos Katun Harian": "Wearing a plain faded cotton daster in soft natural color with loose comfortable fit. Paired with a simple instant hijab.",
                "Kaos Lengan Panjang + Sarung Batik": "Wearing a loose long-sleeved soft cotton shirt paired with a classic faded batik sarong. Paired with a simple neutral hijab.",
                "Daster Kancing Depan Motif Geometris": "Wearing a front-button rayon daster with subtle geometric pattern in muted natural tones. Lightweight and modest. Paired with a simple instant hijab.",
                "Daster Rayon Motif Daun": "Wearing a loose rayon daster with soft faded leaf motif in gentle natural colors. Comfortable home outfit. Paired with a simple bergo hijab."
            },
            "Nenek Siti": {
                "Daster Kaos Motif Bunga Kecil": "Wearing a soft cotton daster with tiny faded floral pattern in soft natural tones. Lightweight and comfortable. Paired with a simple neutral hijab.",
                "Daster Rayon Motif Sogan": "Wearing a traditional Javanese rayon daster with faded soft Sogan batik pattern. Gentle fabric drape. Paired with a simple instant hijab.",
                "Daster Polos Katun": "Wearing a plain faded cotton daster in soft natural color with loose fit. Paired with a simple hijab.",
                "Kaos Lengan Panjang + Jarik": "Wearing a loose long-sleeved soft cotton shirt paired with a faded batik jarik. Paired with a simple neutral hijab.",
                "Daster Kancing Depan Motif Garis": "Wearing a front-button cotton daster with subtle faded stripe pattern. Lightweight daily wear. Paired with a simple hijab.",
                "Daster Rayon Motif Abstrak Lembut": "Wearing a loose rayon daster with soft faded abstract pattern in gentle natural tones. Comfortable home outfit. Paired with a simple hijab."
            },
            "Nenek Marsi": {
                "Daster Batik Lembut": "Wearing a thin soft batik rayon daster in muted traditional tones. Light fabric with natural drape. Paired with a simple instant hijab.",
                "Kaos Panjang + Jarik": "Wearing a loose long-sleeved soft cotton shirt paired with a faded batik jarik. Traditional modest home outfit. Paired with a simple hijab.",
                "Daster Polos Katun Tipis": "Wearing a plain soft cotton daster with loose comfortable fit. Paired with a simple hijab.",
                "Tunik Katun Sederhana": "Wearing a loose cotton tunic in soft faded natural tones. Modest and comfortable daily wear. Paired with a simple hijab.",
                "Daster Kancing Depan": "Wearing a front-button cotton daster in muted natural color. Simple and practical. Paired with a simple hijab.",
                "Daster Motif Geometris Lembut": "Wearing a loose rayon daster with subtle geometric pattern in gentle natural tones. Paired with a simple hijab."
            },
            "Nenek Ponirah": {
                "Daster Kaos Motif Mega Mendung": "Wearing an oversized cotton daster with faded soft Mega Mendung pattern in muted natural tones. Comfortable fabric. Paired with a simple bergo hijab.",
                "Setelan Rumah Rayon": "Wearing a matching loose rayon top and pants in soft faded natural tones. Modest daily wear. Paired with a simple instant hijab.",
                "Daster Kancing Depan Motif Geometris": "Wearing a front-button cotton daster with subtle geometric pattern in muted tones. Lightweight daily outfit. Paired with a simple hijab.",
                "Tunik Katun + Jarik": "Wearing a modest long-sleeved cotton tunic paired with a faded batik jarik. Paired with a simple hijab.",
                "Daster Rayon Motif Daun": "Wearing a loose rayon daster with soft leaf motif in gentle natural tones. Comfortable home wear. Paired with a simple hijab.",
                "Kaos Polo Lengan Panjang + Sarung": "Wearing a modest long-sleeved cotton polo in soft natural tone paired with a faded batik sarong. Paired with a simple hijab."
            },
            "Nenek Juminah": {
                "Daster Rayon Motif Floral": "Wearing a loose rayon daster with soft faded floral pattern in gentle natural tones. Lightweight and comfortable. Paired with a simple hijab.",
                "Kaos Lengan Panjang + Sarung": "Wearing a loose long-sleeved soft cotton shirt paired with a faded batik sarong. Simple daily home outfit. Paired with a simple hijab.",
                "Daster Kaos Polos": "Wearing a plain faded cotton daster with loose fit in soft natural color. Paired with a simple hijab.",
                "Daster Kancing Depan Motif Garis": "Wearing a front-button cotton daster with subtle faded stripe pattern. Lightweight daily wear. Paired with a simple hijab.",
                "Tunik Katun Sederhana": "Wearing a loose cotton tunic in soft faded tone. Modest and comfortable. Paired with a simple hijab.",
                "Daster Rayon Motif Abstrak": "Wearing a loose rayon daster with soft faded abstract pattern in gentle natural tones. Paired with a simple hijab."
            },
            "Nenek Sikem": {
                "Daster Kaos Motif Bunga Kecil": "Wearing a soft cotton daster with tiny faded floral pattern in muted natural tones. Lightweight daily wear. Paired with a simple black jersey bergo hijab.",
                "Daster Polos Katun": "Wearing a plain faded cotton daster with loose comfortable fit. Paired with a simple grey hijab.",
                "Kaos Lengan Panjang + Jarik": "Wearing a loose long-sleeved soft cotton shirt paired with a faded batik jarik. Paired with a simple neutral hijab.",
                "Daster Kancing Depan": "Wearing a front-button cotton daster in muted natural color. Simple and practical. Paired with a simple hijab.",
                "Daster Rayon Motif Daun": "Wearing a loose rayon daster with soft leaf motif in gentle natural tones. Comfortable home wear. Paired with a simple hijab.",
                "Daster Motif Geometris Lembut": "Wearing a loose rayon daster with subtle geometric pattern in gentle natural tones. Paired with a simple hijab."
            },
            "Nenek Dulah": {
                "Daster Kaos Motif Bunga Kecil": "Wearing a soft cotton daster with tiny faded floral pattern in gentle natural tones. Comfortable daily wear. Paired with a simple grey instant hijab.",
                "Daster Rayon Motif Sogan": "Wearing a traditional Javanese rayon daster with faded soft Sogan batik pattern. Paired with a simple neutral hijab.",
                "Kaos Lengan Panjang + Jarik": "Wearing a loose long-sleeved soft cotton shirt paired with a faded batik jarik. Paired with a simple hijab.",
                "Daster Kancing Depan Motif Abstrak": "Wearing a front-button cotton daster with subtle abstract pattern in muted natural tones. Paired with a simple hijab.",
                "Daster Kaos Garis Halus": "Wearing a striped cotton jersey daster in soft natural tones. Loose comfortable fit. Paired with a simple hijab.",
                "Daster Rayon Motif Daun": "Wearing a loose rayon daster with soft leaf motif in gentle natural tones. Paired with a simple hijab."
            },
            "Nenek Sartini": {
                "Daster Rayon Motif Bunga Matahari": "Wearing a loose rayon daster with soft faded floral pattern in gentle warm tones. Comfortable home dress. Paired with a simple grey jersey bergo hijab.",
                "Daster Kaos Motif Batik Pesisiran": "Wearing a short-sleeved cotton daster with faded traditional batik pattern. Paired with a simple black instant hijab.",
                "Kaos Lengan Panjang + Sarung": "Wearing a plain long-sleeved cotton shirt paired with a faded batik sarong. Paired with a simple neutral hijab.",
                "Daster Kancing Depan Motif Geometris": "Wearing a front-button cotton daster with subtle geometric pattern in muted natural tones. Paired with a simple hijab.",
                "Daster Kaos Polos": "Wearing an oversized plain cotton daster in soft natural tone. Comfortable daily wear. Paired with a simple hijab.",
                "Daster Rayon Motif Batik Cap": "Wearing a loose rayon daster with faded soft batik cap pattern. Paired with a simple dark hijab."
            },
            "Nenek Tinah": {
                "Daster Kaos Motif Floral Lembut": "Wearing an oversized cotton daster with soft faded floral pattern in gentle natural tones. Comfortable daily wear. Paired with a simple black bergo hijab.",
                "Daster Rayon Motif Daun": "Wearing a loose rayon daster with soft leaf motif in gentle natural tones. Paired with a simple grey hijab.",
                "Kaos Lengan Panjang Polos": "Wearing a plain faded long-sleeved cotton shirt paired with a dark batik sarong. Paired with a simple white hijab.",
                "Daster Kancing Depan Garis": "Wearing a front-button cotton daster with subtle faded stripe pattern. Paired with a simple navy hijab.",
                "Daster Kaos Polos": "Wearing an oversized plain cotton daster in soft natural tone. Simple daily home wear. Paired with a simple maroon hijab.",
                "Daster Rayon Motif Abstrak": "Wearing a loose rayon daster with soft faded abstract pattern in gentle natural tones. Paired with a simple dark hijab."
            },
            "Nenek Wati": {
                "Daster Kaos Motif Batik Parang": "Wearing an oversized cotton daster with faded parang batik pattern in soft earthy tones. Soft and comfortable. Paired with a simple black bergo hijab.",
                "Kaos Lengan Panjang Polos": "Wearing a plain faded long-sleeved cotton shirt paired with a dark batik sarong. Paired with a simple white hijab.",
                "Daster Rayon Motif Kembang": "Wearing a loose rayon daster with faded flower pattern in gentle natural tones. Paired with a simple grey hijab.",
                "Daster Kancing Depan Kotak": "Wearing a front-button cotton daster with small faded checkered pattern. Paired with a simple navy hijab.",
                "Daster Kaos Polos": "Wearing a plain oversized cotton daster in soft natural tone. Simple home clothing. Paired with a simple maroon hijab.",
                "Daster Rayon Motif Batik Lembut": "Wearing a loose rayon daster with faded soft batik pattern. Paired with a simple dark brown hijab."
            },

            # --- KELOMPOK KAKEK ---
            "Kakek Marto": {
                "Baju Koko Katun Lembut": "Wearing a simple short-sleeved cotton koko shirt in soft natural tones with comfortable drape. Paired with a classic faded batik sarong and a simple black peci.",
                "Baju Koko Putih Polos": "Wearing a plain white short-sleeved cotton koko shirt with natural wrinkles from daily use. Paired with a faded batik sarong and white peci.",
                "Baju Koko Batik Faded": "Wearing a short-sleeved faded batik koko shirt in earthy tones. Paired with a dark batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a soft faded polo shirt with comfortable fit. Paired with a checkered batik sarong and simple white peci.",
                "Kemeja Flanel Kotak & Sarung": "Wearing a faded checkered flannel shirt over a thin undershirt. Paired with a batik sarong and black peci.",
                "Baju Koko Abu & Sarung Lawas": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and black peci."
            },
            "Kakek Somo": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved cotton koko shirt in soft natural tones. Paired with a faded batik sarong and simple white peci.",
                "Baju Koko Batik Lembut": "Wearing a short-sleeved faded soft batik koko shirt. Paired with a checkered batik sarong and white peci haji.",
                "Baju Koko Biru Muda": "Wearing a simple short-sleeved cotton koko shirt in soft faded tone. Paired with a dark batik sarong and black velvet peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded polo shirt with comfortable collar. Paired with a dark green batik sarong and black peci.",
                "Kemeja Kotak & Sarung": "Wearing a faded checkered short-sleeved shirt. Paired with a maroon batik sarong and white peci haji.",
                "Baju Koko Abu & Sarung": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and simple black peci."
            },
            "Kakek Joyo": {
                "Baju Koko Katun Tebal": "Wearing a short-sleeved cotton koko shirt in soft natural tones. Paired with a checkered batik sarong and black velvet peci.",
                "Baju Koko Putih Lawas": "Wearing a clean white short-sleeved cotton koko shirt with natural wrinkles. Paired with a faded batik sarong and white peci haji.",
                "Baju Koko Batik Faded": "Wearing a short-sleeved faded batik koko shirt in earthy tones. Paired with a navy batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a soft faded polo shirt. Paired with a maroon checkered batik sarong and white knitted peci.",
                "Kemeja Flanel & Sarung": "Wearing a faded flannel shirt. Paired with a dark green batik sarong and black peci.",
                "Baju Koko Abu & Sarung Lawas": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and black peci."
            },
            "Kakek Hardi": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved cotton koko shirt in soft natural tones. Paired with a dark batik sarong and white peci haji.",
                "Baju Koko Biru Muda": "Wearing a short-sleeved cotton koko shirt in soft faded tone. Paired with a maroon batik sarong and black velvet peci.",
                "Baju Koko Batik Lembut": "Wearing a faded soft batik koko shirt. Paired with a checkered batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded polo shirt with comfortable fit. Paired with a dark green batik sarong and white peci.",
                "Kemeja Kotak & Sarung": "Wearing a faded checkered shirt. Paired with a maroon batik sarong and black peci.",
                "Baju Koko Abu & Sarung": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and white peci haji."
            },
            "Kakek Sableng": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved cotton koko shirt in soft natural tones. Paired with a dark batik sarong and black velvet peci.",
                "Baju Koko Putih Lawas": "Wearing a clean white short-sleeved cotton koko shirt. Paired with a maroon batik sarong and white peci haji.",
                "Baju Koko Batik Faded": "Wearing a faded earthy batik koko shirt. Paired with a checkered batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded polo shirt. Paired with a dark green batik sarong and white knitted peci.",
                "Kemeja Flanel & Sarung": "Wearing a faded flannel shirt. Paired with a navy batik sarong and black peci.",
                "Baju Koko Abu & Sarung Lawas": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and black peci."
            },
            "Kakek Sinto": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved cotton koko shirt in soft natural tones. Paired with a dark batik sarong and white peci haji.",
                "Baju Koko Biru Muda": "Wearing a short-sleeved cotton koko shirt in soft faded tone. Paired with a maroon batik sarong and black velvet peci.",
                "Baju Koko Batik Lembut": "Wearing a faded soft batik koko shirt. Paired with a checkered batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded polo shirt. Paired with a dark green batik sarong and white peci.",
                "Kemeja Kotak & Sarung": "Wearing a faded checkered shirt. Paired with a maroon batik sarong and black peci.",
                "Baju Koko Abu & Sarung": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and white peci haji."
            },
            "Kakek Wiryo": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved cotton koko shirt in soft natural tones. Paired with a dark batik sarong and black peci.",
                "Baju Koko Putih Lawas": "Wearing a clean white short-sleeved cotton koko shirt. Paired with a maroon batik sarong and white peci haji.",
                "Baju Koko Batik Faded": "Wearing a faded earthy batik koko shirt. Paired with a checkered batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded polo shirt. Paired with a dark green batik sarong and white knitted peci.",
                "Kemeja Flanel & Sarung": "Wearing a faded flannel shirt. Paired with a navy batik sarong and black peci.",
                "Baju Koko Abu & Sarung Lawas": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and black peci."
            },
            "Kakek Usman": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved cotton koko shirt in soft natural tones. Paired with a dark batik sarong and white peci haji.",
                "Baju Koko Biru Muda": "Wearing a short-sleeved cotton koko shirt in soft faded tone. Paired with a maroon batik sarong and black velvet peci.",
                "Baju Koko Batik Lembut": "Wearing a faded soft batik koko shirt. Paired with a checkered batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded polo shirt. Paired with a dark green batik sarong and white peci.",
                "Kemeja Kotak & Sarung": "Wearing a faded checkered shirt. Paired with a maroon batik sarong and black peci.",
                "Baju Koko Abu & Sarung": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and white peci haji."
            }
        }
		# --- 3. MASTER BAHAN MINIATUR MASJID ---
        MASTER_KONTEN_ALL = {
            "🍉 Miniatur Dari Buah": {
				"Semangka: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole watermelon, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a large central dome, supporting domes, and tall symmetrical minarets. "
    				"The silhouette strongly reads as a traditional mosque with clear proportions and hierarchy. "
    				"The structure uses dark green rind with natural striped patterns as the main surface, with carved openings revealing vibrant ruby-red juicy flesh. "
    				"Strong natural contrast between deep green rind and rich red flesh enhances architectural readability. "
    				"Highly detailed geometric carvings with precise symmetry and clean execution. "
    				"High visual clarity, ultra crisp carving edges, strong micro-detail visibility, sharp surface definition, high surface contrast and clean edge separation, rich natural color contrast with deep green and intense red tones, enhanced color separation between rind and flesh, highly detailed texture fidelity, realistic organic surface response, fine grain detail visibility, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with watermelon debris: flesh chunks, rind pieces, seeds, and natural juice residue."
				),

				"Semangka: Megah Berlapis": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole watermelon, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand architectural composition with a dominant central dome, multiple layered secondary domes, and tall symmetrical minarets forming a strong vertical hierarchy. "
    				"The structure has a powerful three-dimensional presence with clearly defined mass, depth, and spatial layering, creating a monumental miniature silhouette. "
    				"The outer structure is formed from dark green striped watermelon rind, deeply carved into recessed arches, layered surfaces, and structural reliefs. "
    				"Deep carved openings reveal vibrant ruby-red juicy flesh, creating strong depth separation between outer rind and inner layers. "
    				"Complex geometric Islamic patterns are deeply engraved with multi-layered carving depth, enhancing structural readability. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed carving precision, ultra crisp edges, strong depth definition, enhanced structural layering, high surface contrast and strong edge separation, ultra rich natural color contrast with deep green and intense red tones, enhanced tonal depth and material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with watermelon debris: flesh chunks, rind pieces, seeds, and natural residue."
				),

				"Semangka: Fokus Ikonik": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole watermelon, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome as the primary focal point, surrounded by layered secondary domes and tall symmetrical minarets with strong vertical emphasis. "
    				"The structure has a powerful visual hierarchy that guides the eye directly to the central dome, creating a striking and iconic silhouette. "
    				"Low-angle macro perspective enhances the perceived scale, making the miniature appear monumental and visually impactful. "
    				"The outer structure is formed from dark green watermelon rind with natural striped patterns, carved with deep recessed arches and intricate layered details. "
    				"Carved openings reveal vibrant ruby-red juicy flesh, creating strong contrast and depth separation. "
    				"Highly intricate geometric carvings with dense detail distribution across all surfaces. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed carving precision, ultra crisp edges, strong focal clarity, enhanced subject isolation, high surface contrast and strong edge separation, ultra rich natural color contrast with deep green and intense red tones, intense material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, visually striking, cinematic presence, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with watermelon debris: flesh chunks, rind pieces, seeds, and natural residue."
				),
				
				"Semangka: Kubah Daging": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole watermelon, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is uniquely formed from exposed watermelon flesh, shaped into a smooth rounded structure with a deep rich ruby-red tone and natural moist texture, acting as the main focal point of the architecture. "
    				"Surrounding the main dome are smaller domes and tall symmetrical minarets carved from dark green rind with natural striped patterns. "
    				"The structure maintains a clear mosque silhouette with strong proportions and balanced architectural hierarchy. "
    				"The walls are formed from thick green rind, deeply carved with ornate Islamic arches, recessed doorways, and layered structural details. "
    				"Carved sections reveal strong contrast between deep red flesh, pale inner rind, and dark green outer rind, enhancing depth and material separation. "
    				"Highly detailed geometric Islamic carvings with precise symmetry and dense micro-detail distribution across all surfaces. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed carving precision, ultra crisp edges, strong surface definition, high surface contrast and strong edge separation, ultra rich natural color contrast with deep green and intense red tones, enhanced material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with watermelon debris: flesh chunks, rind pieces, seeds, and natural juice residue."
				),

				"Buah Naga: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole dragon fruit, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a large central dome, supporting domes, and tall symmetrical minarets. "
    				"The silhouette strongly reads as a traditional mosque with clear proportions and hierarchy. "
    				"The structure uses magenta-red scaly rind as the main surface, with carved openings revealing white or pink fibrous flesh filled with small black seeds. "
    				"Strong natural contrast between vibrant magenta rind and soft inner flesh enhances architectural readability. "
    				"Highly detailed geometric carvings with precise symmetry and clean execution. "
    				"High visual clarity, ultra crisp carving edges, strong micro-detail visibility, sharp surface definition, high surface contrast and clean edge separation, rich natural color contrast with magenta and white tones, enhanced color separation between rind and flesh, highly detailed texture fidelity, realistic organic surface response, fine grain detail visibility, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with dragon fruit debris: flesh chunks, rind pieces, seeds, and natural juice residue."
				),

				"Buah Naga: Megah Berlapis": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole dragon fruit, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand architectural composition with a dominant central dome, multiple layered secondary domes, and tall symmetrical minarets forming a strong vertical hierarchy. "
    				"The structure has a powerful three-dimensional presence with clearly defined mass, depth, and spatial layering. "
    				"The outer structure is formed from magenta scaly rind, deeply carved into recessed arches and layered surfaces. "
    				"Deep carved openings reveal white or pink fibrous flesh with visible seeds, creating strong depth separation. "
    				"Complex geometric carvings are deeply engraved with layered detail. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed carving precision, ultra crisp edges, strong depth definition, enhanced structural layering, high surface contrast and strong edge separation, ultra rich natural color contrast with magenta and white tones, enhanced tonal depth and material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with dragon fruit debris."
				),

				"Buah Naga: Fokus Ikonik": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole dragon fruit, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome as the primary focal point, surrounded by layered domes and tall minarets. "
    				"The structure has strong visual hierarchy guiding attention to the center. "
    				"Low-angle macro perspective enhances scale and visual impact. "
    				"The outer structure is formed from magenta scaly rind, carved with deep recessed arches and intricate details. "
    				"Carved openings reveal soft fibrous flesh with black seeds, creating strong contrast. "
    				"Highly intricate carvings with dense detail distribution. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed carving precision, ultra crisp edges, strong focal clarity, high surface contrast and strong edge separation, ultra rich natural color contrast with magenta and white tones, highly refined texture fidelity, visually striking, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with dragon fruit debris."
				),

				"Buah Naga: Kubah Daging": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole dragon fruit, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from exposed white or pink fibrous flesh, shaped into a smooth rounded structure with visible black seeds, acting as the main focal point. "
    				"Surrounding structures and minarets are carved from magenta scaly rind. "
    				"The structure maintains a clear mosque silhouette with balanced proportions. "
    				"Carved sections reveal strong contrast between textured rind and soft seeded flesh. "
    				"Highly detailed geometric carvings across all surfaces. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed carving precision, ultra crisp edges, strong surface definition, high surface contrast and strong edge separation, ultra rich natural color contrast with magenta and white tones, enhanced material separation, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with dragon fruit debris."
				),

				"Melon: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole melon, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a large central dome and symmetrical minarets. "
    				"The structure uses outer rind with carved openings revealing smooth pale inner flesh. "
    				"Strong natural contrast enhances readability. "
    				"Highly detailed carvings with clean execution. "
    				"High visual clarity, ultra crisp carving edges, strong micro-detail visibility, sharp surface definition, high surface contrast and clean edge separation, rich natural color contrast, highly detailed texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with melon debris."
				),

				"Melon: Megah Berlapis": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole melon, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Layered architectural composition with deep carved structures and multiple domes. "
    				"Outer rind carved into layered forms revealing inner flesh. "
    				"Strong depth and dimensional structure. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and strong edge separation, rich natural color contrast, highly refined texture fidelity, realistic organic surface response. "
    				"The wooden table surface is scattered only with melon debris."
				),

				"Melon: Fokus Ikonik": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole melon, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with dominant dome and strong focal hierarchy. "
    				"Low-angle perspective enhances scale. "
    				"Outer rind carved with deep detail revealing inner flesh. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and strong edge separation, visually striking, vivid yet natural color. "
    				"The wooden table surface is scattered only with melon debris."
				),

				"Melon: Kubah Daging": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole melon, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from smooth inner melon flesh, acting as the focal point. "
    				"Outer structure and minarets carved from rind. "
    				"Strong contrast between soft flesh and outer rind. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and strong edge separation, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with melon debris."
				),
				
				"Labu: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole pumpkin, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with central dome and symmetrical minarets. "
    				"The structure uses thick orange skin with carved openings revealing fibrous inner flesh. "
    				"Strong natural contrast enhances readability. "
    				"Highly detailed carvings with clean execution. "
    				"High visual clarity, ultra crisp carving edges, strong micro-detail visibility, sharp surface definition, high surface contrast and clean edge separation, rich natural color contrast with deep orange tones, highly detailed texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with pumpkin debris."
				),

				"Labu: Megah Berlapis": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole pumpkin, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Layered and deep architectural carving with multiple domes and strong hierarchy. "
    				"Outer skin carved into layered structures revealing fibrous interior. "
    				"Strong depth and dimensional structure. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and strong edge separation, rich natural orange tones, highly refined texture fidelity, realistic organic surface response. "
    				"The wooden table surface is scattered only with pumpkin debris."
				),

				"Labu: Fokus Ikonik": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole pumpkin, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with strong central dome focus and dramatic visual hierarchy. "
    				"Low-angle perspective enhances scale and impact. "
    				"Deep carvings reveal fibrous pumpkin interior. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and strong edge separation, visually striking, vivid yet natural color. "
    				"The wooden table surface is scattered only with pumpkin debris."
				),

				"Labu: Kubah Daging": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole pumpkin, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from dense inner pumpkin flesh, acting as the main focal point. "
    				"Outer structures carved from thick orange skin. "
    				"Strong contrast between outer shell and inner fibrous flesh. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and strong edge separation, rich natural orange tones, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with pumpkin debris."
				),

				"Rambutan: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed entirely from multiple rambutans, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome, supporting domes, and tall symmetrical minarets formed by carefully arranged fruit units. "
    				"The silhouette strongly reads as a traditional mosque with clear proportions and hierarchy. "
    				"The structure is built by tightly assembling whole rambutans, forming dense textured surfaces with their natural red spiky skins. "
    				"Subtle openings reveal the soft translucent white flesh inside, creating natural material contrast. "
    				"Strong repetition and modular arrangement enhance architectural readability. "
    				"High visual clarity, ultra crisp detail definition, strong micro-detail visibility, sharp surface definition, high surface contrast and clean separation between fruit elements, rich natural color contrast with deep red and white tones, enhanced texture visibility, realistic organic surface response, fine grain detail visibility, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with rambutan debris: loose fruits, peels, and natural residue."
				),

				"Rambutan: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed entirely from multiple rambutans, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand architectural composition with a dominant central dome, multiple layered secondary domes, and tall minarets forming a strong vertical hierarchy. "
    				"The structure has a powerful three-dimensional presence with clearly defined mass and depth. "
    				"Rambutans are stacked and layered to create recessed arches, elevated platforms, and structural relief. "
    				"Dense clustered arrangements form thick walls, while gaps reveal inner white flesh, enhancing depth separation. "
    				"Strong modular repetition creates rhythm and architectural complexity. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, enhanced structural layering, high surface contrast and strong separation between fruit elements, ultra rich natural color contrast with red and white tones, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with rambutan debris."
				),

				"Rambutan: Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed entirely from multiple rambutans, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome formed from a dense cluster of rambutans as the main focal point. "
    				"Layered surrounding domes and vertical minarets emphasize strong visual hierarchy. "
    				"Low-angle macro perspective enhances the perceived scale, making the structure appear monumental. "
    				"The outer structure is composed of tightly packed rambutans, with their spiky red surfaces creating intense texture. "
    				"Subtle openings reveal soft white flesh, adding contrast and visual interest. "
    				"Highly dense detail distribution across all surfaces. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and strong separation between fruit elements, ultra rich natural color contrast with red and white tones, highly refined texture fidelity, visually striking, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with rambutan debris."
				),

				"Rambutan: Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed entirely from multiple rambutans, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is uniquely formed from peeled rambutans, exposing smooth translucent white flesh, creating a clean rounded dome as the focal point. "
    				"Surrounding structures and minarets are built from whole rambutans with red spiky skins, forming strong contrast. "
    				"The structure maintains a clear mosque silhouette with balanced proportions. "
    				"Layered arrangement of peeled and unpeeled rambutans creates strong material separation and depth. "
    				"Highly detailed arrangement ensures clarity of architectural form. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and strong separation between red skin and white flesh, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with rambutan debris."
				),

				"Pepaya: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole papaya, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a large central dome, supporting domes, and tall symmetrical minarets. "
    				"The silhouette strongly reads as a traditional mosque with clear proportions and hierarchy. "
    				"The structure uses smooth orange outer skin with carved openings revealing soft orange flesh and dark seeds inside. "
    				"Strong natural contrast between outer skin and inner flesh enhances architectural readability. "
    				"Highly detailed geometric carvings with precise symmetry and clean execution. "
    				"High visual clarity, ultra crisp carving edges, strong micro-detail visibility, sharp surface definition, high surface contrast and clean edge separation, rich natural color contrast with warm orange tones and dark seed accents, enhanced texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with papaya debris: flesh chunks, seeds, skin pieces, and natural residue."
				),

				"Pepaya: Megah Berlapis": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole papaya, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand architectural composition with layered domes and tall minarets forming a strong vertical hierarchy. "
    				"Deep carved structures create strong dimensional layering and recessed architectural forms. "
    				"The outer skin is carved into layered surfaces revealing inner orange flesh and clustered seeds. "
    				"Strong depth separation enhances structural readability. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and strong separation, rich natural orange tones with dark seed contrast, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with papaya debris."
				),

				"Pepaya: Fokus Ikonik": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole papaya, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome as the focal point and strong visual hierarchy. "
    				"Low-angle macro perspective enhances scale and presence. "
    				"The structure is carved from orange papaya skin with deep openings revealing flesh and seeds. "
    				"Strong contrast and dense detail distribution across all surfaces. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and strong edge separation, visually striking, vivid yet natural orange tones without artificial glow. "
    				"The wooden table surface is scattered only with papaya debris."
				),

				"Pepaya: Kubah Daging": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole papaya, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from smooth orange papaya flesh, creating a rounded focal point with visible natural moisture and embedded dark seeds nearby. "
    				"Outer structures and minarets are carved from the papaya skin. "
    				"Strong contrast between soft inner flesh and outer skin enhances depth. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and strong separation, rich natural orange tones with dark seed accents, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with papaya debris."
				),

				"Pisang: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed from multiple bananas and banana segments, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome and symmetrical minarets formed by arranged banana elements. "
    				"The structure combines whole bananas and cut sections to form curved architectural shapes. "
    				"Outer yellow peel contrasts with soft pale inner flesh. "
    				"Strong modular arrangement enhances readability. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and separation, rich natural yellow tones with soft inner flesh contrast, highly detailed texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with banana debris: peels, slices, and soft residue."
				),

				"Pisang: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from layered banana elements, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Layered architectural composition with stacked banana segments forming domes, arches, and towers. "
    				"Curved banana forms create natural flowing architectural lines. "
    				"Strong depth and structure from repeated arrangement. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and separation, rich natural yellow tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with banana debris."
				),

				"Pisang: Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from bananas, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome formed from curved banana segments. "
    				"Strong visual hierarchy and low-angle perspective enhance impact. "
    				"Yellow peel and pale flesh create contrast and visual focus. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, visually striking, vivid yet natural yellow tones. "
    				"The wooden table surface is scattered only with banana debris."
				),

				"Pisang: Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from bananas, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from smooth exposed banana flesh, creating a soft rounded focal point. "
    				"Outer structures are formed from yellow banana peel elements. "
    				"Strong contrast between peel and flesh enhances visual depth. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and separation, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with banana debris."
				),

				"Jeruk: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed from multiple oranges and orange segments, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with domes and minarets formed from assembled orange units. "
    				"Outer orange peel contrasts with juicy segmented flesh. "
    				"Strong modular repetition enhances architectural clarity. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and separation, rich natural orange tones with bright inner flesh highlights, highly detailed texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with orange debris: peels, segments, and juice residue."
				),

				"Jeruk: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from layered orange elements, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Layered domes and structural forms built from stacked oranges and segments. "
    				"Strong depth and dimensional arrangement. "
    				"Outer peel and inner segments create contrast and structure. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and separation, rich natural orange tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with orange debris."
				),

				"Jeruk: Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from oranges, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant dome formed from clustered orange segments. "
    				"Strong focal hierarchy and visual impact. "
    				"Bright juicy segments create natural highlights and contrast. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, visually striking, vivid yet natural orange tones. "
    				"The wooden table surface is scattered only with orange debris."
				),

				"Jeruk: Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from oranges, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from exposed orange segments, creating a vibrant juicy rounded structure as the focal point. "
    				"Outer structures use orange peel elements. "
    				"Strong contrast between peel and inner segments enhances depth. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and separation, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with orange debris."
				),

				"Salak: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed entirely from multiple salak fruits, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome, supporting domes, and tall symmetrical minarets formed by carefully arranged fruit units. "
    				"The silhouette strongly reads as a traditional mosque with clear proportions and hierarchy. "
    				"The structure is built from whole salak fruits with distinctive dark brown scaly skin, forming dense textured surfaces. "
    				"Subtle openings reveal the pale inner flesh, creating natural material contrast. "
    				"Strong modular repetition enhances architectural readability. "
    				"High visual clarity, ultra crisp detail definition, strong micro-detail visibility, sharp surface definition, high surface contrast and clean separation between fruit elements, rich natural color contrast with dark brown and pale tones, enhanced texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with salak debris: whole fruits, peeled skins, and natural residue."
				),

				"Salak: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from layered salak fruits, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand architectural composition with a dominant central dome, layered secondary domes, and tall minarets forming strong hierarchy. "
    				"Salak fruits are stacked and arranged into layered structural forms with recessed depth. "
    				"Scaly skin textures create strong surface richness and depth variation. "
    				"Open sections reveal inner flesh, enhancing contrast and dimensional separation. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and strong separation, rich natural brown tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with salak debris."
				),

				"Salak: Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from salak fruits, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome formed from tightly clustered salak fruits. "
    				"Strong visual hierarchy and low-angle perspective enhance impact. "
    				"The unique scaly texture creates a striking and highly recognizable surface. "
    				"Subtle openings reveal inner flesh for contrast. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, visually striking, rich natural brown tones, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with salak debris."
				),

				"Salak: Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from salak fruits, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from peeled salak fruits, exposing smooth pale inner flesh as a rounded focal point. "
    				"Outer structures and minarets are built from whole salak fruits with scaly skin. "
    				"Strong contrast between dark textured skin and smooth inner flesh enhances depth and readability. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and strong separation, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with salak debris."
				),

				"Anggur: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed entirely from multiple grapes, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with domes and minarets formed from clustered grape units. "
    				"The structure is built from tightly packed grapes forming smooth rounded surfaces. "
    				"Natural translucency and gloss create soft highlights and depth. "
    				"Strong modular repetition enhances clarity and structure. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and separation, rich natural color tones, highly detailed texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with grape debris: loose grapes and juice residue."
				),

				"Anggur: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from layered grape clusters, firmly placed on a rustic wooden table surface. "
    				"Layered domes and structural forms built from stacked grape clusters. "
    				"Strong depth and dimensional arrangement created by overlapping spherical forms. "
    				"Natural translucency enhances internal depth and visual richness. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and separation, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with grape debris."
				),

				"Anggur: Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from grapes, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant dome formed from dense grape clusters. "
    				"Strong focal hierarchy and low-angle perspective enhance visual impact. "
    				"Glossy grape surfaces create natural highlights and visual appeal. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, visually striking, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with grape debris."
				),

				"Anggur: Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from grapes, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from peeled or cut grapes, exposing translucent juicy interiors as a glowing-like but natural focal point. "
    				"Outer structures use whole grapes for contrast. "
    				"Strong contrast between glossy skin and inner flesh enhances depth. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and separation, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with grape debris."
				),

				"Nanas: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a pineapple, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome and symmetrical minarets. "
    				"The structure uses the rough spiky pineapple skin as the main surface, carved into architectural forms. "
    				"Carved openings reveal juicy yellow flesh inside. "
    				"Strong natural contrast between rough outer skin and soft inner flesh enhances readability. "
    				"High visual clarity, ultra crisp carving edges, strong micro-detail visibility, sharp surface definition, high surface contrast and clean edge separation, rich natural yellow and brown tones, highly detailed texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with pineapple debris: skin pieces, flesh chunks, and natural residue."
				),

				"Nanas: Megah Berlapis": (
    				"A hyper-realistic hand-carved miniature mosque made from a pineapple, firmly placed on a rustic wooden table surface. "
    				"Grand layered architectural composition with deep carvings forming domes and structural depth. "
    				"Thick outer skin is carved into layered architectural surfaces revealing inner yellow flesh. "
    				"Strong depth and dimensional structure. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and strong separation, rich natural yellow tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with pineapple debris."
				),

				"Nanas: Fokus Ikonik": (
    				"A hyper-realistic hand-carved miniature mosque made from a pineapple, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant dome and strong vertical presence. "
    				"The pineapple crown leaves subtly enhance the silhouette like natural spires. "
    				"Low-angle perspective enhances scale and visual impact. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, visually striking, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with pineapple debris."
				),

				"Nanas: Kubah Daging": (
    				"A hyper-realistic hand-carved miniature mosque made from a pineapple, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from exposed juicy yellow pineapple flesh, shaped into a smooth rounded structure as the focal point. "
    				"Outer structures and minarets are carved from the rough pineapple skin. "
    				"Strong contrast between textured outer skin and juicy inner flesh enhances depth and structure. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and separation, rich natural yellow tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with pineapple debris."
				),

				"Durian: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole durian, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome, supporting domes, and tall symmetrical minarets. "
    				"The silhouette strongly reads as a traditional mosque with clear proportions and hierarchy. "
    				"The structure uses the thick spiky durian shell as the main surface, carved into architectural forms. "
    				"Carved openings reveal soft pale yellow flesh inside. "
    				"Strong contrast between rough spiky shell and smooth inner flesh enhances readability. "
    				"High visual clarity, ultra crisp carving edges, strong micro-detail visibility, sharp surface definition, high surface contrast and clean edge separation, rich natural green and yellow tones, highly detailed texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with durian debris: shell fragments, flesh chunks, and natural residue."
				),

				"Durian: Megah Berlapis": (
    				"A hyper-realistic hand-carved miniature mosque made from a durian, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand layered architectural composition with deep carvings forming domes, arches, and structural depth. "
    				"The thick durian shell is carved into layered surfaces and recessed forms. "
    				"Openings reveal dense yellow flesh creating strong depth separation. "
    				"The spiky texture creates extreme surface richness and visual complexity. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and strong separation, rich natural tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with durian debris."
				),

				"Durian: Fokus Ikonik": (
    				"A hyper-realistic hand-carved miniature mosque made from a durian, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome and strong vertical hierarchy. "
    				"The extreme spiky surface creates a bold and striking silhouette. "
    				"Low-angle macro perspective enhances scale and intensity. "
    				"Openings reveal soft inner flesh, creating contrast. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, visually striking, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with durian debris."
				),

				"Durian: Kubah Daging": (
    				"A hyper-realistic hand-carved miniature mosque made from a durian, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from exposed soft yellow durian flesh, shaped into a smooth rounded focal structure. "
    				"Outer structures and minarets are carved from the spiky durian shell. "
    				"Strong contrast between sharp outer shell and soft inner flesh enhances depth and readability. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and strong separation, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with durian debris."
				),

				"Kiwi: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed from kiwi fruits and kiwi slices, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome and symmetrical minarets formed from assembled kiwi elements. "
    				"Outer brown fuzzy skin contrasts with vibrant green inner flesh and radial black seeds. "
    				"The radial seed patterns enhance visual detail and symmetry. "
    				"Strong modular arrangement creates architectural clarity. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and separation, rich natural green tones with dark seed patterns, highly detailed texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with kiwi debris: slices, skins, and seeds."
				),

				"Kiwi: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from layered kiwi elements, firmly placed on a rustic wooden table surface. "
    				"Layered domes and structures formed from stacked kiwi slices and whole fruits. "
    				"The radial seed pattern creates repeating visual rhythm and depth. "
    				"Strong dimensional layering enhances structure. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and separation, rich natural green tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with kiwi debris."
				),

				"Kiwi: Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from kiwi fruits, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant dome formed from kiwi slices displaying radial seed patterns. "
    				"Strong focal hierarchy and low-angle perspective enhance visual impact. "
    				"Bright green flesh creates strong visual attraction. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, visually striking, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with kiwi debris."
				),

				"Kiwi: Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from kiwi fruits, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from smooth exposed kiwi flesh with radial seed patterns, creating a vivid green focal point. "
    				"Outer structures are formed from kiwi skin elements. "
    				"Strong contrast between brown fuzzy skin and bright green flesh enhances depth. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and separation, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with kiwi debris."
				),

				"Strawberry: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed from multiple strawberries, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with domes and minarets formed from arranged strawberry units. "
    				"The structure uses red strawberry surfaces with visible seeds and green leaf tops. "
    				"Strong contrast between red flesh and green leaf elements enhances readability. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and separation, rich natural red tones with seed texture, highly detailed texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with strawberry debris: fruits, slices, leaves, and juice residue."
				),

				"Strawberry: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from layered strawberry elements, firmly placed on a rustic wooden table surface. "
    				"Layered domes and structures formed from stacked strawberries and slices. "
    				"Seeds and surface texture create rich visual detail. "
    				"Strong depth and dimensional structure. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and separation, rich natural red tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with strawberry debris."
				),

				"Strawberry: Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from strawberries, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome formed from clustered strawberries. "
    				"Strong visual hierarchy and low-angle perspective enhance impact. "
    				"Bright red tones create strong visual attraction. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, visually striking, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with strawberry debris."
				),

				"Strawberry: Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from strawberries, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from sliced strawberries exposing juicy red interiors with visible seed patterns. "
    				"Outer structures are formed from whole strawberries with green tops. "
    				"Strong contrast between outer surface and inner flesh enhances depth. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and separation, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with strawberry debris."
				),

				"Kelapa: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a coconut, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome, supporting domes, and symmetrical minarets. "
    				"The structure uses hard brown coconut shell as the outer surface with carved openings revealing clean white coconut flesh inside. "
    				"Strong contrast between dark shell and bright white flesh enhances clarity. "
    				"High visual clarity, ultra crisp carving edges, strong micro-detail visibility, high surface contrast and clean edge separation, rich natural tones, highly detailed texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with coconut debris: shell fragments, flesh pieces, and natural residue."
				),

				"Kelapa: Megah Berlapis": (
    				"A hyper-realistic hand-carved miniature mosque made from a coconut, firmly placed on a rustic wooden table surface. "
    				"Layered architectural carving with deep recessed structures forming domes and towers. "
    				"Outer shell carved into multi-layer surfaces revealing white flesh beneath. "
    				"Strong depth and dimensional layering. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and separation, rich natural tones, highly refined texture fidelity. "
    				"The wooden table surface is scattered only with coconut debris."
				),

				"Kelapa: Fokus Ikonik": (
    				"A hyper-realistic hand-carved miniature mosque made from a coconut, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome and strong visual hierarchy. "
    				"Low-angle perspective enhances scale and impact. "
    				"High contrast between shell and flesh creates strong focal clarity. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, high surface contrast, visually striking, vivid yet natural tones. "
    				"The wooden table surface is scattered only with coconut debris."
				),

				"Kelapa: Kubah Daging": (
    				"A hyper-realistic hand-carved miniature mosque made from a coconut, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from smooth white coconut flesh, creating a clean rounded focal point. "
    				"Outer structures are carved from the hard brown shell. "
    				"Strong contrast between shell and flesh enhances depth. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast, highly refined texture fidelity. "
    				"The wooden table surface is scattered only with coconut debris."
				),

				"Blueberry: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed entirely from multiple blueberries, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture formed from tightly clustered blueberry units. "
    				"Smooth glossy surfaces create subtle reflections and depth. "
    				"Strong modular repetition enhances structure. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and separation, rich natural deep blue tones, highly refined texture fidelity, vivid yet natural color. "
    				"The wooden table surface is scattered only with blueberry debris."
				),

				"Blueberry: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from layered blueberry clusters, firmly placed on a rustic wooden table surface. "
    				"Layered domes and structures formed from stacked blueberries. "
    				"Strong depth and dimensional arrangement. "
    				"Ultra high visual clarity, extreme sharpness, strong depth definition, high surface contrast and separation, highly refined texture fidelity. "
    				"The wooden table surface is scattered only with blueberry debris."
				),

				"Blueberry: Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from blueberries, firmly placed on a rustic wooden table surface. "
    				"Cinematic composition with dominant dome formed from dense blueberry cluster. "
    				"Glossy surfaces enhance focal clarity. "
    				"Ultra high visual clarity, extreme sharpness, strong focal clarity, high surface contrast, visually striking. "
    				"The wooden table surface is scattered only with blueberry debris."
				),

				"Blueberry: Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from blueberries, firmly placed on a rustic wooden table surface. "
    				"The central dome is formed from crushed or cut blueberries, revealing deep purple juicy interiors. "
    				"Outer structures use whole blueberries. "
    				"Strong contrast enhances depth. "
    				"Ultra high visual clarity, extreme sharpness, strong surface definition, high surface contrast. "
    				"The wooden table surface is scattered only with blueberry debris."
				),

				"Jagung: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed from corn cobs and kernels, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture formed from tightly packed rows of corn kernels. "
    				"Natural repeating kernel pattern creates strong visual rhythm. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and separation, rich natural yellow tones, highly refined texture fidelity. "
    				"The wooden table surface is scattered only with corn debris."
				),

				"Jagung: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from layered corn structures, firmly placed on a rustic wooden table surface. "
    				"Layered architectural composition using stacked kernels and cob sections. "
    				"Strong depth and repetition. "
    				"Ultra high visual clarity, extreme sharpness, strong depth definition, high surface contrast. "
    				"The wooden table surface is scattered only with corn debris."
				),

				"Jagung: Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from corn, firmly placed on a rustic wooden table surface. "
    				"Cinematic composition with a dominant dome formed from curved corn rows. "
    				"Pattern creates strong visual impact. "
    				"Ultra high visual clarity, extreme sharpness, strong focal clarity. "
    				"The wooden table surface is scattered only with corn debris."
				),

				"Jagung: Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from corn, firmly placed on a rustic wooden table surface. "
    				"The central dome is formed from exposed corn kernels, creating a dense textured surface. "
    				"Outer structures use cob sections. "
    				"Strong contrast enhances depth. "
    				"Ultra high visual clarity, extreme sharpness, strong surface definition. "
    				"The wooden table surface is scattered only with corn debris."
				),

				"Sirsak: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a soursop fruit, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Structure uses spiky green skin with carved openings revealing soft white fibrous flesh. "
    				"Strong texture contrast enhances readability. "
    				"High visual clarity, ultra crisp carving edges, strong surface contrast, rich natural green tones, highly refined texture fidelity. "
    				"The wooden table surface is scattered only with soursop debris."
				),
				
				"Tomat: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed from tomatoes, firmly placed on a rustic wooden table surface. "
    				"Glossy red surface and juicy interior create strong visual contrast. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast, vivid natural red tones. "
    				"The wooden table surface is scattered only with tomato debris."
				),
				
				"Kelapa Tua: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a mature coconut with rough fibrous shell, firmly placed on a rustic wooden table surface. "
    				"The structure uses coarse brown fibers and hard shell, with carved openings revealing white flesh. "
    				"Strong texture contrast creates depth and realism. "
    				"High visual clarity, ultra crisp edges, strong surface contrast, highly detailed texture fidelity. "
    				"The wooden table surface is scattered only with coconut debris."
				),

				"Ceri: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed from multiple cherries, firmly placed on a rustic wooden table surface. "
    				"Glossy red fruits arranged into domes and towers. "
    				"Strong modular structure with reflective surfaces. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast, vivid natural red tones. "
    				"The wooden table surface is scattered only with cherry debris."
				),

				"Mangga: Tajam Natural": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole mango, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a large central dome, supporting domes, and tall symmetrical minarets. "
    				"The silhouette strongly reads as a traditional mosque with clear proportions and hierarchy. "
    				"The structure uses smooth mango skin with natural green to yellow gradients as the main surface, with carved openings revealing rich golden-yellow juicy flesh. "
    				"Strong natural contrast between outer skin and inner flesh enhances architectural readability. "
    				"Highly detailed geometric carvings with precise symmetry and clean execution. "
    				"High visual clarity, ultra crisp carving edges, strong micro-detail visibility, sharp surface definition, high surface contrast and clean edge separation, rich natural color contrast with green, yellow, and orange tones, enhanced color separation between skin and flesh, highly detailed texture fidelity, realistic organic surface response, fine grain detail visibility, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mango debris: flesh chunks, skin pieces, and natural juice residue."
				),

				"Mangga: Megah Berlapis": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole mango, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand architectural composition with a dominant central dome, multiple layered secondary domes, and tall symmetrical minarets forming a strong vertical hierarchy. "
    				"The structure has a powerful three-dimensional presence with clearly defined mass, depth, and spatial layering, creating a monumental miniature silhouette. "
    				"The outer structure is formed from mango skin, deeply carved into recessed arches, layered surfaces, and structural reliefs. "
    				"Deep carved openings reveal rich golden-yellow juicy flesh, creating strong depth separation between outer skin and inner layers. "
    				"Complex geometric carvings are deeply engraved with multi-layered detail, enhancing structural readability. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed carving precision, ultra crisp edges, strong depth definition, enhanced structural layering, high surface contrast and strong edge separation, ultra rich natural color contrast with green, yellow, and orange tones, enhanced tonal depth and material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mango debris: flesh chunks, skin pieces, and juice residue."
				),

				"Mangga: Fokus Ikonik": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole mango, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome as the primary focal point, surrounded by layered secondary domes and tall symmetrical minarets with strong vertical emphasis. "
    				"The structure has a powerful visual hierarchy that guides the eye directly to the central dome, creating a striking and iconic silhouette. "
    				"Low-angle macro perspective enhances the perceived scale, making the miniature appear monumental and visually impactful. "
    				"The outer structure is formed from mango skin with natural gradient tones, carved with deep recessed arches and intricate layered details. "
    				"Carved openings reveal rich golden-yellow juicy flesh, creating strong contrast and depth separation. "
    				"Highly intricate geometric carvings with dense detail distribution across all surfaces. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed carving precision, ultra crisp edges, strong focal clarity, enhanced subject isolation, high surface contrast and strong edge separation, ultra rich natural color contrast with green, yellow, and orange tones, intense material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, visually striking, cinematic presence, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mango debris: flesh chunks, skin pieces, and juice residue."
				),

				"Mangga: Kubah Daging": (
    				"A hyper-realistic hand-carved miniature mosque made from a whole mango, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from exposed mango flesh, shaped into a smooth rounded structure with rich golden-yellow color and natural juicy texture, acting as the main focal point. "
    				"Surrounding domes and tall symmetrical minarets are carved from mango skin with natural gradient tones. "
    				"The structure maintains a clear mosque silhouette with strong proportions and balanced architectural hierarchy. "
    				"The walls are formed from mango skin, deeply carved with ornate arches, recessed doorways, and layered structural details. "
    				"Carved sections reveal strong contrast between juicy flesh and outer skin, enhancing depth and material separation. "
    				"Highly detailed geometric carvings with precise symmetry and dense micro-detail distribution across all surfaces. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed carving precision, ultra crisp edges, strong surface definition, high surface contrast and strong edge separation, ultra rich natural color contrast with golden-yellow and green tones, enhanced material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mango debris: flesh chunks, skin pieces, and natural juice residue."
				),

				"Cabe Merah: Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed from multiple red chili peppers, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome, supporting domes, and tall symmetrical minarets formed by carefully arranged chili elements. "
    				"The elongated curved shape of the chilies is used to create arches, domes, and vertical structures with strong architectural readability. "
    				"Glossy red chili skin forms the outer surface, with sliced sections revealing lighter inner flesh and seeds. "
    				"Strong natural contrast between deep red skin and pale inner flesh enhances clarity. "
    				"Highly detailed arrangement with precise symmetry and clean structural composition. "
    				"High visual clarity, ultra crisp detail definition, strong micro-detail visibility, sharp surface definition, high surface contrast and clean edge separation, rich natural red tones, enhanced material separation, highly detailed texture fidelity, realistic organic surface response, fine grain detail visibility, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with red chili debris: cut chili segments, seeds, and natural juice residue."
				),

				"Cabe Merah: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from layered red chili peppers, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand architectural composition with a dominant central dome, multiple layered secondary domes, and tall symmetrical minarets built from stacked and interwoven chili elements. "
    				"The curved chili forms create layered arches and structural depth, forming a complex and dynamic miniature silhouette. "
    				"Multiple layers of chili surfaces create strong depth and dimensional hierarchy. "
    				"Sliced chili sections reveal inner flesh and seeds, adding contrast and detail variation. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, enhanced structural layering, high surface contrast and strong edge separation, ultra rich natural red tones with subtle variations, enhanced tonal depth and material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with red chili debris: cut pieces, seeds, and residue."
				),

				"Cabe Merah: Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from red chili peppers, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome formed from tightly arranged curved chilies, surrounded by tall vertical minarets created from elongated chili forms. "
    				"The structure has a strong visual hierarchy that emphasizes height and curvature, creating a bold and striking silhouette. "
    				"Low-angle macro perspective enhances scale, making the structure appear monumental despite its small components. "
    				"The glossy red surfaces create strong highlights and visual focus. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, enhanced subject isolation, high surface contrast and strong edge separation, ultra rich natural red tones, intense material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, visually striking, cinematic presence, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with red chili debris: segments, seeds, and juice marks."
				),

				"Cabe Merah: Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from red chili peppers, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from densely packed sliced chili sections, exposing the inner flesh and seeds to create a textured dome with rich organic detail. "
    				"Surrounding structures and minarets are formed from whole curved chilies, creating strong vertical lines and architectural balance. "
    				"The combination of glossy outer skin and exposed inner flesh creates strong visual contrast and depth. "
    				"Highly structured arrangement ensures a clear mosque silhouette despite the organic shapes. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed arrangement precision, ultra crisp edges, strong surface definition, high surface contrast and strong edge separation, ultra rich natural red tones with subtle variations, enhanced material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with red chili debris: sliced sections, seeds, and natural residue."
				),

				"Pisang: MIX Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed from bananas, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome made from layered banana leaves, supported by smaller domes and tall symmetrical minarets formed from banana fruit segments. "
    				"The structure uses smooth yellow banana surfaces as the main material, while wide green banana leaves are shaped into curved dome structures. "
    				"Strong natural contrast between bright yellow fruit and deep green leaves enhances architectural clarity. "
    				"Highly detailed arrangement with precise symmetry and clean structural composition. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and clean edge separation, rich natural yellow and green tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with banana debris: fruit pieces, peel strips, and torn leaf fragments."
				),

				"Pisang: MIX Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from bananas and banana leaves, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand layered architecture with a dominant central dome made from folded banana leaves, surrounded by multiple layered domes and tall minarets built from stacked banana segments. "
    				"The leaves form elegant curved surfaces, while the fruit provides structural mass. "
    				"Layered composition creates strong depth and dimensional hierarchy. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and strong separation, rich natural yellow and green tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with banana debris: fruit chunks, peel layers, and leaf fragments."
				),

				"Pisang: MIX Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from bananas and banana leaves, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome made from large curved banana leaves acting as the main focal point. "
    				"Banana fruits form supporting structures and vertical minarets. "
    				"The strong contrast between green leaf dome and yellow structure creates a striking visual identity. "
    				"Low-angle macro perspective enhances scale and presence. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, visually striking, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with banana debris: fruit pieces, peel strips, and leaf fragments."
				),

				"Pisang: MIX Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from bananas and banana leaves, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from tightly layered banana leaves with visible veins and natural curvature, creating a smooth organic dome shape. "
    				"The main structure and minarets are built from banana fruit, with sliced sections revealing soft pale interior flesh. "
    				"Strong contrast between leaf texture and fruit flesh enhances depth and readability. "
    				"Highly structured composition maintains a clear mosque silhouette. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and separation, rich natural green and yellow tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with banana debris: fruit chunks, peel pieces, and leaf fragments."
				),

				"Kelapa: MIX Tajam Natural": (
    				"A hyper-realistic miniature mosque constructed from coconut materials, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome made from woven young coconut leaves (janur), supported by smaller domes and tall symmetrical minarets. "
    				"The main structure uses hard coconut shell elements, while flexible green-yellow janur leaves are intricately woven into architectural surfaces. "
    				"Strong contrast between rough shell texture and smooth woven leaves enhances clarity. "
    				"Highly detailed craftsmanship with precise symmetry and clean structural composition. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and clean edge separation, rich natural brown, green, and yellow tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with coconut debris: shell fragments, leaf strips, and natural residue."
				),

				"Kelapa: MIX Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed from coconut shell and woven janur leaves, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand layered architecture with a dominant central dome woven from janur, surrounded by multiple layered domes and tall minarets formed from coconut shell and leaf structures. "
    				"The woven leaf patterns create intricate layered surfaces and depth. "
    				"Strong dimensional hierarchy and structural complexity. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong depth definition, high surface contrast and separation, rich natural brown and green-yellow tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with coconut debris: shell pieces, woven leaf fragments, and residue."
				),

				"Kelapa: MIX Fokus Ikonik": (
    				"A hyper-realistic miniature mosque constructed from coconut shell and janur leaves, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome made from intricately woven janur leaves acting as the main focal point. "
    				"Coconut shell forms the structural base and vertical minarets. "
    				"The contrast between woven leaf textures and solid shell creates a strong visual identity. "
    				"Low-angle macro perspective enhances scale and visual impact. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, visually striking, highly refined texture fidelity, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with coconut debris: shell fragments, leaf strips, and residue."
				),

				"Kelapa: MIX Kubah Daging": (
    				"A hyper-realistic miniature mosque constructed from coconut materials, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"The central dome is formed from tightly woven janur leaves, shaped into a smooth rounded dome with visible natural leaf patterns. "
    				"The main structure and minarets are built from coconut shell and inner flesh elements. "
    				"Strong contrast between fibrous shell, soft white flesh, and woven leaves enhances depth and readability. "
    				"Highly structured composition maintains a clear mosque silhouette. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong surface definition, high surface contrast and separation, rich natural tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with coconut debris: shell fragments, flesh pieces, and leaf strips."
				),

				"Biji Jagung: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed entirely from corn kernels, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand layered mosque architecture with a dominant central dome, multiple secondary domes, and tall symmetrical minarets built from densely packed corn kernels. "
    				"The repeating kernel pattern creates strong geometric rhythm and structured surfaces across the entire architecture. "
    				"Layered arrangement forms clear depth, volume, and architectural hierarchy despite the small modular elements. "
    				"High structural density ensures a clearly readable mosque silhouette with strong proportions. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp detail definition, strong micro-detail visibility, high surface contrast and strong edge separation, rich natural yellow tones, enhanced pattern repetition, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with corn kernel debris: loose kernels and fragments."
				),

				"Biji Jagung: Megah Ikonik": (
    				"A hyper-realistic miniature mosque constructed entirely from corn kernels, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic monumental composition with a dominant central dome formed from tightly clustered kernels, supported by layered domes and tall vertical minarets. "
    				"The dense arrangement of kernels creates smooth curved architectural surfaces while maintaining visible granular detail. "
    				"Strong vertical emphasis and symmetrical layout produce a bold and iconic mosque silhouette. "
    				"Low-angle macro perspective enhances scale, making the structure appear grand and monumental. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and strong separation, rich natural golden-yellow tones, intense material definition, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with corn kernel debris."
				),

				"Biji Kacang Hijau: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed entirely from mung beans, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand layered mosque architecture with a dominant central dome, multiple supporting domes, and tall symmetrical minarets built from tightly arranged green beans. "
    				"The small oval shapes create smooth yet detailed surfaces with subtle organic variation. "
    				"Layered arrangement forms strong depth and architectural clarity with a clearly readable mosque silhouette. "
    				"The uniform green tone creates a calm but highly structured visual composition. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp detail definition, strong micro-detail visibility, high surface contrast and clean edge separation, rich natural green tones, enhanced pattern density, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mung bean debris: loose beans and fragments."
				),

				"Biji Kacang Hijau: Megah Ikonik": (
    				"A hyper-realistic miniature mosque constructed entirely from mung beans, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic composition with a dominant central dome and tall vertical minarets, all formed from densely packed green beans. "
    				"The tight clustering creates smooth dome curvature while preserving fine granular detail. "
    				"Strong symmetry and vertical emphasis produce a clear and iconic mosque silhouette. "
    				"Low-angle macro perspective enhances the monumental appearance of the structure. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and separation, rich natural green tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mung bean debris."
				),

				"Biji Kedelai Hitam: Megah Berlapis": (
    				"A hyper-realistic miniature mosque constructed entirely from black soybeans, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand layered mosque architecture with a dominant central dome, multiple secondary domes, and tall symmetrical minarets formed from densely packed black soybeans. "
    				"The smooth rounded beans create compact surfaces with subtle reflective highlights. "
    				"Layered structure produces strong depth and a clearly readable mosque silhouette. "
    				"The deep black tone creates a bold and premium visual presence. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp detail definition, strong micro-detail visibility, high surface contrast and strong edge separation, deep natural black tones with subtle highlights, enhanced density and material separation, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with black soybean debris: loose beans and fragments."
				),

				"Biji Kedelai Hitam: Megah Ikonik": (
    				"A hyper-realistic miniature mosque constructed entirely from black soybeans, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Cinematic monumental composition with a dominant central dome and tall vertical minarets, all formed from tightly packed soybeans. "
    				"The dense arrangement creates smooth architectural curves with fine granular detail. "
    				"Strong symmetry and vertical emphasis produce a powerful and iconic mosque silhouette. "
    				"Low-angle macro perspective enhances scale and visual impact. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp edges, strong focal clarity, high surface contrast and strong separation, deep black tones with subtle reflective highlights, intense material definition, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with black soybean debris."
				),

				"Mix Buah: Kontras Segar": (
    				"A hyper-realistic miniature mosque constructed from a combination of watermelon, kiwi, and blueberries, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a large central dome made from vibrant red watermelon flesh, supported by smaller domes and tall symmetrical minarets. "
    				"The main structural walls are formed from green kiwi slices with visible radial seed patterns, creating strong texture and color contrast. "
    				"Blueberries are used as fine detail elements, forming accents, edges, and decorative architectural features. "
    				"Strong material zoning ensures each fruit occupies a clear structural role, maintaining a readable mosque silhouette. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and clean edge separation, rich natural red, green, and deep blue tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mixed fruit debris: watermelon chunks, kiwi slices, and blueberries."
				),

				"Mix Buah: Tropis Premium": (
    				"A hyper-realistic miniature mosque constructed from a combination of coconut, mango, and grapes, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome formed from rich golden mango flesh, acting as the main focal point. "
    				"The structural walls and main body are built from hard coconut shell and white flesh, providing a strong architectural base. "
    				"Grapes are used as modular decorative elements, forming small domes, accents, and surface details. "
    				"Strong material separation ensures clarity between structural elements and decorative components. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and clean edge separation, rich natural brown, white, yellow, and purple tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mixed fruit debris: coconut shell fragments, mango flesh pieces, and grapes."
				),

				"Mix Buah: Tropis Klasik": (
    				"A hyper-realistic miniature mosque constructed from a combination of pineapple, banana, and coconut, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome formed from layered banana slices, creating a smooth rounded shape. "
    				"The structural walls are carved from pineapple skin, providing a rough geometric texture and strong architectural presence. "
    				"Coconut elements are used for supporting structures and detailing, including minarets and surface accents. "
    				"Strong contrast between rough pineapple texture, smooth banana surfaces, and coconut materials enhances depth and readability. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and clean edge separation, rich natural yellow, green, and brown tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mixed fruit debris: pineapple skin pieces, banana slices, and coconut fragments."
				),

				"Mix Buah: Aesthetic Cerah": (
    				"A hyper-realistic miniature mosque constructed from a combination of strawberries, blueberries, and kiwi, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome formed from strawberries, creating a bold red focal point. "
    				"The structural walls are formed from kiwi slices with visible seed patterns, adding texture and structure. "
    				"Blueberries are used as detailed modular accents across domes, minarets, and edges. "
    				"The combination creates a balanced and vibrant composition with strong color separation. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and clean edge separation, rich natural red, green, and deep blue tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mixed fruit debris: strawberry pieces, kiwi slices, and blueberries."
				),

				"Mix Buah: Manis Hangat": (
    				"A hyper-realistic miniature mosque constructed from a combination of watermelon, mango, and banana, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a central dome formed from mango flesh, creating a smooth and vibrant golden focal point. "
    				"The structural walls are carved from watermelon rind and flesh, providing strong green and red contrast. "
    				"Banana elements are used for supporting domes, arches, and vertical structures. "
    				"The composition creates a warm and inviting visual tone with clear architectural readability. "
    				"High visual clarity, ultra crisp detail definition, strong surface contrast and clean edge separation, rich natural red, green, yellow, and orange tones, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with mixed fruit debris: watermelon chunks, mango pieces, and banana slices."
				),

				"Mix Organik: Megah Diorama Raya": (
    				"A hyper-realistic large-scale miniature mosque diorama constructed from a combination of seeds, leaves, and flowers, firmly placed on a wide rustic wooden table surface, with the entire base clearly resting on the table. "
    				"The structure is designed at an approximate 1-meter scale miniature, giving it a monumental and highly detailed architectural presence. "
    				"Clearly structured grand mosque architecture featuring a dominant central dome, multiple secondary domes, expansive courtyards, and tall symmetrical minarets arranged in a cohesive layout. "
    				"Structural base and walls are densely formed from tightly packed seeds, creating solid architectural mass and fine granular detail. "
    				"Large leaves are used as curved architectural elements, forming domes, canopies, and layered roof structures with smooth organic surfaces. "
    				"Flowers are used selectively as ornamental accents on domes, edges, and focal points, adding color highlights without disrupting structural clarity. "
    				"Strong material zoning ensures each element (seeds, leaves, flowers) has a clear architectural role, maintaining a readable and realistic mosque silhouette. "
    				"Layered composition creates strong depth, spatial hierarchy, and a complete environmental diorama feel. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed construction, ultra crisp edges, strong structural readability, high surface contrast and clean edge separation, rich natural color variation across organic materials, highly refined texture fidelity, realistic organic surface response, fine micro-detail visibility, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with organic debris: loose seeds, torn leaf fragments, and fallen flower petals."
				),

				"Mix Organik: Megah Diorama Ikonik": (
    				"A hyper-realistic monumental mosque diorama constructed from a complex combination of seeds, leaves, and flowers, firmly placed on a large rustic wooden table surface, with the full base clearly grounded on the table. "
    				"The structure is built at an approximate 1-meter miniature scale, appearing massive, dense, and highly intricate. "
    				"Cinematic grand mosque architecture with a dominant oversized central dome, multiple layered domes, expansive terraces, and very tall symmetrical minarets creating a powerful vertical and horizontal presence. "
    				"The base structure is formed from extremely dense seed packing, creating solid architectural mass with ultra fine granular texture. "
    				"Large organic leaves are shaped and layered into sweeping curved domes and roofing structures, adding smooth contrast to the dense seed surfaces. "
    				"Flowers are integrated as high-impact focal accents, placed strategically on domes, entrances, and key architectural nodes, enhancing visual richness without overwhelming the structure. "
    				"Extremely strong structural hierarchy ensures the mosque silhouette is bold, clear, and instantly recognizable despite the complex materials. "
    				"Multi-layered composition with deep spatial separation creates a full cinematic diorama environment with strong depth and perspective. "
    				"Ultra high visual clarity, extreme sharpness, hyper-dense detail distribution, ultra crisp edges, strong focal clarity, enhanced subject dominance, high surface contrast and strong edge separation, ultra rich natural color variation, intense material differentiation between seeds, leaves, and flowers, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, visually striking, cinematic presence, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with organic debris: loose seeds, leaf fragments, flower petals, and natural residue."
				),

				"Mix Buah: Diorama Megah Kontras": (
    				"A hyper-realistic monumental mosque diorama constructed from a combination of watermelon, mango, and kiwi, firmly placed on a wide rustic wooden table surface, with the entire base clearly resting on the table. "
    				"The structure is designed at an approximate 1-meter miniature scale, creating a massive and highly detailed architectural presence. "
    				"Clearly structured grand mosque architecture featuring a dominant central dome, multiple layered domes, expansive courtyards, and tall symmetrical minarets arranged in a cohesive layout. "
    				"The central dome is formed from smooth mango flesh, creating a bold golden focal point. "
    				"The main structural walls and mass are carved from watermelon rind and flesh, providing strong green and red contrast with deep carved architectural depth. "
    				"Kiwi slices are used as detailed surface elements and decorative panels, adding fine texture and radial seed patterns. "
    				"Strong material zoning ensures each fruit has a clear architectural role, maintaining a readable and realistic mosque silhouette. "
    				"Layered composition creates strong depth, spatial hierarchy, and a complete environmental diorama feel. "
    				"Monumental scale presence, grand architectural mass, strong silhouette dominance, highly structured composition. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed carving precision, ultra crisp edges, strong depth definition, high surface contrast and strong edge separation, ultra rich natural color contrast with green, red, and golden tones, enhanced material separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with fruit debris: watermelon chunks, mango pieces, and kiwi slices."
				),

				"Mix Buah: Diorama Megah Tropis": (
    				"A hyper-realistic monumental mosque diorama constructed from a combination of pineapple, banana, and coconut, firmly placed on a wide rustic wooden table surface, with the entire base clearly resting on the table. "
    				"The structure is built at an approximate 1-meter miniature scale, appearing dense, complex, and architecturally massive. "
    				"Clearly structured grand mosque architecture featuring a dominant central dome, multiple layered domes, terraces, and tall symmetrical minarets forming a powerful composition. "
    				"The central dome is formed from layered banana slices, creating a smooth rounded organic surface. "
    				"The main structural walls are carved from pineapple skin, providing rough geometric texture and strong architectural definition. "
    				"Coconut shell and flesh are used for structural support elements, columns, and minarets, adding contrast between hard and soft materials. "
    				"Strong material separation ensures clear readability between structural mass and detailing elements. "
    				"Layered architectural composition creates deep spatial hierarchy and a complete cinematic diorama environment. "
    				"Monumental scale presence, grand architectural mass, strong silhouette dominance, highly structured composition. "
    				"Ultra high visual clarity, extreme sharpness, hyper-dense detail distribution, ultra crisp edges, strong depth definition, high surface contrast and strong edge separation, rich natural yellow, brown, and green tones, enhanced material differentiation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with fruit debris: pineapple skin pieces, banana slices, and coconut fragments."
				),

				"Mix Buah: Diorama Megah Cerah": (
    				"A hyper-realistic monumental mosque diorama constructed from a combination of strawberries, blueberries, and kiwi, firmly placed on a wide rustic wooden table surface, with the entire base clearly resting on the table. "
    				"The structure is designed at an approximate 1-meter miniature scale, giving it a bold, vibrant, and highly detailed presence. "
    				"Clearly structured grand mosque architecture featuring a dominant central dome, multiple supporting domes, and tall symmetrical minarets arranged across a cohesive layout. "
    				"The central dome is formed from strawberries, creating a strong red focal point with organic surface detail. "
    				"The structural walls are formed from kiwi slices, adding green contrast with visible seed patterns and fine texture. "
    				"Blueberries are used as modular decorative elements across domes, edges, and minarets, adding dense micro-detail accents. "
    				"Strong material zoning maintains a clear mosque silhouette and prevents visual chaos. "
    				"Layered composition creates depth, spatial hierarchy, and a complete diorama environment. "
    				"Monumental scale presence, grand architectural mass, strong silhouette dominance, highly structured composition. "
    				"Ultra high visual clarity, extreme sharpness, hyper-detailed construction, ultra crisp edges, strong focal clarity, high surface contrast and strong edge separation, ultra rich natural red, green, and deep blue tones, enhanced color separation, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, visually striking, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with fruit debris: strawberry pieces, kiwi slices, and blueberries."
				),

				"Mix Biji & Daun: Kubah Daun Ikonik": (
    				"A hyper-realistic miniature mosque constructed from a combination of corn kernels and mung beans, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Clearly structured mosque architecture with a dominant central dome made entirely from layered banana leaves, supported by smaller leaf domes and tall symmetrical minarets. "
    				"The structural walls and minarets are built from densely packed corn kernels and mung beans, forming solid architectural mass with fine granular detail. "
    				"Corn kernels provide bright yellow highlights and structural rhythm, while mung beans fill gaps and create smooth green surfaces. "
    				"The banana leaf dome features natural curvature, visible veins, and smooth organic layering, creating a strong visual focal point. "
    				"Strong material zoning ensures clear separation between leaf-based domes and seed-based structures, maintaining a readable mosque silhouette. "
    				"Ultra high visual clarity, extreme sharpness, ultra crisp detail definition, strong micro-detail visibility, high surface contrast and strong edge separation, rich natural green and yellow tones, enhanced material separation, highly refined texture fidelity, realistic organic surface response, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with organic debris: corn kernels, mung beans, and torn banana leaf fragments."
				),

				"Mix Biji & Daun: Kubah Daun Megah Berlapis": (
    				"A hyper-realistic monumental miniature mosque constructed from corn kernels, mung beans, and banana leaves, firmly placed on a rustic wooden table surface, with the base clearly resting on the table. "
    				"Grand architectural composition with a dominant central dome made from large layered banana leaves, surrounded by multiple secondary domes also formed from folded leaf structures. "
    				"Tall symmetrical minarets and structural walls are built from extremely dense packing of corn kernels and mung beans, creating deep layered surfaces and strong architectural mass. "
    				"The layered arrangement of seeds forms clear depth, terraces, and structural hierarchy across the mosque. "
    				"The banana leaves create smooth curved domes that contrast sharply with the dense granular texture of the seed-built structures. "
    				"Strong structural hierarchy ensures a bold, readable, and monumental mosque silhouette. "
    				"Monumental scale presence, grand architectural mass, strong silhouette dominance, highly structured composition. "
    				"Ultra high visual clarity, extreme sharpness, hyper-dense detail distribution, ultra crisp edges, strong depth definition, high surface contrast and strong edge separation, rich natural green and yellow tones with subtle variation, enhanced material contrast between leaf and seed textures, highly refined texture fidelity, realistic organic surface response, micro-surface irregularities, fine grain detail enhancement, vivid yet natural color without artificial glow. "
    				"The wooden table surface is scattered only with organic debris: corn kernels, mung beans, and banana leaf fragments."
				)
				

            },        
            "📦 Miniatur Bahan Sederhana": {
                "XXXXX": (
                    "YYYYY."
                )
            },
            "✨ Miniatur Megah ( LED )": {
                "XXXXX": (
                    "YYYYY."
                )
            }
        }

		# --- 4. MASTER GRANDMA SETTING (Suasana Latar) ---
        MASTER_GRANDMA_SETTING = {
            "Kebun Semangka Biasa": (
                "The character is seated on a low weathered wooden crate in a sprawling natural Indonesian watermelon farm on a normal day. "
                "Dark brown earth with natural uneven terrain and patches of wild grass. "
                "Ripe watermelons of normal size are scattered organically across the field, not in neat rows. "
                "Green vines sprawl unevenly with realistic sparse density and some wild weeds. "
                "In the far background, a few villagers can be seen harvesting watermelons by hand. "
                "Open and airy rural farm atmosphere with wide field feeling."
            ),
            "Kebun Semangka dengan Gubuk": (
                "The character is seated on a low weathered wooden crate beside a simple fresh green bamboo gubuk in the watermelon farm. "
                "Dark brown earth with natural uneven terrain and patches of wild grass. "
                "Ripe watermelons of normal size are scattered organically around the gubuk area. "
                "Green vines sprawl unevenly with realistic sparse density and some wild weeds. "
                "A sturdy gubuk made of fresh green bamboo poles with a thatched roof stands nearby. "
                "Cozy and sheltered farm atmosphere near the bamboo structure."
            ),
            "Kebun Buah Naga Biasa": (
                "The character is seated on a low weathered wooden crate in a sprawling natural dragon fruit plantation on a normal day. "
                "Dark brown earth with natural uneven terrain. "
                "Long climbing dragon fruit vines grow on wooden poles with ripe magenta fruits hanging. "
                "In the far background, a few villagers can be seen harvesting dragon fruit. "
                "Tropical climbing vine plantation atmosphere."
            ),
            "Kebun Buah Naga dengan Gubuk": (
                "The character is seated on a low weathered wooden crate beside a simple fresh green bamboo gubuk in the dragon fruit plantation. "
                "Long climbing dragon fruit vines grow around the bamboo structure with ripe magenta fruits hanging. "
                "A sturdy gubuk made of fresh green bamboo poles with a thatched roof stands nearby. "
                "Intimate plantation atmosphere near the bamboo gubuk."
            ),
            "Kebun Melon Biasa": (
                "The character is seated on a low weathered wooden crate in a sprawling natural melon field on a normal day. "
                "Dark brown earth with natural uneven terrain. "
                "Round ripe melons are scattered organically on trailing vines. "
                "In the far background, a few villagers can be seen harvesting melons. "
                "Open melon patch farm atmosphere."
            ),
            "Kebun Melon dengan Gubuk": (
                "The character is seated on a low weathered wooden crate beside a simple fresh green bamboo gubuk in the melon field. "
                "Round ripe melons are scattered organically around the gubuk area on trailing vines. "
                "A sturdy gubuk made of fresh green bamboo poles with a thatched roof stands nearby. "
                "Sheltered melon patch atmosphere near the gubuk."
            ),
            "Kebun Labu Biasa": (
                "The character is seated on a low weathered wooden crate in a sprawling natural pumpkin field on a normal day. "
                "Dark brown earth with natural uneven terrain. "
                "Large ripe pumpkins are scattered organically on thick vines. "
                "In the far background, a few villagers can be seen harvesting pumpkins. "
                "Open pumpkin patch farm atmosphere."
            ),
            "Kebun Labu dengan Gubuk": (
                "The character is seated on a low weathered wooden crate beside a simple fresh green bamboo gubuk in the pumpkin field. "
                "Large ripe pumpkins are scattered organically around the gubuk area on thick vines. "
                "A sturdy gubuk made of fresh green bamboo poles with a thatched roof stands nearby. "
                "Sheltered pumpkin patch atmosphere near the gubuk."
            ),
            "Kebun Rambutan Biasa": (
                "The character is seated on a low weathered wooden crate under rambutan trees in a natural village orchard on a normal day. "
                "Rambutan fruits hang in clusters from the trees with bright red spiky skin. "
                "Fallen rambutan fruits and leaves are scattered on the ground. "
                "In the far background, a few villagers can be seen harvesting rambutan. "
                "Shady tropical orchard atmosphere."
            ),
            "Kebun Rambutan dengan Gubuk": (
                "The character is seated on a low weathered wooden crate beside a simple fresh green bamboo gubuk under rambutan trees. "
                "Rambutan fruits hang in clusters from the trees with bright red spiky skin. "
                "Fallen rambutan fruits and leaves are scattered around the gubuk area. "
                "A sturdy gubuk made of fresh green bamboo poles with a thatched roof stands nearby. "
                "Shady orchard atmosphere near the bamboo gubuk."
            ),
            "Kebun Pepaya Biasa": (
                "The character is seated on a low weathered wooden crate in a natural papaya plantation on a normal day. "
                "Tall papaya trees with large green and yellow fruits hanging from the trunks. "
                "Fallen papaya leaves and some ripe fruits are scattered on the ground. "
                "In the far background, a few villagers can be seen harvesting papaya. "
                "Tall plantation atmosphere."
            ),
            "Kebun Pepaya dengan Gubuk": (
                "The character is seated on a low weathered wooden crate beside a simple fresh green bamboo gubuk in the papaya plantation. "
                "Tall papaya trees with large green and yellow fruits hanging near the gubuk. "
                "Fallen papaya leaves and some ripe fruits are scattered around the gubuk area. "
                "A sturdy gubuk made of fresh green bamboo poles with a thatched roof stands nearby. "
                "Tall plantation atmosphere near the gubuk."
            ),
            "Kebun Pisang Biasa": (
                "The character is seated on a low weathered wooden crate in a natural banana plantation on a normal day. "
                "Tall banana trees with large green and yellow banana bunches hanging. "
                "Fallen banana leaves and some ripe bananas are scattered on the ground. "
                "In the far background, a few villagers can be seen harvesting bananas. "
                "Tall banana grove atmosphere."
            ),
            "Kebun Pisang dengan Gubuk": (
                "The character is seated on a low weathered wooden crate beside a simple fresh green bamboo gubuk in the banana plantation. "
                "Tall banana trees with large green and yellow banana bunches hanging near the gubuk. "
                "Fallen banana leaves and some ripe bananas are scattered around the gubuk area. "
                "A sturdy gubuk made of fresh green bamboo poles with a thatched roof stands nearby. "
                "Tall banana grove atmosphere near the gubuk."
            ),
            "Kebun Jeruk Biasa": (
                "The character is seated on a low weathered wooden crate under rows of mature orange trees in a sunny Javanese orchard. "
                "Tall trees with glossy green leaves and bright orange fruits hanging heavily from the branches. "
                "Dry fallen leaves and some ripe oranges scattered on the ground. "
                "In the far distance, villagers are picking oranges using long bamboo poles. "
                "Bright and airy orchard atmosphere with the scent of citrus in the air."
            ),
            "Kebun Jeruk Lebat": (
                "The character is seated on a low weathered wooden crate in a dense orange orchard where trees grow close together. "
                "Heavy clusters of ripe oranges weigh down the branches, almost touching the ground in some places. "
                "Thick canopy creates dappled sunlight on the earth below. "
                "In the distance, several villagers are busy filling baskets with harvested oranges. "
                "Lush and shaded citrus orchard atmosphere."
            ),
            "Kebun Salak Biasa": (
                "The character is seated on a low weathered wooden crate among salak palms in a village plantation. "
                "Short palm trees with sharp leaves and clusters of brown scaly fruits hanging near the base. "
                "Dry palm fronds and fallen salak fruits cover the ground. "
                "In the far background, villagers are cutting salak clusters with knives. "
                "Shady and humid salak palm atmosphere."
            ),
            "Kebun Salak Lebat": (
                "The character is seated on a low weathered wooden crate in a thick salak plantation where palms grow densely. "
                "Numerous brown scaly salak fruits cluster heavily at the base of the palms. "
                "Sharp dry leaves carpet the ground almost completely. "
                "Villagers in the distance are harvesting salak in large baskets. "
                "Dense and prickly salak palm grove atmosphere."
            ),
            "Kebun Anggur Biasa": (
                "The character is seated on a low weathered wooden crate in a traditional grape vineyard. "
                "Grape vines climb neatly on wooden trellises with clusters of ripe green and purple grapes hanging. "
                "Some fallen grapes and dry leaves lie on the soil. "
                "In the far background, villagers are picking grapes into woven baskets. "
                "Sunny vineyard atmosphere with rows of trellises."
            ),
            "Kebun Anggur Lebat": (
                "The character is seated on a low weathered wooden crate in a lush grape vineyard where vines grow thickly. "
                "Heavy clusters of ripe grapes hang low from the trellises, almost touching the ground. "
                "Dense foliage creates shaded spots on the earth. "
                "Villagers in the distance are carefully harvesting the heavy grape bunches. "
                "Lush and shaded grape vineyard atmosphere."
            ),
            "Kebun Nanas Biasa": (
                "The character is seated on a low weathered wooden crate in a pineapple plantation. "
                "Low pineapple plants with spiky leaves and ripe yellow-brown fruits growing close to the ground. "
                "Dry pineapple leaves scattered between the plants. "
                "In the far background, villagers are cutting pineapples with long knives. "
                "Open and sunny pineapple field atmosphere."
            ),
            "Kebun Nanas Lebat": (
                "The character is seated on a low weathered wooden crate in a dense pineapple plantation. "
                "Pineapple plants grow tightly together with many ripe fruits visible among the sharp leaves. "
                "Thick layer of dry pineapple leaves covers the ground. "
                "Villagers in the distance are harvesting pineapples in large numbers. "
                "Dense and spiky pineapple field atmosphere."
            ),
            "Kebun Strawberry Biasa": (
                "The character is seated on a low weathered wooden crate in a strawberry field. "
                "Low strawberry plants with bright red ripe fruits peeking from under the leaves. "
                "Soft soil with some dry straw mulch between the plants. "
                "In the far background, villagers are picking strawberries into small baskets. "
                "Low-growing berry field atmosphere."
            ),
            "Kebun Strawberry Lebat": (
                "The character is seated on a low weathered wooden crate in a thick strawberry field. "
                "Strawberry plants grow densely with abundant ripe red fruits visible everywhere. "
                "Ground covered with straw mulch and fallen berries. "
                "Villagers in the distance are busy harvesting strawberries. "
                "Dense and abundant strawberry patch atmosphere."
            ),
            "Kebun Kelapa Biasa": (
                "The character is seated on a low weathered wooden crate in a coconut grove. "
                "Tall coconut trees with large green coconuts hanging high in the crowns. "
                "Fallen coconut husks and dry leaves scattered on the ground. "
                "In the far background, villagers are climbing trees to harvest coconuts. "
                "Tall and breezy coconut grove atmosphere."
            ),
            "Kebun Kelapa Lebat": (
                "The character is seated on a low weathered wooden crate in a dense coconut grove. "
                "Tall coconut trees grow close together with many large green coconuts hanging heavily. "
                "Thick layer of fallen husks and dry fronds cover the ground. "
                "Villagers in the distance are harvesting coconuts. "
                "Dense and shaded coconut grove atmosphere."
            ),
            "Kebun Jagung Biasa": (
                "The character is seated on a low weathered wooden crate in a tall corn field on a normal day. "
                "Tall corn stalks with ripe yellow cobs visible on the plants. "
                "Dry corn leaves rustle in the breeze. "
                "In the far background, villagers are harvesting corn. "
                "Tall and open corn field atmosphere."
            ),
            "Kebun Jagung Lebat": (
                "The character is seated on a low weathered wooden crate in a dense corn field. "
                "Tall corn stalks grow very closely together with many ripe yellow cobs. "
                "Thick canopy of corn leaves blocks much of the sunlight. "
                "Villagers in the distance are harvesting corn. "
                "Dense and tall corn field atmosphere."
            ),
            "Kebun Tomat Biasa": (
                "The character is seated on a low weathered wooden crate in a tomato garden on a normal day. "
                "Tomato plants with clusters of ripe red tomatoes hanging from the vines. "
                "Some fallen tomatoes and leaves on the soil. "
                "In the far background, villagers are picking tomatoes. "
                "Open tomato garden atmosphere."
            ),
            "Kebun Tomat Lebat": (
                "The character is seated on a low weathered wooden crate in a thick tomato garden. "
                "Tomato plants grow densely with heavy clusters of ripe red tomatoes. "
                "Ground covered with fallen tomatoes and leaves. "
                "Villagers in the distance are harvesting tomatoes. "
                "Dense and productive tomato garden atmosphere."
            ),
            "Kebun Cabe Biasa": (
                "The character is seated on a low weathered wooden crate in a chili garden on a normal day. "
                "Chili plants with bright red and green chilies hanging in clusters. "
                "Some fallen chilies scattered on the ground. "
                "In the far background, villagers are harvesting chilies. "
                "Spicy and open chili garden atmosphere."
            ),
            "Kebun Cabe Lebat": (
                "The character is seated on a low weathered wooden crate in a dense chili garden. "
                "Chili plants grow thickly with abundant bright red and green chilies. "
                "Ground covered with fallen chilies. "
                "Villagers in the distance are harvesting chilies. "
                "Dense and spicy chili garden atmosphere."
            ),			
            "Kebun Sayuran Mix Biasa": (
                "The character is seated on a low weathered wooden crate in a mixed vegetable garden on a normal day. "
                "Various vegetables grow together in a natural, slightly messy way: eggplants, long beans, spinach, and chili plants. "
                "Dark brown soil with some patches of grass and scattered dry leaves. "
                "In the far background, a few villagers are tending to the plants and picking vegetables. "
                "Peaceful and productive mixed vegetable garden atmosphere."
            ),
            "Kebun Sayuran Mix dengan Sungai Kecil": (
                "The character is seated on a low weathered wooden crate beside a small shallow stream in a mixed vegetable garden. "
                "Clear water flows slowly beside rows of eggplants, kangkung, tomatoes, and chili plants. "
                "Wet soil near the stream and lush green vegetables growing abundantly. "
                "A few ducks are waddling near the water. "
                "Calm and fresh mixed vegetable garden with a small stream atmosphere."
            ),
            "Kebun Sayuran Mix dengan Gubuk": (
                "The character is seated on a low weathered wooden crate right next to a small bamboo gubuk in a mixed vegetable garden. "
                "The gubuk is surrounded by dense vegetables: cabbage, long beans, mustard greens, and chili plants. "
                "Some harvested vegetables are piled near the gubuk entrance. "
                "A few chickens are pecking around the garden. "
                "Cozy and lived-in mixed vegetable garden with a small bamboo shelter atmosphere."
            ),
            "Sawah Biasa": (
                "The character is seated on a low weathered wooden crate at the edge of a wide rice paddy on a normal day. "
                "Vast green rice fields stretch out with young rice plants swaying gently. "
                "Narrow dirt paths separate the paddies, with some water visible in the fields. "
                "In the far distance, several farmers are working in the rice fields. "
                "Open and expansive rice field atmosphere."
            ),
            "Sawah dengan Pohon Kelapa": (
                "The character is seated on a low weathered wooden crate at the edge of a rice paddy with tall coconut trees nearby. "
                "Lush green rice plants fill the field, with some mature golden patches ready for harvest. "
                "Tall coconut trees stand along the edge of the paddy, their fronds moving in the breeze. "
                "A few farmers can be seen working in the distance. "
                "Scenic rice paddy with coconut trees atmosphere."
            ),
			"Sawah dengan Gubuk di Tengah": (
                "The character is seated on a low weathered wooden crate on a small raised platform beside a simple bamboo gubuk standing right in the middle of the rice paddy. "
                "The gubuk is surrounded by water and young green rice plants on all sides. "
                "Narrow dirt paths lead to the gubuk, with water reflecting the sky in the flooded fields. "
                "Tall rice stalks sway gently around the structure, some already turning golden. "
                "A few birds fly over the vast green sawah. "
                "Peaceful and isolated rice field atmosphere with a lone gubuk in the middle of the paddy."
            ),
			"Kebun Bunga Biasa": (
                "The character is seated on a low weathered wooden crate in a simple village flower garden on a normal day. "
                "Various colorful flowers grow in a natural, slightly messy arrangement: roses, marigolds, jasmine, and hibiscus. "
                "Dark brown earth with patches of grass and scattered fallen petals. "
                "In the far background, a few villagers can be seen tending to the flowers. "
                "Gentle and fragrant village flower garden atmosphere."
            ),
            "Taman Bunga dengan Gazebo Kecil": (
                "The character is seated on a low weathered wooden crate beside a small traditional bamboo gazebo in a beautiful village flower garden. "
                "Colorful flowers bloom abundantly around the gazebo: bright bougainvillea climbing the bamboo, roses, lilies, and orchids. "
                "Stone path leads to the gazebo with fallen flower petals scattered on the ground. "
                "The air feels fresh and fragrant with the scent of blooming flowers. "
                "Peaceful and scenic village flower garden atmosphere with a small bamboo gazebo."
            ),
			"Pinggir Sungai Desa": (
                "The character is seated on a low weathered wooden crate near a small clear village stream. "
                "Gentle flowing water with smooth rocks and lush green grass on the banks. "
                "Bamboo trees and wild ferns grow along the river. "
                "A few women can be seen washing clothes downstream. "
                "Calm and refreshing riverside atmosphere."
            ),
            "Pinggir Hutan Bambu": (
                "The character is seated on a low weathered wooden crate at the edge of a dense bamboo forest. "
                "Tall green bamboo stalks sway gently in the breeze, creating soft rustling sounds. "
                "Soft sunlight filters through the canopy onto the forest floor covered with dry leaves. "
                "A small dirt path leads deeper into the bamboo grove. "
                "Cool and serene bamboo forest edge atmosphere."
            ),
            "Ladang Jagung Kuning": (
                "The character is seated on a low weathered wooden crate in a tall golden corn field ready for harvest. "
                "Tall dry corn stalks with ripe yellow cobs visible. "
                "Dry corn leaves rustle loudly in the wind. "
                "In the far distance, villagers are harvesting corn. "
                "Warm and golden corn field atmosphere."
            ),
            "Pinggir Danau Kecil": (
                "The character is seated on a low weathered wooden crate by the edge of a small calm village lake. "
                "Clear water reflects the sky and surrounding trees. "
                "Lotus plants and water lilies float on the surface. "
                "A few ducks swim quietly near the shore. "
                "Tranquil and serene small lake atmosphere."
            ),
            "Bukit Kecil Desa": (
                "The character is seated on a low weathered wooden crate on a gentle grassy hill overlooking the village. "
                "Rolling green hills with scattered trees and distant rice paddies visible below. "
                "A light breeze blows through the grass. "
                "A few goats graze peacefully on the hillside. "
                "Peaceful and open hilltop atmosphere."
            ),
            "Pinggir Hutan Pinus": (
                "The character is seated on a low weathered wooden crate at the edge of a pine forest. "
                "Tall pine trees with fallen needles covering the ground. "
                "Fresh pine scent fills the air as the trees sway gently. "
                "Soft sunlight creates long shadows on the forest floor. "
                "Cool and aromatic pine forest edge atmosphere."
            ),
            "Ladang Teh": (
                "The character is seated on a low weathered wooden crate on the edge of a lush tea plantation. "
                "Neat rows of tea bushes cover the rolling hills with fresh green leaves. "
                "A light mist lingers in the air. "
                "In the distance, workers are picking tea leaves. "
                "Fresh and misty tea plantation atmosphere."
            ),
            "Pantai Desa Kecil": (
                "The character is seated on a low weathered wooden crate on a quiet village beach. "
                "Gentle waves lap against the sandy shore with coconut trees lining the coast. "
                "Fishing boats are pulled up on the sand. "
                "A few fishermen are mending nets in the distance. "
                "Calm and breezy small village beach atmosphere."
            ),
            "Pinggir Gunung Kecil": (
                "The character is seated on a low weathered wooden crate on a foothill with a view of the mountain. "
                "Steep green slopes with rocky outcrops and wildflowers. "
                "A small waterfall can be heard in the distance. "
                "Cool mountain breeze blows through the area. "
                "Fresh and majestic foothill atmosphere."
            ),
            "Lembah Kecil Desa": (
                "The character is seated on a low weathered wooden crate in a quiet small valley surrounded by hills. "
                "Green fields and scattered trees fill the valley floor. "
                "A narrow river winds through the middle of the valley. "
                "A few houses with smoke rising from the chimneys can be seen in the distance. "
                "Quiet and peaceful small valley atmosphere."
            ),
			"Teras Rumah Jati": (
                "The character is seated on the spacious wooden terrace of a traditional Javanese house made of dark jati wood. "
                "Smooth aged jati planks with visible grain and natural patina from years of use. "
                "A few simple wooden chairs and a low table are placed on the terrace. "
                "Clothes are hanging to dry on a line at the side. "
                "Calm and dignified jati wood terrace atmosphere."
            ),
            "Rumah Ukiran": (
                "The character is seated on a low weathered wooden bench on the terrace of a beautifully carved Javanese house. "
                "Intricate traditional wood carvings adorn the pillars and door frames. "
                "The house has a classic joglo style with detailed ornamentation. "
                "Soft afternoon light falls on the carved wooden details. "
                "Elegant and traditional carved house terrace atmosphere."
            ),
            "Rumah Bambu Hijau": (
                "The character is seated on a low wooden bench beside a simple house made of fresh green bamboo. "
                "The walls and structure are built from natural bamboo poles with a thatched roof. "
                "Green vines climb gently on the bamboo walls. "
                "A few potted plants are placed near the entrance. "
                "Fresh and natural bamboo house atmosphere."
            ),
            "Halaman Depan Rumah": (
                "The character is seated on a low weathered wooden bench in the front yard of a modest village house. "
                "Swept earth ground with a few flowering plants and shrubs near the entrance. "
                "An old wooden gate with climbing bougainvillea stands at the front. "
                "Warm and welcoming front yard atmosphere."
            ),
            "Halaman Belakang Rumah": (
                "The character is seated on a low weathered wooden crate in the backyard of the village house. "
                "Small vegetable plot with chili, long beans, and spinach growing near the back wall. "
                "A clothesline with faded sarongs and shirts sways gently in the breeze. "
                "Practical and everyday backyard atmosphere."
            ),
            "Pekarangan Rumah dengan Pohon Mangga": (
                "The character is seated on a low weathered wooden bench under a large old mango tree in the house yard. "
                "Thick mango tree providing shade with some fruits still hanging and fallen leaves on the ground. "
                "A few ripe mangoes lie scattered near the bench. "
                "Shady and fruity yard atmosphere under the mango tree."
            ),
            "Halaman Samping Rumah": (
                "The character is seated on a low weathered wooden crate in the narrow side yard of the village house. "
                "A row of potted plants and herbs lines the wall of the house. "
                "Some drying herbs hang from a simple rack. "
                "Quiet and functional side yard atmosphere."
            ),
            "Teras Belakang Rumah": (
                "The character is seated on the back wooden terrace of the village house. "
                "Rough weathered wooden floor overlooking the backyard. "
                "A few simple tools and baskets are placed neatly in the corner. "
                "Calm and private back terrace atmosphere."
            ),
            "Halaman Rumah dengan Tempat Cuci": (
                "The character is seated on a low weathered wooden bench in the side yard near the outdoor washing area. "
                "A large stone basin and several buckets are placed near the house wall. "
                "Wet clothes hang on a line nearby. "
                "Everyday practical yard atmosphere with washing area."
            ),
            "Pekarangan Rumah dengan Tanaman Obat": (
                "The character is seated on a low weathered wooden crate in the yard where medicinal plants grow. "
                "Various herbs like turmeric, ginger, lemongrass, and sambiloto are planted in neat but natural rows. "
                "A small wooden rack holds drying medicinal leaves. "
                "Fragrant and healing herbal yard atmosphere."
            ),
            "Ruang Tamu Rumah Jati": (
                "The character is seated on a low wooden chair in the simple living room of a traditional Javanese house made of dark jati wood. "
                "Aged jati furniture with visible wood grain and a low coffee table in the center. "
                "Soft natural light enters through the wooden windows. "
                "A few family photos and an old wall clock hang on the wall. "
                "Calm and warm traditional jati living room atmosphere."
            ),
            "Dapur Rumah Kayu": (
                "The character is seated on a low wooden stool in the simple kitchen inside the village house. "
                "A traditional firewood stove with clay pots and hanging cooking utensils. "
                "Some fresh vegetables and spices are placed on a wooden counter. "
                "Faint smell of cooking lingers in the air. "
                "Warm and functional village kitchen atmosphere."
            ),
            "Kamar Tidur Nenek": (
                "The character is seated on the edge of a simple wooden bed in her modest bedroom. "
                "A thin mattress with a faded batik bedcover and a mosquito net hanging above. "
                "An old wooden wardrobe and a small mirror on the wall. "
                "Soft light filters through the window with lace curtains. "
                "Quiet and personal bedroom atmosphere."
            ),
            "Ruang Keluarga Kecil": (
                "The character is seated on a low bamboo mat in the small family room inside the house. "
                "A simple wooden TV cabinet and a few floor cushions around the room. "
                "Family photos and a calendar hang on the wall. "
                "Natural light comes from the side windows. "
                "Cozy and intimate family room atmosphere."
            ),
            "Serambi Dalam": (
                "The character is seated on a low wooden bench in the inner serambi of the traditional house. "
                "Polished wooden floor with visible grain and simple carved wooden pillars. "
                "A few rolled mats are stored neatly in the corner. "
                "Soft diffused light enters from the open side. "
                "Traditional and serene inner serambi atmosphere."
            ),
            "Ruang Makan Sederhana": (
                "The character is seated at a low wooden dining table inside the house. "
                "Simple wooden chairs and a few plates with glasses on the table. "
                "A ceiling fan hangs above and basic utensils are stored on a sideboard. "
                "Warm afternoon light comes through the window. "
                "Simple and everyday dining area atmosphere."
            ),
            "Sudut Doa Rumah": (
                "The character is seated on a prayer mat in a quiet corner of the house used for prayer. "
                "A small wooden Quran stand and a folded prayer rug are placed neatly. "
                "Soft light from a small window illuminates the corner. "
                "Calm and spiritual prayer corner atmosphere."
            ),
            "Sudut Jahit Nenek": (
                "The character is seated on a low wooden stool in the corner where she usually sews. "
                "An old sewing machine on a small table with colorful threads and fabric pieces. "
                "A basket of unfinished sewing projects sits nearby. "
                "Gentle light falls on the sewing area. "
                "Warm and personal sewing corner atmosphere."
            ),
            "Ruang Depan Dekat Pintu": (
                "The character is seated on a low wooden bench near the main entrance inside the house. "
                "Traditional wooden door with simple carvings and a small shoe rack. "
                "A few daily items like an umbrella and a shopping bag hang on the wall. "
                "Natural light enters from the open doorway. "
                "Welcoming entrance area atmosphere."
            ),
            "Kamar Belakang Rumah": (
                "The character is seated on the edge of a simple bed in the back bedroom of the village house. "
                "A thin mattress with an old batik bedcover and a small wooden side table. "
                "A window with simple curtains overlooking the backyard. "
                "Quiet and private back bedroom atmosphere."
            ),
			"Sawah Hijau Muda": (
                "The character is seated on a low weathered wooden crate at the edge of a vast young rice paddy. "
                "Bright green rice plants sway gently across the flooded field. "
                "Narrow dirt bunds separate the paddies with water reflecting the sky. "
                "In the distance, farmers are working in the rice fields. "
                "Fresh and expansive young rice paddy atmosphere."
            ),
            "Sawah Siap Panen": (
                "The character is seated on a low weathered wooden crate at the edge of a golden rice field ready for harvest. "
                "Mature rice stalks turn golden yellow and sway in the breeze. "
                "Some farmers can be seen cutting rice with sickles in the distance. "
                "Warm and bountiful harvest-ready sawah atmosphere."
            ),
            "Sawah dengan Gubuk di Tengah": (
                "The character is seated on a low weathered wooden crate on a small raised platform beside a simple bamboo gubuk standing right in the middle of the rice paddy. "
                "The gubuk is surrounded by water and green rice plants on all sides. "
                "Narrow dirt paths lead to the gubuk. "
                "A few birds fly over the vast green sawah. "
                "Peaceful and isolated rice field atmosphere with a lone gubuk in the middle."
            ),
            "Sawah dengan Pohon Kelapa": (
                "The character is seated on a low weathered wooden crate at the edge of a rice paddy with tall coconut trees nearby. "
                "Green rice plants fill the field, with some mature golden patches. "
                "Tall coconut trees stand along the edge, their fronds moving in the breeze. "
                "Scenic rice paddy with coconut trees atmosphere."
            ),
            "Sawah di Lereng Bukit": (
                "The character is seated on a low weathered wooden crate on a terraced rice paddy on a gentle hillside. "
                "Layered rice fields follow the contour of the hill with water sparkling between terraces. "
                "In the distance, farmers are tending the upper terraces. "
                "Scenic and layered hillside rice paddy atmosphere."
            ),
			"Belakang Rumah dengan Taman Bunga": (
                "The character is seated on a low weathered wooden bench in the backyard of the village house with a small flower garden. "
                "Colorful flowers bloom naturally: roses, jasmine, marigolds, and hibiscus around the yard. "
                "Fallen petals scatter on the swept earth ground. "
                "A few potted plants are placed near the house wall. "
                "Peaceful and fragrant backyard flower garden atmosphere."
            ),
            "Belakang Rumah dengan Kolam Ikan Kecil": (
                "The character is seated on a low weathered wooden bench in the backyard beside a small fish pond. "
                "Clear water in the shallow pond with a few goldfish swimming and water lilies floating on the surface. "
                "Stone edging around the pond with some moss. "
                "Soft sound of water and gentle breeze. "
                "Calm and serene backyard with small fish pond atmosphere."
            ),
            "Belakang Rumah dengan Pohon Buah": (
                "The character is seated on a low weathered wooden crate under a large mango tree in the backyard. "
                "Thick mango tree providing shade with some ripe mangoes still hanging and fallen leaves on the ground. "
                "A few other fruit trees like guava and papaya are also planted nearby. "
                "Shady and fruity backyard with fruit trees atmosphere."
            ),
            "Belakang Rumah dengan Kebun Sayur Kecil": (
                "The character is seated on a low weathered wooden bench in the backyard with a small vegetable plot. "
                "Chili plants, long beans, spinach, and tomatoes grow in neat but natural rows. "
                "A simple bamboo trellis supports the climbing vegetables. "
                "Some harvested vegetables are placed in a basket nearby. "
                "Practical and green backyard vegetable garden atmosphere."
            ),
            "Belakang Rumah dengan Area Santai": (
                "The character is seated on a low weathered wooden bench in the quiet backyard relaxation area. "
                "A simple bamboo pergola with climbing plants provides partial shade. "
                "A few potted flowers and a small wooden table with a teapot are placed nearby. "
                "Soft natural light filters through the plants. "
                "Cozy and relaxing backyard atmosphere."
            ),
			"Depan Warung Kelontong": (
                "The character is seated on a low wooden bench in front of a small village kelontong warung. "
                "The warung has colorful snack packets, soap, and daily goods displayed on wooden shelves. "
                "A few villagers are buying things and chatting with the owner. "
                "Warm and lively small village shop atmosphere."
            ),
            "Depan Warkop Sederhana": (
                "The character is seated on a low wooden bench in front of a simple village warkop. "
                "Plastic chairs and tables are arranged outside with glasses of sweet tea. "
                "A few men are sitting and talking while drinking coffee. "
                "The smell of kopi tubruk and fried snacks fills the air. "
                "Casual and social village coffee shop atmosphere."
            ),
            "Depan Kios Rokok & Pulsa": (
                "The character is seated on a low wooden stool in front of a small kiosk selling cigarettes and phone credit. "
                "Colorful cigarette packs and pulsa signs are displayed on the front. "
                "A few young men are standing and buying pulsa. "
                "Busy and everyday small kiosk atmosphere."
            ),
            "Pinggir Jalan dengan Penjual Gorengan": (
                "The character is seated on a low wooden bench beside a gorengan seller on the side of the village road. "
                "The seller is frying tempe, tahu, and pisang goreng on a small cart with smoke rising. "
                "Several people are waiting and buying snacks. "
                "Lively roadside fried snack stall atmosphere."
            ),
            "Pinggir Jalan dengan Penjual Es": (
                "The character is seated on a low wooden bench near an es seller on the village roadside. "
                "The cart has colorful syrup bottles and shaved ice. "
                "Children and adults are buying colorful es dawet and es campur. "
                "Hot afternoon roadside ice drink stall atmosphere."
            ),
            "Depan Warung Makan Kecil": (
                "The character is seated on a low wooden bench in front of a tiny warung makan by the roadside. "
                "Simple menu board with nasi goreng and mie ayam written by hand. "
                "A few customers are eating at plastic tables outside. "
                "The smell of fried rice and spices fills the air. "
                "Humble roadside warung makan atmosphere."
            ),
            "Pinggir Jalan dengan Penjual Buah": (
                "The character is seated on a low wooden bench beside a fruit seller on the village road. "
                "Fresh mangoes, rambutan, and bananas are arranged on a wooden cart. "
                "The seller is weighing fruits for customers. "
                "Several people are stopping to buy fruits. "
                "Fresh and colorful roadside fruit stall atmosphere."
            ),
            "Depan Kios Koran & Kopi": (
                "The character is seated on a low wooden bench in front of a small kiosk selling newspapers and coffee. "
                "Morning newspapers are displayed on a rack. "
                "A few older men are reading newspapers while drinking coffee. "
                "Relaxed morning village kiosk atmosphere."
            ),
            "Pinggir Jalan dengan Penjual Sate": (
                "The character is seated on a low wooden bench near a sate seller on the roadside. "
                "Smoke rises from the charcoal grill as the seller fans the sate. "
                "The aroma of grilled chicken sate fills the air. "
                "Several people are waiting for their order. "
                "Lively roadside sate stall atmosphere."
            ),
            "Pinggir Jalan Desa Sore Hari": (
                "The character is seated on a low wooden bench by the quiet village roadside in the late afternoon. "
                "A few small food stalls are open with people buying snacks for maghrib. "
                "Children are playing nearby and motorcycles pass occasionally. "
                "Warm and relaxed late afternoon village roadside atmosphere."
            ),
			"Tempat Barang Bekas di Pinggir Jalan": (
                "The character is seated on a low weathered wooden crate beside a large pile of scrap items on the village roadside. "
                "Old tires, rusty bicycle frames, broken plastic chairs, and tangled wires are stacked messily. "
                "A few villagers are sorting through the scraps. "
                " Dusty and cluttered roadside scrap yard atmosphere."
            ),
            "Halaman Belakang dengan Tumpukan Barang Bekas": (
                "The character is seated on a low wooden bench in the backyard filled with accumulated old items. "
                "Broken wooden furniture, old buckets, rusty farming tools, and empty jerry cans are scattered around. "
                "Some items are covered with tarpaulin. "
                "Cluttered and practical backyard full of old stuff atmosphere."
            ),
            "Depan Gudang Barang Bekas": (
                "The character is seated on a low stool in front of a small shed used to store scrap materials. "
                "Piles of old metal sheets, broken electronics, and plastic bottles are stacked high near the entrance. "
                "A weighing scale and some sacks are visible. "
                "Busy and dusty scrap storage atmosphere."
            ),
            "Tempat Pembuangan Barang Bekas": (
                "The character is seated on a low wooden crate near a large open area where villagers dump old items. "
                "Broken televisions, old mattresses, rusty stoves, and tangled fishing nets are thrown together. "
                "Some items are partially buried in the dirt. "
                "Chaotic and abandoned scrap dumping ground atmosphere."
            ),
            "Pinggir Sungai dengan Barang Bekas": (
                "The character is seated on a low wooden bench near the riverbank where old items have accumulated. "
                "Plastic bottles, old sandals, broken buckets, and fishing nets are washed up along the edge. "
                "The river flows slowly beside the trash. "
                "Messy riverside scrap accumulation atmosphere."
            ),
            "Halaman Rumah Penuh Barang Bekas": (
                "The character is seated on a low wooden chair in the front yard filled with collected old things. "
                "Stacks of empty paint cans, old doors, broken windows, and metal pipes are arranged along the wall. "
                "The yard looks like a small recycling collection point. "
                "Cluttered household scrap collection atmosphere."
            ),
            "Tempat Besi Tua dan Rongsokan": (
                "The character is seated on a low wooden crate in an area full of scrap metal. "
                "Rusty iron rods, old car parts, bent metal sheets, and engine pieces are piled up. "
                "The ground is covered with metal dust and small fragments. "
                "Heavy and industrial scrap metal yard atmosphere."
            ),
            "Sudut Kampung dengan Tumpukan Plastik": (
                "The character is seated on a low wooden bench in a corner of the village where plastic waste is collected. "
                "Huge piles of colorful plastic bottles, bags, and containers are stacked high. "
                "The wind occasionally blows some light plastic pieces. "
                "Colorful but messy plastic scrap collection atmosphere."
            ),
            "Belakang Warung dengan Barang Bekas": (
                "The character is seated on a low wooden stool behind a small warung filled with old inventory. "
                "Empty cardboard boxes, old glass bottles, broken shelves, and expired goods are piled up. "
                "Some items are being sorted for recycling. "
                "Back alley of a shop full of old stock atmosphere."
            ),
            "Lapangan Kecil Penuh Barang Rongsokan": (
                "The character is seated on a low weathered wooden crate at the edge of a small open field used as a scrap yard. "
                "Old motorcycles, broken furniture, discarded refrigerators, and tangled wires cover the area. "
                "A few people are searching for usable items among the pile. "
                "Chaotic and expansive village scrap field atmosphere."
            )
        }
		
		# --- 4. MASTER AUDIO & SOULFUL EXPRESSION (ULTRA STABLE VOICE SYSTEM) ---
        MASTER_AUDIO_STYLE = {
            "Logat_Nenek": [
                "Extremely frail 92-95 year old Javanese village grandmother with thick rural Jawa kampung accent, extremely weak thin breaking voice, constant heavy vocal tremor, raspy hoarse cracking tone, very breathy and airy quality, speaks extremely slowly with long shaky pauses and tired breathing effort, frequent voice cracks on almost every word, sounds physically exhausted and delicate like a real 93+ year old nenek tua with severely weakened lungs",
                "Super elderly 93-year-old Javanese nenek with strong kampung ngoko accent, deeply aged thin trembling voice full of instability, whispery and breaking at times, heavy constant vocal tremor, very low volume, extremely slow shaky delivery, frequent cracking and quivering, authentic extreme old age vocal deterioration with almost no energy left",
                "94+ year old extremely frail Indonesian grandma with thick Jawa kampung accent, very weak raspy voice with strong constant quivering tremor, dry cracked hoarse tone, thin wobbly resonance, labored slow speech with many long pauses for breath, voice often cracks and sounds like it's about to disappear",
                "91-year-old frail nenek tua with thick rural Javanese accent, constantly shaking elderly female voice with high-frequency vocal tremor, very breathy hoarse quality, extremely slow and weak delivery, frequent voice cracks and sudden drops in volume, heavy tired natural breathing"
            ],
            "Logat_Kakek": [
                "Extremely frail 90-93 year old Indonesian village grandfather with thick Jawa kampung accent, deep but very weak raspy old man voice, noticeable heavy vocal tremor, dry cracked hoarse tone, slow labored delivery with long pauses and breath effort, sounds weathered and exhausted like a real 92+ year old kakek",
                "Very old 91-year-old Javanese kakek with rural kampung accent, low-pitched trembling elderly male voice full of instability, heavy age-related wobble, hoarse and rough texture, extremely slow unsteady speech with frequent voice cracks and breath breaks",
                "93+ year old extremely frail Indonesian grandfather with strong Jawa accent, thin shaky old man voice, strong constant vocal tremor, dry cracked breathy tone, extremely slow and effortful delivery, sounds delicate and on the verge of breaking",
                "89-year-old frail kakek tua with thick kampung accent, deep raspy voice with constant trembling, weak resonance, slow unsteady speech with many weary pauses, hoarse from decades of use, sounds physically tired and fragile"
            ],
            "Mood": [
                "Sad and deeply fragile",
                "Tired and resigned with heavy exhaustion",
                "Calm but physically very weak",
                "Peaceful with quiet melancholy",
                "Gentle and nostalgic with shaky delivery",
                "Stoic with visible physical frailty"
            ],
            "Physical Action": [
                "Gently resting her trembling fingers on the edge of the miniature while looking at it quietly.",
                "Lightly touching the carved surface with shaky fingertips, moving very slowly.",
                "Holding the side of the miniature with both frail hands, barely moving it.",
                "Softly tracing a small detail on the object with one unsteady finger.",
                "Resting both trembling hands on the table near the miniature while gazing at it.",
                "Gently placing one shaky hand on top of the miniature for a moment, then lifting it slowly.",
                "Using her frail fingers to lightly brush away a tiny speck from the base of the object.",
                "Keeping her shaky hands close to the miniature without lifting it, just resting nearby."
            ]
        }

        # --- UI LAYOUT ---
        with st.expander("🕌 PINTAR MASJID ENGINE", expanded=True):
            st.markdown('<p class="small-label">PILIH MODUS KONTEN</p>', unsafe_allow_html=True)
            modus_konten = st.selectbox("Select Mode", list(MASTER_KONTEN_ALL.keys()), label_visibility="collapsed")
            st.divider()
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<p class="small-label">PILIH KARAKTER</p>', unsafe_allow_html=True)
                pilihan_user = st.selectbox("Select Character", list(MASTER_FAMILY_SOUL.keys()), label_visibility="collapsed")
                char_key = pilihan_user
            with c2:
                st.markdown(f'<p class="small-label">PAKAIAN {char_key.split(" (")[0].upper()}</p>', unsafe_allow_html=True)
                if char_key in MASTER_FAMILY_WARDROBE:
                    baju_options = list(MASTER_FAMILY_WARDROBE[char_key].keys())
                else:
                    baju_options = ["Standard Daily Wear"]
                baju_pilihan = st.selectbox("Select Wardrobe", baju_options, label_visibility="collapsed")
   
            c3, c4 = st.columns(2)
            with c3:
                st.markdown('<p class="small-label">DETAIL OBJEK / KARYA</p>', unsafe_allow_html=True)
                objek_list = list(MASTER_KONTEN_ALL[modus_konten].keys())
                pilihan_objek = st.selectbox("Select Detail", objek_list, label_visibility="collapsed")
                deskripsi_teknis = MASTER_KONTEN_ALL[modus_konten][pilihan_objek]
            with c4:
                st.markdown('<p class="small-label">SETTING LOKASI</p>', unsafe_allow_html=True)
                pilihan_set = st.selectbox("Select Environment", list(MASTER_GRANDMA_SETTING.keys()), label_visibility="collapsed")
            st.divider()
            c5, c6 = st.columns([2, 1])
            with c5:
                st.markdown('<p class="small-label">DIALOG (NATURAL INDONESIAN)</p>', unsafe_allow_html=True)
                user_dialog = st.text_area(
                    "Input Dialog",
                    placeholder=f"Tulis dialog {char_key.split(' (')[0]} di sini...",
                    height=250,
                    label_visibility="collapsed"
                )
            with c6:
                st.markdown('<p class="small-label">ACTING & PERFORMANCE</p>', unsafe_allow_html=True)
               
                is_perempuan = any(x in pilihan_user.lower() for x in [
                    "nenek","ibu","aminah","siti","marsi","ponirah","juminah",
                    "sikem","dulah","sartini","tinah","wati"
                ])
               
                if is_perempuan:
                    pilih_logat = st.selectbox("Pilih Logat Suara", MASTER_AUDIO_STYLE["Logat_Nenek"], key="logat_nenek")
                else:
                    pilih_logat = st.selectbox("Pilih Logat Suara", MASTER_AUDIO_STYLE["Logat_Kakek"], key="logat_kakek")
               
                pilih_mood = st.selectbox("Pilih Mood", MASTER_AUDIO_STYLE["Mood"], key="mood_select")
                pilih_aksi = st.selectbox("Pilih Gerakan Tubuh", MASTER_AUDIO_STYLE["Physical Action"], key="aksi_select")
            st.write("")
            btn_gen = st.button("🚀 GENERATE VIDEO PROMPT", type="primary", use_container_width=True)

        # --- LOGIC GENERATOR + FINAL PROMPT ---
        if btn_gen:
            soul_desc = MASTER_FAMILY_SOUL.get(pilihan_user, "")
            baju_desc = MASTER_FAMILY_WARDROBE.get(char_key, {}).get(baju_pilihan, "Simple modest daily clothes")
            env_detail = MASTER_GRANDMA_SETTING.get(pilihan_set, "")
            aksi_final = pilih_aksi.strip()
            mood_final = pilih_mood.strip()
            logat_final = pilih_logat.strip()

            is_perempuan = any(x in pilihan_user.lower() for x in [
                "nenek","ibu","aminah","siti","marsi","ponirah","juminah",
                "sikem","dulah","sartini","tinah","wati"
            ])
           
            # Gender Lock yang sangat ringan (ini penting supaya wajah tidak mirip-mirip)
            if is_perempuan:
                gender_lock = "Elderly Javanese grandmother."
            else:
                gender_lock = "Elderly Javanese grandfather."

            # --- ASSEMBLY PROMPT ---
            GLOBAL_QUALITY_LOCK = (
                "EXTREME 8K SHARPNESS DOCUMENTARY LOOK: Maximum micro-detail and clarity like real film. "
                "MANDATORY: Rich warm skin tones with healthy blood undertone and natural glow — completely reject any pale, grey, or lifeless skin. "
                "Vivid juicy colors on the miniature mosque, deep natural contrast, and rich organic texture. "
                "Razor sharp on wrinkles, age spots, fruit flesh, juice droplets, and wood grain. "
                "NO pale skin, NO washed-out colors, NO flat lighting, NO AI smoothing, NO plastic look."
            )

            final_ai_prompt = (
                f"{GLOBAL_QUALITY_LOCK}\n\n"

                f"ULTRA 8K REALISM & SHARPNESS PRIORITY:\n"
                f"- The handcrafted miniature mosque is the primary focal point with strong frame dominance\n"
                f"- Extremely sharp 8K detail on the miniature mosque: clear carving lines, natural material texture, juicy realistic colors, moist reflections, and organic imperfections\n"
                f"- Character's face, eyes, hands, and skin must also be razor sharp with authentic elderly texture, deep wrinkles, age spots, and natural details\n"
                f"- High natural contrast and vivid but realistic colors between the miniature mosque and the elderly character\n"
                f"- True documentary realism: looks like real 8K film footage, NO CGI, NO plastic look, NO over-smoothed skin, NO artificial glow, NO cartoon style\n\n"

                f"CHARACTER IDENTITY:\n"
                f"{soul_desc}\n"
                f"{gender_lock}\n"
                f"Wardrobe: {baju_desc}\n"
                f"MANDATORY: Hyper-realistic elderly skin texture with deep wrinkles, prominent age spots, sunken tired eyes, fragile appearance, NO face smoothing, NO smile.\n\n"

                f"ENVIRONMENT:\n"
                f"{env_detail}\n\n"

                f"LIGHTING & ATMOSPHERE:\n"
                f"Soft late afternoon natural daylight with rich warm golden undertone, slightly diffused but vibrant. "
                f"Warm golden lighting that gives healthy natural glow and warm blood undertone to the elderly skin, "
                f"while making the miniature mosque colors (fruit rind, juicy flesh, juice droplets, seeds) look extremely rich, vivid, and mouthwatering. "
                f"Strong but natural color saturation, good depth and dimension, no cold tones, no pale skin, no washed-out or flat colors.\n\n"

                f"CAMERA & MOTION:\n"
                f"Strict eye-level straight frontal shot. Tight medium composition. "
                f"The miniature mosque must be in the foreground, perfectly centered and taking up most of the frame. "
                f"The elderly character stands directly behind the mosque, only the upper chest and head slightly visible, facing the camera directly. "
                f"Very slow, smooth, organic handheld movement with subtle natural breathing sway. "
                f"Extremely slow and gentle push-in toward the miniature mosque, maintaining razor sharp focus on both the mosque and the character's face/hands the entire time. "
                f"Absolutely NO high angle, NO low angle, NO static camera, NO sudden moves.\n\n"

                f"PERFORMANCE:\n"
                f"{aksi_final}\n"
                f"Mood: {mood_final}\n"
                f"- Minimal but natural elderly movement with trembling hands\n"
                f"- Eyes slowly alternate between the miniature mosque and camera with tired expression\n\n"

                f"VOICE PROFILE:\n"
                f"{logat_final}\n"
                f"Delivery style: {mood_final}. "
                f"Extremely weak, thin, and breaking voice with constant heavy vocal tremor and instability. "
                f"Thick rural Javanese kampung accent, slow elderly speech pattern. "
                f"Voice cracks frequently, quivers on almost every word, very raspy and hoarse, breathy and airy. "
                f"Extremely slow delivery with long weary pauses and natural tired breathing effort. "
                f"Breathing sounds weak and realistic — not exaggerated or heavy. "
                f"Sounds physically exhausted and delicate like a real 90+ year old nenek/kakek Jawa kampung with very weak lungs and vocal cords.\n\n"

                f"SPOKEN DIALOG:\n"
                f"\"{user_dialog}\"\n\n"

                f"DIALOG DELIVERY RULE:\n"
                f"- AUDIO ONLY. STRICTLY NO TEXT OVERLAY ON SCREEN.\n"
                f"- Spoken naturally as real conversation with elderly shaky Jawa kampung voice\n\n"

                f"OBJECT DETAIL:\n"
                f"{deskripsi_teknis}\n\n"

                f"ULTRA DETAIL ENFORCEMENT:\n"
                f"- Razor sharp 8K detail on every carving line, fruit fiber texture, juice droplets, skin pores, deep wrinkles, age spots, hand veins, and wooden table surface\n"
                f"- Rich natural moist reflections, visible organic imperfections, realistic light interaction, and vivid but natural color saturation\n"
                f"- The miniature mosque and the elderly character's skin must both look extremely sharp, alive, and physically real\n\n"

                f"NEGATIVE PROMPT:\n"
                f"blurry, soft focus, low detail, motion blur, AI look, CGI, plastic texture, over-smooth skin, waxy skin, "
                f"artificial sharpness, glowing edges, fast movement, sudden camera change, static camera, "
                f"energetic voice, young voice, middle-aged voice, heavy breathing, asma sound, "
                f"pale skin, washed-out colors, greyish skin, flat lighting, dull colors, overexposed, "
                f"smiling, laughing, wide shot, high angle, low angle, text, watermark, subtitles, on-screen text"
            )

            # --- TAMPILKAN HASIL ---
            st.success("🔥 PROMPT MASJID READY!")
            st.markdown('<p class="small-label">SALIN PROMPT DI BAWAH INI:</p>', unsafe_allow_html=True)
            st.code(final_ai_prompt, language="text")
			
    # ==========================================================================
    # TAB 2: MASJID VERSI BARU (V8 - NATURAL ROAD MOTION)
    # ==========================================================================
    with t_masjid_v2:
        st.status("Sedang tahap pengembangan...", expanded=False)
        # --- 1. DATA MASTER DNA V8 (KUNCI NATURAL) ---
        MASTER_DNA_V2 = {
            "KARAKTER": {
                "Nenek Tua (Sabar)": "An Indonesian elderly woman, brown traditional headscarf (hijab), weary kind face, deep wrinkles, warm skin tone.",
                "Kakek Tua (Pejuang)": "An Indonesian elderly man, weathered sun-baked skin, wearing a simple black skullcap (peci) and a faded traditional shirt.",
            },
            "PAKAIAN": {
                "Batik Cokelat Kuno": "a very old brown batik shirt with faded patterns, thin fabric texture.",
                "Kebaya Jawa Lusuh": "a simple dark grey traditional kebaya, looking humble and aged."
            },
            "LOKASI": {
                "Pinggir Jalan Pantura": "the dusty roadside edge of a busy Indonesian highway (Pantura). An asphalt road is visible in the background."
            },
            "KENDARAAN": {
                "Truk Kuning-Hijau": "a large yellow-green heavy truck driving at normal speed",
                "Bus Antar Kota": "a large intercity passenger bus driving at normal speed"
            },
            "MASJID": {
                "Masjid Agung Jawa (Kayu)": "a traditional Javanese miniature mosque with a triple-tiered wooden roof (atap tumpuk) made of dark brown wood.",
                "Masjid Kubah Emas": "a majestic miniature mosque with a large golden dome and white marble-textured walls."
            },
            "LOGAT_ONLY": {
                "Napas Tua (The Fading Echo)": "MANDATORY AUDIO: Cracking elderly texture, very slow pace, trembling and fragile voice.",
                "Suara Ompong (Whistling)": "MANDATORY AUDIO: Small whistling texture on 'S' and 'T' sounds, light and humble rising intonation."
            }
        }

        with st.expander("🕌 PINTAR MASJID ENGINE V2 (FIXED LOGIC V8 - STABLE)", expanded=True):
            st.markdown('<p class="small-label">🧬 MASTER DNA SELECTION (V8 NATURAL)</p>', unsafe_allow_html=True)
            
            c1_v2, c2_v2 = st.columns(2)
            with c1_v2:
                pilih_char_v2 = st.selectbox("Pilih DNA Karakter", list(MASTER_DNA_V2["KARAKTER"].keys()), key="dna_char_v2")
                pilih_baju_v2 = st.selectbox("Pilih DNA Pakaian", list(MASTER_DNA_V2["PAKAIAN"].keys()), key="dna_baju_v2")
            
            with c2_v2:
                pilih_set_v2 = st.selectbox("Pilih DNA Lokasi", list(MASTER_DNA_V2["LOKASI"].keys()), key="dna_set_v2")
                pilih_car_v2 = st.selectbox("Pilih DNA Kendaraan", list(MASTER_DNA_V2["KENDARAAN"].keys()), key="dna_car_v2")

            st.divider()

            c3_v2, c4_v2 = st.columns(2)
            with c3_v2:
                st.markdown('<p class="small-label">BENTUK MINIATUR MASJID</p>', unsafe_allow_html=True)
                pilih_masjid_v2 = st.selectbox("Select Mosque", list(MASTER_DNA_V2["MASJID"].keys()), label_visibility="collapsed", key="dna_obj_v2")
            with c4_v2:
                st.markdown('<p class="small-label">AUDIO PERFORMANCE</p>', unsafe_allow_html=True)
                logat_v2 = st.selectbox("Select Audio Character", list(MASTER_DNA_V2["LOGAT_ONLY"].keys()), label_visibility="collapsed", key="v2_logat_key")

            st.write("")
            st.markdown('<p class="small-label">✍️ INPUT DIALOG (ADEGAN B)</p>', unsafe_allow_html=True)
            user_dialog_v2 = st.text_area("Dialog Area", placeholder="Tulis dialog...", height=120, label_visibility="collapsed", key="input_dialog_v2")
            
            btn_gen_v2 = st.button("🚀 GENERATE SEQUENTIAL PROMPTS V8", type="primary", use_container_width=True, key="btn_gen_v2")

        if btn_gen_v2:
            char_dna = MASTER_DNA_V2["KARAKTER"][pilih_char_v2]
            baju_dna = MASTER_DNA_V2["PAKAIAN"][pilih_baju_v2]
            set_dna = MASTER_DNA_V2["LOKASI"][pilih_set_v2]
            car_dna = MASTER_DNA_V2["KENDARAAN"][pilih_car_v2]
            masjid_dna = MASTER_DNA_V2["MASJID"][pilih_masjid_v2]
            audio_dna = MASTER_DNA_V2["LOGAT_ONLY"][logat_v2]

            DNA_LOCK_V8 = f"DNA: {char_dna}\nWARDROBE: {baju_dna}\nPOSITION: Standing at a wooden table, 1 meter from the asphalt road, side-profile view."

            st.success("🔥 SEQUENTIAL PROMPTS V8 READY (STABLE & NATURAL)!")

            # 1. GEMINI MASTER (Natural Distance)
            with st.container(border=True):
                st.subheader("📸 1. Gemini Master Image")
                p_gemini = f"ULTRA-HD 2K RESOLUTION.\n\n{DNA_LOCK_V8}\n\nSCENE: The character is standing by a wooden table, side-profile, focusing on building an 80% finished {masjid_dna}.\nBACKGROUND: The {car_dna} is already on the asphalt road in the distance, driving straight.\nLIGHTING: Soft morning sun, natural dusty air."
                st.code(p_gemini, language="text")

            # 2. GROK ADEGAN A (Natural Passing Truck)
            with st.container(border=True):
                st.subheader("🎥 2. Adegan A: Tragedy (Natural Pass)")
                p_grok_a = f"[REQUIRED: USE MASTER IMAGE AS REFERENCE]\n\nSTATIC CAMERA. The {car_dna} in the distance drives past on the asphalt road at a normal speed. As it passes, it creates a natural gust of wind and dust. The 80% finished {masjid_dna} on the table wobbles and naturally topples over, crumbling into pieces. The character stops, looking at the mess with deep sadness. Cinematic and natural."
                st.code(p_grok_a, language="text")

            # 3. GROK ADEGAN B (Close-up & Dialogue)
            with st.container(border=True):
                st.subheader("🎥 3. Adegan B: Plea (Interaction)")
                p_grok_b = f"[REQUIRED: USE MASTER IMAGE AS REFERENCE]\n\nSLOW CINEMATIC ZOOM to face. Character turns head to look at camera lens. Eyes are watery and deeply sorrowful. Lips move speaking the dialog: '{user_dialog_v2}'. Shaky hands pleading. Heartbreaking tone.\nAUDIO: {audio_dna}"
                st.code(p_grok_b, language="text")

            # 4. GROK ADEGAN C (The Process)
            with st.container(border=True):
                st.subheader("🎥 4. Adegan C: Reconstruction (Pacing Natural)")
                p_grok_c = f"[REQUIRED: USE MASTER IMAGE AS REFERENCE]\n\nSTRICT CHARACTER CONSISTENCY. CLOSE-UP ON HANDS. A montage of rebuilding the {masjid_dna} from zero to 100%. Weathered hands placing every wood piece carefully. Natural speed of hand movements."
                st.code(p_grok_c, language="text")

            # 5. GROK ADEGAN D (The Ending)
            with st.container(border=True):
                st.subheader("🎥 5. Adegan D: Final Success (Mengangkat Masjid)")
                p_grok_d = f"[REQUIRED: USE MASTER IMAGE AS REFERENCE]\n\n{DNA_LOCK_V8}\n\nACTION: Character GENTLY LIFTS the 100% finished {masjid_dna} from the table with both hands, showing it to the camera with a thin, peaceful smile of relief and gratitude. Heartwarming cinematic ending."
                st.code(p_grok_d, language="text")
                
    # ==========================================================================
    # TAB 3: ROBLOX
    # ==========================================================================
    with t_roblox:
        st.status("Sedang proses pembuatan...", expanded=False)

    # ==========================================================================
    # TAB 4: MINECRAFT
    # ==========================================================================
    with t_minecraft:
        st.status("Sedang proses pembuatan...", expanded=False)

    # ==========================================================================
    # TAB 5: RANDOM
    # ==========================================================================
    with t_random:
        st.status("Sedang proses pembuatan...", expanded=False)
