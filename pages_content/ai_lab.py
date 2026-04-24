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
            "Nenek Aminah": "88-year-old Javanese grandmother. Unique facial landmark: Narrow face with high-set sharp cheekbones and a distinct mole near the left eye. Face: Paper-thin translucent skin with extreme hyper-pigmentation age spots. Deep vertical forehead wrinkles, sagging jawline. Eyes: Sunken watery eyes with heavy drooping lids. Frame: Tall, severely shrunken skeletal thin frame.",
            "Nenek Siti": "73-year-old petite Javanese grandmother. Unique facial landmark: Small round face with very plump sagging cheeks and a soft chin. Face: Warm yellowish-golden skin with visible sun damage. Eyes: Large round eyes with heavy lids and dark under-eye hollows. Frame: Tiny delicate frame with soft, fragile hunched posture.",
            "Nenek Marsi": "94-year-old Javanese grandmother. Unique facial landmark: Wide square jaw with prominent broad cheekbones. Face: Deep horizontal forehead furrows and loose parchment-like skin hanging under the chin. Deep warm sawo matang skin with prominent age spots. Eyes: Narrow eyes under thick heavy lids. Frame: Broad but frail heavily hunched frame.",
            "Nenek Ponirah": "80-year-old Javanese grandmother. Unique facial landmark: Round full face with heavy sagging cheeks and soft jaw. Face: Warm brownish sun-kissed skin, leathery texture. Eyes: Almond-shaped eyes with noticeable trembling lower eye bags. Frame: Plump but shrunken frame with loose hanging skin on arms.",
            "Nenek Juminah": "91-year-old very thin Javanese grandmother. Unique facial landmark: Sharp angular tirus face with sunken temples and hollow cheeks. Face: Warm tan skin stretched tightly over bone structure. Eyes: Deep-set eyes with thin translucent eyelids. Frame: Extremely thin bony frame, very fragile.",
            "Nenek Sikem": "76-year-old Javanese grandmother. Unique facial landmark: Very round plump face with heavy lower cheeks and multiple soft skin folds. Face: Warm sawo matang skin with golden undertone and visible age spots. Eyes: Small eyes almost hidden under puffy drooping lids. Frame: Short rounded fragile frame.",
            "Nenek Dulah": "68-year-old Sundanese grandmother. Unique facial landmark: Soft oval face with naturally full sagging cheeks. Face: Bright warm langsat skin with subtle sun spots. Eyes: Gentle almond eyes with soft under-eye hollows. Frame: Soft fragile frame with rounded hunched shoulders.",
            "Nenek Sartini": "84-year-old Sundanese grandmother. Unique facial landmark: Wide round face with heavy sagging cheeks and deep nasolabial folds. Face: Warm brownish skin with leathery texture. Eyes: Wide-set eyes with heavy lids and watery gaze. Frame: Plump but frail shrunken frame.",
            "Nenek Tinah": "93-year-old thin Javanese grandmother. Unique facial landmark: Long oval tirus face with deeply sunken cheeks and sharp jawline. Face: Warm tan skin with extreme wrinkle density. Eyes: Deep sunken eyes with heavy lids. Frame: Very thin elongated shrunken frame.",
            "Nenek Wati": "64-year-old small Sundanese grandmother. Unique facial landmark: Small delicate round face with soft heavy sagging skin. Face: Warm langsat tone with visible age-related fatigue lines. Eyes: Large gentle eyes with heavy drooping lids. Frame: Very small delicate fragile frame.",
            "Kakek Marto": "87-year-old Javanese grandfather. Unique facial landmark: Long rectangular face with strong jawline and deep forehead wrinkles. Face: Rough leathery sawo matang skin with prominent hand veins. Eyes: Deep-set eyes with heavy trembling lower lids. Frame: Lean bony frame with heavily hunched shoulders.",
            "Kakek Somo": "79-year-old Javanese grandfather. Unique facial landmark: Round soft face with heavy jowls and multiple soft skin folds. Face: Warm brownish skin with visible sun damage. Eyes: Small tired eyes under puffy lids and dark circles. Frame: Short rounded fragile hunched frame.",
            "Kakek Joyo": "90-year-old Javanese grandfather. Unique facial landmark: Square face with prominent brow ridge and deep horizontal wrinkles. Face: Leathery rough sun-exposed skin with many age spots. Eyes: Narrow eyes with thick heavy lids. Frame: Once sturdy but now severely shrunken frame.",
            "Kakek Hardi": "95-year-old Javanese grandfather. Unique facial landmark: Extremely shrunken skeletal face with hollow cheeks and sunken temples. Face: Thin translucent warm tan skin with visible blood vessels. Eyes: Deep sunken cloudy eyes. Frame: Very thin delicate bony frame.",
            "Kakek Sableng": "83-year-old Javanese grandfather. Unique facial landmark: Broad face with high cheekbones and heavy fatigue lines. Face: Warm tan skin with leathery texture and deep pores. Eyes: Tired eyes with heavy trembling lower lids. Frame: Lean frame with hunched posture.",
            "Kakek Sinto": "94-year-old Javanese grandfather. Unique facial landmark: Deeply sunken skeletal face with hollow cheeks and collapsed jaw. Face: Thin warm tan skin with extreme wrinkle density. Eyes: Deep sunken cloudy eyes with watery gaze. Frame: Very thin delicate frame with bony shaky hands.",
            "Kakek Wiryo": "74-year-old Javanese grandfather. Unique facial landmark: Broad labor-worn face with high cheekbones and deep pores. Face: Rough warm sawo matang skin with sun spots. Eyes: Tired eyes with heavy lower lids. Frame: Lean weathered frame with rough worker's hands.",
            "Kakek Usman": "86-year-old Indonesian grandfather. Unique facial landmark: Deeply wrinkled face with prominent fatigue lines and sunken cheeks. Face: Warm brownish skin with leathery texture. Eyes: Heavy-lidded weary eyes with cloudy pupils. Frame: Thin frame with slow, fragile movements."
        }
		
		# --- 2. MASTER WARDROBE (6 VARIAN PER KARAKTER - DAILY & NEAT HIJAB) ---
        MASTER_FAMILY_WARDROBE = {
            "Nenek Aminah": {
                "Kebaya Lurik Klasik": "A faded brown Javanese lurik kebaya with thin vertical stripes, weathered fabric texture, slightly frayed edges.",
                "Daster Kampung Motif Bunga": "A loose, well-worn house dress (daster) with faded floral patterns, thin cotton material showing age.",
                "Kebaya Encim Putih Lusuh": "A simple white cotton kebaya with subtle traditional embroidery, slightly yellowed by age, modest and humble.",
                "Baju Kurung Tua": "A plain, dark green traditional baju kurung, very thin fabric, looking loose and comfortable for an elderly person.",
                "Setelan Jarik & Kebaya Polos": "A dark navy simple kebaya paired with a brown batik jarik cloth wrapped around the waist, authentic village style."
            },
            "Nenek Siti": {
                "Kebaya Kartini Muda (Faded)": "A simple pale pink kebaya with weathered texture, very thin and looking used for decades.",
                "Daster Katun Tipis": "A dark blue house dress with tiny white dots, faded and soft from years of washing.",
                "Kebaya Kutu Baru Polos": "A humble mustard yellow kebaya with a simple design, showing signs of wear and age.",
                "Baju Kurung Motif Kecil": "A light green traditional baju kurung with very faded tiny floral prints, simple and rural.",
                "Setelan Kaos & Jarik": "A simple oversized white cotton t-shirt paired with a dark brown batik jarik, casual grandma look."
            },
            "Nenek Marsi": {
                "Hijab Katun Pudar": "Faded brown cotton hijab with worn, paper-thin texture, wrapped loosely around the face, paired with a dark purple velvet kebaya.",
                "Tanpa Hijab (Rambut Uban)": "No head covering, showing messy thin white hair with visible scalp, wearing a dark purple velvet kebaya.",
                "Kerudung Putih Tua": "A very old white cotton kerudung loosely draped over the head, paired with a classic brown batik house dress.",
                "Daster Kampung Lusuh": "A dark purple house dress with traditional patterns, weathered and thin fabric."
            },
            "Nenek Ponirah": {
                "Hijab Tanah (Meding)": "Earthy brown cotton hijab, paper-thin and faded, paired with a light yellow cotton kebaya.",
                "Tanpa Hijab (Rambut Tipis)": "No head covering, showing thin white hair and a weathered forehead, wearing a dark red house dress.",
                "Kerudung Lace Putih": "A thin white lace kerudung loosely draped over the head, showing some white hair at the edges.",
                "Kebaya Jawa Klasik": "A simple dark brown kebaya with a traditional design, showing signs of long use."
            },
            "Nenek Juminah": {
                "Hijab Katun Pudar": "Faded brown cotton hijab with worn texture, paired with a thin blue striped lurik kebaya.",
                "Tanpa Hijab (Rambut Uban)": "No head covering, showing messy thin white hair, wearing a loose house dress with earth tones.",
                "Kerudung Putih Tua": "A very old white cotton kerudung loosely draped over the head, paired with a simple black cotton kebaya.",
                "Daster Kampung Lusuh": "A pale yellow house dress with faded patterns, thin and aged fabric."
            },
            "Nenek Sikem": {
                "Hijab Tanah (Meding)": "Earthy brown cotton hijab, paper-thin and faded, paired with a dark maroon velvet kebaya.",
                "Tanpa Hijab (Rambut Tipis)": "No head covering, showing thin white hair, wearing a dark blue batik house dress.",
                "Kerudung Lace Putih": "A thin white lace kerudung loosely draped over the head, paired with a dark green kebaya.",
                "Kebaya Jawa Klasik": "A simple dark green kebaya, showing signs of wear and age, humble village style."
            },
            "Nenek Dulah": {
                "Hijab Katun Pudar": "Faded brown cotton hijab with worn texture, paired with a white kebaya with faded pink flowers.",
                "Tanpa Hijab (Rambut Uban)": "No head covering, showing messy thin white hair, wearing a dark brown house dress.",
                "Kerudung Putih Tua": "A very old white cotton kerudung loosely draped over the head, paired with a dark mustard kebaya.",
                "Daster Kampung Lusuh": "A pale blue traditional baju kurung, thin fabric, looking very humble and simple."
            },
            "Nenek Sartini": {
                "Hijab Katun Pudar": "Faded brown cotton hijab with worn, paper-thin texture, wrapped loosely around the face, paired with a simple floral daster.",
                "Tanpa Hijab (Rambut Uban)": "No head covering, showing messy thin white hair with visible scalp, wearing a very old faded daster.",
                "Kerudung Putih Tua": "A very old white cotton kerudung loosely draped over the head, paired with a faded batik kebaya.",
                "Daster Kampung Lusuh": "A dark blue house dress with tiny white flowers, faded and looking very used."
            },
            "Nenek Tinah": {
                "Hijab Tanah (Meding)": "Earthy brown cotton hijab, paper-thin and faded, paired with a simple white cotton kebaya.",
                "Tanpa Hijab (Rambut Tipis)": "No head covering, showing thin white hair and a weathered forehead, wearing a dark brown batik house dress.",
                "Kerudung Lace Putih": "A thin white lace kerudung loosely draped over the head, paired with a dark green baju kurung.",
                "Kebaya Jawa Klasik": "A simple dark purple kebaya with a traditional design, showing signs of long use."
            },
            "Nenek Wati": {
                "Hijab Tanah (Meding)": "Earthy brown cotton hijab, paper-thin and faded, paired with a simple pink cotton kebaya.",
                "Tanpa Hijab (Rambut Tipis)": "No head covering, showing thin white hair and a weathered forehead, wearing a dark blue house dress.",
                "Kerudung Lace Putih": "A thin white lace kerudung loosely draped over the head, showing some white hair at the edges.",
                "Kebaya Jawa Klasik": "A simple black cotton kebaya, showing signs of wear and age, modest village look."
            },
            "Kakek Marto": {
                "Peci Hitam Berdebu": "A worn black velvet peci with visible dust and faded edges, paired with a faded grey cotton button-up shirt.",
                "Peci Putih Haji (Kuning)": "An old white haji peci that has turned yellowish with age, paired with a simple white oversized t-shirt.",
                "Baju Koko & Peci": "A simple white traditional koko shirt paired with a dusty black peci, modest and rural.",
                "Kakek Tanpa Peci": "No head covering, showing short messy white hair, wearing a dark brown batik shirt with faded patterns."
            },
            "Kakek Somo": {
                "Peci Hitam Berdebu": "A worn black velvet peci with visible dust, paired with a dark red plaid flannel shirt.",
                "Peci Putih Haji": "An old white haji peci that has turned yellowish, paired with a dark blue polo shirt, fabric is thin and aged.",
                "Baju Koko & Peci": "A pale green traditional koko shirt paired with a dusty black peci, simple and rural.",
                "Kakek Sederhana (Tanpa Peci)": "No head covering, showing short thin white hair, wearing a classic brown batik shirt."
            },
            "Kakek Joyo": {
                "Peci Hitam Kusam": "A dark black peci with visible wear and tear on the seams, paired with a faded blue denim shirt.",
                "Peci Putih Tua": "A thin white haji peci, yellowed and unpolished, paired with a simple white cotton t-shirt.",
                "Baju Koko & Sarung": "A simple black traditional koko shirt paired with a dark brown plaid sarong and a dusty black peci.",
                "Kakek Sederhana (Tanpa Peci)": "No head covering, showing short thin white hair, wearing a dark brown batik shirt with large faded patterns."
            },
            "Kakek Hardi": {
                "Peci Hitam Berdebu": "A worn black velvet peci with visible dust, paired with a simple white button-up shirt, yellowed and weathered.",
                "Peci Putih Haji": "An old white haji peci, yellowed with age, paired with a thin grey cotton t-shirt, faded and soft.",
                "Baju Koko & Peci": "A pale blue traditional koko shirt paired with a dusty black peci, simple and rural.",
                "Kakek Tua (Tanpa Peci)": "No head covering, showing short thin white hair, wearing a classic brown batik shirt."
            },
            "Kakek Sableng": {
                "Peci Hitam Berdebu": "A worn black velvet peci with visible dust, paired with a dark blue cotton button-up shirt.",
                "Peci Putih Haji": "An old white haji peci that has turned yellowish, paired with a simple white cotton t-shirt, thin and aged.",
                "Baju Koko & Peci": "A simple brown traditional koko shirt paired with a dusty black peci, simple and rural.",
                "Kakek Tanpa Peci": "No head covering, showing short thin white hair, wearing a classic batik shirt."
            },
            "Kakek Sinto": {
                "Peci Hitam Berdebu": "A worn black velvet peci with visible dust, paired with a simple white button-up shirt, yellowed and weathered.",
                "Peci Putih Haji": "An old white haji peci that has turned yellowish, paired with a thin dark blue cotton t-shirt.",
                "Baju Koko & Peci": "A pale green traditional koko shirt paired with a dusty black peci, simple and rural.",
                "Kakek Tanpa Peci": "No head covering, showing short thin white hair, wearing a dark brown batik shirt with tiny faded patterns."
            },
            "Kakek Wiryo": {
                "Peci Hitam Kusam": "A dark black peci with visible wear, paired with a dark brown cotton button-up shirt, weathered and faded.",
                "Peci Putih Tua": "A thin white haji peci, yellowed and unpolished, paired with a simple white cotton t-shirt, thin and yellowed.",
                "Baju Koko & Sarung": "A simple black traditional koko shirt paired with a dark green plaid sarong and a dusty black peci.",
                "Kakek Tua (Tanpa Peci)": "No head covering, showing short thin white hair, wearing a dark batik shirt with very faded patterns."
            },
            "Kakek Usman": {
                "Peci Hitam Berdebu": "A worn black velvet peci with visible dust, paired with a simple white button-up shirt, yellowed and weathered.",
                "Peci Putih Haji": "An old white haji peci, yellowed with age, paired with a thin black cotton t-shirt, faded and soft.",
                "Baju Koko & Peci": "A dark blue traditional koko shirt paired with a dusty black peci, showing signs of long use.",
                "Kakek Sederhana (Tanpa Peci)": "No head covering, showing short thin white hair, wearing a dark brown batik shirt with faded patterns."
            }
        }
		# --- 3. MASTER BAHAN MINIATUR MASJID ---
        MASTER_KONTEN_ALL = {
            "🍉 Miniatur Dari Buah": {
				"Semangka: Monumental Kubah Daging": (
    				"A hyper-realistic hand-carved mosque made entirely from a whole watermelon, built as a large tabletop monument approximately 1 meter in scale, firmly placed on a wooden table surface. "
    				"The architecture is grand and massive, featuring a dominant central dome formed from solid watermelon flesh, smooth, rounded, and visibly dense with rich red moist texture. "
    				"Multiple supporting domes surround the main dome with clear hierarchical scaling, along with tall symmetrical minarets rising with strong vertical emphasis. "
    				"The walls are constructed from thick watermelon rind, deeply carved into layered arches, recessed corridors, and structural reliefs with strong depth. "
    				"The structure has heavy volumetric presence, with clear mass distribution and architectural weight, not fragile or thin. "
    				"Strong contrast between deep green rind, pale inner rind, and vibrant red flesh enhances readability and separation. "
    				"Ultra high detail carving with deep cuts, strong edge definition, and clear structural layering. "
    				"The table surface is scattered with watermelon debris including rind chunks, seeds, and juice residue."
				),

				"Semangka: Grand Layered Architecture": (
    				"A hyper-realistic hand-carved mosque made from a whole watermelon, constructed as a large-scale tabletop structure around 1 meter in size with strong physical dominance. "
    				"The composition features a monumental central dome built from smooth exposed watermelon flesh, surrounded by multiple layered domes and thick minarets. "
    				"The architecture emphasizes strong vertical hierarchy and deep structural layering, creating a visually powerful mosque silhouette. "
    				"The outer rind is carved into thick architectural walls with deep recessed arches, multi-layer relief carvings, and heavy structural depth. "
    				"The form feels dense, grounded, and massive, with no thin or fragile elements. "
    				"Highly detailed geometric carving with strong shadow depth and surface contrast. "
    				"The table surface contains watermelon carving debris and natural residue."
				),

				"Buah Naga: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from a whole dragon fruit, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from dense white or pink flesh with visible black seeds, smooth and rounded, acting as the dominant focal mass. "
    				"Surrounding structures include layered domes and tall minarets carved from thick magenta rind, forming a strong architectural hierarchy. "
    				"The walls are deeply carved into heavy layered structures with recessed arches and thick geometry. "
    				"Strong contrast between vibrant rind and soft seeded flesh creates deep visual separation. "
    				"The structure feels massive, grounded, and architecturally solid with clear weight distribution. "
    				"The table is scattered with dragon fruit debris."
				),

				"Buah Naga: Grand Sacred Structure": (
    				"A large-scale mosque carved from dragon fruit, approximately 1 meter in size, with a monumental presence on a table surface. "
    				"A dominant central dome made from exposed fruit flesh with visible seeds rises above layered secondary domes. "
    				"The structure features tall minarets, deep carved arches, and multi-layered architectural surfaces. "
    				"The rind is carved thick and deep, avoiding thin or fragile forms. "
    				"The composition emphasizes strong verticality, depth, and mass. "
    				"Highly detailed carving with strong shadow contrast and tactile realism. "
    				"Natural fruit debris surrounds the base."
				),

				"Melon: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from a whole melon, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from smooth dense melon flesh, rounded and thick, acting as a strong focal structure. "
    				"Surrounding domes and minarets are carved from rind, forming a layered architectural system. "
    				"The structure is deeply carved with thick walls, recessed arches, and heavy geometry. "
    				"The composition feels massive and grounded with strong volumetric presence. "
    				"Clear contrast between outer rind and inner flesh enhances structure readability. "
    				"The table surface shows melon debris."
				),

				"Melon: Grand Layered Form": (
    				"A large-scale melon mosque approximately 1 meter in size, built with strong architectural layering and depth. "
    				"The central dome made from exposed melon flesh dominates the composition, supported by secondary domes and tall minarets. "
    				"The rind is carved into thick structural walls with deep recessed details and geometric patterns. "
    				"The structure emphasizes mass, balance, and clarity, avoiding fragile details. "
    				"Strong surface definition and realistic organic texture. "
    				"Natural melon debris surrounds the base."
				),
				
				"Labu: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from a whole pumpkin, built as a large tabletop monument approximately 1 meter in scale with strong physical presence. "
    				"The central dome is formed from dense bright orange pumpkin flesh, thick, smooth, and rounded with visible moist fiber texture, acting as the dominant focal mass. "
    				"Supporting domes and tall minarets are carved from the thick outer skin, forming a strong vertical architectural hierarchy. "
    				"The walls are deeply carved with heavy structural thickness, recessed arches, and layered reliefs. "
    				"The structure feels massive, grounded, and weighty with strong volumetric presence. "
    				"Clear contrast between deep orange flesh and darker outer skin enhances architectural readability. "
    				"The table surface is scattered with pumpkin debris and fiber strands."
				),

				"Labu: Grand Layered Architecture": (
    				"A large-scale pumpkin mosque approximately 1 meter in size, designed with a grand layered architectural composition. "
    				"A dominant central dome made from exposed pumpkin flesh rises above multiple layered domes and thick minarets. "
    				"The structure uses thick carved skin forming deep recessed arches and heavy structural surfaces. "
    				"The composition emphasizes strong depth, hierarchy, and architectural weight. "
    				"Highly detailed carving with strong shadow contrast and tactile realism. "
    				"Pumpkin debris is scattered across the table surface."
				),

				"Pepaya: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from a whole papaya, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from smooth orange papaya flesh, thick and rounded with visible moisture and soft organic texture. "
    				"Secondary domes and minarets are carved from the outer skin, creating a balanced architectural hierarchy. "
    				"The walls are deeply carved with layered arches and structural depth. "
    				"The structure feels solid and massive with strong volume. "
    				"Black seeds appear naturally in carved openings, adding contrast and realism. "
    				"The table surface contains papaya debris and seeds."
				),

				"Pepaya: Grand Sacred Form": (
    				"A large-scale papaya mosque around 1 meter in size, with a monumental layered structure. "
    				"The central dome made from exposed papaya flesh dominates the composition, surrounded by structured domes and tall minarets. "
    				"The outer skin is carved into thick architectural walls with deep recessed carvings. "
    				"Strong contrast between orange flesh, dark seeds, and outer skin enhances depth. "
    				"The structure emphasizes mass, clarity, and realism. "
    				"The table surface is scattered with papaya seeds and flesh residue."
				),

				"Pisang: Monumental Kubah Daging": (
    				"A hyper-realistic mosque constructed from banana fruit, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from compressed banana flesh shaped into a smooth rounded mass, dense and slightly fibrous, acting as the main focal structure. "
    				"The outer walls and minarets are formed from layered banana peel arranged into thick architectural forms. "
    				"The structure uses block-like banana segments forming clear geometric stacking. "
    				"The composition feels heavy, dense, and organic with visible compression and texture. "
    				"The table surface shows banana peel fragments and soft residue."
				),

				"Pisang: Layered Organic Monument": (
    				"A large-scale banana mosque approximately 1 meter in size, built with layered banana flesh blocks and peel structures. "
    				"The central dome made from dense banana flesh dominates the structure, surrounded by layered domes and vertical minarets. "
    				"The architecture emphasizes soft organic structure combined with clear geometric stacking. "
    				"The surface shows compression lines, fiber texture, and natural imperfections. "
    				"The table surface contains banana debris and peel remnants."
				),

				"Jeruk Orange: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from orange fruit, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from tightly packed orange segments shaped into a smooth rounded structure with visible citrus fiber and moisture. "
    				"The outer structure uses orange peel arranged in layered architectural surfaces. "
    				"Thick carved walls and arches create strong depth and structure. "
    				"Juice reflections and pulp detail enhance realism. "
    				"The structure feels dense and visually rich with strong contrast. "
    				"The table surface shows peel fragments and juice droplets."
				),

				"Jeruk Orange: Grand Citrus Architecture": (
    				"A large-scale orange mosque approximately 1 meter in size with a strong layered architectural composition. "
    				"The central dome made from citrus flesh dominates, surrounded by structured domes and minarets formed from peel. "
    				"The architecture emphasizes deep carving, strong layering, and heavy mass. "
    				"Bright color contrast enhances visual clarity. "
    				"The table surface contains orange debris and juice residue."
				),

				"Jeruk Hijau: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from green citrus fruit, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from pale green citrus flesh, smooth, dense, and moist, acting as the dominant structure. "
    				"The outer architecture uses green peel carved into thick walls and minarets. "
    				"The structure has strong depth with carved arches and layered surfaces. "
    				"Subtle color contrast between peel and flesh enhances realism. "
    				"The table surface shows citrus residue and peel fragments."
				),

				"Jeruk Hijau: Sacred Green Structure": (
    				"A large-scale lime mosque approximately 1 meter in size with strong architectural layering. "
    				"The central dome made from exposed citrus flesh dominates the composition. "
    				"The outer peel is carved into thick structural elements with deep detail. "
    				"The structure emphasizes clarity, balance, and strong volumetric presence. "
    				"The table surface contains citrus debris and moisture residue."
				),

				"Anggur: Monumental Kubah Daging": (
    				"A hyper-realistic mosque constructed from grape clusters, built as a large tabletop monument approximately 1 meter in scale with strong physical presence. "
    				"The central dome is formed from tightly packed grape flesh, creating a smooth rounded mass with subtle spherical texture and natural gloss. "
    				"The surrounding structure uses compressed grape clusters forming thick walls, domes, and vertical minarets with strong architectural hierarchy. "
    				"The composition emphasizes dense mass, organic curvature, and strong volumetric presence. "
    				"Juice reflections and translucent grape skin enhance realism and depth. "
    				"The structure feels heavy, cohesive, and visually rich. "
    				"The table surface is scattered with loose grapes and juice residue."
				),

				"Anggur: Grand Cluster Architecture": (
    				"A large-scale grape mosque approximately 1 meter in size, built using tightly arranged grape clusters forming a grand architectural composition. "
    				"The central dome made from compact grape flesh dominates the structure, surrounded by layered domes and vertical minarets. "
    				"The architecture emphasizes organic repetition, dense structure, and strong visual rhythm. "
    				"The surface shows natural gloss, translucency, and moisture. "
    				"The structure feels massive and cohesive. "
    				"The table surface contains grape debris and juice marks."
				),

				"Nanas: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from a whole pineapple, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from dense yellow pineapple flesh, thick and rounded with visible fiber texture and moisture. "
    				"The outer structure uses pineapple skin forming highly textured walls, domes, and tall minarets with strong vertical emphasis. "
    				"The walls are deeply carved with strong geometric patterns and layered structural depth. "
    				"The architecture feels bold, sharp, and massive. "
    				"Strong contrast between rough skin and soft inner flesh enhances readability. "
    				"The table surface is scattered with pineapple debris."
				),

				"Nanas: Grand Textured Architecture": (
    				"A large-scale pineapple mosque approximately 1 meter in size with a powerful architectural composition. "
    				"The central dome made from exposed pineapple flesh dominates, surrounded by layered domes and structured minarets. "
    				"The outer skin forms a sharp geometric texture across the entire structure. "
    				"The architecture emphasizes strong pattern repetition, depth, and mass. "
    				"The surface shows fiber detail and moisture variation. "
    				"The table surface contains pineapple fragments."
				),

				"Durian: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from a whole durian, built as a large tabletop monument approximately 1 meter in scale with strong visual impact. "
    				"The central dome is formed from thick creamy durian flesh, smooth and dense, creating a bold focal mass. "
    				"The outer shell forms spiked architectural walls, domes, and minarets, creating a highly textured and aggressive structure. "
    				"The composition emphasizes strong contrast between soft inner flesh and sharp outer shell. "
    				"The structure feels heavy, dramatic, and highly tactile. "
    				"The table surface is scattered with durian shell fragments."
				),

				"Durian: Grand Spiked Structure": (
    				"A large-scale durian mosque approximately 1 meter in size with a dramatic and monumental structure. "
    				"The central dome made from exposed durian flesh dominates the composition, surrounded by spiked architectural forms. "
    				"The outer shell is carved into thick structural elements with sharp geometric texture. "
    				"The architecture emphasizes contrast, depth, and strong presence. "
    				"The table surface contains durian debris and shell pieces."
				),

				"Kiwi: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from kiwi fruit, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from green kiwi flesh with visible black seeds radiating outward, creating a natural radial pattern. "
    				"The outer structure uses kiwi skin forming textured architectural surfaces and structural elements. "
    				"The walls are deeply carved with layered arches and strong depth. "
    				"The structure feels balanced, organic, and visually unique. "
    				"The table surface is scattered with kiwi residue and seeds."
				),

				"Kiwi: Radial Sacred Architecture": (
    				"A large-scale kiwi mosque approximately 1 meter in size with a strong radial visual identity. "
    				"The central dome made from exposed kiwi flesh dominates, with seed patterns creating a natural ornamental effect. "
    				"The outer structure is carved from skin into thick architectural forms. "
    				"The composition emphasizes symmetry, texture, and depth. "
    				"The table surface contains kiwi debris and moisture residue."
				),

				"Salak: Monumental Kubah Daging": (
    				"A hyper-realistic mosque constructed from salak fruit, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from dense pale salak flesh, smooth and solid, acting as the main focal structure. "
    				"The outer structure uses salak skin with natural scale-like texture forming walls, domes, and minarets. "
    				"The architecture emphasizes strong texture, layered surfaces, and structural clarity. "
    				"The structure feels grounded, dense, and tactile. "
    				"The table surface is scattered with salak peel fragments."
				),

				"Salak: Scaled Grand Structure": (
    				"A large-scale salak mosque approximately 1 meter in size with a bold textured architectural composition. "
    				"The central dome made from exposed salak flesh dominates the structure, surrounded by layered architectural elements. "
    				"The outer skin forms scale-like patterns across the structure, enhancing visual richness. "
    				"The architecture emphasizes texture, depth, and mass. "
    				"The table surface contains salak debris and peel residue."
				),
				
				"Kelapa: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from a whole coconut, built as a large tabletop monument approximately 1 meter in scale with strong architectural dominance. "
    				"The central dome is formed from dense white coconut flesh, thick, smooth, and solid, creating a bold and clean focal mass. "
    				"The outer structure uses coconut shell and fibrous husk forming thick walls, domes, and tall minarets with strong vertical emphasis. "
    				"The architecture features deeply carved structural layers, recessed arches, and heavy geometric forms. "
    				"The contrast between rough fibrous husk, hard shell, and smooth inner flesh enhances visual depth and realism. "
    				"The structure feels heavy, grounded, and monumental with strong volumetric presence. "
    				"The table surface is scattered with coconut fiber, shell fragments, and organic debris."
				),

				"Kelapa: Grand Tropical Architecture": (
    				"A large-scale coconut mosque approximately 1 meter in size with a powerful architectural composition. "
    				"The central dome made from exposed coconut flesh dominates the structure, surrounded by layered domes and tall minarets formed from shell and husk. "
    				"The structure emphasizes strong contrast between smooth inner surfaces and rough outer textures. "
    				"The walls are carved thick with deep architectural recesses and layered details. "
    				"The composition feels massive, balanced, and highly tactile. "
    				"The table surface contains coconut debris and husk fibers."
				),

				"Jagung: Monumental Kubah Daging": (
    				"A hyper-realistic mosque constructed from corn, built as a large tabletop monument approximately 1 meter in scale with strong visual impact. "
    				"The central dome is formed from densely packed yellow corn kernels arranged into a smooth rounded structure, creating a cohesive and textured mass. "
    				"The outer walls and minarets are formed from stacked corn cobs and layered kernels, forming thick architectural structures. "
    				"The architecture emphasizes repetition, density, and strong geometric stacking. "
    				"The surface shows rich granular texture with natural gloss and variation. "
    				"The structure feels dense, structured, and monumental. "
    				"The table surface is scattered with loose corn kernels."
				),

				"Jagung: Grand Modular Structure": (
    				"A large-scale corn mosque approximately 1 meter in size with a modular architectural composition. "
    				"The central dome made from compact corn kernels dominates, surrounded by layered domes and strong vertical minarets. "
    				"The structure uses stacked corn cobs and dense kernel arrangements forming thick walls and arches. "
    				"The architecture emphasizes repetition, depth, and strong structural clarity. "
    				"The surface is highly detailed with granular texture. "
    				"The table surface contains corn debris and loose kernels."
				),

				"Sirsak: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from a whole soursop fruit, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from dense white soursop flesh, smooth yet slightly fibrous, creating a soft but massive focal structure. "
    				"The outer skin with natural spiky texture forms architectural walls, domes, and minarets. "
    				"The structure features deep carved layers, recessed arches, and strong structural thickness. "
    				"The contrast between soft flesh and textured outer skin creates strong visual depth. "
    				"The architecture feels organic yet monumental with clear mass distribution. "
    				"The table surface is scattered with soursop seeds and residue."
				),

				"Sirsak: Organic Grand Structure": (
    				"A large-scale soursop mosque approximately 1 meter in size with a strong organic architectural form. "
    				"The central dome made from exposed soursop flesh dominates the composition, surrounded by layered structures and vertical elements. "
    				"The outer skin forms textured structural surfaces with natural spikes and irregular patterns. "
    				"The architecture emphasizes organic depth, texture, and volumetric presence. "
    				"The table surface contains soursop debris and seeds."
				),

				"Tomat: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from tomato fruit, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from dense tomato flesh, smooth, glossy, and rounded, acting as a strong visual focal point. "
    				"The outer structure uses tomato skin forming clean architectural surfaces with subtle natural curvature. "
    				"The walls are thick and deeply carved with clear structural layering and recessed arches. "
    				"The glossy surface reflects light, enhancing realism and depth. "
    				"The structure feels solid, vibrant, and monumental despite its softness. "
    				"The table surface is scattered with tomato seeds and juice residue."
				),

				"Tomat: Grand Smooth Architecture": (
    				"A large-scale tomato mosque approximately 1 meter in size with a clean and bold architectural composition. "
    				"The central dome made from exposed tomato flesh dominates the structure, surrounded by layered domes and vertical minarets. "
    				"The architecture emphasizes smooth surfaces, strong geometry, and clear structure. "
    				"The surface shows natural gloss and moisture. "
    				"The structure feels dense and visually striking. "
    				"The table surface contains tomato residue and seeds."
				),
				
				"Cherry: Monumental Kubah Daging": (
    				"A hyper-realistic mosque constructed from cherry fruit, built as a large tabletop monument approximately 1 meter in scale with strong visual presence. "
    				"The central dome is formed from densely compressed cherry flesh, smooth, rounded, and glossy, creating a rich and reflective focal mass. "
    				"The outer structure uses tightly packed cherries forming thick architectural walls, domes, and vertical minarets with strong hierarchy. "
    				"The composition emphasizes dense clustering, repetition, and cohesive mass. "
    				"The glossy surface reflects light, enhancing depth and realism. "
    				"The structure feels compact, dense, and monumental. "
    				"The table surface is scattered with cherry stems and juice residue."
				),

				"Cherry: Grand Cluster Architecture": (
    				"A large-scale cherry mosque approximately 1 meter in size with a dense and cohesive architectural structure. "
    				"The central dome made from compact cherry flesh dominates the composition, surrounded by layered domes and structured minarets. "
    				"The outer surface is formed from clustered cherries creating a unique organic pattern. "
    				"The architecture emphasizes repetition, density, and strong volumetric presence. "
    				"The surface shows gloss, translucency, and natural variation. "
    				"The table surface contains cherry debris and stems."
				),

				"Mangga: Monumental Kubah Daging": (
    				"A hyper-realistic mosque carved from a whole mango, built as a large tabletop monument approximately 1 meter in scale with strong architectural presence. "
    				"The central dome is formed from dense mango flesh, smooth, thick, and slightly moist, creating a bold rounded focal structure. "
    				"The outer structure uses mango skin forming thick walls, domes, and vertical minarets with strong hierarchy. "
    				"The walls are deeply carved with layered arches and heavy structural depth. "
    				"The contrast between vibrant skin and soft inner flesh enhances readability. "
    				"The structure feels grounded, solid, and monumental. "
    				"The table surface is scattered with mango residue and peel fragments."
				),

				"Mangga: Grand Smooth Structure": (
    				"A large-scale mango mosque approximately 1 meter in size with a clean and powerful architectural composition. "
    				"The central dome made from exposed mango flesh dominates the structure, surrounded by layered domes and tall minarets. "
    				"The outer skin is carved into thick architectural surfaces with deep recessed details. "
    				"The structure emphasizes smooth surfaces, strong geometry, and volumetric mass. "
    				"The table surface contains mango debris and moisture residue."
				),

				"Cabe: Monumental Kubah Daging": (
    				"A hyper-realistic mosque constructed from red chili peppers, built as a large tabletop monument approximately 1 meter in scale with strong visual impact. "
    				"The central dome is formed from densely compressed chili flesh, shaped into a smooth rounded mass with vibrant red color and glossy surface. "
    				"The outer structure uses layered chili skins forming thick architectural walls and tall slender minarets with dramatic vertical emphasis. "
    				"The structure emphasizes curvature, repetition, and bold color contrast. "
    				"The glossy surface enhances light reflection and depth. "
    				"The architecture feels dynamic yet grounded with strong presence. "
    				"The table surface is scattered with chili seeds and fragments."
				),

				"Cabe: Grand Organic Flame Structure": (
    				"A large-scale chili mosque approximately 1 meter in size with a dramatic and dynamic architectural composition. "
    				"The central dome made from compressed chili flesh dominates the structure, surrounded by flowing layered structures and tall minarets. "
    				"The curved chili forms create organic flowing architecture while maintaining structural clarity. "
    				"The structure emphasizes bold color, movement, and strong volumetric presence. "
    				"The table surface contains chili debris and seeds."
				),
				
				"Pisang: MIX Monumental Kubah Daun": (
    				"A hyper-realistic mosque constructed from bananas and banana leaves, built as a large tabletop monument approximately 1 meter in scale with strong physical dominance. "
    				"The central dome is massive and fully formed from thick layered banana leaves, shaped into a smooth, wide, and dominant curved structure with visible veins and natural leaf texture. "
    				"The main architecture is built from large banana fruit blocks, stacked and carved into thick structural walls, deep arches, and strong geometric forms. "
    				"Multiple secondary domes made from layered leaves surround the main dome, creating clear architectural hierarchy. "
    				"Tall symmetrical minarets rise from dense banana structures, giving strong vertical presence. "
    				"The composition feels heavy, grounded, and monumental with clear volumetric mass. "
    				"Strong contrast between deep green leaf domes and yellow fruit structure enhances clarity and depth. "
    				"The wooden table surface is scattered with banana debris: fruit chunks, peel strips, and torn leaf fragments."
				),

				"Pisang: MIX Grand Layered Architecture": (
    				"A large-scale banana mosque approximately 1 meter in size, designed with a grand layered architectural composition. "
    				"A dominant oversized central dome made from folded and layered banana leaves rises above multiple leaf domes and structured banana minarets. "
    				"The banana fruit forms thick structural walls with deep carving, recessed arches, and heavy geometry. "
    				"The architecture emphasizes strong layering, depth, and mass, avoiding thin or fragile forms. "
    				"The structure feels dense, monumental, and architecturally clear. "
    				"The table surface contains banana debris and leaf fragments."
				),

				"Kelapa: MIX Monumental Kubah Daun": (
    				"A hyper-realistic mosque constructed from coconut materials and woven janur leaves, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is massive and fully formed from tightly woven janur leaves, thick and rounded with intricate natural patterns and strong structural presence. "
    				"The main architecture is built from coconut shell and dense inner flesh, forming thick walls, layered arches, and heavy structural mass. "
    				"Secondary domes made from layered leaf weaving surround the main dome, creating strong hierarchy. "
    				"Tall minarets rise from coconut shell structures with strong vertical emphasis. "
    				"The structure feels grounded, dense, and monumental with strong contrast between rough shell and smooth woven leaves. "
    				"The table surface is scattered with coconut debris and leaf fragments."
				),

				"Kelapa: MIX Grand Woven Architecture": (
    				"A large-scale coconut mosque approximately 1 meter in size with a grand architectural composition. "
    				"The central dome made from layered woven janur leaves dominates the structure, surrounded by multiple domes and vertical minarets. "
    				"The coconut shell forms thick structural walls with deep carving and strong geometric depth. "
    				"The woven leaf surfaces create intricate layered patterns with strong visual richness. "
    				"The structure emphasizes depth, hierarchy, and architectural mass. "
    				"The table surface contains coconut debris and woven leaf fragments."
				),
				
				"Kacang Ijo + Daun: MIX Monumental Kubah Daun": (
    				"A hyper-realistic mosque constructed from mung beans and broad green leaves, built as a large tabletop monument approximately 1 meter in scale with strong physical presence. "
    				"The central dome is massive and fully formed from thick layered green leaves, shaped into a smooth and dominant curved structure with visible veins and natural texture. "
    				"The main architecture is constructed from densely packed mung beans, forming thick structural walls, deep recessed arches, and strong geometric mass. "
    				"The beans are tightly arranged into cohesive surfaces, creating a granular yet solid architectural appearance. "
    				"Multiple secondary domes made from layered leaves surround the main dome, creating clear hierarchy. "
    				"Tall symmetrical minarets rise from compact mung bean structures, emphasizing strong vertical form. "
    				"The structure feels dense, grounded, and monumental with strong volumetric presence. "
    				"The table surface is scattered with mung bean debris and torn leaf fragments."
				),

				"Kacang Ijo + Daun: MIX Grand Dense Structure": (
    				"A large-scale mosque constructed from mung beans and leaves, approximately 1 meter in size, with a grand architectural composition. "
    				"The central dome made from layered leaves dominates the structure, wide and smooth with strong curvature. "
    				"The walls and structural elements are built from densely packed mung beans forming thick, heavy surfaces and deep architectural carvings. "
    				"The architecture emphasizes density, repetition, and strong structural clarity. "
    				"The combination of smooth leaf domes and granular bean surfaces creates strong contrast and depth. "
    				"The structure feels massive and architecturally clear. "
    				"The table surface contains mung bean debris and leaf fragments."
				),

				"Kedelai + Daun: MIX Monumental Kubah Daun": (
    				"A hyper-realistic mosque constructed from soybeans and large green leaves, built as a large tabletop monument approximately 1 meter in scale with strong visual dominance. "
    				"The central dome is formed from thick layered leaves, smooth, wide, and dominant with visible organic vein patterns. "
    				"The main structure is built from tightly packed soybeans forming thick walls, domes, and architectural surfaces with granular texture. "
    				"The soybeans create a dense, cohesive mass with subtle color variation and natural matte finish. "
    				"Secondary domes made from layered leaves surround the main dome, forming strong architectural hierarchy. "
    				"Tall minarets rise from compact soybean structures, emphasizing vertical strength. "
    				"The structure feels heavy, grounded, and monumental with strong volumetric mass. "
    				"The table surface is scattered with soybean debris and leaf fragments."
				),

				"Kedelai + Daun: MIX Grand Modular Architecture": (
    				"A large-scale mosque constructed from soybeans and leaves, approximately 1 meter in size with a strong architectural composition. "
    				"The central dome made from layered leaves dominates the structure with smooth curvature and organic flow. "
    				"The structural walls are built from densely arranged soybeans forming thick modular surfaces and deep carved details. "
    				"The architecture emphasizes repetition, density, and clear structural hierarchy. "
    				"The contrast between smooth leaf domes and textured soybean surfaces enhances visual clarity. "
    				"The structure feels solid, massive, and architecturally defined. "
    				"The table surface contains soybean debris and leaf fragments."
				),

				"Semangka + Nanas: Monumental Hybrid Structure": (
    				"A hyper-realistic mosque constructed from watermelon and pineapple, built as a large tabletop monument approximately 1 meter in scale with strong architectural dominance. "
    				"The central dome is formed from dense watermelon flesh, smooth, thick, and rounded with visible moist texture, acting as the main focal mass. "
    				"The structural walls and minarets are built from pineapple, using its rough textured skin and dense flesh to create strong geometric forms and vertical elements. "
    				"The architecture emphasizes contrast between smooth red dome and highly textured yellow-brown structure. "
    				"Deep carved arches and layered surfaces create strong depth and hierarchy. "
    				"The structure feels massive, grounded, and architecturally clear. "
    				"The table surface is scattered with watermelon and pineapple debris."
				),

				"Semangka + Nanas: Grand Contrast Architecture": (
    				"A large-scale mosque constructed from watermelon and pineapple, approximately 1 meter in size with a bold architectural composition. "
    				"The central dome made from exposed watermelon flesh dominates the structure, surrounded by layered pineapple-based walls and tall minarets. "
    				"The architecture emphasizes strong contrast, deep texture, and structural layering. "
    				"The pineapple forms thick architectural surfaces with carved depth, while watermelon provides smooth volumetric mass. "
    				"The structure feels dense, heavy, and visually striking. "
    				"The table surface contains fruit debris."
				),

				"Mangga + Jeruk: Monumental Citrus Blend": (
    				"A hyper-realistic mosque constructed from mango and orange, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from smooth dense mango flesh, thick and rounded with rich color and slight moisture. "
    				"The outer structure uses orange segments and peel forming layered architectural surfaces with strong texture and detail. "
    				"The contrast between smooth mango dome and segmented citrus structure enhances visual clarity. "
    				"The walls are thick and deeply carved with strong structural definition. "
    				"The architecture feels cohesive, vibrant, and monumental. "
    				"The table surface is scattered with mango and orange debris."
				),

				"Mangga + Jeruk: Grand Citrus Architecture": (
    				"A large-scale mosque constructed from mango and orange, approximately 1 meter in size with a strong architectural presence. "
    				"The central dome made from mango flesh dominates the composition, supported by citrus-based structural elements and tall minarets. "
    				"The architecture emphasizes bright contrast, layering, and volumetric mass. "
    				"The citrus textures add fine detail and depth, while mango provides solid smooth form. "
    				"The structure feels bold, clean, and architecturally strong. "
    				"The table surface contains fruit residue and peel fragments."
				),

				"Pepaya + Kiwi: Monumental Organic Contrast": (
    				"A hyper-realistic mosque constructed from papaya and kiwi, built as a large tabletop monument approximately 1 meter in scale with strong organic visual identity. "
    				"The central dome is formed from dense papaya flesh, smooth and thick with soft orange tone and visible moisture. "
    				"The outer structure uses kiwi flesh and skin, forming layered architectural surfaces with radial seed patterns and natural texture. "
    				"The contrast between smooth papaya dome and detailed kiwi structure creates strong visual interest. "
    				"The walls are thick and deeply carved with strong structural clarity. "
    				"The structure feels organic yet monumental. "
    				"The table surface is scattered with papaya and kiwi debris."
				),

				"Pepaya + Kiwi: Grand Radial Architecture": (
    				"A large-scale mosque constructed from papaya and kiwi, approximately 1 meter in size with a unique radial architectural composition. "
    				"The central dome made from papaya flesh dominates, while kiwi elements form detailed structural layers and decorative surfaces. "
    				"The architecture emphasizes organic texture, contrast, and depth. "
    				"The kiwi seeds create intricate visual patterns, enhancing realism and structure. "
    				"The structure feels dense, artistic, and architecturally clear. "
    				"The table surface contains fruit debris and seeds."
				),

				"Anggur + Cherry: Monumental Cluster Structure": (
    				"A hyper-realistic mosque constructed from grapes and cherries, built as a large tabletop monument approximately 1 meter in scale with strong visual density. "
    				"The central dome is formed from compressed grape flesh, smooth and rounded with natural gloss and translucency. "
    				"The outer structure uses tightly packed cherry clusters forming thick walls, domes, and vertical minarets. "
    				"The architecture emphasizes repetition, density, and cohesive cluster formation. "
    				"The glossy surfaces enhance light reflection and depth. "
    				"The structure feels compact, dense, and monumental. "
    				"The table surface is scattered with stems and fruit debris."
				),

				"Anggur + Cherry: Grand Glossy Architecture": (
    				"A large-scale mosque constructed from grapes and cherries, approximately 1 meter in size with a dense architectural composition. "
    				"The central dome made from grape flesh dominates, while cherry clusters form structured architectural layers. "
    				"The architecture emphasizes glossy surfaces, repetition, and volumetric density. "
    				"The structure feels cohesive, rich, and visually striking. "
    				"The table surface contains fruit residue and stems."
				),

				"Durian + Nanas: Monumental Extreme Texture": (
    				"A hyper-realistic mosque constructed from durian and pineapple, built as a large tabletop monument approximately 1 meter in scale with dramatic visual impact. "
    				"The central dome is formed from thick creamy durian flesh, smooth and dense, creating a strong focal structure. "
    				"The outer structure uses pineapple skin forming sharp geometric surfaces and structural elements. "
    				"The architecture emphasizes extreme texture contrast between soft creamy dome and rough spiked exterior. "
    				"The walls are thick, deeply carved, and highly detailed. "
    				"The structure feels heavy, aggressive, and monumental. "
    				"The table surface is scattered with durian and pineapple debris."
				),

				"Durian + Nanas: Grand Spiked Architecture": (
    				"A large-scale mosque constructed from durian and pineapple, approximately 1 meter in size with a bold architectural composition. "
    				"The central dome made from durian flesh dominates the structure, surrounded by spiked and textured architectural forms. "
    				"The pineapple skin creates strong geometric patterns and depth. "
    				"The architecture emphasizes contrast, layering, and strong volumetric mass. "
    				"The structure feels dramatic and architecturally powerful. "
    				"The table surface contains fruit debris."
				),
				"Labu + Kelapa: Monumental Tropical Structure": (
    				"A hyper-realistic mosque constructed from pumpkin and coconut, built as a large tabletop monument approximately 1 meter in scale with strong architectural mass. "
    				"The central dome is formed from dense pumpkin flesh, smooth, thick, and rounded with visible fiber texture, acting as the dominant focal structure. "
    				"The outer structure uses coconut shell and inner flesh forming thick walls, domes, and tall minarets with strong vertical emphasis. "
    				"The architecture emphasizes contrast between smooth orange dome and rough fibrous coconut surfaces. "
    				"Deep carved arches and layered structural surfaces create strong depth and clarity. "
    				"The structure feels heavy, grounded, and monumental. "
    				"The table surface is scattered with pumpkin and coconut debris."
				),

				"Labu + Kelapa: Grand Rustic Architecture": (
    				"A large-scale mosque constructed from pumpkin and coconut, approximately 1 meter in size with a strong architectural composition. "
    				"The central dome made from pumpkin flesh dominates, surrounded by coconut-based structural walls and vertical minarets. "
    				"The architecture emphasizes rustic texture, strong layering, and volumetric mass. "
    				"The contrast between soft flesh and rough shell enhances realism. "
    				"The structure feels dense and architecturally solid. "
    				"The table surface contains fruit debris and shell fragments."
				),

				"Semangka + Pepaya: Monumental Soft Contrast": (
    				"A hyper-realistic mosque constructed from watermelon and papaya, built as a large tabletop monument approximately 1 meter in scale. "
    				"The central dome is formed from dense papaya flesh, smooth and thick with rich orange tone and visible moisture. "
    				"The outer structure uses watermelon rind and inner layers forming thick walls, arches, and structural mass. "
    				"The architecture emphasizes contrast between smooth dome and layered rind surfaces. "
    				"The structure feels balanced, dense, and monumental. "
    				"The table surface is scattered with watermelon and papaya debris."
				),

				"Semangka + Pepaya: Grand Dual Tone Architecture": (
    				"A large-scale mosque constructed from watermelon and papaya, approximately 1 meter in size with a strong dual-tone architectural composition. "
    				"The central dome made from papaya flesh dominates, supported by watermelon-based structural elements and minarets. "
    				"The architecture emphasizes color contrast, structural layering, and strong volumetric presence. "
    				"The structure feels bold and architecturally clear. "
    				"The table surface contains fruit residue."
				),

				"Jeruk + Kiwi: Monumental Citrus Fusion": (
    				"A hyper-realistic mosque constructed from orange and kiwi, built as a large tabletop monument approximately 1 meter in scale with strong visual identity. "
    				"The central dome is formed from dense orange flesh, smooth and rounded with visible citrus fibers and moisture. "
    				"The outer structure uses kiwi flesh and skin forming layered architectural surfaces with radial seed patterns and organic texture. "
    				"The architecture emphasizes contrast between smooth citrus dome and detailed kiwi structure. "
    				"The structure feels vibrant, dense, and monumental. "
    				"The table surface is scattered with fruit debris and seeds."
				),

				"Jeruk + Kiwi: Grand Radial Citrus Architecture": (
    				"A large-scale mosque constructed from orange and kiwi, approximately 1 meter in size with a strong radial and layered composition. "
    				"The central dome made from orange flesh dominates, while kiwi forms intricate structural surfaces. "
    				"The architecture emphasizes detail, texture, and volumetric depth. "
    				"The structure feels visually rich and architecturally clear. "
    				"The table surface contains citrus and kiwi residue."
				),

				"Pisang + Mangga: Monumental Soft Structure": (
    				"A hyper-realistic mosque constructed from banana and mango, built as a large tabletop monument approximately 1 meter in scale with strong structural mass. "
    				"The central dome is formed from dense mango flesh, smooth, thick, and rounded with slight moisture. "
    				"The outer structure uses banana flesh and peel forming layered architectural surfaces and vertical minarets. "
    				"The architecture emphasizes soft organic forms combined with clear geometric stacking. "
    				"The structure feels dense, grounded, and monumental. "
    				"The table surface is scattered with banana and mango debris."
				),

				"Pisang + Mangga: Grand Organic Architecture": (
    				"A large-scale mosque constructed from banana and mango, approximately 1 meter in size with a smooth and layered architectural composition. "
    				"The central dome made from mango flesh dominates, supported by banana-based structural elements and layered forms. "
    				"The architecture emphasizes soft texture, layering, and volumetric mass. "
    				"The structure feels organic yet architecturally strong. "
    				"The table surface contains fruit residue."
				),

				"Tomat + Cherry: Monumental Glossy Structure": (
    				"A hyper-realistic mosque constructed from tomato and cherry, built as a large tabletop monument approximately 1 meter in scale with strong glossy visual presence. "
    				"The central dome is formed from dense tomato flesh, smooth, rounded, and reflective with visible moisture. "
    				"The outer structure uses tightly packed cherries forming thick architectural walls and domes. "
    				"The architecture emphasizes glossy surfaces, repetition, and cohesive structure. "
    				"The structure feels compact, dense, and visually striking. "
    				"The table surface is scattered with seeds and stems."
				),

				"Tomat + Cherry: Grand Reflective Architecture": (
    				"A large-scale mosque constructed from tomato and cherry, approximately 1 meter in size with a reflective and dense architectural composition. "
    				"The central dome made from tomato flesh dominates, surrounded by cherry-based structural layers. "
    				"The architecture emphasizes gloss, repetition, and volumetric density. "
    				"The structure feels cohesive and architecturally bold. "
    				"The table surface contains fruit residue."
				),

				"Salak + Kelapa: Monumental Textured Structure": (
    				"A hyper-realistic mosque constructed from salak and coconut, built as a large tabletop monument approximately 1 meter in scale with strong tactile presence. "
    				"The central dome is formed from dense coconut flesh, smooth and solid, acting as the main focal mass. "
    				"The outer structure uses salak skin with scale-like texture forming thick architectural surfaces and minarets. "
    				"The architecture emphasizes strong texture contrast and structural clarity. "
    				"The structure feels grounded, dense, and monumental. "
    				"The table surface is scattered with peel and shell fragments."
				),

				"Salak + Kelapa: Grand Scaled Architecture": (
    				"A large-scale mosque constructed from salak and coconut, approximately 1 meter in size with a bold textured architectural composition. "
    				"The central dome made from coconut flesh dominates, surrounded by layered salak-based structural elements. "
    				"The architecture emphasizes scale-like texture, depth, and volumetric mass. "
    				"The structure feels heavy and architecturally strong. "
    				"The table surface contains debris and shell residue."
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
				),

				"Semangka: Susun Struktur Monumental": (
    				"A hyper-realistic mosque constructed from multiple watermelon components, built as a large tabletop monument approximately 1 meter in scale with strong architectural dominance, firmly resting on a wooden table surface. "
    				"The structure features a grand central dome, supporting domes, and tall symmetrical minarets with clear hierarchical proportions. "
    				"Each architectural section is formed from thick watermelon segments, creating a strong sense of structural mass and layered assembly. "
    				"The walls are heavy and deeply constructed, not thin or fragile, with visible joints and interlocking sections. "
    				"Dark green rind panels act as structural outer surfaces, while deep red flesh appears in controlled sections for contrast. "
    				"The structure feels dense, grounded, and monumental with strong volumetric presence. "
    				"The table surface is scattered with watermelon debris: rind fragments, flesh pieces, seeds, and subtle juice residue."
				),

				"Semangka: Craftsmanship Monumental": (
    				"A hyper-realistic mosque constructed from hand-cut watermelon pieces, built as a large-scale structure approximately 1 meter in size with strong physical presence on a wooden table. "
    				"The architecture follows a grand mosque layout with a dominant central dome and tall minarets. "
    				"Each element shows visible craftsmanship with knife marks, uneven cuts, and natural imperfections, but forms a thick and heavy structural mass. "
    				"The walls are not thin but deeply layered, reinforcing architectural weight. "
    				"Rind and flesh create controlled contrast with strong surface depth. "
    				"The structure feels solid, grounded, and monumental. "
    				"The table surface contains irregular watermelon debris."
				),

				"Semangka: Gaya Lego Monumental": (
    				"A hyper-realistic mosque constructed from modular watermelon blocks, built as a large tabletop monument approximately 1 meter in scale with strong structural clarity. "
    				"The architecture features a dominant central dome and structured minarets built from repeated thick geometric blocks. "
    				"Each block is large and dense, forming heavy walls and strong architectural mass rather than small decorative pieces. "
    				"The structure emphasizes clear stacking, strong alignment, and volumetric presence. "
    				"Dark rind and red flesh create bold geometric contrast. "
    				"The structure feels dense, stable, and monumental. "
    				"The table surface shows cut cube fragments, seeds, and juice residue."
				),
				
				"Nanas: Susun Struktur Monumental": (
					"A hyper-realistic mosque constructed from pineapple segments, built as a large tabletop monument approximately 1 meter in scale with strong architectural dominance. "
					"The structure features a massive central dome, supporting domes, and tall minarets with clear hierarchy. "
					"Pineapple skin forms thick structural walls, deeply carved with strong geometric depth and layered surfaces. "
					"The architecture feels heavy, grounded, and volumetric, not thin or fragile. "
					"Strong contrast between textured skin and fibrous flesh enhances realism. "
					"The table surface contains pineapple debris and fibers."
				),

				"Nanas: Craftsmanship Monumental": (
					"A hyper-realistic mosque constructed from hand-cut pineapple pieces, built as a large-scale architectural structure approximately 1 meter in size. "
					"The structure follows a grand mosque form with a dominant dome and tall minarets. "
					"Each piece shows real craftsmanship with knife marks and imperfections, but forms a thick and heavy structural composition. "
					"The walls are dense and deeply layered, creating strong architectural presence. "
					"The structure feels bold, textured, and monumental. "
					"The table surface contains pineapple debris."
				),

				"Nanas: Gaya Lego Monumental": (
					"A hyper-realistic mosque constructed from modular pineapple blocks, built as a large tabletop monument approximately 1 meter in scale. "
					"Large geometric pineapple segments form thick structural walls, domes, and minarets with strong alignment. "
					"The architecture emphasizes repetition, density, and structural clarity. "
					"The structure feels massive and architecturally solid. "
					"The table surface shows pineapple cube debris and fibers."
				),
				
				"Melon: Massive Assembled Architecture": (
    				"A hyper-realistic mosque constructed from large melon segments, built as a massive tabletop structure approximately 1 meter in scale with strong architectural dominance and physical weight. "
    				"The central dome is formed from thick solid melon flesh, carved into a large smooth hemispherical mass with visible dense texture and subtle moisture. "
    				"The structure is assembled using large block-like melon sections, forming heavy layered walls, deep recessed corridors, and multi-tier architectural levels. "
    				"Supporting domes and minarets are built from stacked melon structures, emphasizing strong vertical hierarchy and mass distribution. "
    				"The architecture focuses on heavy construction logic, with visible seams, interlocking parts, and structural thickness. "
    				"The overall form feels dense, grounded, and monumental with clear volumetric weight. "
    				"The table surface is scattered with large melon chunks, rind pieces, and moist residue."
				),

				"Jeruk: Massive Segmented Architecture": (
    				"A hyper-realistic mosque constructed from orange fruit segments, built as a large-scale tabletop monument approximately 1 meter in size with strong visual mass and density. "
    				"The central dome is formed from tightly compressed orange flesh, shaped into a thick rounded mass with visible citrus fibers and moisture. "
    				"The structure uses layered orange segments arranged into thick walls, deep arches, and tiered architectural levels, creating a segmented yet cohesive construction. "
    				"Peel elements reinforce structural edges and vertical minarets, adding contrast and rigidity. "
    				"The architecture emphasizes modular stacking, density, and strong structural clarity. "
    				"The form feels compact, heavy, and monumental with strong surface definition. "
    				"The table surface contains orange segments, peel fragments, and juice traces."
				),

				"Pisang: Compressed Mass Architecture": (
    				"A hyper-realistic mosque constructed from compressed banana flesh and peel, built as a large tabletop structure approximately 1 meter in scale with strong physical presence and architectural mass. "
    				"The central dome is formed from densely compressed banana flesh, shaped into a large smooth rounded form with visible fiber compression and organic texture. "
    				"The structure is built using stacked banana blocks and layered peel, forming thick architectural walls, deep structural cuts, and heavy volumetric forms. "
    				"The architecture emphasizes compression, density, and soft organic mass shaped into strong geometric structure. "
    				"Minarets rise from dense banana stacks, maintaining vertical clarity. "
    				"The structure feels heavy, grounded, and cohesive despite the soft material. "
    				"The table surface shows banana fragments, peel strips, and compressed residue."
				),

				"Labu: Heavy Carved Block Architecture": (
    				"A hyper-realistic mosque constructed from large pumpkin sections, built as a massive tabletop monument approximately 1 meter in scale with strong architectural weight and presence. "
    				"The central dome is formed from thick pumpkin flesh, carved into a large smooth dome with visible dense fiber texture and rich orange tone. "
    				"The structure is assembled from large carved pumpkin blocks, forming thick walls, deep recessed arches, and multi-layer architectural tiers. "
    				"The outer skin is used as structural panels, creating strong contrast and reinforcing edges. "
    				"The architecture emphasizes heavy carving, block construction, and strong volumetric mass. "
    				"The structure feels dense, bold, and monumental with clear architectural hierarchy. "
    				"The table surface is scattered with pumpkin chunks, fibers, and carved fragments."
				),

				"Mangga: Layered Mass Architecture": (
    				"A hyper-realistic mosque constructed from mango fruit, built as a large tabletop structure approximately 1 meter in scale with strong architectural mass and presence. "
    				"The central dome is formed from dense mango flesh, thick, smooth, and rounded, creating a bold and dominant focal structure with subtle moisture and rich color. "
    				"The structure is assembled from large mango blocks stacked into multi-layer architectural tiers, forming deep walls, elevated platforms, and recessed corridors. "
    				"The outer skin reinforces structural edges, creating contrast and clarity between layers. "
    				"The architecture emphasizes vertical stacking, depth, and heavy volumetric mass. "
    				"The structure feels dense, grounded, and monumental. "
    				"The table surface is scattered with mango chunks, peel fragments, and soft residue."
				),

				"Apel: Dense Structural Stack": (
    				"A hyper-realistic mosque constructed from apple fruit, built as a massive tabletop monument approximately 1 meter in scale with strong structural presence. "
    				"The central dome is formed from compact apple flesh, smooth, thick, and slightly glossy, creating a solid hemispherical mass. "
    				"The structure uses large apple segments stacked into thick architectural layers, forming strong walls, deep arches, and multi-level geometry. "
    				"The outer skin creates defined edges and visual separation between structural sections. "
    				"The architecture emphasizes density, symmetry, and strong geometric stacking. "
    				"The structure feels compact, heavy, and architecturally clear. "
    				"The table surface contains apple fragments, seeds, and juice traces."
				),

				"Tomat: Fluid Mass Architecture": (
    				"A hyper-realistic mosque constructed from tomato fruit, built as a large tabletop structure approximately 1 meter in scale with strong visual dominance. "
    				"The central dome is formed from dense tomato flesh, smooth, glossy, and rounded, reflecting light and creating a vivid focal structure. "
    				"The architecture is assembled from thick tomato segments forming layered structural mass, deep recessed forms, and curved architectural transitions. "
    				"The soft material is shaped into strong geometric forms, balancing fluid organic surfaces with architectural clarity. "
    				"The structure emphasizes smooth curvature, density, and volumetric presence. "
    				"The structure feels bold, vibrant, and monumental. "
    				"The table surface is scattered with seeds and juice residue."
				),

				"Durian: Heavy Core Architecture": (
    				"A hyper-realistic mosque constructed from durian fruit, built as a massive tabletop monument approximately 1 meter in scale with strong architectural weight. "
    				"The central dome is formed from thick creamy durian flesh, dense and smooth, creating a powerful central mass. "
    				"The structure is built from large durian segments with the outer shell forming thick spiked architectural walls and vertical structures. "
    				"The architecture emphasizes extreme contrast between soft inner core and aggressive outer shell texture. "
    				"Multiple structural layers create depth, hierarchy, and strong volumetric mass. "
    				"The structure feels heavy, bold, and dramatically monumental. "
    				"The table surface is scattered with shell fragments and organic debris."
				),

				"Anggur: Cluster Mass Architecture": (
    				"A hyper-realistic mosque constructed from grape clusters, built as a large tabletop monument approximately 1 meter in scale with strong density and cohesion. "
    				"The central dome is formed from compressed grape flesh, smooth and rounded with subtle translucency and natural gloss. "
    				"The structure uses tightly packed grape clusters forming thick architectural mass, layered walls, and vertical minarets. "
    				"The architecture emphasizes repetition, clustering, and cohesive structural density. "
    				"The form feels compact, heavy, and visually rich with organic pattern flow. "
    				"The structure maintains strong architectural clarity despite organic material. "
    				"The table surface is scattered with loose grapes and stems."
				),

				"Buah Naga: Organic Hybrid Architecture": (
    				"A hyper-realistic mosque constructed from dragon fruit, built as a large tabletop structure approximately 1 meter in scale with strong architectural presence. "
    				"The central dome is formed from dense dragon fruit flesh, smooth and rounded with visible black seeds embedded throughout, creating a unique textured mass. "
    				"The structure blends organic curvature with architectural layering, forming thick walls, flowing arches, and multi-level forms. "
    				"The outer skin adds contrast with bold magenta tones and natural irregularity. "
    				"The architecture emphasizes organic flow combined with heavy structural mass. "
    				"The structure feels dense, grounded, and visually striking. "
    				"The table surface is scattered with fruit debris and seeds."
				),

				"Kiwi: Radial Organic Structure": (
    				"A hyper-realistic mosque constructed from kiwi fruit, built as a large tabletop monument approximately 1 meter in scale with strong visual identity. "
    				"The central dome is formed from dense kiwi flesh, smooth and thick, with radial seed patterns spreading outward from the center. "
    				"The architecture incorporates layered structural mass with radial symmetry, forming walls, domes, and arches that follow natural seed patterns. "
    				"The kiwi skin provides subtle outer texture and structural edges. "
    				"The architecture emphasizes symmetry, organic detail, and strong volumetric presence. "
    				"The structure feels unique, dense, and architecturally defined. "
    				"The table surface contains kiwi residue and seeds."
				),

				"Alpukat: Core Mass Architecture": (
    				"A hyper-realistic mosque constructed from avocado, built as a large tabletop structure approximately 1 meter in scale with strong architectural mass. "
    				"The central dome is formed from dense avocado flesh, smooth, thick, and creamy, creating a soft but solid hemispherical mass. "
    				"The structure is built around the natural core logic, with thick layers forming walls, arches, and structural platforms. "
    				"The outer skin reinforces structural edges, adding contrast and definition. "
    				"The architecture emphasizes core density, smooth surfaces, and layered structural mass. "
    				"The structure feels grounded, heavy, and cohesive. "
    				"The table surface is scattered with avocado fragments and peel."
				),

				"Stroberi: Cluster Flow Architecture": (
    				"A hyper-realistic mosque constructed from strawberry fruit, built as a large tabletop monument approximately 1 meter in scale with strong visual presence. "
    				"The central dome is formed from compressed strawberry flesh, smooth yet slightly textured with visible seeds across the surface. "
    				"The structure uses layered strawberry forms creating flowing architectural shapes combined with structural mass. "
    				"The surface shows seed patterns adding fine detail and texture. "
    				"The architecture emphasizes organic flow, layering, and volumetric density. "
    				"The structure feels vibrant, cohesive, and monumental. "
    				"The table surface is scattered with strawberry residue and seeds."
				),

				"Cabe: Dynamic Flow Architecture": (
    				"A hyper-realistic mosque constructed from chili peppers, built as a large tabletop structure approximately 1 meter in scale with strong dynamic presence. "
    				"The central dome is formed from compressed chili flesh, smooth, rounded, and glossy, creating a bold focal mass. "
    				"The structure incorporates curved chili forms creating flowing architectural elements while maintaining strong structural clarity. "
    				"The architecture emphasizes movement, curvature, and dense structural mass. "
    				"The structure feels energetic, bold, and monumental. "
    				"The table surface is scattered with chili seeds and fragments."
				),

				"Wortel: Layered Root Architecture": (
    				"A hyper-realistic mosque constructed from carrot, built as a large tabletop monument approximately 1 meter in scale with strong structural clarity. "
    				"The central dome is formed from dense carrot flesh, smooth and thick with visible natural fiber lines. "
    				"The structure is assembled from layered carrot segments forming thick walls, deep arches, and stepped architectural forms. "
    				"The architecture emphasizes linear texture, layering, and strong geometric mass. "
    				"The structure feels grounded, dense, and architecturally solid. "
    				"The table surface is scattered with carrot fragments and residue."
				),

				"Semangka: Kabah Royal Monolithic Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure made entirely from watermelon, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence and architectural dominance. "
    				"The structure forms a perfectly proportioned cube with extremely clean geometry, sharp edges, and balanced symmetry, clearly representing the iconic Ka'bah form. "
    				"The outer surface is constructed from thick, carefully layered dark green watermelon rind panels arranged in horizontal overlapping strips, creating a heavy kiswah-like appearance with subtle natural folds and fabric-like flow. "
    				"The layering feels dense, elegant, and luxurious, not rough or random, with controlled alignment and refined surface rhythm. "
    				"A thin, continuous horizontal band made from pale inner rind wraps precisely around the upper section, clean, straight, and visually refined. "
    				"A slightly elevated rectangular door is carved with clean depth, sharp edges, and clear proportional placement, maintaining architectural accuracy. "
    				"All components are built from large, solid fruit sections, ensuring strong structural mass and eliminating any fragile or miniature appearance. "
    				"The surface retains natural organic texture but remains clean, controlled, and premium in appearance. "
    				"The structure feels heavy, sacred, and monumental with strong visual authority. "
    				"The table surface contains subtle watermelon debris: minimal rind fragments and controlled residue."
				),

				"Semangka: Kabah Sacred Precision Structure": (
    				"A hyper-realistic handcrafted Ka'bah made entirely from watermelon, constructed as a large-scale tabletop object approximately 1 meter in size with strong sacred architectural presence. "
    				"The cube is perfectly formed with precise proportions, flat planar surfaces, and crisp edges, emphasizing iconic Ka'bah geometry and symmetry. "
    				"The exterior uses tightly aligned dark rind panels arranged in refined horizontal layers, forming a smooth, dense kiswah-like surface with minimal irregularity. "
    				"The surface appears calm, controlled, and visually premium, avoiding rough or chaotic textures. "
    				"A thin horizontal band made from pale inner rind runs seamlessly around the upper section with perfect alignment and consistent thickness. "
    				"The door is cleanly carved, slightly elevated, and sharply defined with subtle depth contrast, maintaining structural accuracy. "
    				"The build uses medium-to-large fruit blocks with precise alignment, ensuring strong mass and clean architectural readability. "
    				"Surface detail remains natural but highly controlled, with minimal cutting marks and no excessive roughness. "
    				"The structure feels refined, sacred, and architecturally precise. "
    				"The table surface contains only minimal and clean watermelon residue."
				),

				"Mangga: Kabah Royal Monolithic Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure made entirely from mango, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence and architectural dominance, clearly not a real building but visually heavy and commanding. "
    				"A perfectly proportioned cube constructed from dense mango sections with extremely clean geometry, sharp edges, and strong planar surfaces, accurately reflecting the iconic Ka'bah form. "
    				"The outer surface is formed using thick mango skin panels arranged in overlapping horizontal layers, creating a refined kiswah-like surface with subtle organic curvature and controlled flow. "
    				"The layering is dense and intentional, giving a luxurious and fabric-like appearance while maintaining structural clarity and fruit authenticity. "
    				"Clearly visible but controlled cutting marks and edge transitions reinforce real handcrafted construction without appearing rough or chaotic. "
    				"A thin, continuous horizontal band made from lighter mango flesh wraps precisely around the upper section with clean alignment and consistent thickness. "
    				"A slightly elevated rectangular door is carved with sharp edges, clear depth, and accurate proportional placement, seamlessly integrated into the cube structure. "
    				"All components are built from large, solid mango sections, avoiding small fragmented pieces and reinforcing a bold, heavy architectural presence. "
    				"Surface texture shows subtle natural moisture, fine fiber detail, and organic imperfection while remaining clean and premium in appearance. "
    				"The structure feels dense, sacred, monumental, and visually authoritative. "
    				"The wooden table surface contains minimal mango debris, including controlled peel fragments and soft residue."
				),

				"Mangga: Kabah Sacred Precision Structure": (
    				"A hyper-realistic handcrafted Ka'bah made entirely from mango, constructed as a large-scale tabletop object approximately 1 meter in size with strong sacred architectural presence and clean visual authority. "
    				"The cube is perfectly formed with precise proportions, flat planar surfaces, and crisp edge definition, emphasizing iconic Ka'bah geometry and symmetry. "
    				"The exterior is composed of tightly aligned mango skin panels arranged in refined horizontal layering, forming a smooth and dense kiswah-like surface with minimal irregularity. "
    				"Cutting marks are subtle and controlled, indicating precise craftsmanship rather than rough manual work. "
    				"A thin horizontal band made from pale mango flesh runs seamlessly around the upper section with perfect alignment and uniform thickness. "
    				"The door is cleanly carved, slightly elevated, and sharply defined with subtle depth contrast and accurate placement. "
    				"All elements are assembled from medium-to-large mango sections with precise alignment and structural consistency. "
    				"Surface detail remains natural with fine organic texture, but controlled and refined, avoiding excessive roughness. "
    				"The structure feels calm, sacred, balanced, and architecturally precise. "
    				"The table surface contains minimal and clean mango residue consistent with controlled construction."
				),

				"Apel: Kabah Royal Monolithic Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure made entirely from apple, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence and architectural dominance. "
    				"A perfectly proportioned cube formed from dense apple sections with sharp edges, smooth surfaces, and precise structural alignment. "
    				"The outer surface uses apple skin arranged in layered horizontal panels, creating a smooth and slightly glossy kiswah-like appearance with subtle organic reflection. "
    				"The layering is consistent and controlled, forming a refined and premium surface without chaotic irregularity. "
    				"Visible cutting marks are subtle and clean, reinforcing handcrafted realism while maintaining elegance. "
    				"A thin horizontal band made from pale apple flesh wraps seamlessly around the upper section with straight alignment and consistent thickness. "
    				"A clearly defined rectangular door is carved with depth, crisp edges, and accurate proportional placement. "
    				"All structural components are made from large apple sections, ensuring strong mass and avoiding miniature fragmentation. "
    				"The surface shows fine natural gloss, slight moisture, and organic variation while remaining controlled and refined. "
    				"The structure feels compact, dense, luxurious, and architecturally strong. "
    				"The table surface contains minimal apple debris and juice traces."
				),

				"Apel: Kabah Sacred Precision Structure": (
    				"A hyper-realistic handcrafted Ka'bah made entirely from apple, constructed as a large-scale tabletop structure approximately 1 meter in size with strong sacred architectural clarity. "
    				"The cube is perfectly symmetrical with flat surfaces, sharp edges, and precise geometric proportions. "
    				"The exterior uses tightly aligned apple skin panels forming a smooth and controlled kiswah-like surface with minimal texture variation. "
    				"Cutting marks are extremely subtle, indicating precise and careful craftsmanship. "
    				"A thin horizontal band made from inner apple flesh runs around the upper section with perfect alignment. "
    				"The door is cleanly carved, slightly elevated, and sharply defined with accurate proportions. "
    				"All components are assembled using medium-to-large apple sections with clean alignment and structural integrity. "
    				"The surface remains natural but refined, with controlled gloss and minimal irregularity. "
    				"The structure feels calm, sacred, balanced, and architecturally precise. "
    				"The table surface contains minimal residue."
				),

				"Durian: Kabah Royal Monolithic Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure made entirely from durian, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence and dramatic architectural dominance. "
    				"A perfectly proportioned cube constructed from dense durian flesh and shell, with sharp edges and strong structural mass. "
    				"The outer surface uses durian shell arranged in controlled layered patterns, forming a bold kiswah-like texture with sharp, spiked geometry softened into architectural rhythm. "
    				"The layering is dense and intentional, creating a luxurious yet aggressive surface character. "
    				"Visible carving marks and natural shell irregularities are present but controlled, emphasizing handcrafted realism. "
    				"A thin horizontal band made from lighter inner durian flesh wraps around the upper section with clean alignment. "
    				"A slightly elevated door is carved with clear depth and strong contrast against the textured surface. "
    				"All elements are constructed from large durian segments, ensuring heavy mass and strong visual presence. "
    				"The surface combines creamy smooth inner flesh with sharp outer shell, creating powerful contrast and tactile richness. "
    				"The structure feels bold, sacred, dense, and architecturally dominant. "
    				"The table surface contains durian shell fragments and organic debris."
				),

				"Durian: Kabah Sacred Precision Structure": (
    				"A hyper-realistic handcrafted Ka'bah made entirely from durian, constructed as a large-scale tabletop structure approximately 1 meter in size with controlled sacred presence. "
    				"The cube is perfectly formed with precise proportions, flat surfaces, and clean geometric definition. "
    				"The outer shell texture is aligned into controlled layered patterns, forming a structured kiswah-like exterior. "
    				"Cutting marks and surface irregularities are minimized and refined, indicating careful craftsmanship. "
    				"A thin horizontal band made from inner durian flesh wraps cleanly around the upper section. "
    				"The door is sharply carved, slightly elevated, and proportionally accurate. "
    				"All components are assembled from medium-to-large sections with precise alignment. "
    				"The surface remains natural but controlled, balancing texture and refinement. "
    				"The structure feels powerful yet calm, sacred, and architecturally precise. "
    				"The table surface contains minimal debris."
				),

				"Kiwi: Kabah Royal Monolithic Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure made entirely from kiwi, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence and architectural dominance. "
    				"A perfectly proportioned cube constructed from dense kiwi sections with sharp edges, smooth surfaces, and strong geometric clarity. "
    				"The outer surface is formed using kiwi skin and flesh arranged in layered horizontal panels, creating a refined kiswah-like surface with subtle organic softness and natural seed texture embedded within. "
    				"The layering is dense and intentional, forming a smooth yet slightly textured exterior that feels organic but controlled. "
    				"Clearly visible but refined cutting marks emphasize handcrafted construction without appearing rough or chaotic. "
    				"A thin horizontal band made from lighter kiwi flesh wraps precisely around the upper section with clean alignment. "
    				"A slightly elevated rectangular door is carved with crisp edges, clear depth, and accurate proportional placement. "
    				"All elements are built from large kiwi sections, ensuring strong mass and eliminating miniature fragmentation. "
    				"The surface shows fine organic detail, subtle moisture, and seed patterns while remaining clean and premium. "
    				"The structure feels unique, sacred, dense, and visually refined. "
    				"The table surface contains minimal kiwi debris and seeds."
				),

				"Kiwi: Kabah Sacred Precision Structure": (
    				"A hyper-realistic handcrafted Ka'bah made entirely from kiwi, constructed as a large-scale tabletop structure approximately 1 meter in size with strong sacred architectural clarity. "
    				"The cube is perfectly symmetrical with flat surfaces and crisp edges. "
    				"The exterior uses tightly aligned kiwi panels forming a smooth and controlled kiswah-like surface with subtle seed texture. "
    				"Cutting marks are minimal and refined, indicating precise craftsmanship. "
    				"A thin horizontal band wraps seamlessly around the upper section. "
    				"The door is cleanly carved, slightly elevated, and sharply defined. "
    				"All components are assembled from medium-to-large kiwi sections with precise alignment. "
    				"The structure feels calm, balanced, and architecturally precise. "
    				"The table surface contains minimal residue."
				),

				"Alpukat: Kabah Royal Monolithic Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure made entirely from avocado, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence. "
    				"A perfectly proportioned cube formed from dense avocado flesh with smooth, creamy surfaces and sharp structural edges. "
    				"The outer skin is arranged in layered horizontal panels forming a soft kiswah-like surface with subtle organic flow and muted green tones. "
    				"The layering is controlled and dense, creating a luxurious yet natural appearance. "
    				"Visible cutting marks are subtle and refined, reinforcing handcrafted realism. "
    				"A thin horizontal band made from lighter avocado flesh wraps cleanly around the upper section. "
    				"A slightly elevated door is carved with clean depth and precise geometry. "
    				"All elements are built from large avocado sections, ensuring strong structural mass. "
    				"The surface shows fine organic texture with controlled softness and natural variation. "
    				"The structure feels calm, dense, and premium. "
    				"The table surface contains minimal avocado debris."
				),

				"Alpukat: Kabah Sacred Precision Structure": (
    				"A hyper-realistic handcrafted Ka'bah made entirely from avocado, constructed as a large-scale tabletop structure approximately 1 meter in size. "
    				"The cube is perfectly formed with smooth surfaces and precise edges. "
    				"The exterior uses tightly aligned avocado panels forming a clean kiswah-like surface with minimal irregularity. "
    				"A thin horizontal band wraps seamlessly around the upper section. "
    				"The door is cleanly carved and proportionally accurate. "
    				"The structure feels balanced, refined, and architecturally precise. "
    				"The table surface contains minimal residue."
				),

				"Anggur: Kabah Royal Monolithic Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure made entirely from grapes, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence and dense visual character. "
    				"A perfectly proportioned cube formed from tightly packed grape clusters, creating a cohesive and heavy structural mass. "
    				"The outer surface forms a layered kiswah-like appearance with subtle organic curvature and glossy texture from grape skins. "
    				"The layering is dense and intentional, forming a luxurious and visually rich surface. "
    				"Subtle cutting and compression marks emphasize handcrafted realism. "
    				"A thin horizontal band wraps cleanly around the upper section. "
    				"A slightly elevated door is carved with clear depth and proportional accuracy. "
    				"All elements are constructed from dense grape formations, ensuring structural cohesion and weight. "
    				"The surface shows gloss, translucency, and organic variation while remaining controlled. "
    				"The structure feels rich, dense, and premium. "
    				"The table surface contains grape residue and stems."
				),

				"Anggur: Kabah Sacred Precision Structure": (
    				"A hyper-realistic handcrafted Ka'bah made entirely from grapes, constructed as a large-scale tabletop structure approximately 1 meter in size. "
    				"The cube is perfectly aligned with clean geometric proportions. "
    				"Grape clusters are arranged into controlled surfaces forming a refined kiswah-like exterior. "
    				"A thin horizontal band wraps precisely around the upper section. "
    				"The door is cleanly defined and minimal. "
    				"The structure feels cohesive, balanced, and architecturally strong. "
    				"The table surface contains minimal residue."
				),

				"Nanas: Kabah Royal Monolithic Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure made entirely from pineapple, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence. "
    				"A perfectly proportioned cube constructed from dense pineapple sections with strong edges and geometric clarity. "
    				"The outer skin is arranged in layered horizontal panels forming a textured kiswah-like surface with geometric pattern repetition. "
    				"The layering is bold, consistent, and visually rich while remaining controlled. "
    				"Visible carving marks and natural imperfections enhance realism. "
    				"A thin horizontal band wraps cleanly around the upper section. "
    				"A slightly elevated door is carved with depth and precision. "
    				"All elements are built from large pineapple sections, ensuring strong mass and structural clarity. "
    				"The surface shows fiber detail and organic texture. "
    				"The structure feels bold, dense, and luxurious. "
    				"The table surface contains pineapple debris."
				),

				"Nanas: Kabah Sacred Precision Structure": (
    				"A hyper-realistic handcrafted Ka'bah made entirely from pineapple, constructed as a large-scale tabletop structure approximately 1 meter in size. "
    				"The cube is perfectly formed with clean geometry and structured alignment. "
    				"The exterior uses aligned pineapple textures forming a controlled surface. "
    				"A thin horizontal band wraps seamlessly around the upper section. "
    				"The door is cleanly carved and precise. "
    				"The structure feels strong, balanced, and architecturally refined. "
    				"The table surface contains minimal residue."
				),

				"Pepaya: Kabah Royal Monolithic Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure made entirely from papaya, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence. "
    				"A perfectly proportioned cube constructed from dense papaya flesh with smooth surfaces and sharp edges. "
    				"The outer skin is layered into horizontal panels forming a soft kiswah-like surface with subtle organic curvature. "
    				"The layering is controlled and refined, creating a premium appearance. "
    				"A thin horizontal band wraps cleanly around the upper section. "
    				"A slightly elevated door is carved with clear depth and clean edges. "
    				"All elements are built from large papaya sections, ensuring structural mass. "
    				"The structure feels smooth, dense, and elegant. "
    				"The table surface contains papaya debris and seeds."
				),

				"Pepaya: Kabah Sacred Precision Structure": (
    				"A hyper-realistic handcrafted Ka'bah made entirely from papaya, constructed as a large-scale tabletop structure approximately 1 meter in size. "
    				"The cube is perfectly aligned with smooth surfaces and crisp edges. "
    				"The exterior is clean and controlled with minimal irregularity. "
    				"A thin horizontal band wraps precisely around the upper section. "
    				"The door is cleanly defined. "
    				"The structure feels calm, balanced, and precise. "
    				"The table surface contains minimal residue."
				),

				"Salak: Kabah Royal Monolithic Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure made entirely from salak, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence. "
    				"A perfectly proportioned cube constructed from dense salak flesh and skin with strong edges and geometric clarity. "
    				"The outer skin forms layered horizontal panels creating a textured kiswah-like surface with scale-like pattern repetition. "
    				"The layering is dense and visually rich, forming a luxurious and tactile exterior. "
    				"Subtle carving marks emphasize handcrafted realism. "
    				"A thin horizontal band wraps cleanly around the upper section. "
    				"A slightly elevated door is carved with depth and accuracy. "
    				"All elements are constructed from large salak sections, ensuring strong structural mass. "
    				"The structure feels textured, dense, and premium. "
    				"The table surface contains salak debris."
				),

				"Salak: Kabah Sacred Precision Structure": (
    				"A hyper-realistic handcrafted Ka'bah made entirely from salak, constructed as a large-scale tabletop structure approximately 1 meter in size. "
    				"The cube is perfectly formed with precise geometry and clean alignment. "
    				"The exterior uses controlled scale textures forming a structured surface. "
    				"A thin horizontal band wraps seamlessly around the upper section. "
    				"The door is cleanly carved and proportionally accurate. "
    				"The structure feels balanced, refined, and architecturally precise. "
    				"The table surface contains minimal residue."
				),

				"Semangka + Kacang Ijo: Kabah Royal Granular Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure constructed from watermelon and mung beans, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence and architectural dominance. "
    				"The structure forms a perfectly proportioned cube using dense watermelon flesh and thick rind panels, creating sharp edges, flat surfaces, and strong geometric clarity that accurately represents the iconic Ka'bah form. "
    				"The outer surface is covered with tightly arranged mung beans, forming a dense, continuous granular kiswah-like layer that wraps around the cube with consistent thickness and controlled alignment. "
    				"The beans are not scattered randomly but carefully embedded and structured into a cohesive surface system, creating a rich tactile texture while maintaining visual order and elegance. "
    				"The layering creates a fabric-like effect with subtle variation in depth and density, enhancing realism and luxury. "
    				"A thin horizontal band made from lighter inner rind runs precisely around the upper section, clean, straight, and uninterrupted. "
    				"A slightly elevated rectangular door is carved with sharp edges, clear depth, and accurate proportional placement. "
    				"All elements are built from large watermelon sections combined with dense bean layering, ensuring strong structural mass and eliminating any miniature appearance. "
    				"The surface shows organic imperfections but remains controlled and premium in appearance. "
    				"The structure feels dense, sacred, monumental, and visually rich. "
    				"The table surface contains scattered mung beans, rind fragments, and subtle juice residue."
				),

				"Semangka + Kedelai: Kabah Sacred Modular Texture": (
    				"A hyper-realistic handcrafted Ka'bah constructed from watermelon and soybeans, built as a large-scale tabletop structure approximately 1 meter in size with strong sacred architectural clarity. "
    				"The cube is perfectly formed with precise proportions, flat planar surfaces, and crisp edges, emphasizing iconic Ka'bah symmetry. "
    				"The exterior uses tightly packed soybeans arranged in controlled modular patterns, forming a dense kiswah-like surface with subtle natural variation and matte texture. "
    				"The soybean layer is evenly distributed and carefully structured, creating a refined and uniform exterior without chaotic irregularity. "
    				"A thin horizontal band made from pale inner rind wraps seamlessly around the upper section with perfect alignment. "
    				"The door is cleanly carved, slightly elevated, and sharply defined with accurate placement. "
    				"All components are assembled from medium-to-large watermelon sections with precise bean integration. "
    				"The structure feels calm, balanced, dense, and architecturally precise. "
    				"The table surface contains minimal soybean debris and controlled residue."
				),

				"Mangga + Jagung: Kabah Royal Layered Texture": (
    				"A hyper-realistic handcrafted Ka'bah structure made from mango and corn kernels, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence. "
    				"The cube is formed from dense mango flesh and skin, creating a smooth, solid structural base with sharp edges and clean geometry. "
    				"The outer surface is layered with tightly packed corn kernels arranged in structured horizontal bands, forming a rich textured kiswah-like appearance with subtle depth variation. "
    				"The kernels are carefully aligned and embedded into the surface, creating a cohesive and luxurious pattern rather than random distribution. "
    				"A thin horizontal band made from lighter mango flesh wraps precisely around the upper section. "
    				"A slightly elevated door is carved with clean depth and accurate proportions. "
    				"The structure feels vibrant, dense, and architecturally refined. "
    				"The table surface contains corn kernels and mango residue."
				),

				"Apel + Kedelai: Kabah Sacred Precision Texture": (
    				"A hyper-realistic handcrafted Ka'bah constructed from apple and soybeans, built as a large-scale tabletop structure approximately 1 meter in size. "
    				"The cube is perfectly symmetrical with clean edges and smooth planar surfaces. "
    				"The exterior uses tightly aligned soybeans forming a controlled and uniform kiswah-like layer with minimal irregularity. "
    				"The texture appears dense and refined, with subtle matte variation across the surface. "
    				"A thin horizontal band made from pale apple flesh wraps seamlessly around the upper section. "
    				"The door is cleanly carved, slightly elevated, and precisely defined. "
    				"The structure feels calm, sacred, and architecturally precise. "
    				"The table surface contains minimal residue."
				),

				"Durian + Kacang Ijo: Kabah Royal Textured Contrast": (
    				"A hyper-realistic handcrafted Ka'bah structure constructed from durian and mung beans, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence and dramatic visual impact. "
    				"The cube is formed from dense durian flesh and shell, creating strong structural mass and sharp geometry. "
    				"The outer surface is layered with tightly packed mung beans, creating a dense granular kiswah-like coating that softens the aggressive durian shell texture into a controlled architectural surface. "
    				"The contrast between spiked shell structure and fine granular layering creates strong tactile richness. "
    				"A thin horizontal band made from lighter durian flesh wraps around the upper section with clean alignment. "
    				"A slightly elevated door is carved with depth and clear contrast. "
    				"The structure feels bold, dense, and architecturally powerful. "
    				"The table surface contains durian shell fragments and mung beans."
				),

				"Anggur + Kedelai: Kabah Sacred Dense Composition": (
    				"A hyper-realistic handcrafted Ka'bah constructed from grapes and soybeans, built as a large-scale tabletop structure approximately 1 meter in size with strong sacred clarity. "
    				"The cube is formed from compressed grape mass, creating smooth rounded surfaces that are refined into flat planes and sharp edges. "
    				"The outer surface is coated with tightly arranged soybeans forming a dense and uniform kiswah-like exterior. "
    				"The texture is consistent and controlled, with subtle variation adding realism without disrupting structure. "
    				"A thin horizontal band wraps precisely around the upper section. "
    				"The door is cleanly carved and proportionally accurate. "
    				"The structure feels cohesive, dense, and architecturally balanced. "
    				"The table surface contains grape residue and soybean fragments."
				),

				"Melon + Kacang Ijo: Kabah Royal Granular Kiswah": (
    				"A hyper-realistic handcrafted Ka'bah structure constructed from melon and mung beans, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence and architectural dominance. "
    				"The structure forms a perfectly proportioned cube using dense melon flesh and thick rind panels, creating sharp edges, flat surfaces, and strong geometric clarity that accurately reflects the iconic Ka'bah form. "
    				"The outer surface is covered with tightly arranged mung beans, forming a dense, continuous granular kiswah-like layer with consistent thickness and precise alignment. "
    				"The beans are carefully embedded into the surface, forming a cohesive material system rather than random distribution, creating a refined and luxurious texture. "
    				"The layering creates subtle depth variation, enhancing tactile realism while maintaining visual order. "
    				"A thin horizontal band made from lighter melon flesh wraps precisely around the upper section with clean and uninterrupted alignment. "
    				"A slightly elevated rectangular door is carved with crisp edges, clear depth, and accurate proportional placement. "
    				"All components are constructed from large melon sections combined with dense bean layering, ensuring strong structural mass. "
    				"The surface shows subtle organic moisture and natural variation while remaining clean and premium. "
    				"The structure feels dense, sacred, monumental, and visually refined. "
    				"The table surface contains scattered mung beans and melon fragments."
				),

				"Melon + Kedelai: Kabah Sacred Precision Texture": (
    				"A hyper-realistic handcrafted Ka'bah constructed from melon and soybeans, built as a large-scale tabletop structure approximately 1 meter in size with strong sacred architectural clarity. "
    				"The cube is perfectly formed with precise proportions, flat planar surfaces, and crisp edges. "
    				"The exterior uses tightly packed soybeans arranged in a uniform and controlled pattern, forming a dense kiswah-like surface with subtle matte variation. "
    				"The soybean layer is evenly distributed and precisely aligned, creating a refined and clean exterior without chaotic irregularity. "
    				"A thin horizontal band made from pale melon flesh wraps seamlessly around the upper section with perfect alignment. "
    				"The door is cleanly carved, slightly elevated, and sharply defined. "
    				"All elements are assembled from medium-to-large melon sections with precise integration of soybean texture. "
    				"The structure feels calm, balanced, dense, and architecturally precise. "
    				"The table surface contains minimal residue."
				),

				"Buah Naga + Kacang Ijo: Kabah Royal Organic Granular": (
    				"A hyper-realistic handcrafted Ka'bah structure constructed from dragon fruit and mung beans, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence and visual richness. "
    				"The cube is formed from dense dragon fruit flesh and skin, creating strong structural mass with smooth planar surfaces and sharp edges. "
    				"The outer surface is coated with tightly packed mung beans, forming a dense kiswah-like layer that contrasts with the vibrant magenta tones and embedded black seeds of the fruit beneath. "
    				"The beans are structured in controlled layering, creating a cohesive and luxurious surface system rather than random scattering. "
    				"The interaction between fine granular beans and natural seed patterns creates complex visual texture while maintaining architectural clarity. "
    				"A thin horizontal band made from lighter dragon fruit flesh wraps precisely around the upper section. "
    				"A slightly elevated door is carved with clear depth and accurate proportions. "
    				"The structure feels bold, unique, dense, and visually striking. "
    				"The table surface contains seeds, beans, and fruit residue."
				),

				"Buah Naga + Kedelai: Kabah Sacred Precision Organic": (
    				"A hyper-realistic handcrafted Ka'bah constructed from dragon fruit and soybeans, built as a large-scale tabletop structure approximately 1 meter in size. "
    				"The cube is perfectly aligned with flat surfaces and sharp edges, maintaining iconic Ka'bah proportions. "
    				"The exterior uses tightly arranged soybeans forming a uniform kiswah-like coating with subtle natural variation. "
    				"The underlying dragon fruit structure provides rich color and organic depth beneath the controlled soybean layer. "
    				"A thin horizontal band wraps seamlessly around the upper section. "
    				"The door is cleanly carved and precisely positioned. "
    				"The structure feels balanced, refined, and architecturally strong. "
    				"The table surface contains minimal residue."
				),

				"Kiwi + Kacang Ijo: Kabah Royal Radial Texture": (
    				"A hyper-realistic handcrafted Ka'bah structure constructed from kiwi and mung beans, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence. "
    				"The cube is formed from dense kiwi flesh with visible radial seed patterns refined into flat planes and sharp edges. "
    				"The outer surface is layered with tightly packed mung beans, forming a dense kiswah-like exterior that overlays the natural radial texture beneath. "
    				"The beans are embedded in structured alignment, creating a cohesive and luxurious granular surface. "
    				"The combination of radial seed patterns and granular layering creates depth and visual complexity while maintaining control. "
    				"A thin horizontal band wraps around the upper section. "
    				"A slightly elevated door is carved with crisp edges and accurate proportions. "
    				"The structure feels unique, dense, and visually rich. "
    				"The table surface contains seeds and beans."
				),

				"Kiwi + Kedelai: Kabah Sacred Precision Radial": (
    				"A hyper-realistic handcrafted Ka'bah constructed from kiwi and soybeans, built as a large-scale tabletop structure approximately 1 meter in size. "
    				"The cube is perfectly symmetrical with refined planar surfaces. "
    				"The exterior uses tightly aligned soybeans forming a controlled kiswah-like layer with subtle matte variation. "
    				"The underlying kiwi structure provides organic depth while remaining visually controlled. "
    				"A thin horizontal band wraps precisely around the upper section. "
    				"The door is cleanly carved and proportionally accurate. "
    				"The structure feels calm, balanced, and architecturally precise. "
    				"The table surface contains minimal residue."
				),

				"Pisang + Jagung: Kabah Royal Modular Grain": (
    				"A hyper-realistic handcrafted Ka'bah structure constructed from banana and corn kernels, built as a large tabletop monument approximately 1 meter in scale with strong sacred presence. "
    				"The cube is formed from dense banana flesh and peel, creating smooth surfaces and strong geometric edges. "
    				"The outer surface is layered with tightly arranged corn kernels forming a structured kiswah-like texture with subtle repetition and depth. "
    				"The kernels are embedded in controlled rows, creating a modular and refined exterior system. "
    				"A thin horizontal band wraps cleanly around the upper section. "
    				"A slightly elevated door is carved with depth and clarity. "
    				"The structure feels warm, dense, and architecturally cohesive. "
    				"The table surface contains kernels and banana residue."
				),

				"Pisang + Kedelai: Kabah Sacred Soft Precision": (
    				"A hyper-realistic handcrafted Ka'bah constructed from banana and soybeans, built as a large-scale tabletop structure approximately 1 meter in size. "
    				"The cube is perfectly aligned with smooth surfaces and clean geometry. "
    				"The exterior uses tightly packed soybeans forming a uniform kiswah-like layer. "
    				"The structure remains soft yet controlled, with balanced visual density. "
    				"A thin horizontal band wraps precisely around the upper section. "
    				"The door is cleanly carved and defined. "
    				"The structure feels calm, dense, and refined. "
    				"The table surface contains minimal residue."
				),

				"Semangka + Kacang Ijo: Monumental Granular Mosque": (
    				"A hyper-realistic mosque constructed from watermelon and mung beans, built as a large tabletop monument approximately 1 meter in scale with strong architectural dominance. "
    				"The central dome is formed from dense watermelon flesh, smooth, thick, and perfectly rounded with visible moist texture, acting as the dominant focal structure. "
    				"The main walls and structural mass are built from thick watermelon rind and flesh blocks, forming deep arches, layered walls, and strong geometric mass. "
    				"The outer surfaces are coated with tightly arranged mung beans, forming a dense granular texture that enhances architectural depth and realism. "
    				"The beans are embedded into the structure in controlled layers, not scattered, creating a cohesive material system. "
    				"Secondary domes and minarets rise symmetrically, maintaining clear hierarchy and strong vertical presence. "
    				"The structure feels heavy, grounded, and monumental with clear volumetric mass. "
    				"The table surface contains watermelon fragments, seeds, and mung bean debris."
				),

				"Mangga + Jagung: Monumental Layered Mosque": (
    				"A hyper-realistic mosque constructed from mango and corn kernels, built as a large tabletop structure approximately 1 meter in scale with strong architectural presence. "
    				"The central dome is formed from dense mango flesh, smooth and thick with rich color and subtle moisture. "
    				"The structure uses mango blocks forming thick walls, deep recessed arches, and layered architectural tiers. "
    				"Corn kernels are tightly arranged across surfaces, forming structured texture layers that enhance detail and depth. "
    				"The kernels are embedded in aligned patterns, creating a refined and cohesive exterior system. "
    				"The structure emphasizes layered mass, symmetry, and volumetric presence. "
    				"The table surface contains corn kernels and mango debris."
				),

				"Melon + Kedelai: Monumental Precision Mosque": (
    				"A hyper-realistic mosque constructed from melon and soybeans, built as a large tabletop monument approximately 1 meter in size with strong architectural clarity. "
    				"The central dome is formed from dense melon flesh, smooth, thick, and rounded with soft organic texture. "
    				"The walls and structures are built from melon sections forming strong geometric mass and deep architectural layers. "
    				"The outer surfaces are covered with tightly packed soybeans, forming a uniform and refined texture system. "
    				"The soybean layer is evenly distributed, creating a clean and controlled visual appearance. "
    				"The structure feels balanced, dense, and architecturally precise. "
    				"The table surface contains soybean debris and melon residue."
				),

				"Buah Naga + Kacang Ijo: Monumental Organic Mosque": (
    				"A hyper-realistic mosque constructed from dragon fruit and mung beans, built as a large tabletop monument approximately 1 meter in scale with strong visual identity. "
    				"The central dome is formed from dense dragon fruit flesh, smooth and rounded with embedded black seeds adding natural texture. "
    				"The structure uses thick fruit sections forming walls, arches, and structural mass. "
    				"Mung beans are layered across surfaces, forming a dense granular exterior that contrasts with the vibrant fruit tones. "
    				"The combination creates rich texture while maintaining architectural clarity. "
    				"The structure feels bold, unique, and monumental. "
    				"The table surface contains seeds, beans, and fruit debris."
				),

				"Kiwi + Kedelai: Monumental Radial Mosque": (
    				"A hyper-realistic mosque constructed from kiwi and soybeans, built as a large tabletop structure approximately 1 meter in scale. "
    				"The central dome is formed from kiwi flesh with radial seed patterns refined into smooth rounded geometry. "
    				"The structure uses layered kiwi sections forming thick walls and architectural depth. "
    				"Soybeans create a uniform outer surface, forming controlled texture across the structure. "
    				"The architecture emphasizes symmetry, radial detail, and volumetric mass. "
    				"The structure feels refined, dense, and architecturally strong. "
    				"The table surface contains kiwi seeds and soybean residue."
				),

				"Pisang + Jagung: Monumental Modular Mosque": (
    				"A hyper-realistic mosque constructed from banana and corn kernels, built as a large tabletop monument approximately 1 meter in scale with strong structural mass. "
    				"The central dome is formed from compressed banana flesh, smooth and rounded with visible fiber texture. "
    				"The structure is built from stacked banana blocks forming thick walls and deep architectural layers. "
    				"Corn kernels are embedded across surfaces, forming modular texture patterns that enhance detail. "
    				"The architecture emphasizes density, repetition, and structural clarity. "
    				"The structure feels grounded, cohesive, and monumental. "
    				"The table surface contains kernels and banana debris."
				),

				"Apel + Kedelai: Monumental Clean Mosque": (
    				"A hyper-realistic mosque constructed from apple and soybeans, built as a large tabletop structure approximately 1 meter in scale with strong architectural clarity. "
    				"The central dome is formed from dense apple flesh, smooth, slightly glossy, and rounded. "
    				"The structure uses large apple sections forming clean geometric walls and arches. "
    				"Soybeans create a uniform and refined surface texture across the structure. "
    				"The architecture emphasizes clean lines, symmetry, and controlled detail. "
    				"The structure feels compact, dense, and architecturally precise. "
    				"The table surface contains minimal residue."
				),

				"Durian + Kacang Ijo: Monumental Extreme Texture Mosque": (
    				"A hyper-realistic mosque constructed from durian and mung beans, built as a large tabletop monument approximately 1 meter in scale with strong visual impact. "
    				"The central dome is formed from thick durian flesh, smooth and dense, creating a powerful focal structure. "
    				"The outer structure uses durian shell forming aggressive textured walls and minarets. "
    				"Mung beans are layered across the surface, softening and structuring the texture into architectural clarity. "
    				"The structure emphasizes contrast, depth, and strong volumetric mass. "
    				"The structure feels bold, dramatic, and monumental. "
    				"The table surface contains durian shell fragments and beans."
				),

				"Anggur + Kedelai: Monumental Cluster Mosque": (
    				"A hyper-realistic mosque constructed from grapes and soybeans, built as a large tabletop monument approximately 1 meter in scale with strong density. "
    				"The central dome is formed from compressed grape flesh, smooth and rounded with subtle translucency. "
    				"The structure uses dense grape clusters forming thick architectural mass. "
    				"Soybeans create a uniform outer layer, refining the structure into a cohesive surface. "
    				"The architecture emphasizes density, clustering, and volumetric presence. "
    				"The structure feels compact, rich, and monumental. "
    				"The table surface contains grape debris and soybeans."
				),

				"Labu + Jagung: Monumental Heavy Mosque": (
    				"A hyper-realistic mosque constructed from pumpkin and corn kernels, built as a large tabletop monument approximately 1 meter in scale with strong architectural weight. "
    				"The central dome is formed from dense pumpkin flesh, smooth and thick with visible fiber texture. "
    				"The structure uses carved pumpkin blocks forming heavy walls, deep arches, and layered tiers. "
    				"Corn kernels are embedded into the structure forming detailed texture layers. "
    				"The architecture emphasizes heavy mass, depth, and strong structural clarity. "
    				"The structure feels bold, grounded, and monumental. "
    				"The table surface contains pumpkin fragments and kernels."
				)
				
            },        
            "📦 Miniatur Bahan Sederhana": {
				"Koran Bekas: Layered Panel": (
					"A hyper-realistic miniature mosque constructed from layered newspaper panels, firmly assembled on a rustic wooden table surface, with the base clearly resting on the table. "
					"The structure features domes and minarets built from stacked and cut newspaper sheets arranged in clean architectural layers. "
					"Visible paper edges, thin layered stacks, and slightly uneven cuts create strong material definition. "
					"Printed text, faded ink, and subtle discoloration remain visible across surfaces without overwhelming readability. "
					"Each panel is aligned with clear assembly logic, maintaining structural clarity. "
					"Fine paper fiber texture, slight curling edges, and controlled surface wear enhance realism. "
					"Balanced tones prevent over-bright white areas or washed-out contrast. "
					"The wooden table surface contains small paper scraps and subtle fiber debris."
				),

				"Koran Bekas: Crumpled Repair": (
					"A hyper-realistic miniature mosque constructed from crumpled and re-shaped newspaper, assembled on a rustic wooden table surface. "
					"The structure maintains mosque proportions while using compressed paper forms with visible folds and wrinkles. "
					"Sharp creases, layered folds, and irregular compression create strong shadow depth and tactile complexity. "
					"Torn sections are repaired using visible tape strips and patched paper layers. "
					"Printed text appears distorted across the folded surfaces, reinforcing material realism. "
					"Edges remain uneven with controlled damage, avoiding chaotic destruction. "
					"Lighting emphasizes fold depth and micro-texture without flattening detail. "
					"The table contains wrinkled scraps, torn edges, and subtle debris."
				),

				"Koran Bekas: Modular Recycled": (
					"A hyper-realistic miniature mosque constructed from modular newspaper blocks arranged precisely on a rustic wooden table surface. "
					"Uniform folded paper units form domes and towers with structured repetition and clear architectural rhythm. "
					"Each module shows visible folds, edges, and layered paper thickness. "
					"Printed text fragments create subtle visual variation across the structure. "
					"Clean segmentation reinforces modular construction while preserving organic paper texture. "
					"Edges remain crisp but slightly imperfect, avoiding synthetic appearance. "
					"Balanced color and contrast prevent glare or washed-out highlights. "
					"The table surface shows neatly cut paper modules and minimal scraps."
				),

				"Kardus Bekas: Layered Panel": (
					"A hyper-realistic miniature mosque constructed from layered cardboard panels, firmly assembled on a rustic wooden table surface, with the base clearly resting on the table. "
					"The structure features domes and minarets built from stacked cardboard sheets arranged in clear architectural layers. "
					"Corrugated edges are visible along cut sections, revealing the inner fluted structure of the cardboard. "
					"Surface textures include worn print marks, faded labels, and subtle stains. "
					"Each panel is aligned with precise assembly logic, maintaining strong structural readability. "
					"Rough edges, slight fraying, and fiber exposure enhance tactile realism. "
					"Balanced tones prevent flat or overly dull appearance. "
					"The table surface contains cardboard fragments and fine fiber debris."
				),

				"Kardus Bekas: Crumpled Repair": (
					"A hyper-realistic miniature mosque constructed from crumpled and reshaped cardboard, assembled on a rustic wooden table surface. "
					"The structure maintains mosque proportions while using bent and compressed cardboard forms. "
					"Visible fold lines, crushed edges, and structural dents create strong texture and shadow depth. "
					"Torn areas are reinforced with tape, patches, and layered cardboard repairs. "
					"Corrugated interiors are partially exposed along broken edges. "
					"Damage remains controlled, preserving the overall architectural clarity. "
					"Surface detail includes worn print, scratches, and subtle dirt marks. "
					"The table contains torn cardboard pieces and repair fragments."
				),

				"Kardus Bekas: Modular Recycled": (
					"A hyper-realistic miniature mosque constructed from modular cardboard blocks arranged precisely on a rustic wooden table surface. "
					"Uniform cardboard units form domes and towers with structured repetition and strong architectural rhythm. "
					"Each block reveals corrugated layers, rough edges, and natural fiber texture. "
					"Printed markings and faded labels add subtle variation across modules. "
					"Visible segmentation reinforces modular construction without appearing artificial. "
					"Edges remain clean but retain organic imperfections. "
					"Balanced color tones prevent flat brown appearance. "
					"The table surface shows neatly cut cardboard pieces and minimal debris."
				),

				"Botol Plastik Bekas (Aqua): Layered Panel": (
					"A hyper-realistic miniature mosque constructed from cut and layered transparent plastic bottle panels, assembled on a rustic wooden table surface, with the base clearly resting on the table. "
					"The structure features domes and minarets formed from flattened and shaped plastic sections. "
					"Semi-transparent surfaces create layered depth with subtle light transmission without overexposure. "
					"Wrinkles, minor scratches, and slight deformation from previous use are visible across the plastic. "
					"Faded label fragments and adhesive residue remain partially attached, adding realism. "
					"Each panel is arranged with clear structural logic, maintaining architectural readability. "
					"Edges are clean but slightly irregular, avoiding synthetic perfection. "
					"The table surface contains small plastic scraps and label fragments."
				),

				"Botol Plastik Bekas (Aqua): Crumpled Repair": (
					"A hyper-realistic miniature mosque constructed from crumpled and reshaped plastic bottles, assembled on a rustic wooden table surface. "
					"The structure maintains mosque proportions while using compressed plastic forms with visible folds and dents. "
					"Surface shows creases, stress marks, and light scratches from repeated use. "
					"Cut sections are reattached using visible tape and overlapping plastic layers. "
					"Transparent areas create subtle internal reflections with controlled lighting. "
					"Labels appear torn, partially peeled, and distorted along curved surfaces. "
					"Damage remains controlled, preserving structural clarity. "
					"The table contains crumpled plastic fragments, tape pieces, and residue."
				),

				"Botol Plastik Bekas (Aqua): Modular Recycled": (
					"A hyper-realistic miniature mosque constructed from modular plastic bottle segments arranged precisely on a rustic wooden table surface. "
					"Uniform cut sections form domes and towers with structured repetition. "
					"Transparent and semi-opaque plastic pieces create layered geometric composition. "
					"Each module retains natural plastic texture including slight scratches, thickness variation, and subtle distortion. "
					"Visible segmentation reinforces modular construction without appearing synthetic. "
					"Balanced reflections prevent excessive glare or unrealistic shine. "
					"The table surface shows neatly cut plastic segments and minimal debris."
				),

				"Kaleng Bekas: Layered Panel": (
					"A hyper-realistic miniature mosque constructed from cut and layered metal can panels, assembled on a rustic wooden table surface, with the base clearly resting on the table. "
					"The structure features domes and minarets formed from flattened metal sheets arranged in structured layers. "
					"Surface shows worn paint, scratches, and areas of oxidation with realistic variation. "
					"Edges reveal sharp but slightly irregular cuts, exposing raw metal underneath. "
					"Subtle rust patches appear along edges and seams without overwhelming the structure. "
					"Each panel is aligned with clear construction logic, maintaining architectural clarity. "
					"Reflections are controlled, avoiding excessive shine. "
					"The table contains small metal scraps and paint flakes."
				),

				"Kaleng Bekas: Crumpled Repair": (
					"A hyper-realistic miniature mosque constructed from dented and reshaped metal cans, assembled on a rustic wooden table surface. "
					"The structure maintains mosque proportions while using compressed and bent metal forms. "
					"Surface shows dents, creases, scratches, and layered rust with realistic texture depth. "
					"Torn or cut sections are patched using overlapping metal pieces and visible fastening points. "
					"Oxidation appears in layered tones, adding strong tactile detail. "
					"Damage remains controlled, preserving overall structure. "
					"Reflections are muted and realistic. "
					"The table contains metal fragments, rust particles, and debris."
				),

				"Kaleng Bekas: Modular Recycled": (
					"A hyper-realistic miniature mosque constructed from modular metal can segments arranged precisely on a rustic wooden table surface. "
					"Uniform geometric pieces form domes and towers with structured repetition. "
					"Each segment retains worn paint, scratches, and subtle rust textures. "
					"Visible segmentation enhances architectural clarity while maintaining organic metal imperfections. "
					"Edges are clean but not perfectly uniform. "
					"Reflections are balanced, avoiding mirror-like surfaces. "
					"The table surface shows neatly cut metal pieces and minimal residue."
				),

				"Sachet Kopi: Layered Panel": (
					"A hyper-realistic miniature mosque constructed from layered used coffee sachet panels, firmly assembled on a rustic wooden table surface, with the base clearly resting on the table. "
					"The structure features domes and minarets built from flattened sachet materials arranged in clean architectural layers. "
					"Glossy printed surfaces show wrinkles, scratches, and faded branding with partial text visibility. "
					"Foil and plastic layers create subtle reflective variation without excessive glare. "
					"Edges reveal thin material layering with slight fraying and irregular cuts. "
					"Each panel is aligned with clear structural logic, maintaining readability. "
					"Balanced reflections prevent over-bright highlights. "
					"The table contains small sachet fragments and torn edges."
				),

				"Sachet Kopi: Crumpled Repair": (
					"A hyper-realistic miniature mosque constructed from crumpled and reshaped coffee sachets, assembled on a rustic wooden table surface. "
					"The structure maintains mosque proportions while using compressed and folded material. "
					"Wrinkles, creases, and compression marks create strong texture and shadow depth. "
					"Torn areas are repaired with overlapping sachet layers and visible tape. "
					"Printed branding appears distorted across folded surfaces. "
					"Foil highlights remain controlled without excessive reflection. "
					"The table contains crumpled sachet pieces and debris."
				),

				"Sachet Kopi: Modular Recycled": (
					"A hyper-realistic miniature mosque constructed from modular coffee sachet segments arranged precisely on a rustic wooden table surface. "
					"Uniform cut pieces form domes and towers with structured repetition. "
					"Printed surfaces create colorful variation across modules. "
					"Each segment retains wrinkles, fine scratches, and material layering. "
					"Visible segmentation reinforces modular construction. "
					"Balanced reflection avoids glare. "
					"The table shows neatly cut sachet pieces and minimal debris."
				),

				"Sachet Shampoo: Layered Panel": (
					"A hyper-realistic miniature mosque constructed from layered used shampoo sachet panels, assembled on a rustic wooden table surface. "
					"The structure features domes and minarets built from flattened flexible plastic sheets. "
					"Smooth glossy surfaces show subtle wrinkles, scratches, and faded print. "
					"Colorful branding elements remain partially visible. "
					"Edges show thin plastic layers with slight deformation. "
					"Each panel is arranged with clear structural logic. "
					"Reflections are controlled to avoid excessive shine. "
					"The table contains plastic fragments and label residue."
				),

				"Sachet Shampoo: Crumpled Repair": (
					"A hyper-realistic miniature mosque constructed from crumpled shampoo sachets, assembled on a rustic wooden table surface. "
					"The structure uses compressed plastic forms with visible folds and dents. "
					"Surface shows creases, scratches, and stretched material areas. "
					"Torn sections are patched with tape and overlapping layers. "
					"Gloss remains soft and controlled. "
					"The table contains crumpled plastic pieces and residue."
				),

				"Sachet Shampoo: Modular Recycled": (
					"A hyper-realistic miniature mosque constructed from modular shampoo sachet pieces arranged precisely on a rustic wooden table surface. "
					"Uniform plastic segments form structured domes and towers. "
					"Printed colors create visual variation. "
					"Each piece retains subtle surface wear and fine scratches. "
					"Visible segmentation enhances structure. "
					"Reflections are balanced. "
					"The table shows neatly cut plastic pieces."
				),

				"Bungkus Indomie: Layered Panel": (
					"A hyper-realistic miniature mosque constructed from layered instant noodle packaging panels, assembled on a rustic wooden table surface. "
					"The structure features domes and minarets formed from flattened packaging sheets. "
					"Glossy printed surfaces show wrinkles, folds, and faded branding details. "
					"Bright colors remain visible but controlled to avoid oversaturation. "
					"Edges reveal thin material layers with slight fraying. "
					"Each panel is arranged with clear architectural logic. "
					"The table contains packaging fragments and torn edges."
				),

				"Bungkus Indomie: Crumpled Repair": (
					"A hyper-realistic miniature mosque constructed from crumpled instant noodle packaging, assembled on a rustic wooden table surface. "
					"The structure uses compressed and folded material with visible creases and dents. "
					"Printed graphics distort across the surface, adding visual complexity. "
					"Torn sections are repaired with layered patches and tape. "
					"Gloss is controlled to prevent glare. "
					"The table contains crumpled packaging debris."
				),

				"Bungkus Indomie: Modular Recycled": (
					"A hyper-realistic miniature mosque constructed from modular instant noodle packaging segments arranged precisely on a rustic wooden table surface. "
					"Uniform pieces form structured domes and towers. "
					"Printed colors create patterned repetition. "
					"Each segment retains wrinkles and fine surface wear. "
					"Visible segmentation reinforces modular structure. "
					"The table shows neatly cut packaging pieces."
				),

				"Kayu Lapuk: Layered Panel": (
					"A hyper-realistic miniature mosque constructed from weathered decayed wood panels, assembled on a rustic wooden table surface. "
					"The structure features domes and minarets formed from layered wood pieces. "
					"Surface shows cracks, splinters, and rough grain with deep texture. "
					"Color variation includes faded brown, gray, and natural aging marks. "
					"Edges are irregular with visible fiber separation. "
					"Each panel maintains structural clarity despite decay. "
					"The table contains wood fragments and dust."
				),

				"Kayu Lapuk: Crumpled Repair": (
					"A hyper-realistic miniature mosque constructed from broken and repaired decayed wood pieces. "
					"The structure shows cracks, splits, and patched sections. "
					"Surface texture is rough with deep grain and splintering detail. "
					"Damage is controlled, preserving structure. "
					"The table contains irregular wood debris."
				),

				"Kayu Lapuk: Modular Recycled": (
					"A hyper-realistic miniature mosque constructed from modular decayed wood blocks arranged precisely. "
					"Each block shows cracks, rough grain, and surface aging. "
					"Structured repetition enhances architectural clarity. "
					"The table shows neatly arranged wood pieces."
				),

				"Bata Lapuk: Layered Panel": (
					"A hyper-realistic miniature mosque constructed from weathered brick fragments assembled on a rustic wooden table surface. "
					"The structure features domes and minarets formed from stacked brick pieces. "
					"Surface shows chipped edges, cracks, and powdery texture. "
					"Color variation includes faded red, brown, and gray tones. "
					"Each piece is arranged with structural clarity. "
					"The table contains brick dust and fragments."
				),

				"Bata Lapuk: Crumpled Repair": (
					"A hyper-realistic miniature mosque constructed from broken and repaired brick pieces. "
					"The structure shows cracks, chipped surfaces, and patched areas. "
					"Texture is rough with visible grain and dust. "
					"Damage remains controlled. "
					"The table contains debris and dust."
				),

				"Bata Lapuk: Modular Recycled": (
					"A hyper-realistic miniature mosque constructed from modular brick units arranged precisely. "
					"Each block shows chipped edges and natural wear. "
					"Structured repetition enhances clarity. "
					"The table shows neatly arranged brick pieces."
				),

				"Kayu Jati: Layered Panel": (
					"A hyper-realistic miniature mosque constructed from high-quality teak wood panels assembled on a rustic wooden table surface. "
					"The structure features domes and minarets formed from layered polished wood. "
					"Rich wood grain patterns and deep natural tones are clearly visible. "
					"Surface shows fine texture with subtle aging marks. "
					"Edges are clean with slight natural variation. "
					"Each panel is arranged with precision and balance. "
					"The table contains fine wood dust."
				),

				"Kayu Jati: Craftsmanship": (
					"A hyper-realistic miniature mosque constructed from hand-carved teak wood pieces. "
					"Detailed carving marks, smooth surfaces, and refined grain emphasize craftsmanship. "
					"Natural wood texture remains dominant. "
					"The table contains fine wood shavings."
				),

				"Kayu Jati: Modular Recycled": (
					"A hyper-realistic miniature mosque constructed from modular teak wood blocks arranged precisely. "
					"Uniform pieces form structured architectural elements. "
					"Grain patterns create visual variation. "
					"The table shows neatly cut wood blocks."
				),

				"Kardus Bekas: Structural Layer Pro": (
					"A hyper-realistic miniature mosque constructed from multi-layered cardboard structures, firmly assembled on a rustic wooden table surface, with the base clearly resting on the table. "
					"The structure features domes and minarets built from stacked cardboard sheets with clearly visible layered construction. "
					"Exposed corrugated interiors reveal fluted channels and internal structure with high micro-detail clarity. "
					"Outer surfaces show worn print, faded ink, scratches, and subtle stains from previous use. "
					"Edges are rough with fiber separation, slight fraying, and natural tearing patterns. "
					"Each structural layer is aligned with clear architectural logic, creating strong depth and readability. "
					"Surface variation includes soft compression marks and subtle bending. "
					"Balanced tones prevent flat brown appearance while preserving realistic cardboard color. "
					"The wooden table surface contains cardboard dust, fiber particles, and small torn fragments."
				),

				"Kardus Bekas: Compressed Repair Build": (
					"A hyper-realistic miniature mosque constructed from crushed and reshaped cardboard, assembled on a rustic wooden table surface. "
					"The structure maintains mosque proportions while using compressed, dented, and partially collapsed cardboard forms. "
					"Surface shows deep fold lines, pressure dents, and structural deformation with strong shadow depth. "
					"Torn sections are reinforced with layered cardboard patches, visible tape, and overlapping materials. "
					"Corrugated interiors are exposed along broken edges, revealing internal texture. "
					"Printed surfaces appear distorted and partially worn out. "
					"Damage remains controlled, preserving overall architectural clarity. "
					"Surface detail includes dust, fiber texture, and subtle wear patterns. "
					"The table contains torn cardboard pieces, tape fragments, and debris."
				),

				"Kardus Bekas: Modular Block Engine": (
					"A hyper-realistic miniature mosque constructed from modular cardboard blocks arranged precisely on a rustic wooden table surface. "
					"Uniform geometric cardboard units form domes and towers with strong structural repetition and architectural rhythm. "
					"Each block reveals layered cardboard structure with visible corrugated interiors and fiber texture. "
					"Edges are clean but retain natural irregularities and slight fraying. "
					"Printed markings, faded labels, and subtle stains create variation across modules. "
					"Visible segmentation reinforces modular construction without appearing artificial. "
					"Balanced color density prevents dull or flat appearance while maintaining realistic tones. "
					"The table surface shows neatly cut cardboard pieces, dust, and minimal debris."
				),

				"Sedotan Plastik: Modular Frame": (
					"A hyper-realistic miniature mosque constructed from modular plastic straw segments, firmly assembled on a rustic wooden table surface, with the base clearly resting on the table. "
					"The structure features domes and minarets formed from aligned cylindrical straw tubes arranged in structured repetition. "
					"Hollow interiors of the straws create visible depth and layered geometry. "
					"Different colored straws create controlled visual variation without overwhelming the structure. "
					"Each segment is precisely arranged with clear architectural logic and clean alignment. "
					"Surface shows fine scratches, slight bending, and natural plastic wear. "
					"Balanced reflections prevent excessive glare or artificial shine. "
					"The table surface contains small straw cuttings and fragments."
				),

				"Sedotan Plastik: Linear Layer Build": (
					"A hyper-realistic miniature mosque constructed from layered straw segments arranged in parallel formations on a rustic wooden table surface. "
					"The structure uses horizontal and vertical straw alignment to form walls, domes, and towers. "
					"Linear repetition creates strong architectural rhythm and depth. "
					"Surface detail includes minor scratches, subtle deformation, and realistic plastic texture. "
					"Edges remain slightly imperfect to maintain realism. "
					"Color variation remains controlled and balanced. "
					"The table contains aligned straw pieces and minimal debris."
				),

				"Sedotan Plastik: Structural Bundle": (
					"A hyper-realistic miniature mosque constructed from bundled straw clusters forming structural components. "
					"Multiple straws are grouped tightly to create thicker columns and domes. "
					"Visible gaps between tubes add depth and complexity. "
					"The structure maintains clear mosque proportions with organic modular repetition. "
					"Surface shows subtle bending, wear, and texture variation. "
					"Lighting emphasizes depth inside the hollow tubes. "
					"The table surface contains bundled straw fragments."
				),

				"Karet Gelang: Interwoven Structure": (
					"A hyper-realistic miniature mosque constructed from interwoven rubber bands stretched and layered across a structural frame, firmly placed on a rustic wooden table surface. "
					"The structure features domes and minarets formed through tensioned rubber bands crossing and looping in controlled patterns. "
					"Elastic strands create dynamic curves and structural tension. "
					"Surface shows subtle rubber texture, slight matte finish, and natural stretching marks. "
					"Each band is positioned with clear structural logic, forming stable architectural shapes. "
					"Layered intersections create depth and shadow complexity. "
					"The table surface contains loose rubber bands and minor debris."
				),

				"Karet Gelang: Tension Frame Build": (
					"A hyper-realistic miniature mosque constructed from rubber bands stretched across a rigid frame, forming structural surfaces and domes. "
					"The elastic material creates smooth curved forms with visible tension. "
					"Layered bands form semi-transparent surfaces with controlled density. "
					"Surface shows fine rubber grain and slight wear from stretching. "
					"Each band contributes to the architectural structure through controlled placement. "
					"Lighting highlights tension lines and layered intersections. "
					"The table contains spare rubber bands and fragments."
				),

				"Karet Gelang: Modular Loop System": (
					"A hyper-realistic miniature mosque constructed from repeating rubber band loops arranged in structured modular patterns. "
					"Each loop connects to others, forming domes and towers through repetition and layering. "
					"Elastic forms create organic geometry with consistent rhythm. "
					"Surface detail includes subtle rubber texture and slight deformation. "
					"Visible connections reinforce structural integrity. "
					"Balanced composition prevents chaotic overlap. "
					"The table shows grouped rubber bands and minimal debris."
				),

				"Gelas Plastik Aqua: Transparent Panel": (
					"A hyper-realistic miniature mosque constructed from cut transparent plastic cup panels, firmly assembled on a rustic wooden table surface. "
					"The structure features domes and minarets formed from curved transparent sheets. "
					"Semi-transparent material creates layered depth with soft internal reflections. "
					"Surface shows scratches, slight deformation, and subtle usage marks. "
					"Edges reveal thin plastic thickness with natural irregularities. "
					"Each panel is arranged with clear structural logic. "
					"Balanced reflections prevent glare or overexposure. "
					"The table contains plastic fragments and cut edges."
				),

				"Gelas Plastik Aqua: Crumpled Form Build": (
					"A hyper-realistic miniature mosque constructed from crumpled and reshaped plastic cups, assembled on a rustic wooden table surface. "
					"The structure maintains mosque proportions while using compressed and dented plastic forms. "
					"Surface shows folds, creases, and pressure marks with strong texture depth. "
					"Transparent areas create layered light interaction without excessive shine. "
					"Edges are slightly warped, maintaining realism. "
					"Each section is positioned with controlled structure. "
					"The table contains crumpled plastic fragments."
				),

				"Gelas Plastik Aqua: Hybrid Layer Assembly": (
					"A hyper-realistic miniature mosque constructed from a combination of flat and curved plastic cup segments arranged in layered assembly. "
					"The structure uses both transparent panels and curved forms to build domes and walls. "
					"Material variation creates depth, reflection, and structural complexity. "
					"Surface detail includes scratches, subtle wear, and slight deformation. "
					"Each component is aligned with clear architectural logic. "
					"Balanced lighting enhances transparency without glare. "
					"The table shows mixed plastic pieces and minimal residue."
				),

				"Mix Bekas: Recycled Hybrid Structure": (
					"A hyper-realistic miniature mosque constructed from a combination of used cardboard, plastic bottles, and newspaper, firmly assembled on a rustic wooden table surface, with the base clearly resting on the table. "
					"The main structure is built from layered worn cardboard with visible corrugated interiors, rough edges, and fiber separation. "
					"Transparent plastic bottle panels are integrated as windows and upper structural elements, showing scratches, dents, and label residue. "
					"Newspaper fragments are used as surface layering with visible text, folds, and slight tearing. "
					"The central dome is constructed from crumpled transparent plastic bottle material, forming a semi-transparent layered dome with subtle internal reflections. "
					"All materials show clear signs of prior use: faded prints, scratches, stains, and structural wear. "
					"Each component is arranged with controlled assembly logic, maintaining architectural clarity. "
					"Balanced lighting prevents glare from plastic and avoids flattening cardboard texture. "
					"The table surface contains mixed debris: paper scraps, plastic fragments, and cardboard fibers."
				),

				"Mix Bekas: Industrial Scrap Assembly": (
					"A hyper-realistic miniature mosque constructed from used metal can fragments, rubber bands, and cardboard, assembled on a rustic wooden table surface. "
					"The base structure is formed from layered cardboard panels with rough edges and exposed corrugated interiors. "
					"Metal can pieces are integrated as structural plates, showing dents, scratches, faded paint, and controlled rust patches. "
					"Rubber bands are stretched and interwoven across sections, creating tension-based structural elements and flexible connectors. "
					"The central dome is constructed from layered rusted metal fragments, forming a solid dome with textured oxidation and subtle reflective variation. "
					"Surface detail emphasizes wear: chipped paint, rust layers, stretched rubber, and fiber exposure. "
					"Damage remains controlled, preserving clear mosque proportions. "
					"Reflections are muted and realistic, avoiding excessive shine. "
					"The table contains metal scraps, rubber bands, cardboard debris, and dust."
				),

				"Mix Bekas: Lightweight Patchwork Build": (
					"A hyper-realistic miniature mosque constructed from used plastic sachets, instant noodle packaging, and thin cardboard, assembled on a rustic wooden table surface. "
					"The structure is formed from flexible layered materials with visible folds, wrinkles, and patchwork assembly. "
					"Sachet surfaces show faded branding, scratches, and partial tearing, with foil layers creating subtle reflective variation. "
					"Instant noodle packaging adds colorful but worn graphic elements, distorted across folded surfaces. "
					"Thin cardboard provides structural support with visible layering and rough edges. "
					"The central dome is constructed from tightly folded and layered instant noodle packaging, forming a textured dome with wrinkled surface and controlled color distribution. "
					"All materials show clear signs of usage: creases, stains, faded print, and wear marks. "
					"Each element is arranged with clear structural intent, avoiding chaotic composition. "
					"Balanced lighting controls reflections and preserves texture detail. "
					"The table surface contains mixed packaging fragments, plastic scraps, and fiber debris."
				),

				"KoranKardus + Kubah Jerami": (
					"A hyper-realistic miniature mosque constructed from used newspaper and cardboard, firmly assembled on a rustic wooden table surface. "
					"The structure is built from layered cardboard panels with exposed corrugated interiors and newspaper sheets showing faded text, folds, and slight tearing. "
					"Edges are rough with fiber separation and natural wear from usage. "
					"The central dome is constructed from tightly arranged dry straw, forming a dense organic dome with fine fibrous texture and natural irregularity. "
					"All materials show realistic aging: wrinkles, discoloration, and structural wear. "
					"Balanced lighting enhances texture without flattening detail. "
					"The table contains paper scraps, cardboard fibers, and straw debris."
				),

				"KardusBotol + Kubah Plastik": (
					"A hyper-realistic miniature mosque constructed from used cardboard and plastic bottle material, assembled on a rustic wooden table surface. "
					"The structure uses layered cardboard with visible corrugated channels, rough edges, and slight deformation. "
					"Plastic bottle pieces are integrated into structural sections, showing scratches, dents, and label residue. "
					"The central dome is formed from crumpled transparent plastic bottle material, creating a semi-transparent layered dome with controlled reflections. "
					"All materials show wear, fading, and surface imperfections from prior use. "
					"The table contains cardboard fragments and plastic scraps."
				),

				"KoranJerami + Kubah Jerami": (
					"A hyper-realistic miniature mosque constructed from compressed newspaper and straw elements, assembled on a rustic wooden table surface. "
					"The structure is formed from crumpled newspaper with visible folds, wrinkles, and distorted printed text. "
					"Straw is integrated into the walls, adding fibrous organic texture. "
					"The central dome is fully constructed from tightly packed straw, forming a thick textured dome with fine natural fibers. "
					"Surface shows aging, fading ink, and slight tearing. "
					"The table contains paper scraps and straw fragments."
				),

				"SachetIndomie + Kubah Indomie": (
					"A hyper-realistic miniature mosque constructed from used sachet packaging and instant noodle wrappers, assembled on a rustic wooden table surface. "
					"The structure is formed from layered sachets with wrinkles, scratches, and faded branding. "
					"Foil and plastic layers create controlled reflective variation without glare. "
					"The central dome is constructed from folded instant noodle packaging, forming a wrinkled dome with worn colorful print. "
					"Surface shows clear signs of use including creases and slight tearing. "
					"The table contains packaging fragments and plastic scraps."
				),

				"BotolKoran + Kubah Plastik": (
					"A hyper-realistic miniature mosque constructed from used plastic bottles and newspaper, assembled on a rustic wooden table surface. "
					"The structure combines semi-transparent plastic panels with layered newspaper showing faded text and folds. "
					"Plastic surfaces show scratches, dents, and slight deformation. "
					"The central dome is made from curved transparent plastic bottle material, forming a smooth layered dome with controlled reflections. "
					"All materials show wear and realistic imperfections. "
					"The table contains plastic fragments and paper scraps."
				),

				"GelasKardus + Kubah Gelas": (
					"A hyper-realistic miniature mosque constructed from used plastic cups and cardboard, assembled on a rustic wooden table surface. "
					"The structure uses cardboard as the base with visible layered edges and corrugated texture. "
					"Plastic cup material forms curved structural elements with scratches and dents. "
					"The central dome is formed from a reshaped plastic cup, creating a smooth curved dome with subtle transparency and deformation. "
					"Surface detail includes wear marks, slight warping, and material fatigue. "
					"The table contains plastic fragments and cardboard debris."
				),

				"KardusIndomie + Kubah Kardus": (
					"A hyper-realistic miniature mosque constructed from used cardboard and instant noodle packaging, assembled on a rustic wooden table surface. "
					"The structure is built from layered cardboard panels with visible corrugated interiors and rough edges. "
					"Packaging material adds colorful but worn surface detail with folds and scratches. "
					"The central dome is constructed from layered cardboard pieces, forming a solid dome with visible fiber texture and structural depth. "
					"Surface shows fading, creases, and natural wear. "
					"The table contains cardboard fragments and packaging scraps."
				),

				"SachetKoran + Kubah Sachet": (
					"A hyper-realistic miniature mosque constructed from used sachet packaging and newspaper, assembled on a rustic wooden table surface. "
					"The structure uses layered sachet material with visible wrinkles, scratches, and faded branding combined with newspaper layers. "
					"Printed text and graphics create subtle visual variation. "
					"The central dome is formed from tightly folded sachet material, creating a wrinkled reflective dome with controlled highlights. "
					"All materials show wear, folds, and slight tearing. "
					"The table contains paper scraps and sachet fragments."
				),

				"JeramiKardus + Kubah Jerami": (
					"A hyper-realistic miniature mosque constructed from dry straw and used cardboard, assembled on a rustic wooden table surface. "
					"The structure combines rigid cardboard panels with organic straw layering, creating strong contrast between hard and fibrous textures. "
					"Cardboard shows rough edges and exposed layers, while straw adds fine detail and irregularity. "
					"The central dome is built entirely from dense straw, forming a thick organic dome with high micro-texture. "
					"Surface shows natural aging and wear. "
					"The table contains straw fragments and cardboard fibers."
				),

				"BotolSachet + Kubah Plastik": (
					"A hyper-realistic miniature mosque constructed from used plastic bottles and sachet packaging, assembled on a rustic wooden table surface. "
					"The structure uses flexible plastic layers with visible scratches, wrinkles, and faded branding. "
					"Sachet material adds reflective variation while bottle plastic provides structure. "
					"The central dome is formed from curved plastic bottle segments, creating a smooth semi-transparent dome with subtle deformation. "
					"Surface shows wear, dents, and usage marks. "
					"The table contains plastic fragments and packaging scraps."
				),

				"KoranBotol + Kubah Koran": (
					"A hyper-realistic miniature mosque constructed from used newspaper and discarded plastic bottle material, firmly assembled on a rustic wooden table surface. "
					"The structure is built from layered newspaper sheets with visible folds, creases, faded ink, and partially torn edges. "
					"Plastic bottle fragments are integrated into structural sections, showing scratches, dents, label residue, and slight deformation from prior use. "
					"The central dome is constructed from tightly layered and crumpled newspaper, forming a soft dome with visible text patterns, wrinkles, and uneven compression. "
					"Surface detail emphasizes wear: discoloration, dirt smudges, fiber exposure, and irregular edges. "
					"All materials clearly appear used and aged, with no clean or pristine surfaces. "
					"Balanced lighting preserves texture without flattening detail. "
					"The table contains paper scraps, plastic fragments, and fiber debris."
				),

				"KardusSachet + Kubah Sachet": (
					"A hyper-realistic miniature mosque constructed from used cardboard and discarded sachet packaging, assembled on a rustic wooden table surface. "
					"The structure is formed from layered cardboard panels with exposed corrugated interiors, rough torn edges, and visible compression marks. "
					"Sachet materials are layered across surfaces, showing wrinkles, scratches, faded branding, and partially peeled print. "
					"The central dome is constructed from tightly folded and compressed sachet material, forming a wrinkled reflective dome with distorted graphics and worn surfaces. "
					"Surface detail includes creases, dirt marks, and material fatigue from repeated use. "
					"All elements clearly show signs of wear and aging, avoiding any clean or new appearance. "
					"The table contains cardboard fibers, foil fragments, and packaging debris."
				),

				"KoranGelas + Kubah Gelas": (
					"A hyper-realistic miniature mosque constructed from used newspaper and discarded plastic cups, assembled on a rustic wooden table surface. "
					"The structure combines layered paper with visible folds, wrinkles, and faded printed text, alongside curved plastic cup fragments showing scratches and dents. "
					"Plastic surfaces are slightly cloudy and worn, with subtle deformation and usage marks. "
					"The central dome is formed from a reshaped plastic cup, creating a curved dome with visible stress marks, scratches, and uneven edges. "
					"Surface detail emphasizes aging: paper discoloration, plastic scuffing, and structural wear. "
					"All materials clearly appear used and imperfect. "
					"The table contains paper scraps, plastic fragments, and minor debris."
				),

				"KardusJerami + Kubah Kardus": (
					"A hyper-realistic miniature mosque constructed from used cardboard and dry straw, assembled on a rustic wooden table surface. "
					"The structure uses layered cardboard panels with exposed corrugated interiors, torn edges, and visible fiber separation. "
					"Straw elements are loosely integrated into walls, adding fibrous organic texture with irregular direction and density. "
					"The central dome is constructed from stacked and shaped cardboard layers, forming a rough dome with visible grain, cracks, and structural imperfections. "
					"Surface shows aging, dirt marks, and slight deformation from use. "
					"The table contains straw fragments, cardboard dust, and fiber debris."
				),

				"SachetBotol + Kubah Sachet": (
					"A hyper-realistic miniature mosque constructed from discarded sachet packaging and used plastic bottle fragments, assembled on a rustic wooden table surface. "
					"The structure combines flexible sachet layers with rigid plastic bottle segments, both showing scratches, wrinkles, and wear. "
					"Sachet surfaces display faded branding, creases, and slight tearing, while plastic shows dents and label residue. "
					"The central dome is constructed from tightly folded sachet material, forming a reflective but worn dome with wrinkled texture and distorted print. "
					"Surface detail includes scuff marks, dirt, and material fatigue. "
					"All materials clearly appear used and aged. "
					"The table contains foil scraps, plastic fragments, and debris."
				),

				"KoranIndomie + Kubah Indomie": (
					"A hyper-realistic miniature mosque constructed from used newspaper and instant noodle packaging, assembled on a rustic wooden table surface. "
					"The structure uses layered newspaper with faded text, wrinkles, and slight tearing combined with colorful but worn packaging surfaces. "
					"Packaging shows creases, scratches, and dull areas where print has faded. "
					"The central dome is constructed from folded instant noodle packaging, forming a wrinkled dome with distorted colors and visible wear. "
					"Surface detail emphasizes aging and repeated use. "
					"All materials avoid any clean or glossy appearance. "
					"The table contains paper scraps and packaging debris."
				),

				"BotolJerami + Kubah Jerami": (
					"A hyper-realistic miniature mosque constructed from used plastic bottle fragments and dry straw, assembled on a rustic wooden table surface. "
					"The structure combines rigid plastic with organic straw layering, creating contrast between smooth worn surfaces and fibrous textures. "
					"Plastic shows scratches, dents, and cloudiness from use, while straw appears dry and uneven. "
					"The central dome is built entirely from dense straw, forming a thick fibrous dome with irregular layering and natural variation. "
					"Surface detail includes dirt, wear, and structural imperfection. "
					"The table contains straw debris and plastic fragments."
				),

				"KardusGelas + Kubah Gelas": (
					"A hyper-realistic miniature mosque constructed from used cardboard and plastic cups, assembled on a rustic wooden table surface. "
					"The structure uses cardboard layers with rough edges, visible corrugation, and compression marks. "
					"Plastic cup material forms curved elements with scratches, dents, and slight deformation. "
					"The central dome is formed from a reshaped plastic cup with visible wear, stress marks, and uneven curvature. "
					"Surface shows realistic aging and usage. "
					"The table contains cardboard debris and plastic fragments."
				),

				"KoranKardus + Kubah Janur": (
					"A hyper-realistic miniature mosque constructed from used newspaper and cardboard, firmly assembled on a rustic wooden table surface. "
					"The structure is built from layered newspaper sheets with visible folds, faded text, wrinkles, and torn edges combined with cardboard panels showing exposed corrugated interiors and rough fiber separation. "
					"All surfaces show clear aging: discoloration, creases, dirt smudges, and structural wear from prior use. "
					"The central dome is constructed from woven young coconut leaves (janur), forming a curved dome with layered leaf strips, visible fibers, natural bending, and slight drying at the edges. "
					"The contrast between rigid paper structure and organic leaf dome creates strong visual hierarchy. "
					"Lighting enhances paper texture and leaf fiber without flattening detail. "
					"The table contains paper scraps, cardboard fibers, and leaf fragments."
				),

				"KardusBotol + Kubah Daun Pisang": (
					"A hyper-realistic miniature mosque constructed from used cardboard and plastic bottle fragments, assembled on a rustic wooden table surface. "
					"The structure uses layered cardboard with visible corrugated interiors, torn edges, and compression marks, combined with plastic bottle panels showing scratches, dents, and cloudy wear. "
					"All materials clearly appear used with faded surfaces, stains, and deformation. "
					"The central dome is formed from large banana leaves, layered and slightly folded to create a smooth curved dome with visible veins, tears, and natural texture variation. "
					"The leaf surface shows subtle dryness and edge imperfections, reinforcing realism. "
					"The table contains cardboard debris, plastic fragments, and leaf pieces."
				),

				"SachetKoran + Kubah Daun Kelapa": (
					"A hyper-realistic miniature mosque constructed from used sachet packaging and newspaper, assembled on a rustic wooden table surface. "
					"The structure combines wrinkled sachet surfaces with faded branding and scratched foil layers, alongside newspaper sheets with folds and torn edges. "
					"Surface detail includes creases, dirt marks, and worn textures. "
					"The central dome is constructed from layered green coconut leaves, arranged in overlapping strips forming a dense dome with visible fibers, natural curvature, and slight edge drying. "
					"Leaf texture contrasts with reflective sachet surfaces. "
					"The table contains foil scraps, paper fragments, and leaf debris."
				),

				"BotolKardus + Kubah Janur": (
					"A hyper-realistic miniature mosque constructed from used plastic bottles and cardboard, assembled on a rustic wooden table surface. "
					"The structure features rigid cardboard panels with rough edges and exposed corrugation, combined with plastic bottle elements showing scratches, dents, and label residue. "
					"All materials show wear and aging from prior use. "
					"The central dome is made from woven janur leaves, forming a structured dome with visible interlacing patterns, fine fibers, and natural irregularities. "
					"Surface detail emphasizes both material contrast and realism. "
					"The table contains plastic fragments, cardboard fibers, and leaf strips."
				),

				"KoranIndomie + Kubah Pisang": (
					"A hyper-realistic miniature mosque constructed from used newspaper and instant noodle packaging, assembled on a rustic wooden table surface. "
					"The structure combines layered paper with faded text and wrinkled packaging with worn colorful print and scratches. "
					"Surface detail includes folds, creases, and slight tearing. "
					"The central dome is formed from layered banana leaves, curved naturally with visible veins, slight tears, and uneven edges. "
					"The organic leaf dome contrasts with the synthetic packaging textures. "
					"The table contains paper scraps, packaging fragments, and leaf debris."
				),

				"GelasSachet + Kubah Daun Kelapa": (
					"A hyper-realistic miniature mosque constructed from used plastic cups and sachet packaging, assembled on a rustic wooden table surface. "
					"The structure uses curved plastic surfaces with scratches and dents combined with wrinkled sachet layers. "
					"Surface shows wear, fading, and slight deformation. "
					"The central dome is constructed from layered green coconut leaves, forming a natural dome with visible fibers, bending, and organic layering. "
					"Lighting enhances subtle transparency of plastic and texture of leaves. "
					"The table contains plastic fragments, foil scraps, and leaf pieces."
				),

				"KardusJerami + Kubah Janur": (
					"A hyper-realistic miniature mosque constructed from used cardboard and dry straw, assembled on a rustic wooden table surface. "
					"The structure uses rough cardboard panels with exposed layers and straw elements adding fibrous texture. "
					"Surface shows aging, cracks, and fiber separation. "
					"The central dome is made from woven janur leaves, forming a structured organic dome with visible interlacing and natural variation. "
					"The table contains straw fragments, cardboard dust, and leaf debris."
				),

				"BotolKoran + Kubah Pisang": (
					"A hyper-realistic miniature mosque constructed from used plastic bottle fragments and newspaper, assembled on a rustic wooden table surface. "
					"The structure combines semi-transparent plastic with layered paper showing folds, wrinkles, and faded text. "
					"Plastic surfaces show scratches and cloudiness. "
					"The central dome is formed from banana leaves with visible veins, folds, and slight tearing. "
					"Surface detail emphasizes material contrast and wear. "
					"The table contains plastic and paper debris along with leaf fragments."
				),

				"SachetIndomie + Kubah Janur": (
					"A hyper-realistic miniature mosque constructed from used sachet packaging and instant noodle wrappers, assembled on a rustic wooden table surface. "
					"The structure uses layered flexible materials with wrinkles, scratches, and faded print. "
					"Foil surfaces create subtle reflective variation. "
					"The central dome is constructed from woven janur leaves with visible fibers, layered strips, and natural curvature. "
					"Surface detail shows clear usage and wear. "
					"The table contains packaging scraps and leaf debris."
				),

				"KardusSachet + Kubah Pisang": (
					"A hyper-realistic miniature mosque constructed from used cardboard and sachet packaging, assembled on a rustic wooden table surface. "
					"The structure uses layered cardboard with rough edges and wrinkled sachet surfaces. "
					"Surface shows fading, scratches, and fiber exposure. "
					"The central dome is formed from banana leaves with natural curvature, visible veins, and slight imperfections. "
					"The table contains cardboard fibers, foil scraps, and leaf fragments."
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
			"Kebun Semangka Natural Asri": (
				"The character is seated on a low weathered wooden crate in a lush and naturally grown Indonesian watermelon garden. "
				"The ground is rich dark soil with uneven terrain, mixed with patches of fresh grass, creeping vines, and small wild plants. "
				"Ripe watermelons grow organically across the field with irregular spacing, some partially hidden under leaves, creating a natural layered environment. "
				"Watermelon vines spread freely with varying density, overlapping and intertwining naturally instead of appearing arranged. "
				"Foreground includes scattered leaves, small branches, and a few fallen fruits, adding depth and realism. "
				"In the far background, soft silhouettes of additional plants and distant rural land create depth without distraction. "
				"A gentle natural breeze moves the leaves and vines slightly, making the environment feel alive. "
				"The atmosphere feels calm, fresh, and deeply natural with strong depth separation and controlled visual balance."
			),

			"Kebun Semangka Asri dengan Gubuk": (
				"The character is seated on a low weathered wooden crate beside a simple bamboo gubuk within a naturally grown watermelon garden. "
				"The ground consists of dark soil, patches of grass, and organic debris such as fallen leaves and vine fragments. "
				"Watermelons grow irregularly around the area, some clustered near the gubuk, others spread naturally across the field. "
				"The vines grow freely and partially climb around the bamboo structure, blending the gubuk into the environment. "
				"The bamboo gubuk appears aged and natural, with subtle texture and slight imperfections. "
				"In the background, soft layers of vegetation and distant crops create natural depth. "
				"A light breeze moves leaves and vines gently, adding life to the scene. "
				"The environment feels grounded, peaceful, and naturally integrated with strong subject focus."
			),

			"Kebun Buah Naga Natural Asri": (
				"The character is seated on a low weathered wooden crate in a natural dragon fruit garden with organic growth patterns. "
				"The ground is dark soil with uneven texture, mixed with grass patches and small wild plants. "
				"Dragon fruit plants grow on wooden poles, but with natural irregular spacing and variation, avoiding perfect alignment. "
				"The vines extend outward unevenly, with some hanging lower and others growing more densely, creating visual depth. "
				"Ripe dragon fruits appear in varied positions, some partially hidden among the vines. "
				"Foreground includes subtle organic debris such as dry stems and fallen leaves. "
				"Background fades into layers of similar plants and distant vegetation, maintaining depth without distraction. "
				"The environment feels calm, slightly wild, and naturally alive with strong visual balance."
			),

			"Kebun Buah Naga Asri dengan Gubuk": (
				"The character is seated on a low weathered wooden crate beside a simple bamboo gubuk inside a dragon fruit garden. "
				"Dragon fruit plants surround the structure with organic spacing, some vines leaning or growing toward the gubuk naturally. "
				"The wooden poles vary slightly in height and alignment, avoiding artificial symmetry. "
				"Ripe fruits hang in natural distribution, creating visual rhythm and depth. "
				"The ground is a mix of soil, grass, and scattered organic elements. "
				"The bamboo gubuk blends into the environment with natural aging and texture. "
				"Background vegetation remains soft and layered, enhancing depth. "
				"The atmosphere feels quiet, natural, and harmoniously integrated."
			),

			"Kebun Melon Natural Asri": (
				"The character is seated on a low weathered wooden crate in a naturally grown melon field with organic structure. "
				"The ground is dark soil with uneven terrain, mixed with creeping vines, grass patches, and small plants. "
				"Melons grow along trailing vines with irregular spacing, some resting on the soil while others are partially covered by leaves. "
				"The vines spread naturally with varied density, creating layered visual depth. "
				"Foreground includes subtle debris such as leaves and small plant fragments. "
				"Background vegetation fades softly, maintaining strong depth separation. "
				"The environment feels fresh, grounded, and naturally alive without appearing artificially arranged."
			),

			"Kebun Melon Asri dengan Gubuk": (
				"The character is seated beside a simple bamboo gubuk within a natural melon field. "
				"Melon vines grow around and partially under the structure, blending the gubuk into the environment. "
				"The fruits appear in varied positions with natural spacing, creating a balanced but organic look. "
				"The ground consists of soil, grass patches, and organic debris. "
				"The bamboo structure appears weathered and integrated naturally. "
				"Background layers of vegetation create depth without distraction. "
				"The atmosphere feels calm, natural, and visually grounded."
			),

			"Kebun Labu Natural Asri": (
				"The character is seated on a low weathered wooden crate in a naturally grown pumpkin field. "
				"The ground is dark uneven soil with patches of grass and scattered leaves. "
				"Pumpkins rest on thick vines that spread organically across the ground with irregular density. "
				"Some pumpkins are partially hidden under leaves, creating depth and realism. "
				"The vines overlap and twist naturally, forming layered visual texture. "
				"Foreground includes organic debris such as leaves and stems. "
				"Background fades into soft vegetation layers, maintaining depth and focus. "
				"The environment feels grounded, slightly wild, and naturally balanced."
			),

			"Kebun Labu Asri dengan Gubuk": (
				"The character is seated beside a simple bamboo gubuk within a natural pumpkin field. "
				"Pumpkin vines spread freely around the structure, some reaching toward or around the gubuk. "
				"Pumpkins appear in varied sizes and positions, creating natural distribution. "
				"The ground is textured with soil, grass, and scattered plant debris. "
				"The bamboo gubuk blends into the environment with natural wear and organic integration. "
				"Background vegetation remains soft and layered. "
				"The atmosphere feels calm, natural, and visually cohesive."
			),

			"Kebun Mangga Natural Asri": (
				"The character is seated on a low handcrafted bamboo table with a tightly woven natural surface, placed in a lush and organically grown mango orchard in a rural Indonesian setting. "
				"The ground is composed of rich dark soil with uneven terrain, mixed with patches of soft grass, dry leaves, and scattered organic debris such as small twigs and fallen mango stems. "
				"Mango trees grow with irregular spacing, their thick trunks and dense leafy canopies forming layered overhead coverage that filters light naturally. "
				"Some branches extend lower with visible ripe mangoes hanging in varied positions, while several fallen fruits rest on the ground, partially hidden among leaves and grass. "
				"The foreground includes detailed elements such as curled dry leaves, small broken branches, and subtle soil texture variations, creating strong tactile realism. "
				"The midground features overlapping tree canopies and hanging fruit clusters, forming rich natural depth and visual layering. "
				"In the background, additional rows of mango trees gradually fade into softer silhouettes, maintaining depth without drawing focus. "
				"The bamboo table shows natural imperfections, slight curvature, and fiber texture, reinforcing handcrafted authenticity. "
				"A gentle natural breeze subtly moves leaves and thin branches, creating a calm, living atmosphere. "
				"The overall environment feels shaded, cool, and deeply natural with strong spatial depth and controlled visual balance, ensuring the subject remains dominant."
			),

			"Kebun Durian Natural Asri": (
				"The character is seated on a thick solid wood slab table with rough natural edges, placed in a dense durian grove with strong vertical tree presence. "
				"The ground is layered with dry leaves, rough soil, and organic debris, creating a textured and slightly uneven natural surface. "
				"Tall durian trees rise irregularly with thick trunks and heavy foliage forming a dense canopy above, creating a deeper shaded environment. "
				"Several durian fruits lie on the ground in varied positions, some partially covered by leaves, adding natural randomness and realism. "
				"The foreground includes sharp leaf textures, broken stems, and uneven soil details, enhancing tactile depth. "
				"The midground shows tree trunks and layered foliage with complex overlapping shadows and natural density. "
				"In the background, darker silhouettes of additional trees create depth and a slightly enclosed atmosphere without overpowering the subject. "
				"The wooden slab table appears heavy, with visible grain, cracks, and natural imperfections, reinforcing material realism. "
				"Subtle movement of leaves and small branches from natural wind adds life to the scene without distraction. "
				"The overall environment feels dense, grounded, slightly heavy, and deeply immersive, with strong contrast between light and shadow while maintaining detail visibility."
			),

			"Kebun Anggur Natural Asri": (
				"The character is seated on a clean yet natural bamboo table beneath a loosely structured grape vine canopy in a rural garden setting. "
				"Grape vines grow overhead on simple wooden supports, arranged organically with slight irregularity, allowing clusters of grapes to hang at varied heights and positions. "
				"The ground consists of compact soil mixed with grass patches, fallen leaves, and subtle organic debris. "
				"The foreground includes hanging grape clusters, overlapping leaves, and fine stem details, creating strong depth and visual layering. "
				"The midground features vine structures and leaf coverage forming a semi-open canopy that filters light naturally, producing soft layered shadows. "
				"In the background, additional vine rows and vegetation fade gradually, maintaining depth without distraction. "
				"The bamboo table shows fine texture, natural color variation, and handcrafted imperfections. "
				"A gentle breeze causes slight movement in leaves and hanging grape clusters, adding a calm and living dynamic. "
				"The overall environment feels airy, balanced, and naturally structured, with clear spatial separation and a peaceful atmosphere."
			),
			"Kebun Apel Natural Asri": (
				"The character is seated on a rustic wooden plank table made from uneven aged boards, placed in a naturally grown apple orchard. "
				"The ground consists of compact dark soil mixed with patches of grass, scattered dry leaves, and fallen apples in various stages of freshness. "
				"Apple trees grow with slightly irregular spacing, their branches extending outward with visible clusters of apples hanging at different heights. "
				"Some fruits hang low while others are partially hidden within dense foliage, creating natural depth and variation. "
				"The foreground includes detailed elements such as leaf piles, apple stems, and small soil imperfections, enhancing tactile realism. "
				"The midground features overlapping branches and fruit clusters forming layered visual structure and depth. "
				"In the background, rows of apple trees fade gradually into softer silhouettes, maintaining depth without distraction. "
				"The wooden table shows visible grain, cracks, and rough edges, reinforcing handcrafted authenticity. "
				"A gentle natural breeze subtly moves leaves and branches, creating a calm and living atmosphere. "
				"The environment feels fresh, slightly structured yet organic, with balanced density and strong subject separation."
			),

			"Kebun Buah Naga Natural Asri": (
				"The character is seated on a low bamboo table with woven surface, placed in a naturally grown dragon fruit garden. "
				"The ground is composed of dark soil with uneven texture, mixed with grass patches and scattered dry stems. "
				"Dragon fruit plants grow on wooden poles with natural variation in height and spacing, avoiding perfect alignment. "
				"The vines extend outward unevenly, some hanging lower while others wrap around the supports, creating organic complexity. "
				"Ripe dragon fruits appear in varied positions, some clearly visible while others are partially hidden within the vines. "
				"The foreground shows detailed elements such as dry stems, fallen leaves, and subtle soil texture variations. "
				"The midground features layered poles and vines forming strong vertical and horizontal structure. "
				"In the background, additional plants fade softly into distance, maintaining depth without distraction. "
				"The bamboo table shows fine woven texture and slight imperfections. "
				"A soft natural breeze moves vines and leaves gently, adding life to the scene. "
				"The environment feels calm, slightly wild, and naturally balanced with strong visual depth."
			),

			"Kebun Melon Natural Asri": (
				"The character is seated on a low wooden slab table with natural uneven edges, placed in a naturally grown melon field. "
				"The ground consists of dark soil mixed with creeping vines, grass patches, and small organic debris. "
				"Melon plants spread across the ground with irregular density, their vines overlapping and intertwining naturally. "
				"Melons rest on the soil in varied positions, some partially covered by leaves while others are fully visible. "
				"The foreground includes detailed vine textures, leaves, and small plant fragments, creating strong tactile realism. "
				"The midground features layered vine growth forming natural depth and complexity. "
				"In the background, the field continues with softened detail, maintaining strong depth separation. "
				"The wooden slab table shows natural grain patterns and slight cracks. "
				"A gentle breeze subtly moves leaves and vines, adding a calm dynamic to the environment. "
				"The overall scene feels grounded, fresh, and naturally alive without appearing artificially arranged."
			),

			"Kebun Kiwi Natural Asri": (
				"The character is seated on a simple bamboo table with smooth top surface, placed in a kiwi garden with natural growth patterns. "
				"The ground is a mix of soil, grass patches, and scattered plant debris such as leaves and stems. "
				"Kiwi vines spread across wooden supports with irregular spacing and organic overlap, forming a semi-dense canopy. "
				"The leaves create layered textures with varying density, while fruits hang subtly within the foliage. "
				"The foreground includes overlapping leaves, vine textures, and small debris, adding depth and realism. "
				"The midground shows structural supports and vine layers creating visual complexity. "
				"In the background, the vegetation fades softly, maintaining depth without distraction. "
				"The bamboo table shows natural tone variation and handcrafted imperfections. "
				"A light breeze moves leaves gently, creating a calm and enclosed atmosphere. "
				"The environment feels slightly dense, natural, and visually cohesive."
			),

			"Kebun Pepaya Natural Asri": (
				"The character is seated on a rough wooden table made from thick planks, placed in a papaya garden with natural spacing. "
				"The ground consists of dark soil with patches of grass and scattered dry leaves. "
				"Papaya trees grow tall and slender with irregular spacing, their fruits clustered along the trunks at different heights. "
				"Some fruits appear ripe while others remain unripe, adding natural variation. "
				"The foreground includes leaf fragments, soil texture, and small organic debris. "
				"The midground features multiple papaya trees creating vertical rhythm and depth. "
				"In the background, additional trees fade into softer silhouettes. "
				"The wooden table shows rough texture and natural imperfections. "
				"A gentle breeze subtly moves leaves and branches. "
				"The environment feels open, warm, and naturally structured."
			),

			"Kebun Salak Natural Asri": (
				"The character is seated on a low bamboo table with woven structure, placed in a dense salak garden. "
				"The ground is covered with soil, dry leaves, and natural debris from the plants. "
				"Salak plants grow close to the ground with dense, spiky foliage forming a compact and layered environment. "
				"Clusters of salak fruit appear near the base of the plants, partially hidden within the leaves. "
				"The foreground shows detailed textures of leaves, stems, and soil. "
				"The midground features dense plant layering creating strong depth. "
				"In the background, the vegetation becomes softer and darker, enhancing depth. "
				"The bamboo table shows natural fiber texture and slight irregularities. "
				"A subtle breeze moves the leaves slightly. "
				"The environment feels dense, enclosed, and richly textured."
			),

			"Kebun Pisang Natural Asri": (
				"The character is seated on a thick bamboo table with a smooth flat surface, placed in a lush banana grove. "
				"The ground is a mix of dark soil, moist patches, fallen banana leaves, and organic debris. "
				"Banana trees grow densely with large wide leaves forming layered overhead coverage, some leaves torn naturally with visible texture. "
				"Banana clusters hang at varying heights, some partially hidden by leaves while others are clearly visible. "
				"The foreground includes large leaf fragments, plant fibers, and soil texture variations, enhancing realism. "
				"The midground shows overlapping banana trunks and leaf layers creating strong depth. "
				"In the background, additional banana trees fade into softer silhouettes. "
				"The bamboo table shows natural fiber detail and slight imperfections. "
				"A gentle breeze moves large leaves slowly, creating a calm and immersive atmosphere. "
				"The environment feels humid, dense, and naturally alive."
			),

			"Kebun Jeruk Natural Asri": (
				"The character is seated on a rustic wooden plank table with visible grain and uneven edges, placed in a citrus orchard. "
				"The ground consists of compact soil mixed with grass patches and scattered fallen oranges. "
				"Orange trees grow with moderate spacing, their branches filled with dense green leaves and visible fruit clusters. "
				"Some oranges hang low while others are partially hidden within foliage, creating natural variation. "
				"The foreground includes fallen fruit, leaves, and subtle soil detail. "
				"The midground shows tree rows with overlapping branches forming layered depth. "
				"In the background, orchard rows fade gradually into softer shapes. "
				"The wooden table appears aged with cracks and natural imperfections. "
				"A light breeze gently moves leaves and small branches. "
				"The environment feels fresh, open, and naturally balanced."
			),

			"Kebun Tomat Natural Asri": (
				"The character is seated on a low wooden slab table placed in a naturally grown tomato garden. "
				"The ground is composed of dark soil with small stones, plant debris, and patches of grass. "
				"Tomato plants grow with irregular spacing, supported by simple wooden sticks and natural ties. "
				"Clusters of tomatoes appear at different ripeness stages, some hanging low, others hidden among leaves. "
				"The foreground includes stems, leaves, and soil texture details. "
				"The midground shows layered plant rows with varied density. "
				"In the background, additional plants fade softly. "
				"The wooden slab table shows rough texture and natural grain. "
				"A gentle breeze subtly moves leaves and stems. "
				"The environment feels grounded, organic, and naturally cultivated."
			),

			"Kebun Nanas Natural Asri": (
				"The character is seated on a sturdy bamboo table with woven top surface, placed in a natural pineapple field. "
				"The ground is dry soil mixed with grass patches and plant debris. "
				"Pineapple plants grow low and dense with sharp leaves forming repeating patterns across the field. "
				"Fruits appear at the center of each plant with natural variation in size and position. "
				"The foreground includes sharp leaf textures and soil details. "
				"The midground shows repeating plant formations creating visual rhythm. "
				"In the background, the field fades gradually into softer detail. "
				"The bamboo table shows fine woven detail and natural imperfections. "
				"A subtle breeze causes slight leaf movement. "
				"The environment feels structured yet natural and slightly dry."
			),

			"Kebun Stroberi Natural Asri": (
				"The character is seated on a low wooden table with smooth worn surface, placed in a strawberry garden. "
				"The ground is a mix of soil, small plants, and organic debris. "
				"Strawberry plants grow close to the ground with dense leaves and visible small fruits. "
				"Some strawberries are ripe and visible, while others remain partially hidden beneath foliage. "
				"The foreground includes fine leaf textures and small fruit details. "
				"The midground shows dense plant coverage forming layered depth. "
				"In the background, additional rows fade softly. "
				"The wooden table appears smooth but aged with subtle imperfections. "
				"A light breeze gently moves small leaves. "
				"The environment feels soft, fresh, and naturally detailed."
			),

			"Kebun Wortel Natural Asri": (
				"The character is seated on a rough wooden plank table placed in a carrot field. "
				"The ground is loose soil with visible root texture and small plant debris. "
				"Carrot plants grow with thin green tops emerging from the soil with natural spacing. "
				"Some carrots are partially visible above the ground, adding realism. "
				"The foreground includes soil clumps, roots, and leaf fragments. "
				"The midground shows rows of plants with natural irregularity. "
				"In the background, the field fades into soft vegetation. "
				"The wooden table shows rough edges and grain detail. "
				"A gentle breeze moves thin leaves slightly. "
				"The environment feels open, earthy, and grounded."
			),

			"Kebun Alpukat Natural Asri": (
				"The character is seated on a thick wooden slab table with natural edges, placed in an avocado orchard. "
				"The ground consists of soil, grass patches, and scattered leaves. "
				"Avocado trees grow with irregular spacing, forming dense foliage and layered canopy. "
				"Some fruits hang within branches while others are partially hidden. "
				"The foreground includes leaves and soil detail. "
				"The midground shows overlapping tree structures. "
				"In the background, trees fade softly into depth. "
				"The wooden table shows natural grain and imperfections. "
				"A light breeze gently moves leaves. "
				"The environment feels shaded, calm, and naturally rich."
			),

			"Kebun Cabai Natural Asri": (
				"The character is seated on a low bamboo table placed in a chili garden. "
				"The ground is soil mixed with plant debris and small stones. "
				"Chili plants grow with natural spacing, supported by simple wooden sticks. "
				"Chili fruits appear in various stages of ripeness, creating color variation. "
				"The foreground includes leaves, stems, and soil texture. "
				"The midground shows plant rows forming layered depth. "
				"In the background, additional plants fade softly. "
				"The bamboo table shows natural texture and slight imperfections. "
				"A gentle breeze moves leaves slightly. "
				"The environment feels lively, natural, and slightly vibrant."
			),

			"Kebun Kelapa Natural Asri": (
				"The character is seated on a rough wooden table placed in a coconut grove. "
				"The ground consists of sand, soil, dry leaves, and coconut husk debris. "
				"Tall coconut trees rise with irregular spacing, creating strong vertical composition. "
				"Some coconuts lie on the ground while others hang high above. "
				"The foreground includes husk fragments and soil texture. "
				"The midground shows tree trunks and scattered coconuts. "
				"In the background, trees fade into distance. "
				"The wooden table shows weathered texture. "
				"A soft breeze moves palm leaves above. "
				"The environment feels open, airy, and tropical."
			),

			"Sawah Terasering Natural Asri": (
				"The character is seated on a low bamboo table with woven surface, placed on the edge of a lush terraced rice field. "
				"The foreground shows detailed soil edges, small grass patches, and water reflections along the terrace boundary. "
				"The rice plants grow densely with natural variation in height and direction, creating a rich textured surface. "
				"The midground reveals multiple layers of terraced fields descending gradually, each layer filled with vibrant rice plants and thin water channels. "
				"Subtle reflections appear in the shallow water between rows, adding depth and realism. "
				"In the background, distant terraces fade into softer shapes, maintaining strong depth separation without distraction. "
				"The bamboo table shows fine woven detail and natural imperfections. "
				"A gentle breeze moves the rice plants in soft waves, creating a calm and living atmosphere. "
				"The environment feels expansive, fresh, and deeply natural with strong visual layering."
			),

			"Sawah Pinggir Irigasi Alami": (
				"The character is seated on a rustic wooden plank table near a small flowing irrigation canal in a rice field. "
				"The foreground includes wet soil, small stones, grass patches, and flowing water with subtle ripples and reflections. "
				"Rice plants grow thickly along both sides of the canal with natural irregularity and density. "
				"The midground features extended rice fields intersected by narrow water paths, creating natural patterns and depth. "
				"The water surface reflects surrounding plants and light softly. "
				"In the background, fields extend outward with soft fading vegetation and distant rural elements. "
				"The wooden table shows visible grain, cracks, and aged texture. "
				"A soft breeze moves both the rice plants and water surface gently. "
				"The environment feels calm, grounded, and rich with natural detail."
			),

			"Sawah Tengah Hamparan Luas": (
				"The character is seated on a low wooden slab table placed in the middle of a wide open rice field. "
				"The foreground shows dense rice plants with visible leaf texture and subtle soil beneath. "
				"The plants vary slightly in height and direction, avoiding uniformity and enhancing realism. "
				"The midground expands into a wide uninterrupted field of rice, forming a continuous textured surface. "
				"In the background, the horizon line is defined by distant vegetation and faint silhouettes of rural landscape. "
				"The wooden slab table shows natural grain patterns and slight imperfections. "
				"A gentle breeze creates soft wave-like movement across the rice field. "
				"The environment feels open, airy, and immersive with strong natural continuity."
			),

			"Sawah Dekat Pohon Teduh": (
				"The character is seated on a thick wooden table under a large tree beside a rice field. "
				"The foreground includes shaded soil, fallen leaves, and small plant details under the tree canopy. "
				"Rice plants grow just beyond the shaded area, creating contrast between light and shadow. "
				"The midground shows a balanced mix of open rice field and partial tree coverage, forming layered visual depth. "
				"In the background, additional trees and fields fade softly into distance. "
				"The wooden table shows rough texture, visible grain, and natural wear. "
				"The tree leaves move gently with wind, casting soft shifting shadows. "
				"The environment feels cool, calm, and naturally sheltered."
			),

			"Sawah Jalan Setapak Alami": (
				"The character is seated on a bamboo table placed beside a narrow natural footpath cutting through a rice field. "
				"The foreground shows the footpath made of compact soil with grass edges and small stones, adding realistic detail. "
				"Rice plants grow on both sides of the path with slight variation in density and height. "
				"The midground follows the path as it curves gently into the distance, guiding visual depth naturally. "
				"In the background, the path fades into softer vegetation and distant landscape. "
				"The bamboo table shows natural texture and handcrafted detail. "
				"A gentle breeze moves the rice plants softly along the path. "
				"The environment feels intimate, grounded, and visually engaging."
			),

			"Gubuk Bambu Hijau Segar": (
				"The character is seated on a smooth bamboo table with a woven top surface inside a freshly built gubuk made from green bamboo. "
				"The bamboo poles appear vibrant with natural green tones, slightly glossy, and tightly tied with visible fiber bindings. "
				"The ground consists of compact soil mixed with fresh grass patches and small organic debris. "
				"The foreground shows bamboo textures, rope bindings, and subtle imperfections in the structure. "
				"The gubuk stands open on all sides, allowing a clear view of surrounding greenery and soft vegetation layers. "
				"In the midground, natural plants and crops grow with organic spacing, creating depth. "
				"The background fades into soft rural landscape with trees and vegetation. "
				"A gentle breeze moves surrounding leaves and slightly vibrates hanging bamboo elements. "
				"The environment feels fresh, clean, and naturally alive with strong depth separation."
			),

			"Gubuk Bambu Kuning Kering": (
				"The character is seated on a rustic bamboo table inside a gubuk constructed from dried yellow bamboo. "
				"The bamboo poles show warm yellow tones with slight cracks and natural aging, creating a dry textured appearance. "
				"The ground is a mix of dry soil, scattered leaves, and light organic debris. "
				"The foreground includes visible bamboo fibers, rope ties, and rough structural joints. "
				"The gubuk structure is slightly uneven, enhancing realism and handcrafted feel. "
				"The midground shows open farmland or garden with soft plant distribution. "
				"The background fades into distant vegetation and open land. "
				"A light breeze moves dry leaves and creates subtle movement in the structure. "
				"The environment feels warm, grounded, and slightly dry but natural."
			),

			"Gubuk Bambu Lapuk Tua": (
				"The character is seated on a rough wooden table inside an old gubuk made from aged and weathered bamboo. "
				"The bamboo structure shows faded color, cracks, darkened spots, and signs of long-term exposure. "
				"The ground is covered with soil, dry leaves, and decaying organic material. "
				"The foreground shows worn bamboo textures, broken edges, and rough joints. "
				"The gubuk appears slightly tilted and imperfect, enhancing realism. "
				"The midground contains dense vegetation and natural plant growth reclaiming parts of the structure. "
				"The background fades into darker trees and layered foliage. "
				"A soft breeze moves leaves and loose elements subtly. "
				"The environment feels aged, quiet, and deeply natural."
			),

			"Gubuk Bambu Campuran Alami": (
				"The character is seated on a bamboo table with natural woven texture inside a gubuk made from mixed bamboo materials of different ages. "
				"Some bamboo poles appear fresh and green, while others are dry and slightly aged, creating natural variation. "
				"The ground is a mix of soil, grass patches, and scattered plant debris. "
				"The foreground includes detailed bamboo textures, knots, and binding elements. "
				"The gubuk structure shows slight irregularity in shape and alignment. "
				"The midground contains surrounding crops or plants growing organically. "
				"The background fades into soft vegetation and rural landscape. "
				"A gentle breeze moves leaves and surrounding plants. "
				"The environment feels balanced, natural, and visually rich."
			),

			"Gubuk Bambu Atap Daun Rumbia": (
				"The character is seated on a low wooden plank table inside a bamboo gubuk with a roof made from layered dried palm leaves. "
				"The bamboo frame supports the thick layered roof, which shows natural fiber texture and slight irregular edges. "
				"The ground is covered with soil, grass patches, and fallen leaf fragments from the roof. "
				"The foreground shows detailed textures of bamboo, leaf fibers, and natural bindings. "
				"The midground reveals surrounding fields or plants visible through the open sides. "
				"The background fades into soft vegetation and distant landscape. "
				"A gentle breeze causes slight movement in the leaf roof edges and surrounding plants. "
				"The environment feels shaded, cool, and naturally protected."
			),

			"Gubuk Kayu Sederhana Pedesaan": (
				"The character is seated on a thick wooden slab table inside a simple rural gubuk made from rough wooden planks. "
				"The wood shows natural grain, cracks, and uneven edges, creating a raw handcrafted appearance. "
				"The ground is compact soil with scattered leaves and organic debris. "
				"The foreground includes detailed wood textures, joints, and structural imperfections. "
				"The midground shows surrounding farmland or vegetation. "
				"The background fades into soft rural scenery with trees and plants. "
				"A soft breeze moves leaves and subtle elements in the environment. "
				"The atmosphere feels grounded, simple, and naturally authentic."
			),

			"Gubuk Setengah Terbuka Pinggir Sawah": (
				"The character is seated on a bamboo table inside a semi-open gubuk located at the edge of a rice field. "
				"The structure is made from bamboo and wood combination with open sides allowing a clear view of the surrounding field. "
				"The ground is a mix of soil, grass, and scattered plant debris. "
				"The foreground shows bamboo textures, structural joints, and small natural details. "
				"The midground reveals rice plants growing densely with visible movement. "
				"The background fades into extended rice fields and distant vegetation. "
				"A gentle breeze moves both rice plants and parts of the gubuk structure. "
				"The environment feels open, airy, and strongly connected to nature."
			),

			"Hutan Tropis Lembap Lebat": (
				"The character is seated on a thick wooden slab table with natural rough edges, placed deep within a dense tropical rainforest. "
				"The foreground is filled with wet soil, fallen leaves, exposed roots, and small plants with high moisture detail. "
				"Large tropical plants with broad leaves overlap and layer naturally, creating strong depth and complexity. "
				"The midground shows dense vegetation with intertwined vines, tree trunks, and layered foliage forming a visually rich environment. "
				"Water droplets cling to leaves and surfaces, enhancing realism and humidity. "
				"In the background, tall trees rise and fade into darker green tones, maintaining depth without distraction. "
				"The wooden table shows wet texture, visible grain, and natural imperfections. "
				"Subtle movement of leaves from a soft breeze creates a calm yet alive atmosphere. "
				"The environment feels humid, dense, immersive, and deeply natural."
			),

			"Hutan Tropis Dekat Aliran Air": (
				"The character is seated on a smooth bamboo table beside a small natural stream within a tropical rainforest. "
				"The foreground includes wet stones, flowing water, moss-covered surfaces, and small plants growing near the stream edges. "
				"The water flows gently with visible ripples and reflections, adding motion and realism. "
				"The midground features layered vegetation including ferns, vines, and tree trunks surrounding the water source. "
				"Large leaves hang at different heights, partially covering the scene and creating depth. "
				"In the background, dense forest vegetation fades softly into shadow. "
				"The bamboo table shows natural texture and slight moisture. "
				"A gentle breeze moves leaves and lightly disturbs the water surface. "
				"The environment feels fresh, cool, and naturally dynamic."
			),

			"Hutan Tropis Cahaya Menyusup": (
				"The character is seated on a rustic wooden plank table placed within a tropical forest where light subtly filters through the canopy. "
				"The foreground shows detailed forest floor with soil, roots, fallen leaves, and small plants. "
				"Beams of filtered light pass through gaps in the dense canopy, creating soft contrast and depth across the scene. "
				"The midground contains layered foliage, tree trunks, and hanging vines forming a complex structure. "
				"Light touches certain leaves while others remain in shadow, enhancing visual separation. "
				"In the background, tall trees fade into softer silhouettes. "
				"The wooden table shows natural wear, grain, and imperfections. "
				"A gentle breeze causes slight leaf movement. "
				"The environment feels mystical, calm, and naturally cinematic."
			),

			"Hutan Tropis Lantai Akar Besar": (
				"The character is seated on a low bamboo table placed on a forest floor dominated by large exposed tree roots. "
				"The foreground shows thick intertwined roots, moist soil, moss, and small plants growing between root structures. "
				"The midground features large tree trunks rising vertically with dense foliage above. "
				"Vines wrap around trees and roots, adding organic complexity. "
				"Leaves and debris are scattered naturally across the uneven ground. "
				"In the background, the forest becomes denser and darker, enhancing depth. "
				"The bamboo table shows natural fiber texture and subtle imperfections. "
				"A soft breeze moves leaves gently. "
				"The environment feels grounded, ancient, and deeply natural."
			),

			"Hutan Tropis Terbuka Semi Kanopi": (
				"The character is seated on a wooden slab table placed in a slightly more open section of a tropical rainforest. "
				"The foreground includes soil, grass patches, and scattered leaves with less density than deeper forest areas. "
				"The midground shows trees spaced more loosely, allowing more openness and visual breathing room. "
				"Plants still grow abundantly but with less overlap, creating a balanced environment. "
				"In the background, the forest gradually becomes denser again, maintaining depth. "
				"The wooden table shows visible grain and natural wear. "
				"A gentle breeze moves leaves and smaller plants. "
				"The environment feels airy, fresh, and naturally balanced while still rich in detail."
			),

			"Kebun Sayuran Campuran Natural Asri": (
				"The character is seated on a low bamboo table with woven surface in a mixed vegetable garden with organic growth patterns. "
				"The foreground shows dark soil with uneven texture, small stones, trimmed leaves, and scattered plant debris. "
				"Various vegetables such as leafy greens, chilies, and tomatoes grow with irregular spacing, creating a naturally layered environment. "
				"The midground features loosely structured rows with slight variation in height and density, avoiding perfect symmetry. "
				"In the background, additional crops and soft vegetation fade gradually into depth. "
				"The bamboo table shows fine fiber texture and natural imperfections. "
				"A gentle breeze moves leaves subtly, creating a calm and living atmosphere. "
				"The environment feels fresh, productive, and naturally balanced."
			),

			"Kebun Sayuran Organik Liar": (
				"The character is seated on a rough wooden slab table in a slightly overgrown organic vegetable garden. "
				"The foreground includes thick soil, weeds, small wild plants, and scattered leaves. "
				"Vegetables grow freely with uneven density, some areas denser while others more sparse, creating a natural wild look. "
				"The midground shows overlapping plant growth and varied textures forming visual depth. "
				"In the background, the garden fades into soft vegetation and natural land. "
				"The wooden slab table shows cracks, grain, and rough edges. "
				"A soft breeze gently moves leaves and stems. "
				"The environment feels alive, slightly untamed, and deeply natural."
			),

			"Kebun Sayuran Tertata Alami": (
				"The character is seated on a smooth wooden plank table in a well-maintained vegetable garden. "
				"The ground consists of compact soil, light grass patches, and trimmed plant debris. "
				"Vegetables are arranged in soft rows with slight irregularity, maintaining natural appearance without strict symmetry. "
				"The midground shows layered plant rows with consistent spacing but natural variation. "
				"In the background, additional crops fade into soft silhouettes. "
				"The wooden table shows subtle wear and natural grain texture. "
				"A gentle breeze moves leaves lightly. "
				"The environment feels calm, productive, and harmonious."
			),

			"Kebun Sayuran Lembap Subur": (
				"The character is seated on a bamboo table in a lush and slightly moist vegetable garden. "
				"The foreground shows damp soil, small puddles, plant roots, and fresh leaves with visible moisture. "
				"Vegetables grow densely with rich green tones and layered foliage. "
				"The midground features overlapping plant growth forming strong depth and texture. "
				"In the background, the garden continues into softer vegetation layers. "
				"The bamboo table shows slight moisture and natural texture. "
				"A soft breeze moves leaves gently. "
				"The environment feels fertile, humid, and naturally vibrant."
			),

			"Kebun Sayuran Dekat Jalan Tanah": (
				"The character is seated on a rustic wooden table beside a narrow dirt path running through a vegetable garden. "
				"The foreground includes the path with compact soil, grass edges, and small stones. "
				"Vegetables grow on both sides of the path with natural variation in spacing and density. "
				"The midground follows the path as it extends into the garden, creating natural perspective. "
				"In the background, plants fade softly into depth. "
				"The wooden table shows aged texture and natural imperfections. "
				"A gentle breeze moves leaves and small plants. "
				"The environment feels grounded, natural, and visually engaging."
			),

			"Taman Bunga Warna Alami": (
				"The character is seated on a bamboo table surrounded by a natural flower garden with soft color variation. "
				"The foreground includes soil, small plants, petals, and fallen leaves scattered naturally. "
				"Flowers grow in mixed clusters with irregular spacing, creating organic color layering. "
				"The midground shows overlapping flower patches with varied height and density. "
				"In the background, the garden fades into soft floral silhouettes. "
				"The bamboo table shows natural woven detail. "
				"A gentle breeze moves petals and stems softly. "
				"The environment feels calm, colorful, and naturally balanced."
			),

			"Taman Bunga Liar Asri": (
				"The character is seated on a wooden slab table in a slightly wild flower field. "
				"The foreground shows grass, small plants, scattered petals, and uneven soil texture. "
				"Flowers grow freely with mixed species and irregular density, creating a natural wild aesthetic. "
				"The midground features layered plant growth with overlapping colors and textures. "
				"In the background, the field fades into soft vegetation. "
				"The wooden table shows rough grain and imperfections. "
				"A light breeze moves flowers gently. "
				"The environment feels free, natural, and visually rich."
			),

			"Taman Bunga Tertata Natural": (
				"The character is seated on a smooth wooden table in a well-maintained flower garden. "
				"The foreground includes trimmed plants, soil, and scattered petals. "
				"Flowers are arranged in soft patterns with slight irregularity to maintain natural appearance. "
				"The midground shows layered flower beds with balanced spacing. "
				"In the background, the garden fades into soft floral layers. "
				"The wooden table shows subtle wear and clean surface. "
				"A gentle breeze moves petals and leaves. "
				"The environment feels calm, neat, and naturally elegant."
			),

			"Taman Bunga Dekat Air": (
				"The character is seated on a bamboo table near a small water feature within a flower garden. "
				"The foreground includes water reflections, stones, soil, and surrounding plants. "
				"Flowers grow around the water edge with natural variation and density. "
				"The midground features layered plant growth with water adding depth and movement. "
				"In the background, the garden fades softly into vegetation. "
				"The bamboo table shows natural texture and slight imperfections. "
				"A gentle breeze moves flowers and lightly disturbs the water surface. "
				"The environment feels fresh, calm, and naturally dynamic."
			),

			"Taman Bunga Semi Teduh": (
				"The character is seated on a wooden table under partial tree shade within a flower garden. "
				"The foreground shows shaded soil, leaves, and small plants with soft light contrast. "
				"Flowers grow in mixed clusters with some areas in light and others in shadow. "
				"The midground shows layered plants and partial canopy coverage. "
				"In the background, trees and flowers fade softly. "
				"The wooden table shows natural grain and texture. "
				"A soft breeze moves leaves and petals gently. "
				"The environment feels cool, calm, and naturally layered."
			),

			"Kolam Ikan Alami Batu dan Lumut": (
				"The character is seated on a thick wooden slab table placed beside a natural fish pond surrounded by stones and moss. "
				"The foreground includes wet rocks, small puddles, patches of moss, and subtle water reflections with gentle ripples. "
				"The pond water is slightly clear with visible fish moving beneath the surface, creating soft distortion and motion. "
				"Plants grow naturally around the edges, including small ferns and low vegetation. "
				"The midground shows the full pond structure with irregular stone arrangement and layered plant growth. "
				"In the background, additional greenery and natural vegetation fade softly into depth. "
				"The wooden slab table shows visible grain, moisture, and natural imperfections. "
				"A gentle breeze creates subtle movement on the water surface and surrounding leaves. "
				"The environment feels calm, cool, and naturally immersive."
			),

			"Kolam Ikan Pinggir Taman Asri": (
				"The character is seated on a bamboo table with woven surface near a well-maintained garden fish pond. "
				"The foreground shows water edges with grass, small plants, and reflections of surrounding greenery. "
				"The pond water is calm with occasional ripples and visible fish beneath the surface. "
				"The midground features balanced plant arrangement around the pond, including flowering plants and decorative greenery. "
				"The pond shape is slightly structured but still natural in appearance. "
				"In the background, garden elements fade softly into depth. "
				"The bamboo table shows fine woven texture and slight imperfections. "
				"A light breeze moves leaves and gently disturbs the water surface. "
				"The environment feels fresh, balanced, and naturally elegant."
			),

			"Kolam Ikan Koi Air Jernih": (
				"The character is seated on a smooth wooden plank table beside a clear koi fish pond. "
				"The foreground includes water surface reflections, small stones, and subtle ripple patterns. "
				"Koi fish with varied patterns swim slowly beneath the clear water, visible with gentle distortion. "
				"The midground shows clean pond edges with natural stone lining and minimal plant coverage. "
				"The water clarity enhances depth and visual detail. "
				"In the background, surrounding plants and garden elements fade softly. "
				"The wooden table shows smooth surface with subtle wear and grain texture. "
				"A gentle breeze creates soft ripple movement across the water. "
				"The environment feels calm, refined, and visually clean."
			),

			"Kolam Ikan Desa Tradisional": (
				"The character is seated on a rough wooden table near a traditional village fish pond. "
				"The foreground shows muddy soil, grass patches, and uneven ground near the pond edge. "
				"The pond water is slightly murky with natural coloration, with fish occasionally visible near the surface. "
				"The midground includes simple natural surroundings such as plants, wooden structures, and organic elements. "
				"The pond edges are irregular and unrefined, enhancing realism. "
				"In the background, rural vegetation and simple landscape fade into depth. "
				"The wooden table shows rough texture, cracks, and aged appearance. "
				"A soft breeze moves surrounding plants gently. "
				"The environment feels grounded, simple, and authentically rural."
			),

			"Kolam Ikan dengan Tanaman Air": (
				"The character is seated on a bamboo table beside a pond filled with aquatic plants. "
				"The foreground shows water surface with floating leaves, subtle ripples, and reflections. "
				"Aquatic plants such as lily pads and small floating vegetation cover parts of the pond surface. "
				"Fish move beneath the plants, occasionally visible through gaps. "
				"The midground features layered aquatic growth and natural pond edges with mixed vegetation. "
				"In the background, surrounding greenery fades softly into depth. "
				"The bamboo table shows natural fiber texture and slight irregularities. "
				"A gentle breeze moves floating leaves and creates light ripple effects. "
				"The environment feels calm, lush, and naturally dynamic."
			),

			"Pinggir Hutan Pinus": (
				"The character is seated at the edge of a pine forest. "
				"Pine trees rise with controlled spacing and natural depth. "
				"Fallen needles cover the ground with subtle texture. "
				"Light creates soft shadows across the forest floor. "
				"The atmosphere is cool, balanced, and visually grounded."
			),

			"Ladang Teh": (
				"The character is seated at the edge of a tea plantation. "
				"Tea bushes form gentle rows with controlled density across the terrain. "
				"A light mist softens the background without reducing clarity. "
				"In the distance, workers harvest quietly. "
				"The environment feels fresh and balanced with controlled light diffusion."
			),

			"Pantai Desa Kecil": (
				"The character is seated on a quiet village beach. "
				"Soft waves move gently along the shore with controlled reflections. "
				"Coconut trees line the coast with natural spacing. "
				"Boats rest quietly in the background. "
				"The atmosphere is calm and visually balanced with controlled brightness."
			),

			"Pinggir Gunung Kecil": (
				"The character is seated on a low weathered wooden crate on a foothill with a mountain view. "
				"Green slopes and rocky textures appear with controlled visual depth. "
				"Wildflowers grow naturally with balanced color presence. "
				"A distant waterfall is subtly visible. "
				"The environment feels fresh and visually controlled with balanced lighting."
			),

			"Lembah Kecil Desa": (
				"The character is seated in a quiet small valley surrounded by hills. "
				"Green fields and scattered trees fill the space with controlled density. "
				"A narrow river flows through the valley with soft reflections. "
				"Distant houses appear subtly with light smoke. "
				"The atmosphere is calm and visually balanced with natural depth."
			),

			"Teras Rumah Jati": (
				"The character is seated on a spacious wooden terrace of a traditional Javanese house. "
				"Dark jati wood textures appear rich with controlled highlights. "
				"Simple furniture is placed naturally across the space. "
				"Clothes hang lightly in the background. "
				"The lighting is soft and controlled, emphasizing texture and warmth."
			),

			"Rumah Ukiran": (
				"The character is seated on a carved wooden terrace of a traditional house. "
				"Intricate carvings appear with strong texture and controlled contrast. "
				"The structure maintains a balanced visual presence without overpowering the subject. "
				"Soft light enhances the carved details. "
				"The environment feels elegant and visually controlled."
			),

			"Rumah Bambu Hijau": (
				"The character is seated beside a simple house made of fresh green bamboo. "
				"Bamboo textures appear natural with controlled color intensity. "
				"Green vines climb gently along the structure. "
				"Potted plants are placed subtly near the entrance. "
				"The lighting is balanced with soft highlights and clear subject focus."
			),

			"Halaman Depan Rumah": (
				"The character is seated in the front yard of a modest village house. "
				"Swept earth ground appears clean with subtle texture. "
				"Small plants and flowers grow naturally near the entrance. "
				"A wooden gate stands quietly in the background. "
				"The environment is warm and visually balanced with controlled light."
			),

			"Halaman Belakang Rumah": (
				"The character is seated in the backyard of a village house. "
				"A small vegetable plot grows with controlled density near the wall. "
				"Clothes hang naturally with soft movement. "
				"The space feels practical and grounded. "
				"The lighting remains soft and balanced with clear subject separation."
			),

			"Pekarangan Rumah dengan Pohon Mangga": (
				"The character is seated under a large mango tree in the yard. "
				"The tree provides natural shade with controlled light filtering through the leaves. "
				"Fallen leaves and fruits scatter subtly on the ground. "
				"The space feels calm and naturally balanced. "
				"The lighting emphasizes shade and depth without over-brightness."
			),

			"Halaman Samping Rumah": (
				"The character is seated in the side yard of the house. "
				"Potted plants and herbs line the wall with controlled arrangement. "
				"Drying herbs hang lightly from a rack. "
				"The space feels quiet and functional. "
				"The environment remains visually balanced with soft lighting."
			),

			"Teras Belakang Rumah": (
				"The character is seated on the back wooden terrace of the house. "
				"Weathered wood textures appear with natural detail and controlled highlights. "
				"Simple tools and baskets are placed neatly in the corner. "
				"The space feels calm and private. "
				"The lighting remains soft and cinematic."
			),

			"Halaman Rumah dengan Tempat Cuci": (
				"The character is seated near an outdoor washing area. "
				"A stone basin and buckets appear with natural texture. "
				"Wet clothes hang nearby with subtle movement. "
				"The environment feels practical and grounded. "
				"The lighting is balanced with controlled reflections."
			),

			"Pekarangan Rumah dengan Tanaman Obat": (
				"The character is seated in a yard filled with medicinal plants. "
				"Herbs grow in controlled rows with natural variation. "
				"A wooden rack holds drying leaves with subtle detail. "
				"The environment feels fragrant and calm. "
				"The lighting maintains clarity and controlled color depth."
			),

			"Ruang Tamu Rumah Jati": (
				"The character is seated in a traditional jati wood living room. "
				"Wood textures appear rich with controlled contrast. "
				"Simple furniture is arranged naturally around the space. "
				"Soft light enters through the windows. "
				"The environment feels warm and visually balanced."
			),

			"Dapur Rumah Kayu": (
				"The character is seated in a simple wooden kitchen. "
				"A traditional stove and utensils appear with natural detail. "
				"Fresh ingredients rest on a wooden surface. "
				"The space feels functional and grounded. "
				"The lighting is soft with controlled highlights."
			),

			"Kamar Tidur Nenek": (
				"The character is seated on a simple wooden bed in a modest bedroom. "
				"Fabric textures appear soft with natural folds. "
				"A wardrobe and mirror stand quietly in the room. "
				"Light filters gently through the window. "
				"The atmosphere feels quiet and intimate with balanced lighting."
			),

			"Ruang Keluarga Kecil": (
				"The character is seated in a small family room. "
				"Simple furniture and floor seating appear naturally arranged. "
				"Photos and objects hang subtly on the walls. "
				"Light enters softly from the side. "
				"The environment is cozy and visually controlled."
			),

			"Serambi Dalam": (
				"The character is seated in the inner serambi of the house. "
				"Wood textures and pillars appear with controlled detail. "
				"Rolled mats are placed neatly in the corner. "
				"Soft diffused light enters from the side. "
				"The atmosphere is calm and traditional with balanced lighting."
			),

			"Ruang Makan Sederhana": (
				"The character is seated at a simple dining table. "
				"Wooden furniture appears naturally arranged. "
				"Utensils and plates are placed subtly. "
				"Light enters through the window with soft contrast. "
				"The environment feels everyday and visually balanced."
			),

			"Sudut Doa Rumah": (
				"The character is seated in a quiet prayer corner. "
				"A prayer mat and small wooden stand are placed neatly. "
				"Soft light illuminates the space gently. "
				"The environment feels calm and spiritual. "
				"The lighting is soft with strong focus on the subject."
			),

			"Sudut Jahit Nenek": (
				"The character is seated near a sewing area. "
				"A sewing machine and fabric pieces appear with natural detail. "
				"Threads and tools are placed subtly around. "
				"Light falls gently on the workspace. "
				"The environment feels warm and personal with balanced lighting."
			),

			"Ruang Depan Dekat Pintu": (
				"The character is seated near the main entrance inside the house. "
				"A wooden door and simple storage elements appear naturally. "
				"Daily items hang subtly on the wall. "
				"Light enters from the doorway with controlled brightness. "
				"The space feels welcoming and visually balanced."
			),

			"Kamar Belakang Rumah": (
				"The character is seated in a back bedroom. "
				"A simple bed and furniture appear with natural texture. "
				"A window provides soft incoming light. "
				"The space feels quiet and private. "
				"The lighting remains balanced and controlled."
			),

			"Hutan Hujan Tropis Sepi": (
				"The character is seated on a low weathered wooden crate in a dense tropical rainforest. "
				"Thick green foliage surrounds the scene with layered depth and controlled density. "
				"Moist ground covered with fallen leaves and subtle natural textures. "
				"Soft light filters through the canopy creating gentle shadow patterns. "
				"The environment is quiet, immersive, and visually controlled with balanced lighting."
			),

			"Tepi Danau Berkabut": (
				"The character is seated near the edge of a calm lake surrounded by light mist. "
				"Still water reflects the muted surroundings with controlled brightness. "
				"Low vegetation and smooth stones line the shoreline. "
				"The mist softens distant elements without reducing clarity. "
				"The atmosphere feels serene, isolated, and visually balanced."
			),

			"Padang Rumput Luas": (
				"The character is seated on a grassy plain with gently rolling terrain. "
				"Soft grass textures move subtly with natural variation. "
				"Scattered trees appear in the far distance with controlled spacing. "
				"The sky provides soft, even illumination without harsh brightness. "
				"The environment is open but visually controlled with strong depth."
			),

			"Pinggir Tebing Batu": (
				"The character is seated near the edge of a rocky cliff overlooking a vast landscape. "
				"Rough stone textures appear detailed with natural imperfections. "
				"Distant terrain fades softly into the background with atmospheric depth. "
				"The lighting is directional but controlled, enhancing surface contrast. "
				"The environment feels dramatic yet balanced with clear subject focus."
			),

			"Gurun Pasir Halus": (
				"The character is seated on a low wooden crate in a wide desert of fine sand. "
				"Smooth sand dunes form gentle curves with controlled highlights. "
				"Subtle wind patterns create natural surface textures. "
				"The lighting is warm but controlled, avoiding excessive glare. "
				"The atmosphere is quiet, minimal, and visually clean."
			),

			"Pantai Sepi Berbatu": (
				"The character is seated on a rocky shoreline by a quiet sea. "
				"Waves move gently against the stones with soft reflections. "
				"Dark rocks and wet surfaces create rich texture contrast. "
				"The horizon remains calm with no visual distractions. "
				"The environment is peaceful, grounded, and visually balanced."
			),

			"Hutan Pinus Berkabut": (
				"The character is seated among tall pine trees in a misty forest. "
				"Pine trunks rise vertically with controlled spacing and depth. "
				"The forest floor is covered with needles and subtle texture layers. "
				"Mist diffuses the background softly without flattening contrast. "
				"The lighting is soft, cool, and cinematic."
			),

			"Jalan Tanah Sepi": (
				"The character is seated on a quiet dirt path surrounded by nature. "
				"The path stretches into the distance with soft perspective depth. "
				"Grass and small plants grow along the edges in controlled distribution. "
				"The lighting remains balanced with no excessive highlights. "
				"The environment feels isolated and calm."
			),

			"Goa Batu Alami": (
				"The character is seated inside a natural stone cave. "
				"Rough cave walls show detailed textures with natural depth. "
				"Light enters from the cave opening, creating controlled contrast. "
				"Shadows remain soft and layered without losing detail. "
				"The atmosphere is enclosed, quiet, and cinematic."
			),

			"Padang Kabut Pagi": (
				"The character is seated in an open field covered with early morning fog. "
				"Low vegetation appears softly through the mist with controlled visibility. "
				"The fog diffuses light evenly without washing out details. "
				"Distant shapes fade naturally into the background. "
				"The environment feels calm, soft, and visually balanced."
			),

			"Interior Rumah Joglo Mewah": (
				"The character is seated on a low wooden platform inside a grand traditional Javanese joglo house. "
				"Massive carved wooden pillars rise symmetrically with intricate traditional patterns. "
				"Polished dark wood floor reflects light subtly with rich texture detail. "
				"Open interior space with layered depth and structured composition. "
				"Soft natural light enters from the sides, creating balanced highlights and controlled shadows."
			),

			"Interior Rumah Kayu Klasik Elegan": (
				"The character is seated in a spacious classic wooden interior with refined craftsmanship. "
				"Dark wooden walls and beams show deep grain textures with natural imperfections. "
				"Minimalist furniture is placed with intentional spacing for visual balance. "
				"Subtle decorative elements enhance the atmosphere without clutter. "
				"The lighting is soft and directional, emphasizing texture and depth."
			),

			"Interior Rumah Bambu Estetik Modern": (
				"The character is seated inside a modern bamboo house with clean architectural design. "
				"Smooth bamboo surfaces form walls and ceiling with precise alignment. "
				"Natural fiber textures and woven details add subtle complexity. "
				"The space feels open yet controlled with strong structural lines. "
				"Soft diffused light enhances the organic materials without overexposure."
			),

			"Interior Rumah Minimalis Kayu Modern": (
				"The character is seated in a modern minimalist wooden house interior. "
				"Clean wooden panels with smooth matte finish create a refined look. "
				"Furniture is minimal with clear spacing and strong composition. "
				"Neutral tones dominate with subtle texture variations. "
				"The lighting is controlled and balanced, maintaining sharp detail and depth."
			),

			"Interior Rumah Tradisional Ukiran Detail": (
				"The character is seated in a traditional house interior filled with detailed wood carvings. "
				"Intricate carved panels cover walls and pillars with high texture fidelity. "
				"Ornamental details appear rich but controlled without visual overload. "
				"The space feels dense yet visually structured. "
				"Soft directional light enhances carvings with strong micro-contrast."
			),

			"Interior Ruang Tengah Rumah Mewah Desa": (
				"The character is seated in the central room of a refined village house. "
				"High ceiling structure creates vertical depth with visible wooden beams. "
				"Floor surfaces show natural wear with detailed texture. "
				"Furniture and objects are arranged with subtle balance. "
				"The lighting is natural and controlled, keeping the subject dominant."
			),

			"Interior Rumah Batu Alam Artistik": (
				"The character is seated inside a house built from natural stone materials. "
				"Stone walls display rough textures with layered surface depth. "
				"Wooden elements contrast with stone, adding warmth to the composition. "
				"The interior feels solid and grounded with strong tactile presence. "
				"Light enters selectively, creating controlled highlights and deep shadows."
			),

			"Interior Rumah Tua Vintage Artistik": (
				"The character is seated inside an old vintage house with aged materials. "
				"Worn wooden surfaces and faded textures create rich visual character. "
				"Subtle imperfections add realism without visual noise. "
				"The space feels nostalgic and layered with natural depth. "
				"The lighting is soft and slightly directional, enhancing texture detail."
			),

			"Interior Rumah Jepang Tradisional": (
				"The character is seated inside a traditional Japanese-style interior. "
				"Sliding wooden panels and tatami flooring create clean geometric structure. "
				"Minimalist design emphasizes balance and empty space. "
				"Natural textures appear subtle but refined. "
				"The lighting is soft and diffused, maintaining calm visual harmony."
			),

			"Interior Loft Kayu Industrial": (
				"The character is seated in a wooden loft with subtle industrial elements. "
				"Exposed beams and structured layout create strong architectural depth. "
				"Wood surfaces mix with raw textures like metal and concrete accents. "
				"The space feels open but controlled with intentional composition. "
				"The lighting is directional and cinematic, enhancing contrast and material detail."
			),

			"Halaman Rumah Joglo Luas": (
				"The character is seated on a low wooden bench in the spacious front yard of a traditional joglo house. "
				"Wide packed earth ground with subtle texture and natural irregularities. "
				"Large wooden structure stands behind with visible carved details and deep shadows. "
				"A few trees provide partial shade with controlled light filtering through leaves. "
				"The environment is open but visually balanced with strong subject focus."
			),

			"Teras Rumah dengan Taman Rapi": (
				"The character is seated on a wooden terrace facing a neatly arranged garden. "
				"Small plants and flowers grow in controlled composition with clean spacing. "
				"Stone path runs through the garden with subtle texture detail. "
				"The house structure frames the background with natural depth. "
				"Lighting is soft and controlled, enhancing color without overexposure."
			),

			"Halaman Rumah dengan Kolam Ikan": (
				"The character is seated beside a small fish pond in the house yard. "
				"Still water reflects surrounding elements with controlled brightness. "
				"Stone edges and aquatic plants add texture without visual clutter. "
				"The house wall stands behind with natural material detail. "
				"The environment feels calm with balanced light and soft reflections."
			),

			"Samping Rumah dengan Jalan Tanah": (
				"The character is seated beside a narrow dirt path next to the house. "
				"Rough ground texture shows natural wear and subtle variation. "
				"Side wall of the house displays material detail and aging surfaces. "
				"Small plants grow along the edge in controlled distribution. "
				"The lighting is directional but balanced, maintaining strong depth."
			),

			"Belakang Rumah dengan Area Kayu": (
				"The character is seated in the backyard where stacked wood and tools are arranged neatly. "
				"Wood textures show natural grain and variation with strong detail. "
				"The house structure provides a grounded background with subtle shadow depth. "
				"The area feels functional but visually controlled. "
				"Lighting is soft with clear separation between subject and environment."
			),

			"Halaman Rumah dengan Pohon Besar": (
				"The character is seated under a large tree in the house yard. "
				"Thick trunk and branches create strong natural structure with deep texture. "
				"Leaves filter light softly, producing controlled shadow patterns. "
				"The house appears partially behind the tree with balanced visibility. "
				"The environment feels shaded, calm, and visually grounded."
			),

			"Teras Rumah Menghadap Sawah": (
				"The character is seated on a wooden terrace overlooking open rice fields. "
				"The house structure frames the foreground with strong composition. "
				"Rice fields stretch outward with controlled depth and soft perspective. "
				"No activity appears in the distance, maintaining visual calm. "
				"The lighting is natural and balanced, preserving clarity and contrast."
			),

			"Halaman Rumah dengan Batu Alam": (
				"The character is seated on a low stone surface in a yard designed with natural rock elements. "
				"Large stones create layered composition with rich surface texture. "
				"Ground transitions between soil and stone with natural variation. "
				"The house stands behind with subtle architectural detail. "
				"The lighting emphasizes texture while remaining controlled and soft."
			),

			"Teras Rumah dengan Pilar Kayu": (
				"The character is seated on a terrace supported by large wooden pillars. "
				"Pillars show deep carved detail and strong vertical presence. "
				"The floor surface reflects light subtly with fine texture. "
				"Open space beyond the terrace adds depth without distraction. "
				"The environment is structured and cinematic with controlled lighting."
			),

			"Halaman Rumah dengan Jalan Batu": (
				"The character is seated near a stone pathway leading to the house. "
				"Irregular stones form a natural path with strong texture detail. "
				"Surrounding ground has controlled vegetation and subtle variation. "
				"The house appears as a solid backdrop with balanced visibility. "
				"The lighting remains even, highlighting textures without glare."
			),

			"Ruang Kerja Kayu Ukir Tradisional": (
				"The character is seated inside a traditional wood carving workspace within a wooden house. "
				"Rough wooden walls and beams display deep grain texture with visible aging and natural imperfections. "
				"Hand-carved wooden ornaments and tools are arranged on a sturdy workbench with controlled detail density. "
				"Wood shavings scatter lightly across the floor, adding subtle texture without clutter. "
				"Directional natural light enters from the side, creating strong micro-contrast and controlled shadows."
			),

			"Ruang Kerja Jahit Tradisional Kayu": (
				"The character is seated in a traditional sewing workspace inside a wooden house. "
				"Aged wooden walls and floor show rich texture and natural wear. "
				"An old sewing machine sits on a wooden table with fabric and threads arranged in a controlled composition. "
				"Folded cloth and small tools add layered detail without visual overload. "
				"Soft directional light highlights textures while maintaining balanced contrast."
			),

			"Ruang Kerja Anyaman Bambu": (
				"The character is seated inside a bamboo weaving workspace within a wooden house. "
				"Wooden walls and bamboo materials create layered organic textures. "
				"Half-finished woven baskets and raw bamboo strips are arranged neatly with controlled density. "
				"The floor shows natural texture with subtle material variation. "
				"Light filters softly through gaps, producing controlled highlights and shadow depth."
			),

			"Ruang Kerja Perkakas Kayu Tradisional": (
				"The character is seated in a traditional woodworking space inside a rustic wooden house. "
				"Heavy wooden beams and walls show deep texture and aged surface detail. "
				"Hand tools such as chisels, hammers, and carving tools are placed in an organized manner. "
				"Work surfaces show wear marks and natural imperfections. "
				"Directional light enhances texture contrast without overexposure."
			),

			"Ruang Kerja Lukis Tradisional": (
				"The character is seated in a traditional painting workspace inside a wooden house. "
				"Wooden walls and floor provide a warm textured background. "
				"Canvas, brushes, and paint containers are arranged with controlled visual balance. "
				"Subtle paint stains add realism without cluttering the scene. "
				"Soft natural light highlights surfaces with gentle contrast."
			),

			"Ruang Kerja Batik Tradisional": (
				"The character is seated in a traditional batik workspace inside a wooden house. "
				"Wooden structures display detailed grain and aged texture. "
				"Batik cloth hangs neatly with intricate patterns visible in controlled arrangement. "
				"Tools and wax containers are placed carefully with subtle detail layering. "
				"Warm directional light enhances pattern detail and texture depth."
			),

			"Interior Rumah Kayu Tua Detail Tinggi": (
				"The character is seated inside an old wooden house with high texture detail. "
				"Walls, beams, and floor show cracked surfaces, deep grain, and natural aging. "
				"Subtle imperfections add realism without overwhelming the composition. "
				"The space feels grounded with strong tactile presence. "
				"Soft directional light creates controlled highlights and deep shadow separation."
			),

			"Interior Rumah Kayu Rustic Natural": (
				"The character is seated inside a rustic wooden house with natural construction. "
				"Uneven wooden planks and beams show organic structure and raw texture. "
				"Minimal objects are placed to maintain visual clarity and focus. "
				"The environment feels raw but controlled. "
				"Lighting remains balanced with strong texture emphasis."
			),

			"Interior Rumah Kayu dengan Meja Kerja": (
				"The character is seated at a wooden work table inside a detailed wooden house. "
				"The table surface shows scratches, grain, and natural wear. "
				"Wooden walls and beams create layered depth and strong structure. "
				"Small tools and materials are placed with controlled visual density. "
				"Directional light enhances surface detail and maintains subject dominance."
			),

			"Interior Rumah Kayu Gelap Dramatis": (
				"The character is seated inside a dimly lit wooden house interior. "
				"Dark wooden textures absorb light, creating strong contrast and depth. "
				"Limited light sources create focused highlights on key surfaces. "
				"Shadows remain deep but detailed without losing texture. "
				"The atmosphere is dramatic, intimate, and cinematic."
			)

        }

		# --- 4. MASTER AUDIO & SOULFUL EXPRESSION (ULTRA STABLE VOICE SYSTEM) ---
        MASTER_AUDIO_STYLE = {
    		"Logat_Nenek": [
        		"Elderly village grandmother with thick rural kampung accent, soft thin old voice, calm and weary delivery",           # Normal tua
        		"Very old frail grandma with gentle soft Javanese accent, whispery thin voice, slow and delicate",                    # Sangat lembut
        		"Frail 92-year-old grandmother with strong rural kampung accent, raspy weak voice, very slow and exhausted",         # Paling tua & lemah
        		"91+ year old nenek tua with soft natural Indonesian accent, quiet tired voice, gentle and fragile",                 # Lebih halus
        		"Elderly thin grandmother with slightly husky kampung accent, shaky fragile voice, slow and weak",                   # Kurus & gemetar
        		"Small elderly grandma with warm soft kampung accent, breathy tired voice, calm and gentle"                          # Kecil & hangat
    		],
        	"Logat_Kakek": [
            	"Voice of a 92-year-old Javanese village grandfather, heavy rural 'Medhok' accent. Voice: EXTREMELY THIN RASP, high-pitched age-cracks. Voice must sound physically weak and village-authentic.",
            	"Frail elderly Javanese kakek, thick rural accent. Voice: Weak, quivering, and hollow. Pacing: Inconsistent speed with audible struggle for breath between phrases.",
            	"90+ year old Javanese kakek tua, rural accent. Voice: High vocal jitter, thin and papery quality, physically exhausted. Performance: Intonation is tired, medhok, and resigned.",
            	"Skeletal old Javanese grandfather, rough 'Medhok' kampung accent. Voice: Thin but gravelly, high-pitched trembling, and very slow. NO bapak-bapak depth.",
            	"Elderly Javanese grandfather, dying rural breath voice. Voice: Fragile, high-pitched age-rasp, quiet and deeply weary. Pace: Very hesitant and emotionally broken."
        	],
			"Mood": [
				"Tired, resigned, and quietly sad with a hint of loneliness",
        		"Gentle sorrow mixed with sincere pasrah and soft vulnerability",
        		"Heavy sadness wrapped in sincere pasrah and weary acceptance",
        		"Fragile melancholic resignation, tired but still gently longing for kindness",
        		"Soft sadness with a hint of loneliness and quiet pleading",
        		"Weary and ikhlas, carrying years of silent endurance",
        		"Calm but emotionally drained, speaking with quiet resignation"
    		],
    		"Physical Action": [
        		"Resting shaky, bone-thin hands near the mosque, then slowly looking up at the lens with heavy lids and a fragile, weary gaze.",
        		"Gently touching the miniature with trembling fingers, eyes shifting slowly from the work to the camera with a soft, resigned expression.",
        		"Keeping weak hands flat on the table near the mosque, head slightly tilted, meeting the camera's gaze with a stoic but heartbreaking stare.",
        		"One hand hovers near the central dome, trembling slightly, while the character looks at the lens with a tired, silent pleading look.",
        		"Sitting very still, hands resting weakly near the object, then slowly rotating the head to look at the camera with hollow, sad eyes.",
        		"Fingertips resting on the wooden table near the miniature, gaze lifting very slowly from the object to meet the camera with a resigned look."
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
                "[ VISUAL CORE: ANALOG CINEMA ] EXTREME 8K RAW DOCUMENTARY FILM - SHOT ON KODAK VISION3 500T 35MM: "
                "Maximum organic realism, heavy film grain, razor-sharp optical texture. NATURAL COLOR PROFILE: "
                "Warm skin tones with deep subsurface scattering and realistic blood-vessel undertones. "
                "ZERO AI SMOOTHING, NO digital haze, NO overexposure. ULTRA-HIGH MICRO-CONTRAST: "
                "Deep tonal separation with rich, dense blacks and weathered highlights. "
                "SURFACE PRIORITY: Every wrinkle, skin pore, age spot, and hair fiber must be hyper-detailed and tactile."
            )

            final_ai_prompt = (
                f"{GLOBAL_QUALITY_LOCK}\n\n"
                
    			f"[ SUBJECT PRIORITY ]\n"
    			f"- The handcrafted miniature mosque is the absolute main subject — dead-center frame dominance.\n"
    			f"- Razor-sharp 8K focus on the miniature mosque. Character face, eyes, hands, deep wrinkles also fully sharp.\n"
    			f"- All materials must appear worn, aged, imperfect — never clean or new.\n"
    			f"- Clear edge separation between surfaces. No muddy texture overlap.\n\n"

    			f"[ CAMERA & CINEMATOGRAPHY ]\n"
    			f"- 85mm cinema lens, f/1.4. EXTREME CLOSE-UP.\n"
    			f"- Strict eye-level axis: camera, the object, and character on the same horizontal plane.\n"
    			f"- Natural handheld breathing movement: VERY SLOW organic micro-tremors with an almost imperceptible, slow push-in to the character's gaze.\n\n"

    			f"[ LIGHTING & COLOR ]\n"
    			f"- Kodak 5219 High Contrast Profile: Deep crushed shadows, weathered highlights.\n"
    			f"- Low-angle directional daylight, warm but not amber — controlled golden quality without orange flooding.\n"
    			f"- Light from one dominant side: strong depth and surface contour, no harsh glare.\n"
    			f"- NO overhead light, NO flat lighting, NO reddish glow, NO amber tint.\n\n"

    			f"[ CHARACTER DNA ]\n"
    			f"{soul_desc}\n"
    			f"{gender_lock}\n"
    			f"Wardrobe: {baju_desc}\n"
				f"MANDATORY: Raw hyper-realistic elderly skin with visible pores, deep natural wrinkles, age spots, and shaky hand veins.\n"
    			f"Sharp, clear, and detailed face with natural micro-expressions. NO face smoothing, NO plastic skin, NO generic old face.\n\n"

    			f"[ ENVIRONMENT ]\n"
    			f"{env_detail}\n"
    			f"- Background supports the subject — must not compete with or overpower the miniature.\n"
    			f"- Lighting consistent with main subject: same directional daylight, no conflicting sources.\n\n"

    			f"[ PERFORMANCE & ATMOSPHERE ]\n"
    			f"Action: {aksi_final}\n"
    			f"Mood & delivery: {mood_final}\n\n"

    			f"[ THE VOICE: ULTRA-AGED 'KEPRET' PROTOCOL ]\n"
    			f"Voice profile: {logat_final}\n"

    			f"[ SPOKEN DIALOG ]\n"
				f"\"{user_dialog}\"\n\n"

    			f"[ AUDIO RULES ]\n"
    			f"- AUDIO ONLY. STRICTLY NO TEXT ON SCREEN.\n"
    			f"- NO background music, NO BGM, NO ambient sound, NO sound effects.\n"
    			f"- ONLY the character's raw spoken voice and natural breathing. Pure voice audio. Nothing else.\n\n"

				f"OBJECT:\n"
    			f"{deskripsi_teknis}\n\n"

    			f"[ NEGATIVE PROMPT ]\n"
    			f"Tears, crying, weeping, background music, BGM, soundtrack, cinematic score, instrumental, ambient music, "
    			f"orange tint, amber glow, reddish light, sunset red, warm color flooding, "
    			f"pale skin, washed-out color, grey skin, white haze, overexposure, sun glare, "
    			f"digital smoothing, AI look, CGI texture, plastic skin, over-smooth face, "
    			f"blurry background, excessive bokeh, high angle, low angle, wide shot, text on screen\n"
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
