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
            "Nenek Aminah": (
                "IDENTITY: Extremely frail 92-year-old Javanese grandmother. "
                "FACE: Extremely thin delicate facial structure with very deep dense wrinkles, heavy sagging skin, prominent dark liver spots, and dry parchment-like texture. "
                "EYES: Deeply sunken dull weary 'sayu' gaze with heavy drooping eyelids showing extreme fatigue. "
                "BODY: Very fragile shrunken frame, slightly trembling posture, visible bone structure under thin skin. "
                "MOUTH: Thin relaxed lips with noticeable micro-tremor and age-related sagging during slow speech."
            ),
            "Nenek Siti": (
                "IDENTITY: Extremely frail 93-year-old petite Javanese grandmother. "
                "FACE: Very small shrunken facial structure, pale translucent heavily sagging skin with deep natural folds and numerous age spots. "
                "EYES: Distant hollow eyes with heavy lids reflecting long solitude and extreme old age. "
                "BODY: Tiny delicate shrunken frame, very passive and humble elderly posture. "
                "MOUTH: Loose sagging mouth with realistic severe muscle laxity of extreme old age."
            ),
            "Nenek Marsi": (
                "IDENTITY: Extremely frail 94-year-old Javanese grandmother. "
                "FACE: Heavily shrunken facial structure, dry parchment-like skin with deep sunken cheeks and many prominent age spots. "
                "EYES: Heavy lowered eyelids, thick with fatigue and quiet acceptance of very advanced age. "
                "BODY: Passive extremely fragile bone structure, almost motionless shrunken elderly frame. "
                "MOUTH: Sagging corners with slow heavy natural speech movement."
            ),
            "Nenek Ponirah": (
                "IDENTITY: Extremely frail 91-year-old Javanese grandmother. "
                "FACE: Broad facial structure with heavily weathered sun-damaged skin, very deep furrowed wrinkles, and visible age spots. "
                "EYES: Calm but deeply hollow 'sayu' gaze with heavy neutral stare of extreme old age. "
                "BODY: Stable but very frail posture showing decades of hard labor and physical decline. "
                "MOUTH: Firm yet relaxed for dialogue, surrounded by deep nasolabial folds of advanced age."
            ),
            "Nenek Juminah": (
                "IDENTITY: Extremely frail 92-year-old very thin Javanese grandmother. "
                "FACE: Sharp prominent bone structure with highly detailed aged skin, deep grooves, and numerous liver spots. "
                "EYES: Low weary heavily tired lids showing quiet endurance of extreme old age. "
                "BODY: Minimal movement, slow controlled gestures with extremely fragile thin hands. "
                "MOUTH: Natural speech movement with realistic thinning and trembling of aged lips."
            ),
            "Nenek Sikem": (
                "IDENTITY: Extremely frail 94-year-old Javanese grandmother. "
                "FACE: Extremely small facial structure, dry deeply folded sagging skin with heavy natural wrinkles and age spots. "
                "EYES: Slow heavy lids showing very low emotional intensity and calm fatigue of advanced age. "
                "BODY: Extremely passive, grounded, and severely shrunken elderly frame. "
                "MOUTH: Fully functional for speech with natural lip movement and subtle tremor."
            ),
            "Nenek Dulah": (
                "IDENTITY: Extremely frail 90-year-old Sundanese grandmother. "
                "FACE: Soft rounded face with naturally sunken cheeks, realistic heavy aging folds, and subtle age spots. "
                "EYES: Deep-set almond eyes with calm tired gaze and hollow undereyes of extreme old age. "
                "BODY: Fragile gentle presence with subtle age-related instability and trembling. "
                "MOUTH: Neutral relaxed mouth showing natural severe muscle slackness."
            ),
            "Nenek Sartini": (
                "IDENTITY: Extremely frail 89-year-old Sundanese grandmother. "
                "FACE: Wider round face with visible heavy sagging skin, deep marionette lines, and loose aged texture. "
                "EYES: Tired eyes with heavy lids and calm blank expression of advanced old age. "
                "BODY: Stable but clearly elderly and frail posture. "
                "MOUTH: Neutral mouth position capturing realistic sagging of lower facial muscles."
            ),
            "Nenek Tinah": (
                "IDENTITY: Extremely frail 93-year-old thin Javanese grandmother. "
                "FACE: Fragile facial structure with severe deep natural aging wrinkles, deeply sunken hollow cheeks, and dry aged skin. "
                "EYES: Dull heavy eyes with low gaze and minimal facial reaction. "
                "BODY: Shrunken and very frail body structure showing extreme old age. "
                "MOUTH: Relaxed mouth for speech with natural thinning of the lips."
            ),
            "Nenek Wati": (
                "IDENTITY: Extremely frail 91-year-old small Sundanese grandmother. "
                "FACE: Small fragile face with thin bone structure, soft heavy sagging skin, and visible natural veins. "
                "EYES: Calm tired eyes with gentle melancholic lonely gaze of very old age. "
                "BODY: Small-framed, very delicate and still elderly posture. "
                "MOUTH: Neutral mouth for speaking with subtle trembling of the lower jaw."
            ),

            # === KAKEK ===
            "Kakek Marto": (
                "IDENTITY: Extremely frail 91-year-old Javanese grandfather. "
                "FACE: Elongated fragile facial structure with sunken temples, high forehead ridge, and very deep wisdom lines. "
                "EYES: Dull distant 'sayu' gaze with profound weary eyelids of advanced age. "
                "BODY: Lean fragile frame with quiet endurance and withdrawn posture. "
                "MOUTH: Relaxed jaw and lips with natural aged movement and subtle lip-thinning."
            ),
            "Kakek Somo": (
                "IDENTITY: Extremely frail 90-year-old Javanese grandfather. "
                "FACE: Rounded soft facial structure now heavily aged and exhausted with drooping eyelids and deep skin creases. "
                "EYES: Tired calm slightly empty gaze showing quiet passive fatigue of extreme old age. "
                "BODY: Small fragile frame with gentle slow-moving presence. "
                "MOUTH: Neutral relaxed mouth with natural muscle laxity."
            ),
            "Kakek Joyo": (
                "IDENTITY: Extremely frail 89-year-old Javanese grandfather. "
                "FACE: Square jaw structure with leathery sun-baked skin, very deep forehead furrows, and thick aged texture. "
                "EYES: Protective pensive 'sayu' gaze with significant emotional weight of old age. "
                "BODY: Once strong but now heavily burdened and frail posture with slow movements. "
                "MOUTH: Flexible jaw showing aged lip texture."
            ),
            "Kakek Hardi": (
                "IDENTITY: Extremely frail 93-year-old Javanese grandfather. "
                "FACE: Shrunken facial structure with thin parchment-like skin, hollow cheeks, and visible bone structure. "
                "EYES: Deeply tired soft distant gaze reflecting sincere but fading presence. "
                "BODY: Extremely fragile and thin frame with whisper-like movements. "
                "MOUTH: Relaxed mouth with paper-thin lips."
            ),
            "Kakek Sableng": (
                "IDENTITY: Extremely frail 90-year-old Javanese grandfather. "
                "FACE: Strong bony facial structure with heavy eye bags and deep fatigue lines across the face. "
                "EYES: Sharp but emotionally wounded 'sayu' gaze showing internal brokenness of old age. "
                "BODY: Stoic and emotionally restrained but clearly shrunken elderly frame. "
                "MOUTH: Natural jaw movement with subtle tension in aged lips."
            ),
            "Kakek Sinto": (
                "IDENTITY: Extremely frail 94-year-old Javanese grandfather. "
                "FACE: Deeply sunken skeletal facial structure with paper-thin translucent skin and heavy wrinkle density. "
                "EYES: Cloudy distant gaze with profound emotional depth and calm acceptance. "
                "BODY: Nearing silence, spiritually detached, extremely shrunken and delicate frame. "
                "MOUTH: Fully flexible lips showing natural sag of extreme old age."
            ),
            "Kakek Wiryo": (
                "IDENTITY: Extremely frail 88-year-old Javanese grandfather. "
                "FACE: Strong labor-worn facial structure with dark bronze sun-exposed skin, deep pores, and rough aged texture. "
                "EYES: Tired but steady 'nrimo' gaze showing decades of hard work. "
                "BODY: Hardworking stoic but now very frail and weathered posture. "
                "MOUTH: Relaxed jaw with natural speech articulation and aged lip texture."
            ),
            "Kakek Usman": (
                "IDENTITY: Extremely frail 89-year-old Indonesian grandfather. "
                "FACE: Deeply wrinkled face with emotional fatigue lines, sun-damaged skin texture, and thin white hair. "
                "EYES: Emotional heavy gaze with subtle moisture reflection and weary lids. "
                "BODY: Emotionally burdened but sincere and slow elderly posture. "
                "MOUTH: Natural lip sync with relaxed jaw showing realistic aged skin movement."
            )
        }
		# --- 2. MASTER WARDROBE (6 VARIAN PER KARAKTER - DAILY & NEAT HIJAB) ---
        MASTER_FAMILY_WARDROBE = {
            # --- KELOMPOK NENEK ---

            "Nenek Aminah": {
                "Daster Rayon Motif Floral Lembut": "Wearing a loose soft rayon daster with delicate muted floral pattern in faded sage green and cream tones. Lightweight breathable fabric with natural soft drape. Paired with a simple cream instant bergo hijab.",
                "Daster Kaos Motif Batik Parang": "Wearing an oversized cotton daster with subtle faded brown parang batik pattern. Soft and comfortable fabric. Paired with a light brown jersey hijab.",
                "Daster Polos Katun Harian": "Wearing a plain faded emerald green cotton daster with smooth texture and loose comfortable fit. Paired with a simple grey instant hijab.",
                "Kaos Lengan Panjang + Sarung Batik": "Wearing a loose long-sleeved soft beige cotton shirt paired with a classic brown batik sarong. Paired with a soft white instant hijab.",
                "Daster Kancing Depan Motif Geometris": "Wearing a front-button rayon daster in muted maroon with subtle geometric pattern. Lightweight and modest daily wear. Paired with a navy instant hijab.",
                "Daster Rayon Motif Daun": "Wearing a loose rayon daster with soft green leaf motif on a light base. Comfortable with natural fabric movement. Paired with a simple black bergo hijab."
            },

            "Nenek Siti": {
                "Daster Kaos Motif Bunga Kecil": "Wearing a soft cotton daster with tiny faded floral pattern in pastel colors. Lightweight and comfortable for daily use. Paired with a dusty pink instant hijab.",
                "Daster Rayon Motif Sogan": "Wearing a traditional Javanese rayon daster with faded soft brown Sogan batik pattern. Thin and gentle fabric drape. Paired with a cream bergo hijab.",
                "Daster Polos Katun": "Wearing a plain faded mint green cotton daster with loose comfortable fit. Paired with a simple white instant hijab.",
                "Kaos Lengan Panjang + Jarik": "Wearing a loose long-sleeved beige cotton shirt paired with a dark brown jarik cloth. Paired with a soft grey hijab.",
                "Daster Kancing Depan Motif Garis": "Wearing a front-button cotton daster with faded subtle stripe pattern. Lightweight daily wear. Paired with a navy instant hijab.",
                "Daster Rayon Motif Abstrak Lembut": "Wearing a loose rayon daster with soft faded abstract pattern in muted tones. Comfortable home outfit. Paired with a simple maroon hijab."
            },

            "Nenek Marsi": {
                "Daster Batik Lembut": "Wearing a thin soft batik rayon daster in muted brown and cream tones. Light fabric with natural drape. Paired with a simple white instant hijab.",
                "Kaos Panjang + Jarik": "Wearing a long sleeve soft cotton shirt paired with a simple batik jarik. Traditional modest home outfit. Paired with a grey hijab.",
                "Daster Polos Katun Tipis": "Wearing a plain soft pastel cotton daster with loose fit. Paired with a simple hijab.",
                "Tunik Katun Sederhana": "Wearing a loose cotton tunic in faded dusty rose tone. Comfortable and modest daily wear. Paired with a soft hijab.",
                "Daster Kancing Depan": "Wearing a front-button cotton daster in faded maroon. Simple and practical. Paired with a navy instant hijab.",
                "Daster Motif Geometris Lembut": "Wearing a loose rayon daster with subtle geometric pattern in muted colors. Paired with a simple black bergo hijab."
            },

            "Nenek Ponirah": {
                "Daster Kaos Motif Mega Mendung": "Wearing an oversized cotton daster with faded soft Mega Mendung pattern in muted navy and grey. Comfortable fabric with natural drape. Paired with a simple black jersey bergo hijab.",
                "Setelan Rumah Rayon": "Wearing a matching loose rayon top and pants in faded chocolate brown with subtle pattern. Modest and practical daily wear. Paired with a plain grey instant hijab.",
                "Daster Kancing Depan Motif Geometris": "Wearing a front-button cotton daster in dark maroon with faded geometric pattern. Lightweight daily outfit. Paired with a simple white hijab.",
                "Tunik Katun + Jarik": "Wearing a modest long-sleeved tunic in faded sky blue paired with a dark brown batik jarik. Paired with a simple navy hijab.",
                "Daster Rayon Motif Daun": "Wearing a loose rayon daster with large faded green leaf pattern. Comfortable home wear. Paired with a simple black instant hijab.",
                "Kaos Polo Lengan Panjang + Sarung": "Wearing a modest long-sleeved cotton polo in faded forest green paired with a dark batik sarong. Paired with a simple white hijab."
            },

            "Nenek Juminah": {
                "Daster Rayon Motif Floral": "Wearing a loose rayon daster with soft faded floral pattern in muted navy tones. Lightweight and comfortable. Paired with a simple grey jersey bergo hijab.",
                "Kaos Lengan Panjang + Sarung": "Wearing a loose long-sleeved beige cotton shirt paired with a dark batik sarong. Simple daily home outfit. Paired with a white instant hijab.",
                "Daster Kaos Polos": "Wearing a plain faded maroon cotton daster with loose fit. Paired with a plain grey cotton hijab.",
                "Daster Kancing Depan Motif Garis": "Wearing a front-button cotton daster with faded vertical stripes. Lightweight daily wear. Paired with a navy instant hijab.",
                "Tunik Katun Sederhana": "Wearing a loose cotton tunic in faded dusty rose. Modest and comfortable. Paired with a soft white hijab.",
                "Daster Rayon Motif Abstrak": "Wearing a loose rayon daster with soft faded abstract pattern. Paired with a simple black bergo hijab."
            },

            "Nenek Sikem": {
                "Daster Kaos Motif Bunga Kecil": "Wearing a soft cotton daster with tiny faded floral pattern in muted blue tones. Lightweight daily wear. Paired with a simple black jersey bergo hijab.",
                "Daster Polos Katun": "Wearing a plain faded green cotton daster with loose comfortable fit. Paired with a simple grey hijab.",
                "Kaos Lengan Panjang + Jarik": "Wearing a loose long-sleeved beige cotton shirt paired with a dark batik jarik. Paired with a soft grey hijab.",
                "Daster Kancing Depan": "Wearing a front-button cotton daster in faded navy. Simple and practical. Paired with a white instant hijab.",
                "Daster Rayon Motif Daun": "Wearing a loose rayon daster with soft green leaf motif. Comfortable home wear. Paired with a simple maroon hijab.",
                "Daster Motif Geometris Lembut": "Wearing a loose rayon daster with subtle geometric pattern in muted tones. Paired with a simple black bergo hijab."
            },

            "Nenek Dulah": {
                "Daster Kaos Motif Bunga Kecil": "Wearing a short-sleeved cotton jersey daster in faded mint green with small floral patterns. Comfortable daily wear. Paired with a simple grey jersey instant hijab.",
                "Daster Rayon Motif Sogan": "Wearing a traditional Javanese rayon daster with faded soft brown Sogan pattern. Paired with a simple black bergo hijab.",
                "Kaos Lengan Panjang + Sarung": "Wearing a loose long-sleeved beige cotton shirt paired with a dark batik sarong. Paired with a simple white instant hijab.",
                "Daster Kancing Depan Motif Abstrak": "Wearing a front-button cotton daster in faded purple with subtle abstract pattern. Paired with a navy instant hijab.",
                "Daster Kaos Garis Halus": "Wearing a striped cotton jersey daster in faded blue and white. Loose comfortable fit. Paired with a simple maroon instant hijab.",
                "Daster Rayon Motif Daun": "Wearing a loose rayon daster with soft green leaf motif. Paired with a simple grey hijab."
            },

            "Nenek Sartini": {
                "Daster Rayon Motif Bunga Matahari": "Wearing a loose rayon daster in faded yellow with soft sunflower prints. Comfortable home dress. Paired with a simple grey jersey bergo hijab.",
                "Daster Kaos Motif Batik Pesisiran": "Wearing a short-sleeved cotton daster with faded red coastal batik pattern. Paired with a simple black instant hijab.",
                "Kaos Lengan Panjang + Sarung": "Wearing a plain long-sleeved cotton t-shirt in faded white paired with a dark batik sarong. Paired with a simple navy instant hijab.",
                "Daster Kancing Depan Motif Geometris": "Wearing a front-button cotton daster in faded emerald green with subtle geometric pattern. Paired with a white instant hijab.",
                "Daster Kaos Polos": "Wearing an oversized plain cotton daster in faded maroon. Comfortable daily wear. Paired with a grey simple hijab.",
                "Daster Rayon Motif Batik Cap": "Wearing a loose rayon daster with faded dark batik cap pattern. Paired with a simple dark brown instant hijab."
            },

            "Nenek Tinah": {
                "Daster Kaos Motif Floral Lembut": "Wearing an oversized cotton daster in faded blue with soft floral print. Comfortable daily wear. Paired with a simple black bergo hijab.",
                "Daster Rayon Motif Daun": "Wearing a loose rayon daster in faded green with large leaf pattern. Paired with a grey instant hijab.",
                "Kaos Lengan Panjang Polos": "Wearing a plain faded yellow long-sleeved cotton shirt paired with a dark batik sarong. Paired with a white instant hijab.",
                "Daster Kancing Depan Garis": "Wearing a front-button cotton daster with faded striped pattern. Paired with a navy instant hijab.",
                "Daster Kaos Polos": "Wearing an oversized plain cotton daster in faded orange. Simple daily home wear. Paired with a maroon instant hijab.",
                "Daster Rayon Motif Abstrak": "Wearing a loose rayon daster with faded soft abstract pattern. Paired with a dark brown instant hijab."
            },

            "Nenek Wati": {
                "Daster Kaos Motif Batik Parang": "Wearing an oversized cotton daster with faded parang batik pattern. Soft and comfortable. Paired with a black instant bergo hijab.",
                "Kaos Lengan Panjang Polos": "Wearing a plain faded red long-sleeved cotton shirt paired with a dark batik sarong. Paired with a white hijab.",
                "Daster Rayon Motif Kembang": "Wearing a loose rayon daster with faded flower pattern. Paired with a grey instant hijab.",
                "Daster Kancing Depan Kotak": "Wearing a front-button cotton daster with small faded checkered pattern. Paired with a navy hijab.",
                "Daster Kaos Polos": "Wearing a plain oversized cotton daster in faded mustard yellow. Simple home clothing. Paired with a maroon instant hijab.",
                "Daster Rayon Motif Batik Lembut": "Wearing a loose rayon daster with faded soft batik pattern. Paired with a dark brown instant hijab."
            },
            
            # --- KELOMPOK KAKEK ---
            "Kakek Marto": {
                "Baju Koko Katun Lembut": "Wearing a simple short-sleeved light brown cotton koko shirt with soft texture and natural drape from daily use. Paired with a classic checkered batik sarong in faded brown tones and a simple black velvet peci.",
                "Baju Koko Putih Polos": "Wearing a clean white short-sleeved cotton koko shirt with slight natural wrinkles. Paired with a dark brown batik sarong and a white peci haji.",
                "Baju Koko Batik Faded": "Wearing a short-sleeved faded earthy batik koko shirt with soft worn texture. Paired with a navy batik sarong and a simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a soft faded green short-sleeved polo shirt with comfortable fit. Paired with a maroon checkered batik sarong and a simple white knitted peci.",
                "Kemeja Flanel Kotak & Sarung": "Wearing a faded blue-grey flannel shirt over a thin white undershirt. Paired with a dark green batik sarong and black velvet peci.",
                "Baju Koko Abu & Sarung Lawas": "Wearing a simple short-sleeved faded grey cotton koko shirt. Paired with a traditional faded batik sarong and a black peci."
            },
            "Kakek Somo": {
                "Baju Koko Katun Polos": "Wearing a soft faded beige short-sleeved cotton koko shirt with natural drape. Paired with a brown batik sarong and simple white peci.",
                "Baju Koko Batik Lembut": "Wearing a short-sleeved faded soft brown batik koko shirt. Paired with a checkered batik sarong and white peci haji.",
                "Baju Koko Biru Muda": "Wearing a simple short-sleeved light blue cotton koko shirt. Paired with a dark maroon batik sarong and black velvet peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded orange short-sleeved polo shirt with comfortable collar. Paired with a dark green batik sarong and black peci.",
                "Kemeja Kotak & Sarung": "Wearing a faded blue checkered short-sleeved shirt. Paired with a maroon batik sarong and white peci haji.",
                "Baju Koko Abu & Sarung": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and simple black peci."
            },
            "Kakek Joyo": {
                "Baju Koko Katun Tebal": "Wearing a short-sleeved light brown cotton koko shirt with soft texture. Paired with a checkered batik sarong and black velvet peci.",
                "Baju Koko Putih Lawas": "Wearing a clean white short-sleeved cotton koko shirt with slight natural wrinkles. Paired with a dark batik sarong and white peci haji.",
                "Baju Koko Batik Faded": "Wearing a short-sleeved faded earthy tone batik koko shirt. Paired with a navy batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded green short-sleeved polo shirt. Paired with a maroon checkered batik sarong and white knitted peci.",
                "Kemeja Flanel & Sarung": "Wearing a faded blue-grey flannel shirt. Paired with a dark green batik sarong and black peci.",
                "Baju Koko Abu & Sarung Lawas": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional faded batik sarong and black peci."
            },
            "Kakek Hardi": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved faded beige cotton koko shirt with soft texture. Paired with a dark batik sarong and white peci haji.",
                "Baju Koko Biru Muda": "Wearing a short-sleeved light blue cotton koko shirt. Paired with a maroon batik sarong and black velvet peci.",
                "Baju Koko Batik Lembut": "Wearing a faded soft brown batik koko shirt with natural drape. Paired with a checkered batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded navy polo shirt with comfortable fit. Paired with a dark green batik sarong and white peci.",
                "Kemeja Kotak & Sarung": "Wearing a faded blue checkered shirt. Paired with a maroon batik sarong and black peci.",
                "Baju Koko Abu & Sarung": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and white peci haji."
            },
            "Kakek Sableng": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved light brown cotton koko shirt with soft texture. Paired with a dark batik sarong and black velvet peci.",
                "Baju Koko Putih Lawas": "Wearing a clean white short-sleeved cotton koko shirt. Paired with a maroon batik sarong and white peci haji.",
                "Baju Koko Batik Faded": "Wearing a faded earthy batik koko shirt with soft worn texture. Paired with a checkered batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded green polo shirt. Paired with a dark green batik sarong and white knitted peci.",
                "Kemeja Flanel & Sarung": "Wearing a faded blue-grey flannel shirt. Paired with a navy batik sarong and black peci.",
                "Baju Koko Abu & Sarung Lawas": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and black peci."
            },
            "Kakek Sinto": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved faded beige cotton koko shirt. Paired with a dark batik sarong and white peci haji.",
                "Baju Koko Biru Muda": "Wearing a short-sleeved light blue cotton koko shirt. Paired with a maroon batik sarong and black velvet peci.",
                "Baju Koko Batik Lembut": "Wearing a faded soft brown batik koko shirt. Paired with a checkered batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded navy polo shirt. Paired with a dark green batik sarong and white peci.",
                "Kemeja Kotak & Sarung": "Wearing a faded blue checkered shirt. Paired with a maroon batik sarong and black peci.",
                "Baju Koko Abu & Sarung": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and white peci haji."
            },
            "Kakek Wiryo": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved faded beige cotton koko shirt with soft texture. Paired with a dark batik sarong and black peci.",
                "Baju Koko Putih Lawas": "Wearing a clean white short-sleeved cotton koko shirt. Paired with a maroon batik sarong and white peci haji.",
                "Baju Koko Batik Faded": "Wearing a faded earthy batik koko shirt. Paired with a checkered batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded green polo shirt. Paired with a dark green batik sarong and white knitted peci.",
                "Kemeja Flanel & Sarung": "Wearing a faded blue-grey flannel shirt. Paired with a navy batik sarong and black peci.",
                "Baju Koko Abu & Sarung Lawas": "Wearing a simple faded grey cotton koko shirt. Paired with a traditional batik sarong and black peci."
            },
            "Kakek Usman": {
                "Baju Koko Katun Polos": "Wearing a simple short-sleeved faded beige cotton koko shirt. Paired with a dark batik sarong and white peci haji.",
                "Baju Koko Biru Muda": "Wearing a short-sleeved light blue cotton koko shirt. Paired with a maroon batik sarong and black velvet peci.",
                "Baju Koko Batik Lembut": "Wearing a faded soft brown batik koko shirt. Paired with a checkered batik sarong and simple black peci.",
                "Kaos Polo Lembut & Sarung": "Wearing a faded navy polo shirt. Paired with a dark green batik sarong and white peci.",
                "Kemeja Kotak & Sarung": "Wearing a faded blue checkered shirt. Paired with a maroon batik sarong and black peci.",
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

        MASTER_GRANDMA_SETTING = {
            "Kebun Semangka: Pasca Hujan": (
                "The character is seated on a low weathered wooden crate behind the workspace, nestled within a sprawling, unkempt Indonesian watermelon farm after a rain shower. "
                "Background: The landscape is defined by dark, rich, damp brown mud with visible puddles in the tire tracks and furrow lines. "
                "Colossal watermelons rest directly on the muddy earth, some covered in fine wet soil. The tangled green vines are lush and glistening with natural rainwater, sprawling unevenly across the field with realistic, sparse density and patches of wild weeds. "
                "Atmosphere: Authentic rural tropical environment. Surrounding objects: A stack of empty, weathered plastic fruit crates and a discarded blue tarpaulin sheet near the drainage ditch. Natural daylight reflects off the wet surfaces, creating a moist, fresh ambiance."
            ),

            "Kebun Semangka: Gubuk Panen": (
                "The character is seated on a simple weathered wooden bench behind the workspace, set next to a rustic, temporary harvest shed at the edge of the watermelon field. "
                "Background: A tumble-down lean-to structure made of bamboo and tattered tarpaulin. The farm floor is dry, greyish-brown soil with sparse, wild watermelon vines sprawling unevenly. "
                "Colossal watermelons are scattered naturally, some partially buried in the dirt and others tangled under thin, dry-green vines. Clutter: A high pile of newly harvested watermelons stacked messily under the shed's shade, a couple of old jute sacks, and a rustic wooden handcart parked nearby. "
                "Lighting: Warm, side golden hour daylight highlighting the textures of raw bamboo, burlap, and dusty fruit. Zero artificial elements or manicured rows."
            ),

            "Kebun Semangka: Tepian Sungai": (
                "The character is seated on a large flat river stone or low wooden crate behind the workspace, by a muddy path at the edge of a watermelon farm that borders a wide, slow-moving tropical river. "
                "Background: Dense, lush bamboo thickets and tattered banana leaves lining the riverbank in the distant background. "
                "The farm floor is a sandy-brown soil mixed with river stones. Colossal watermelons are nestled naturally among loose, wild green vines and tall river weeds. Realistic clutter: A rustic wooden canoe partially visible moored to a post in the river and a pile of river rocks and old fishing nets near the garden edge. "
                "The setting captures the wild, unkempt nature of a rural Indonesian riverside garden under natural daylight. No whole watermelons or tools on the table."
            ),
            "Kebun Semangka: Panen": (
                "The character is seated on a simple weathered wooden crate behind the workspace, in an authentic Indonesian watermelon field during harvest. "
                "The expansive field shows dry greyish-brown soil with tangled, sparse green vines. "
                "Background activity: A few distant Indonesian farmers in conical hats are working; one is carrying a normal-sized watermelon, another is pushing a rustic wooden handcart filled with several standard harvested watermelons. "
                "The field is cluttered naturally with dry leaves and weeds. Far in the distance, a row of burlap sacks and a tattered blue tarpaulin are visible. "
                "Lighting: Warm, natural golden hour sunlight from the side, highlighting the dusty ground. No internal lighting in the background."
            ),

            "Kebun Semangka: Perawatan": (
                "The character is seated on a low wooden crate behind the workspace by a dusty red dirt path at the edge of a watermelon farm that borders a wide tropical garden. "
                "Background: Rows of monumental watermelons on dry, grey-brown soil. "
                "Background activity: A single distant Indonesian farm worker is walking slowly through the rows, wearing a faded pesticide backpack sprayer and a protective face cloth. A faint, real-world misty cloud of natural fertilizer is partially visible near the worker, catching the light. Realistic clutter: A rustic wooden handcart parked near the garden edge and a few river stones. "
                "Lighting: Natural daytime sunlight, highlighting the fuzzy vines and dusty ground. The structure's deeply recessed portals show the glistening ruby-red interior flesh under natural daylight. No internal lighting Mechanisms."
            ),

            "Kebun Melon: Tradisional": (
                "The character is seated on a low weathered wooden crate behind the workspace, in the middle of a traditional Indonesian melon field. "
                "Background: The ground is dry, sandy light-brown soil with patches of wild grass. "
                "Normal-sized melons with tan-netted rinds are scattered naturally on the ground, partially shaded by large, wide green leaves and sprawling vines. "
                "Authentic clutter: Several bamboo sticks (ajir) are leaning messily against each other, and an old plastic watering can is visible in the distant background. "
                "Lighting: Natural golden hour daylight, highlighting the rough netted texture of the melons and the dusty soil."
            ),

            "Kebun Melon: Sisa Panen": (
                "The character is seated on a simple weathered wooden stool behind the workspace. "
                "Background: An Indonesian melon field just after harvest. The field shows dry, cracked earth with mostly withered yellow-brown vines. "
                "A few rejected, small normal-sized melons are left scattered in the dirt. "
                "Realistic clutter: Piles of dry vines gathered in small heaps and a few discarded burlap sacks near a rustic bamboo fence in the distance. "
                "Atmosphere: A raw, quiet rural field under warm afternoon sunlight with deep natural shadows."
            ),

            "Kebun Melon: Penyiraman": (
                "The character is seated on a low wooden crate behind the workspace by a dusty path at the edge of a melon farm. "
                "Background: Rows of healthy melon plants with large green leaves. "
                "Background activity: A distant Indonesian farmer is seen carrying two buckets of water using a traditional wooden shoulder pole (pikulan). "
                "The ground is a mix of dry earth and damp dark patches from recent watering. Authentic clutter: A rustic wooden handcart parked near a small irrigation ditch. "
                "Lighting: Soft morning sunlight, highlighting the moisture on the leaves and the dusty ground texture."
            ),

            "Kebun Melon: Sortir Panen": (
                "The character is seated on a rustic bamboo bench behind the workspace, set at the edge of the field. "
                "Background activity: A few distant Indonesian workers are seen sorting normal-sized melons into several weathered plastic fruit crates on the ground. "
                "The farm floor is dry greyish-brown soil with scattered dry leaves and broken bamboo pieces. "
                "Realistic clutter: A stack of empty wooden crates and a discarded blue tarpaulin sheet visible in the far distance. "
                "Lighting: Warm, side golden hour daylight, creating an authentic rural harvest ambiance."
            ),

            "Kebun Melon: Pinggir Desa": (
                "The character is seated on a low wooden crate behind the workspace. "
                "Background: A small, unkempt melon garden bordering a village. Visible in the distant background are a few rustic wooden houses and tattered banana trees. "
                "The field is messy with wild vines, normal-sized netted melons, and patches of weeds on sandy soil. "
                "Authentic clutter: A stray chicken or two pecking at the ground in the far distance and an old bicycle leaned against a coconut tree. "
                "Atmosphere: A slow-paced, honest tropical village environment under natural daylight."
                
            ),
            "Kebun Jeruk: Rimbun": (
                "The character is seated on a low weathered wooden stool behind the workspace, inside a lush, slightly overgrown Indonesian orange orchard. "
                "Background: Rows of small, gnarled orange trees with dense dark-green foliage. Normal-sized bright orange fruits are hanging heavily from the branches, some nearly touching the ground. "
                "The ground is covered in a thick layer of dry brown leaves and fallen twigs on top of dark earth. "
                "Authentic clutter: A couple of old bamboo ladders (tangga bambu) leaning against a tree and a faded plastic bucket in the distance. "
                "Lighting: Dappled sunlight filtering through the leaves, creating a soft, natural forest-like ambiance."
            ),

            "Kebun Jeruk: Pemetikan": (
                "The character is seated on a low wooden crate behind the workspace in the middle of an orange grove. "
                "Background activity: A distant Indonesian farmer in a conical hat is standing on a short bamboo ladder, carefully picking normal-sized oranges into a colorful plastic crate perched on a branch. "
                "The orchard floor is dry earth with scattered fallen fruit. Realistic clutter: Several stacked plastic crates filled with oranges and a discarded burlap sack near the orchard edge. "
                "Lighting: Warm, side golden hour sunlight highlighting the porous texture of the orange rinds and the dusty air."
            ),

            "Kebun Jeruk: Tepian Jalan": (
                "The character is seated on a rustic wooden bench behind the workspace at the edge of an orange orchard. "
                "Background: The dense green trees form a natural wall, with vibrant oranges visible among the leaves. A dusty red dirt path runs alongside the orchard. "
                "Background activity: A distant old motorbike with two large rattan baskets (bronjong) on the back is parked under a tree. "
                "Atmosphere: Authentic rural village life. The ground is a mix of red soil, small stones, and dry leaves under clear natural daylight."
            ),

            "Kebun Jeruk: Perawatan": (
                "The character is seated on a simple weathered wooden crate behind the workspace. "
                "Background: Rows of orange trees with some yellowing leaves, showing a raw, unmanicured farm look. "
                "Background activity: A distant Indonesian worker is seen pruning branches with manual shears, wearing a faded long-sleeve shirt and a towel wrapped around the neck. "
                "Realistic clutter: A pile of pruned branches on the ground and an old rusted watering can near an irrigation pipe. "
                "Lighting: Natural daytime sunlight, highlighting the rough bark of the trees and the uneven soil."
            ),

            "Kebun Jeruk: Sortir": (
                "The character is seated on a low wooden stool behind the workspace under the shade of a large orange tree. "
                "Background activity: A few distant Indonesian women are sitting on the ground, sorting normal-sized oranges from a large pile into smaller bamboo baskets (besek) or plastic crates. "
                "The ground is hard-packed earth with scattered orange leaves. Clutter: A rustic wooden handcart and a few stray chickens pecking at the ground in the distance. "
                "Atmosphere: A busy but slow-paced harvest morning with natural lighting."
            ),

            "Kebun Naga: Rimbun": (
                "The character is seated on a simple weathered wooden stool behind the workspace, inside a lush, slightly overgrown Indonesian dragon fruit farm. "
                "Background: Rows of old, weathered concrete posts supporting heavy, tangled masses of sprawling green cactus-like dragon fruit vines. Normal-sized bright pink fruits with green scales are hanging messily from the branches, some nearly touching the ground. "
                "The ground is covered in a mix of dry earth, small stones, and patches of wild weeds. "
                "Authentic clutter: A couple of old bamboo sticks (ajir) leaning against a post and a faded plastic watering can in the distance. "
                "Lighting: Dappled sunlight filtering through the cacti-like vines, creating a raw, natural forest-like ambiance."
            ),

            "Kebun Naga: Pemetikan": (
                "The character is seated on a low wooden crate behind the workspace in the middle of a dragon fruit grove. "
                "Background activity: A distant Indonesian farmer in a conical hat is carefully picking normal-sized pink dragon fruits into a colorful plastic crate perched on a cart. "
                "The orchard floor is dry earth with scattered fallen leaves. Realistic clutter: Several stacked plastic crates filled with dragon fruits and a discarded burlap sack near the orchard edge. "
                "Lighting: Warm, side golden hour sunlight highlighting the rough texture of the vines and the dusty soil."
            ),

            "Kebun Naga: Tepian Jalan": (
                "The character is seated on a rustic wooden bench behind the workspace at the edge of a dragon fruit orchard. "
                "Background: The dense cacti-like vines form a unique textured wall, with vibrant pink fruits visible among the green. A dusty red dirt path runs alongside the orchard. "
                "Background activity: A distant old motorbike with two large rattan baskets (bronjong) on the back is parked under a palm tree. "
                "Atmosphere: Authentic rural village life. The ground is a mix of red soil, small stones, and dry leaves under clear natural daylight."
            ),

            "Kebun Naga: Perawatan": (
                "The character is seated on a simple weathered wooden crate behind the workspace. "
                "Background: Rows of dragon fruit trees on dry, grey-brown soil. "
                "Background activity: A single distant Indonesian farm worker is walking slowly through the field, wearing a faded pesticide backpack sprayer, with a faint natural mist catching the sunlight. "
                "Realistic clutter: A rustic wooden handcart parked near a dry irrigation pipe and scattered river stones on the dusty soil. "
                "Lighting: Natural daytime sunlight, highlighting the rough bark of the trees and the uneven soil."
            ),

            "Kebun Naga: Sortir": (
                "The character is seated on a low wooden stool behind the workspace under the shade of a large mango tree near the farm. "
                "Background activity: A few distant Indonesian women are sitting on the ground, sorting normal-sized dragon fruits from a large pile into smaller bamboo baskets (besek) or plastic crates. "
                "The ground is hard-packed earth with scattered orange leaves. Clutter: A rustic wooden handcart and a few stray chickens pecking at the ground in the distance. "
                "Atmosphere: A busy but slow-paced harvest morning with natural lighting."
            ),

            "Kebun Nanas: Tradisional": (
                "The character is seated on a low weathered wooden stool behind the workspace. "
                "Background: A vast field of low-growing pineapple plants with sharp-edged, spiky grey-green leaves. Normal-sized pineapples with rough yellow-brown skin are nestled in the center of the plants. "
                "The ground is dry, sandy grey soil with plenty of visible earth and scattered dry grass. "
                "Authentic clutter: A couple of old plastic crates stacked at the edge and a discarded burlap sack in the distance. "
                "Lighting: Harsh afternoon sun creating high contrast and highlighting the jagged textures."
            ),

            "Kebun Nanas: Panen": (
                "The character is seated on a low wooden crate behind the workspace. "
                "Background activity: Distant Indonesian farmers in thick long-sleeve shirts are manually picking normal-sized pineapples into large rattan baskets (bronjong). "
                "The field is messy with scattered dry leaf debris and dusty soil. "
                "Realistic clutter: A rustic wooden handcart parked nearby, overflowing with harvested fruit. "
                "Lighting: Warm golden hour sunlight making the yellow rinds pop against the grey-green foliage."
            ),

            "Kebun Nanas: Tepian": (
                "The character is seated on a rustic bamboo bench behind the workspace. "
                "Background: The spiky pineapple plants form a dense, jagged texture. A dusty red dirt path runs along the edge of the farm. "
                "Background activity: A distant old motorbike with large wooden crates on the back is parked under a nearby coconut tree. "
                "Atmosphere: Authentic rural tropical environment with a mix of red soil and dry leaves under clear daylight."
            ),

            "Kebun Nanas: Pemeliharaan": (
                "The character is seated on a weathered wooden crate. "
                "Background: Rows of pineapple plants with patches of wild weeds and dry brown leaves between them. "
                "Background activity: A distant worker is seen clearing weeds with a small manual sickle (arit), wearing a faded conical hat. "
                "Realistic clutter: A pile of cleared weeds and a discarded plastic bucket near a dry irrigation ditch. "
                "Lighting: Natural daytime sunlight highlighting the rough, sharp textures of the farm floor."
            ),

            "Kebun Nanas: Sortir": (
                "The character is seated on a low wooden stool under a simple bamboo lean-to. "
                "Background activity: Distant workers are sitting on the ground, sorting a pile of normal-sized pineapples into bamboo baskets (besek). "
                "The ground is hard-packed earth with scattered organic debris and dry leaves. "
                "Atmosphere: A busy but slow-paced morning in a rural village with natural, soft lighting."
            ),

            "Kebun Pepaya: Rimbun": (
                "The character is seated on a rustic bamboo bench behind the workspace. "
                "Background: Tall papaya trees with straight, ring-patterned trunks and a dense canopy of large, umbrella-like leaves. Clusters of normal-sized green and yellow papayas hang high. "
                "The ground is covered in large, dry, tattered papaya leaves and dark moist soil. "
                "Authentic clutter: A long bamboo pole with a net (galah) leaning against a tree and an old plastic bucket. "
                "Lighting: Soft, diffused sunlight filtering through the canopy."
            ),

            "Kebun Pepaya: Panen": (
                "The character is seated on a low weathered wooden crate. "
                "Background activity: A distant Indonesian worker is using a long bamboo pole (galah) to carefully reach and harvest a ripe papaya from a tall tree. "
                "The ground is a mix of red soil and scattered dry leaves. "
                "Realistic clutter: A rustic wooden handcart with a few harvested papayas and a pile of organic debris. "
                "Lighting: Clear natural daylight highlighting the unique texture of the tree trunks."
            ),

            "Kebun Pepaya: Tepi Desa": (
                "The character is seated on a low wooden stool. "
                "Background: A messy papaya grove bordering a village with a few rustic wooden houses and banana trees in the far distance. "
                "The field is unkempt with wild grass and fallen fruit on sandy-brown soil. "
                "Authentic clutter: A stray chicken or two in the far background and an old bicycle leaned against a tree. "
                "Atmosphere: A slow-paced, honest tropical village environment under natural daylight."
            ),

            "Kebun Pepaya: Sortir": (
                "The character is seated on a simple weathered wooden bench near the trees. "
                "Background activity: Distant workers are laying out normal-sized papayas on a bed of dry straw for sorting. "
                "The farm floor is hard-packed earth with scattered dry leaves and old newspapers. "
                "Realistic clutter: A stack of empty wooden fruit crates and a discarded blue tarpaulin in the far distance. "
                "Lighting: Warm, side golden hour sunlight."
            ),

            "Kebun Pepaya: Perawatan": (
                "The character is seated on a low wooden crate behind the workspace. "
                "Background activity: A distant farm worker is walking slowly through the trees, carrying a faded pesticide backpack sprayer with a faint natural mist. "
                "The ground is dusty grey earth with natural uneven textures and scattered river stones. "
                "Lighting: Natural daytime sunlight creating long shadows on the uneven soil. Zero giant fruits in the background."
            ),

            "Kebun Pisang: Rimbun": (
                "The character is seated on a rustic bamboo bench behind the workspace. "
                "Background: A dense grove of tall banana trees with massive, tattered green leaves. Large bunches of normal-sized green bananas are hanging from the trees. "
                "The ground is covered in a thick layer of large, dry, brown banana leaves and dark moist earth. "
                "Authentic clutter: A rustic wooden ladder leaning against a trunk and an old plastic bucket. "
                "Lighting: Soft, diffused sunlight filtering through the massive leaves."
            ),
            "Kebun Pisang: Panen": (
                "The character is seated on a low weathered wooden crate. "
                "Background activity: A distant Indonesian farmer is seen carrying a large bunch of normal-sized bananas on his shoulder. "
                "The ground is messy with organic debris and scattered stones. "
                "Realistic clutter: A pile of freshly cut banana hearts (jantung pisang) and a rustic wooden handcart parked nearby. "
                "Lighting: Warm golden hour sunlight highlighting the waxy texture of the leaves."
            ),
            "Kebun Pisang: Pembersihan": (
                "The character is seated on a low wooden stool. "
                "Background activity: A distant worker is seen pruning dry leaves with a long-handled sickle (arit). "
                "The field shows a mix of red soil and plenty of dry, curled brown leaves on the ground. "
                "Authentic clutter: A stack of dried banana leaves gathered for wrapping and an old bicycle in the distance. "
                "Lighting: Natural daytime sunlight with realistic shadows."
            ),
            "Kebun Pisang: Tepi Desa": (
                "The character is seated on a simple weathered stool. "
                "Background: A wild banana grove bordering a village with a few rustic wooden houses visible far behind the trees. "
                "The floor is hard-packed earth with wild weeds and fallen debris. "
                "Realistic clutter: A stray chicken pecking near the trees and a discarded burlap sack. "
                "Atmosphere: A quiet, slow-paced tropical village morning."
            ),
            "Kebun Pisang: Sortir": (
                "The character is seated on a weathered bench. "
                "Background activity: Distant workers are laying out bunches of normal-sized bananas on a bed of dry leaves for sorting. "
                "The ground is dusty grey earth with scattered organic clutter. "
                "Realistic clutter: A few empty wooden crates and a tattered blue tarpaulin sheet. "
                "Lighting: Warm, side golden hour sunlight."
            ),

            "Kebun Anggur: Para-Para": (
                "The character is seated on a low wooden crate. "
                "Background: A traditional Indonesian vineyard with low-hanging grapevines supported by a rustic bamboo overhead trellis (para-para). Normal-sized bunches of grapes hang down from the vines. "
                "The floor is dry, sandy soil with patches of wild grass. "
                "Authentic clutter: Several bamboo poles supporting the structure and an old watering can. "
                "Lighting: Dappled sunlight filtering through the overhead leaves and grape clusters."
            ),
            "Kebun Anggur: Panen": (
                "The character is seated on a simple weathered stool. "
                "Background activity: A distant farmer in a conical hat is carefully clipping normal-sized grape bunches into a small bamboo basket (besek). "
                "The ground is dusty with scattered dry leaves. "
                "Realistic clutter: A stack of bamboo baskets and a discarded burlap sack. "
                "Lighting: Warm golden hour daylight highlighting the translucent fruit."
            ),
            "Kebun Anggur: Perawatan": (
                "The character is seated on a weathered wooden crate. "
                "Background activity: A distant worker is seen tying young vines to the bamboo trellis. "
                "The ground is a mix of grey earth and small river stones. "
                "Authentic clutter: A coil of raffia string and a pair of manual shears on a nearby post. "
                "Lighting: Natural daytime sunlight."
            ),
            "Kebun Anggur: Sortir": (
                "The character is seated on a rustic bamboo bench. "
                "Background activity: Distant workers are sitting on low stools, sorting grapes into small plastic containers. "
                "The floor is hard-packed earth with scattered dry leaves and organic clutter. "
                "Realistic clutter: A rustic wooden handcart and an old blue plastic bucket. "
                "Lighting: Soft natural light under the shade of the vines."
            ),
            "Kebun Anggur: Tepi Kebun": (
                "The character is seated on a low wooden stool. "
                "Background: The edge of the vineyard where the bamboo trellis meets a row of banana trees. "
                "The ground is a mix of red soil and dry grass. "
                "Authentic clutter: An old motorbike with rattan baskets (bronjong) parked nearby. "
                "Atmosphere: Authentic rural farming environment under clear daylight."
            ),

            "Kebun Pepaya: Rimbun": (
                "The character is seated on a rustic bamboo bench. "
                "Background: Tall papaya trees with ring-patterned trunks and a canopy of large, umbrella-like leaves. Normal-sized papayas are clustered at the top. "
                "The ground is covered in large, dry, tattered papaya leaves and dark moist soil. "
                "Authentic clutter: A long bamboo pole with a net (galah) leaning against a tree. "
                "Lighting: Soft, diffused sunlight filtering through the canopy."
            ),
            "Kebun Pepaya: Panen Galah": (
                "The character is seated on a low weathered wooden crate. "
                "Background activity: A distant worker is using a long bamboo pole (galah) to harvest a ripe papaya. "
                "The ground is a mix of red soil and scattered dry leaves. "
                "Realistic clutter: A rustic wooden handcart with a few harvested fruits. "
                "Lighting: Clear natural daylight highlighting the tree bark texture."
            ),
            "Kebun Pepaya: Tepi Desa": (
                "The character is seated on a low wooden stool. "
                "Background: A messy papaya grove bordering a village with rustic houses in the distance. "
                "The field is unkempt with wild grass and fallen fruit on sandy-brown soil. "
                "Authentic clutter: A stray chicken in the far background and an old bicycle. "
                "Atmosphere: A slow-paced tropical village environment."
            ),
            "Kebun Pepaya: Sortir": (
                "The character is seated on a simple weathered bench. "
                "Background activity: Distant workers are laying out normal-sized papayas on a bed of dry straw for sorting. "
                "The floor is hard-packed earth with scattered dry leaves and old newspapers. "
                "Realistic clutter: A stack of empty wooden fruit crates and a discarded blue tarpaulin. "
                "Lighting: Warm, side golden hour sunlight."
            ),
            "Kebun Pepaya: Perawatan": (
                "The character is seated on a low wooden crate. "
                "Background activity: A distant farm worker is walking slowly through the trees with a pesticide backpack sprayer. "
                "The ground is dusty grey earth with natural uneven textures and scattered stones. "
                "Lighting: Natural daytime sunlight with long shadows."
            ),

            "Kebun Strawberry: Bedengan": (
                "The character is seated on a low weathered wooden stool behind the workspace. "
                "Background: An Indonesian highland strawberry farm with long, raised soil beds covered in weathered silver-black plastic mulch. Small, lush green strawberry plants grow from holes in the mulch. "
                "Normal-sized bright red strawberries are visible hanging near the soil. The paths between beds are dusty grey earth with scattered dry leaves. "
                "Authentic clutter: An old plastic watering can and a few bamboo sticks. "
                "Lighting: Clear, cool highland morning sunlight with soft shadows."
            ),
            "Kebun Strawberry: Panen": (
                "The character is seated on a low wooden crate. "
                "Background activity: Distant farmers in sweaters and conical hats are squatting, carefully picking strawberries into small plastic baskets. "
                "The ground is a mix of dry earth and small stones. "
                "Realistic clutter: A stack of small transparent plastic containers and a discarded burlap sack in the distance. "
                "Lighting: Warm side golden hour light highlighting the seeds on the fruit's surface."
            ),
            "Kebun Strawberry: Terasering": (
                "The character is seated on a rustic wooden bench. "
                "Background: A terraced strawberry garden on a hillside with distant misty mountains visible. "
                "The beds are messy with wild runners and weeds growing between the mulch. "
                "Authentic clutter: A rustic bamboo fence at the edge of the terrace and a stray chicken in the far distance. "
                "Atmosphere: Fresh, airy highland village environment under natural daylight."
            ),
            "Kebun Strawberry: Sortir": (
                "The character is seated on a weathered stool. "
                "Background activity: Distant workers are sitting under a small bamboo shack, sorting strawberries from large buckets into small baskets. "
                "The floor is hard-packed earth with organic debris and old newspapers. "
                "Realistic clutter: A rustic wooden handcart and a tattered blue tarpaulin sheet. "
                "Lighting: Soft, diffused natural light under the shade."
            ),
            "Kebun Strawberry: Perawatan": (
                "The character is seated on a low wooden crate. "
                "Background activity: A distant worker is seen spraying organic fertilizer with a manual backpack sprayer, creating a faint mist in the sunlight. "
                "The ground is dusty with natural uneven textures. "
                "Authentic clutter: A pile of pulled weeds and a pair of garden shears on a wooden post. "
                "Lighting: Bright natural daylight highlighting the vibrant green leaves."
            ),

            "Kebun Salak: Rimbun Duri": (
                "The character is seated on a rustic bamboo bench. "
                "Background: A dense, shadowy grove of snake fruit (Salak) trees with extremely sharp, thorny fronds arching over the workspace. "
                "Clusters of normal-sized brown scaly fruits are growing near the base of the thorny trunks. "
                "The ground is a thick carpet of dry, thorny brown fronds and dark moist soil. "
                "Authentic clutter: A long bamboo pole and an old plastic bucket. "
                "Lighting: Darker, atmospheric dappled sunlight filtering through the dense thorny canopy."
            ),
            "Kebun Salak: Panen Arit": (
                "The character is seated on a low weathered wooden crate. "
                "Background activity: A distant farmer is seen using a small sickle (arit) to carefully cut a cluster of salak, wearing thick protective gloves. "
                "The ground is messy with dry, sharp organic debris. "
                "Realistic clutter: A large rattan basket (bronjong) half-filled with scaly brown fruit. "
                "Lighting: Warm afternoon light highlighting the snake-like skin texture of the fruit."
            ),
            "Kebun Salak: Pembersihan": (
                "The character is seated on a low wooden stool. "
                "Background activity: A distant worker is seen clearing dry, thorny fronds into a pile. "
                "The floor is dark earth mixed with grey volcanic ash and dry leaves. "
                "Authentic clutter: A smoldering small pile of leaves with faint smoke in the far distance and an old bicycle. "
                "Lighting: Natural daytime sunlight with deep, high-contrast shadows."
            ),
            "Kebun Salak: Sortir": (
                "The character is seated on a weathered wooden bench. "
                "Background activity: Distant workers are sorting salak by hand, rubbing the scales to clean them before packing into bamboo baskets. "
                "The ground is hard-packed earth with scattered dry thorns and leaves. "
                "Realistic clutter: A pile of rejected small fruits and several empty bamboo besek. "
                "Lighting: Side golden hour sunlight."
            ),
            "Kebun Salak: Tepi Dusun": (
                "The character is seated on a low wooden stool. "
                "Background: The edge of a salak plantation bordering a rustic village house made of wood and brick. "
                "The ground is a mix of red soil and dry organic clutter. "
                "Authentic clutter: A stray dog resting in the shade of the thorns and an old motorbike parked nearby. "
                "Atmosphere: Quiet, honest rural Indonesian village life."
            ),

            "Kebun Apel: Rimbun": (
                "The character is seated on a low weathered stool. "
                "Background: A lush Indonesian apple orchard with short, gnarled trees. Normal-sized red and green apples are hanging heavily from branches supported by bamboo sticks. "
                "The ground is covered in dry grass and fallen leaves on dark soil. "
                "Authentic clutter: A bamboo ladder leaning against a tree and an old plastic bucket. "
                "Lighting: Soft morning sunlight filtering through the orchard canopy."
            ),
            "Kebun Apel: Panen": (
                "The character is seated on a low wooden crate. "
                "Background activity: A distant farmer is standing on a short wooden ladder, picking apples into a cloth bag. "
                "The orchard floor is dry earth with scattered fallen fruit. "
                "Realistic clutter: Several wooden crates filled with apples and a discarded burlap sack. "
                "Lighting: Warm golden hour daylight highlighting the smooth skin of the apples."
            ),
            "Kebun Apel: Sortir": (
                "The character is seated on a rustic bamboo bench. "
                "Background activity: Distant workers are sitting on the ground, sorting apples by color and size into wooden boxes. "
                "The floor is hard-packed earth with scattered dry leaves and old newspapers. "
                "Realistic clutter: A rustic wooden handcart and a stack of empty crates. "
                "Lighting: Side natural light creating a warm harvest ambiance."
            ),
            "Kebun Apel: Pemangkasan": (
                "The character is seated on a simple weathered stool. "
                "Background activity: A distant worker is pruning the apple trees with shears, wearing a faded long-sleeve shirt. "
                "The ground shows a mix of soil and a pile of pruned branches. "
                "Authentic clutter: An old rusted watering can near an irrigation pipe. "
                "Lighting: Natural daytime sunlight with realistic shadows."
            ),
            "Kebun Apel: Tepi Bukit": (
                "The character is seated on a low wooden crate. "
                "Background: The orchard edge on a slope with a distant view of other orchards and village houses. "
                "The ground is a mix of red soil, stones, and wild grass. "
                "Authentic clutter: An old motorbike with rattan baskets parked nearby. "
                "Atmosphere: Authentic highland farming environment under clear daylight."
            ),

            "Kebun Cabe: Rimbun Merah": (
                "The character is seated on a low weathered wooden stool behind the workspace. "
                "Background: A lush, slightly messy Indonesian chili farm with low, bushy plants. Millions of normal-sized bright red and green chilies are hanging thickly from the branches. "
                "The ground is dry greyish-brown earth with scattered dry leaves and patches of wild weeds. "
                "Authentic clutter: A small plastic bucket for picking and a discarded burlap sack in the distance. "
                "Lighting: Bright natural daylight highlighting the waxy, reflective skin of the chilies."
            ),
            "Kebun Cabe: Panen": (
                "The character is seated on a low wooden crate. "
                "Background activity: A few distant Indonesian workers in conical hats are squatting between the rows, picking ripe chilies into small colorful plastic pails. "
                "The ground is dusty with natural uneven textures. "
                "Realistic clutter: A rustic wooden handcart parked at the edge of the field with several sacks of harvested chili. "
                "Lighting: Warm golden hour sunlight creating long shadows through the chili bushes."
            ),
            "Kebun Cabe: Pemeliharaan": (
                "The character is seated on a rustic bamboo bench. "
                "Background activity: A distant worker is seen spraying natural fertilizer with a manual backpack sprayer, a faint mist visible in the air. "
                "The field shows a mix of soil and bamboo sticks (ajir) used to support the heavy plants. "
                "Authentic clutter: An old watering can and a pile of pulled weeds. "
                "Lighting: Clear morning sunlight with a fresh, airy tropical farm atmosphere."
            ),
            "Kebun Cabe: Sortir": (
                "The character is seated on a weathered stool. "
                "Background activity: Distant workers are sitting on a tarpaulin on the ground, sorting red chilies into large bamboo baskets (besek). "
                "The floor is hard-packed earth with scattered organic debris. "
                "Realistic clutter: A stack of empty baskets and a tattered blue tarpaulin sheet near the irrigation ditch. "
                "Lighting: Soft natural light under the shade of a large tree nearby."
            ),
            "Kebun Cabe: Tepi Sawah": (
                "The character is seated on a low wooden crate. "
                "Background: The edge of a chili garden bordering a wide green rice field. A few coconut trees are visible in the far distance. "
                "The ground is a mix of red soil, stones, and dry grass. "
                "Authentic clutter: An old motorbike with rattan baskets parked under a tree. "
                "Atmosphere: Authentic rural farming environment under clear daylight."
            ),

            "Kebun Tomat: Rimbun": (
                "The character is seated on a low weathered stool. "
                "Background: Rows of tall, bushy tomato plants supported by a messy bamboo trellis (ajir). Normal-sized clusters of red and green tomatoes are visible among the fuzzy green leaves. "
                "The ground is dark, moist soil with scattered dry leaves. "
                "Authentic clutter: A long bamboo pole and a faded plastic bucket. "
                "Lighting: Dappled sunlight filtering through the trellis, highlighting the textured tomato stems."
            ),
            "Kebun Tomat: Panen": (
                "The character is seated on a low wooden crate. "
                "Background activity: Distant farmers are carefully picking ripe tomatoes and placing them into wooden fruit crates. "
                "The orchard floor is dry earth with scattered fallen fruit. "
                "Realistic clutter: Several stacked wooden crates filled with tomatoes and a discarded burlap sack. "
                "Lighting: Warm golden hour daylight highlighting the smooth, round fruit."
            ),
            "Kebun Tomat: Sortir": (
                "The character is seated on a rustic bamboo bench. "
                "Background activity: Distant workers are sitting on the ground, sorting tomatoes from a large pile into plastic crates based on ripeness. "
                "The floor is hard-packed earth with scattered dry leaves and old newspapers. "
                "Realistic clutter: A rustic wooden handcart and a stack of empty crates. "
                "Lighting: Side natural light creating a warm harvest ambiance."
            ),
            "Kebun Tomat: Pemangkasan": (
                "The character is seated on a simple weathered stool. "
                "Background activity: A distant worker is seen tying vines to bamboo sticks and pruning leaves with manual shears. "
                "The ground shows a mix of soil and a pile of pruned branches. "
                "Authentic clutter: An old rusted watering can near an irrigation pipe. "
                "Lighting: Natural daytime sunlight with realistic shadows."
            ),
            "Kebun Tomat: Tepi Desa": (
                "The character is seated on a low wooden crate. "
                "Background: A small tomato garden bordering a rustic village house with tattered banana trees in the background. "
                "The ground is a mix of red soil, stones, and wild grass. "
                "Authentic clutter: A stray chicken or two pecking at the ground in the distance. "
                "Atmosphere: Honest rural Indonesian village life."
            ),

            "Kebun Matahari: Rimbun": (
                "The character is seated on a low weathered wooden stool. "
                "Background: A dense field of tall, blooming sunflowers with thick green stalks and massive yellow flower heads. The flowers are facing the sun. "
                "The ground is dry, sandy light-brown soil with patches of wild grass. "
                "Authentic clutter: A couple of old bamboo sticks leaning against each other. "
                "Lighting: Bright, direct natural sunlight highlighting the vibrant yellow petals and the rough texture of the stalks."
            ),
            "Kebun Matahari: Panen Biji": (
                "The character is seated on a simple weathered stool. "
                "Background activity: Distant farmers are seen cutting large, dried sunflower heads that are heavy with black seeds. "
                "The ground is dusty with scattered dry leaves and petals. "
                "Realistic clutter: A stack of burlap sacks half-filled with dried sunflower heads. "
                "Lighting: Warm golden hour daylight highlighting the seeds in the center of the flowers."
            ),
            "Kebun Matahari: Perawatan": (
                "The character is seated on a weathered wooden crate. "
                "Background activity: A distant worker is seen clearing weeds between the tall stalks. "
                "The ground is a mix of grey earth and small river stones. "
                "Authentic clutter: A rustic wooden handcart and an old plastic watering can. "
                "Lighting: Natural daytime sunlight with long shadows."
            ),
            "Kebun Matahari: Sortir Biji": (
                "The character is seated on a rustic bamboo bench. "
                "Background activity: Distant workers are sitting on a tarpaulin, threshing dried sunflower heads to extract the seeds (kuaci). "
                "The floor is hard-packed earth with scattered dry flower debris and organic clutter. "
                "Realistic clutter: A few empty wooden fruit crates and a tattered blue tarpaulin. "
                "Lighting: Soft natural light under a simple bamboo lean-to."
            ),
            "Kebun Matahari: Tepi Bukit": (
                "The character is seated on a low wooden stool. "
                "Background: The edge of a sunflower field on a slope with a distant view of misty mountains and village houses. "
                "The ground is a mix of red soil and dry grass. "
                "Authentic clutter: An old motorbike parked under a nearby tree. "
                "Atmosphere: Authentic highland farming environment under clear daylight."
            ),

            "Kebun Sayur: Tumpang Sari": (
                "The character is seated on a low weathered wooden stool behind the workspace, in the middle of a vibrant Indonesian vegetable garden. "
                "Background: A mix of low-growing leafy greens like kangkung, spinach, and mustard greens (sawi) planted in several small, organic-shaped soil beds. "
                "The ground is dark, rich moist earth with narrow muddy paths between the beds. "
                "Authentic clutter: A couple of rustic bamboo watering poles and an old plastic bucket. "
                "Lighting: Soft, fresh morning sunlight highlighting the dew on the green leaves."
            ),

            "Kebun Sayur: Bersih Rumput": (
                "The character is seated on a low wooden crate behind the workspace. "
                "Background activity: A few distant Indonesian women in conical hats are squatting, manually pulling weeds from between rows of spring onions and cabbages. "
                "The ground is a mix of damp dark soil and piles of cleared green weeds. "
                "Realistic clutter: A small hand-hoe (cangkul kecil) leaning against a wooden post in the distance. "
                "Lighting: Bright natural daylight with soft shadows from nearby banana trees."
            ),

            "Kebun Sayur: Panen": (
                "The character is seated on a rustic bamboo bench behind the workspace. "
                "Background activity: A distant farmer is seen bundling fresh mustard greens (sawi) and placing them into a large bamboo basket (besek). "
                "The field floor is messy with discarded outer leaves and muddy footprints. "
                "Realistic clutter: Several overflowing bamboo baskets and a discarded burlap sack near the irrigation ditch. "
                "Lighting: Warm, side golden hour sunlight reflecting off the moist, leafy textures."
            ),

            "Kebun Sayur: Penyiraman": (
                "The character is seated on a simple weathered wooden crate. "
                "Background activity: A distant worker is walking through the rows, carefully watering the plants with a manual sprayer, creating a faint, natural watery mist. "
                "The ground shows a beautiful contrast between dry grey earth and dark, wet patches of watered soil. "
                "Authentic clutter: A rustic wooden handcart parked near a small water well in the background. "
                "Lighting: Natural daytime sunlight catching the mist in the air."
            ),

            "Kebun Sayur: Tepian Parit": (
                "The character is seated on a low wooden stool by a small, slow-flowing irrigation ditch at the edge of the vegetable garden. "
                "Background: Rows of chili plants and long beans (kacang panjang) on bamboo trellises bordering the field. "
                "The ground is a mix of red soil, river stones, and mossy patches near the water. "
                "Authentic clutter: A stray duck or two swimming in the ditch in the far distance and an old bicycle. "
                "Atmosphere: A peaceful, authentic rural Indonesian farming scene under clear daylight."
            ),

            "Sawah: Hijau Royo-Royo": (
                "The character is seated on a simple weathered wooden stool behind the workspace, overlooking a vast Indonesian rice field. "
                "Background: Rows of young, vibrant green rice stalks growing in flooded paddies. The water surface reflects the clear sky. "
                "The paths (pematang sawah) are narrow, made of hard-packed mud with patches of wild grass. "
                "Authentic clutter: A small wooden scarecrow (orang-orangan sawah) in the distance and a few coconut trees on the horizon. "
                "Lighting: Bright morning sunlight highlighting the lush, waxy texture of the rice leaves."
            ),

            "Sawah: Kuning Emas": (
                "The character is seated on a low weathered wooden crate behind the workspace. "
                "Background: An expansive field of mature, golden-yellow rice stalks swaying in the wind. "
                "Background activity: Distant Indonesian farmers in conical hats are actively cutting the rice with small sickles (ani-ani or arit). "
                "The ground is dry, dusty earth near the harvest area. Realistic clutter: A pile of harvested rice stalks and a few large burlap sacks (karung goni) stacked nearby. "
                "Lighting: Warm, golden hour sunlight, making the whole field glow with a rich amber hue."
            ),

            "Sawah: Bajak Lumpur": (
                "The character is seated on a rustic bamboo bench behind the workspace. "
                "Background: A flooded rice field being prepared for planting. The landscape is dominated by thick, dark-brown mud and glistening water. "
                "Background activity: A distant farmer is seen plowing the field with a traditional water buffalo (kerbau) or a small red tractor. "
                "The ground around the workspace is messy with damp mud and tire tracks. Authentic clutter: A rustic wooden handcart parked nearby. "
                "Atmosphere: A raw, honest rural farming scene with a moist, earthy ambiance under natural daylight."
            ),

            "Sawah: Tepian Irigasi": (
                "The character is seated on a low wooden stool by a small cement or stone irrigation canal at the edge of the rice field. "
                "Background: The field is a mix of green rice and muddy patches. A distant small wooden hut (gubuk sawah) is visible in the background. "
                "The floor is a mix of red soil, river stones, and mossy patches near the water flow. "
                "Authentic clutter: An old bicycle leaned against a coconut tree and a few ducks swimming in the canal in the far distance. "
                "Lighting: Clear natural daylight, highlighting the texture of the moving water and the muddy paths."
            ),

            "Sawah: Sisa Panen": (
                "The character is seated on a weathered wooden crate. "
                "Background: A dry rice field after harvest, showing short straw stubble and cracked earth. "
                "Background activity: Distant workers are seen threshing the rice manually (gebot) against a wooden board. "
                "The ground is dusty grey earth with scattered straw and organic debris. Realistic clutter: A discarded blue tarpaulin sheet used for drying grain and several empty baskets. "
                "Lighting: Soft, afternoon sunlight creating long shadows on the cracked soil."
            ),

            "Pinggir Jalan: Warung Tenda": (
                "The character is seated on a low wooden stool on the dusty shoulder of a village road. "
                "Background: Across the asphalt road, a row of traditional street food stalls (kaki lima) with colorful weathered tarpaulin tents. "
                "Background activity: Distant customers are sitting on long benches under the tents, and a seller is busy preparing food. A few motorbikes are parked haphazardly in front of the stalls. "
                "The ground around the character is dry grey earth with scattered gravel and a few dry leaves. "
                "Lighting: Warm late afternoon sunlight, creating a nostalgic, busy roadside atmosphere."
            ),

            "Pinggir Jalan: Pasar Tumpah": (
                "The character is seated on a weathered wooden crate on the edge of a bustling roadside. "
                "Background: Across the road is a vibrant morning market scene with many umbrella-shaded vendors selling snacks and traditional cakes (jajanan pasar). "
                "Background activity: A crowd of distant Indonesian villagers in casual wear are interacting, buying, and selling. A slow-moving old bicycle and a motorbike are passing through the narrow space. "
                "Authentic clutter: Scattered plastic waste and organic debris on the sun-baked soil near the drainage ditch. "
                "Atmosphere: High-energy, honest rural commerce under bright natural morning light."
            ),

            "Pinggir Jalan: Asap Sate/Ayam Bakar": (
                "The character is seated on a simple rustic bench on the roadside shoulder. "
                "Background: Directly across the street, a street food vendor is grilling food, with a faint, realistic cloud of white smoke drifting from the grill into the air. "
                "Background activity: People are standing in line waiting for their food. A bright yellow 'Sate' or 'Ayam Bakar' banner is partially visible in the distance. "
                "Lighting: Golden hour sunlight catching the drifting smoke, creating a cinematic, atmospheric hazy look. The road surface is aged, cracked asphalt."
            ),

            "Pinggir Jalan: Deretan Gerobak": (
                "The character is seated on a low cement step by the road. "
                "Background: Across the quiet street, three different traditional food carts (Gerobak Bakso and Gerobak Mie Ayam) are parked in a row under a large flamboyant tree. "
                "Background activity: A few kids are buying snacks, and the sellers are chatting. A stray cat is walking near the carts. "
                "The ground is a mix of mossy paving blocks and dry soil. Authentic clutter: A stack of empty wooden crates and a plastic bucket nearby. "
                "Lighting: Soft dappled sunlight filtering through the tree branches."
            ),

            "Pinggir Jalan: Pertigaan Ramai": (
                "The character is seated on a wooden crate near a village junction. "
                "Background: Across the road is a permanent wooden kiosk (warung kelontong) flanked by small food vendors. "
                "Background activity: Several motorbikes are passing by in the distance, and people are gathered at the kiosk talking. Some colorful snack sachets are hanging in the background warung. "
                "The ground is dusty red soil with scattered river stones. "
                "Atmosphere: Authentic, slow-paced but living rural Indonesian street scene under clear natural daylight."
            ),

            "Halaman Samping: Dapur Pawon": (
                "The character is seated on a low weathered wooden stool in the dirt yard just outside an open-air traditional kitchen (pawon). "
                "Background: A rustic stack of chopped firewood piled high against a soot-stained wooden wall. A faint, natural thin wisp of smoke drifts from a stone hearth inside the open doorway. "
                "Background activity: A distant family member is seen carrying a basket of vegetables or tending to a large clay pot. "
                "The floor is dark, ash-dusted earth with scattered wood shavings and dry twigs. "
                "Lighting: Warm, atmospheric golden hour light hitting the smoke and the rough wood textures."
            ),

            "Halaman Depan: Area Jemur Gabah": (
                "The character is seated on a wide rustic bamboo bench (lincak) in a large, open sun-baked yard. "
                "Background: A large blue tarpaulin is spread on the ground, covered with a thin layer of golden harvested rice grain (gabah) drying in the sun. "
                "Background activity: A distant worker or neighbor is using a wooden rake to spread the grain. Several stray chickens are pecking at the edges of the tarpaulin. "
                "The ground is hard-packed grey earth with natural cracks and scattered straw. "
                "Lighting: Bright, high-contrast midday sun, making the golden grain look vibrant and sharp."
            ),

            "Halaman Rumah: Sudut Kerajinan": (
                "The character is seated on a low wooden crate in a shaded corner of the yard filled with traditional farm tools. "
                "Background: A collection of long bamboo poles, a rustic wooden plow, and several large rattan baskets (bronjong) leaning against a fruit tree. "
                "Background activity: A distant neighbor is seen stopping by on an old bicycle to chat. "
                "The floor is a mix of red soil and patches of green moss near an old stone water well (sumur). "
                "Lighting: Soft dappled sunlight filtering through tree leaves, creating a calm, productive rural vibe."
            ),

            "Teras Rumah: Kayu Jati Tua": (
                "The character is seated on a low weathered wooden stool on the porch of a traditional Indonesian wooden house. "
                "Background: The wall is made of aged, dark teak wood panels with beautiful natural grain. A pair of old wooden chairs with a small round table sits in the corner. "
                "Background activity: A distant neighbor is seen walking past the house on a dusty path. A few bird cages (sangkar burung) hang from the wooden eaves. "
                "The floor is made of smooth, dark wooden planks with natural gaps. Authentic clutter: A pair of worn-out rubber sandals (sandal jepit) near the stairs. "
                "Lighting: Warm, soft natural light filtering through the porch roof, creating a cozy and nostalgic atmosphere."
            ),

            "Teras Rumah: Bata Merah & Motor": (
                "The character is seated on a wide rustic bamboo bench (lincak) on a porch with unfinished red-brick walls. "
                "Background: The weathered red-brick wall is partially covered in moss, with an old wooden door and a small window nearby. "
                "Background activity: A distant family member is seen sitting on a plastic chair in the background, drinking tea or scrolling through a phone. "
                "The porch floor is cracked cement with a few potted plants in recycled biscuit tins. Realistic clutter: An old dusty motorbike is parked partially visible under the porch roof. "
                "Lighting: Side golden hour sunlight reflecting off the warm bricks, creating deep, rich shadows."
            ),

            "Teras Rumah: Halaman & Jemuran": (
                "The character is seated on a simple weathered wooden bench on a tiled porch that overlooks a spacious dirt yard. "
                "Background: A view of the front yard with a rustic bamboo fence. A long laundry line with colorful clothes is visible in the distant background. "
                "Background activity: Two neighbors are seen chatting near the gate in the distance. A few stray chickens are pecking at the ground in the yard. "
                "The porch floor is old patterned tiles with some cracks. Authentic clutter: A stack of dried coconut shells and an old bicycle leaned against a pillar. "
                "Lighting: Bright morning sunlight illuminating the yard and casting long shadows onto the porch."
            ),

            "Gubuk: Lesehan Bambu": (
                "The character is sitting cross-legged (lesehan) directly on the raised bamboo floor of a rustic, open-air harvest hut. "
                "Background: The interior of the hut shows weathered bamboo pillars and a thatched roof made of dried palm leaves (rumbia). "
                "Background activity: A distant view of the green rice fields through the open side of the hut, with a small scarecrow visible. "
                "The workspace (miniature) is placed on the same bamboo floor in front of the character. Authentic clutter: A small woven mat (tikar pandan) and an old clay water jug (kendi). "
                "Lighting: Soft, natural shaded light with bright sunlight visible in the distant background."
            ),

            "Gubuk: Ambane Lincak": (
                "The character is seated on the edge of a wide, built-in bamboo platform (lincak) that serves as the hut's porch. "
                "Background: A rustic, tumble-down shack made of rough-hewn wood and bamboo. Several dried corn husks or garlic bunches hang from the rafters. "
                "Background activity: A distant farmer is seen walking along the narrow field path. "
                "The floor below the platform is hard-packed earth with scattered dry leaves and organic debris. Authentic clutter: A rustic farming tool (arit) leaning against a post in the far distance. "
                "Lighting: Warm golden hour sunlight hitting the side of the hut, creating long, deep shadows."
            ),

            "Gubuk: Tunggak Kayu": (
                "The character is seated on a large, smooth weathered tree stump (tunggak) inside a small, rustic shelter. "
                "Background: A simple structure with a leaky tin roof and walls made of tattered burlap and bamboo slats. "
                "Background activity: A few stray chickens are scratching the dirt floor near the entrance. "
                "The ground is dusty grey earth with natural uneven textures and a few river stones used as floor stabilization. "
                "Atmosphere: A raw, honest, and humble resting place for a farm worker under natural daylight."
            ),

            "Gubuk: Tengah Sawah": (
                "The character is sitting cross-legged (lesehan) on a raised bamboo floor of a small, open-sided harvest hut (gubuk) in the middle of a vast rice field. "
                "Background: An expansive view of green rice paddies stretching to the horizon under a clear sky. A few coconut trees are visible in the far distance. "
                "The hut structure is made of weathered bamboo with a thatched dried-grass roof. "
                "The workspace is placed directly on the bamboo slats in front of the character. Authentic clutter: A small clay water jug (kendi) and an old conical hat (caping) hanging on a pillar. "
                "Lighting: Bright, airy morning sunlight with soft reflections from the water in the rice fields."
            ),

            "Gubuk: Tengah Kebun": (
                "The character is seated on a wide bamboo platform (lincak) inside a rustic, shady hut surrounded by dense fruit trees. "
                "Background: A mix of banana leaves, papaya trees, and rambling vines visible through the hut's open walls. The environment feels lush and enclosed. "
                "Inside the hut: Bunches of dried corn or garlic are hanging from the rafters. The ground below the raised floor is dark earth with scattered dry leaves. "
                "Authentic clutter: A rustic wooden rake leaning against the hut and an old burlap sack. "
                "Lighting: Dappled sunlight filtering through the trees and the gaps in the hut's roof, creating a cinematic hazy atmosphere."
            ),

            "Gubuk: Tepi Hutan": (
                "The character is sitting on a smooth weathered tree stump (tunggak) inside a very simple, rugged shelter with a rusty tin roof. "
                "Background: A wilder, unkempt environment with tall grass and large tropical trees. The hut's walls are just a few bamboo slats and tattered sacks. "
                "The floor is hard-packed grey earth with natural cracks and small stones. "
                "Authentic activity: A few stray chickens pecking at the dirt near the entrance. "
                "Atmosphere: A raw, humble, and very authentic rural resting place under natural daytime sunlight."
            ),

            "Halaman Belakang: Kolam Koi Alami": (
                "The character is seated on a low wooden stool on a shaded patio overlooking a clear koi pond built with rough river stones. "
                "Background: The pond is filled with vibrant orange, white, and calico koi fish swimming just below the shimmering water surface. Water lilies and small mossy rocks line the edges. "
                "The patio floor is made of aged, dark grey cement with natural cracks. "
                "Background activity: A small bamboo water fountain (shishi odoshi style) is trickling water, creating gentle ripples. A few potted ferns are scattered around. "
                "Lighting: Soft, diffused natural light filtering through an overhead canopy, highlighting the glistening water and the scales of the fish."
            ),

            "Halaman Belakang: Teras Kolam": (
                "The character is seated on a wide rustic bamboo bench (lincak) right at the edge of a large, clear fish pond. "
                "Background: The water is crystal clear, showing many colorful koi fish gathered near the character, expecting food. The far side of the pond is lined with lush tropical plants like monstera and palms. "
                "The floor is a mix of wooden decking and smooth river pebbles. "
                "Authentic clutter: An old ceramic bowl containing fish food sits on the floor nearby. In the distance, a laundry line is partially visible behind some trees. "
                "Lighting: Warm afternoon sunlight hitting the water at an angle, creating beautiful caustic light patterns on the character's back."
            ),

            "Halaman Belakang: Kolam Semen Tradisional": (
                "The character is seated on a low weathered wooden crate next to a rectangular cement fish pond in a humble backyard. "
                "Background: The pond walls are slightly mossy grey cement. Inside, large koi fish in bright red and gold colors are swimming actively. "
                "The backyard floor is hard-packed earth with a few patches of moss and fallen leaves near the pond. "
                "Authentic clutter: A plastic bucket and a small hand-net leaning against the pond wall. A few stray chickens are pecking at the ground in the distant yard. "
                "Atmosphere: A peaceful, honest, and cool backyard environment under natural daylight."
            ),

            "Halaman: Jemuran Hasil Bumi": (
                "The character is seated on a low weathered wooden stool in a large, open sun-baked dirt yard. "
                "Background: A large, tattered blue tarpaulin is spread on the ground, covered with a thin layer of drying golden rice grain (gabah) or brown coffee beans. "
                "Background activity: A distant family member is using a wooden rake to spread the grain evenly. A few stray chickens are pecking at the edges. "
                "The floor is hard-packed grey earth with natural cracks. Authentic clutter: A stack of empty burlap sacks and a rustic wooden broom leaning against a tree. "
                "Lighting: Bright, high-contrast midday sun, making the golden grains look vibrant and sharp."
            ),

            "Halaman Belakang: Tepian Sungai": (
                "The character is seated on a large flat river stone or low wooden crate behind the house, overlooking a slow-moving shallow river. "
                "Background: The riverbank is lined with lush bamboo thickets and tattered banana leaves. The water is clear with visible river stones. "
                "Background activity: A distant neighbor is seen washing a motorbike or fetching water. A few ducks are swimming by. "
                "The ground around the character is sandy soil mixed with river pebbles and moss. "
                "Atmosphere: Cool, fresh, and serene tropical riverside environment under natural daylight."
            ),

            "Halaman Samping: Tumpukan Kayu": (
                "The character is seated on a low weathered wooden crate in the shady side-yard of a traditional house. "
                "Background: A massive, rustic pile of chopped firewood stacked unevenly against an old soot-stained wooden wall. "
                "Background activity: A faint wisp of natural smoke drifts from an open-air kitchen (pawon) nearby. A distant person is seen carrying a basket of coconut shells. "
                "The floor is dark, ash-dusted earth with scattered wood shavings and dry twigs. "
                "Lighting: Warm, cinematic golden hour light filtering through the trees, hitting the smoke and the rough wood textures."
            ),

            "Halaman: Bengkel Anyaman": (
                "The character is seated on a low wooden stool in a shaded side-yard used for bamboo crafting. "
                "Background: Stacks of long bamboo poles leaning against a rustic wooden wall, with several half-finished woven baskets (besek) or mats (tikar) scattered around. "
                "Background activity: A distant family member is seen stripping a bamboo pole into thin slats. Fine bamboo shavings are scattered on the ground. "
                "The floor is dark earth mixed with dry leaves and wood shavings. "
                "Lighting: Soft dappled sunlight filtering through a simple bamboo trellis overhead."
            ),

            "Halaman: Bawah Pohon Kelapa": (
                "The character is seated on a rustic lincak (bamboo bench) in a yard dominated by several tall, leaning coconut trees. "
                "Background: A view of a neighbor's house behind a simple bamboo fence. On the ground, a pile of dry coconut husks (sabut) and shells is stacked near an old tree trunk. "
                "Background activity: A distant neighbor is seen pulling a small wooden cart or riding a bicycle on a sandy path. "
                "The ground is sandy-brown soil with scattered dry palm fronds and small river stones. "
                "Lighting: Bright, high-contrast sunlight with long, dramatic shadows from the coconut trees."
            ),

            "Halaman Belakang: Area Sumur": (
                "The character is seated on a low weathered wooden crate near an old stone water well with a traditional pulley system (timba). "
                "Background: The well is covered in green moss and surrounded by large tropical leaves (talas or elephant ears). A bucket of water sits on the mossy edge. "
                "Background activity: A distant person is seen washing clothes or rinsing vegetables near a stone slab. A few ducks are wandering nearby. "
                "The ground is damp, dark earth with mossy patches and smooth river pebbles around the water area. "
                "Atmosphere: Cool, humid, and deeply nostalgic rural Indonesian morning vibe."
            ),

            "Kebun Bambu: Teduh Asri": (
                "The character is seated cross-legged (lesehan) on a raised bamboo floor, nestled inside a cozy, open-air green bamboo hut (gubuk) in the heart of a dense, lush, vibrant bamboo forest. "
                "Background: The forest is an expansive, textured wall of living green and yellow bamboo stalks forming a deeply shadowed, cool, and tranquil sanctuary. Massive bamboo leaves create a thick canopy above. "
                "Background activity: A distant Indonesian farmer is seen carrying natural bamboo poles on a winding forest path. Bird cages hang from the green branches. "
                "The ground is a thick carpet of dry, thin bamboo leaves and natural earth debris. Authentic clutter: A small clay kendi (water jug) and an old conical hat (caping) near a pillar. "
                "Lighting: Soft, natural dappled sunlight filtering through the narrow bamboo leaves, creating cool, high-contrast shadows and high depth."
            ),

            "Kebun Bunga: Bambu Hias": (
                "The character is seated on a wide rustic bamboo platform (lincak) inside a shaded bamboo gubuk surrounded by a vibrant, rimbun (dense) tropical flower garden. "
                "Background: Rows of living green ornamental bamboo plants create a cool, structured wall. Between the bamboo, bursts of colorful tropical flowers (orchid, monstera, bougainvillea) are densely packed. "
                "The ground below is hard-packed earth covered in rich moss and fallen flower petals. "
                "Authentic clutter: A rustic bamboo watering pole leaning against a gubuk post and an old woven pandan mat. A pair of worn-out rubber sandals near the stairs. "
                "Atmosphere: High fresh, vibrant, and deeply aromatic ambiance under clear daylight, with long, cool shadows from the tall bamboo and trees."
            ),

            "Kebun: Gubuk Bambu Hijau": (
                "The character is seated on a large smooth tree stump (tunggak) inside a humble, raw, open-air green bamboo shelter bordering a wilder garden edge. "
                "Background: The hut is built entirely of fresh-looking green bamboo with a rumbia (thatched) roof. Behind it, wild green vines and tall native grass create a lush textured wall. "
                "Background activity: A few distant ducks are wandering near a small muddy patch, and a distant person is fetching water from an old stone sumur (well). "
                "The floor is dark, damp earth with mossy patches and smooth river pebbles. Clutter: A discarded blue tarpaulin sheet near a dry irrigation pipe. "
                "Lighting: Deep, high-contrast dapple sunlight from a large overhead tree canopy, creating a cool and rugged atmosphere."
            ),

            "Depan Rumah: Jalan Setapak": (
                "The character is seated on a low weathered wooden stool on a shaded front porch, in the foreground. "
                "Background: Across a well-kept, lush green grass yard, a modest but charming Indonesian village house is visible in the distance. The house has clean, cream-colored plaster walls, a small terracotta tiled roof, and a neat wooden porch. It is surrounded by healthy mango and frangipani trees, creating a shaded and adem (cool) atmosphere. "
                "Background activity: A distant neighbor is seen walking along a narrow, winding dirt path towards the house, pushing an old bicycle. "
                "The foreground ground around the character is smooth, dark grey cement with a few potted plants in recycled tins. "
                "Lighting: Warm, soft natural daylight, highlighting the vibrant green foliage."
            ),

            "Samping Rumah: Sumur & Moss": (
                "The character is seated on a rustic lincak (bamboo bench) under the deep shade of a large jackfruit tree in the side-yard. "
                "Background: In the distance, the neat, white-walled side of the modest village house is visible, showing a simple wooden door and a shaded window. The roofline is clean and terracotta. The house is surrounded by neat rows of vegetable plants and flourishing flowering bushes. "
                "Background activity: Near the distant house, a person is seen sitting on the porch drinking tea. "
                "The foreground features an old, moss-covered stone water well (sumur) with a traditional timba (pulley system) near a paved path of river pebbles and moss. Authentic clutter: A stack of firewood. "
                "Lighting: Soft, shaded daylight filtering through the trees, creating a calm, cool environment."
            ),

            "Belakang Rumah: Kolam Ikan": (
                "The character is seated on a low weathered wooden crate by the edge of a clean, rectangular cement fish pond in the backyard. "
                "Background: Across the spacious backyard, the charming, traditional wooden rear-view of the simple village house is visible in the distance. The house features rich, dark teak-wood panels, a clean roof, and a neatly stacked wood pile under the eaves. Lush tropical plants like monstera and palms surround the house. "
                "Background activity: Two distant family members are seen sorting vegetables on the far side of the yard. "
                "The foreground ground around the pond is dark earth mixed with smooth river stones and scattered leaves. Authentic clutter: A small hand-net and a clay water kendi near the pond. "
                "Lighting: Warm, side golden hour daylight, creating beautiful caustics on the water and deep, rich colors on the house."
            ),

            "Dalam Rumah: Ruang Tamu": (
                "The character is seated on a wide rustic bamboo bench (lincak) in a spacious, clean living room of a traditional village house. "
                "Background: The room features high ceilings with exposed wooden beams and clean cream-colored walls. In the distance, an open wooden front door reveals a glimpse of the lush green front yard. A simple wooden guest table with a lace tablecloth sits nearby. "
                "Background activity: A distant family member is seen walking through the hallway or tidying up a wooden shelf. "
                "Interior details: Traditional patterned floor tiles (tegel kunci) and a few framed old family photos on the wall. "
                "Lighting: Bright natural light streaming in through the open door and large windows, creating soft, airy shadows."
            ),

            "Dalam Rumah: Dekat Jendela": (
                "The character is seated on a low wooden stool next to a large open wooden window with classic shutters. "
                "Background: Through the window, a vibrant green garden with banana leaves and flowering bushes is visible in the distance. Inside, the room is simple with a clean white wall and a rustic wooden cabinet. "
                "Background activity: A distant person is seen in the backyard through the window frame. "
                "Interior details: A small potted plant on the windowsill and a stack of old books. The floor is smooth, polished cement. "
                "Lighting: Strong, cinematic side-lighting from the window, highlighting the character's profile and the textures of the workspace."
            ),

            "Dalam Rumah: Ruang Tengah": (
                "The character is seated on a colorful woven pandan mat (tikar) on the floor in the center of a clean, airy room. "
                "Background: The room opens up into a dining area with a simple wooden table and a traditional food cover (tudung saji). A doorway in the distance leads to a sunlit backyard. "
                "Background activity: Distant family members are seen sitting around the dining table, chatting or drinking tea. "
                "Interior details: A large wooden wall clock and a birdcage hanging near the back entrance. The floor is clean, cool patterned tiles. "
                "Lighting: Soft, diffused indoor lighting with a bright glow coming from the distant back door."
            ),

            "Dalam Rumah: Dekat Pawon": (
                "The character is seated on a low weathered wooden crate in a clean, spacious traditional kitchen area. "
                "Background: A row of neatly stacked clay pots and wooden utensils on a rustic shelf. In the distance, a simple wooden back door is open, showing a green vegetable garden. "
                "Background activity: A distant family member is seen preparing snacks or pouring water from a clay jar (kendi). "
                "Interior details: Exposed brick accents on the lower wall and a floor made of hard-packed earth and stones near the entrance. "
                "Lighting: Atmospheric natural light from the doorway, creating a warm, earthy, and productive vibe."
            ),

            "Dalam Rumah: Beranda Dalam": (
                "The character is seated on a rustic bamboo chair in a semi-open inner porch that connects the main house to the back area. "
                "Background: A view of a small indoor garden patch with a few tropical plants and a stone water feature. The neat wooden walls of the house surround the area. "
                "Background activity: A distant neighbor is seen waving from the back gate. A cat is resting on a nearby wooden ledge. "
                "Interior details: Hanging ferns and a floor of smooth river pebbles mixed with cement tiles. "
                "Lighting: Overhead natural light from a skylight or open roof section, creating a bright, fresh, and very 'adem' atmosphere."
            ),

            "Alam: Kebun Bunga Asri": (
                "The character is seated on a low weathered wooden stool on a natural dirt path, nestled inside a lush, vibrant tropical garden. "
                "Background: The garden is a dense, colorful tapestry of blooming flowers (orchids, monstera, heloconia, bougainvillea) growing densely and naturally. Through a distant gap in the rimbun (lush) jungle canopy, a natural waterfall is visible cascading down a verdant cliff face. "
                "Background activity: A distant Indonesian villager is seen carrying a basket of flowers or plants on a winding forest path. Bird cages hang from large tree branches. "
                "The ground around the character is covered in a carpet of dry leaves, fallen twigs, and patches of moss. Authentic clutter: A small clay kendi (water jug) and an old conical hat near a pillar. "
                "Lighting: Soft, natural dappled sunlight filtering through the dense leaves, creating cool, high-contrast shadows and depth."
            ),

            "Alam: Tepian Sungai Kecil": (
                "The character is seated on a wide rustic bamboo platform (lincak) inside a shaded bamboo gubuk overlooking a clear, slow-moving river. "
                "Background: Across the clear river, a massive, vibrant tropical forest rises, and a majestic, natural waterfall is visible in the distant background flowing down a lush cliff. The far riverbank is lined with various colorful flowering bushes and large ferns. "
                "Background activity: Distant villagers are seen fishing or washing clothes in the distance. A few ducks are swimming by. "
                "The foreground ground is a mix of red soil, smooth river pebbles, and moss. "
                "Atmosphere: High fresh, vibrant, and deeply aromatic ambiance under clear daylight, with long, cool shadows from the tall trees."
            ),

            "Alam: Terasering Bunga": (
                "The character is seated on a simple weathered stool on a shaded terrace of a sloping, unkempt flower garden. "
                "Background: The hillside garden is covered in vibrant colorful flowers in naturally messy terraced beds. A distant, natural waterfall is visible in the far distance, cascading down a deep, forested valley. The far valley edge is bordered by dense coconut trees. "
                "Background activity: Two distant villagers are seen carefully picking or planting flowers on the far terrace. A stray cat is wandering near the garden edge. "
                "The ground is a mix of red soil, natural rock steps, and dry leaves.Authentic clutter: Several empty wooden fruit crates and an old bamboo watering pole nearby. "
                "Lighting: Warm golden hour sunlight highlighting the vibrant colors and creating deep, atmospheric haze."
            ),

            "Alam: Tepi Hutan Bambu": (
                "The character is seated on a low weathered wooden crate behind a simple rustic bamboo shelter. "
                "Background: A view into a vast, dense green bamboo jungle on the far bank of a small stream. Through a distant clear section in the forest, a narrow, natural waterfall is visible flowing down a verdant rock face in the deep distance. Colorful flowering vines scramble over the foreground bamboo structure. "
                "Background activity: Distant farmers are seen carrying bundles of bamboo or crops on a forest trail. A small wooden scarecrow is visible in the far field. "
                "The ground is dusty earth mixed with river stones and dry organic debris. Authentic clutter: An old motorbike with rattan bronjong baskets parked near a tree. "
                "Lighting: Deep, high-contrast dapple sunlight, creating a very cool and rugged atmosphere."
            ),

            "Alam: Sumur Alami Asri": (
                "The character is seated on a low weathered wooden bench next to an old, moss-covered natural spring well with a wooden pulley. "
                "Background: The well is nestled among large tropical leaves (talas, ferns) and colorful wild orchids. In the far distance, through the forest opening, a beautiful natural waterfall cascading down a verdant cliff is visible. "
                "Background activity: A distant person is seen washing vegetables or filling water from the spring. "
                "The ground around the character is damp, dark earth mixed with mossy patches and smooth river stones.Authentic clutter: A clay kendi and a rustic hand-net nearby. "
                "Atmosphere: Very cool, humid, and deeply nostalgic rural Indonesian morning vibe under natural daylight."
            ),

            "Warkop: Teras Depan": (
                "The character is seated on a low wooden stool on the shaded porch of a humble village coffee shop (Warkop). "
                "Background: The warung wall is filled with hanging colorful instant coffee sachets (renceng). A few weathered wooden benches sit across from the character. "
                "Background activity: Distant village men are seen sitting, drinking coffee, and chatting. A few motorbikes are parked in the dusty front yard. "
                "The floor is cracked cement with scattered cigarette butts and dry leaves. Authentic clutter: A small glass jar of crackers (kaleng kerupuk) on a nearby table. "
                "Lighting: Warm, soft natural light under the porch roof with a bright sun-drenched road in the far distance."
            ),

            "Pasar: Kios Kelontong": (
                "The character is seated on a weathered wooden crate in front of a busy traditional market stall. "
                "Background: The kiosk is packed with sacks of rice, colorful snack packages, and hanging bananas. "
                "Background activity: Distant customers in casual village attire are seen bargaining and carrying plastic grocery bags. A slow-moving old bicycle passes through the narrow market aisle. "
                "The ground is hard-packed earth with organic debris and scattered vegetable scraps. "
                "Atmosphere: High-energy, bustling, and honest rural commerce under bright morning sunlight."
            ),

            "Pasar: Kios Sayur": (
                "The character is seated on a simple rustic bench next to a vibrant display of vegetables. "
                "Background: Baskets filled with red chilies, green cabbage, and orange carrots are stacked neatly behind the character. "
                "Background activity: A distant seller is seen weighing vegetables for a customer. A stray cat is wandering near the baskets. "
                "The floor is damp grey cement with a few puddles from the morning mist. Authentic clutter: A stack of empty bamboo baskets (besek) nearby. "
                "Lighting: Clear, fresh morning daylight highlighting the dewy textures of the vegetables."
            ),

            "Toko: Sembako Desa": (
                "The character is seated on a low wooden stool on the sidewalk in front of a modest village provision store. "
                "Background: A row of large open sacks filled with various grains and flour. Colorful soap and detergent advertisements are plastered on the wooden walls. "
                "Background activity: A distant person is seen loading goods onto a motorbike's rattan baskets (bronjong). "
                "The ground is dusty red soil with scattered river stones. Authentic clutter: An old rusted scale and a stack of wooden crates. "
                "Lighting: Side golden hour sunlight creating rich, deep shadows and warm tones."
            ),

            "Pasar: Kios Gorengan/Jajanan": (
                "The character is seated on a rustic bamboo bench near a traditional snack vendor. "
                "Background: A glass display case filled with golden fried snacks (gorengan) and traditional cakes. A faint wisp of steam or smoke drifts from a large frying wok in the distance. "
                "Background activity: Kids are seen gathered around buying snacks. A few motorbikes are passing by on the street. "
                "The floor is a mix of mossy paving blocks and dry earth. "
                "Atmosphere: Authentic, lively, and nostalgic village street scene under natural daylight."
            )         
        }
		
		# --- 4. MASTER AUDIO & SOULFUL EXPRESSION (ULTRA STABLE VOICE SYSTEM) ---
        MASTER_AUDIO_STYLE = {
            "Logat_Nenek": [
                "Extremely frail 92-year-old Javanese village grandmother with thick rural Jawa kampung accent, extremely weak thin and breaking voice, constant heavy vocal tremor, very raspy hoarse cracking tone, breathy and airy quality, speaks extremely slowly with long shaky pauses and visible tired breathing effort, frequent voice cracks on almost every word, sounds physically exhausted and delicate like a real 92-95 year old nenek tua with very weak lungs",
                "Super elderly 93-year-old Javanese nenek, thick kampung ngoko accent, deeply aged thin trembling voice full of instability, whispery and breaking at times, heavy constant vocal tremor, very low volume, extremely slow shaky delivery around 45-60 words per minute, frequent cracking and quivering, authentic extreme old age vocal deterioration, almost no energy left, natural weak breathing",
                "94+ year old extremely frail Indonesian grandma with strong Jawa kampung accent, very weak raspy voice with strong constant quivering tremor, dry cracked hoarse tone, thin wobbly resonance, labored slow speech with many long pauses for breath, voice often cracks and sounds like it's about to disappear, zero energy, sounds physically exhausted and fragile",
                "90-year-old extremely frail nenek tua with thick rural Javanese accent, constantly shaking elderly female voice with high-frequency vocal tremor, very breathy hoarse quality, extremely slow and weak delivery, frequent voice cracks and instability, heavy tired natural breathing effort, sounds exhausted and physically fragile like a real 92+ year old grandmother with severely weakened lungs and vocal cords"
            ],
            "Logat_Kakek": [
                "Extremely frail 89-year-old Indonesian village grandfather with thick Jawa kampung accent, deep but very weak and raspy old man voice, noticeable heavy vocal tremor and shakiness, dry cracked hoarse tone, slow labored delivery with long pauses and breath effort, sounds like a real 90+ year old kakek with weathered and tired vocal cords",
                "Very old 91-year-old Javanese kakek with rural kampung accent, low-pitched trembling elderly male voice full of instability, heavy age-related wobble, hoarse and rough texture, extremely slow speech around 50-60 words per minute, frequent voice cracks and breath breaks, physically weak and exhausted sounding",
                "93+ year old extremely frail Indonesian grandfather with strong Jawa accent, thin shaky old man voice despite low pitch, strong constant vocal tremor, dry cracked and breathy tone, extremely slow and effortful delivery, sounds delicate and on the verge of breaking",
                "89-year-old extremely frail kakek tua with thick kampung accent, deep raspy voice with constant trembling, weak resonance, slow and unsteady speech with many pauses, hoarse from decades of use, sounds physically old, tired and fragile like a real 92-year-old grandfather"
            ],

            "Mood": [
                "Sad and deeply fragile",
                "Tired and resigned with heavy exhaustion",
                "Calm but physically very weak",
                "Peaceful with quiet melancholy",
                "Emotional yet extremely tired",
                "Stoic with visible physical frailty",
                "Gentle and nostalgic with shaky delivery",
                "Resigned and accepting with weary tone"
            ],

            "Physical Action": [
                "Gently holding the miniature mosque with both trembling hands, slowly turning it slightly while looking at it with tired eyes.",
                "Carefully touching the carved dome with shaky fingertips, then slowly tracing the edge with great care.",
                "Holding the watermelon mosque close to her chest with frail arms, then slowly lowering it onto the table while breathing heavily.",
                "Using one shaky hand to gently adjust the position of the miniature while the other hand supports it from below.",
                "Slowly lifting one trembling hand to point at a small detail on the mosque, then lowering it back with visible effort.",
                "Cradling the carved mosque in her lap with both hands, gently rotating it while gazing at it quietly.",
                "Softly brushing away tiny rind scraps from the base of the mosque using her frail fingers, movements slow and unsteady.",
                "Holding the object with both hands, slowly bringing it closer to her face to look at it more clearly, then lowering it again."
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
                    label_visibility="collapsed",
                    key="input_dialog_key"
                )
                st.session_state.current_dialog = user_dialog

            with c6:
                st.markdown('<p class="small-label">ACTING & PERFORMANCE</p>', unsafe_allow_html=True)
                
                is_perempuan = any(x in pilihan_user.lower() for x in [
                    "nenek", "ibu", "aminah", "siti", "marsi", "ponirah", "juminah",
                    "sikem", "dulah", "sartini", "tinah", "wati"
                ])
                
                if is_perempuan:
                    pilih_logat = st.selectbox("Pilih Logat Suara", MASTER_AUDIO_STYLE["Logat_Nenek"], key="logat_nenek")
                else:
                    pilih_logat = st.selectbox("Pilih Logat Suara", MASTER_AUDIO_STYLE["Logat_Kakek"], key="logat_kakek")
                
                pilih_mood = st.selectbox("Pilih Mood", MASTER_AUDIO_STYLE["Mood"], key="mood_select")
                pilih_aksi = st.selectbox("Pilih Gerakan Tubuh", MASTER_AUDIO_STYLE["Physical Action"], key="aksi_select")

            st.write("")
            btn_gen = st.button("🚀 GENERATE VIDEO PROMPT", type="primary", use_container_width=True, key="btn_generate_video")


        # --- LOGIC GENERATOR (ULTRA LOCK VERSION) ---
        if btn_gen:
            scene_context = (
                f"LIGHTING: Soft, diffused 5 PM golden-hour side lighting with natural contrast. "
                f"Natural outdoor exposure, flat documentary film look.\n"
                f"COMPOSITION: STRICT LOW-ANGLE Tight Medium-Shot. Camera height locked at chest-level. "
                f"Strong frame dominance on the handcrafted miniature mosque."
            )

            env_detail = MASTER_GRANDMA_SETTING.get(pilihan_set, "Natural outdoor setting.")
            soul_desc = MASTER_FAMILY_SOUL.get(pilihan_user, "An Indonesian person.")
            
            wardrobe_dict = MASTER_FAMILY_WARDROBE.get(char_key, {})
            baju_desc = wardrobe_dict.get(baju_pilihan, "Simple modest clothes.")

            # Gender & Visual Identity Lock
            is_perempuan = any(x in pilihan_user.lower() for x in [
                "nenek","ibu","aminah","siti","marsi","ponirah","juminah",
                "sikem","dulah","sartini","tinah","wati"
            ])
            
            if is_perempuan:
                gender_lock = "Extremely frail 88-92 year old Indonesian grandmother with deeply wrinkled sagging skin, prominent age spots, thin white hair, sunken tired eyes, hollow cheeks, and fragile posture."
            else:
                gender_lock = "Extremely frail 88-92 year old Indonesian grandfather with deep wrinkles, sun-parched skin, prominent age spots, thin white hair and beard, sunken weary eyes, and fragile frame."

            aksi_final = pilih_aksi.strip()
            mood_final = pilih_mood.strip()
            logat_final = pilih_logat.strip()

            # --- ASSEMBLY PROMPT (V.39 - HIJAB + SUPER FRAIL JAWA KAMPUNG) ---
            GLOBAL_QUALITY_LOCK = (
                "RAW CINEMATIC FOOTAGE LOCK: Must look like real unedited 8K documentary footage shot on film. "
                "EXTREMELY SHARP DETAIL, rich natural contrast, NO AI smoothing, NO CGI look, NO plastic textures, "
                "NO over-sharpening, capture true optical imperfections, subtle film grain, and natural lens breathing."
            )

            final_ai_prompt = (
                f"{GLOBAL_QUALITY_LOCK}\n\n"
                
                f"ULTRA 8K REALISM & SHARPNESS PRIORITY:\n"
                f"- The handcrafted miniature mosque is the primary focal point with strong frame dominance\n"
                f"- Extremely sharp 8K detail on the miniature mosque: clear carving lines, natural material texture, realistic colors, moist reflections, and organic imperfections\n"
                f"- Character's face, eyes, and weathered hands must also be razor sharp with authentic elderly skin texture, deep wrinkles, age spots, and natural skin details\n"
                f"- High natural contrast between the miniature mosque and the elderly character\n"
                f"- True documentary realism: looks like real 8K film footage, NO CGI, NO plastic look, NO over-smoothed skin, NO artificial glow, NO cartoon style\n\n"
                
                f"CHARACTER IDENTITY:\n"
                f"{soul_desc}\n"
                f"{gender_lock}\n"
                f"Wardrobe: {baju_desc}\n"
                f"MANDATORY: Hyper-realistic elderly skin texture with deep wrinkles, prominent age spots, sunken tired eyes, fragile appearance, NO face smoothing, NO smile, NO youthful features.\n\n"
                
                f"ENVIRONMENT:\n"
                f"{env_detail}\n"
                f"- High rustic wooden table at chest level.\n"
                f"Lighting and Atmosphere: {scene_context}\n\n"
                
                f"CAMERA & MOTION:\n"
                f"Very slow organic handheld movement with subtle natural sway. Extremely slow gentle push-in toward the miniature mosque and character's hands. "
                f"Natural micro movements only. Both the miniature mosque and the character's face/hands stay razor sharp throughout the shot. "
                f"NO sudden camera moves, NO fast zoom, NO static locked camera.\n\n"
                
                f"PERFORMANCE:\n"
                f"{aksi_final}\n"
                f"Mood: {mood_final}\n"
                f"- Minimal but natural elderly movement\n"
                f"- Eyes slowly alternate between the miniature mosque and camera with tired expression\n\n"
                
                f"VOICE PROFILE:\n"
                f"{logat_final}\n"
                f"Delivery style: {mood_final}. "
                f"Extremely weak, thin, and breaking voice with constant heavy vocal tremor and instability. "
                f"Thick rural Javanese kampung accent, slow ngoko-style elderly speech pattern. "
                f"Voice cracks frequently, quivers on almost every word, very raspy and hoarse, breathy and airy. "
                f"Extremely slow delivery with long weary pauses and natural tired breathing effort. "
                f"Breathing sounds weak, labored, and realistic — not exaggerated. "
                f"Sounds physically exhausted and on the verge of fading like a real 92-95 year old nenek Jawa kampung with very weak lungs and vocal cords. "
                f"Almost no energy, voice sounds fragile and delicate.\n\n"
                
                f"SPOKEN DIALOG:\n"
                f"\"{user_dialog}\"\n\n"
                
                f"DIALOG DELIVERY RULE:\n"
                f"- AUDIO ONLY. STRICTLY NO TEXT OVERLAY ON SCREEN.\n"
                f"- Spoken naturally with real elderly shaky Jawa kampung voice and breathing effort\n\n"
                
                f"OBJECT DETAIL:\n"
                f"{deskripsi_teknis}\n\n"
                
                f"ULTRA DETAIL ENFORCEMENT:\n"
                f"- Razor sharp 8K detail on every carving line, material texture, juice droplets, and skin wrinkles\n"
                f"- Natural moist reflections, visible imperfections, realistic light interaction\n\n"
                
                f"NEGATIVE PROMPT:\n"
                f"blurry, soft focus, low detail, motion blur, AI look, CGI, plastic texture, over-smooth skin, waxy skin, "
                f"artificial sharpness, glowing edges, fast movement, sudden camera change, static camera, "
                f"energetic voice, young voice, middle-aged voice, smiling, laughing, wide shot, high angle, "
                f"text, watermark, subtitles, on-screen text"
            )

            # --- 7. TAMPILKAN HASIL ---
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
