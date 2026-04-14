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
            # ========================== KELOMPOK NENEK (Teduh & Berwibawa) ==========================
            "Nenek Aminah": (
                "A kind-hearted elderly Javanese woman, strictly aged 75-80 years old, with a soft oval face. "
                "The skin is deeply weathered with pronounced wrinkles, saggy cheeks, and thin 'papery' texture typical of an 80-year-old. "
                "Her expression is gentle and serene, with a slight, warm but weary smile. "
                "Warm bronze skin tone with natural age spots (lentigines) and sun-kissed glowing patches. "
                "Her eyes are watery, clear, and full of wisdom, with heavy hooded eyelids and deep laugh lines. "
                "Neat, very thin snow-white hair visible under her headscarf. "
                "The overall look is peaceful, frail yet dignified, and motherly. "
                "Hyper-realistic skin texture, 8k resolution, maintaining a soft and approachable look without being harsh."
            ),
            "Nenek Siti": (
                "A joyful, petite Javanese elder, strictly 75-80 years old, with a plump, round face and aged rosy undertones. "
                "The skin is deeply weathered with many fine, crossing wrinkles and visible sagging at the jawline. "
                "She has very deep dimples and pronounced nasolabial folds when she smiles. "
                "Her skin has a soft, thin 'crepe' texture, very well-cared-for but showing clear signs of advanced age. "
                "A small button nose and narrow, twinkling 'hooded' eyes with deep crow's feet that radiate happiness. "
                "Visible small moles and age spots around the neck and cheeks. "
                "The look of a very elderly, cheerful grandmother, frail but full of life. "
                "Hyper-realistic 8k texture, soft cinematic lighting, extremely detailed aged skin."
            ),
            "Nenek Marsi": (
                "A tiny, very frail Javanese grandmother, strictly 80-85 years old, with a shrunken, heart-shaped face. "
                "Classic 'toothless' facial structure where the jaw is slightly recessed, bringing the chin closer to the nose, creating an innocent and endearing look. "
                "Skin is extremely thin, translucent, and deeply creased with hundreds of fine 'paper-crinkle' wrinkles. "
                "Soft matte skin texture with visible age spots and faint white peach fuzz on the sunken cheeks. "
                "Huge, expressive dark eyes that are slightly watery and look incredibly humble and sincere. "
                "A very fragile, precious, and weathered village elder look, looking very tiny in her clothes. "
                "Focus on the 'sweetness' of old age, strictly avoiding any scary or harsh features. "
                "Hyper-realistic 8k resolution, detailed weathered skin, cinematic soft lighting."
            ),
            "Nenek Ponirah": (
                "A dignified and calm Javanese elder, strictly 75-80 years old, with a wide, symmetrical facial structure. "
                "Her skin is like burnished copper, weathered and leathery from years of working under the sun, yet clean and healthy. "
                "Deep horizontal wise aging lines across the forehead and pronounced crow's feet. "
                "A strong, flat nose and a wide, friendly mouth with thin, calm lips. "
                "Her gaze is steady, protective, and incredibly calm—the true matriarch of the family. "
                "Texture shows realistic deep pores, fine wrinkles, and natural sunspots (lentigines). "
                "The look of a sturdy, hard-working village woman who is respected by everyone. "
                "Soft natural lighting, hyper-realistic 8k skin texture, capturing a peaceful and sturdy face without harsh shadows."
            ),
            "Nenek Juminah": (
                "An extremely lean and thin-faced Javanese elderly woman, strictly 80-85 years old. "
                "Sunken cheeks with very prominent, high cheekbones and a sharp, bony jawline that shows her frail structure. "
                "Her skin is like ancient parchment paper, tightly stretched over her bones but deeply creased with thousands of fine, dry 'crackle' wrinkles. "
                "Visible hollows around the temples and deep-set, weary dark eyes with heavy hooded eyelids and thick crow's feet. "
                "Authentic weathered skin with significant sun-damage, scattered age spots (lentigines), and uneven pigmentation from years of outdoor life. "
                "No facial fat or soft volume, strictly bony and gaunt facial structure to emphasize a fragile, hard-working look. "
                "Hyper-realistic 8k resolution, detailed skin pores, cinematic natural lighting, very humble and sincere expression."
            ),
            "Nenek Sikem": (
                "An incredibly frail Javanese elder, strictly 85-90 years old, with a very small, shrunken facial structure. "
                "Her skin is extremely dry, almost translucent, with deep vertical fissures and 'cracked earth' wrinkles on her cheeks and forehead. "
                "Severely drooping hooded eyelids that almost cover her pupils, creating a weary but resilient and stoic look. "
                "Visible salt-and-pepper peach fuzz on her chin and upper lip typical of very advanced age. "
                "The skin texture is raw, uneven, and covered in prominent large sun-spots (lentigines) and thick, leathery patches. "
                "Neck skin is severely loose, hanging in thin, delicate 'turkey-neck' folds. "
                "A masterpiece of hyper-realistic aging, showing the harsh interaction between sharp bone structure and sagging, papery skin. "
                "No filters, raw 8k skin texture, cinematic lighting that emphasizes every deep crease and age spot."
            ),
            "Nenek Dulah": (
                "An elderly Sundanese woman, strictly 75-80 years old, with a soft heart-shaped face that has significantly lost its firmness. "
                "The skin is pale, delicate, and translucent, hanging in soft, heavy 'jowl' folds along the jawline. "
                "Distinct 'sayu' almond-shaped eyes that look weary and emotional, with very thin, sparse white eyebrows and heavy, drooping upper lids. "
                "Her nose is refined but the skin around the nostrils is deeply creased with age. "
                "Texture is focused on 'fine-cracked' wrinkles, resembling old porcelain, with thousands of delicate micro-creases rather than deep canyons. "
                "Authentic faint but numerous age spots (lentigines) across the cheeks. "
                "Her mouth is small, with a soft, slightly trembling upper lip typical of a fragile state. "
                "No harsh edges, focusing on a fragile, soft, and aristocratic aged Sundanese look. "
                "Hyper-realistic 8k resolution, soft natural lighting, extremely detailed papery skin texture."
            ),
            "Nenek Sartini": (
                "An elderly Sundanese grandmother, strictly 75-80 years old, with a wider, rounder facial base and high, flat cheekbones. "
                "Significant sagging in the lower face, creating deep, heavy marionette lines that reach the chin. "
                "Her eyes are constantly moist and slightly reddened, suggesting chronic fatigue, with puffy, dark eye bags and sagging lower lids. "
                "The skin texture is matte, showing visible large pores and broken capillaries (telangiectasia) on the fleshy cheeks. "
                "A very realistic double-chin with loose, 'crepey' skin texture that hangs naturally. "
                "Her expression is one of deep, silent endurance and maternal strength. "
                "Raw and unpolished cinematic detail, focusing on the heavy, sagging volume of an aged rural Sundanese face. "
                "Hyper-realistic 8k resolution, natural lighting that emphasizes skin gravity and weight, authentic sun-damaged skin."
            ),
            "Nenek Tinah": (
                "An incredibly broken Javanese elderly woman appearing in her late 80s. "
                "Her face is a tragic map of deep, chaotic wrinkles and severe volume loss. "
                "The skin hangs loosely in heavy, dark folds around her hollowed jaw and throat (crepey skin). "
                "Her eyes are her most haunting feature: bloodshot, raw from crying, and continuously glistening with unshed tears. "
                "A profound, silent, and distant 'bengong' expression, staring blankly without focus. "
                "Her lower lip has a constant, deeply realistic tremor (quiver) due to emotional pain. "
                "Skin texture is raw, dry, and covered in deep sun-damage and dark age spots. "
                "Visible trembling in her hands as they rest. An aura of complete despair and vulnerability."
                "Raw, unpolished, zero smoothing filters. The look of a soul crushed by grief."
            ),
            "Nenek Wati": (
                "A tiny, terribly frail Sundanese grandmother, strictly 80-85 years old, appearing extremely fragile. "
                "Her small, oval face is consumed by deep, vertical worry lines and incredibly sagging, thin jowls. "
                "Eyes are deeply recessed and hollow, looking intensely 'sayu', with heavily reddened, sore-looking, and drooping eyelids that show significant bags. "
                "The skin texture is pale, translucent like thin porcelain, and covered in fine white, dry 'flaky' textures typical of very aged skin. "
                "Her lips are thin, pale, and pressed tightly together, forming a melancholic, pensive line that emphasizes her quiet suffering. "
                "Neck skin is severely loose and translucent, forming multiple deep, papery folds along her shrunken throat. "
                "Prominent branching blue veins (venous mapping) clearly visible on her thin temples. "
                "An almost ethereal presence of quiet heartbreak, looking deeply tired and physically exhausted. "
                "Hyper-realistic 8k resolution, raw weathered skin, no smoothing, natural soft lighting to show the translucent skin quality."
            ),
            "Kakek Marto": (
                "A lean, elderly Javanese man, strictly 75-80 years old, with an elongated and thin facial structure. "
                "His face is deeply lined with 'wisdom wrinkles' and deep vertical creases that follow his sharp, bony structure. "
                "A long, thin refined nose and a very kind, serene expression in his slightly watery dark brown eyes. "
                "He has a sparse, wispy snow-white goatee and a very thin mustache that adds to his scholarly village elder look. "
                "Skin texture is dry, sun-parched, and leathery but well-cared-for, with realistic fine age spots and visible pores. "
                "Sunken temples and a high forehead that emphasize his intellectual and humble aura. "
                "The overall look is that of a quiet, respected village patriarch. "
                "Hyper-realistic 8k texture, soft natural golden-hour lighting, extremely detailed weathered skin."
            ),
            "Kakek Somo": (
                "A jolly elderly Javanese man, strictly 75-80 years old, with a round, friendly face and aged chubby cheeks that show slight sagging at the jawline. "
                "He has heavy, deep-set laugh lines around his eyes (crow's feet) that cause his eyes to squint into happy slits when he smiles. "
                "His skin is a warm, sun-kissed tan with a soft, weathered 'crepe' texture, showing fine pores and age spots. "
                "A wide, friendly mouth and a small, flat nose with natural creases around the nostrils. "
                "Visible soft grey stubble (short white beard) along his jawline, looking natural and well-groomed. "
                "He radiates a cheerful, approachable grandfatherly energy, looking full of life and kind. "
                "Hyper-realistic 8k resolution, soft natural lighting, capturing the warm and friendly texture of an aged cheerful face."
            ),
            "Kakek Joyo": (
                "A sturdy Javanese elder, strictly 75-80 years old, with a broad forehead and a strong, square jawline. "
                "Despite his firm bone structure, his eyes are incredibly soft, watery, and protective, with heavy drooping lids. "
                "Deep horizontal furrows on his forehead that show decades of hard work, with thick skin texture and prominent brow ridges. "
                "His skin is like dark burnished bronze, leathery and weathered from the sun, showing deep realistic creases. "
                "Large, thick ears and neat, short-cropped salt-and-pepper hair that is thinning at the top. "
                "The look of a hardworking retired farmer who has found inner peace, looking resilient yet humble. "
                "Hyper-realistic 8k resolution, detailed pores, natural sunlight, emphasizing a masculine but naturally aged face."
            ),
            "Kakek Hardi": (
                "A very petite and thin Javanese elder, strictly 80-85 years old, with a small, narrow, and shrunken facial structure. "
                "His skin is extremely thin, like aged translucent parchment, showing the subtle movement of muscles and faint blue veins underneath. "
                "Large, expressive eyes that are slightly watery, deeply recessed, and look intensely sincere and humble. "
                "The mouth is slightly shrunken and recessed (toothless structure), giving him a very sweet, innocent, and fragile elderly expression. "
                "Faint, sparse white eyebrows and a very clean, translucent skin texture with natural age spots and uneven pigmentation. "
                "He looks incredibly fragile and precious, with a hollow temple and bony jawline that emphasizes his advanced age. "
                "The overall aura is that of a gentle soul who deeply appreciates his craft. "
                "Hyper-realistic 8k resolution, raw weathered skin texture, cinematic soft lighting to highlight the translucent skin quality."
            ),
            "Kakek Sableng": (
                "A distinguished elderly Indonesian man, strictly 75-80 years old, with a sharp, noble, and bony facial structure. "
                "High, prominent forehead with deep, etched horizontal wisdom lines and visible temporal veins. "
                "His nose is straight, firm, and aristocratic. The jawline is strong but the skin hangs in thin, aged folds. "
                "The skin is like dark, weathered leather, showing extensive deep sun-damage, fine age spots, and uneven pigmentation. "
                "Eyes are sharp, piercing but kind, with heavy drooping lids and dark, realistic puffy eye bags that show deep fatigue. "
                "Thin, wispy silver-white hair neatly combed back, revealing a high hairline. "
                "Visible fine silver-white stubble on a strong, rugged jawline. No filters, strictly raw aged masculinity. "
                "Hyper-realistic 8k texture, cinematic contrast lighting to emphasize the sharp facial angles and leathery skin."
            ),
            "Kakek Sinto": (
                "An extremely aged Javanese man, strictly 85-90 years old, appearing profoundly frail and skeletal. "
                "His face is deeply sunken, showing total loss of facial volume with a visible bony skull structure underneath. "
                "Skin is paper-thin, translucent, and 'parchment-like', covered in thousands of fine cross-hatched wrinkles and large dark liver spots (lentigines). "
                "Hollowed cheeks and deeply sunken temples that emphasize his extreme age. "
                "His eyes are cloudy with visible milky white cataracts, looking incredibly tired, distant, and emotional. "
                "A very thin, wispy snow-white beard and a fragile moustache that looks like soft silk threads. "
                "Profoundly vulnerable, heartbreaking presence, with loose sagging neck skin in multiple thin folds. "
                "Hyper-realistic 8k texture, raw skin detail, no smoothing, cinematic soft lighting to show the depth of the wrinkles."
            ),
            "Kakek Wiryo": (
                "A sturdy, square-faced elderly Javanese man, strictly 70-75 years old, with a rugged, leathery complexion. "
                "Broad nose and an incredibly strong, thick jawline with visible masseter muscle definition. "
                "His skin is deeply sun-baked, dark bronze, and rough, featuring large visible pores, deep pits, and realistic sweat-beads. "
                "Deep, heavy nasolabial folds and thick, calloused-looking 'turkey-neck' skin with prominent tendons. "
                "Short, messy salt-and-pepper hair, thinning and coarse. "
                "His expression is intensely focused and resilient, showing the grit of a lifetime of heavy physical labor. "
                "Raw, unpolished cinematic details, no skin smoothing, 8k resolution, high-contrast lighting to emphasize muscle and deep skin texture."
            ),
            "Kakek Usman": (
                "An elderly Indonesian grandfather, strictly 75-80 years old, with a small, narrow face contorted in profound grief. "
                "His most striking feature is his raw, reddened, and severely swollen eyes, glistening with heavy moisture and thick, realistic tears rolling down. "
                "The skin around his eyes and hollow cheeks is puffy, tender, and slightly inflamed from prolonged crying. "
                "Deeply furrowed brow with intense vertical worry lines and a visibly trembling, quivering lower lip. "
                "Thin, disheveled snow-white hair and a sparse, unkempt beard that adds to his look of total despair. "
                "The look of a man who has lost everything, heart-wrenching and vulnerable. "
                "100% emotional realism, 8k resolution, raw skin texture with salty tear streaks, haunting and cinematic lighting."
            )
        }

        # --- 2. MASTER WARDROBE (6 VARIAN PER KARAKTER - DAILY & NEAT HIJAB) ---
        MASTER_FAMILY_WARDROBE = {
            # --- KELOMPOK NENEK ---
            "Nenek Aminah": {
                "Daster Arab Polos (No Lace)": "Wearing a very simple, oversized rayon 'Daster Arab' in faded emerald green. No gold embroidery or lace, just basic stitching. The fabric is thin and shows heavy water-splash stains around the chest, paired with a dusty black instant bergo hijab.",
                "Daster Kaos Motif Karat / Abstrak": "Wearing a stretched-out cotton daster with a blurry, faded abstract pattern in earthy brown tones. The armholes are loose (melar), paired with a simple navy blue jersey hijab that is tucked into the neckline for a practical home look.",
                "Setelan Celana Rayon (One-Set Desa)": "Wearing a matching long-sleeved shirt and loose trousers set made of cheap, thin rayon with a small polka-dot pattern. The colors are faded from sun exposure. Complemented by a simple white instant hijab with a soft, worn-out foam pad.",
                "Kaos Souvenir / Partai & Sarung Lilit": "Wearing a faded orange promotional cotton t-shirt (Kaos Souvenir) with cracked printed text on the back. Paired with a dark purple batik sarong wrapped tightly at the waist and a simple grey square hijab pinned with a small safety pin.",
                "Daster Kancing Bobok & Handuk Leher": "Wearing a traditional front-opening 'Daster Kancing Bobok' in faded maroon with a small checkered pattern. A worn-out, thin white towel is draped around her neck, over her simple maroon instant hijab, looking like she's busy with household chores.",
                "Baju Tidur Babydoll Katun Kusam": "Wearing a very modest, loose-fitting 'Babydoll' style cotton set in faded pastel blue. The fabric has a stiff, weathered texture. Paired with a simple black jersey hijab that shows realistic weight and drape over the shoulders."
            },
            "Nenek Siti": {
                "Daster Daster Sogan Klasik": "Wearing a traditional Javanese 'Sogan' pattern rayon daster with intricate brown and black batik motifs. The fabric is thin and limp (jatuh), looking well-worn. Paired with a simple cream-colored instant bergo hijab that has a slightly loose chin area.",
                "Daster Kaos Motif Bunga Kecil": "Wearing a short-sleeved cotton-jersey daster in faded mint green, covered in tiny pink floral patterns (motif bunga kecil). The fabric shows realistic pilling. Paired with matching long hand-sleeves (manset) and a dusty pink jersey hijab tucked into the collar.",
                "Daster Pelangi Luntur (Tie-Dye)": "Wearing a loose 'Tie-Dye' or 'Daster Pelangi' in faded purple and yellow. The colors are muted and washed out. Complemented by a simple white instant hijab that looks soft and thin, showing a very casual and humble village home-stay look.",
                "Daster Karakter Kartun Kusam": "Wearing an oversized cotton daster with a large, faded, and cracked cartoon character print on the chest. The base color is a dull sky blue. Paired with a simple navy blue bergo hijab. A very realistic daily look for a grandmother at home.",
                "Daster Batas Dada Motif Etnik": "Wearing a 'Daster Kerut' or 'Daster Batas Dada' with a simple ethnic geometric pattern in faded maroon and black. The elastic around the chest looks stretched out. Complemented by a simple grey cotton hijab tied loosely under the chin.",
                "Daster Kaos Polos & Handuk Bahu": "Wearing a very plain, oversized mustard yellow cotton-jersey daster with a slightly stretched neckline. A small, frayed green hand towel is draped over her left shoulder, paired with a simple black instant hijab that shows natural fabric weight."
            },
            "Nenek Marsi": {
                "Daster Rayon Motif Batik Lawasan": "Wearing an oversized, thin rayon daster with a faded 'Lawasan' batik pattern in muted brown and cream. The fabric looks very limp and soft from years of washing. Paired with a simple, slightly oversized white instant hijab that frames her small face gently.",
                "Kaos Oblong Lengan Panjang & Jarik": "Wearing a very thin, plain long-sleeved cotton shirt in faded lilac. The fabric is almost translucent due to age. Paired with a dark-toned batik jarik cloth wrapped high around her waist and a simple grey jersey hijab pinned tightly under the chin.",
                "Daster Kancing Serut Motif Polkadot": "Wearing a front-buttoned daster with a small white polkadot pattern on a faded navy background. The elastic around the waist is loose. Complemented by a simple maroon bergo hijab that looks a bit too big for her small head, adding to her fragile look.",
                "Tunik Katun Tipis & Celana Santai": "Wearing a very simple, short-sleeved cotton tunic in a faded dusty rose color with a few visible mended spots (bekas jahitan tangan). Paired with loose black batik trousers and a soft white instant hijab that drapes naturally over her narrow shoulders.",
                "Daster Kaos Motif Daun (Leafy Pattern)": "Wearing a soft cotton-jersey daster with a faded green leafy pattern. The neckline is slightly stretched. A small, frayed white towel is tucked into her simple black instant hijab. The overall look is very humble and grandmotherly.",
                "Baju Kurung Katun Lawas & Kerudung Segi Empat": "Wearing a classic, loose-fitting baju kurung made of old, faded yellow cotton. The fabric is stiff and weathered. Paired with a simple square cotton hijab (hijab segi empat) folded simply and fastened with a small, rusted safety pin under her chin."
            },
            "Nenek Ponirah": {
                "Daster Kaos Motif Mega Mendung (Faded)": "Wearing a sturdy, oversized cotton-jersey daster with a large 'Mega Mendung' cloud pattern in faded navy and grey. The fabric has a heavy, realistic drape. Paired with a dark black jersey bergo hijab with a firm foam pad (pet) that looks well-worn but neat.",
                "Setelan Celana Batik Kulot (Daily Set)": "Wearing a matching set of a short-sleeved top and loose 'kulot' trousers made of thick, non-shiny rayon in a deep chocolate brown with ethnic circle patterns. The colors are muted. Complemented by a dusty grey instant hijab that covers her shoulders perfectly.",
                "Daster Kancing Depan Motif Geometris": "Wearing a practical front-buttoned daster in a dark maroon color with simple white geometric diamond patterns. The fabric is thick and weathered. Paired with a simple white instant hijab pinned tightly under the chin, looking like a strong, capable village matriarch.",
                "Tunik Katun Oxford & Jarik Cokelat": "Wearing a modest long-sleeved tunic made of thick, faded sky-blue Oxford cotton. Paired with a dark, heavy-weight brown batik jarik cloth wrapped securely at the waist and a simple navy blue jersey hijab tucked into the collar.",
                "Daster Rayon Motif Daun Lebar": "Wearing a loose rayon daster with a large, bold green leaf pattern on a black background. The fabric is slightly shiny but wrinkled from daily wear. A small, thin white towel is draped neatly over her shoulder, over her simple black instant hijab.",
                "Kaos Polo Lengan Panjang & Sarung Lawasan": "Wearing a modest, oversized long-sleeved polo shirt in a faded forest green. The fabric is thick cotton. Paired with a weathered 'Lawasan' batik sarong and a simple, breathable white instant hijab that frames her wide, calm face."
            },
            "Nenek Juminah": {
                "Daster Rayon Kusut & Handuk Leher": "Wearing a limp, faded navy blue rayon daster with large blurry floral prints, showing heavy realistic wrinkles. A small, frayed white hand towel is draped around her neck, tucked slightly into her simple grey jersey bergo hijab. The fabric looks very thin on her bony shoulders.",
                "Kaos Haji Putih & Sarung Lawasan": "Wearing a classic Indonesian 'Kaos Haji' (white long-sleeved undershirt with a small pocket) that looks grayish from many washes. Paired with an extremely faded 'Lawasan' batik sarong and a thin, breathable white instant hijab pinned tightly under the chin.",
                "Daster Kaos Melar & Kerudung Segi Empat": "Wearing an oversized, stretched-out (melar) soft cotton t-shirt style daster in faded maroon. Complemented by a simple square cotton hijab (hijab segi empat) that is folded haphazardly and tied loosely behind her neck, showing a very casual home-stay look.",
                "Kebaya Katun Jadul Polos": "Wearing a very thin, semi-translucent white cotton kebaya without embroidery, fastened by a single rusty safety pin. The fabric shows significant aging and yellowing, paired with a dark brown batik sarong that has a rough, starched texture.",
                "Daster Kancing Serut Motif Garis": "Wearing a front-buttoned daily daster with faded vertical stripes in muted green. The fabric is thin and looks soft from years of use. Paired with a simple black instant hijab that frames her thin, sunken cheeks perfectly.",
                "Kaos Lengan Panjang Souvenir & Jarik": "Wearing an oversized long-sleeved cotton souvenir t-shirt in faded yellow with cracked printed text. Paired with a dark chocolate-toned batik jarik and a simple white jersey hijab. The oversized shirt emphasizes her lean and fragile frame."
            },
            "Nenek Sikem": {
                "Daster Kaos Karakter & Bergo": "Wearing an oversized, stretched-out cotton daster in faded sky blue with a large, cracked cartoon character print on the chest. The fabric shows heavy pilling. Paired with a simple black jersey bergo hijab with a soft, worn-out foam pad (pet).",
                "Kaos Souvenir Toko Bangunan & Sarung": "Wearing a faded orange long-sleeved promotional t-shirt (Kaos Souvenir) with a cracked black logo of a local hardware store on the back. Paired with a dark purple batik sarong wrapped tightly at the waist and a simple grey instant hijab.",
                "Daster Kelelawar Motif Bunga Besar": "Wearing a loose 'Kelelawar' style rayon daster with large, blurry orange floral prints on a dark brown background. The fabric is very limp and wrinkled. Complemented by a dusty maroon instant hijab pinned simply under the chin.",
                "Daster Kancing Dada Motif Polkadot": "Wearing a practical front-buttoned short-sleeved daster in faded navy blue with small white polkadot patterns. A small black plastic coin purse is tucked into the side pocket. Paired with a simple white instant hijab that looks soft and thin.",
                "Daster Pelangi Luntur (Tie-Dye)": "Wearing a loose, sleeveless tie-dye daster (Daster Pelangi) in muted purple and yellow that has faded from sun exposure. Layered with long black matching hand-sleeves (manset) and a simple navy blue jersey hijab.",
                "Kaos Olahraga Sekolah & Jarik": "Wearing an old, oversized long-sleeved school sports t-shirt (Kaos Olahraga) in faded red with blurry school text on the back. The fabric is thin and weathered. Paired with a dark chocolate-toned batik jarik and a simple grey bergo hijab."
            },
            "Nenek Dulah": {
                "Daster Kaos Motif Bunga Kecil": "Wearing a short-sleeved cotton-jersey daster in faded mint green, covered in tiny pink floral patterns. The fabric shows realistic pilling and a stretched neckline. Paired with a simple grey instant jersey hijab that shows realistic fabric weight.",
                "Daster Rayon Motif Sogan Jawa": "Wearing a traditional Javanese 'Sogan' style rayon daster with dense brown and black batik patterns. The fabric is thin, limp, and heavily wrinkled. Complemented by a simple black bergo hijab with a soft, worn-out foam pad (pet).",
                "Kaos Lengan Panjang Hadiah Toko Mas": "Wearing a faded red long-sleeved promotional t-shirt with a cracked gold-colored logo of a local jewelry store on the chest. Paired with a dark-toned batik sarong and a simple white instant hijab pinned tightly under the chin.",
                "Daster Kancing Dada Motif Batik Abstrak": "Wearing a front-buttoned daily daster in faded purple with a blurry, white abstract batik print. The fabric is weathered and thin. Paired with a simple navy blue instant hijab that looks soft and well-washed.",
                "Daster Kaos Garis-Garis & Handuk Leher": "Wearing an oversized striped cotton-jersey daster in faded blue and white. A small, well-worn blue hand towel is draped around her neck, tucked into a simple maroon instant hijab, looking like she's ready for her daily market trip.",
                "Kaos Olahraga Desa & Jarik Cokelat": "Wearing a modest long-sleeved village sports t-shirt (Kaos Senam) in faded orange with blurry text on the back. Paired with a dark chocolate-toned batik jarik and a practical grey 'slup' instant hijab for a quiet, grandmotherly home-stay vibe."
            },
            "Nenek Sartini": {
                "Daster Rayon Motif Bunga Matahari": "Wearing a loose rayon daster in faded yellow with large, blurry brown sunflower prints. The fabric is very limp and shows heavy wrinkles around the waist. Paired with a simple, well-worn grey jersey bergo hijab that frames her face naturally.",
                "Daster Kaos Motif Batik Pesisiran": "Wearing a short-sleeved cotton-jersey daster with a bright but faded red 'Pesisiran' batik pattern. The fabric shows realistic pilling and a loose neckline. Complemented by a simple black instant hijab that drapes over her shoulders.",
                "Kaos Lengan Panjang Oleh-Oleh": "Wearing an oversized long-sleeved white cotton t-shirt with a cracked, faded souvenir print of a famous landmark on the chest. The fabric is thin and weathered. Paired with a dark-toned floral sarong and a simple navy blue instant hijab.",
                "Daster Kancing Depan Motif Geometris": "Wearing a practical front-buttoned daster in faded emerald green with simple white geometric patterns. A small black plastic coin purse is visible in her side pocket. Paired with a thin, breathable white instant hijab pinned simply under the chin.",
                "Daster Kaos Polos & Manset Lengan": "Wearing a very plain, oversized faded maroon cotton-jersey daster. Paired with mismatched long black hand-sleeves (manset) and a simple grey square hijab folded into a triangle and tied loosely behind her neck.",
                "Daster Rayon Motif Batik Cap": "Wearing a humble, loose-fitting rayon daster with a dark purple 'Batik Cap' pattern that has almost faded away. The fabric is soft and heavily creased. Paired with a practical dark brown 'slup' instant hijab, looking like she's ready for a quick trip to the neighbor's house."
            },
            "Nenek Tinah": {
                "Daster Kaos Motif Karakter Kartun Kusam": "Wearing an oversized cotton-jersey daster in faded sky blue with a large, cracked cartoon character print on the chest. The fabric is stretched out and shows heavy pilling. Paired with a simple black instant bergo hijab that looks soft and well-worn.",
                "Daster Rayon Motif Batik Daun": "Wearing a loose, limp rayon daster in faded forest green with large white leaf patterns. The fabric is heavily wrinkled and shows realistic water-splash stains around the hem. Complemented by a dusty grey instant hijab pinned simply under the chin.",
                "Kaos Lengan Panjang Toko Pupuk Pertanian": "Wearing a faded yellow long-sleeved promotional t-shirt with a cracked black logo of a local fertilizer shop on the back. Paired with a dark-toned traditional batik sarong and a thin, breathable white instant hijab that frames her face naturally.",
                "Daster Kancing Dada Motif Garis-Garis": "Wearing a practical front-buttoned short-sleeved daster with faded vertical stripes in muted maroon and white. The neckline is slightly loose. Paired with a simple navy blue jersey hijab that drapes over her shoulders for a daily village look.",
                "Daster Kaos Polos & Handuk Leher": "Wearing a very plain, oversized faded orange cotton-jersey daster. A small, frayed white hand towel is draped around her neck, tucked into her simple maroon instant hijab, looking like she's busy with her morning house errands.",
                "Daster Rayon Motif Abstrak Pelangi": "Wearing a humble, loose-fitting rayon daster with a faded 'Tie-Dye' or rainbow abstract pattern in muted purple and pink. The colors are washed out from sun exposure. Paired with a practical dark brown 'slup' instant hijab for a quiet, grandmotherly home-stay vibe."
            },
            "Nenek Wati": {
                "Daster Kaos Motif Batik Parang Kusam": "Wearing an oversized cotton-jersey daster with a classic 'Parang' batik pattern in faded brown and white. The fabric shows heavy pilling and a stretched-out collar. Paired with a simple black instant bergo hijab that has a soft, worn-out foam pad.",
                "Kaos Lengan Panjang Jalan Sehat": "Wearing a faded red long-sleeved t-shirt from a village fun-walk event ('Jalan Sehat') with blurry white text on the chest. The fabric is thin and weathered. Paired with a dark-toned batik sarong and a simple white instant hijab pinned tightly.",
                "Daster Rayon Motif Kembang Besar": "Wearing a loose, limp rayon daster with large, faded purple flower prints (motif kembang) on a dark navy background. The fabric is heavily wrinkled at the hem. Complemented by a dusty grey instant hijab that drapes naturally over her shoulders.",
                "Daster Kancing Depan Motif Kotak-Kotak": "Wearing a practical front-buttoned short-sleeved daster with a small checkered pattern in faded green and white. A small black plastic coin purse is clutched in her hand. Paired with a simple navy blue jersey hijab for a daily market-goer look.",
                "Daster Kaos Polos & Handuk Bahu": "Wearing a very plain, oversized faded mustard yellow cotton-jersey daster. A small, frayed green hand towel is draped over her left shoulder, tucked into her simple maroon instant hijab, looking like she just finished chores.",
                "Daster Rayon Motif Batik Cap Luntur": "Wearing a humble, loose-fitting rayon daster with a dark maroon 'Batik Cap' pattern that has almost faded away from frequent washing. The fabric is soft and thin. Paired with a practical dark brown 'slup' instant hijab for a peaceful village home-stay vibe."
            },

            # --- KELOMPOK KAKEK ---
            "Kakek Marto": {
                "Kaos Berkerah (Polo) Kusam & Sarung": "Wearing a faded green short-sleeved polo shirt with a slightly curled and stretched collar. The fabric shows light pilling. Paired with a classic multicolored checkered sarong tied high at the waist and a well-worn black velvet peci that looks slightly dusty.",
                "Kaos Partai Lengan Panjang & Celana Bahan": "Wearing a faded yellow long-sleeved promotional t-shirt (Kaos Partai) with blurry political text on the chest. The fabric is thin and wrinkled. Paired with loose black cotton trousers and a white knitted skullcap (peci rajut) that frames his long, thin face.",
                "Kemeja Flanel Kotak & Sarung Batik": "Wearing an unbuttoned, oversized flannel shirt in muted blue and grey over a thin white cotton undershirt. Paired with a dark chocolate-toned batik sarong and a faded black peci. The sleeves are rolled up to the elbows, showing a rustic daily village look.",
                "Kaos Oblong Putih & Sarung Wadimor": "Wearing a classic thin white cotton undershirt (kaos oblong) with a small chest pocket. The fabric looks yellowish from age. Paired with a maroon checkered sarong and a simple batik cloth slung over his shoulder, looking like he's ready for a chat at the warung.",
                "Baju Kurung Katun & Peci Haji": "Wearing a very simple, short-sleeved brown cotton shirt with two large pockets at the bottom. The fabric is stiff and weathered. Paired with a blue checkered sarong and a white hajj cap (peci haji) that looks soft and well-washed.",
                "Kemeja Batik Pasar & Celana Komprang": "Wearing an oversized, faded batik shirt with a simple repetitive pattern in earthy tones. The fabric is thin and limp. Paired with loose black ankle-length trousers (sirwal) and a simple black peci, looking like a humble and wise village elder."
            },
            "Kakek Somo": {
                "Kaos Berkerah Hadiah Toko Bangunan": "Wearing a short-sleeved faded orange polo shirt with a cracked black logo of a local hardware store on the chest. The fabric is stretched out around the waist. Paired with a dark green checkered sarong and a black velvet peci that is tilted slightly back on his round head.",
                "Kaos Oblong Putih & Handuk Bahu": "Wearing a classic, thin white cotton undershirt (kaos oblong) that looks yellowish and soft from frequent use. A small, frayed green hand towel is draped over his shoulder. Paired with a brown batik sarong and no headwear, showing his sparse grey hair.",
                "Kemeja Pendek Motif Kotak & Sarung": "Wearing a short-sleeved, oversized button-down shirt with a large checkered pattern in faded blue and white. Only the middle buttons are fastened. Paired with a maroon sarong and a white hajj cap (peci haji) that looks soft and well-worn.",
                "Kaos Souvenir Jalan Sehat & Celana Kolor": "Wearing a faded red t-shirt from a village fun-walk event with blurry white text. Paired with loose, dark grey cotton drawstring trousers (celana kolor) and a simple batik cloth slung over his shoulder like a sash.",
                "Kaos Polo Garis-Garis & Peci Rajut": "Wearing a horizontal striped polo shirt in faded navy and grey. The collar is curled and weathered. Paired with a classic checkered sarong in muted tones and a white knitted skullcap (peci rajut) that sits snugly on his head.",
                "Baju Koko Santai & Sarung Batik": "Wearing a very simple, short-sleeved light blue 'Baju Koko' with simple embroidery that has started to fray. The fabric is thin and wrinkled. Paired with a dark chocolate-toned batik sarong and a faded black peci, looking like a cheerful grandfather ready for a chat."
            },
            "Kakek Joyo": {
                "Kemeja Pendek Polos & Sarung Wadimor": "Wearing a simple, short-sleeved cotton shirt in faded forest green with two large chest pockets. The fabric is stiff and weathered. Paired with a classic multicolored checkered sarong tied neatly and a black velvet peci that looks well-maintained but old.",
                "Kaos Polo Tebal & Celana Bahan": "Wearing a sturdy, short-sleeved polo shirt in deep navy blue with a slightly faded collar. The fabric has a heavy, realistic drape over his sturdy frame. Paired with loose black cotton trousers and a white knitted skullcap (peci rajut).",
                "Baju Takwa Sederhana & Sarung Batik": "Wearing a very basic, short-sleeved white 'Baju Takwa' with simple stitching. The fabric is slightly yellowish and heavily wrinkled. Paired with a dark chocolate-toned batik sarong and a faded black peci, looking like a dignified village patriarch.",
                "Kaos Lengan Panjang 'Kelompok Tani'": "Wearing a faded maroon long-sleeved promotional t-shirt from a local 'Kelompok Tani' (farmers group). The fabric is thick and weathered. Paired with a dark green checkered sarong and a simple batik cloth slung over his shoulder.",
                "Kemeja Batik Katun Kasar & Sarung": "Wearing an oversized, short-sleeved batik shirt with a large, repetitive pattern in earthy brown tones. The fabric is a bit rough and non-shiny. Paired with a plain navy blue sarong and a white hajj cap (peci haji) that looks soft from frequent washing.",
                "Kaos Oblong Putih & Jaket Kemeja": "Wearing a classic thin white cotton undershirt (kaos oblong), layered with an unbuttoned, faded grey work shirt used as a light jacket. Paired with a dark-toned batik sarong and a black peci, looking like a hardworking elder taking a rest."
            },
            "Kakek Hardi": {
                "Kaos Oblong Putih Tipis & Sarung": "Wearing a very thin, oversized white cotton undershirt (kaos oblong) that looks almost translucent and yellowish from age. The fabric drapes loosely over his narrow shoulders. Paired with a faded blue checkered sarong tied high and a white knitted skullcap (peci rajut).",
                "Kemeja Pendek Lungsuran & Peci Haji": "Wearing a short-sleeved, oversized button-down shirt in faded sky blue that looks too big for his small frame. The fabric is limp and wrinkled. Paired with a dark brown batik sarong and a soft white hajj cap (peci haji) that sits low on his forehead.",
                "Kaos Lengan Panjang Hadiah Toko Pupuk": "Wearing a faded green long-sleeved promotional t-shirt with a cracked yellow logo of a local fertilizer shop. The sleeves are a bit too long for him. Paired with a maroon checkered sarong and a simple batik cloth draped around his neck like a scarf.",
                "Baju Koko Anak Muda Lungsuran": "Wearing a modest, long-sleeved white 'Baju Koko' that clearly looks like a hand-me-down, showing a slightly large fit on his frail body. The fabric is thin and well-washed. Paired with a dark-toned batik sarong and a faded black velvet peci.",
                "Kaos Polo Garis-Garis & Celana Komprang": "Wearing an oversized horizontal striped polo shirt in faded grey and white. The fabric shows heavy pilling. Paired with loose black ankle-length trousers (sirwal) and a simple white peci rajut, looking like a very humble and fragile village elder.",
                "Kemeja Batik Lawasan & Sarung Batik": "Wearing an old, thin batik shirt with a small repetitive pattern in muted earthy tones. The fabric is soft and weathered. Paired with a matching dark chocolate-toned batik sarong and a simple white hajj cap, looking innocent and sincere as he holds his craft."
            },
            "Kakek Sableng": {
                "Kaos Oblong Putih & Jaket Tipis (Peci Hitam)": "Wearing a thin white cotton undershirt (kaos oblong) layered with an unbuttoned, faded navy windbreaker jacket that looks oversized. Paired with a dark-toned batik sarong tied haphazardly at the waist. On his head is a well-worn black velvet peci tilted sharply to the side, looking slightly mischievous.",
                "Kaos Partai Luntur & Sarung (Peci Haji)": "Wearing a faded orange long-sleeved promotional t-shirt (Kaos Partai) with a blurry, cracked logo on the chest. The fabric is stretched out. Paired with a multicolored checkered sarong and a soft white hajj cap (peci haji) that sits slightly loose on his head, showing his playful village elder vibe.",
                "Kemeja Flanel Berantakan & Peci Hitam": "Wearing an unbuttoned, oversized checkered flannel shirt in faded red over a bare chest or thin undershirt. The sleeves are rolled up unevenly. Paired with a dark green sarong and an old black peci that has turned slightly greyish from dust and age.",
                "Kaos Souvenir Jalan Sehat (Peci Haji)": "Wearing a faded red t-shirt from a local village event with blurry text. A small, frayed green hand towel is draped over his head, covered by a white hajj cap (peci haji). Paired with loose black cotton trousers and a batik cloth slung over his shoulder like a cape.",
                "Daster Lungsuran & Peci Hitam (Nyeleneh)": "Wearing an oversized, faded floral daster that clearly looks like a hand-me-down from his wife, showing a funny but humble daily look. Paired with loose grey trousers underneath and a classic black velvet peci, radiating a 'Sableng' yet friendly aura.",
                "Kaos Polo Garis-Garis & Sarung (Peci Haji)": "Wearing a horizontal striped polo shirt in faded navy and white with a curled collar. One side of the shirt is tucked into his sarong while the other is out. Paired with a maroon checkered sarong and a simple white hajj cap, looking like a cheerful, eccentric grandfather."
            },
            "Kakek Sinto": {
                "Kemeja Batik Pasar & Peci Hitam": "Wearing an oversized, faded batik shirt with a repetitive simple pattern in muted brown. The shirt is unbuttoned at the top, showing a thin white undershirt. Paired with a dark-toned sarong and a black velvet peci that looks slightly greyish from dust.",
                "Kaos Lengan Panjang 'Koperasi' & Peci Haji": "Wearing a faded navy blue long-sleeved t-shirt with a cracked white logo of a local 'Koperasi' on the chest. Paired with a multicolored checkered sarong tied high and a white hajj cap (peci haji) that looks soft and thin.",
                "Kaos Oblong & Jaket Bahan (Peci Hitam)": "Wearing a classic thin white cotton undershirt (kaos oblong) layered with an old, faded grey zip-up jacket. Paired with a dark chocolate-toned batik sarong and a well-worn black peci tilted forward on his forehead.",
                "Baju Koko Harian & Peci Haji": "Wearing a very simple, short-sleeved light grey 'Baju Koko' made of thin cotton. The fabric is heavily wrinkled and shows minor stains from daily activities. Paired with a maroon sarong and a simple white hajj cap (peci haji) that sits snugly.",
                "Kaos Kerah Garis-Garis & Peci Hitam": "Wearing a faded green and white horizontal striped polo shirt with a curled collar. Paired with a dark green sarong and a classic black velvet peci. A small batik cloth is slung diagonally across his chest like a sash.",
                "Kaos Partai & Jaket Parasut (Peci Haji)": "Wearing a faded yellow promotional t-shirt (Kaos Partai) layered with a thin, old navy parachute jacket. The jacket shows realistic creases and salt-stains. Paired with a simple brown sarong and a white hajj cap (peci haji) sitting slightly crooked."
            },
            "Kakek Wiryo": {
                "Kaos Lengan Panjang Toko Benih (Peci Hitam)": "Wearing a faded green long-sleeved promotional t-shirt with a cracked yellow logo of a local seed shop (Toko Benih) on the back. The fabric is thin and pilling. Paired with a dark chocolate-toned batik sarong and a dusty black velvet peci.",
                "Kemeja Safari Jadul & Sarung (Peci Haji)": "Wearing an old-fashioned, short-sleeved safari shirt in faded khaki with four front pockets. The fabric is stiff and weathered. Paired with a multicolored checkered sarong and a soft white hajj cap (peci haji) that looks well-washed.",
                "Kaos Oblong Putih & Handuk Bahu (Peci Hitam)": "Wearing a classic thin white cotton undershirt (kaos oblong) that is slightly yellowish around the collar. A small blue hand towel is draped over his shoulder. Paired with a dark green sarong and a classic black peci tilted slightly forward.",
                "Kemeja Flanel Kusam & Sarung (Peci Haji)": "Wearing an oversized, unbuttoned flannel shirt in faded brown and grey over a bare chest. The sleeves are rolled up to the elbows. Paired with a maroon checkered sarong and a simple white hajj cap (peci haji) pinned with a small safety pin.",
                "Kaos Polo Garis-Garis & Peci Hitam": "Wearing a horizontal striped polo shirt in faded navy and mustard yellow. The collar is curled and stretched. Paired with a dark-toned batik sarong and a well-worn black velvet peci that shows realistic fabric age.",
                "Kaos Partai & Celana Komprang (Peci Haji)": "Wearing a faded orange promotional t-shirt (Kaos Partai) with a blurry logo. Paired with loose black ankle-length trousers (sirwal) and a simple white hajj cap, looking like a humble grandfather resting after his morning activities."
            },
            "Kakek Usman": {
                "Baju Koko Katun Putih & Sarung (Peci Hitam)": "Wearing a very simple, short-sleeved white cotton 'Baju Koko' with minimal embroidery. The fabric looks soft, yellowish from age, and heavily wrinkled. Paired with a dark chocolate-toned batik sarong and a well-worn black velvet peci that looks slightly dusty.",
                "Baju Koko Kurta Kusam & Peci Haji": "Wearing a modest, long-sleeved 'Kurta' style baju koko in faded sage green. The fabric is thin and shows realistic pilling. Paired with a multicolored checkered sarong and a soft white hajj cap (peci haji) that sits comfortably on his forehead.",
                "Kaos Oblong & Baju Koko Terbuka (Peci Hitam)": "Wearing a classic thin white cotton undershirt (kaos oblong), layered with an unbuttoned white baju koko used like a light jacket. Paired with a maroon sarong and a classic black peci tilted slightly back, looking like a relaxed village elder.",
                "Baju Koko Biru Muda & Sarung (Peci Haji)": "Wearing a simple, short-sleeved baju koko in faded sky blue with a small chest pocket. The fabric is stiff and weathered. Paired with a dark green checkered sarong and a simple white hajj cap (peci haji) that looks thin and breathable.",
                "Kaos Lengan Panjang Toko Bangunan (Peci Hitam)": "Wearing a faded orange promotional t-shirt from a local hardware store with cracked black logos. Paired with a dark-toned batik sarong and a dusty black velvet peci, showing his humble daily look for going to the warung.",
                "Baju Koko Cokelat Tua & Peci Haji": "Wearing a very basic, short-sleeved baju koko in a deep chocolate brown color. The fabric is limp and heavily creased. Paired with a classic multicolored sarong and a white hajj cap (peci haji), radiating a calm and spiritual village grandfather vibe."
            }
        }

        # --- 3. MASTER BAHAN (ARCHITECTURAL PRECISION: FRUIT LUXURY EDITION) ---
        MASTER_KONTEN_ALL = {
            "🍉 Miniatur Dari Buah": {
                "Semangka: Pahatan Murni": (
                    "An intricately carved miniature mosque sculpted entirely from a whole watermelon, resting on a high wooden table. "
                    "The structure features a large central dome from smooth green rind with natural striped patterns, surrounded by smaller domes and multiple symmetrical minarets. "
                    "Each minaret is cylindrical, topped with small domes and fine spires, all precisely carved from the rind with sharp edges. "
                    "The walls are thick green rind, deeply carved with recessed arched doorways and windows, revealing dense, vibrant ruby-red watermelon flesh inside. "
                    "The inner carved sections show a realistic juicy watermelon flesh with a natural fibrous structure and visible grain. "
                    "The red flesh surface is glistening and moist with high-fidelity detail. "
                    "Pure ornamental structure with strictly no text or calligraphy. Clean, sharp carving edges in sharp focus. "
                    "The wooden table is scattered with realistic watermelon debris: glistening red flesh chunks, loose seeds, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Semangka: Kubah Merah": (
                    "An intricately carved miniature mosque sculpted from a whole watermelon, resting on a high wooden table. "
                    "The central dome is carved from exposed vibrant ruby-red watermelon flesh, shaped into a smooth rounded structure with dense fibrous texture, visible grain, and glistening natural moisture. "
                    "Surrounding the main dome are smaller domes and multiple symmetrical minarets crafted from thick green rind, each topped with finely carved spires. "
                    "The structural walls are made from green rind, deeply carved with precise arches and recessed doorways, revealing the transition between rind and flesh. "
                    "All exposed flesh areas show realistic fruit behavior: fiber density, seed pockets, and subtle juice residue. "
                    "Clean, sharp carving edges with extreme clarity. Pure architectural structure with no text or calligraphy. "
                    "Table surface is scattered with realistic watermelon debris: red flesh chunks, loose seeds, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Semangka: Arsitektur Berlapis": (
                    "An intricately carved miniature mosque sculpted from a whole watermelon, resting on a high wooden table. "
                    "The structure emphasizes layered construction: dark green outer rind, pale white inner rind, and dense ruby-red flesh. "
                    "The central dome and minarets are carved to expose these alternating layers, creating a natural multi-tone architectural depth with high color contrast. "
                    "All sections reveal realistic fruit structure with visible fibers and moisture. The red flesh is vibrant, solid, and glistening. "
                    "Deep-carved arched windows and doors with sharp-edged precision. Pure architectural shapes with strictly no text or calligraphy. "
                    "Sharp focus on all layers with high-fidelity detail. "
                    "Table surface is scattered with mixed debris: red flesh chunks, white rind strips, green rind shavings, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Semangka: Ukiran Tipis": (
                    "An ultra-precise miniature mosque carved from a whole watermelon, resting on a high wooden table. "
                    "The structure is defined by extremely thin carving work, with green rind shaved down to delicate architectural thickness. "
                    "Domes and minarets are slender and refined, featuring very fine, sharp edges and highly controlled carving depth. "
                    "Sections reveal thin layers of white rind above vibrant red flesh. The red flesh is dense, solid, and glistening with natural moisture. "
                    "Clean, sharp carving edges with high-fidelity architectural detail in sharp focus. Strictly no motion blur or soft textures on the mosque. "
                    "Pure ornamental structure with strictly no text or calligraphy. "
                    "Table surface is covered with fine carving residue: thin curled rind shavings, micro shavings, and scattered seeds. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Semangka: Ukiran Tradisional": (
                    "A roughly carved miniature mosque sculpted from a whole watermelon, resting on a high wooden table. "
                    "The structure features visibly uneven carving and imperfect geometry, reflecting authentic traditional hand-cut techniques. "
                    "Green rind walls are thick and irregular, with arches and openings carved in a raw, organic manner with visible tool traces. "
                    "Exposed red flesh appears rough and fibrous with visible tearing and natural juice pooling. The flesh is dense, opaque, and glistening. "
                    "Sharp focus on the raw carving marks and organic imperfections. Strictly no text or calligraphy. "
                    "The wooden table is heavily messy, covered with large chunks of red flesh, broken rind pieces, and deep juice stains. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Semangka: Modular Block": (
                    "A completed miniature mosque constructed from multiple carved watermelon pieces assembled into a cohesive structure, resting on a high wooden table. "
                    "The architecture appears modular, with distinct blocks of green rind and red flesh forming walls, domes, and minarets. "
                    "The central dome is assembled from curved segments of rind fitted together, while smaller domes and minarets are built from stacked cylindrical pieces. "
                    "Joints between pieces are visible, showing natural seams and slight misalignment, reinforcing a hand-assembled construction style. "
                    "Exposed red flesh is dense, fibrous, and glistening with natural moisture. "
                    "Sharp focus on the raw assembly marks and organic imperfections. Strictly no text or calligraphy. "
                    "The wooden table is heavily messy, covered with cut fragments, loose segments, seeds, and juice marks from the assembly process. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Semangka: Kompleks Masjid": (
                    "A large-scale miniature mosque complex carved from a whole watermelon, resting on a high wooden table. "
                    "The structure includes a central grand mosque surrounded by smaller satellite buildings, courtyards, and multiple clustered minarets, creating a dense architectural layout. "
                    "All elements are carved from green rind with exposed red flesh used for depth accents and inner sections. "
                    "The red flesh is dense, fibrous, and vibrant with natural glistening moisture. "
                    "Clean, sharp carving edges across the entire complex. Every tiny satellite building and minaret must be in sharp focus with high-fidelity detail. "
                    "Pure architectural structure with strictly no text or calligraphy. "
                    "The wooden table is widely covered with extensive carving debris: flesh chunks, rind fragments, seeds, and juice stains, reflecting a massive project. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Semangka: Ukiran Utuh": (
                    "A whole intact round watermelon with its natural spherical shape preserved, resting on a high wooden table. "
                    "A miniature mosque is intricately carved directly into the surface as a recessed architectural relief, embedded into the rind. "
                    "The mosque features a central dome and minarets carved inward, following the natural curve of the fruit, maintaining the original round volume. "
                    "Carved sections reveal vibrant, glistening ruby-red flesh forming depth within windows and arches. The flesh is dense and fibrous. "
                    "Sharp focus on the carving edges and the smooth green striped texture of the whole watermelon. Strictly no text or calligraphy. "
                    "The wooden table surface is scattered with realistic carving debris: rind shavings, red flesh fragments, and juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Semangka: Tipe Mewah": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole watermelon, resting on a high wooden table. "
                    "The structure features a towering central main dome with natural striped patterns and multiple complex symmetrical minarets with slender, fine-spires, all sculpted from the thick green rind. "
                    "The walls are thick dark green rind, meticulously detailed with multi-layered geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved outward, revealing the inner vibrant, dense, glistening ruby-red watermelon flesh which is packed with tiny seeds. Strictly with no etched text or calligraphy. "
                    "The watermelon surface is realistic with a rough rind texture and naturally glistening red flesh showing organic fibers. The carving edges are clean, sharp, and highly defined for maximum clarity. "
                    "Table clutter: Small, realistic glistening red flesh chunks, tiny seed clusters, and curled rind shavings scattered naturally on the table. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Semangka: LED Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole watermelon, resting on a high wooden table. "
                    "The structure features a towering central main dome with natural striped patterns and multiple complex symmetrical minarets with slender, fine-spires, all sculpted from the thick green rind. "
                    "The walls are thick dark green rind, meticulously detailed with multi-layered geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved outward, revealing the inner vibrant, dense, glistening ruby-red watermelon flesh which is packed with tiny seeds. "
                    "The watermelon surface is realistic with a rough rind texture and naturally glistening red flesh showing organic fibers. The carving edges are clean, sharp, and highly defined for maximum clarity. "
                    "Pure ornamental structure with strictly no text or calligraphy. "
                    "Table clutter: Small, realistic glistening red flesh chunks, tiny seed clusters, and curled rind shavings scattered naturally on the table. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Buah Naga: Pahatan Murni": (
                    "An intricately carved miniature mosque sculpted entirely from a fresh dragon fruit, resting on a high wooden table. "
                    "Architecture features precise geometric carving to create building facades. The walls and multiple symmetrical minarets are made of the bright pinkish-purple dragon fruit skin, with its natural distinct green-tipped scales forming decorative textures. "
                    "Walls are bright pink, precisely carved out with deep, recessed arched doorways and windows. The exposed surfaces within the doors and windows are the contrasting glistening white dragon fruit flesh filled with tiny natural black seeds. "
                    "The central main dome is a large structure made of smooth pinkish rind with symmetrical scales, topped with small domes and tiny spires. "
                    "Pure architectural structure with strictly no text or calligraphy. Clean, sharp carving edges in sharp focus. "
                    "Table clutter: Realistic glistening white flesh fragments with black seeds and pink rind shavings scattered naturally on the table surface. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Buah Naga: Kubah Putih": (
                    "An intricately carved miniature mosque sculpted from a whole dragon fruit, resting on a high wooden table. "
                    "The central dome is formed from exposed white dragon fruit flesh, carefully shaped into a smooth rounded structure with dense, moist texture and visible tiny black seeds embedded throughout. "
                    "The white flesh dome appears physically solid and opaque, with a glistening wet surface that catches natural daylight. "
                    "Surrounding the main dome are smaller domes and multiple symmetrical minarets crafted from thick bright pink dragon fruit rind with distinct green-tipped scales. "
                    "The structural walls are made from pink rind, deeply carved with precise arches and recessed doorways, revealing the layered transitions between pink rind and white seeded flesh. "
                    "Clean, sharp carving edges with high-fidelity detail. Pure ornamental structure with strictly no text or calligraphy. "
                    "Table surface is scattered with realistic white flesh fragments, black seeds, and pink rind shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Buah Naga: Kubah Merah": (
                    "An intricately carved miniature mosque sculpted from a red-fleshed dragon fruit, resting on a high wooden table. "
                    "The central dome is a massive carved block of deep, vibrant purple-red dragon fruit flesh, glistening and moist, filled with tiny natural black seeds. "
                    "The purple flesh appears solid and catches natural external daylight with high color saturation. "
                    "Structural walls and minarets are made of bright pink rind with green scales, creating a monochrome yet high-contrast purple-pink aesthetic. "
                    "All exposed flesh areas show natural moist texture and visible seed patterns. "
                    "Clean, sharp carving edges with extreme clarity. Strictly no text or calligraphy. "
                    "Table clutter: Glistening purple flesh scraps, juice marks, and pink rind debris. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Buah Naga: Arsitektur Berlapis": (
                    "An intricately carved miniature mosque sculpted entirely from a whole dragon fruit, placed on a high wooden table. "
                    "The structure emphasizes layered construction using all parts of the dragon fruit: bright pinkish-purple skin with distinct green-tipped scales, thin white inner rind, and contrasting white dragon fruit flesh filled with tiny natural black seeds. "
                    "The central dome is a masterpiece of material gradation, with a base of pink skin and an upper structure deeply carved to reveal alternating layers of the white rind and the glistening seeded white flesh, creating a striking natural multi-tone architectural effect. "
                    "The structural walls are made from pink rind, deeply carved with precise geometric patterns and recessed arched doorways. Carved sections are carefully composed to expose the transition between pink outer skin and white seeded flesh inside, providing depth and contrast without text or calligraphy. "
                    "Glistening natural moisture and organic fibers of the flesh with black seeds are visible, reflecting natural golden hour daylight. Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table surface is widely covered with extensive carving debris: flesh chunks, pink rind fragments, seeds, and juice stains. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Buah Naga: Kompleks Masjid": (
                    "A large-scale miniature mosque complex intricately carved from a single large dragon fruit, placed on a high wooden table. "
                    "The structure includes a central grand mosque surrounded by smaller satellite buildings, courtyards, and multiple clustered minarets, creating a dense architectural layout. "
                    "All elements are carved from the pink rind with its distinct green-tipped scales forming decorative textures. "
                    "The complex walls are bright pink, deeply carved out with recessed arched doorways and windows, revealing contrasting glistening white dragon fruit flesh filled with tiny natural black seeds, strictly with no text or calligraphy. "
                    "Central main dome is smooth pink skin with symmetrical scales, topped with small domes and tiny spires. "
                    "Table clutter: Extensive scattering of glistening white flesh fragments with black seeds, seeds, and pink rind shavings, indicating massive work. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Buah Naga: Tipe Mewah": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole dragon fruit, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the bright pink rind with distinct green-tipped scales. "
                    "The walls are meticulously detailed with multi-layered geometric patterns and deep-recessed ornate arches, showcasing high-level craftsmanship. "
                    "The inner carved sections reveal vibrant white dragon fruit flesh filled with tiny natural black seeds, glistening like moist marble under natural golden hour daylight. "
                    "Each doorway and window is precisely carved to show the sharp transition between pink rind and seeded flesh. Strictly no text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "Table surface is scattered with realistic dragon fruit debris: white flesh chunks, black seeds, and pink rind shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Buah Naga: LED Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole dragon fruit, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the bright pink rind with distinct green-tipped scales. "
                    "The walls are meticulously detailed with multi-layered geometric patterns and deep-recessed ornate arches. "
                    "The inner carved sections reveal dense white flesh with black seeds, glistening like moist marble under natural golden hour daylight. "
                    "Surface response follows real fruit physics: natural daylight reflects naturally on the moist flesh and black seeds. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. Pure architectural structure with no text or calligraphy. "
                    "Table surface is scattered with realistic dragon fruit debris: white flesh chunks, black seeds, and pink rind shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Melon: Pahatan Murni": (
                    "An intricately carved miniature mosque sculpted entirely from a whole honeydew melon, resting on a high wooden table. "
                    "The structure features a large central dome made from the natural netted tan-colored rind of the melon. "
                    "The walls and multiple symmetrical minarets are precisely carved from the thick melon rind, showcasing the distinct rough texture of the outer skin. "
                    "Walls are deeply carved with recessed arched doorways and windows, revealing the succulent, vibrant pale-green melon flesh inside. "
                    "The inner carved sections show realistic juicy melon texture with a smooth, glistening surface that catches natural daylight. "
                    "Pure ornamental structure with strictly no text or calligraphy. Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is scattered with realistic melon debris: glistening pale-green flesh fragments, small slippery seeds, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Melon: Kubah Hijau Muda": (
                    "An intricately carved miniature mosque sculpted from a whole honeydew melon, resting on a high wooden table. "
                    "The central dome is carved from exposed vibrant pale-green melon flesh, shaped into a smooth rounded structure with dense fibrous texture, visible grain, and glistening natural moisture. "
                    "The green flesh appears solid and opaque, catching natural daylight with vivid saturation. "
                    "Surrounding the main dome are smaller domes and multiple symmetrical minarets crafted from thick netted tan-colored rind, each topped with finely carved spires. "
                    "The structural walls are made from the textured melon rind, deeply carved with precise arches and recessed doorways, revealing the transition between rind and pale-green flesh. "
                    "All exposed flesh areas show realistic fruit behavior: fiber density, seed pockets, and subtle juice residue. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. Pure architectural structure with no text or calligraphy. "
                    "Table surface is scattered with realistic melon debris: pale-green flesh chunks, slippery seeds, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Melon: Kubah Orange": (
                    "An intricately carved miniature mosque sculpted from a whole cantaloupe melon, resting on a high wooden table. "
                    "The central dome is carved from exposed vibrant orange melon flesh, shaped into a smooth rounded structure with dense fibrous texture, visible grain, and glistening natural moisture. "
                    "The orange flesh appears solid and opaque, catching natural daylight with vivid saturation. "
                    "Surrounding the main dome are smaller domes and multiple symmetrical minarets crafted from thick netted tan-colored rind, each topped with finely carved spires. "
                    "The structural walls are made from the textured melon rind, deeply carved with precise arches and recessed doorways, revealing the transition between rind and vibrant orange flesh. "
                    "All exposed flesh areas show realistic fruit behavior: fiber density, seed pockets, and subtle juice residue. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. Pure architectural structure with no text or calligraphy. "
                    "Table surface is scattered with realistic melon debris: orange flesh chunks, slippery seeds, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Melon: Ukiran Elite": (
                    "An intricately full-carved miniature mosque sculpted from a whole cantaloupe melon, resting on a high wooden table. "
                    "The entire surface of the melon is covered in deep, precise architectural carvings, leaving no part of the rind untouched, creating a highly detailed lace-like effect on the tan netted skin. "
                    "The structure features a massive central dome and tiered minarets, all intricately engraved with complex geometric Islamic patterns and sharp-edged textures. "
                    "The walls are thick textured rind, deeply recessed to reveal the vibrant, rich-orange melon flesh inside, which appears dense, moist, and glistening with natural daylight. "
                    "Each doorway and arched window is a masterpiece of precision, showing the transition between the rough tan rind and the smooth orange interior. "
                    "Pure architectural structure with strictly no text or calligraphy. Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is covered with fine carving debris: orange flesh fragments, thin rind shavings, and small slippery seeds. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Melon: Dual-Tone": (
                    "An incredible miniature mosque constructed from two different types of melons: a honeydew and a cantaloupe, combined into one structure on a high wooden table. "
                    "The central grand dome is carved from the tan-netted rind revealing vibrant orange flesh, while the surrounding minarets and satellite domes are carved from green-fleshed melon. "
                    "The structure emphasizes the sharp color contrast between the emerald-green and the rich-orange fruit flesh, creating a natural jewel-like architectural masterpiece. "
                    "All sections are dense, opaque, and glistening with natural moisture, reflecting external daylight. No text or calligraphy. "
                    "Table clutter: a mix of orange and green flesh fragments, seeds, and rind shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Melon: Kubah Kristal": (
                    "A unique miniature mosque where the entire upper structure and domes are carved from de-skinned melon flesh, resting on a high wooden table. "
                    "The domes are massive spheres of glistening pale-green melon flesh, meticulously shaped to look like smooth, solid emerald stone, catching natural daylight with high saturation. "
                    "The base of the mosque and the lower walls maintain the tan-netted rind for structural contrast. "
                    "The exposed flesh is moist and fibrous. Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "Table surface is wet with melon juice, seeds, and large chunks of flesh. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Melon: Tipe Mewah": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole Cantaloupe melon, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets with slender, fine-spires, all sculpted from the tan netted rind. "
                    "The walls are thick textured rind, meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive feel. "
                    "Each door and window is precisely carved outward, revealing the inner vibrant, rich-orange Cantaloupe flesh which is dense, moist, and glistening with natural daylight. Strictly with no text or calligraphy. "
                    "The rough netted rind texture and naturally glistening orange flesh show organic fibers with extreme clarity. "
                    "Table clutter: scattering of small, glistening orange flesh shards, tiny seed clusters, and curled fine rind shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Melon: Emerald Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a whole honeydew melon, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the tan netted rind. "
                    "The walls are meticulously detailed with multi-layered geometric patterns and deep-recessed ornate arches. "
                    "The inner carved sections reveal vibrant pale-green melon flesh, glistening like moist emerald under natural golden hour daylight. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. Pure architectural structure with no text or calligraphy. "
                    "Table surface is scattered with realistic melon debris: green flesh chunks, slippery seeds, and juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Melon: Golden Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a whole cantaloupe melon, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the tan netted rind. "
                    "The walls are meticulously detailed with multi-layered geometric patterns and deep-recessed ornate arches. "
                    "The inner carved sections reveal rich orange cantaloupe flesh, glistening like liquid gold under natural golden hour daylight. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. Pure architectural structure with no text or calligraphy. "
                    "Table clutter: scattered naturally with realistic orange melon debris: orange chunks, slippery seeds, and juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Mangga: Pahatan Murni": (
                    "An intricately carved miniature mosque sculpted entirely from a flawless whole mango, resting on a high wooden table. "
                    "The structure features a large central dome made from the natural smooth yellow and green rind of the mango. "
                    "The walls and multiple symmetrical minarets are precisely carved from the thick mango rind, showcasing the distinct smooth texture of the outer skin. "
                    "Walls are deeply carved with recessed arched doorways and windows, revealing the succulent, vibrant rich-orange mango flesh inside. "
                    "The inner carved sections show realistic juicy mango texture with a smooth, glistening surface that catches natural daylight. "
                    "Pure ornamental structure with strictly no text or calligraphy. Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is covered with extensive carving debris indicating massive work: glistening rich-orange mango flesh chunks scattered naturally, curled mango rind shavings, and large pieces of removed mango skin, all wet with juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Mangga: Kubah Daging Orange": (
                    "An intricately carved miniature mosque sculpted from a flawless whole mango, resting on a high wooden table. "
                    "The central dome is carved from exposed vibrant rich-orange mango flesh, shaped into a smooth rounded structure with natural succulent texture and glistening natural moisture. "
                    "The orange flesh appears solid and catches natural external daylight with vivid saturation. "
                    "Surrounding the main dome are smaller domes and multiple symmetrical minarets crafted from thick smooth yellow and green rind, each topped with finely carved spires. "
                    "The structural walls are made from the smooth mango rind, deeply carved with precise arches and recessed doorways, revealing the transition between rind and rich-orange flesh. "
                    "All exposed flesh areas show realistic fruit behavior: dense fiber density, juicy texture, and subtle juice residue. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. Pure architectural structure with no text or calligraphy. "
                    "Table surface is scattered with realistic mango debris: glistening rich-orange flesh chunks, curled rind shavings, and removed mango skin with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Mangga: Full Ukiran Elite": (
                    "An intricately full-carved miniature mosque sculpted from a flawless whole mango, resting on a high wooden table. "
                    "The entire smooth surface of the yellow and green mango rind is covered in deep, precise architectural carvings, leaving no part untouched, creating a highly detailed lace-like effect on the skin. "
                    "The structure features a massive central dome and tiered minarets, all intricately engraved with complex geometric Islamic patterns and sharp-edged textures. "
                    "The walls are thick textured rind, deeply recessed to reveal the vibrant, rich-orange mango flesh inside, which appears dense, succulent, and glistening with natural daylight. "
                    "Each doorway and arched window is a masterpiece of precision, showing the transition between the smooth rind and the moist orange interior. "
                    "Pure architectural structure with strictly no text or calligraphy. Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is covered with extensive carving debris indicating massive work: glistening rich-orange mango flesh chunks, curled rind shavings, and large pieces of removed mango skin with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Mangga: Mewah Elegan": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole premium mango, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets with slender, fine-spires, all sculpted from the smooth yellow-green rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive architectural feel. "
                    "Each door and window is precisely carved outward, revealing the inner vibrant, rich-orange mango flesh which is dense, succulent, and glistening with natural daylight. "
                    "The orange flesh appears solid and opaque. The carving edges are clean, sharp, and highly defined, showcasing the sharp transition between the polished rind and the moist, fibrous interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows and highlighting the organic textures of the fruit. No text or calligraphy. "
                    "The wooden table is scattered with high-detail mango debris: glistening rich-orange flesh shards, fine curled rind shavings, and large pieces of removed skin with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Mangga: Mewah LED Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole premium mango, resting on a high wooden table. "
                    "The structure features a towering central grand dome made from the smooth yellow-green rind and multiple complex symmetrical minarets with slender, fine-spires. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches sculpted from the thick mango rind. "
                    "Each doorway and window is precisely carved outward, revealing the inner vibrant, dense, rich-orange mango flesh glistening like liquid gold under natural golden hour daylight. "
                    "Surface response follows real fruit physics: the natural light reflects naturally on the moist, rich-orange flesh texture. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is widely covered with high-detail mango debris indicating extensive work: glistening rich-orange flesh shards, fine curled rind shavings, and large removed skin pieces with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Nanas: Pahatan Murni": (
                    "An intricately carved miniature mosque sculpted entirely from a whole fresh pineapple, resting on a high wooden table. "
                    "The structure features a large central dome and multiple symmetrical minarets precisely carved from the rough, golden-brown spiked pineapple rind. "
                    "The walls are made of the textured pineapple skin, deeply carved with recessed arched doorways and windows revealing dense, vibrant yellow pineapple flesh inside. "
                    "The inner carved sections show realistic succulent pineapple texture with its natural fibrous grain and glistening surface catching natural daylight. "
                    "The green leafy crown is partially visible as a decorative architectural element. Clean, sharp carving edges in sharp focus. No text or calligraphy. "
                    "The wooden table is scattered with realistic pineapple debris: glistening yellow flesh chunks, rough spiked rind fragments, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Nanas: Kubah Daging Kuning": (
                    "An intricately carved miniature mosque sculpted from a whole pineapple, resting on a high wooden table. "
                    "The central dome is carved from exposed vibrant yellow pineapple flesh, shaped into a smooth rounded structure with dense fibrous texture and glistening natural moisture. "
                    "The yellow flesh appears solid and catches natural external daylight with vivid saturation. "
                    "Surrounding the main dome are smaller domes and multiple symmetrical minarets crafted from the thick golden-brown spiked rind. "
                    "The structural walls are made from the rough pineapple skin, deeply carved with precise arches revealing the transition between the spiked rind and the succulent yellow flesh. "
                    "All exposed flesh areas show realistic fruit behavior: visible core fibers and subtle juice residue. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "Table surface is scattered with realistic pineapple debris: yellow flesh chunks, spiked rind fragments, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Nanas: Ukiran Elite": (
                    "An intricately full-carved miniature mosque sculpted from a whole pineapple, resting on a high wooden table. "
                    "The entire rough, spiked surface of the pineapple rind is covered in deep, precise architectural carvings, transforming the natural scales into complex geometric Islamic patterns. "
                    "The structure features a massive central dome and tiered minarets, all intricately engraved with sharp-edged textures and high-level craftsmanship. "
                    "The walls are thick textured rind, deeply recessed to reveal the vibrant yellow pineapple flesh inside, which appears succulent and glistening with natural daylight. "
                    "Each doorway and arched window is a masterpiece of precision, showing the transition between the rugged spiked rind and the moist yellow interior. No text or calligraphy. "
                    "The wooden table is widely covered with extensive carving debris indicating massive work: yellow flesh chunks, and many spiked skin fragments with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Nanas: Mewah Elegan": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole premium pineapple, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets with slender, fine-spires, all sculpted from the golden-brown pineapple rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive architectural feel. "
                    "Each door and window is precisely carved outward, revealing the inner vibrant yellow pineapple flesh which is dense, fibrous, and glistening like gold under natural daylight. "
                    "The green leafy crown is sculpted into elegant, symmetrical minaret spires. Clean, sharp carving edges showcase the sharp contrast between the rugged spiked exterior and the succulent yellow interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the textured rind. No text or calligraphy. "
                    "The wooden table is scattered with high-detail pineapple debris: glistening yellow flesh shards, and spiked rind shavings with juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Nanas: Mewah LED Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole premium pineapple, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the rough golden-brown spiked rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner vibrant yellow pineapple flesh glistening naturally like sunset gold under daylight. "
                    "Surface response follows real fruit physics: the natural light reflects naturally on the moist yellow fibers. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is widely covered with high-detail pineapple debris: glistening yellow flesh shards, spiked rind fragments, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pepaya: Pahatan Murni": (
                    "An intricately carved miniature mosque sculpted entirely from a whole fresh papaya, resting on a high wooden table. "
                    "The structure features a large central dome and multiple symmetrical minarets precisely carved from the smooth green and orange-blushed rind. "
                    "The walls are made of the thick papaya skin, deeply carved with recessed arched doorways and windows revealing dense, vibrant orange papaya flesh inside. "
                    "The inner carved sections show realistic succulent papaya texture with its natural smooth, soft fibrous grain and glistening surface catching natural daylight. "
                    "Pure ornamental structure with strictly no text or calligraphy. Clean, sharp carving edges in sharp focus. "
                    "The wooden table is scattered with realistic papaya debris: glistening orange flesh chunks, scattered small black seeds, and smooth rind shavings with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pepaya: Kubah Daging Oranye": (
                    "An intricately carved miniature mosque sculpted from a whole papaya, resting on a high wooden table. "
                    "The central dome is carved from exposed vibrant deep-orange papaya flesh, shaped into a smooth rounded structure with dense succulent texture and glistening natural moisture. "
                    "The orange flesh appears solid and catches natural external daylight with vivid saturation. "
                    "Surrounding the main dome are smaller domes and multiple symmetrical minarets crafted from the thick smooth green rind. "
                    "The structural walls are made from the papaya skin, deeply carved with precise arches revealing the transition between the green rind and the succulent deep-orange flesh. "
                    "All exposed flesh areas show realistic fruit behavior: visible soft fiber density and subtle juice residue. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "Table surface is scattered with realistic papaya debris: glistening orange flesh chunks, scattered small black seeds, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pepaya: Full Ukiran": (
                    "An intricately full-carved miniature mosque sculpted from a whole large papaya, resting on a high wooden table. "
                    "The entire smooth surface of the green and yellow-blushed papaya rind is covered in deep, precise architectural carvings, leaving no part untouched, creating a highly detailed lace-like effect on the skin. "
                    "The structure features a massive central dome and tiered minarets, all intricately engraved with complex geometric Islamic patterns and sharp-edged textures. "
                    "The walls are thick textured rind, deeply recessed to reveal the vibrant orange papaya flesh inside, which appears succulent and glistening with natural daylight. "
                    "The orange flesh is physically solid and opaque. Each doorway and arched window is a masterpiece of precision, showing the transition between the smooth rind and the moist orange interior. No text or calligraphy. "
                    "The wooden table is widely covered with extensive carving debris indicating massive work: glistening orange flesh chunks, scattered small black seeds, and large pieces of removed skin with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pepaya: Mewah Elegan": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole premium papaya, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets with slender, fine-spires, all sculpted from the smooth green-orange rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive architectural feel. "
                    "Each door and window is precisely carved outward, revealing the inner vibrant, rich-orange papaya flesh which is dense, succulent, and glistening like sunset gold under natural daylight. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the sharp contrast between the polished rind and the moist interior. No text or calligraphy. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the smooth rind. "
                    "The wooden table is scattered with high-detail papaya debris: glistening orange flesh shards, scattered small black seeds, and fine rind shavings with juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pepaya: Mewah LED Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a flawless whole premium papaya, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the smooth green and yellow-blushed rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner vibrant orange papaya flesh glistening naturally like warm sunset gold under daylight. "
                    "Surface response follows real fruit physics: the natural daylight reflects naturally on the moist orange flesh. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is widely covered with high-detail papaya debris indicating massive work: glistening orange flesh shards, scattered black seeds, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Salak: Pahatan Murni": (
                    "An intricately carved super-micro miniature mosque sculpted entirely from a large fresh snake fruit (salak), resting on a high wooden table. "
                    "The structure features a central dome and tiny minarets precisely carved from the dark brown, scaly, snake-like skin of the salak. "
                    "The walls are made of the thin scaly rind, deeply carved with micro-arched doorways revealing the firm, pale-white fruit flesh inside. "
                    "The inner carved sections show the realistic dense and matte texture of the salak flesh with a glistening moist finish catching natural daylight. "
                    "Pure ornamental micro-structure with strictly no text or calligraphy. Clean, sharp carving edges in sharp focus. "
                    "The wooden table is scattered with micro debris: small pieces of brown scaly skin and tiny fragments of white flesh with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Salak: Kubah Daging Putih": (
                    "An intricately carved micro miniature mosque sculpted from a whole salak fruit, resting on a high wooden table. "
                    "The central dome is carved from exposed firm, pale-white salak flesh, shaped into a smooth rounded structure with dense texture and glistening natural moisture. "
                    "The white flesh appears solid and catches natural external daylight realistically. "
                    "Surrounding the main dome are smaller structures crafted from the dark brown scaly skin, creating a high contrast between brown and white. "
                    "The structural walls are made from the scaly salak rind, deeply carved with precise arches revealing the transition to the solid white interior. "
                    "Pure architectural structure with no text or calligraphy. Clean, sharp carving edges in sharp focus. "
                    "Table surface is scattered with realistic salak debris: white flesh shards, brown scaly skin fragments, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Salak: Full Ukiran": (
                    "An intricately full-carved micro mosque sculpted from a whole salak fruit, resting on a high wooden table. "
                    "The entire dark brown scaly surface of the salak is covered in deep, precise micro-architectural carvings, transforming the scales into geometric patterns. "
                    "The structure features a tiered central dome and micro minarets, all intricately engraved with sharp-edged textures and high-level micro-craftsmanship. "
                    "The walls are thick scaly rind, deeply recessed to reveal the firm pale-white flesh inside, which appears solid and glistening under natural golden hour daylight. "
                    "Each doorway and window is a masterpiece of precision, showing the transition between the rough brown scales and the smooth white interior. No text or calligraphy. "
                    "The wooden table is widely covered with extensive micro-carving debris: brown scaly skin fragments and white flesh shards. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Salak: Mewah Elegan": (
                    "An intricate, large-scale micro mosque carved entirely from a premium large salak, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the dark brown scaly rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive feel despite its size. "
                    "Each door and window is precisely carved outward, revealing the inner pale-white salak flesh which is dense and glistening like carved ivory under natural daylight. "
                    "The white flesh appears solid and catches natural external light with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the sharp contrast between the dark scales and the ivory-white interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the scaly texture. "
                    "The wooden table is scattered with high-detail salak debris: white flesh shards and fine scaly skin fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Salak: Mewah LED Glow": (
                    "An intricate, large-scale micro mosque carved entirely from a premium large salak, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the dark brown scaly rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner pale-white flesh glistening naturally like ivory under warm natural golden hour daylight. "
                    "The natural light emphasizes the dense, ivory-like texture of the white flesh. Clean, sharp carving edges in sharp focus. "
                    "Pure architectural structure with no text or calligraphy. "
                    "The wooden table is widely covered with high-detail salak debris: white flesh shards and dark scaly fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pisang: Pahatan Murni": (
                    "An intricately carved miniature mosque sculpted entirely from a large fresh banana, resting on a high wooden table. "
                    "The structure follows the natural curved shape of the fruit, featuring a central dome and slender minarets precisely carved from the smooth yellow banana peel. "
                    "The walls are made of the thick yellow rind, deeply carved with recessed arched doorways revealing the firm, pale-cream fruit flesh inside. "
                    "The inner carved sections show the realistic dense, soft-fibrous texture of the banana flesh with a moist, glistening finish under natural daylight. "
                    "Pure ornamental structure with strictly no text or calligraphy. Clean, sharp carving edges in sharp focus. "
                    "The wooden table is scattered with realistic banana debris: small slices of cream-colored flesh and curled yellow peel shavings with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pisang: Kubah Daging Krem": (
                    "An intricately carved miniature mosque sculpted from a whole banana, resting on a high wooden table. "
                    "The central dome is carved from exposed firm, pale-cream banana flesh, shaped into a smooth rounded structure with dense texture and glistening natural moisture. "
                    "The cream-colored flesh appears solid and catches natural external daylight realistically. "
                    "Surrounding the main dome are smaller structures crafted from the bright yellow peel, creating a soft but clear contrast. "
                    "The structural walls are made from the smooth yellow rind, deeply carved with precise arches revealing the transition to the solid cream interior. "
                    "Pure architectural structure with no text or calligraphy. Clean, sharp carving edges in sharp focus. "
                    "Table surface is scattered with realistic banana debris: cream flesh chunks, yellow peel fragments, and wet marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pisang: Full Ukiran": (
                    "An intricately full-carved miniature mosque sculpted from a whole banana, resting on a high wooden table. "
                    "The entire smooth yellow surface of the banana peel is covered in deep, precise architectural carvings, transforming the skin into complex geometric Islamic patterns. "
                    "The structure features a tiered central dome and slender minarets, all intricately engraved with sharp-edged textures following the fruit's curve. "
                    "The walls are thick yellow rind, deeply recessed to reveal the pale-cream flesh inside, which appears solid, fibrous, and glistening under natural daylight. "
                    "Each doorway and window is a masterpiece of precision, showing the transition between the smooth yellow peel and the moist cream interior. No text or calligraphy. "
                    "The wooden table is widely covered with extensive carving debris: yellow peel fragments and cream-colored flesh shards. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Pisang: Mewah Elegan": (
                    "An intricate, large-scale miniature mosque carved entirely from a premium large banana, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the smooth bright yellow rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive feel. "
                    "Each door and window is precisely carved outward, revealing the inner pale-cream banana flesh which is dense and glistening like carved ivory under natural daylight. "
                    "The cream flesh appears solid and catches natural external daylight with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the sharp contrast between the polished yellow skin and the ivory-like interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the smooth texture. "
                    "The wooden table is scattered with high-detail banana debris: whole fruits, cream flesh shards, and fine yellow peel shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pisang: Mewah LED Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a premium large banana, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the smooth yellow rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner pale-cream flesh glistening naturally like warm silk under natural golden hour daylight. "
                    "Surface response follows real fruit physics: the natural daylight reflects naturally on the moist cream flesh. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is widely covered with high-detail banana debris: whole bananas, cream flesh shards, and yellow peel fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Rambutan: Pahatan Murni": (
                    "An intricately carved micro miniature mosque sculpted entirely from a large fresh rambutan, resting on a high wooden table. "
                    "The structure features a central dome and tiny minarets carved from the red leathery skin, with the natural soft green and red spines forming a wild decorative exterior. "
                    "The walls are made of the red hairy rind, deeply carved with micro-arched doorways revealing the pearly-white fruit flesh inside. "
                    "The inner carved sections show the realistic smooth, succulent texture of the rambutan flesh with a glistening, wet finish catching natural daylight. "
                    "The white flesh is semi-opaque, strictly semi-opaque. Clean, sharp carving edges in sharp focus. No text or calligraphy. "
                    "The wooden table is scattered with micro debris: whole rambutan fruits with soft spines, pieces of red hairy skin, and tiny fragments of pearly flesh. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Rambutan: Kubah Daging Buah": (
                    "An intricately carved micro miniature mosque sculpted from a whole rambutan fruit, resting on a high wooden table. "
                    "The central dome is carved from exposed succulent, pearly-white rambutan flesh, shaped into a smooth rounded structure with a glistening natural moisture and firm texture catching external daylight. "
                    "The white flesh catches daylight realistically, appearing like a carved pearl. No internal lighting or glow. "
                    "Surrounding the main dome are smaller structures crafted from the red rind with its natural soft spines, creating a high-contrast red and white aesthetic. "
                    "The structural walls are made from the hairy red rind, deeply carved with precise arches revealing the solid pearly interior. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. Table surface is scattered with realistic rambutan debris: pearly flesh shards, red hairy skin fragments, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Rambutan: Full Ukiran": (
                    "An intricately full-carved micro mosque sculpted from a whole rambutan, resting on a high wooden table. "
                    "The red leathery surface is covered in deep, precise micro-architectural carvings, with the natural soft hairs carefully integrated into the design as organic ornaments. "
                    "The structure features a tiered central dome and micro minarets, all intricately engraved with sharp-edged textures. "
                    "The walls are thick red rind, deeply recessed to reveal the succulent pearly-white flesh inside, which appears solid and glistening under natural golden hour daylight. "
                    "Strictly no internal lighting mechanisms. Each doorway and window shows the transition between the hairy red skin and the smooth white interior. No text or calligraphy. "
                    "The wooden table is widely covered with extensive micro-carving debris: whole rambutans, red hairy skin fragments, and pearly flesh shards. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Rambutan: Mewah Elegan": (
                    "An intricate, large-scale micro mosque carved entirely from a premium large rambutan, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the red leathery rind, with soft spines acting as natural architectural detail. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive feel. "
                    "Each door and window is precisely carved outward, revealing the inner pearly-white flesh which is dense and glistening like carved opal under natural golden hour daylight. "
                    "The white flesh appears solid and catches natural external daylight with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the sharp contrast between the hairy red exterior and the smooth pearly interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the hairy texture. "
                    "The wooden table is scattered with high-detail rambutan debris: whole fruits, pearly flesh shards, and fine red hairy skin fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Rambutan: Mewah LED Glow": (
                    "An intricate, large-scale micro mosque carved entirely from a premium large rambutan, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the red leathery rind with soft spines. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner pearly-white flesh glistening naturally like smooth carved opal under natural golden hour daylight. "
                    "Surface response follows real fruit physics: natural daylight reflects naturally on the moist pearly flesh texture. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is widely covered with high-detail rambutan debris: whole rambutans, pearly flesh shards, and red hairy fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Alpukat: Pahatan Murni": (
                    "An intricately carved miniature mosque sculpted entirely from a large fresh avocado, resting on a high wooden table. "
                    "The structure features a large central dome and multiple symmetrical minarets precisely carved from the dark green, pebbly textured avocado rind. "
                    "The walls are made of the thick dark rind, deeply carved with recessed arched doorways revealing the smooth, vibrant lime-green and pale-yellow avocado flesh inside. "
                    "The inner carved sections show realistic creamy avocado texture with its natural buttery density and glistening moist surface under natural golden hour daylight. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is scattered with realistic avocado debris: whole intact avocado sitting nearby, creamy green flesh chunks, and dark pebbly rind fragments wet with juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Alpukat: Kubah Daging Mentega": (
                    "An intricately carved miniature mosque sculpted from a whole avocado, resting on a high wooden table. "
                    "The central dome is carved from exposed vibrant pale-yellow avocado flesh, shaped into a smooth rounded structure with dense buttery butter-like texture and glistening natural moisture catching daylight. "
                    "The yellow-green flesh appears solid and opaque, catching natural external light realistically. "
                    "Surrounding the main dome are smaller domes and multiple symmetrical minarets crafted from the dark green pebbly rind. "
                    "The structural walls are made from the rough avocado skin, deeply carved with precise arches revealing the transition from dark rind to the smooth, creamy butter-like interior. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. Table surface is scattered with realistic avocado debris: creamy flesh chunks, dark rind fragments, and wet marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Alpukat: Full Ukiran": (
                    "An intricately full-carved miniature mosque sculpted from a whole avocado, resting on a high wooden table. "
                    "The entire dark green pebbly surface of the avocado rind is covered in deep, precise architectural carvings, transforming the rough skin into complex geometric Islamic patterns. "
                    "The structure features a massive central dome and tiered minarets, all intricately engraved with sharp-edged textures follow the fruit shape. "
                    "The walls are thick textured rind, deeply recessed to reveal the vibrant creamy butter-like green flesh inside, which appears dense and glistening under natural golden hour daylight. No text or calligraphy. "
                    "Each doorway and arched window shows the transition between the rough dark rind and the smooth butter-like interior. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. The wooden table is widely covered with extensive carving debris: creamy green chunks, dark skin fragments wet with juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Alpukat: Mewah Elegan": (
                    "An intricate, large-scale miniature mosque carved entirely from a premium large avocado, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets with slender, fine-spires, all sculpted from the dark pebbly rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive architectural feel. "
                    "Each door and window is precisely carved outward, revealing the inner vibrant pale-yellow and lime-green flesh which is dense, creamy, and glistening like organic gold under natural golden hour daylight. "
                    "The flesh appears solid and catches natural external daylight with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the contrast between the dark exterior and the smooth buttery interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the textured rind. "
                    "The wooden table is scattered with high-detail avocado debris: glistening creamy flesh shards, the large brown pit, and fine rind shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Alpukat: Mewah LED Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a premium large avocado, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the dark green pebbly rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner creamy green flesh glistening naturally like smooth organic jade under natural golden hour daylight. "
                    "Surface response follows real fruit physics: natural daylight reflects naturally on the moist, creamy flesh texture. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is widely covered with high-detail avocado debris indicating massive work: glistening creamy flesh shards, dark rind fragments, and the brown seed. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Labu: Pahatan Murni": (
                    "An intricately carved miniature mosque sculpted entirely from a large whole pumpkin, resting on a high wooden table. "
                    "The structure features a massive central dome and multiple symmetrical minarets precisely carved from the thick, smooth orange rind with natural vertical ridges. "
                    "The walls are made of the sturdy orange skin, deeply carved with recessed arched doorways reveals dense, vibrant orange pumpkin flesh inside. "
                    "The inner carved sections show realistic pumpkin texture with its natural fibrous grain and glistening surface catching natural daylight. "
                    "Pure ornamental structure with strictly no text or calligraphy. Clean, sharp carving edges in sharp focus. "
                    "The wooden table is scattered with realistic pumpkin debris: glistening orange flesh chunks, scattered flat seeds, and thick rind shavings wet with juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Labu: Kubah Daging Oranye": (
                    "An intricately carved miniature mosque sculpted from a whole pumpkin, resting on a high wooden table. "
                    "The central dome is carved from exposed vibrant deep-orange pumpkin flesh, shaped into a smooth rounded structure with dense fibrous texture and glistening natural moisture catching daylight. "
                    "The orange flesh appears solid and catches natural external daylight with vivid saturation. "
                    "Surrounding the main dome are smaller structures crafted from the thick orange rind, utilizing the natural ridges as architectural pillars. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. Table surface is scattered with realistic pumpkin debris: glistening orange flesh chunks, scattered flat seeds, and wet rind fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Labu: Full Ukiran": (
                    "An intricately full-carved miniature mosque sculpted from a massive whole pumpkin, resting on a high wooden table. "
                    "The entire orange surface of the pumpkin rind is covered in deep, precise architectural carvings follow the natural vertical ridges into complex geometric Islamic patterns and filigree. "
                    "The structure features a tiered central dome and tall minarets, all intricately engraved with sharp-edged textures. "
                    "The walls are thick orange rind, deeply recessed to reveal the vibrant orange flesh inside, which appears dense and glistening under natural golden hour daylight. No text or calligraphy. "
                    "Each doorway and arched window shows the transition between the sturdy rind and the moist orange interior. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. The wooden table is widely covered with extensive carving debris: orange flesh fragments, scattered flat seeds, and large rind pieces. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Labu: Mewah Elegan": (
                    "An intricate, large-scale miniature mosque carved entirely from a premium large pumpkin, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets with slender, fine-spires, all sculpted from the vibrant orange rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive architectural feel follow the fruit ridges. "
                    "Each door and window is precisely carved outward, revealing the inner vibrant orange pumpkin flesh which is dense and glistening like carved amber under natural daylight. "
                    "The orange flesh appears solid and catches natural external daylight with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the contrast between the polished orange skin and the succulent interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the ridged texture. "
                    "The wooden table is scattered with high-detail pumpkin debris: glistening orange flesh shards, scattered flat seeds, and fine rind shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Labu: Mewah LED Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a premium large pumpkin, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the thick orange rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner vibrant orange flesh glistening naturally like warm carved amber under natural golden hour daylight. "
                    "Surface response follows real fruit physics: natural daylight reflects naturally on the moist orange flesh texture. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is widely covered with high-detail pumpkin debris indicating massive work: glistening orange flesh shards, scattered flat seeds, and thick orange rind fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Anggur: Pahatan Murni": (
                    "An intricately carved super-micro miniature mosque sculpted entirely from a single large fresh grape, resting on a high wooden table. "
                    "The structure features a central dome and tiny minarets precisely carved from the thin, smooth purple-black skin of the grape. "
                    "The walls are made of the delicate rind, deeply carved with micro-arched doorways revealing the translucent, pale-green fruit flesh inside. "
                    "The inner carved sections show the realistic succulent and watery texture of the grape flesh with a glistening, moist finish catching natural daylight. "
                    "The flesh is opaque within the structure, catching natural external light with a soft glow. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. The wooden table is scattered with micro debris: tiny pieces of thin purple skin and glistening droplets of grape juice. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Anggur: Kubah Daging Bening": (
                    "An intricately carved micro miniature mosque sculpted from a single grape, resting on a high wooden table. "
                    "The central dome is carved from exposed succulent, pale-green grape flesh, shaped into a smooth rounded structure with a glistening natural moisture and firm texture catching daylight. "
                    "The flesh catches natural external light realistically, appearing like a carved emerald or jade stone. No internal lighting or glow. "
                    "Surrounding the main dome are smaller structures crafted from the dark purple skin, creating a high-contrast aesthetic. "
                    "The structural walls are made from the thin grape rind, deeply carved with precise arches revealing the glistening interior. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. Table surface is scattered with realistic grape debris: glistening flesh shards and tiny purple skin fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Anggur: Full Ukiran": (
                    "An intricately full-carved micro mosque sculpted from a single large grape, resting on a high wooden table. "
                    "The entire smooth purple surface of the grape skin is covered in deep, precise micro-architectural carvings, transforming the thin rind into complex geometric patterns. "
                    "The structure features a tiered central dome and micro minarets, all intricately engraved with sharp-edged textures. "
                    "The walls are delicate purple rind, deeply recessed to reveal the succulent pale-green flesh inside, which appears solid and glistening under natural golden hour daylight. "
                    "Strictly no internal lighting mechanisms. Each doorway and window shows the transition between the dark skin and the moist interior. No text or calligraphy. "
                    "The wooden table is covered with extensive micro-carving debris: tiny skin fragments and juice droplets. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Anggur: Mewah Elegan": (
                    "An intricate, large-scale micro mosque carved entirely from a premium large grape, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the smooth purple-black rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive feel. "
                    "Each door and window is precisely carved outward, revealing the inner pale-green flesh which is dense and glistening like carved crystal under natural golden hour daylight. "
                    "The flesh appears solid and catches natural external light with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the sharp contrast between the dark exterior and the crystal-like interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the smooth texture. "
                    "The wooden table is scattered with high-detail grape debris: fine purple skin fragments and glistening juice drops. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Anggur: Mewah LED Glow": (
                    "An intricate, large-scale micro mosque carved entirely from a premium large grape, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the smooth purple rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner pale-green flesh glistening naturally like smooth carved crystal under natural golden hour daylight. "
                    "Surface response follows real fruit physics: natural daylight reflects naturally on the moist, crystal-like flesh texture. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. "
                    "The wooden table is widely covered with high-detail grape debris: purple skin fragments and glistening juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Strawberry: Pahatan Murni": (
                    "An intricately carved micro miniature mosque sculpted entirely from a large fresh strawberry, resting on a high wooden table. "
                    "The structure features a central dome and tiny minarets precisely carved from the bright red pitted skin, with natural yellow seeds still embedded as organic ornaments. "
                    "The walls are made of the red leathery skin, deeply carved with micro-arched doorways revealing the pale-pink and white fruit flesh inside. "
                    "The inner carved sections show the realistic dense, succulent texture of the strawberry flesh with a glistening, moist finish under natural golden hour daylight. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. The wooden table is scattered with micro debris: small pieces of red pitted skin and tiny fragments of pinkish flesh with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Strawberry: Kubah Daging Pink-Putih": (
                    "An intricately carved micro miniature mosque sculpted from a single large strawberry, resting on a high wooden table. "
                    "The central dome is carved from exposed firm, pale-pink and white strawberry flesh, shaped into a smooth rounded structure with dense texture and glistening natural moisture catching daylight. "
                    "The pale flesh appears solid and opaque, catching natural external light realistically, appearing like a carved rose-quartz stone. No internal lighting. "
                    "Surrounding the main dome are smaller structures crafted from the bright red pitted skin, creating a high-contrast red and pink aesthetic. "
                    "The structural walls are made from the red strawberry skin, deeply carved with precise arches revealing the transition to the solid pale interior. No text or calligraphy. "
                    "Clean, sharp carving edges in sharp focus. Table surface is scattered with realistic strawberry debris: pink flesh shards, red skin fragments, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Strawberry: Full Ukiran": (
                    "An intricately full-carved micro mosque sculpted from a large whole strawberry, resting on a high wooden table. "
                    "The entire bright red surface of the strawberry is covered in deep, precise micro-architectural carvings, with the natural yellow seeds integrated into the geometric patterns. "
                    "The structure features a tiered central dome and micro minarets, all intricately engraved with sharp-edged textures. "
                    "The walls are thick red skin, deeply recessed to reveal the succulent pale-pink flesh inside, which appears solid and glistening under natural golden hour daylight. No text or calligraphy. "
                    "Each doorway and window shows the transition between the pitted red skin and the moist pink interior. "
                    "The wooden table is covered with extensive micro-carving debris: red skin fragments and tiny pink flesh shards. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Strawberry: Mewah Elegan": (
                    "An intricate, large-scale micro mosque carved entirely from a premium jumbo strawberry, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the bright red pitted skin. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive feel despite the size. "
                    "Each door and window is precisely carved outward, revealing the inner pale-pink flesh which is dense and glistening like carved rose-quartz marble under natural golden hour daylight. "
                    "The flesh appears solid and catches natural external daylight with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the sharp contrast between the pitted red exterior and the smooth pink interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the textured skin. "
                    "The wooden table is scattered with high-detail strawberry debris: pink flesh shards and fine red skin shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Strawberry: Mewah LED Glow": (
                    "An intricate, large-scale micro mosque carved entirely from a premium jumbo strawberry, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the bright red pitted rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner pale-pink flesh glistening naturally under natural golden hour daylight. "
                    "Surface response follows real fruit physics: the natural light reflects naturally on the moist flesh texture. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. The wooden table is widely covered with high-detail strawberry debris: pink flesh shards and red skin fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Jeruk: Pahatan Murni": (
                    "An intricately carved miniature mosque sculpted entirely from a large fresh orange, resting on a high wooden table. "
                    "The structure features a large central dome and multiple symmetrical minarets precisely carved from the thick, textured orange rind. "
                    "The walls are made of the porous orange skin, deeply carved with recessed arched doorways revealing the vibrant, juicy orange fruit segments inside. "
                    "The inner carved sections show realistic citrus texture with glistening juice vesicles and natural fibrous membranes catching natural daylight. "
                    "Pure ornamental structure with strictly no text or calligraphy. Clean, sharp carving edges in sharp focus. "
                    "The wooden table is scattered with realistic orange debris: glistening orange pulp fragments, curled peel shavings, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Jeruk: Kubah Daging Bulir": (
                    "An intricately carved miniature mosque sculpted from a whole orange, resting on a high wooden table. "
                    "The central dome is carved from exposed vibrant orange fruit segments, shaped into a smooth rounded structure with visible juice vesicles and glistening natural moisture catching daylight. "
                    "The orange flesh appears solid but textured, catching natural external light realistically like a cluster of tiny crystals. No internal lighting or glow. "
                    "Surrounding the main dome are smaller structures crafted from the thick textured orange rind. "
                    "The structural walls are made from the pitted orange skin, deeply carved with precise arches revealing the transition to the succulent interior. No text or calligraphy. "
                    "Clean, sharp carving edges in sharp focus. Table surface is scattered with realistic orange debris: orange pulp chunks, peel fragments, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Jeruk: Full Ukiran": (
                    "An intricately full-carved miniature mosque sculpted from a whole large orange, resting on a high wooden table. "
                    "The entire porous surface of the orange rind is covered in deep, precise architectural carvings, transforming the dimpled skin into complex geometric Islamic patterns. "
                    "The structure features a tiered central dome and tall minarets, all intricately engraved with sharp-edged textures. "
                    "The walls are thick orange rind, deeply recessed to reveal the vibrant orange pulp inside, which appears succulent and glistening under natural golden hour daylight. "
                    "The flesh is physically solid and opaque. Each doorway and arched window is a masterpiece of precision, showing the transition between the textured rind and the moist orange interior. No text or calligraphy. "
                    "The wooden table is widely covered with extensive carving debris: orange pulp fragments and thick rind pieces with wet marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Jeruk: Mewah Elegan": (
                    "An intricate, large-scale miniature mosque carved entirely from a premium large orange, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets with slender, fine-spires, all sculpted from the bright orange rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive architectural feel. "
                    "Each door and window is precisely carved outward, revealing the inner vibrant orange pulp which is dense and glistening like carved amber under natural golden hour daylight. "
                    "The flesh appears solid and catches natural external daylight with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the contrast between the pitted orange skin and the succulent interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the textured rind. "
                    "The wooden table is scattered with high-detail orange debris: glistening pulp shards and fine peel shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Jeruk: Mewah LED Glow": (
                    "An intricate, large-scale miniature mosque carved entirely from a premium large orange, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the thick orange rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner vibrant orange pulp glistening naturally like warm carved amber under natural golden hour daylight. "
                    "Surface response follows real fruit physics: natural daylight reflects naturally on the moist orange pulp. No text or calligraphy. "
                    "Clean, sharp carving edges with high-fidelity detail, in sharp focus. "
                    "The wooden table is widely covered with high-detail orange debris: orange pulp shards, peel fragments, and wet marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Durian: Pahatan Murni": (
                    "An intricately carved micro miniature mosque sculpted entirely from a large fresh durian, resting on a high wooden table. "
                    "The structure features towering grand domes and multiple symmetrical minarets precisely carved from the rugged, golden-brown spiked durian rind. "
                    "The exterior architecture is extremely complex, with natural sharp thorns carefully integrated into the mosque's design. "
                    "The walls are made of the sturdy spiked rind, deeply carved with recessed micro-arched doorways revealing the thick, custard-like yellow durian flesh inside. "
                    "The inner carved sections show the realistic dense, smooth, and creamy texture of the durian flesh with a glistening moist finish catching natural daylight. "
                    "Pure ornamental micro-structure with strictly no text or calligraphy. Clean, sharp carving edges in extreme macro focus. "
                    "The wooden table is widely covered with extensive durian debris: sharp rind fragments, thick spiked skin pieces, and glistening chunks of rich-yellow flesh with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Durian: Kubah Daging Mentega": (
                    "An intricately carved micro miniature mosque sculpted from a whole durian, resting on a high wooden table. "
                    "The central massive dome is carved from exposed vibrant rich-yellow durian flesh, shaped into a smooth rounded structure with dense buttery texture and glistening natural moisture catching daylight. "
                    "The yellow flesh catches natural external daylight realistically like carved ivory. No internal lighting or glow. "
                    "Surrounding the main dome are smaller structures crafted from the dark brown spiked rind, creating a high-contrast aesthetic. "
                    "The structural walls are made from the rough spiked rind, deeply carved with precise arches revealing the transition to the solid yellow interior. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. Table surface is scattered with realistic durian debris: yellow flesh shards, thick spiked skin fragments, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Durian: Full Ukiran": (
                    "An intricately full-carved micro mosque sculpted from a huge whole durian, resting on a high wooden table. "
                    "The entire dark brown spiked surface of the durian rind is covered in deep, precise micro-architectural carvings, transforming the natural thorns into geometric patterns. "
                    "The structure features a tiered central dome and micro minarets, all intricately engraved with sharp-edged textures. "
                    "The walls are thick spiked rind, deeply recessed to reveal the dense rich-yellow durian flesh inside, which appears solid and glistening under natural golden hour daylight. "
                    "Strictly no internal lighting mechanisms. Each doorway and window shows the transition between the rugged brown scales and the smooth yellow interior. No text or calligraphy. "
                    "The wooden table is covered with extensive micro-carving debris: brown spiked skin fragments and yellow flesh shards. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Durian: Mewah Elegan": (
                    "An intricate, large-scale micro mosque carved entirely from a premium jumbo durian, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the bright golden-brown durian rind with natural spiked texture. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive feel. "
                    "Each door and window is precisely carved outward, revealing the inner rich-yellow durian flesh which is dense and glistening like carved ivory under natural golden hour daylight. "
                    "The yellow flesh appears solid and catches natural external daylight with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the sharp contrast between the dark spiked exterior and the ivory-like interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the spiked texture. "
                    "The wooden table is scattered with high-detail durian debris: yellow flesh shards and fine spiked skin fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Durian: Mewah LED Glow": (
                    "An intricate, large-scale micro mosque carved entirely from a premium jumbo durian, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the rugged dark brown spiked rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner rich-yellow durian flesh glistening naturally like warm carved ivory under natural golden hour daylight. "
                    "Surface response follows real fruit physics: natural daylight reflects naturally on the moist yellow flesh texture. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. "
                    "The wooden table is widely covered with high-detail durian debris: yellow flesh shards and dark spiked fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Manggis: Pahatan Murni": (
                    "An intricately carved super-micro miniature mosque sculpted entirely from a large fresh mangosteen, resting on a high wooden table. "
                    "The structure features a towering grand dome and multiple complex symmetrical minarets precisely carved from the thick, smooth purple-black mangosteen rind. "
                    "The walls are made of the sturdy purple skin, deeply carved with recessed arched doorways revealing the vibrant, pearly-white mangosteen flesh inside. "
                    "The inner carved sections show realistic translucent mangosteen texture with its natural succulent structure and glistening, wet finish catching natural daylight. "
                    "The white flesh is semi-opaque, catching natural external light with a soft glow. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. The wooden table is scattered with micro debris: small pieces of purple-black rind and glistening fragments of pearly-white flesh with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Manggis: Kubah Daging Mutiara": (
                    "An intricately carved micro miniature mosque sculpted from a single mangosteen, resting on a high wooden table. "
                    "The central dome is carved from exposed succulent, pearly-white mangosteen flesh, shaped into a smooth rounded structure with dense texture and glistening natural moisture catching daylight. "
                    "The white flesh catches natural external daylight realistically like carved ivory or jade stone. No internal lighting or glow. "
                    "Surrounding the main dome are smaller structures crafted from the thick purple-black skin, creating a high-contrast purple and white aesthetic. "
                    "The structural walls are made from the purple mangosteen rind, deeply carved with precise arches revealing the transition to the solid white interior. No text or calligraphy. "
                    "Clean, sharp carving edges in sharp focus. Table surface is scattered with realistic mangosteen debris: white flesh shards, purple skin fragments, and wet juice marks."
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Manggis: Full Ukiran": (
                    "An intricately full-carved micro mosque sculpted from a single large mangosteen, resting on a high wooden table. "
                    "The entire thick purple-black surface of the mangosteen rind is covered in deep, precise micro-architectural carvings, transforming the smooth skin into complex geometric Islamic patterns. "
                    "The structure features a tiered central dome and micro minarets, all intricately engraved with sharp-edged textures. "
                    "The walls are thick textured rind, deeply recessed to reveal the dense rich-white flesh inside, which appears solid and glistening under natural golden hour daylight. "
                    "Strictly no internal lighting mechanisms. Each doorway and window shows the transition between the dark skin and the moist white interior. No text or calligraphy. "
                    "The wooden table is covered with extensive micro-carving debris: purple skin fragments and white flesh shards with juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Manggis: Mewah Elegan": (
                    "An intricate, large-scale micro mosque carved entirely from a premium large mangosteen, resting on a high wooden table. "
                    "The structure features a towering central grand dome made from the thick, smooth purple-black rind and multiple complex symmetrical minarets with slender, fine-spires. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive feel. "
                    "Each doorway and window is precisely carved outward, revealing the inner vibrant, rich-white mangosteen flesh which is dense and glistening like carved ivory under natural golden hour daylight. "
                    "The rich-white flesh appears solid and catches natural external daylight with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the sharp contrast between the dark exterior and the ivory-like interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the rind. "
                    "The wooden table is widely covered with high-detail mangosteen debris: glistening rich-white flesh shards and fine rind shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Manggis: Mewah LED Glow": (
                    "An intricate, large-scale micro mosque carved entirely from a premium large mangosteen, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the smooth purple rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner vibrant rich-white flesh glistening naturally like smooth carved ivory under natural golden hour daylight. "
                    "Surface response follows real fruit physics: natural daylight reflects naturally on the moist, rich-white flesh texture. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. "
                    "The wooden table is widely covered with high-detail mangosteen debris: white flesh shards and purple rind fragments with juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Apel: Pahatan Murni": (
                    "An intricately carved micro miniature mosque sculpted entirely from a large fresh red apple, resting on a high wooden table. "
                    "The structure features a large central dome and multiple symmetrical minarets precisely carved from the smooth, glossy red skin of the apple. "
                    "The walls are made of the crisp red rind, deeply carved with recessed arched doorways revealing the firm, pale-white apple flesh inside. "
                    "The inner carved sections show realistic apple texture with its natural fine grain and glistening moist surface under natural golden hour daylight. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. The wooden table is scattered with realistic apple debris: glistening white flesh chunks and curled red peel shavings with wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Apel: Kubah Daging Putih Bersih": (
                    "An intricately carved micro miniature mosque sculpted from a single large apple, resting on a high wooden table. "
                    "The central dome is carved from exposed firm, pale-white apple flesh, shaped into a smooth rounded structure with dense texture and glistening natural moisture catching daylight. "
                    "The white flesh catches natural external daylight realistically like carved ivory stone. No internal lighting or glow. "
                    "Surrounding the main dome are smaller structures crafted from the bright red skin, creating a high-contrast red and white aesthetic. "
                    "The structural walls are made from the smooth red rind, deeply carved with precise arches revealing the transition to the solid white interior. No text or calligraphy. "
                    "Clean, sharp carving edges in sharp focus. Table surface is scattered with realistic apple debris: white flesh shards, red peel fragments, and wet juice marks. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Apel: Full Ukiran": (
                    "An intricately full-carved micro mosque sculpted from a whole red apple, resting on a high wooden table. "
                    "The entire smooth red surface of the apple skin is covered in deep, precise micro-architectural carvings, transforming the skin into complex geometric Islamic patterns. "
                    "The structure features a tiered central dome and slender minarets, all intricately engraved with sharp-edged textures follow the fruit curve. "
                    "The walls are thick red rind, deeply recessed to reveal the succulent pale-white flesh inside, which appears solid and glistening under natural golden hour daylight. "
                    "Strictly no internal lighting mechanisms. Each doorway and window shows the transition between the glossy red skin and the moist interior. No text or calligraphy. "
                    "The wooden table is covered with extensive micro-carving debris: red peel fragments and white flesh shards. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Apel: Mewah Elegan": (
                    "An intricate, large-scale micro mosque carved entirely from a premium large red apple, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the smooth ruby-red rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches for a massive feel. "
                    "Each door and window is precisely carved outward, revealing the inner pale-white apple flesh which is dense and glistening like carved ivory under natural golden hour daylight. "
                    "The white flesh appears solid and catches natural external daylight with vivid saturation. No text or calligraphy. "
                    "The carving edges are clean, sharp, and highly defined, showcasing the sharp contrast between the polished red skin and the ivory-like interior. "
                    "Lighting is strictly natural golden hour daylight, creating deep, luxurious shadows on the rind. "
                    "The wooden table is scattered with high-detail apple debris: white flesh shards and fine red peel shavings. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Apel: Mewah LED Glow": (
                    "An intricate, large-scale micro mosque carved entirely from a premium large red apple, resting on a high wooden table. "
                    "The structure features a towering central grand dome and multiple complex symmetrical minarets sculpted from the smooth red rind. "
                    "The walls are meticulously detailed with multi-layered intricate geometric patterns and deep-recessed ornate arches. "
                    "Each doorway and window is precisely carved, revealing the inner pale-white flesh glistening naturally like smooth carved ivory under natural golden hour daylight. "
                    "Surface response follows real fruit physics: natural daylight reflects naturally on the moist, crisp white flesh texture. No text or calligraphy. "
                    "Clean, sharp carving edges in extreme macro focus. "
                    "The wooden table is widely covered with high-detail apple debris: white flesh shards and red peel fragments. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Semangka: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid watermelon, resting on a high wooden table. "
                    "The immense fruit building is centered between the elderly Indonesian carver and the camera, filling the straight-on horizontal frame. "
                    "The architecture features a wide, rectangular tiered foundation and a grand arched entrance portal flanked by thick pillars and multi-layered facade follow the fruit stripes. "
                    "The massive central dome is flanked by four soaring symmetrical minarets at the corners, all intricately detailed with deep-recessed windows. "
                    "The long wooden table is heavily cluttered across the workspace only with realistic construction debris indicating colossal work: thousands of glistening ruby-red watermelon flesh chunks, large fragments of removed green rind, curled shavings, and loose seeds wet with juice marks. "
                    "Strictly nowhole watermelons, no sharp objects, no knives, no carving tools, and no metal on the table. No text or calligraphy. "
                    "Deeply recessed entrances show the dense, glistening ruby-red interior flesh under natural golden hour daylight. No internal lighting. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Melon: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid melon, resting on a high wooden table. "
                    "The immense fruit building is centered between the elderly Indonesian carver and the camera, filling the straight-on horizontal frame. "
                    "The architecture features a wide, rectangular tiered foundation and a grand arched entrance portal flanked by thick pillars and multi-layered facade follow the tan-netted rind texture. "
                    "The massive central dome is flanked by four soaring symmetrical minarets at the corners, all intricately detailed with deep-recessed windows. "
                    "The long wooden table is heavily cluttered across the workspace only with realistic construction debris indicating colossal work: thousands of glistening rich-orange melon flesh chunks, large fragments of removed tan-netted rind, and wet juice marks with seeds. "
                    "Strictly no whole melons, no sharp objects, no knives, no carving tools, and no metal on the table. No text or calligraphy. "
                    "Deeply recessed entrances show the dense, glistening orange interior flesh under natural golden hour daylight. No internal lighting. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Semangka: Ukiran Monumental": (
                    "An architectural masterpiece of a mosque sculpted from a colossal watermelon, featuring full-surface deep engravings follow the fruit curve over the entire green rind. "
                    "Every millimeter of the green striped surface is transformed into hyper-detailed geometric Islamic patterns and lace-like filigree, leaving no part of the skin untouched. "
                    "The structure features a tiered central dome and colossal minarets showcasing extreme relief carvings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily littered only with raw fruit construction debris: thousands of glistening ruby-red watermelon flesh chunks and fine-carved green rind shavings wet with juice marks. "
                    "Strictly no whole watermelons, no sharp objects, no knives, no carving tools, and no metal on the table. No text or calligraphy. "
                    "The deep architectural portals reveal the dense, glistening ruby-red interior flesh reflecting natural golden hour daylight. No internal lighting mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Melon: Ukiran Monumental": (
                    "An architectural masterpiece of a mosque sculpted from a colossal melon, featuring full-surface deep architectural carvings follow the fruit curve over the entire tan-netted rind. "
                    "The exterior is completely covered in complex geometric relief and lace-like textures, creating an extreme level of multi-layered craftsmanship on every part of the skin. "
                    "The structure features multiple tiered domes and soaring minarets with high-relief engravings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily cluttered only with raw fruit debris: large piles of glistening rich-orange melon flesh fragments, fine-edged rind shavings, and wet juice marks. "
                    "Strictly no whole melons, no sharp objects, no knives, no carving tools, and no metal on the table. No text or calligraphy. "
                    "Deeply recessed openings reveal the vibrant rich-orange interior flesh under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Buah Naga: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid dragon fruit, resting on a high wooden table. "
                    "The immense fruit building centered between the elderly Indonesian carver and the camera, filling the straight-on horizontal frame. "
                    "The architecture features a wide rectangular tiered foundation and utilizes the bright pink rind and green-tipped scales as distinct structural elements follow the fruit texture on the grand facade. "
                    "The massive central dome is flanked by four soaring symmetrical minarets at the corners, all intricately detailed with deep-recessed windows. "
                    "The long wooden table is heavily cluttered across the entire workspace only with realistic construction debris indicating colossal work: thousands of vibrant white flesh chunks filled with black seeds, large fragments of removed pink rind, and wet juice marks. No text or calligraphy. "
                    "Strictly no whole dragon fruits, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Nanas: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid pineapple, resting on a high wooden table. "
                    "The immense fruit building is centered between the elderly Indonesian carver and the camera, filling the straight-on horizontal frame. "
                    "The architecture features a wide rectangular tiered foundation, utilizing the golden-brown rugged spiked rind follow the fruit curve as a textured stone-like facade. "
                    "The massive central dome is flanked by four soaring symmetrical minarets at the corners, all carved with high-fidelity architectural details. No text or calligraphy. "
                    "The long wooden table is heavily cluttered across the workspace only with realistic construction debris indicating colossal work: thousands of succulent yellow pineapple flesh chunks, large fragments of removed spiked rind, and wet juice marks under natural golden hour daylight. "
                    "Strictly no whole pineapples, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Mangga: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid mango, resting on a high wooden table. "
                    "The immense fruit building is centered between the elderly Indonesian carver and the camera, filling the straight-on horizontal frame. "
                    "The architecture features a wide rectangular tiered foundation and a grand entrance portal carved from the smooth yellow-green rind follow the fruit shape. "
                    "The massive central dome is flanked by four soaring symmetrical minarets at the corners, with deep-recessed windows. No text or calligraphy. "
                    "The long wooden table is heavily cluttered across the workspace only with realistic construction debris indicating colossal work: thousands of vibrant orange mango flesh chunks, large fragments of removed smooth rind, curled shavings, and wet juice marks. "
                    "Strictly no whole mangoes, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Buah Naga: Ukiran Monumental": (
                    "A 1-meter-long architectural masterpiece of a mosque sculpted from a colossal dragon fruit, featuring full-surface deep engravings follow the fruit curve over the entire pink scaled rind. "
                    "Every millimeter of the pink skin and green-tipped scales is transformed into hyper-detailed geometric Islamic patterns and lace-like filigree, leaving no part untouched. "
                    "The structure features multiple tiered domes and soaring minarets showcasing extreme relief carvings, positioned precisely in front of the elderly Indonesian carver. No text or calligraphy. "
                    "The long wooden table is heavily littered only with raw fruit construction debris indicating monumental work: glistening white flesh chunks with black seeds, fine-carved pink rind fragments, and wet juice marks under natural golden hour daylight. "
                    "Strictly no whole dragon fruits, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Nanas: Ukiran Monumental": (
                    "A 1-meter-long architectural masterpiece of a mosque sculpted from a colossal pineapple, featuring full-surface deep engravings follow the fruit curve over the rugged spiked rind. "
                    "The entire golden-brown surface is transformed into hyper-detailed geometric relief and lace-like textures, integrating the natural thorns into the architectural design. No text or calligraphy. "
                    "The structure features a towering central dome and colossal minarets showcasing extreme multi-layered relief carvings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily littered only with raw fruit construction debris indicating monumental work: thousands of glistening yellow flesh chunks and fine-carved spiked rind shavings. "
                    "Strictly no whole pineapples, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Mangga: Ukiran Monumental": (
                    "A 1-meter-long architectural masterpiece of a mosque sculpted from a colossal mango, featuring full-surface deep engravings follow the fruit shape over the entire yellow-green rind. "
                    "Every millimeter of the smooth skin is transformed into hyper-detailed geometric Islamic patterns and complex relief carvings, leaving no part of the rind untouched. "
                    "The structure features a massive tiered dome and soaring minarets with high-fidelity architectural detail, positioned precisely in front of the elderly Indonesian carver. No text or calligraphy. "
                    "The long wooden table is heavily littered only with raw fruit construction debris indicating monumental work: thousands of glistening orange flesh chunks and fine-carved mango rind shavings under natural golden hour sunlight. "
                    "Strictly no whole mangoes, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Pepaya: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid papaya, resting on a high wooden table. "
                    "The immense fruit building centered between the elderly Indonesian carver and the camera, filling the straight-on horizontal frame. "
                    "The architecture features a wide rectangular tiered foundation and a grand entrance portal carved from the smooth green-orange rind follow the fruit shape. "
                    "The massive central dome is flanked by four soaring symmetrical minarets at the corners, with deep-recessed windows. No text or calligraphy. "
                    "The long wooden table is heavily cluttered across the entire workspace only with realistic construction debris indicating colossal work: thousands of vibrant orange papaya flesh chunks, scattered black seeds, large fragments of removed smooth rind, and wet juice marks under natural golden hour daylight. "
                    "Strictly no whole papayas, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Salak: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid snake fruit (salak), resting on a high wooden table. "
                    "The dark brown scaly rind acting as a natural textured stone facade follow the fruit curve along the 1-meter width, centered between the character and the camera. "
                    "The architecture features a grand central dome and soaring minarets, all intricately detailed to show the overlap of natural scales integrated into the design. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw fruit construction debris indicating colossal work: thousands of firm ivory-white flesh chunks, large fragments of removed dark brown scaly skin, and wet marks. "
                    "Strictly no whole fruits, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pisang: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid banana, resting on a high wooden table. "
                    "The diorama spans 1 meter wide, featuring a unique organic architectural layout carved from the smooth yellow rind follow the fruit curve, centered between the character and the camera. "
                    "The structure features a series of majestic domes and slender minarets, with the wide foundation showing multi-layered architectural details. No text or calligraphy. "
                    "The long wooden table is heavily cluttered across the entire workspace only with raw fruit debris indicating colossal work: thousands of soft pale-yellow banana flesh chunks, large fragments of removed yellow peel, and glistening moist marks under natural golden hour daylight. "
                    "Strictly no whole bananas, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pepaya: Ukiran Monumental": (
                    "A 1-meter-long architectural masterpiece of a mosque sculpted from a colossal papaya, featuring full-surface deep engravings follow the fruit shape over the entire smooth green-orange rind. "
                    "Every millimeter of the skin is transformed into hyper-detailed geometric Islamic patterns and complex relief carvings, leaving no part of the rind untouched. "
                    "The structure features multiple tiered domes and soaring minarets showcasing extreme relief carvings, positioned precisely in front of the elderly Indonesian carver. No text or calligraphy. "
                    "The long wooden table is heavily littered only with raw fruit construction debris indicating monumental work: thousands of glistening orange flesh chunks, scattered black seeds, and fine-carved rind shavings under natural golden hour sunlight. "
                    "Strictly no whole papayas, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Salak: Ukiran Monumental": (
                    "A 1-meter-long architectural masterpiece of a mosque sculpted from a colossal snake fruit (salak), featuring full-surface deep engravings follow the fruit curve over the dark brown scaly rind. "
                    "Every single scale on the skin is meticulously carved into intricate decorative patterns, creating a complex multi-layered architectural facade along the 1-meter width. "
                    "The structure features a tiered central dome and colossal minarets showcasing extreme relief carvings, positioned precisely in front of the elderly Indonesian carver. No text or calligraphy. "
                    "The long wooden table is heavily littered only with raw fruit construction debris indicating monumental work: firm ivory-white flesh chunks and fine-carved dark scaly skin shavings. "
                    "Strictly no whole fruits, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Pisang: Ukiran Monumental": (
                    "A 1-meter-long architectural masterpiece of a mosque sculpted from a colossal banana, featuring full-surface deep engravings follow the fruit curve over the entire yellow peel. "
                    "The smooth yellow surface is completely transformed into hyper-detailed geometric relief and lace-like textures, leaving no part of the peel untouched. No text or calligraphy. "
                    "The structure features multiple tiered domes and soaring minarets with high-relief engravings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily cluttered only with raw fruit debris indicating monumental work: thousands of pale-yellow flesh fragments, fine-edged yellow peel shavings, and moist marks under natural daylight. "
                    "Strictly no whole bananas, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Rambutan: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid rambutan fruit, resting on a high wooden table. "
                    "The architecture spans 1 meter wide, centered between the elderly Indonesian carver and the camera, utilizing the bright red skin and soft organic hair-like spines follow the fruit texture as a unique decorative facade. "
                    "The structure features a wide rectangular foundation and a grand central dome with soaring minarets, all intricately carved to integrate the fruit's natural texture into the walls. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw fruit construction debris indicating colossal work: thousands of translucent-white succulent flesh chunks, large fragments of removed hairy red rind, and wet juice marks under natural golden hour daylight. "
                    "Strictly no whole fruits, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Alpukat: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid avocado, resting on a high wooden table. "
                    "The diorama fills the straight-on horizontal frame centered between the character and the camera, with the dark green pebbled rind acting as a natural textured stone facade follow the fruit curve along the 1-meter width. "
                    "The architecture features a grand arched entrance portal with thick pillars and a massive central dome flanked by soarimg minarets. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw fruit construction debris indicating colossal work: thousands of glistening creamy light-green and yellow flesh chunks, large fragments of removed rough dark rind, and moist marks under natural golden hour daylight. "
                    "Strictly no whole avocados, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Labu: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid pumpkin, resting on a high wooden table. "
                    "The immense fruit building centered between the elderly Indonesian carver and the camera, filling the straight-on horizontal frame. "
                    "The architecture features a wide rectangular tiered foundation and a grand entrance portal carved from the thick orange rind follow the natural vertical ridges. "
                    "The massive central dome is flanked by multiple high minarets, all intricately detailed with deep-recessed windows. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with realistic construction debris: thousands of dense orange pumpkin flesh chunks, large fragments of removed thick rind, and wet juice marks with seeds under natural golden hour daylight. "
                    "Strictly no whole pumpkins, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Rambutan: Ukiran Monumental": (
                    "A 1-meter-long architectural masterpiece of a mosque sculpted from a colossal rambutan, featuring full-surface deep engravings follow the fruit curve over the red hairy rind. "
                    "Every millimeter of the red skin and every organic spine is meticulously carved into intricate decorative patterns, creating a complex multi-layered architectural facade. "
                    "The structure features a tiered central dome and colossal minarets showcasing extreme relief carvings, positioned precisely in front of the elderly Indonesian carver. No text or calligraphy. "
                    "The long wooden table is heavily littered only with raw fruit construction debris: translucent-white flesh chunks and fine-carved hairy rind shavings wet with juice under natural golden hour daylight. "
                    "Strictly no whole fruits, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Alpukat: Ukiran Monumental": (
                    "A 1-meter-long architectural masterpiece of a mosque sculpted from a colossal avocado, featuring full-surface deep engravings follow the fruit curve over the rough pebbled dark green rind. "
                    "The entire textured surface is transformed into hyper-detailed geometric relief and lace-like patterns, leaving no part of the skin untouched. No text or calligraphy. "
                    "The structure features multiple tiered domes and soaring minarets with high-relief engravings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily cluttered only with raw fruit debris: creamy light-green flesh fragments, fine-edged rough rind shavings, and moist marks under natural golden hour daylight. "
                    "Strictly no whole avocados, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Labu: Ukiran Monumental": (
                    "A 1-meter-long architectural masterpiece of a mosque sculpted from a colossal pumpkin, featuring full-surface deep engravings follow the fruit shape over the entire thick orange rind. "
                    "Every millimeter of the smooth orange skin is transformed into hyper-detailed geometric Islamic patterns and complex relief carvings, leaving no part untouched. No text or calligraphy. "
                    "The structure features multiple tiered domes and soaring minarets with high-relief engravings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily cluttered only with raw fruit debris: thousands of dense orange flesh fragments, fine-edged rind shavings, pumpkin seeds, and wet juice marks under natural golden hour sunlight. "
                    "Strictly no whole pumpkins, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Anggur: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid grape material, resting on a high wooden table. "
                    "The diorama fills the horizontal frame centered between the character and the camera, featuring a wide facade carved from the smooth purple-black skin follow the fruit shape. "
                    "The architecture includes a grand central dome and soaring minarets, all intricately detailed with deep-recessed windows. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw fruit construction debris: thousands of translucent-green succulent flesh chunks, large fragments of removed smooth purple skin, and wet juice marks under natural golden hour daylight. "
                    "Strictly no whole grapes, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Strawberry: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid strawberry, resting on a high wooden table. "
                    "The architecture spans 1 meter wide centered between the character and the camera, utilizing the bright red pitted skin follow the fruit shape as a unique textured facade. "
                    "The structure features a wide tiered foundation and a grand central dome with soaring minarets, all intricately carved to integrate the tiny seeds into the architectural patterns. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw fruit construction debris: thousands of pale-red and white succulent flesh chunks, large fragments of removed red seeded skin, and wet juice marks under natural golden hour daylight. "
                    "Strictly no whole strawberries, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Jeruk: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid orange, resting on a high wooden table. "
                    "The diorama spans 1 meter wide, featuring a massive horizontal layout carved from the porous orange rind follow the fruit curve, centered between the elderly Indonesian carver and the camera. "
                    "The architecture features a towering central dome and multiple high minarets, with the wide tiered foundation showing deep-recessed windows. No text or calligraphy. "
                    "The long wooden table is heavily cluttered across the entire workspace only with realistic construction debris indicating colossal work: thousands of vibrant orange juice vesicles, large fragments of removed porous rind, and wet juice marks under natural golden hour daylight. "
                    "Strictly no whole oranges, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Durian: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid durian, resting on a high wooden table. "
                    "The diorama spans 1 meter wide, utilizing the rugged golden-brown spiked rind follow the fruit shape as a massive, aggressive stone-like facade, centered between the character and the camera. "
                    "The architecture features a towering central dome and multiple high minarets, with the natural sharp thorns integrated into the geometric pillars and walls. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw fruit construction debris: thousands of creamy-yellow custard-like flesh chunks, large fragments of removed thick spiked rind, and wet marks under natural golden hour daylight. "
                    "Strictly no whole durians, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Anggur: Ukiran Monumental": (
                    "An architectural masterpiece of a mosque sculpted from a colossal giant grape, featuring full-surface deep engravings follow the fruit curve over the smooth purple skin. "
                    "Every millimeter of the surface is transformed into hyper-detailed geometric Islamic patterns and lace-like filigree, leaving no part of the skin untouched. No text or calligraphy. "
                    "The structure features multiple tiered domes and soaring minarets showcasing extreme relief carvings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily littered only with raw fruit construction debris: translucent-green flesh chunks and fine-carved purple skin shavings wet with juice marks under natural golden hour daylight. "
                    "Strictly no whole grapes, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Strawberry: Ukiran Monumental": (
                    "An architectural masterpiece of a mosque sculpted from a colossal strawberry, featuring full-surface deep engravings follow the fruit shape over the red seeded skin. "
                    "The entire red surface and the tiny seeds are meticulously transformed into hyper-detailed geometric relief and lace-like patterns, leaving no part untouched. No text or calligraphy. "
                    "The structure features multiple tiered domes and soaring minarets with high-relief engravings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily cluttered only with raw fruit debris indicating monumental work: pale-red and white flesh fragments, fine-edged red skin shavings, and moist marks under natural golden hour daylight. "
                    "Strictly no whole strawberries, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Jeruk: Ukiran Monumental": (
                    "An architectural masterpiece of a mosque sculpted from a colossal orange, featuring full-surface deep engravings follow the fruit curve over the entire porous orange rind. "
                    "Every millimeter of the textured skin is transformed into hyper-detailed geometric Islamic patterns and complex relief carvings, leaving no part untouched. No text or calligraphy. "
                    "The structure features multiple tiered domes and soaring minarets with high-relief engravings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily cluttered only with raw fruit debris indicating monumental work: thousands of orange pulps, fine-edged rind shavings, and wet juice marks under natural golden hour daylight. "
                    "Strictly no whole oranges, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Durian: Ukiran Monumental": (
                    "An architectural masterpiece of a mosque sculpted from a colossal durian, featuring full-surface deep engravings follow the fruit curve over the thick golden-brown spiked rind. "
                    "Every millimeter of the rugged skin and every sharp thorn is meticulously transformed into hyper-detailed geometric relief and complex architectural patterns. No text or calligraphy. "
                    "The structure features multiple tiered domes and soaring minarets showcasing extreme relief carvings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily cluttered only with raw fruit construction debris: thousands of creamy-yellow flesh fragments and fine-carved thick spiked rind shavings wet with juice marks. "
                    "Strictly no whole durians, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Manggis: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid mangosteen, resting on a high wooden table. "
                    "The diorama spans 1 meter wide centered between the elderly Indonesian carver and the camera, featuring a wide facade carved from the thick, smooth purple-black rind follow the fruit shape. "
                    "The architecture includes a massive central dome and soaring symmetrical minarets, all intricately detailed with deep-recessed windows. No text or calligraphy. "
                    "The long wooden table is heavily cluttered across the workspace only with realistic construction debris indicating colossal work: thousands of pearly-white succulent flesh chunks, large fragments of removed thick purple-black rind, and wet juice marks under natural golden hour daylight. "
                    "Strictly no whole mangosteens, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Apel: Diorama Monumental": (
                    "A monumental, complete grand mosque building with full architectural structural integrity, sculpted entirely from a colossal solid red apple, resting on a high wooden table. "
                    "The diorama spans 1 meter wide centered between the elderly Indonesian carver and the camera, featuring a majestic horizontal layout carved from the smooth, glossy red rind follow the fruit curve. "
                    "The architecture features a towering central dome and multiple high minarets, with the wide tiered foundation showing deep-recessed windows. No text or calligraphy. "
                    "The long wooden table is heavily cluttered across the workspace only with realistic construction debris indicating colossal work: thousands of pale-white crisp apple flesh chunks, large fragments of removed glossy red peel, and wet juice marks under natural golden hour daylight. "
                    "Strictly no whole apples, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Kiwi: Ukiran Monumental": (
                    "An architectural masterpiece of a mosque sculpted from a colossal kiwi fruit, featuring full-surface deep engravings follow the fruit curve over the fuzzy brown skin. "
                    "The entire textured surface is transformed into hyper-detailed geometric relief and complex architectural patterns. No text or calligraphy. "
                    "The structure features multiple tiered domes and soaring minarets showcasing extreme relief carvings, positioned precisely in front of the elderly Indonesian carver. "
                    "The long wooden table is heavily cluttered only with raw fruit debris: thousands of green flesh fragments with black seeds and fine-carved fuzzy skin shavings under natural golden hour daylight. "
                    "Strictly no whole kiwis, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Biji Jagung: Diorama Monumental": (
                    "A monumental, complete grand mosque building constructed entirely from millions of solid yellow corn kernels, positioned precisely in front of the elderly Indonesian carver. "
                    "The structure spans 1 meter wide, with the kernels tightly packed to form a massive golden-yellow mosaic facade. "
                    "The architecture features a wide rectangular foundation and a grand central dome flanked by four soaring minarets, showing a dense organic texture. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw material debris: thousands of loose yellow corn kernels and small fragments of broken maize. "
                    "Strictly no whole corn cobs, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw material debris under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Biji Kacang Ijo: Diorama Monumental": (
                    "A monumental, complete grand mosque building constructed entirely from millions of small solid green mung beans, positioned precisely in front of the elderly Indonesian carver. "
                    "The diorama fills the horizontal frame, featuring a wide facade with a dense green matte texture along the 1-meter span. "
                    "The architecture includes a massive central dome and soaring symmetrical minarets, all built from tightly packed green beans. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw material debris: thousands of loose green mung beans scattered across the workspace. "
                    "Strictly no whole bean pods, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw bean material debris under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Cabe: Diorama Monumental": (
                    "A monumental, complete grand mosque building sculpted entirely from a colossal solid mass of red chili peppers, positioned precisely in front of the elderly Indonesian carver. "
                    "The architecture spans 1 meter wide, utilizing the bright waxy red skin follow the fruit shape as a vibrant decorative facade. "
                    "The structure features a towering central dome and multiple high minarets with natural curves integrated into the pillars. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw fruit construction debris: thousands of sliced red chili pieces, scattered white seeds, and wet juice marks. "
                    "Strictly no whole intact chilies, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Tomat: Diorama Monumental": (
                    "A monumental, complete grand mosque building sculpted entirely from a colossal solid tomato, positioned precisely in front of the elderly Indonesian carver. "
                    "The diorama spans 1 meter wide, featuring a majestic horizontal layout carved from the smooth, glossy red tomato skin follow the fruit shape. "
                    "The architecture features a towering central dome and multiple high minarets, with the wide tiered foundation showing deep-recessed windows. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw fruit debris: thousands of vibrant red tomato flesh chunks, clusters of watery seeds, and wet juice marks. "
                    "Strictly no whole tomatoes, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris under natural golden hour daylight. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),
                
                "Biji Kedelai Hitam: Diorama Monumental": (
                    "A monumental, complete grand mosque building constructed entirely from millions of solid black soybean grains, positioned precisely in front of the elderly Indonesian carver. "
                    "The structure spans 1 meter wide, with the small black beans tightly packed to form a massive, deep-black glossy mosaic facade. "
                    "The architecture features a wide rectangular tiered foundation and a grand central dome flanked by four soaring minarets, all showing a dense organic black texture. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw material debris: thousands of loose black soybeans scattered under natural golden hour daylight. "
                    "Strictly no whole pods, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
                ),

                "Biji Kuaci: Diorama Monumental": (
                    "A monumental, complete grand mosque building constructed entirely from millions of sunflower seeds (kuaci), positioned precisely in front of the elderly Indonesian carver. "
                    "The diorama fills the horizontal frame, featuring a wide facade with the natural black-and-white striped patterns of the seeds along the 1-meter span. "
                    "The architecture includes a massive central dome and soaring symmetrical minarets, all built from tightly packed striped seeds. No text or calligraphy. "
                    "The long wooden table is heavily cluttered only with raw material debris: thousands of loose sunflower seeds and broken seed shells scattered under natural golden hour daylight. "
                    "Strictly no whole sunflowers, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw material debris. No internal lighting Mechanisms. "
                    "The structure is positioned precisely in the absolute center foreground, situated directly between the camera lens and the character's body in a perfectly straight-on, symmetrical composition. "
                    "The structure is fixed firmly on the central wooden table at chest-level, physically obscuring the character's midsection and torso to create a dominating presence and intimate close-up framing with no lateral gap."
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
        # --- 4. MASTER AUDIO & SOULFUL EXPRESSION (ANTI-ASMA & HIGH-VULNERABILITY) ---
        MASTER_AUDIO_STYLE = {
            "Logat": [
                "Natural Village-Authentic: A raw, unpolished voice with a flat, honest intonation. It carries a rhythmic 'broken' cadence, sounding deeply sincere and unpretentious with a texture that is slightly dry and dusty, lacking any urban polish.",
                "Old Javanese Phonetic: Slow and deliberate with a heavy, vibrating 'dh' and 'th' percussion. The tone is deeply humble, featuring a low-register chest voice that sounds like a calm, rhythmic hum.",
                "Soft Sundanese Lilt: A melodic, undulating rhythm (mendayu) with a gentle rising and falling pitch. The voice is airy and breathy, characterized by a smooth, high-frequency flow with no harsh edges.",
                "Coastal Melayu Cadence: Quick-paced and rhythmic with a dry, gravelly texture. The intonation is punchy and direct, sounding like a weathered voice shaped by salt air and open spaces.",
                "Village-Common 'Kering' Voice: A thin, cracked, and slightly shaky (gemetar) voice. It carries the texture of a dry throat, with high-register raspiness and frequent breathy pauses between phrases.",
                "The Serene Matriarch: Extremely slow tempo, almost a whisper. The voice is calm, stable, and deeply reverent, with soft guttural friction in the throat that suggests a lifetime of silent prayer."
            ],
            "Mood": [
                "Sedih & Sayu (Quiet Vulnerability - Steady gaze, eyes heavy with deep emotion)",
                "Tenang & Bengong (Pensive Stillness - Calm facial expression, long natural pauses)",
                "Damai Sejahtera (Graceful Serenity - Serene and peaceful look, slow breathing)",
                "Tulus Ikhlas (Humble Devotion - Gentle and sincere facial expression)",
                "Tegar & Bijak (Stoic Calmness - A steady, wise face reflecting years of memories)",
                "Fokus Khusyuk (Sacred Focus - Deeply focused expression, absolute sincerity)",
                "Penuh Harapan (Peaceful Hope - A calm, hopeful look in the eyes)"
            ],
            "Physical Action": [
                "Menyentuh kubah dengan lembut sambil sesekali menatap kamera (Gently touching the mosque's dome, occasionally shifting gaze to look warmly at the camera)",
                "Menatap tajam detail lalu mendongak tersenyum (Holding a focused gaze on the details, then briefly looking up at the camera with a subtle smile)",
                "Mata berkaca-kaca menatap kamera dengan tulus (Looking directly at the camera with glistening eyes and a deeply soulful, hopeful expression)",
                "Tangan bersedekap di pangkuan menatap penuh doa (Hands resting on the lap in a prayerful pose, looking at the camera with silent devotion)",
                "Tersenyum tipis ke arah kamera sambil memegang miniatur (A peaceful smile while looking directly at the camera, hands gently supporting the model)",
                "Mengusap debu lalu menatap puas ke kamera (Gently wiping a speck of dust, then looking at the camera with a satisfied and contented expression)",
                "Memejamkan mata bersyukur lalu membukanya menatap kamera (Closing eyes in gratitude, then opening them to look warmly at the camera)",
                "Menunduk khusyuk merakit sesekali melirik kamera (Looking down with intense focus on the craft, occasionally glancing at the camera with a confident smile)"
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
                # --- LANGSUNG KE DETAIL OBJEK ---
                st.markdown('<p class="small-label">DETAIL OBJEK / KARYA</p>', unsafe_allow_html=True)
                
                # List objek otomatis ambil dari 'modus_konten' yang dipilih di paling atas UI
                objek_list = list(MASTER_KONTEN_ALL[modus_konten].keys())
                
                # User tinggal milih detailnya (Merah Klasik, Hijau Ukir, dll)
                pilihan_objek = st.selectbox("Select Detail", objek_list, label_visibility="collapsed")
    
                # Ambil deskripsi teknisnya untuk dikirim ke Grok
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
                pilih_logat = st.selectbox("Pilih Logat", MASTER_AUDIO_STYLE["Logat"])
                pilih_mood = st.selectbox("Pilih Mood", MASTER_AUDIO_STYLE["Mood"])
                pilih_aksi = st.selectbox("Pilih Gerakan Tubuh", MASTER_AUDIO_STYLE["Physical Action"])

            st.write("")
            btn_gen = st.button("🚀 GENERATE VIDEO PROMPT", type="primary", use_container_width=True, key="btn_generate_video")

        # --- LOGIC GENERATOR (V26: THE HIGH-TABLE SYNC) ---
        if btn_gen:
            # 1. UBAH DARI LESEHAN KE POSISI MEJA TINGGI
            # Ini kunci agar objek sejajar dengan dada, bukan di kaki.
            posisi_nenek = "sitting behind a high rustic wooden table (meja tinggi)"
            
            scene_context = (
                f"LIGHTING: Very soft 5 PM golden-hour side lighting creating a delicate warm rim light. "
                f"COMPOSITION: 50/50 balanced frame share between the character and the miniature at chest-height. "
                f"MOTION: Extremely subtle, almost imperceptible slow zoom-in toward the face at 0.1x speed. "
                f"FOCUS: Razor-sharp on the character's weathered face and the intricate fruit-carved mosque."
            )

            # 3. AMBIL DATA MASTER (Tetap)
            env_detail = MASTER_GRANDMA_SETTING.get(pilihan_set, "Natural outdoor setting.")
            soul_desc = MASTER_FAMILY_SOUL.get(pilihan_user, "An Indonesian person.")
            
            # Ambil Pakaian dari Master Wardrobe lo
            wardrobe_dict = MASTER_FAMILY_WARDROBE.get(char_key, {})
            baju_desc = wardrobe_dict.get(baju_pilihan, "Simple modest clothes.")

            # --- 4. THE MAGIC MAGIC GENDER & WARDROBE LOCK (INI RAHASIANYA DIAN!) ---
            ANATOMY_LOCK = "STRICTLY TWO HUMAN HANDS, five fingers each. No ghost limbs."
            
            # --- CEK GENDER SECARA OTOMATIS BERDASARKAN KARAKTER ---
            # Logic ini nahan AI biar nggak nambahin jenggot ke Nenek atau Hijab ke Kakek.
            is_perempuan = any(x in pilihan_user.lower() for x in ["nenek", "ibu", "aminah", "siti", "marsi", "ponirah", "juminah", "sikem", "dulah", "sartini", "tinah", "wati"])
            
            if is_perempuan:
                gender_lock = (
                    "PHYSICAL MANDATORY: An elderly Indonesian grandmother (Nenek). "
                    "FACE LOCK: Strictly 100% hairless face, NO beard, NO mustache, NO facial hair. "
                    "SKIN TEXTURE: Hyper-realistic deeply wrinkled skin, sagging textures, liver spots, and aged sun-damage. NO smoothing, NO beauty filters, 100% RAW skin. "
                    "GENDER WARDROBE: Wearing a traditional Indonesian Hijab (Kerudung) that fully covers the hair and neck. Outfit: Simple village woman's house dress (Daster) or a modest Kebaya."
                )
            else:
                gender_lock = (
                    "PHYSICAL MANDATORY: An elderly Indonesian grandfather (Kakek). "
                    "FACE LOCK: Weathered masculine face, clean-shaven or with very thin, sparse natural stubble. NO hijab, NO female garments. "
                    "SKIN TEXTURE: Deeply wrinkled, leathery, sun-parched skin with prominent veins on temples and hands. "
                    "GENDER WARDROBE: Wearing a classic Indonesian Black Kopiah (Peci) on the head. Outfit: A simple Koko shirt or a plain, worn-out daily village shirt."
                )

            # --- 5. FILTER PEMBERSIH (LOGIKA SETELAH TITIK DUA) ---
            def bersihkan_teks(teks):
                # Kita cari tanda titik dua paling kanan
                if ':' in teks:
                    # Ambil semua teks di sebelah kanan titik dua paling akhir
                    return teks.split(':')[-1].strip()
                # Kalau gak ada titik dua, baru cari di dalam kurung (buat jaga-jaga)
                elif '(' in teks and ')' in teks:
                    return teks.split('(')[1].split(')')[0].strip()
                return teks.strip()

            aksi_final = bersihkan_teks(pilih_aksi)
            mood_final = bersihkan_teks(pilih_mood)
            logat_final = pilih_logat.split(':')[-1].strip()
                

            # --- FINAL ASSEMBLY (V25: THE CHEST-LEVEL MASTERY) ---
            final_ai_prompt = (
                # 1. Fondasi Gaya (Pindahan dari GLOBAL_STYLE)
                f"CINEMATIC STYLE: Cinematic photography, shot on 35mm lens, f/2.8 aperture. "
                f"High-end documentary aesthetic, authentic rural Indonesian color grading. "
                f"Hyper-realistic textures, 8k resolution, highly detailed skin pores and intricate fruit fibers. \n\n"

                # 2. Scene Context (Lighting & Motion)
                f"SCENE CONTEXT: {scene_context} \n\n" 
            
                # 3. Identitas, Wardrobe, & Anatomy
                f"CHARACTER IDENTITY: {soul_desc}. {gender_lock} \n"
                f"ANATOMY LOCK: {ANATOMY_LOCK} \n"
                f"WARDROBE: {baju_desc}. \n"
            
                # 4. Environment (Kunci Meja Tinggi)
                f"ENVIRONMENT: {env_detail}. A high rustic wooden table is positioned directly in front of the character's chest. \n\n"
            
                # 5. Performance & Lip-Sync
                f"PERFORMANCE & INTERACTION: {aksi_final}. \n"
                f"MOOD & EMOTION: {mood_final}. Strictly focus on a soulful, humble, and pleading connection with the viewer. "
                f"MANDATORY: Mouth, jaw, and throat must move in perfect lip-sync with the dialogue. \n\n"
            
                # 6. Detail Objek
                f"THE MASTERPIECE: {deskripsi_teknis}. The 60cm fruit-carved mosque sits on the table at chest-height. \n\n"
            
                # 7. Audio & Dialog
                f"DIALOG CONTEXT: '{user_dialog}' delivered with {logat_final} accent. \n\n"
                f"AUDIO ENFORCEMENT: Voice must be extremely aged and frail but MAINTAIN clear articulation and perfect lip-sync. \n\n"
            
                # 8. Technical Specs Final (Kunci Framing)
                f"TECHNICAL SPEC: Eye-level Tight Medium-Shot (Bust-up). Both hands visible. Soft natural bokeh background. \n\n"
            
                # 9. Negative Prompt
                f"NEGATIVE PROMPT: knife, blade, tools on table, blood, smiling, laughing, teeth, "
                f"beard on woman, mustache on woman, wide shot, full body, watermark, text, caption."
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
