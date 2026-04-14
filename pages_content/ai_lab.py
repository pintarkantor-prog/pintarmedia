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
            "🕌 Miniatur Masjid": {
                "Semangka Tipe Meja (Proses)": (
                    "A substantial 60cm mosque model made of fresh watermelon, placed on a high rustic wooden table directly in front of the character's chest. "
                    "The dome is carved from ruby-red flesh, while the body is dark-green rind. "
                    "Positioned at chest-level so the character can work on it comfortably. "
                    "Natural daylight, no LEDs, no artificial glow."
                ),
                "Semangka Tipe Jadi (Display)": (
                    "A finished 60cm watermelon mosque masterpiece, resting on a high wooden table at chest-level. "
                    "The character's hands are resting on the table beside the mosque. "
                    "The composition ensures the mosque is tall enough to be in the same frame as the character's torso and head."
                ),
                "Buah Semangka Tipe 3": (
                    "An elegant 60cm miniature mosque precisely carved from the white inner layer of a watermelon rind, resting in a lap (dipangku). "
                    "The structure looks like carved organic ivory. "
                    "Features very thin, tall white minarets with hand-carved lattice geometric holes, standing prominently. "
                    "The main dome is a smooth spherical piece of white rind. "
                    "A character's hands are supporting the base gently. "
                    "No internal lights, no LEDs, no glowing effects, natural daylight."
                ),
                "Buah Semangka Tipe 4": (
                    "A unique 60cm mosque made of carved red watermelon flesh, held by a person's hands. "
                    "The red exterior walls are decorated with thousands of real, organic black watermelon seeds embedded manually in intricate geometric patterns. "
                    "The minarets are tall red columns with spiral patterns made of black seeds. "
                    "A character's hands are holding the base of the mosque firmly. "
                    "No artificial lights. Natural organic daylight highlighting the high contrast between red fruit and black seeds."
                ),
                "Buah Semangka Tipe 5": (
                    "A substantial 60cm architectural mosque model held in a lap (dipangku). "
                    "The structure shows clear definition with layered watermelon anatomy: dark green striped rind base, "
                    "white rind layer mid-section, and vibrant red flesh main domes. "
                    "Features multiple small green minarets standing prominently at the corners. "
                    "A character's hands are holding the layered base. "
                    "No lighting, no electronics, strictly fruit textures in natural daylight."
                ),
                "Buah Semangka Tipe 6": (
                    "A monumental 1-meter mosque diorama built with architectural precision from watermelon anatomy. "
                    "The walls are composed of millions of pressurized, ruby-red watermelon cubes with a glistening, high-moisture finish. "
                    "The main dome is a sphere of translucent, polished watermelon flesh, glowing with a soft, internal 'Ember Amber' LED light that reveals the organic cellular structure. "
                    "Inside the dome, thousands of black seeds are meticulously arranged in sacred geometric patterns, silhouetted against the warm internal glow. "
                    "Minarets of dark-green striped rind are subtly traced with thin, steady warm-white fiber-optic lines, avoiding aggressive flickering. "
                    "The lighting is cinematic and moody, seeping through the red fruit like a glowing hearth."
                ),
                "Buah Pepaya Tipe 1": (
                    "A 60cm mosque model carved entirely from a ripe papaya, resting in a person's lap (dipangku). "
                    "The main dome is a smooth, vibrant orange sphere carved from the papaya's internal flesh. "
                    "The pillars are made of the smooth yellow-green outer skin. "
                    "Features four clearly defined minarets standing tall, carved from firm papaya sections. "
                    "No internal lights, no LEDs. Natural daylight on the matte orange fruit texture."
                ),
                "Buah Pepaya Tipe 2": (
                    "A sturdy 60cm mosque miniature made of 100% green unripened papaya skin, lifted by two hands. "
                    "The exterior is all smooth green skin, chiseled into blocks. "
                    "Features two thick, prominent minarets flanking the entrance made of solid green papaya. "
                    "The orange flesh is only visible through small arched windows. "
                    "No electronics, no lighting, no LEDs. Focus on the smooth green organic surface."
                ),
                "Buah Pepaya Tipe 3": (
                    "A unique 60cm mosque carved from orange papaya, held in a character's hands. "
                    "The walls are decorated with clusters of real black, wet papaya seeds arranged in geometric patterns. "
                    "The minarets are tall orange towers with black seed rings at the top. "
                    "No lights, no glowing effects. High contrast between the orange flesh and the shiny black seeds."
                ),
                "Buah Pepaya Tipe 4": (
                    "A beautiful 60cm mosque model carved from a fully ripe yellow-skinned papaya, resting in a lap. "
                    "The architecture is simple and clean, using the bright yellow outer skin for the domes. "
                    "Features tall, slender minarets standing prominently at the corners. "
                    "Character's hands are holding the base of the fruit mosque. "
                    "No LEDs, no artificial glow. Natural sunlight highlighting the bright yellow fruit."
                ),
                "Buah Pepaya Tipe 5": (
                    "A 60cm architectural mosque model held securely by hands, showing layered papaya anatomy. "
                    "The base is green skin, the walls are bright orange flesh, and the minarets are decorated with black seeds. "
                    "All components are 100% papaya. "
                    "Features multiple small minarets standing prominently. "
                    "No lighting, no electronics. Pure organic textures in natural light."
                ),
                "Buah Naga Tipe 1": (
                    "A dominant 60cm mosque model constructed from whole vibrant pink dragon fruit skins, resting in a person's lap (dipangku). "
                    "The structure is defined by the striking pink leather-like skin with the iconic green scaled 'fins' prominently featured along the walls and domes. "
                    "Features four tall minarets made of stacked pink dragon fruit rind sections. "
                    "A character's hands are holding the detailed scaled base of the mosque. "
                    "No internal lights, no LEDs, no artificial glow, only natural daylight on the intense pink fruit skin."
                ),
                "Buah Naga Tipe 2": (
                    "A unique 60cm mosque carved precisely from the internal white flesh of a dragon fruit, held by a character's hands. "
                    "The walls and domes have a speckled black-and-white mosaic pattern from thousands of tiny black seeds embedded in the white flesh. "
                    "Features two prominent, tall white minarets with intricate geometric fretwork cutouts. "
                    "The vibrant pink skin is only visible as thin trim at the bottom edges. "
                    "No electronics, no lighting, no LEDs. Pure organic fruit texture in natural light."
                ),
                "Buah Naga Tipe 3": (
                    "A striking 60cm mosque model resting in a lap, made from deep magenta (red-fleshed) dragon fruit. "
                    "The main dome is a smooth, vibrant deep-purple-pink sphere carved from the flesh, showing the embedded black seed textures. "
                    "The base is made of the bright pink skin with green scale details. "
                    "Features multiple small green minarets standing prominently at the corners, carved from the rind scales. "
                    "No lights, no glowing effects. High color contrast, natural daylight."
                ),
                "Buah Naga Tipe 4": (
                    "A substantial 60cm architectural mosque model held in a lap (dipangku). "
                    "The exterior is 100% composed of deeply layered, scaled dragon fruit skin, looking like a robust pink fortress. "
                    "Features two massive, prominent pink minarets flanking the main entrance, made of thick stacked scales. "
                    "No flesh is visible; strictly focus on the detailed pink and green scaled textures and heavy structure. "
                    "No electronics, no lighting, no LEDs. Macro shot, matte organic finish."
                ),
                "Buah Naga Tipe 5": (
                    "A 60cm detailed mosque model held securely by hands, showing layered dragon fruit anatomy. "
                    "The base is thick pink skin, the walls are patterned white seed-flesh, and the main domes are carved deep magenta flesh. "
                    "Every component is 100% dragon fruit. Features multiple small minarets standing prominently at the corners. "
                    "No lighting, no electronics, no LEDs, no glowing parts. Pure organic textures, natural daylight, macro photography."
                ),
                "Buah Naga Tipe 6": (
                    "A monumental 1-meter mosque object built from the vibrant anatomy of Dragonfruit. "
                    "The walls are covered in overlapping magenta rind scales with lime-green tips, creating a futuristic 'organic armor' look. "
                    "The colossal main dome is a sphere of translucent white dragonfruit flesh, embedded with millions of tiny black seeds that create a natural 'stardust' texture. "
                    "Inside, a 'Cyber-Violet' internal LED glow pulses slowly, making the seeds look like a floating galaxy trapped in ice. "
                    "Minarets are built from twisted magenta rinds, illuminated with thin, steady electric-pink fiber-optic lines that accentuate the sharp scales."
                ),
                "Buah Labu Tipe 1": (
                    "A 60cm mosque model carved from a large orange pumpkin, resting in a person's lap (dipangku). "
                    "The entire structure is made of the bright orange outer skin. "
                    "Features a large central dome and four tall minarets standing prominently, carved from thick pumpkin sections. "
                    "The character's hands are holding the base of the orange pumpkin mosque. "
                    "No internal lights, no LEDs, no artificial glow. Natural daylight on the smooth orange skin."
                ),
                "Buah Labu Tipe 2": (
                    "A substantial 60cm mosque miniature carved from the dense internal orange flesh of a butternut squash, held by hands. "
                    "The walls have a rich, matte, and slightly fibrous orange texture. "
                    "Features two tall, sturdy minarets that are clearly defined and standing tall. "
                    "The outer pale-yellow skin is only visible as small decorative accents at the base. "
                    "No electronics, no lighting, no LEDs. Pure organic fruit craftsmanship in natural light."
                ),
                "Buah Labu Tipe 3": (
                    "A sturdy 60cm mosque model made of 100% green Kabocha pumpkin rind, lifted by two hands. "
                    "The exterior is dark green with rough, bumpy textures like ancient stone. "
                    "Features prominent green minarets flanking the entrance, looking like strong towers. "
                    "A character's hands are gripping the sides of the green pumpkin mosque firmly. "
                    "No lights, no glowing effects. Focus on the rugged green organic texture."
                ),
                "Buah Labu Tipe 4": (
                    "A unique 60cm mosque carved from a pumpkin, resting in a lap. "
                    "The arched windows and doors are decorated with real, dried white pumpkin seeds arranged in patterns. "
                    "The minarets are tall orange towers with white seed rings at the top. "
                    "The character's hands are supporting the base gently. "
                    "No artificial lights. High contrast between the orange flesh and the white seeds."
                ),
                "Buah Labu Tipe 5": (
                    "A 60cm architectural mosque model held securely by hands, showing layered squash anatomy. "
                    "The base is the tough outer rind, the walls are deep orange flesh, and the domes are polished smooth. "
                    "Features multiple small minarets standing prominently at the corners. "
                    "No lighting, no electronics, no LEDs, no glowing parts. Pure organic textures in natural daylight."
                ),
                "Buah Strawberry Tipe 1": (
                    "A substantial 60cm mosque model constructed from giant ripe strawberries, lifted up by two hands (diangkat). "
                    "The exterior walls and domes are vibrant red with distinct yellow seed pores on the surface. "
                    "Features four tall minarets made of stacked strawberry sections, standing prominently. "
                    "The character's hands are gripping the base of the red fruit mosque firmly. "
                    "No internal lights, no LEDs, no artificial glow. Natural daylight on the seedy fruit texture."
                ),
                "Buah Strawberry Tipe 2": (
                    "A 60cm mosque miniature made of fresh strawberry, held by a character's hands (dipegang). "
                    "The main dome is made from the green leafy top (sepals) of a strawberry, precisely trimmed into a dome shape. "
                    "The body is carved from juicy red strawberry flesh. "
                    "Features two prominent minarets standing tall at the front. "
                    "No electronics, no lighting, no LEDs. Pure organic craftsmanship in natural daylight."
                ),
                "Buah Strawberry Tipe 3": (
                    "A unique 60cm mosque carved from the white-ish internal flesh of a strawberry, lifted by hands. "
                    "The walls have a pale pink and white gradient texture, looking very organic and soft. "
                    "The minarets are tall towers carved from the firmer white core of the strawberry. "
                    "The character's hands are supporting the structure from the sides. "
                    "No lights, no glowing effects. Focus on the internal fruit fibers and natural colors."
                ),
                "Buah Strawberry Tipe 4": (
                    "A detailed 60cm mosque model where the exterior is entirely covered in the textured yellow seeds of a strawberry. "
                    "The architecture is simple, but the surface pattern is highly complex and organic. "
                    "Features four clearly defined minarets standing prominently at the corners. "
                    "A character is lifting the mosque up to chest height. "
                    "No artificial lights. High contrast between the red skin and yellow seeds."
                ),
                "Buah Strawberry Tipe 5": (
                    "A 60cm architectural mosque model showing all parts of a strawberry: green leaves for accents, red skin for the body, and white flesh for windows. "
                    "Every component is 100% strawberry fruit. It is being held securely by two hands. "
                    "Features multiple small minarets standing prominently at the corners. "
                    "No lighting, no electronics, no LEDs, no glowing parts. Macro photography of fruit textures."
                ),
                "Buah Strawberry Tipe 6": (
                    "A gigantic 1-meter mosque model constructed from high-density strawberry slices. "
                    "The facade is a masterwork of texture, featuring the pitted red skin of the fruit with thousands of tiny yellow seeds acting as natural golden rivets. "
                    "The colossal dome is made of translucent strawberry-infused crystal gelatin, illuminated by a deep 'Crimson Dusk' internal wash light that creates a soft, diffused halo. "
                    "Instead of bright neon, the arches are outlined with a dim, steady rose-gold glow that accentuates the fruit's natural curves. "
                    "The minarets are capped with fresh green leaves, illuminated from below by subtle warm-white spotlights, creating a sophisticated and organic masterpiece."
                ),
                "Buah Nanas Tipe 1": (
                    "A grand 60cm mosque model constructed from fresh pineapple, being lifted up by two hands. "
                    "The main dome is made from the green leafy crown of the pineapple, trimmed into a perfect sphere. "
                    "The body features the yellow-orange hexagonal skin patterns, resembling ancient tiles. "
                    "Features four tall, clearly defined minarets carved from solid pineapple cores, standing prominently. "
                    "No internal lights, no LEDs. Natural daylight highlighting the rough, scaly texture of the fruit."
                ),
                "Buah Nanas Tipe 2": (
                    "A massive 60cm mosque miniature carved from the bright yellow internal flesh of a pineapple, held firmly by hands. "
                    "The walls have a fibrous, juicy yellow texture with horizontal carving lines. "
                    "Features two towering minarets standing prominently at the front, looking very structural and solid. "
                    "The character is lifting the heavy 60cm fruit mosque to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the vibrant yellow organic surface."
                ),
                "Buah Nanas Tipe 3": (
                    "A sturdy 60cm mosque fortress made entirely of the dark brown and green pineapple rind. "
                    "The natural hexagonal patterns of the skin act as the building blocks for the walls. "
                    "Features massive, thick minarets made of stacked pineapple rind cylinders, standing tall. "
                    "Hands are gripping the sides of the heavy 60cm structure. "
                    "No lights, no glowing effects. A very rugged and detailed organic stone-like look."
                ),
                "Buah Nanas Tipe 4": (
                    "A unique 60cm mosque model where the minarets and arches are decorated with the sharp, spiky green leaves of the pineapple. "
                    "The architecture is bold and sharp, using the fruit's natural spikes as decorative finials. "
                    "The main dome is polished yellow flesh. It is being lifted up by a character. "
                    "No artificial lights. High contrast between the green spikes and the yellow fruit body."
                ),
                "Buah Nanas Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all layers: green leaves for the top, hexagonal rind for the walls, and yellow flesh for the domes. "
                    "Every part is 100% pineapple. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure fruit craftsmanship in bright natural light."
                ),
                "Buah Nanas Tipe 6": (
                    "A grand 1-meter standalone mosque object built from interlocking geometric pineapple rind segments. "
                    "The diamond-patterned skin creates a rugged, golden-brown architectural armor. "
                    "The main dome is a massive sphere of carved, succulent yellow pineapple, glowing with a 'Champagne Solar' internal LED that highlights the fibrous golden veins of the fruit. "
                    "The sharp, spiked green crowns of the pineapple form the minaret towers, lit with a very dim, steady emerald-green wash from the base. "
                    "No neon strips; instead, the light 'bleeds' naturally through the gaps in the rind, creating a rhythmic and high-luxury play of light and shadow."
                ),
                "Buah Melon Tipe 1": (
                    "A grand 60cm mosque model made of 100% real honeydew melon, lifted up by two hands. "
                    "The exterior walls feature the natural white netted 'web' pattern of the green melon skin, looking like complex carvings. "
                    "The domes are smooth spheres of light-green melon flesh. "
                    "Features four tall minarets standing prominently, carved from solid melon rind. "
                    "No internal lights, no LEDs. Natural daylight highlighting the textured skin and juicy flesh."
                ),
                "Buah Melon Tipe 2": (
                    "A massive 60cm mosque miniature carved from the vibrant orange flesh of a Cantaloupe melon, held firmly by hands. "
                    "The walls have a dense, matte orange fruit texture with clean architectural lines. "
                    "Features two towering minarets standing prominently at the front, looking very solid. "
                    "The character is lifting the 60cm fruit mosque to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the bright orange organic surface."
                ),
                "Buah Melon Tipe 3": (
                    "A sturdy 60cm mosque model made entirely of bright yellow 'Golden Melon' skin. "
                    "The exterior is smooth, shiny, and vibrant yellow, chiseled with simple Islamic geometric patterns. "
                    "Features prominent yellow minarets standing tall at each corner. "
                    "Hands are gripping the base of the heavy 60cm structure. "
                    "No lights, no glowing effects. A very clean and premium organic look."
                ),
                "Buah Melon Tipe 4": (
                    "A unique 60cm mosque model where the skin of the melon is partially peeled to create a white and green lattice effect. "
                    "The architecture is intricate, showing the layers of the melon rind. "
                    "The main dome is a large, polished sphere of pale-green flesh. "
                    "Features four clearly defined minarets standing tall. It is being lifted up by a character. "
                    "No artificial lights. High contrast between the outer skin and inner flesh."
                ),
                "Buah Melon Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all layers: the textured outer net-skin, the firm white rind, and the soft colored flesh. "
                    "Every part is 100% melon fruit. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at the corners. "
                    "No lighting, no electronics, no LEDs. Pure fruit craftsmanship in natural light."
                ),
                "Buah Melon Tipe 6": (
                    "A colossal 1-meter diorama built from honeydew and cantaloupe melon. "
                    "The walls showcase the intricate, reticulated 'net' texture of the rind, looking like aged ivory carvings. "
                    "The colossal main dome is made of translucent pale-jade melon flesh, filled with a 'Starlight Mint' internal lighting scheme—thousands of micro-fiber optic points that twinkle like a distant galaxy. "
                    "The minarets are smooth, polished rinds with a soft, steady turquoise glow emanating from the window slits. "
                    "The overall lighting is soft, ethereal, and diffused, making the mosque appear like a glowing emerald sanctuary in a quiet, twilight atmosphere."
                ),
                "Buah Salak": (
                    "A grand 1-meter mosque model constructed entirely from snake-fruit (salak) scales. "
                    "The facade is a masterwork of dark-brown, high-gloss metallic-looking scales, arranged in a perfect shingle pattern like ancient dragon skin. "
                    "The main dome is a stark contrast, made of polished, bone-white ivory salak flesh with a subtle matte finish. "
                    "Lighting: No external lamps; instead, a 'Ghostly Moonwhite' LED glows from deep within the cracks of the scales, creating a high-contrast, mysterious aura. "
                    "The minarets are tall, dark pillars of stacked scales, topped with a single, steady amber pin-light for a sophisticated, ancient look."
                ),
                "Buah Durian": (
                    "A massive 1-meter mosque object built from thousands of sharp, golden-brown durian thorns. "
                    "The architecture is aggressive and monumental, with every inch of the walls covered in hyper-detailed, needle-sharp spikes. "
                    "The colossal main dome is made of rich, creamy yellow durian pulp with a high-gloss finish, glowing with a 'Royal Tungsten' internal light that makes it look like molten gold. "
                    "Minarets are crafted from the thick, woody durian rinds, wrapped in a very dim, steady warm-white glow seeping through the gaps of the thorns. "
                    "The visual is heavy, powerful, and overwhelmingly detailed."
                ),
                "Buah Kiwi": (
                    "A unique 1-meter mosque diorama built from the fuzzy and succulent anatomy of Kiwi fruit. "
                    "The main structure is wrapped in the brown, velvet-like 'fuzzy' skin of the kiwi, creating a soft, organic, moss-like texture. "
                    "The main dome is a cross-section of a giant kiwi, where the radial pattern of black seeds and vibrant green fibers are illuminated by an 'Electric Lime' internal wash. "
                    "The light bleeds through the translucent green flesh, highlighting every tiny fiber. "
                    "Minarets are smooth, carved kiwi wood capped with vibrant green slices, lit with steady mint-colored fiber-optics for a fresh, serene architectural vibe."
                ),
                "Buah Pisang Tipe 1": (
                    "A grand 60cm mosque model constructed entirely from fresh yellow bananas, lifted up by two hands. "
                    "The exterior walls are made of smooth, vibrant yellow banana peels, looking like polished golden plates. "
                    "The main dome is a large sphere carved from a cluster of banana fruit. "
                    "Features four tall minarets standing prominently, made of long, straight unpeeled bananas. "
                    "No internal lights, no LEDs. Natural daylight highlighting the smooth yellow organic texture."
                ),
                "Buah Pisang Tipe 2": (
                    "A massive 60cm mosque miniature carved from the firm white internal flesh of bananas, held firmly by hands. "
                    "The walls have a dense, creamy white fruit texture with vertical carving lines. "
                    "Features two towering minarets standing prominently at the front, looking solid and structural. "
                    "The character is lifting the 60cm white fruit mosque to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the clean white organic surface."
                ),
                "Buah Pisang Tipe 3": (
                    "A sturdy 60cm mosque model made of 100% green unripened banana skin. "
                    "The exterior is a solid dark green with a matte, slightly ridged texture. "
                    "Features prominent green minarets made of thick, straight green banana sections. "
                    "Hands are gripping the sides of the heavy 60cm green structure. "
                    "No lights, no glowing effects. A very rugged and firm organic look."
                ),
                "Buah Pisang Tipe 4)": (
                    "A unique 60cm mosque model where the yellow banana skins are etched with geometric Islamic patterns, revealing the white flesh underneath. "
                    "The architecture is intricate, showing high contrast between yellow skin and white interior. "
                    "The main dome is a large, polished yellow sphere. "
                    "Features four clearly defined minarets standing tall. It is being lifted up by a character. "
                    "No artificial lights. High contrast and detailed hand-carved fruit textures."
                ),
                "Buah Pisang Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all parts of the banana: the yellow outer peel for the base, "
                    "the white fruit for the walls, and the stem sections for decorative pillars. "
                    "Every component is 100% banana. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure fruit craftsmanship in natural light."
                ),
                "Buah Pisang Tipe 6": (
                    "A monumental 1-meter mosque diorama built from the complete anatomy of a banana tree. "
                    "The walls are crafted from layers of fresh, waxy green banana leaves with deep, parallel ribbing textures. "
                    "The colossal main dome is a sphere made of thousands of curved, bright yellow banana slices, glowing from within with a 'Soft Canary' LED scheme that highlights the tiny black seeds in the center. "
                    "Tall minarets are built from the textured, fibrous stalks of the banana bunch, wrapped in steady warm-white fiber-optic lines. "
                    "All entrance arches are outlined with a dim, steady lime-green neon glow, reflecting off the glossy, organic surface of the leaves."
                ),
                "Buah Manggis Tipe 1": (
                    "A grand 60cm mosque model constructed entirely from dark purple mangosteen rinds, lifted up by two hands. "
                    "The exterior walls are made of thick, smooth, deep-purple mangosteen skins with a matte finish. "
                    "The main dome is a large sphere carved from the purple rind, featuring the iconic star-shaped fruit bottom as a decorative crest. "
                    "Features four tall minarets standing prominently, made of stacked purple rind sections. "
                    "No internal lights, no LEDs. Natural daylight highlighting the rich purple organic texture."
                ),
                "Buah Manggis Tipe 2": (
                    "A massive 60cm mosque miniature carved from the pristine white internal segments of mangosteen, held firmly by hands. "
                    "The walls have a soft, juicy, and bright white fruit texture, looking like pure snow. "
                    "Features two towering minarets standing prominently at the front, looking very structural and solid. "
                    "The character is lifting the 60cm white fruit mosque to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the clean white organic surface."
                ),
                "Buah Manggis Tipe 3": (
                    "A sturdy 60cm mosque model featuring the thick green sepals (leaves) of the mangosteen as decorative elements. "
                    "The body is made of dark purple rind, while the minaret tops and dome accents are made of the sturdy green fruit stems. "
                    "Features prominent minarets standing tall at each corner. "
                    "Hands are gripping the sides of the heavy 60cm purple and green structure. "
                    "No lights, no glowing effects. A very vibrant and detailed organic look."
                ),
                "Buah Manggis Tipe 4": (
                    "A unique 60cm mosque model where the dark purple skin is partially carved away to reveal the white flesh segments underneath. "
                    "The architecture shows high contrast between the thick purple walls and the white interior rooms visible through arched windows. "
                    "The main dome is a large, polished purple sphere. "
                    "Features four clearly defined minarets standing tall. It is being lifted up by a character. "
                    "No artificial lights. High contrast and detailed hand-carved fruit textures."
                ),
                "Buah Manggis Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all parts: the dark purple outer rind for the walls, "
                    "the green stem for the pillars, and the white segments for the domes. "
                    "Every component is 100% mangosteen. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure fruit craftsmanship in natural light."
                ),
                "Buah Manggis Tipe 6": (
                    "A monumental 1-meter mosque model built from Mangosteen anatomy. "
                    "The walls are thick, matte-textured rinds in deep royal purple. "
                    "The main dome is a sphere of snow-white mangosteen segments with a high-gloss finish, glowing from within with a 'Celestial White' LED that makes it look like polished marble. "
                    "Minarets are topped with the iconic wooden petal-shaped bases of the fruit, lit by subtle warm-white pin-lights."
                ),
                "Buah Jeruk": (
                    "A grand 1-meter mosque object constructed from Orange anatomy. "
                    "The walls feature the hyper-detailed pitted texture of orange rinds. "
                    "The main dome is a massive sphere of interlocking translucent citrus sacs, glowing with a 'Warm Amber' internal wash. "
                    "The light refracts through the juicy pulp, creating a shimmering, crystalline effect like thousands of tiny orange gemstones."
                ),
                "Buah Apel": (
                    "A monumental 1-meter standalone mosque object built entirely from thousands of high-gloss red and green Apple anatomy. "
                    "The walls are constructed from millions of interlocking, polished red apple skin segments, looking like deep obsidian-ruby scales with realistic waxy texture. "
                    "The colossal main dome is a translucent sphere of polished, crisp white apple flesh, glowing from within with a soft, internal 'Amber Harvest' LED that reveals the fine organic grain of the fruit. "
                    "Tall minarets are crafted from tightly packed whole red apples, wrapped in thin, steady warm-white fiber-optic lines. "
                    "All entrance arches are outlined with a dim, steady lime-green neon glow, reflecting beautifully off the ultra-glossy apple skin surface against a high-contrast dark environment."
                ),
                "Buah Anggur": (
                    "A gigantic 1-meter standalone mosque diorama built from thousands of glossy purple and green grape halves. "
                    "The entire structure has a luscious, 'wet-look' texture, made of densely packed translucent grapes looking like clusters of polished amethyst gemstones. "
                    "The colossal main dome is a sphere of clear gelatin where thousands of grape seeds are arranged in intricate geometric Arabic calligraphy patterns, silhouetted against a deep 'Royal Violet' internal LED glow. "
                    "Tall minarets are crafted from stacked purple grapes, wrapped in intensely flickering colorful LED fairy lights and framed by intense multi-colored RGB neon strips. "
                    "The entire fruity surface glows powerfully against the dark background, casting a magical, colorful wash over the intricate sugary craftsmanship."
                ),
                "Batok Kelapa Tipe 1": (
                    "A grand 60cm mosque model made of 100% polished dark brown coconut shells, lifted up by two hands. "
                    "The exterior walls and domes are made of smooth, deep-brown shell sections with a natural glossy finish. "
                    "Features four tall minarets standing prominently, made of precisely turned coconut shell cylinders. "
                    "No internal lights, no LEDs. Natural daylight highlighting the rich woody texture and smooth surface."
                ),
                "Batok Kelapa Tipe 2": (
                    "A massive 60cm mosque miniature featuring the rough, hairy fibrous texture of an unpolished coconut shell. "
                    "The architecture looks ancient and organic, with visible coconut fibers on the walls. "
                    "Features two towering minarets standing prominently at the front, looking very structural. "
                    "The character is lifting the 60cm heavy structure to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the raw, earthy organic surface."
                ),
                "Batok Kelapa Tipe 3": (
                    "A unique 60cm mosque model where the dark shell is carved to reveal the bright white coconut meat inside. "
                    "The domes are smooth white spheres of coconut meat, while the walls are dark brown shell. "
                    "Features prominent brown minarets standing tall at each corner. "
                    "Hands are gripping the sides of the heavy 60cm structure. "
                    "No lights, no glowing effects. High contrast between the dark shell and white interior."
                ),
                "Batok Kelapa Tipe 4": (
                    "A detailed 60cm mosque model constructed from thousands of small, hand-cut coconut shell squares in a mosaic pattern. "
                    "The architecture is complex, featuring intricate geometric Islamic fretwork carved into the shell. "
                    "Features four clearly defined minarets standing tall. It is being lifted up by a character. "
                    "No artificial lights. Focus on the craftsmanship and the natural dark brown shades."
                ),
                "Batok Kelapa Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all parts: polished shell for the domes, rough husk for the base, and white meat for the windows. "
                    "Every component is 100% coconut. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure organic craftsmanship in natural light."
                ),
                "Batok Kelapa Tipe 6": (
                    "A monumental 1-meter mosque diorama built from the rugged anatomy of Coconuts. "
                    "The walls feature the raw, fibrous brown texture of coconut husks (sabut) and polished dark-brown coconut shells (batok). "
                    "The colossal main dome is made of translucent, snowy-white coconut flesh with a high-gloss finish, glowing from within with a 'Crystal White' LED that highlights the organic ridges. "
                    "Minarets are crafted from stacked coconut shells, wrapped in steady warm-white fiber-optic lines that accentuate the rough fibers. "
                    "The lighting is humble yet dignified, seeping through the fibrous cracks of the husk against a dark, moody background."
                ),
                "Serabut Kelapa Tipe 1": (
                    "A grand 60cm mosque model made entirely from raw brown coconut husk fibers, lifted up by two hands. "
                    "The walls and domes are constructed from densely packed and shaped coconut fibers, giving a fuzzy and organic appearance. "
                    "Features four tall minarets standing prominently, made of tightly bound fiber columns. "
                    "No internal lights, no LEDs. Natural daylight highlighting the messy yet structured fibrous texture."
                ),
                "Serabut Kelapa Tipe 2": (
                    "A massive 60cm mosque miniature featuring intricate patterns made of braided coconut fibers. "
                    "The architecture is defined by thick, woven ropes of husk that form the arches and domes. "
                    "Features two towering minarets standing prominently, looking like solid woven pillars. "
                    "The character is lifting the 60cm heavy fiber mosque to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the complex woven organic surface."
                ),
                "Serabut Kelapa Tipe 3": (
                    "A sturdy 60cm mosque model made of sun-dried golden-yellow coconut husks. "
                    "The exterior has a lighter, brighter tone with a very dry and coarse texture. "
                    "Features prominent golden fiber minarets standing tall at each corner. "
                    "Hands are gripping the sides of the heavy 60cm structure. "
                    "No lights, no glowing effects. A very rustic, earthy, and sun-kissed organic look."
                ),
                "Serabut Kelapa Tipe 4": (
                    "A detailed 60cm mosque model where the coconut husk is compressed into solid blocks before being carved. "
                    "The architecture shows clean lines but with the visible texture of thousands of tiny overlapping fibers. "
                    "Features four clearly defined minarets standing tall. It is being lifted up by a character. "
                    "No artificial lights. Focus on the density of the fiber and the hand-crafted mosque shape."
                ),
                "Serabut Kelapa Tipe 5": (
                    "A majestic 60cm architectural mosque model showing a mix of loose fibers for the domes and compressed husk for the walls. "
                    "Every part is 100% coconut husk and fiber material. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure organic craftsmanship in natural light."
                ),
                "Buah Markisa": (
                    "A gigantic 1-meter mosque model built from Passionfruit anatomy. "
                    "The exterior walls are made of dark, shriveled purple skins showing intense, realistic organic wrinkles. "
                    "The colossal main dome is a sphere of translucent orange passionfruit pulp, where millions of crunchy black seeds are suspended like a swirling galaxy. "
                    "Inside, a 'Solar Flare' golden LED scheme makes the seeds look like a floating nebula trapped in glass. "
                    "Every minaret is a pillar of purple rind wrapped in thin, steady violet neon strips, casting a powerful, saturated glow over the wet, glossy fruity interior."
                ),
                "Daun Pisang Tipe 1": (
                    "A grand 60cm mosque model constructed entirely from fresh vibrant green banana leaves, lifted up by two hands. "
                    "The structure is made of expertly folded and layered leaf sections, showing the natural parallel vein textures. "
                    "The domes are large spheres made of overlapping leaf strips. "
                    "Features four tall minarets standing prominently, made of tightly rolled green leaves. "
                    "No internal lights, no LEDs. Natural daylight highlighting the waxy green surface."
                ),
                "Daun Pisang Tipe 2": (
                    "A majestic 60cm mosque miniature made from ripening yellow banana leaves, held firmly by hands. "
                    "The architecture has a bright golden-yellow tone with soft organic textures. "
                    "Features two towering minarets standing prominently, made of bundled yellow leaf midribs. "
                    "The character is lifting the 60cm yellow structure to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the smooth yellow organic surface."
                ),
                "Daun Pisang Tipe 3": (
                    "A unique 60cm mosque model featuring a mix of fresh green and naturally dried brown banana leaves. "
                    "The architecture shows a beautiful contrast between the flexible green walls and the crisp brown domes. "
                    "Features prominent minarets standing tall at each corner with alternating textures. "
                    "Hands are gripping the sides of the heavy 60cm folded leaf structure. "
                    "No lights, no glowing effects. High contrast between fresh and dried leaf textures."
                ),
                "Daun Pisang Tipe 4": (
                    "A detailed 60cm mosque model where the frame is made of thick banana leaf midribs and covered in thin leaf layers. "
                    "The architecture is sharp and sturdy, showing the thick structural veins of the banana leaf. "
                    "Features four clearly defined minarets made of straight, bundled leaf ribs. It is being lifted up by a character. "
                    "No artificial lights. Focus on the craftsmanship and the natural green shades."
                ),
                "Daun Pisang Tipe 5": (
                    "A rustic 60cm architectural mosque model made entirely of sun-dried, papery brown banana leaves. "
                    "The texture is crisp, featuring the iconic shredded edges of old banana leaves. "
                    "Every part is 100% dried banana leaf. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure organic craftsmanship in natural light."
                ),
                "Daun Pisang Tipe 6": (
                    "A monumental 1-meter mosque model built from layers of fresh and dried banana leaves. "
                    "The walls feature the deep, rhythmic parallel ribbing of waxy green leaves. "
                    "The main dome is a colossal sphere of tightly woven young banana leaves (janur), glowing with an internal 'Forest Mint' LED that highlights the translucent green veins. "
                    "Minarets are tall, rolled-up leaf scrolls wrapped in steady warm-white fiber-optic lines. "
                    "The atmosphere is fresh, organic, and high-contrast against the dark background."
                ),
                "Daun Jati": (
                    "A grand 1-meter mosque built from the wide, rough-textured leaves of the Teak tree. "
                    "The facade has a leathery, matte brown-green texture with prominent, rugged veins like ancient parchment. "
                    "The main dome is made of overlapping dried teak leaves, glowing from within with a 'Deep Amber' LED that seeps through the natural holes and cracks in the leaves. "
                    "This creates a mysterious, rustic, and 'old-world' architectural vibe. "
                    "No neon; just raw, weathered organic textures in a high-contrast cinematic setting."
                ),
                "Daun Pakis": (
                    "A gigantic 1-meter mosque diorama constructed from thousands of intricate fern fronds. "
                    "The architecture looks like a fractal masterpiece, with curled fern 'heads' (fiddleheads) forming the arches and pillar decorations. "
                    "The colossal dome is a dense weave of delicate fern leaves, illuminated by a 'Neon Lime' internal wash that creates complex shadows. "
                    "Tall minarets are crafted from upright fern stalks wrapped in thin, silver-white fiber-optic lines, looking like a glowing jungle sanctuary."
                ),
                "Daun Kelapa Tipe 1": (
                    "A grand 60cm mosque model intricately woven from young yellow coconut leaves (janur), lifted up by two hands. "
                    "The entire structure features complex traditional weaving patterns, with a bright pale-yellow color. "
                    "The domes are smooth, woven spheres, and the four tall minarets are tightly braided yellow leaf strips standing prominently. "
                    "No internal lights, no LEDs. Natural daylight highlighting the fresh, flexible organic texture."
                ),
                "Daun Kelapa Tipe 2": (
                    "A sturdy 60cm mosque miniature made from mature dark-green coconut leaves, held firmly by hands. "
                    "The walls are made of layered green leaf sections, looking like organic shingles or tiles. "
                    "Features two towering minarets standing prominently, made of thick, bundled green leaf ribs (lidi). "
                    "The character is lifting the 60cm green structure to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the vibrant green organic surface."
                ),
                "Daun Kelapa Tipe 3": (
                    "A unique 60cm mosque model featuring a mix of young yellow janur and mature green leaves. "
                    "The architecture shows a beautiful color gradient, with green bases and yellow woven domes. "
                    "Features prominent minarets standing tall at each corner with alternating green and yellow patterns. "
                    "Hands are gripping the sides of the 60cm woven structure. "
                    "No lights, no glowing effects. High contrast between the yellow and green leaf textures."
                ),
                "Daun Kelapa Tipe 4": (
                    "A detailed 60cm mosque model where the framework is made of coconut leaf midribs (lidi) and covered in thin leaf strips. "
                    "The architecture is sharp and skeletal yet elegant, showing the strength of the leaf ribs. "
                    "Features four clearly defined, very straight minarets made of bundled lidi. It is being lifted up by a character. "
                    "No artificial lights. Focus on the craftsmanship and the natural light-brown and green shades."
                ),
                "Daun Kelapa Tipe 5": (
                    "A majestic 60cm architectural mosque model made of sun-dried brown coconut leaves. "
                    "The texture is crisp and papery, giving an ancient, rustic look like a traditional temple. "
                    "Every part is 100% dried coconut leaf. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure organic craftsmanship in natural light."
                ),
                "Daun Kelapa Tipe 6": (
                    "A monumental 1-meter mosque diorama built from the complete anatomy of Coconut leaves. "
                    "The walls are constructed from millions of dry, brown coconut leaflets arranged in a sharp, rhythmic chevron pattern. "
                    "The colossal main dome is a masterwork of 'Janur' (young yellow coconut leaves), woven into an intricate, tight diamond-mesh pattern. "
                    "Inside, a 'Golden Harvest' internal LED scheme glows through the gaps of the weave, creating a mesmerizing pattern of light and shadow (ray-traced shadows). "
                    "Tall minarets are crafted from thousands of bundled 'Lidi' (leaf midribs), looking like slender ivory towers wrapped in steady warm-white fiber-optic lines. "
                    "The overall look is incredibly detailed, organic, and culturally rich against a high-contrast dark background."
                ),
                "Daun Talas": (
                    "A monumental 1-meter mosque model built from oversized, waxy Taro leaves. "
                    "The surface features hyper-realistic water droplets that bead and roll across the velvet-textured green surface. "
                    "The main dome is a massive, single curved leaf glowing with an internal 'Deep Cyan' LED, showing a soft diffused light. "
                    "Every arch is outlined with a subtle moisture-glimmer, looking fresh and ethereal."
                ),
                "Daun Sirih": (
                    "A grand 1-meter mosque built from thousands of heart-shaped Betel leaves. "
                    "The walls are arranged in a shimmering scale-like pattern, showcasing the elegant curved veins of each leaf. "
                    "The main dome is a sphere of translucent green membranes, glowing with an internal 'Emerald Forest' LED that reveals the intricate network of veins. "
                    "The look is delicate, sacred, and very detailed."
                ),
                "Daun Kering": (
                    "A fragile 1-meter mosque model built from weathered, crispy dried leaves. "
                    "The texture is a mix of brittle browns and ochre, featuring realistic holes and frayed edges from age. "
                    "The main dome is a skeletal structure of leaf veins, glowing with a dim, flickering 'Candle-Light' LED that leaks through the natural decay. "
                    "This creates a profoundly sad yet beautiful architectural masterpiece, looking extremely old and fragile."
                ),
                "Daun Bambu": (
                    "A monumental 1-meter mosque model built from thousands of slender, needle-like Bamboo leaves. "
                    "The walls feature a clean, vertical striped texture made from overlapping fresh green leaf blades. "
                    "The main dome is a sharp, conical structure glowing with an internal 'Pale Jade' LED that highlights the elegant parallel veins. "
                    "The look is minimalist, serene, and incredibly sharp in 8K resolution."
                ),
                "Daun Pepaya": (
                    "A grand 1-meter mosque object built from the deeply lobed, finger-like anatomy of Papaya leaves. "
                    "The architecture features complex, star-shaped patterns on the walls where the leaf lobes overlap. "
                    "The colossal main dome is an intricate lace-like structure, glowing with an internal 'Solar Amber' LED that casts dramatic, jagged shadows. "
                    "It looks like an ancient, organic cathedral made of green lace."
                ),
                "Daun Teratai": (
                    "A monumental 1-meter mosque diorama built from oversized, circular Lotus leaves. "
                    "The main dome is a single, massive perfectly curved leaf with a soft matte texture and high-gloss water droplets on top. "
                    "Internal 'Lunar Ice' LED lighting creates a soft, ethereal glow that makes the leaf appear translucent. "
                    "The minarets are crafted from porous lotus stems, with light leaking through the natural internal air-canals."
                ),
                "Daun Pandan": (
                    "A monumental 1-meter mosque model built from thousands of long, slender Pandan leaves. "
                    "The walls feature a masterwork of complex diagonal weaving, showcasing the sharp central rib of each leaf. "
                    "The main dome is a sphere of knotted and plaited pandan strips, glowing with an internal 'Lime Forest' LED that seeps through the tight weaves. "
                    "The look is incredibly neat, rhythmic, and possesses a high-gloss organic finish that catches the light beautifully."
                ),
                "Daun Pucuk Merah": (
                    "A grand 1-meter mosque diorama built from millions of tiny leaves from the Syzygium (Pucuk Merah) plant. "
                    "The facade shows a stunning natural gradient, with bright crimson-red leaves at the tips of the minarets fading into deep forest green at the base. "
                    "The main dome is a dense, fluffy mound of tiny red leaves, glowing from within with a 'Sunset Gold' LED that highlights the delicate, small-scale texture. "
                    "It looks like a mosque built from living, glowing embers."
                ),
                "Bunga Mawar": (
                    "A monumental 1-meter mosque model built from millions of deep red rose petals. "
                    "The walls feature a soft, velvet-like texture of overlapping petals, creating a rich 'Ombre' effect from dark maroon to bright scarlet. "
                    "The colossal main dome is a massive, blooming rose head with a high-gloss dew finish, glowing from within with a 'Deep Ruby' LED that seeps through the petal layers. "
                    "Minarets are crafted from dark green rose stems with realistic sharp thorns, lit by steady warm-white fiber optics. "
                    "The look is romantic, majestic, and incredibly detailed in its organic softness."
                ),
                "Bunga Melati": (
                    "A gigantic 1-meter mosque diorama built from thousands of tiny, ivory-white Jasmine buds. "
                    "The facade is a dense mosaic of unopened buds, looking like precious pearls or white marble carvings. "
                    "The main dome is a sphere of fully bloomed jasmine flowers, glowing from within with a soft 'Lunar Pearl' LED wash. "
                    "Instead of neon, the arches are outlined with a dim, steady warm-white glow that emphasizes the purity of the white petals. "
                    "The visual is serene, spiritual, and looks incredibly fragile and clean."
                ),
                "Bunga Matahari": (
                    "A grand 1-meter mosque object built from the anatomy of Sunflowers. "
                    "The walls are covered in the rough, fibrous texture of sunflower petals, while the arches are framed by the large, vibrant yellow outer petals. "
                    "The colossal main dome is a sphere made of millions of dark brown sunflower seeds arranged in perfect Fibonacci spirals, glowing with an internal 'Golden Flare' LED. "
                    "Tall minarets are thick, hairy green stalks topped with smaller sunflower heads, wrapped in steady amber fiber-optic lines. "
                    "The look is bold, warm, and high-contrast."
                ),
                "Bunga Teratai": (
                    "A monumental 1-meter mosque built from oversized Pink Lotus petals. "
                    "The walls have a waxy, semi-translucent texture that captures light beautifully. "
                    "The main dome is a massive, multi-layered lotus flower glowing from its core with a 'Zen Pink' internal LED, making the petal veins visible. "
                    "Inside the dome, the yellow seed pod (receptacle) acts as a glowing chandelier. "
                    "The minarets are smooth, pale-green stalks, giving a very calm, ethereal architectural vibe."
                ),
                "Bunga Anggrek": (
                    "A gigantic 1-meter mosque model built from vibrant purple and white Orchid petals. "
                    "The architecture features the unique, organic shapes of orchid lips (labellum) as entrance arches. "
                    "The main dome is a sphere of translucent orchid wings, glowing with a 'Mystic Violet' internal LED that highlights the intricate purple spots and veins. "
                    "The minarets are slender, curved orchid stems wrapped in thin, steady silver-white fiber optics. "
                    "The visual is extremely luxurious, rare, and artistic."
                ),
                "Bunga Lavender": (
                    "A unique 1-meter mosque diorama built from millions of tiny purple lavender sprigs. "
                    "The texture is extremely 'busy' and fuzzy, creating a soft purple haze across the walls. "
                    "The main dome is a dense mound of lavender buds glowing with a 'Soft Lilac' internal wash. "
                    "The minarets are tall, slender bundles of lavender stalks wrapped in rapidly pulsing violet fairy lights. "
                    "It looks like a mosque built from a magical purple cloud, very atmospheric and moody."
                ),
                "Bunga Kamboja": (
                    "A monumental 1-meter mosque model built from thousands of thick-petaled Frangipani (Kamboja) flowers. "
                    "The walls have a smooth, waxy porcelain-like finish with a natural white-to-yellow gradient. "
                    "The main dome is a sphere of overlapping waxy petals, glowing from within with a 'Golden Butter' LED that reveals the soft organic texture. "
                    "Minarets are crafted from the thick, greyish-green woody stems of the Kamboja tree, lit by steady warm-white fiber optics for a serene, tropical vibe."
                ),
                "Bunga Sepatu": (
                    "A gigantic 1-meter mosque diorama built from vibrant red Hibiscus flowers. "
                    "The walls feature the silky, fibrous texture of large red petals. "
                    "The colossal main dome is formed by hundreds of translucent petals, with a central golden stamen acting as a majestic spire. "
                    "Inside, a 'Crimson Pulse' LED highlights the delicate veins of the petals, making the entire structure glow like a red lantern against a dark background."
                ),
                "Bunga Tulip": (
                    "A grand 1-meter mosque object built from thousands of perfectly curved Tulip petals. "
                    "The architecture is minimalist and sleek, with a satin-like glossy finish on every surface. "
                    "The colossal main dome is a closed-chalice shape made of deep purple petals, glowing with a 'Mystic Amethyst' internal LED wash. "
                    "All arches are outlined with a dim, steady silver-white glow, creating a high-luxury and modern botanical masterpiece."
                ),
                "Bunga Bougainvillea": (
                    "A unique 1-meter mosque model built from millions of paper-thin Bougainvillea petals in vibrant magenta. "
                    "The texture is crisp and intricate, with petals arranged like roofing shingles across the entire facade. "
                    "The main dome is a dense, glowing mound of paper-like membranes, illuminated by a 'Neon Fuchsia' internal wash that leaks through the paper-thin petals. "
                    "The visual is incredibly light, airy, and intensely colorful."
                ),
                "Pisang & Kamboja": (
                    "A monumental 1-meter mosque model blending fresh banana leaves and white frangipani. "
                    "The walls are built from waxy green banana leaf scrolls, while every entrance arch is meticulously decorated with thousands of white-and-yellow Kamboja flowers. "
                    "The colossal dome is a weave of green 'Janur' with blooming kamboja flowers acting as glowing jewels. "
                    "Internal 'Forest Gold' LED lighting seeps through the leaves and petals, creating a lush, tropical paradise vibe in high-contrast."
                ),
                "Jati & Mawar": (
                    "A grand 1-meter mosque diorama mixing rugged dried Teak leaves and deep red roses. "
                    "The structure has a rustic brown-leather base made from teak leaves, contrasted by a colossal main dome made entirely of millions of red velvet rose petals. "
                    "The minarets are thick teak stalks wrapped in thorny rose vines. "
                    "Lighting: A 'Deep Crimson' internal LED makes the dome glow like a burning ember, while the brown leaves stay in dramatic shadow."
                ),
                "Teratai & Melati": (
                    "A gigantic 1-meter mosque built from oversized circular Lotus leaves and tiny Jasmine buds. "
                    "The facade is a pure white mosaic of jasmine flowers, built upon a sturdy base of dark green lotus stalks. "
                    "The main dome is a massive, perfectly curved lotus leaf with jasmine garlands draped over it like lace. "
                    "Inside, a 'Lunar Ice' white LED creates a serene, spiritual glow that makes the white petals look like glowing porcelain."
                ),
                "Keladi & Bougainvillea": (
                    "A monumental 1-meter mosque object featuring heart-shaped Caladium leaves and magenta Bougainvillea. "
                    "The walls are a vibrant mix of red-veined leaves and paper-thin magenta petals, creating a stunning organic gradient. "
                    "The main dome is a sphere of translucent pink membranes, glowing with an internal 'Fuchsia Galaxy' LED scheme. "
                    "This is the ultimate 'warna-warni' look, appearing like a glowing magical garden cathedral in the dark."
                ),
                "Bambu & Anggrek": (
                    "A grand 1-meter mosque combining slender green bamboo leaves and purple orchids. "
                    "The walls feature clean, vertical bamboo lines, while the arches are framed by exotic purple orchid lips (labellum). "
                    "The colossal dome is a sphere of bamboo weave with orchid petals embedded like stained glass. "
                    "Internal 'Pale Amethyst' LED lighting highlights the purple veins and green fibers, creating a high-luxury, peaceful vibe."
                ),
                "Brokoli": (
                    "A monumental 1-meter mosque model built entirely from Romanesco broccoli. "
                    "The walls feature thousands of natural, lime-green fractal pyramids and spiral cones. "
                    "The colossal main dome is a massive fractal spire glowing from within with a 'Toxic Emerald' LED wash that highlights the organic math-like patterns. "
                    "Minarets are tall fractal stalks wrapped in steady warm-white fiber-optic lines, looking like a masterpiece of alien architecture."
                ),
                "Jagung": (
                    "A gigantic 1-meter mosque diorama constructed from millions of translucent 'Glass Gem' corn kernels. "
                    "Each kernel looks like a polished, multi-colored gemstone in shades of blue, pink, purple, and gold. "
                    "The main dome is a massive sphere of glowing corn-gems, illuminated by a 'Prism RGB' internal LED that scatters colorful light through the translucent grains. "
                    "The visual is incredibly luxurious, resembling a cathedral made of thousands of tiny stained-glass beads."
                ),
                "Pare": (
                    "A grand 1-meter mosque object built from the rugged, bumpy skin of Bitter Gourds (Pare). "
                    "The walls have an intensely detailed, warty green texture that creates deep shadows. "
                    "The colossal main dome is made of polished, translucent pale-green pare flesh, glowing with a soft 'Acid Mint' internal LED. "
                    "The lighting 'bleeds' through the bumpy ridges, making the texture look hyper-detailed and sharp in 8K resolution."
                ),
                "Cabai Rawit": (
                    "A monumental 1-meter mosque model built from millions of vibrant red and bird's eye chilies. "
                    "The facade is a dense, high-gloss mosaic of shiny red chili skins. "
                    "The main dome is a sphere of densely packed chilies, glowing with a 'Lava Red' internal LED scheme that makes the entire structure look like a burning, sacred ember. "
                    "Minarets are topped with green chili stems, lit by steady warm-white pin-lights for a powerful and aggressive visual."
                ),
                "Terong": (
                    "A gigantic 1-meter mosque model built from high-gloss purple eggplant skins. "
                    "The texture is smooth, dark, and deeply reflective, looking like polished purple obsidian. "
                    "The colossal main dome is made of bone-white eggplant flesh, glowing from within with a 'Soft Amethyst' LED wash. "
                    "The contrast between the near-black purple skin and the glowing white interior creates a very sophisticated and high-luxury architectural vibe."
                ),
                "Jamur Kuping": (
                    "A unique 1-meter mosque diorama built from translucent black wood-ear mushrooms (Jamur Kuping). "
                    "The walls have a wavy, rubbery, and semi-translucent dark texture. "
                    "The main dome is a sphere of overlapping mushroom membranes, glowing with a dim 'Ethereal Blue' LED that highlights the veins of the fungus. "
                    "The look is dark, mysterious, and very high-contrast, perfect for a moody cinematic scene."
                ),
                "Bawang Merah": (
                    "A monumental 1-meter mosque model built from thousands of glossy purple shallot skins and cloves. "
                    "The walls feature the translucent, papery texture of red onion skins, layered like delicate shingles. "
                    "The colossal main dome is a sphere of polished white onion flesh, glowing from within with a 'Soft Lilac' LED that highlights the concentric ring patterns. "
                    "Minarets are topped with dried onion roots, looking like intricate ancient spires, lit by steady warm-white fiber optics."
                ),
                "Kol Ungu": (
                    "A gigantic 1-meter mosque diorama built from the tightly packed, wavy leaves of Purple Cabbage. "
                    "The facade shows a complex maze of white veins against deep violet leaf membranes. "
                    "The colossal main dome is a cross-section of a cabbage head, glowing with a 'Mystic Magenta' internal LED wash that reveals the labyrinth-like internal structure. "
                    "The lighting 'bleeds' through the purple fibers, creating a high-luxury and artistic architectural look."
                ),
                "Paprika": (
                    "A grand 1-meter mosque object built from high-gloss red, yellow, and orange Bell Peppers. "
                    "The walls have an ultra-smooth, waxy finish that reflects the surroundings like polished enamel. "
                    "The main dome is a sphere of translucent pepper flesh with internal 'Amber Sun' LED lighting, making the seeds inside visible as soft silhouettes. "
                    "All arches are outlined with a dim, steady gold neon glow, emphasizing the vibrant, juicy colors of the vegetable."
                ),
                "Jagung Manis": (
                    "A monumental 1-meter mosque constructed from millions of golden corn kernels and dried husks. "
                    "The walls are built from the pale-tan, fibrous texture of corn husks (kelobot), while the dome is a sphere of shiny, plump yellow kernels. "
                    "Internal 'Buttery Gold' LED lighting makes every kernel glow like a tiny amber gemstone. "
                    "The minarets are wrapped in 'corn silk' (rambut jagung), lit by thin, flickering fiber-optic lines for a soft, ethereal golden aura."
                ),
                "Labu Parang": (
                    "A massive 1-meter mosque model built from the thick, ribbed skin of Pumpkins. "
                    "The architecture is grand and heavy, featuring the deep grooves and textured orange rind. "
                    "The colossal main dome is a carved pumpkin sphere, glowing from within with a powerful 'Harvest Fire' orange LED that leaks through geometric star-shaped carvings. "
                    "The look is sturdy, warm, and cinematic, perfect for a high-contrast dark environment."
                ),
                "Wortel": (
                    "A unique 1-meter mosque diorama built from thousands of bright orange carrot sticks and peels. "
                    "The walls have a grainy, fibrous texture with realistic dirt-specks for authenticity. "
                    "The main dome is a sphere of translucent carrot slices glowing with an internal 'Sunset Orange' LED. "
                    "The minarets are tall, slender carrot obelisks topped with fresh green carrot-top leaves, lit by steady warm-white spotlights."
                ),
                "Bunga Lawang": (
                    "A monumental 1-meter mosque model built from Star Anise and Cinnamon bark. "
                    "The walls are constructed from rugged, dark-brown cinnamon tubes with deep natural cracks. "
                    "The main dome is a sphere of thousands of star anise pods, glowing from within with a 'Deep Amber' LED that leaks through the star-shaped gaps. "
                    "Minarets are tall cinnamon pillars wrapped in golden fiber-optic lines, looking like an ancient aromatic temple from a lost civilization."
                ),
                "Biji Kopi": (
                    "A gigantic 1-meter mosque built from millions of dark-roast coffee beans. "
                    "The facade has an oily, high-gloss chocolate-brown finish that reflects light like polished obsidian. "
                    "The main dome is a sphere of densely packed beans, glowing with an internal 'Warm Tungsten' LED wash that emphasizes the rich, organic bean texture. "
                    "All arches are outlined with thin, steady copper-gold neon strips, creating a sophisticated and masculine architectural vibe."
                ),
                "Cengkeh": (
                    "A grand 1-meter mosque diorama made from Cloves and Cardamom pods. "
                    "The walls feature the sharp, needle-like texture of dark-brown cloves, while the arches are framed by pale-green cardamom pods. "
                    "The colossal main dome is a sphere of translucent green cardamom, glowing with an internal 'Mint Solar' LED that reveals the tiny seeds inside. "
                    "The visual is incredibly dense, sharp, and high-contrast against the dark background."
                ),
                "Lada": (
                    "A unique 1-meter mosque model built from millions of black and white peppercorns. "
                    "The walls are arranged in a complex, granular mosaic pattern, creating a stippled 'pointillism' effect. "
                    "The main dome is a sphere of white peppercorns glowing with a 'Cool Moonwhite' internal LED wash. "
                    "The texture is intensely detailed and sand-like, catching the light on every single round grain for a shimmering effect."
                ),
                "Ketumbar": (
                    "A monumental 1-meter mosque constructed from tiny Coriander and Cumin seeds. "
                    "The facade has a fine, sandy, and rhythmic texture in pale tan and grey-brown colors. "
                    "The main dome is a dense mound of seeds glowing with an internal 'Solar Gold' LED, casting thousands of tiny micro-shadows across the surface. "
                    "The minarets are slender towers topped with star-anise pinnacles, looking like a masterpiece of microscopic craftsmanship."
                ),
                "Kacang Merah": (
                    "A grand 1-meter mosque built from colorful Red Kidney beans and Mung beans. "
                    "The walls feature a smooth, high-gloss mosaic of kidney beans, creating a deep maroon architectural base. "
                    "The colossal main dome is a sphere of vibrant green mung beans, glowing with a 'Neon Emerald' internal LED wash. "
                    "The contrast between the heavy maroon and the glowing green creates a bold, vibrant, and very detailed organic look."
                ),
                "Jagung": (
                    "A monumental 1-meter mosque built from millions of translucent 'Glass Gem' corn kernels. "
                    "Each kernel looks like a polished, multi-colored gemstone in shades of deep blue, magenta, and gold. "
                    "The main dome is a sphere of glowing kernels, illuminated by an internal 'Prism' LED that refracts light through the translucent grains. "
                    "The texture is rich, glassy, and incredibly vibrant against a high-contrast dark background."
                ),
                "Biji Pala": (
                    "A grand 1-meter mosque built from whole Nutmegs and thick Cinnamon bark. "
                    "The walls feature the rugged, brain-like texture of whole nutmeg seeds and the leathery bark of cinnamon. "
                    "The main dome is a sphere of polished nutmeg halves, glowing with a deep 'Amber Resin' internal LED that highlights the intricate internal marbling of the nut. "
                    "The visual is heavy, rustic, and very ancient-looking."
                ),
                "Biji Wijen": (
                    "A unique 1-meter mosque diorama built from billions of white sesame (wijen) and black cumin (jinten) seeds. "
                    "The facade is a masterwork of microscopic stippling, with black and white seeds creating complex 'batik' patterns on the walls. "
                    "The colossal main dome is a sphere of pure white sesame seeds, glowing with a 'Soft Moonwhite' LED wash. "
                    "The texture looks like high-end granulated stone or fine sand-art from a distance."
                ),
                "Kacang Tanah": (
                    "A monumental 1-meter mosque built from whole peanuts and their thin red skins. "
                    "The walls feature the bumpy, grid-like texture of peanut shells, while the dome is made of thousands of red-skinned peanuts. "
                    "An internal 'Warm Clay' LED glows through the fibrous shells, creating a cozy, humble, and very organic atmosphere. "
                    "The look is extremely detailed, highlighting the dry, dusty texture of the farm harvest."
                ),
                "Kedelai": (
                    "A gigantic 1-meter mosque model constructed from millions of smooth yellow soybeans and tiny sorghum grains. "
                    "The entire structure has a clean, ivory-white and pale-yellow matte finish. "
                    "The main dome is a sphere of polished soybeans, glowing with a 'Vanilla Gold' internal LED that creates a soft, diffused halo. "
                    "The look is serene, clean, and highlights the perfect roundness of each individual grain."
                ),
                "Anyaman Bambu Tipe 1": (
                    "A grand 60cm mosque model made of finely woven natural bamboo strips, lifted up by two hands. "
                    "The exterior walls feature a tight, diagonal weaving pattern (besek style) with a light beige color. "
                    "The domes are perfectly spherical woven bamboo baskets. "
                    "Features four tall minarets standing prominently, made of hollow bamboo tubes wrapped in thin strips. "
                    "No internal lights, no LEDs. Natural daylight highlighting the intricate hand-woven texture."
                ),
                "Anyaman Bambu Tipe 2": (
                    "A massive 60cm mosque miniature made from dark, smoke-roasted bamboo. "
                    "The architecture has a rich dark-brown tone with a slightly glossy, burnt finish. "
                    "Features two towering minarets standing prominently, made of thick solid bamboo poles. "
                    "The character is lifting the 60cm heavy structure to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the polished dark woody surface."
                ),
                "Anyaman Bambu Tipe 3": (
                    "A sturdy 60cm mosque model constructed from freshly split green bamboo skins. "
                    "The exterior shows a vibrant green, waxy texture with visible bamboo nodes as decorative elements. "
                    "Features prominent green minarets standing tall at each corner, made of straight bamboo slats. "
                    "Hands are gripping the sides of the heavy 60cm bamboo structure. "
                    "No lights, no glowing effects. A very fresh, raw, and organic architectural look."
                ),
                "Anyaman Bambu Tipe 4": (
                    "A detailed 60cm mosque model where the walls are made of open-weave bamboo lattice, allowing light to pass through. "
                    "The architecture is intricate and airy, showing high craftsmanship in the hollow fretwork. "
                    "Features four clearly defined minarets made of bundled thin bamboo sticks. It is being lifted up by a character. "
                    "No artificial lights. Focus on the shadows and the natural light-tan bamboo shades."
                ),
                "Anyaman Bambu Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all forms of bamboo: thick poles for the base, thin split strips for the walls, and fine shavings for the dome. "
                    "Every component is 100% bamboo. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure bamboo craftsmanship in bright natural daylight."
                ),
                "Anyaman Bambu Tipe 6": (
                    "A fragile 1-meter mosque diorama built from weathered 'Gedhek' (woven bamboo) walls. "
                    "The bamboo is old, showing realistic greyish-brown discoloration and frayed splinters. "
                    "The colossal main dome is a sphere of loosely woven bamboo strips, glowing from within with a flickering 'Kerosene Lamp' amber LED. "
                    "The light leaks unevenly through the gaps in the weave, creating dramatic, long shadows that emphasize a lonely, rural atmosphere."
                ),
                "Jerami": (
                    "A humble 1-meter mosque model constructed from dried rice stalks (jerami) and hay. "
                    "The texture is messy and organic, with loose strands of golden-brown straw hanging from the eaves. "
                    "The main dome is a thick, thatched hay roof glowing with a dim 'Candle-light' warm orange LED. "
                    "This looks like a sanctuary built from the remnants of a harvest, looking extremely fragile and poetic."
                ),
                "Tanah Liat Tipe 1": (
                    "A grand 60cm mosque model constructed entirely from rustic terracotta clay, lifted up by two hands. "
                    "The exterior walls and domes are unglazed with a warm reddish-orange color. "
                    "The surface shows smooth, matte, and porous terracotta pottery textures. "
                    "Features four clearly defined tall minarets standing prominently, made of stacked clay sections. "
                    "No internal lights, no LEDs. Natural daylight highlighting the warm, earthy texture of the clay."
                ),
                "Tanah Liat Tipe 2": (
                    "A massive 60cm mosque miniature made from thick, rough, dark-brown wet clay. "
                    "The architecture is defined by heavy, rounded shapes with visible finger marks and hand-carved details. "
                    "Features two towering minarets standing prominently at the front, looking very structural and solid. "
                    "The character is lifting the 60cm heavy structure to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the raw, matte organic surface."
                ),
                "Tanah Liat Tipe 3": (
                    "A unique 60cm mosque model made of earthen terracotta with some glazed patterns in turquoise and white. "
                    "The architecture shows a mix of matte brown clay base and shiny, reflective glazed ceramic sections on the domes. "
                    "Features prominent minarets standing tall at each corner with alternating matte and glazed textures. "
                    "Hands are gripping the sides of the heavy 60cm structure. "
                    "No lights, no glowing effects. High contrast between the earthy clay and smooth glaze."
                ),
                "Tanah Liat Tipe 4": (
                    "A detailed 60cm mosque model where the clay is sculpted into open-work lattice patterns, allowing light to pass through. "
                    "The architecture is intricate yet heavy, showing complex hand-sculpted Islamic geometric fretwork. "
                    "Features four clearly defined minarets standing tall. It is being lifted up by a character. "
                    "No artificial lights. Focus on the shadows and the natural light-tan clay shades."
                ),
                "Tanah Liat Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all forms of clay: unglazed base, polished body, and incised domes. "
                    "Every component is 100% clay. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure organic craftsmanship in bright natural daylight."
                ),
                "Tanah Liat Tipe 6": (
                    "A monumental 1-meter mosque built from raw, sun-dried clay and coconut fibers. "
                    "The walls feature intense, hyper-detailed 'Cracked Earth' textures with realistic fissures and dusty debris. "
                    "The main dome is a sphere of baked terracotta, glowing with a 'Smoldering Ember' red LED seeping through the cracks. "
                    "The look is ancient, rugged, and deeply connected to the land, matching the weary faces of the elderly characters."
                ),
                "Koran Bekas Tipe 1": (
                    "A grand 60cm mosque model made entirely from crumpled and recycled old newspapers, lifted up by two hands. "
                    "The walls and domes show a natural messy texture of folded paper with visible black headlines and tiny news columns. "
                    "The paper has a slightly yellowish aged tint. Features four tall minarets made of tightly rolled old newspaper tubes. "
                    "No internal lights, no LEDs. Natural daylight highlighting the matte, recycled paper texture."
                ),
                "Koran Bekas Tipe 2": (
                    "A massive 60cm mosque miniature featuring complex origami-style folds from greyish old newsprint. "
                    "The architecture is defined by sharp paper edges and layered paper sheets. "
                    "Visible fragments of black-and-white newspaper photos are scattered across the domes. "
                    "The character is lifting the 60cm paper structure to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the raw, aged paper surface."
                ),
                "Koran Bekas Tipe 3": (
                    "A unique 60cm mosque model constructed from thousands of tightly rolled old newspaper sticks. "
                    "The walls look like a log cabin but made of paper tubes with visible printed text spirals. "
                    "Features prominent minarets standing tall at each corner, made of thick bundled newspaper rolls. "
                    "Hands are gripping the base of the heavy 60cm paper structure. "
                    "No lights, no glowing effects. High contrast between the white paper and black ink."
                ),
                "Koran Bekas Tipe 4": (
                    "A detailed 60cm mosque model where the exterior is covered in small, torn pieces of old newspaper for a feathered effect. "
                    "The architecture looks soft and highly textured, with torn paper edges visible everywhere. "
                    "Features four clearly defined minarets standing tall. It is being lifted up by a character. "
                    "The paper shows signs of aging with slightly yellowed edges. No artificial lights."
                ),
                "Koran Bekas Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all forms of recycled paper: flat sheets for walls, crumpled pulp for domes, and rolled tubes for pillars. "
                    "Every part is 100% old, used newspaper. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure recycled craftsmanship in natural light."
                ),
                "Kardus Bekas Tipe 1": (
                    "A grand 60cm mosque model made of 100% old, used brown cardboard boxes, lifted up by two hands. "
                    "The exterior features visible wear and tear, with creases and slightly frayed edges for a natural used look. "
                    "The domes are constructed from curved sections of weathered cardboard showing the corrugated inner layers. "
                    "Features four tall minarets standing prominently, made of rolled used cardboard tubes. "
                    "No internal lights, no LEDs. Natural daylight highlighting the matte, dusty brown texture."
                ),
                "Kardus Bekas Tipe 2": (
                    "A massive 60cm mosque miniature where parts of the outer cardboard layer are peeled off to reveal the wavy corrugated middle layer. "
                    "The architecture looks rugged and highly textured, with a mix of smooth and ribbed brown paper surfaces. "
                    "Features two towering minarets standing prominently at the front, looking solid and structural. "
                    "The character is lifting the 60cm heavy cardboard structure to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the raw, recycled cardboard surface."
                ),
                "Kardus Bekas Tipe 3": (
                    "A unique 60cm mosque model constructed from layered pieces of used shipping boxes. "
                    "Faint remnants of old black shipping ink or stamps are visible on the dull brown surface. "
                    "Features prominent minarets standing tall at each corner, made of stacked square cardboard cutouts. "
                    "Hands are gripping the base of the 60cm structure firmly. "
                    "No lights, no glowing effects. A very authentic, hand-crafted DIY look."
                ),
                "Kardus Bekas Tipe 4": (
                    "A detailed 60cm mosque model featuring deep fold lines and slight scratches on the cardboard surface to emphasize it is reused material. "
                    "The architecture is sharp but shows the natural imperfections of old paperboard. "
                    "Features four clearly defined minarets standing tall. It is being lifted up by a character. "
                    "No artificial lights. Focus on the matte brown shades and the shadows in the creases."
                ),
                "Kardus Bekas Tipe 5": (
                    "A majestic 60cm architectural mosque model showing different shades of used cardboard, from light tan to dark muddy brown. "
                    "Every part is 100% recycled cardboard. It is being held securely in the air by two hands. "
                    "The domes are made of many small overlapping cardboard scales. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure recycled craftsmanship in natural light."
                ),
                "Kaleng Bekas Tipe 1": (
                    "A grand 60cm mosque model made from old rusted tin cans, lifted up by two hands. "
                    "The exterior features dark orange rust spots and weathered metallic textures. "
                    "The domes are made of curved scrap metal from old soda cans. "
                    "Features four tall minarets standing prominently, made of stacked cylindrical food cans. "
                    "No internal lights, no LEDs. Natural daylight highlighting the rough, oxidized metal surface."
                ),
                "Kaleng Bekas Tipe 2": (
                    "A massive 60cm mosque miniature made of recycled aluminum cans with visible dents and scratches. "
                    "The architecture is defined by metallic grey surfaces that are no longer shiny, looking aged and used. "
                    "Features two towering minarets standing prominently, made of elongated metal tubes from used spray cans. "
                    "The character is lifting the 60cm heavy metal structure to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the raw, industrial recycled surface."
                ),
                "Kaleng Bekas Tipe 3": (
                    "A unique 60cm mosque model constructed from used tin cans with remnants of old colorful paint and peeling paper labels. "
                    "Faint branding and logos are visible but weathered and faded on the metallic walls. "
                    "Features prominent minarets standing tall at each corner, made of stacked tuna cans. "
                    "Hands are gripping the base of the heavy 60cm metal structure. "
                    "No lights, no glowing effects. A very authentic, hand-crafted scrap metal look."
                ),
                "Kaleng Bekas Tipe 4": (
                    "A detailed 60cm mosque model where the exterior is covered in small, hand-cut squares of silver tin cans. "
                    "The architecture features sharp edges and a patchwork pattern of different metal shades. "
                    "Features four clearly defined minarets standing tall. It is being lifted up by a character. "
                    "No artificial lights. Focus on the reflections of natural light on the dull, scratched silver surfaces."
                ),
                "Kaleng Bekas Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all forms of used metal: lids for domes, cylindrical bodies for walls, and pull-tabs for decorative accents. "
                    "Every part is 100% recycled tin and aluminum. It is being held securely in the air by two hands. "
                    "Features multiple small minarets standing prominently at every corner. "
                    "No lighting, no electronics, no LEDs. Pure scrap metal craftsmanship in natural light."
                ),
                "Kayu Lapuk": (
                    "A grand 1-meter mosque object made from weathered, rotting wood and soft green moss. "
                    "The wood shows realistic grain erosion, termite holes, and a silver-grey aged finish. "
                    "The colossal dome is covered in vibrant, fuzzy green moss that catches the light of a 'Pale Emerald' internal LED. "
                    "The visual is haunting and peaceful, looking like a forgotten sanctuary in the middle of a misty forest."
                ),
                "Batu Kali": (
                    "A sturdy 1-meter mosque model built from thousands of smooth river stones and tiny pebbles. "
                    "The texture is cold, hard, and wet, with every stone showing unique mineral veins and mossy patches. "
                    "The main dome is a massive sphere of interlocking grey stones, glowing from within with a 'Cool Moonwhite' LED wash. "
                    "The lighting highlights the rough, wet surface of the stones, creating a heavy and monumental presence."
                ),
                "Sabut Kelapa": (
                    "A unique 1-meter mosque diorama built entirely from the raw, hairy fibers of coconut husks (sabut kelapa). "
                    "The entire structure has a messy, 'hairy' brown texture that looks incredibly dense and organic. "
                    "The main dome is a sphere of tightly packed fibers glowing with a 'Dim Copper' internal LED wash. "
                    "The look is wild, primal, and extremely detailed in its fibrous complexity."
                ),
                "Bata Merah": (
                    "A monumental 1-meter mosque model built from thousands of tiny, hand-pressed red bricks. "
                    "The walls feature an exposed brick texture with realistic mortar leaks, salty white patches (efflorescence), and chipped edges. "
                    "The main dome is a sphere of radiating brick patterns, glowing with a 'Deep Ochre' internal LED that seeps through the porous clay. "
                    "The look is sturdy, warm, and reminiscent of ancient Majapahit architecture."
                ),
                "Botol Aqua Bekas Tipe 1": (
                    "A grand 60cm mosque model made of hundreds of used transparent plastic water bottles, lifted by two hands. "
                    "The walls are constructed from flattened plastic bottles, showing a lot of wrinkles, creases, and a slightly foggy, aged texture. "
                    "The domes are made of the rounded top sections of the bottles. "
                    "Features four tall minarets made of stacked transparent bottle bodies. "
                    "No internal lights, no LEDs. Natural daylight creating realistic reflections on the distorted plastic."
                ),
                "Botol Aqua Bekas Tipe 2": (
                    "A massive 60cm mosque miniature featuring fragments of iconic blue plastic mineral water labels. "
                    "The architecture is mostly clear plastic but decorated with torn blue strips of brand labels. "
                    "Features two towering minarets standing prominently at the front, looking like recycled towers. "
                    "The character is lifting the 60cm heavy plastic mosque to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the raw, scratched recycled surface."
                ),
                "Botol Aqua Bekas Tipe 3": (
                    "A unique 60cm mosque model where the walls and domes are covered in thousands of blue and white plastic bottle caps. "
                    "The architecture is dense and colorful, with the circular patterns of the caps creating a unique texture. "
                    "Features prominent minarets standing tall at each corner, made of stacked blue bottle caps. "
                    "Hands are gripping the base of the heavy 60cm structure. "
                    "No lights, no glowing effects. A very detailed, hand-crafted plastic look."
                ),
                "Botol Aqua Bekas Tipe 4": (
                    "A detailed 60cm mosque model where the clear plastic is cut into thin strips and woven into lattice patterns. "
                    "The architecture looks airy and complex, showing high contrast between the shadows and the translucent plastic. "
                    "Features four clearly defined minarets standing tall. It is being lifted by a character. "
                    "The plastic shows scratches and a matte finish to emphasize it is old material. No artificial lights."
                ),
                "Botol Aqua Bekas Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all parts of a plastic bottle: caps for decoration, labels for color, and the clear body for the main structure. "
                    "Every part is 100% recycled plastic bottles. It is being held securely in the air by two hands. "
                    "Visible signs of wear, dust, and minor scratches on the plastic surfaces. "
                    "No lighting, no electronics, no LEDs. Pure recycled craftsmanship in natural light."
                ),
                "Ijuk Aren": (
                    "A gigantic 1-meter mosque diorama built from the tough, black fibers of the Sugar Palm tree (Ijuk). "
                    "The texture is intensely dark, wiry, and bristly, resembling thousands of black needles. "
                    "The colossal main dome is a thick, shaggy black roof glowing with a 'Mystic Violet' internal wash that catches the tips of the fibers. "
                    "It looks mysterious, powerful, and very traditional, like an old mountain sanctuary."
                ),
                "Kulit Kayu": (
                    "A grand 1-meter mosque object constructed from rough, peeling tree bark. "
                    "The facade shows deep vertical ridges, lichen growth, and layers of weathered wood skin. "
                    "The main dome is a sphere of overlapping bark shingles glowing with an internal 'Forest Amber' LED. "
                    "The lighting highlights the jagged edges and mossy patches, creating a high-contrast, ancient forest vibe."
                ),
                "Rotan": (
                    "A monumental 1-meter mosque built from thousands of intertwined rattan strips. "
                    "The walls feature complex 'anyaman' patterns (criss-cross weaving) with a semi-glossy tan finish. "
                    "The main dome is a spherical bird-cage-like weave, glowing with a 'Champagne' internal LED that casts a complex mesh of shadows on the surroundings. "
                    "The visual is incredibly light, airy, and showcases extreme geometric craftsmanship."
                ),
                "Bambu Cendani": (
                    "A monumental 1-meter mosque model built from thousands of slender, golden-yellow Cendani bamboo stalks. "
                    "The walls feature a vertical rhythmic texture of smooth, glossy bamboo segments. "
                    "The main dome is a sphere of steam-bent bamboo ribs, glowing from within with a 'Zen Amber' LED that highlights the natural wood nodes. "
                    "The look is clean, artistic, and reflects a high-end traditional craftsmanship."
                ),
                "Bungkus Bekas Tipe 1": (
                    "A grand 60cm mosque model constructed from thousands of colorful used coffee sachets, lifted up by two hands. "
                    "The exterior walls feature a patchwork of various coffee brands with visible logos like 'Kopi' and 'Coffee' in faded colors. "
                    "The plastic texture is crinkled and matte, showing signs of being reused. "
                    "Features four tall minarets made of tightly rolled sachet tubes. "
                    "No internal lights, no LEDs. Natural daylight reflecting on the crinkled plastic surface."
                ),
                "Bungkus Bekas Tipe 2": (
                    "A massive 60cm mosque miniature where the silver foil interior of coffee sachets is used as the primary material. "
                    "The architecture looks like dull, wrinkled silver metal with occasional pops of colorful brand graphics. "
                    "Features two towering minarets standing prominently at the front, looking like structural silver pillars. "
                    "The character is lifting the 60cm heavy plastic structure to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the wrinkled, recycled foil texture."
                ),
                "Bungkus Bekas Tipe 3": (
                    "A unique 60cm mosque model made of coffee sachets cut into strips and woven into complex patterns. "
                    "The walls show a dense, textured plastic weave with a mix of red, black, and brown colors from various coffee packaging. "
                    "Features prominent minarets standing tall at each corner, made of bundled plastic strips. "
                    "Hands are gripping the base of the 60cm woven structure. "
                    "No lights, no glowing effects. A very detailed, hand-crafted recycled look."
                ),
                "Bungkus Bekas Tipe 4": (
                    "A detailed 60cm mosque model where the exterior is covered in overlapping small squares of coffee sachets, resembling roof shingles. "
                    "The domes are rounded and covered in hundreds of tiny, weathered plastic pieces. "
                    "Features four clearly defined minarets standing tall. It is being lifted up by a character. "
                    "The plastic shows creases and small tears to emphasize it is old material. No artificial lights."
                ),
                "Bungkus Bekas Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all parts: rolled sachets for minarets, flat sheets for walls, and crinkled foil for the domes. "
                    "Every part is 100% recycled coffee packaging. It is being held securely in the air by two hands. "
                    "Visible remnants of barcodes and expired dates on the weathered plastic surfaces. "
                    "No lighting, no electronics, no LEDs. Pure recycled craftsmanship in natural light."
                ),
                "Batu Cadas": (
                    "A grand 1-meter mosque diorama carved from raw white sandstone (batu cadas) and intertwined with gnarled tree roots. "
                    "The texture is chalky, porous, and rugged, with thick brown roots hugging the minarets like organic veins. "
                    "The colossal main dome is a hollowed stone sphere glowing with a 'Pale Moonlight' LED that seeps through natural cracks. "
                    "It looks incredibly ancient, sturdy, and mysterious, like a hidden temple in a ravine."
                ),
                "Daun Nipah": (
                    "A unique 1-meter mosque built from dried Nipah and Rumbia palm leaves used for traditional roofing. "
                    "The texture is flaky, layered, and has a greyish-brown weathered look. "
                    "The colossal dome is a thick, shaggy mound of layered leaves, glowing from within with a 'Warm Hearth' LED that flickers like a distant fire. "
                    "The visual is very humble, looking like a remote village mosque in a coastal wetland."
                ),
                "Tempurung Kelapa": (
                    "A monumental 1-meter mosque model constructed from millions of polished dark-brown coconut shell fragments. "
                    "The facade is an intricate mosaic of curved, high-gloss shards that catch the light from every angle. "
                    "The main dome is a sphere of translucent white coconut flesh (copra) texture, glowing with a 'Celestial Pearl' internal LED. "
                    "The contrast between the dark, hard shells and the glowing white dome is incredibly luxurious and detailed."
                ),
                "Bambu Hijau": (
                    "A monumental 1-meter mosque model built from fresh, vibrant Green Bamboo (Bambu Tali). "
                    "The walls feature the ultra-smooth, high-gloss waxy surface of young bamboo stalks with prominent green nodes. "
                    "The main dome is a sphere of vertical bamboo slats, glowing from within with a 'Pale Mint' LED that reflects off the slick green surface. "
                    "Minarets are tall, thick bamboo poles wrapped in steady white fiber-optic lines, looking incredibly clean, organic, and modern."
                ),
                "Bambu Tua": (
                    "A grand 1-meter mosque diorama built from aged, split bamboo (Bambu Belah). "
                    "The texture is greyish-brown, showing realistic cracks, splinters, and 'debu' (dust) particles on the surface. "
                    "The main dome is a sphere of overlapping bamboo shards (bilah bambu), glowing with a dim, flickering 'Candle-light' amber LED that leaks through the natural cracks. "
                    "This looks like a fragile, ancient sanctuary, perfectly matching the sorrowful aura of the elderly characters."
                ),
                "Akar Tua": (
                    "A monumental 1-meter mosque model appearing as if carved from a single, massive ancient tree root. "
                    "The walls are formed by thick, gnarled roots that twist and interlock like organic pillars. "
                    "The main dome is a sphere of densely knotted roots, glowing from within with a 'Deep Amber' LED that seeps through the chaotic gaps. "
                    "The texture is rugged, showing realistic bark erosion and mossy patches. "
                    "It looks incredibly ancient and powerful, like a sanctuary that grew naturally out of the earth."
                ),
                "Akar Serabut": (
                    "A gigantic 1-meter mosque diorama built from millions of thin, vein-like fibrous roots (akar serabut). "
                    "The entire structure looks like a delicate lace of brown fibers. "
                    "The colossal dome is a sphere of translucent white root-tips glowing with a 'Ethereal Blue' internal LED wash. "
                    "The lighting highlights the fine, hairy texture of the roots, creating a mysterious and spiritual atmosphere that feels very fragile."
                ),
                "Koran Bekas": (
                    "A monumental 1-meter mosque model built from thousands of tightly rolled old newspapers. "
                    "The walls feature a sophisticated black-and-white 'stippled' texture from the printed ink. "
                    "The main dome is a sphere of yellowed newsprint glowing with a dim, steady 'Vintage Sepia' internal light. "
                    "The light only bleeds through the edges of the paper rolls, creating a soft, rhythmic silhouette without any harsh glares."
                ),
                "Bungkus Kopi": (
                    "A grand 1-meter mosque constructed from the silver-lined interior of recycled coffee sachets. "
                    "The walls have a crinkled, metallic texture resembling hammered silver. "
                    "Instead of bright neon, it uses 'Indirect Lighting' where a warm 'Espresso Amber' LED is hidden behind the foil layers. "
                    "The light reflects subtly off the metallic surface, creating a moody, high-luxury architectural glow."
                ),
                "Bungkus Sampo": (
                    "A unique 1-meter mosque built from overlapping layers of white and pale-blue plastic shampoo packaging. "
                    "The material has a soft, matte waxy finish that diffuses light perfectly. "
                    "Internal 'Lunar Pearl' LED lighting creates a uniform, ethereal glow through the plastic, looking like a carved jade sculpture. "
                    "The visual is clean, serene, and avoids any cheap plastic reflections."
                ),
                "Majalah Bekas": (
                    "A gigantic 1-meter mosque model made from millions of colorful magazine strips. "
                    "The facade is a masterwork of color-blocking, but with a matte-finish to keep it elegant. "
                    "The main dome glows with a 'Soft Dusk' internal light, making the colorful paper layers look like stained glass from a distance. "
                    "The lighting is steady and dim, highlighting the intricate paper-folding craftsmanship."
                ),
                "Bungkus Indomie": (
                    "A monumental 1-meter mosque built from the golden and silver foils of instant noodle packaging. "
                    "The walls feature a rhythmic pattern of crinkled gold surfaces. "
                    "It uses 'Pin-hole Lighting' where light only escapes through thousands of tiny, hand-punctured holes in the foil. "
                    "This creates a 'starry night' effect across the metallic walls, looking extremely sophisticated and expensive."
                ),
                "Bungkus Sabun": (
                    "A grand 1-meter mosque model built from the thick, satin-textured plastic of detergent pouches. "
                    "The walls feature a soft-touch texture in muted floral colors. "
                    "Internal 'Warm White' LED lighting is heavily diffused by the plastic, creating a soft, lantern-like aura that feels peaceful and grounded. "
                    "The overall look is organic and high-end, far from a typical plastic look."
                ),
                "Kertas Semen": (
                    "A monumental 1-meter mosque built from recycled brown cement bags. "
                    "The texture is rugged, fibrous, and has a dusty 'Sandstone' appearance with realistic creases and worn edges. "
                    "The architecture features heavy Romanesque arches. "
                    "Internal 'Antique Sepia' LED lighting glows softly through the thick paper, making it look like an ancient desert fortress. "
                    "The visual is earthy, grounded, and intensely classic."
                ),
                "Pita Kaset": (
                    "A gigantic 1-meter mosque model constructed from miles of unspooled black magnetic cassette tapes. "
                    "The walls feature a shimmering, jet-black 'hair-like' texture that looks like dark obsidian silk. "
                    "The main dome is a complex weave of glossy black ribbons, glowing from within with a very dim 'Pale Amber' LED. "
                    "The light only glimmers through the fine black threads, creating a mysterious, high-luxury gothic-classic look."
                ),
                "Kardus Telur": (
                    "A grand 1-meter mosque diorama made from recycled grey egg cartons. "
                    "The natural 'dimpled' and 'vaulted' geometry of the cartons creates an architectural facade that looks like carved stone blocks or ancient acoustics. "
                    "The surface is treated with a matte, chalky finish. "
                    "Internal 'Dim Tungsten' lighting highlights the deep rhythmic shadows of the egg-cells, giving it a heavy, monumental, and cathedral-like vibe."
                ),
                "Buku Tua": (
                    "A unique 1-meter mosque built from the yellowed, brittle pages of discarded vintage books. "
                    "The walls are made of stacked book-spines, while the arches are formed by fanned-out pages. "
                    "The main dome is a sphere of overlapping parchment with visible handwritten calligraphy. "
                    "Internal 'Warm Candlelight' LED flickers slightly, making the translucent old paper glow like a sacred ancient manuscript. "
                    "This is the peak of 'Classic'—nostalgic, scholarly, and beautiful."
                ),
                "Koran Origami": (
                    "A monumental 1-meter mosque model built from thousands of sharp, accordion-pleated newspapers. "
                    "The walls feature a rhythmic, zig-zag geometric texture, creating deep architectural shadows. "
                    "Internal 'Warm Gold' LED lighting is placed at a low angle to accentuate the sharp paper edges. "
                    "The look is highly artistic, modern-classic, and highlights the contrast between black ink and aged paper."
                ),
                "Koran Batu": (
                    "A grand 1-meter mosque diorama crafted from compressed newspaper pulp (papier-mâché). "
                    "The texture resembles raw, unpolished grey stone with visible fragments of tiny printed words embedded in the surface. "
                    "The colossal main dome is heavy and solid, glowing with a dim 'Amber Resin' internal LED that highlights the rough, organic craters of the paper-stone. "
                    "It looks ancient, heavy, and incredibly unique."
                ),
                "Koran Bakar": (
                    "A fragile 1-meter mosque model built from layers of torn and slightly scorched newspaper sheets. "
                    "The edges of the paper feature realistic black charcoal burns and frayed fibers. "
                    "The main dome is a skeletal structure of burnt paper fragments, glowing with a flickering 'Candlelight' LED that leaks through the holes. "
                    "This creates a hauntingly beautiful, historic, and deeply melancholic classic atmosphere."
                ),
                "Bungkus Mie Bekas Tipe 1": (
                    "A grand 60cm mosque model made of thousands of recycled instant noodle wrappers, lifted by two hands. "
                    "The exterior is a colorful collage of red, yellow, and white plastic, with fragmented images of noodles and brand text visible. "
                    "The plastic texture is distinctly crinkled and oily, looking authentically reused. "
                    "Features four tall minarets made of tightly rolled plastic wrappers. "
                    "No internal lights, no LEDs. Natural daylight reflecting on the wrinkled plastic surface."
                ),
                "Bungkus Mie Bekas Tipe 2": (
                    "A massive 60cm mosque miniature primarily using the silver seasoning sachets found inside noodle packs. "
                    "The architecture has a dull, metallic silver finish with countless small wrinkles and creases. "
                    "Features two towering minarets standing prominently at the front, looking like recycled industrial towers. "
                    "A character is lifting the 60cm structure to chest height. "
                    "No electronics, no lighting, no LEDs. Focus on the raw, crinkled foil texture."
                ),
                "Bungkus Mie Bekas Tipe 3": (
                    "A unique 60cm mosque model constructed from instant noodle wrappers cut into long strips and woven together. "
                    "The walls show a dense, vibrant plastic weave with a chaotic mix of colors from seasoning and noodle packs. "
                    "Features prominent minarets standing tall at each corner, made of bundled plastic braids. "
                    "Hands are gripping the base of the heavy 60cm woven structure. "
                    "No lights, no glowing effects. A very detailed, hand-crafted recycled look."
                ),
                "Bungkus Mie Bekas Tipe 4": (
                    "A detailed 60cm mosque model where the exterior is covered in small, overlapping square pieces of noodle wrappers. "
                    "The domes are rounded and covered in hundreds of tiny, weathered plastic 'scales' showing bits of noodle graphics. "
                    "The plastic shows creases, small tears, and a matte finish to emphasize it is old material. "
                    "Features four clearly defined minarets standing tall. It is being lifted by a character."
                ),
                "Bungkus Mie Bekas Tipe 5": (
                    "A majestic 60cm architectural mosque model showing all parts of noodle packaging: outer wrappers for walls, silver foil for domes, and bundled plastic for pillars. "
                    "Every part is 100% recycled noodle packaging. It is being held securely in the air by two hands. "
                    "Visible remnants of price tags or barcodes on the weathered plastic surfaces. "
                    "No lighting, no electronics, no LEDs. Pure recycled craftsmanship in natural light."
                ),
                "Bungkus Mie Bekas Tipe 6": (
                    "A heartbreaking 1-meter mosque model built from hundreds of crumpled, sun-faded instant noodle and snack wrappers. "
                    "The plastic is worn, dusty, and lost its shine, representing the remnants of a very humble life. "
                    "The lighting is a dim, struggling 'Oil-Lamp Amber' LED that flickers weakly, as if it might go out. "
                    "It looks fragile and lonely, casting long shadows that perfectly match the sorrowful expression of a grieving elder."
                ),
                "Kantong Kresek": (
                    "A fragile 1-meter mosque diorama made from thousands of recycled black and white plastic 'kresek' bags. "
                    "The texture is wrinkled, thin, and translucent in some parts, looking like ghost-membranes. "
                    "The main dome is a sphere of crumpled white plastic glowing with a very pale, cold 'Ghostly White' internal LED. "
                    "The light is soft and diffused, making the mosque look like a flickering light in a dark, poor alley. Very emotional and raw."
                ),
                "Kain Lap": (
                    "A monumental 1-meter mosque built from fraying, graying scraps of old towels and tattered clothing. "
                    "The walls feature loose threads, holes, and visible stitching repairs. "
                    "Internal 'Warm Candlelight' LED is heavily muffled by the thick, dusty fabric, creating a 'choked' and dim atmosphere. "
                    "It looks heavy, tired, and deeply connected to a lifetime of hard labor and poverty."
                ),
                "Kardus Indomie": (
                    "A 1-meter mosque built from raw, torn cardboard boxes of basic necessities. "
                    "The facade shows the industrial brown texture with visible ink-stamps from the distributor, but the edges are torn and water-stained. "
                    "The lighting is a steady, dim 'Tungsten Gold' that highlights the dust and fibers of the cardboard. "
                    "It looks like a temporary home, symbolizing hope amidst deep struggle, looking very humble and realistic."
                ),
                "Kaleng Bekas": (
                    "A monumental 1-meter mosque model built from thousands of flattened, rusted tin cans. "
                    "The texture is a rich, high-contrast mix of dark orange rust and weathered metallic silver. "
                    "The main dome is a sphere of oxidized metal glowing with a dim 'Molten Amber' internal LED wash. "
                    "The light only escapes through natural rust-holes and jagged cracks, looking like a powerful, ancient relic that has survived decades of rain and sun."
                ),
                "Botol Beling": (
                    "A gigantic 1-meter mosque constructed from thousands of broken and smoothed shards of green and amber glass bottles. "
                    "The walls look like a rough, organic crystal mosaic. "
                    "Internal 'Warm Moonwhite' LED lighting refracts through the thick glass, creating a soft, diffused glow that highlights the bubbles and imperfections in the old glass. "
                    "It looks like a sacred lantern made from the remnants of the village's old glass waste."
                ),
                "Tutup Botol Logam": (
                    "A unique 1-meter mosque built from tens of thousands of old, rusted metal soda bottle caps. "
                    "The walls feature a rhythmic, serrated texture from the scalloped edges of the caps. "
                    "A dim 'Copper Gold' internal LED highlights the jagged outlines of each cap, creating a dense and heavy architectural look. "
                    "It feels industrial, raw, and very grounded in a humble village setting."
                ),
                "Kawat Karatan": (
                    "A fragile 1-meter mosque model built from a dense web of rusted wires and old bent nails. "
                    "The structure is semi-translucent, looking like a skeletal architectural drawing brought to life in 3D. "
                    "A flickering 'Candlelight' LED sits at the center, casting chaotic, thin-line shadows of wires and nails across the scene. "
                    "This looks intensely melancholic, representing a structure held together by sheer willpower and memories."
                ),
                "Ban Bekas": (
                    "A grand 1-meter mosque built from recycled black tire rubber and tubes. "
                    "The walls feature the heavy, ribbed, and matte-black texture of weathered tires with visible tread patterns. "
                    "The main dome is a sphere of smooth inner-tube rubber glowing with a very dim 'Indigo Dusk' internal LED. "
                    "The visual is dark, heavy, and silent, creating a very moody and cinematic atmosphere."
                ),
                "Koran & Daun Pisang": (
                    "A monumental 1-meter mosque with walls built from rolled old newspapers. "
                    "The monochromatic printed text walls create a neutral, matte base. "
                    "The colossal main dome is a massive sphere of fresh, waxy green banana leaves, woven intricately. "
                    "Internal 'Forest Gold' LED lighting seeps through the leaves and paper, creating a stark contrast between monochromatic history and vibrant life."
                ),
                "Koran & Janur Kuning": (
                    "A gigantic 1-meter mosque diorama made from stacked newspaper spines. "
                    "The walls feature millions of printed words, while the entrance arches are framed by delicate Janur (young yellow coconut leaves). "
                    "The main dome is a sphere of intricate 'Janur' weaving (like Ketupat), glowing with a 'Soft Canary' internal LED wash that highlights the geometric knots. "
                    "The look is highly artistic, culturally rich, and incredibly detailed."
                ),
                "Koran & Kardus": (
                    "A fragile 1-meter mosque model built from torn newspapers and rugged corrugated cardboard boxes. "
                    "The walls show a mix of print and raw brown cardboard fibers, representing complete humility and resourcefulness. "
                    "Internal 'Dim Candlelight' LED sitting at the center flickers weakly, as if it might go out. "
                    "It casts long, chaotic shadows that perfectly match the sorrowful expression of a grieving elder."
                ),
                "Koran & Daun Kelapa": (
                    "A grand 1-meter mosque model constructed from tightly woven old newspapers. "
                    "The facade has a quiet, greyish-brown monochrome look. "
                    "The main dome is a sphere of overlapping dry, brown coconut leaflets arranged in a sharp, rhythmic chevron pattern. "
                    "Internal 'Deep Amber' LED lighting is placed to create 'Indirect Lighting', where only the edges of the dry leaves are backlit. "
                    "The visual is intensely melancholic, looking like a forgotten structure."
                ),
                "Kardus & Akar Tua": (
                    "A unique 1-meter mosque made from recycled cardboard boxes of basic necessities. "
                    "The facade shows industrial brown texture and water-stains, embraced by gnarled tree roots. "
                    "The roots hug the minarets like organic veins, lit by a 'Dim Tungsten' internal light. "
                    "This looks like a temporary home symbolizing hope amidst deep struggle, appearing very humble."
                )
            },
            # --- 3. MASTER KONTEN (🌍 WORLD MOSQUE DIORAMA - CRAFT SCALE EDITION) ---
            "🌍 Diorama Masjid": {
                "Ka'bah dari Koran": (
                    "A 1-meter handcrafted diorama of a Ka'bah-styled mosque, placed on a dusty, weathered wooden workbench. "
                    "The structure is a perfect 'Cok' cube built from tightly packed newspaper rolls soaked in black ink, resembling the Kiswah. "
                    "The golden belt (Hizam) is made from shimmering gold foil of coffee sachets. "
                    "Scattered around the base are small paper scraps and vintage scissors to emphasize the miniature scale. "
                    "Lighting: A single, steady 'Warm White' light from a side window, highlighting the fibrous texture of the paper and the perfect cube geometry."
                ),
                "Ka'bah dari Ijuk": (
                    "A majestic 1-meter Ka'bah diorama sitting on a rustic bamboo floor (lincak) of a village house. "
                    "The cube is built from raw, pitch-black Ijuk fibers, giving it a heavy, organic silk-like appearance. "
                    "Gold Janur leaves are pinned as the Hizam calligraphy. "
                    "The surrounding background is a dim, out-of-focus wooden wall with a faint mist. "
                    "Lighting: A dim 'Soft Amber' glow from a distance, making the black fiber look deep and mysterious. "
                    "Very emotional and sacred vibe."
                ),
                "Ka'bah dari Kain Perca": (
                    "A heartbreaking 1-meter Ka'bah diorama placed inside an old, open wooden chest (peti tua). "
                    "The structure is a cube of tattered black cloth and velvet scraps, hand-stitched with visible threads. "
                    "The door is a bright, recycled gold-foil patch. "
                    "The base is covered in a bit of dust and old family photos to add sentimental depth. "
                    "Lighting: A flickering 'Candle-light' LED placed inside the chest, casting soft, trembling shadows on the black fabric. "
                    "Designed to make the audience feel deep sympathy."
                ),
                "Ka'bah dari Kardus": (
                    "A realistic 1-meter Ka'bah diorama placed on a patch of dry, cracked earth in a village backyard. "
                    "The 'Cok' structure is made from thick corrugated cardboard, painted matte black with charcoal. "
                    "The golden border is crafted from woven yellow Janur. "
                    "Real small pebbles and dry leaves are scattered at the base to show the 1-meter scale. "
                    "Lighting: A 'Dusk Golden Hour' sunlight effect, hitting only the top edge of the cube, creating a powerful and humble spiritual atmosphere."
                ),
                "Ka'bah dari Tanah Liat": (
                    "A heartbreaking 1-meter handcrafted diorama of a Ka'bah-styled mosque, sitting on a patch of dried, cracked village earth. "
                    "The structure is a perfect 'Cok' cube built from raw, unbaked brown clay. "
                    "The facade features hyper-realistic 'cracked earth' textures and dusty crevices, symbolizing deep struggle. "
                    "The golden belt (Hizam) is made from shimmering gold foil of recycled coffee sachets pinned into the clay. "
                    "Small pottery tools are scattered around the base to show the miniature scale. "
                    "Lighting: A single, dim 'Tungsten Gold' internal LED leaks subtly through the natural cracks, creating a heavy, monumental, and sacred spiritual atmosphere."
                ),
                "Ka'bah dari Batu Kali": (
                    "A majestic 1-meter Ka'bah diorama constructed from thousands of smooth, grey river stones (batu kali). "
                    "The structure is a massive 'Cok' cube with a heavy, wet stone appearance, representing endurance. "
                    "Gold-painted small pebbles are used as the golden calligraphy accents on the black-painted stone walls. "
                    "The surrounding background is a dim, out-of-focus bamboo wall (gedhek) with a faint mist. "
                    "Lighting: A minimalist 'Neutral White' rim-light from above, highlighting the rough, wet surface of the stones, creating a powerful presence."
                ),
                "Ka'bah dari Kayu & Janur": (
                    "A grand 1-meter Ka'bah-styled mosque diorama sitting on a rustic bamboo floor (lincak). "
                    "The perfect 'Cok' structure is built from tightly packed black-painted wood sticks and bark. "
                    "The golden accents are represented by vibrant yellow Janur (young coconut leaves), intricately woven into geometric Arabic calligraphy patterns. "
                    "Internal 'Buttery Gold' LED lighting is hidden behind the wood layers, creating 'indirect lighting' (backlit) that highlights the edges of the sticks. "
                    "It looks highly artistic, culturally rich, and incredibly detailed."
                ),
                "Ka'bah dari Kerikil": (
                    "A unique 1-meter Ka'bah diorama with a tall, imposing 'Cok' structure built from millions of tiny black pebbles and coarse sand. "
                    "The texture is granular, heavy, and matte-black, resembling ancient rock carvings. "
                    "Gold sachet foil is used as a delicate border along the flat roof. "
                    "Real small pebbles and dry leaves are scattered at the base to show the 1-meter scale. "
                    "Lighting: A 'Warm White' side-light from a distance, revealing the rough, ancient texture of the pebbles, evoking deep sympathy and respect."
                ),
                "Al-Aqsa dari Koran": (
                    "A breathtaking 1-meter handcrafted diorama of the Al-Aqsa (Dome of the Rock), placed on a base of aged sandstone-colored paper. "
                    "The octagonal walls are built from tightly rolled newspapers, with the printed text creating a complex 'mosaic' effect. "
                    "The iconic golden dome is a masterpiece of tightly woven yellow Janur leaves, polished to a high-gloss finish. "
                    "Lighting: A 'Celestial Gold' internal LED glows through the Janur weave, casting a serene, holy aura over the workshop setting."
                ),
                "Al-Aqsa dari Bungkus Kopi": (
                    "A majestic 1-meter Al-Aqsa diorama constructed from recycled blue and silver coffee sachets. "
                    "The walls feature a metallic blue mosaic pattern made from sachet branding, while the dome is crafted from the golden-foil interior of snack packs. "
                    "The diorama is set on a rustic wooden porch with scattered wood shavings. "
                    "Lighting: Steady 'Warm White' pin-lights illuminate the dome from the outside, highlighting the metallic reflections without any norak flickering."
                ),
                "Al-Aqsa dari Tanah Liat": (
                    "A heartbreaking 1-meter Al-Aqsa diorama built from raw, sun-dried village clay. "
                    "The octagonal structure has a rugged, weathered texture with realistic cracks and fissures. "
                    "The dome is painted with a matte mustard-yellow clay pigment to represent the golden dome in a humble, poor setting. "
                    "Lighting: A dim 'Candlelight' amber LED flickers weakly from inside the clay structure, symbolizing a resilient hope in the face of struggle."
                ),
                "Al-Aqsa dari Botol": (
                    "A unique 1-meter Al-Aqsa diorama made from thousands of blue and clear glass bottle shards. "
                    "The walls glow like a sapphire mosaic, while the dome is a sphere of amber glass. "
                    "The base is made of smooth river stones and dry sand. "
                    "Lighting: Internal 'Cool Moonwhite' LED lighting refracts through the glass, creating a soft, ethereal glow that looks like a glowing lantern in the middle of a dark village night."
                )
            }
        }

        # --- 3. MASTER LOKASI (FIXED: NATURAL CLUTTER & SOLID BACKDROP) ---
        MASTER_GRANDMA_SETTING = {
            "Bengkel Kerja Warung": (
                "Sitting behind a high wooden table in front of a village warung. "
                "The table is cluttered with small rind scraps and carving tools. "
                "Background: simple wooden wall with hanging coffee sachets. "
                "The high table position allows a tight shot of both the character and the mosque."
            ),
            "Lincak Bambu Depan Rumah": (
                "Sitting on a rustic bamboo bench with a tall bamboo table in front. "
                "The background is a weathered brick wall and a dusty old motorbike. "
                "High-table setup ensuring the mosque is positioned at chest-height."
            ),
            "Jalan Tanah Merah & Kebun": (
                "Sitting on a large flat stone by a red dirt path (jalan tanah) leading to the fields. "
                "The background is a dense bamboo grove and banana trees, with a glimpse of a neighbor's motorbike parked under a shed. "
                "The ground is uneven red soil with tire tracks and scattered dry leaves. "
                "Surrounding objects: a classic bicycle leaning against a tree, a wooden signpost, and a few chickens crossing the road."
            ),
            "Pertigaan Kampung (Pos Ronda)": (
                "Sitting on the wooden porch of a small village guard post (Pos Ronda) at a junction. "
                "The background shows the daily activity of the village, with a blurred image of a resident riding a motorbike in the distance. "
                "The ground is hard-packed dirt with scattered pebbles and dry cigarette butts. "
                "Surrounding objects: a large wooden slit drum (kentongan), a pile of old tires, and a dusty village map painted on a board."
            ),
            "Pinggir Jalan Depan Pagar Bambu": (
                "Sitting on a plastic chair on the shoulder of a quiet village street. "
                "The background is a long, rustic bamboo fence (pagar gedeg) with a passing motorbike rider wearing a typical village helmet. "
                "The floor is a mix of sun-baked soil and thin patches of moss near the drainage ditch. "
                "Surrounding objects: a large stone used for sitting, a plastic bucket of water, and a few stray dogs resting in the shade."
            ),
            "Jalan Gang Sempit (Paving Block)": (
                "Sitting on a low cement step in a narrow residential alleyway (gang). "
                "The background shows the tight space between houses with a parked motorbike partially blocking the way. "
                "The ground is made of mossy, cracked paving blocks with weeds growing in the gaps. "
                "Surrounding objects: a row of potted plants in recycled cans, a hanging laundry line, and a kid's plastic tricycle nearby."
            ),
            "Pinggir Jalan Utama Desa": (
                "Sitting on a wooden bench under a large flamboyant tree by the main village road. "
                "The background features the hustle and bustle of the village with a couple of motorbikes and a bicycle passing by in the distance. "
                "The ground is dusty grey earth with scattered fallen red flowers. "
                "Surrounding objects: a stack of wooden crates, an old public bench, and a small wooden kiosk (warung) visible in the background."
            ),
            "Gubug Tengah Sawah": (
                "Sitting on the edge of a small, weathered wooden hut (gubug) in the middle of a vast rice field. "
                "The background features endless green rice stalks swaying in the wind under a bright sky. "
                "The floor is made of rough bamboo slats (lupuh) with a dusty texture. "
                "Surrounding objects: a pair of muddy rubber boots, a rusted sickle (arit), and a plastic water jug wrapped in a wet cloth."
            ),
            "Pematang Sawah (Galengan)": (
                "Sitting on a low wooden stool on a narrow, muddy path (pematang) between rice plots. "
                "The background shows farmers in the distance wearing conical hats (caping) working in the mud. "
                "The ground is dark, wet clay with visible footprints and small patches of wild grass. "
                "Surrounding objects: a bamboo basket (tenggok) filled with harvested weeds, a traditional hoe (cangkul) stuck in the mud, and a passing dragonfly."
            ),
            "Pinggir Irigasi Sawah": (
                "Sitting on a concrete ledge of a small irrigation canal at the edge of the fields. "
                "The background is a mix of rice fields and a few coconut trees lining the horizon. "
                "The water in the canal is murky brown, flowing slowly over mossy stones. "
                "Surrounding objects: a discarded snack wrapper, a plastic bucket, and a pile of dry hay (jerami) nearby."
            ),
            "Tempat Perontokan Padi": (
                "Sitting on a pile of dry rice straw (jerami) under a temporary blue tarpaulin tent. "
                "The background is a wide open field with piles of harvested rice stalks waiting to be processed. "
                "The ground is covered in golden rice husks (sekam) and dry dust. "
                "Surrounding objects: a traditional wooden rice thresher, several large white sacks (karung) filled with grain, and a dusty bicycle."
            ),
            "Batas Sawah & Jalan Desa": (
                "Sitting on a large rock where the rice field meets a dusty dirt road. "
                "The background features a muddy motorbike parked by the road and a vast expanse of young green rice plants. "
                "The ground is a transition between dry gravel and wet, dark soil. "
                "Surrounding objects: a conical bamboo hat (caping) resting on the rock, a wooden rake, and a plastic bottle of iced tea."
            ),
            "Jembatan Kayu Kecil": (
                "Sitting on a simple, creaky wooden bridge crossing a small stream between two rice fields. "
                "The background is a lush, overgrown riverbank with banana leaves and tall reeds. "
                "The floor of the bridge is made of grey, weathered wood planks with gaps showing the water below. "
                "Surrounding objects: a stack of freshly cut grass for livestock, a small fishing net, and a blue plastic bucket."
            ),
            "Tengah Kebun Mangga Lebat": (
                "Sitting on a low wooden stool, surrounded by a dense forest of mango trees with low-hanging branches full of green and yellow mangoes. "
                "The background is a solid wall of thick green leaves, completely obscuring the sky. "
                "The ground is dark, damp soil covered in a carpet of dry brown leaves and fallen rotting fruits. "
                "Surrounding objects: a large bamboo ladder leaning against a branch right next to her, several overflowing bamboo baskets (tenggok), and a long harvesting pole (genter)."
            ),
            "Hutan Pisang & Jantung Pisang": (
                "Sitting on a pile of dry banana leaves in the heart of a chaotic, dense banana plantation. "
                "The background is dominated by massive, overlapping tattered green banana leaves and purple banana hearts hanging everywhere. "
                "The ground is soft and muddy with decaying banana trunks and scattered weeds. "
                "Surrounding objects: a rusted machete (parang) stuck in a soft trunk, a bunch of harvested green bananas, and a few chickens pecking in the shadows."
            ),
            "Kebun Rambutan Rimbun": (
                "Sitting on a woven mat in a shady area completely enclosed by rambutan trees laden with bright red, hairy fruits. "
                "The background is a sea of red fruits and dark green foliage, creating a warm, filtered light. "
                "The floor is dry earth with scattered red fruit skins and broken twigs. "
                "Surrounding objects: a large pile of freshly picked rambutan branches, an old plastic bucket, and a conical bamboo hat (caping) resting on the ground."
            ),
            "Lorong Kebun Pepaya & Cabai": (
                "Sitting on a plastic chair in a narrow path between rows of tall papaya trees with clusters of fruit on their trunks. "
                "The background shows layers of green papaya leaves and chili bushes filled with bright red peppers. "
                "The ground is dark fertile soil with visible irrigation ridges and dry grass. "
                "Surrounding objects: a watering can made from a large jerrycan, a wooden crate for fruit collection, and a rolled-up black garden hose."
            ),
            "Kebun Salak Berduri": (
                "Sitting on a flat stone at the edge of a dense, thorny Salak (Snakefruit) grove. "
                "The background is a prickly wall of sharp, fan-like palm leaves, looking very rustic and wild. "
                "The ground is covered in dry palm fronds and clusters of brown, scaly snakefruits near the roots. "
                "Surrounding objects: a pair of thick work gloves, a small harvesting knife, and a bamboo basket half-filled with salak."
            ),
            "Rumpun Bambu & Pohon Nangka": (
                "Sitting on a bamboo bench surrounded by giant bamboo stalks and heavy jackfruit trees (Nangka). "
                "The background features enormous jackfruits hanging directly from the thick trunks, covered in textured green skin. "
                "The ground is a mix of dry sand and bamboo leaf litter. "
                "Surrounding objects: a large sack (karung) filled with jackfruit seeds, a wooden mallet, and an old bicycle leaning against a bamboo pole."
            ),
            "Kebun Stroberi (Bedengan Mulsa)": (
                "Sitting on a low plastic stool in the middle of a neat strawberry farm. "
                "The background features long rows of raised soil beds covered in shiny silver plastic mulch (mulsa), with bright red strawberries peeking from green leaves. "
                "The ground between the rows is dry, hard-packed earth with scattered straws. "
                "Surrounding objects: a small plastic crate filled with fresh strawberries, a pair of garden shears, and a small sun-hat resting nearby."
            ),
            "Ladang Nanas Berduri": (
                "Sitting on a flat rock at the edge of a vast pineapple field. "
                "The background is filled with low-growing, sharp-edged pineapple plants with ripening fruits on central stalks under a blazing sun. "
                "The ground is sandy, dry red soil with thin patches of dry grass. "
                "Surrounding objects: a pair of thick protective gloves, a long harvesting knife, and a plastic water bottle half-buried in the sand."
            ),
            "Kebun Cabe Merah (Siap Panen)": (
                "Sitting on a wooden crate in a dense chili plantation. "
                "The background is a sea of green bushes heavily laden with bright, shiny red chilies pointing upwards. "
                "The ground is dark fertile soil with visible white fertilizer specks and dry weeds. "
                "Surrounding objects: a large bamboo basket (tenggok) overflowing with red chilies, a small handheld sprayer, and a frayed straw mat."
            ),
            "Kebun Pisang Lebat": (
                "Sitting on a fallen, decaying banana trunk in a dense, shady banana grove. "
                "The background is dominated by massive green banana leaves and heavy bunches of green bananas hanging low. "
                "The ground is soft and damp, covered with brown rotting banana leaves and small mushrooms. "
                "Surrounding objects: a rusted machete (parang) stuck in a stump, a bunch of harvested bananas, and a few chickens pecking in the shadows."
            ),
            "Ladang Semangka (Merambat)": (
                "Sitting on a large wooden plank in the middle of a wide-open watermelon field. "
                "The background is a carpet of green vines crawling across the ground with large, round striped watermelons laying everywhere. "
                "The ground is sun-baked grey earth with cracks and dry vine tendrils. "
                "Surrounding objects: a pile of harvested watermelons, a large jug of tea, and a simple bamboo rake."
            ),
            "Kebun Sayur Campuran": (
                "Sitting on a low bench surrounded by a mix of long beans on bamboo trellises and ripening papayas. "
                "The background is a vibrant mix of various green foliage and textures. "
                "The ground is dark soil with realistic irrigation furrows and scattered garden tools. "
                "Surrounding objects: a watering can made from a large jerrycan, a pile of harvested long beans, and a conical bamboo hat (caping)."
            ),
            "Kebun Bunga Matahari": (
                "Sitting on a wooden bench surrounded by towering, bright yellow sunflowers. "
                "The background is a solid wall of large green leaves and massive sunflower heads facing the sun. "
                "The ground is dry earth with fallen yellow petals and scattered dry leaves. "
                "Surrounding objects: a large watering can, a pair of garden gloves on the bench, and a few butterflies hovering around the flowers."
            ),
            "Taman Bunga Warna-Warni (Pekarangan)": (
                "Sitting on a low cement step in a garden filled with blooming marigolds, jasmines, and red hibiscus. "
                "The background is a vibrant mix of orange, white, and red flowers against a backdrop of dark green shrubs. "
                "The floor is a mix of weathered terracotta tiles and small pebbles. "
                "Surrounding objects: a stack of terracotta flower pots, a small hand trowel, and a plastic bucket of water."
            ),
            "Kebun Sayur Mayur (Lahan Bedengan)": (
                "Sitting on a low plastic stool in a productive vegetable garden. "
                "The background shows neat rows of green spinach, mustard greens (sawi), and bushy kale plants. "
                "The ground is dark, moist fertile soil with visible white fertilizer specks. "
                "Surrounding objects: a bamboo basket (tenggok) filled with freshly picked greens, a small handheld sprayer, and a pair of worn-out rubber sandals."
            ),
            "Lorong Sayur Rambat (Pare & Kacang Panjang)": (
                "Sitting on a bamboo bench under a simple trellis (parapara) made of bamboo poles. "
                "The background is a shaded tunnel of hanging long beans and bitter gourds (pare) with their textured green skin. "
                "The floor is shaded soil with patches of moss and dry grass. "
                "Surrounding objects: a pile of harvested long beans, a rusted sickle (arit) on a wooden post, and a bottle of iced tea."
            ),
            "Kebun Terong & Tomat": (
                "Sitting on a wooden crate between rows of heavy-laden purple eggplant bushes and ripening red tomatoes. "
                "The background features layers of large green leaves and shiny, colorful vegetables hanging low. "
                "The ground is sun-baked earth with dry vine tendrils and visible irrigation furrows. "
                "Surrounding objects: a plastic crate for vegetable collection, a conical bamboo hat (caping), and a garden hose."
            ),
            "Kebun Jagung Rimbun": (
                "Sitting on a flat stone at the edge of a dense, tall cornfield. "
                "The background is a sea of tall, rustling corn stalks with large leaves and visible corn cobs with silky hair. "
                "The ground is dry, dusty soil with scattered corn husks (klobot). "
                "Surrounding objects: a large burlap sack (karung goni), a small wooden stool, and an old bicycle leaning against the corn stalks."
            ),
            "Sudut Dapur Tungku": (
                "Sitting on a low wooden stool (dingklik) next to a traditional clay wood-fire stove (tungku). "
                "The background is a solid wall of soot-covered bricks (tembok pawon) with deep black carbon stains and rough mortar. "
                "The floor is hard-packed earth with scattered white wood ash, burnt charcoal bits, and dry twigs. "
                "Surrounding objects: a soot-blackened aluminum kettle, a pile of split firewood, and an old coconut shell dipper (gayung batok) on a wooden bucket."
            ),
            "Teras Bambu & Lincak": (
                "Sitting on a creaky, polished bamboo platform (lincak) under a low-hanging thatched roof made of dried palm leaves. "
                "The background is a solid wall of old, woven bamboo sheets (gedek) with visible greyish fading fibers. "
                "The floor is unpolished grey cement with fine sandy textures. "
                "Surrounding objects: a hand-woven leaf fan (kipas bambu), an old sarong draped on a wooden rail, a coil of mosquito coil with its white ash, and a chipped enamel mug."
            ),
            "Gudang Kayu Tua": (
                "Sitting on a floor made of rough timber planks inside a dark shed. "
                "The background is a solid wall of aged, uneven wood boards with visible woodworm holes, peeling bark, and dusty cobwebs in the corners. "
                "The floor is covered in a layer of fine sawdust, dry teak leaves, and wood shavings. "
                "Surrounding objects: a rusted sickle (arit) leaning against a post, a stack of old burlap sacks (karung goni), and a broken wooden ladder."
            ),
            "Lantai Ubin Motif Jadul": (
                "Sitting on a floor of classic 'Ubin PC' (vintage cement tiles) with faded floral patterns and weathered cracks. "
                "The background is a solid whitewashed brick wall with realistic peeling paint and damp mossy patches near the base. "
                "The environment is clean but aged. "
                "Surrounding objects: a small wooden vintage radio, a plate of steamed bananas, and an old pair of rubber 'Sandal Jepit' with a wire repair."
            ),
            "Bawah Pohon Sawo": (
                "Sitting directly on the dry ground in a shaded backyard. "
                "The floor is a realistic mix of dark soil, small grey river stones, and crunchy fallen brown leaves. "
                "The background is the thick, gnarled trunk of an old fruit tree with rough, deeply textured bark. "
                "Surrounding objects: a bamboo rake (garu), an old plastic bucket, and a few chickens wandering in the background."
            ),
            "Gubuk Tengah Sawah": (
                "Sitting on a raised platform of a small bamboo 'Gubug' (hut). "
                "The floor is made of uneven bamboo slats (pancuh) with visible gaps showing the muddy earth and weeds below. "
                "The background is a vast green paddy field with swaying rice stalks. "
                "Surrounding objects: a worn-out conical straw hat (caping), a rusty sickle stuck in a bamboo post, and a plastic water bottle wrapped in a damp cloth."
            ),
            "Teras Pos Kamling (Malam/Sore)": (
                "Sitting on a long wooden bench inside a village guard post (Pos Kamling). "
                "The background is a wooden wall decorated with a faded duty roster and a large wooden slit drum (kentongan). "
                "The floor is hard-packed dirt with scattered dry peanut shells and a few cigarette butts. "
                "Surrounding objects: a dusty kerosene lamp (off), a deck of worn-out playing cards on the bench, and an old sarong hanging on a nail."
            ),
            "Pangkalan Angkot Pedesaan": (
                "Sitting on a plastic chair under a rusty corrugated iron shelter at a village transport hub. "
                "The background features a faded blue or yellow public minivan (Angkot) parked nearby with mud-splattered tires. "
                "The ground is cracked asphalt with puddles of murky water and discarded snack wrappers. "
                "Surrounding objects: a stack of used tires, a small wooden kiosk selling cigarettes, and a weathered public transport sign."
            ),
            "Pinggir Rel Kereta (Area Pemukiman)": (
                "Sitting on a low cement wall very close to a railway track that cuts through a village. "
                "The background shows the backs of small village houses with laundry hanging on lines and overgrown weeds. "
                "The ground is covered in grey ballast stones and patches of oil-stained dirt. "
                "Surrounding objects: a rusty signal pole, a discarded plastic bucket, and a small vegetable patch grown right next to the tracks."
            ),
            "Halaman Bengkel Las / Pandai Besi": (
                "Sitting on a wooden crate in front of a traditional blacksmith (Pandai Besi) workshop. "
                "The background is a dark, soot-covered shed with glowing embers and various iron tools hanging on the wall. "
                "The floor is covered in black charcoal dust and metallic scraps. "
                "Surrounding objects: a heavy anvil on a log, a pile of raw iron bars, and a large bucket of murky cooling water."
            ),
            "Bawah Pohon Beringin Besar": (
                "Sitting on a large, gnarled tree root of a massive, ancient Banyan tree (Pohon Beringin). "
                "The background is filled with thick, hanging aerial roots and dense dark green foliage, creating a mysterious atmosphere. "
                "The ground is covered in a thick layer of dry leaves and mossy stones. "
                "Surrounding objects: a small stone shrine with dry flower offerings (sesaji), an old bicycle, and a weathered wooden bench."
            ),
            "Depan Penggilingan Kerupuk": (
                "Sitting on a stool in front of a home-based cracker factory (Pabrik Kerupuk). "
                "The background shows hundreds of round bamboo trays (tampah) filled with colorful raw crackers drying in the sun. "
                "The ground is sun-baked white cement with a thin layer of flour dust. "
                "Surrounding objects: a large frying wok (wajan), several stacked tins of crackers (kaleng kerupuk), and a dusty delivery motorbike."
            ),
            "Gubuk Deru Hujan": (
                "Sitting inside a small field hut with a thick, shaggy thatched roof (atap rumbia). "
                "The floor is wet bamboo with realistic water puddles and mud stains. "
                "The background is a misty view of rain falling on the rice fields. "
                "Surrounding objects: an old burlap sack used as a raincoat, a clay pot for boiling water, and a pair of mud-stained rubber boots."
            ),
            "Gubuk Panen Jerami": (
                "Sitting on a thick pile of dry, golden rice stalks (jerami) inside a rough teak-wood hut. "
                "The background is a harvested rice field with scattered hay stacks. "
                "The environment is filled with loose straw and golden husks. "
                "Surrounding objects: a large woven basket (tenggok) filled with unhusked rice, a traditional wooden rake, and a stained enamel plate."
            ),
            "Kandang Kambing Kayu": (
                "Sitting on a weathered wooden plank platform next to an empty livestock pen. "
                "The background is a solid wall of vertical dark teak wood slats with visible wood grain and gaps. "
                "The floor is a mix of dry soil and scattered hay. "
                "Surrounding objects: an old woven grass basket (kranjang rumput), a rusted metal bucket, and a hanging kerosene lantern (without light)."
            ),
            "Bawah Pohon Bambu": (
                "Sitting on a pile of dry, crunchy bamboo leaves (klaras) in a secluded grove. "
                "The background is a dense thicket of green and yellow bamboo poles (Pring Petung). "
                "The floor is dark, damp soil mixed with fallen organic debris. "
                "Surrounding objects: a pile of bamboo shoots (rebung), an old rusty bicycle carrier, and a small birdcage hanging from a branch."
            ),
            "Sumur Tua Berlumut": (
                "Sitting on a low mossy stone wall next to a traditional village well (sumur timba). "
                "The background is a solid wall of old red bricks covered in thick green moss and ferns. "
                "The floor is wet grey cement with realistic puddles and water stains. "
                "Surrounding objects: a black rubber bucket with a frayed rope, a bar of soap on a stone, and a pair of wooden clogs (gapyak)."
            ),
            "Pinggir Lapangan Voli Desa": (
                "Sitting on a weathered wooden bench at the edge of a dusty, hard-packed dirt volleyball court. "
                "The background features a sagging net and a few village youths playing in soft focus. "
                "The ground is dry, dusty earth with white chalk lines for the court boundaries. "
                "Surrounding objects: a plastic water gallon, a few scattered sandals, and a rusty bicycle leaning against a tree."
            ),
            "Tempat Pembuatan Batu Bata (Lio)": (
                "Sitting on a stack of unbaked grey clay bricks inside a large open-walled shed. "
                "The background shows rows of thousands of red bricks stacked in a pyramid shape. "
                "The floor is covered in fine red brick dust and dry straw used for firing. "
                "Surrounding objects: a wooden brick mold, a pile of wet dark clay, and a soot-covered furnace in the distance."
            ),
            "Halaman Jemuran Baju semrawut": (
                "Sitting on a plastic chair in a narrow backyard filled with hanging laundry. "
                "The background is a solid wall of colorful clothes, sarongs, and towels hanging on makeshift bamboo poles. "
                "The ground is damp cement with patches of green moss and soap suds. "
                "Surrounding objects: a plastic laundry basin, a tangled garden hose, and a few stray kittens playing nearby."
            ),
            "Pinggir Hutan Bambu & Sungai": (
                "Sitting on a large mossy rock where a bamboo forest meets a small stream. "
                "The background is a dense, dark green thicket with sunlight barely breaking through the bamboo leaves. "
                "The ground is a mix of wet river sand, smooth pebbles, and decaying bamboo leaves. "
                "Surrounding objects: a bamboo fishing rod, a blue plastic bucket, and a pile of river stones."
            ),
            "Tempat Pembuatan Batu Bata (Lio)": (
                "Sitting on a stack of unbaked grey clay bricks inside a large open-walled shed. "
                "The background shows rows of thousands of red bricks stacked in a pyramid shape. "
                "The floor is covered in fine red brick dust and dry straw used for firing. "
                "Surrounding objects: a wooden brick mold, a pile of wet dark clay, and a soot-covered furnace in the distance."
            ),
            "Pinggir Sungai Berbatu": (
                "Sitting on a massive flat grey river stone. "
                "The background is a flowing river with white water splashes and smooth boulders. "
                "The floor is a mix of rounded pebbles, fine sand, and sun-bleached drift-wood. "
                "Surrounding objects: a bamboo fishing rod, a small plastic bucket, and a sarong laid out to dry on a rock."
            ),
            "Lantai Tanah & Jemuran Gabah": (
                "Sitting on a low plastic stool on a flat, swept dirt floor (tanah liat). "
                "The background is a solid wall of old red bricks with mossy patches and white salt stains. "
                "The floor is covered by a large blue plastic tarp used for drying unhusked rice (gabah). "
                "Surrounding objects: a bamboo broom (sapu lidi), a wooden rake, and a few scattered chickens picking at the grain."
            ),
            "Pojok Gudang Kayu Bakar": (
                "Sitting on a stack of rough timber planks in a shed. "
                "The background is a massive pile of split firewood (kayu bakar) stacked unevenly reaching the ceiling. "
                "The floor is covered in dry bark, wood chips, and fine sawdust. "
                "Surrounding objects: an old rusted axe, a pile of dry coconut husks (sepet), and a dusty spiderweb in the corner."
            ),
            "Samping Kandang Ayam": (
                "Sitting on a wooden crate next to a bamboo chicken coop (kandang ayam petelur). "
                "The background is a wall of bamboo slats with visible wire mesh and feathers stuck in the gaps. "
                "The floor is dark soil mixed with dry straw and grain husks. "
                "Surrounding objects: a plastic feed bucket, a pile of old bamboo poles, and a discarded rubber tire used as a planter."
            ),
            "Teras Belakang & Cucian Piring": (
                "Sitting on a cold cement steps near a backyard washing area. "
                "The background is a solid wall of unpainted cement with green water stains and mold. "
                "The floor is wet and slippery with realistic soap suds and puddles. "
                "Surrounding objects: a stack of enamel plates, a blackened cooking pot, a pair of worn-out sandals (sandal jepit), and a plastic basin."
            ),
            "Bawah Pohon Melinjo": (
                "Sitting on the ground on top of a flattened cardboard box. "
                "The background is the trunk of a tall Gnetum gnemon tree (pohon melinjo) and a dense thicket of wild shrubs. "
                "The floor is covered in small yellowish melinjo seeds and dry, crunchy leaves. "
                "Surrounding objects: a bamboo basket (tenggok) for gathering leaves, and an old radio on a stone."
            ),
            "Pojok Genteng Tua": (
                "Sitting on a low wooden plank leaning against a massive stack of old, mossy terracotta roof tiles (genteng tanah liat). "
                "The background is a solid wall of stacks of tiles with realistic chips, cracks, and patches of grey lichen. "
                "The floor is dark, damp soil with scattered broken tile fragments and small ferns. "
                "Surrounding objects: an old bamboo ladder, a rusted watering can, and a pile of dry coconut husks (sepet)."
            ),
            "Selasar Kandang Sapi": (
                "Sitting on a thick timber beam next to a traditional village cattle pen made of heavy teak logs. "
                "The background is a solid wall of dark, weathered wood with visible rope tie-marks and animal-rubbed textures. "
                "The floor is a mix of packed earth and dried yellow straw (jerami). "
                "Surrounding objects: a large woven bamboo basket (tenggok) filled with grass, a plastic bucket, and an old salt-lick block on a stump."
            ),
            "Jemuran Pakaian Belakang": (
                "Sitting on a low stone next to a simple clothesline made of frayed plastic rope tied between two trees. "
                "The background is a solid wall of unpainted, weathered grey cement with water stains and peeling moss. "
                "The floor is uneven dirt with small puddles of soapy water and a few plastic clothespins scattered around. "
                "Surrounding objects: a pile of wet laundry in a plastic basin, a pair of wooden clogs (bakiak), and a small cat playing with a thread."
            ),
            "Pojok Kebun Singkong": (
                "Sitting on a fallen log in the middle of a dense cassava plantation. "
                "The background is a wall of vertical cassava stems and large, palmate green leaves. "
                "The ground is covered in dark, loose soil with realistic root bumps and dry weeds. "
                "Surrounding objects: a pile of harvested cassava roots with clinging dirt, and a worn-out conical straw hat (caping)."
            ),
            "Gubuk Alat Tani": (
                "Sitting on a stack of old burlap sacks inside a small, open-air tool shed. "
                "The background is a solid wall of vertically arranged bamboo poles with farm tools hanging from rusty nails. "
                "The floor is covered in a layer of fine dust, dry grass, and old fertilizer bags. "
                "Surrounding objects: a bamboo rake (garu), and an old radio playing static on a wooden crate."
            ),
            "Kebun Semangka": (
                "Sitting on a flat wooden plank in the middle of a sprawling watermelon field. "
                "The background is a solid carpet of large, lobed green leaves and tangled curly vines (sulur) spreading across the ground. "
                "The floor is dry, sandy soil with realistic cracks and scattered straw mulch. "
                "Surrounding objects: several large striped watermelons still attached to vines, a pile of harvested fruit, and an old plastic bucket for watering."
            ),
            "Kebun Melon": (
                "Sitting on a low stool inside a greenhouse or open melon farm with vertical bamboo trellises (ajir). "
                "The background is a wall of hanging green melons supported by small plastic nets and climbing vines. "
                "The floor is covered in black plastic mulch (mulsa) with small holes where the stems grow out. "
                "Surrounding objects: a small notebook for recording harvest, and a discarded fertilizer bag."
            ),
            "Kebun Nanas": (
                "Sitting on a clear patch of earth surrounded by sharp, spiky pineapple plants. "
                "The background is a dense sea of long, serrated grey-green leaves with a few pineapples growing from the centers. "
                "The floor is reddish-brown volcanic soil with small pebbles and dry weeds. "
                "Surrounding objects: a thick pair of protective gloves, a large woven basket (tenggok), and a wooden crate for fruit."
            ),
            "Kebun Buah Naga": (
                "Sitting on a stone against a background of concrete pillars covered in sprawling Dragon Fruit cactus vines. "
                "The facade features long, triangular green cactus arms hanging down like organic curtains. "
                "The floor is dry dirt with fallen pink flower petals and small stone fragments. "
                "Surrounding objects: a long bamboo pole for harvesting, a plastic crate, and an old wide-brimmed straw hat (caping)."
            ),
            "Kebun Strawberry": (
                "Sitting on a small wooden plank in a highland strawberry farm. "
                "The background features rows of black polybags or elevated wooden planters filled with green strawberry plants and small white flowers. "
                "The floor is covered in dry pine needles or straw mulch to keep the fruits clean. "
                "Surrounding objects: several bright red strawberries hanging from the vines, and a small plastic basket for picking."
            ),
            "Kebun Jeruk": (
                "Sitting on a low stool under the dense canopy of orange trees. "
                "The background is a wall of dark green waxy leaves and dozens of round yellow oranges hanging from the branches. "
                "The floor is dark soil mixed with fallen orange leaves and a few overripe fruits on the ground. "
                "Surrounding objects: a long bamboo harvesting pole (galah), a large woven bamboo basket (tenggok), and an old plastic crate."
            ),
            "Kebun Pepaya": (
                "Sitting on a fallen papaya trunk against a background of tall, slender papaya trees with large star-shaped leaves. "
                "The facade features bunches of green and ripening orange papayas clustered near the top of the trunks. "
                "The ground is covered in dry greyish leaves and loose soil with realistic root bumps. "
                "Surrounding objects: a wooden ladder leaning against a tree, a pile of harvested fruit, and an old 'arit' (sickle) on the ground."
            ),
            "Kebun Anggur": (
                "Sitting on a wooden bench under a low-hanging bamboo trellis covered in grapevine leaves. "
                "The background features heavy clusters of purple and green grapes hanging directly above the diorama. "
                "The floor is a mix of pebbles and fine sand with fallen vine tendrils and dry leaves. "
                "Surrounding objects: a glass of tea on a wooden box, and a traditional conical hat (caping)."
            ),
            "Kebun Pisang": (
                "Sitting on a fallen, rotting banana trunk (gedebog) in a dense, humid grove. "
                "The background is a solid wall of massive green banana leaves, some tattered and frayed by wind, mixed with hanging dry brown leaves (klaras). "
                "The floor is damp, dark soil covered in decaying organic matter and small wild mushrooms. "
                "Surrounding objects: a bunch of harvested green bananas (pisang kepok), and a discarded plastic tarp."
            ),
            "Pojok Pasar Tradisional": (
                "Sitting on a low wooden bench in a crowded, narrow aisle of a traditional village market. "
                "The background is a blur of colorful hanging goods, stacks of baskets, and other traders in the distance. "
                "The ground is damp, dark cement with scattered vegetable scraps and discarded plastic bags. "
                "Surrounding objects: a large pile of coconuts, a hanging scale (timbangan dacin), and a stack of wooden egg crates."
            ),
            "Pinggir Sungai Desa": (
                "Sitting on a large, smooth river stone by the edge of a shallow, rocky river. "
                "The background features lush green bamboo trees leaning over the water and a glimpse of a small concrete bridge. "
                "The water is clear, flowing over mossy stones with realistic reflections of the sky. "
                "Surrounding objects: a colorful plastic laundry basin, a bar of soap on a rock, and a pile of wet clothes being sun-dried."
            ),
            "Pangkalan Ojek / Pos Ronda": (
                "Sitting on a long wooden bench (lincak) inside a small, open-walled village guard post. "
                "The background shows a quiet village crossroads with a dusty motorbike parked nearby. "
                "The floor is hard-packed dirt with scattered dry leaves and a few cigarette butts. "
                "Surrounding objects: a large wooden slit drum (kentongan), a dusty village announcement board, and an old wall calendar hanging on a post."
            ),
            "Halaman Sekolah Desa": (
                "Sitting on a cement bench under a large flamboyant tree in a quiet school yard. "
                "The background features a simple white-and-red school building with long corridors and a flagpole. "
                "The ground is a mix of sun-baked soil and patches of thin grass. "
                "Surrounding objects: a few scattered plastic snack wrappers, a rusty bicycle, and a colorful mural painted on a low wall."
            ),
            "Teras Balai Desa / Balai RW": (
                "Sitting on a plastic chair on the wide, tiled terrace of a village community hall. "
                "The background features a solid white wall with a large village map and several wooden announcement boards. "
                "The floor is made of clean but old grey cement tiles with realistic reflections. "
                "Surrounding objects: a tall flagpole with a fluttering red and white flag, a stack of plastic chairs in the corner, and a large clay water pot (gentong)."
            ),
            "Jembatan Bambu (Sesek)": (
                "Sitting on the edge of a creaky bamboo bridge crossing a small ravine or stream. "
                "The background is a dense green thicket of bamboo and tropical ferns under a soft morning mist. "
                "The bridge surface is made of woven bamboo (sesek) with visible gaps and weathered textures. "
                "Surrounding objects: a long bamboo pole used for balance, a stack of harvested firewood, and a plastic bucket."
            ),
            "Pojok Jantung Pisang": (
                "Sitting on a low wooden stool directly under a low-hanging purple banana blossom (jantung pisang). "
                "The background features several thick, moist banana trunks with realistic layered textures and water-stain patterns. "
                "The ground is covered in dry banana fibers and fallen purple blossom petals. "
                "Surrounding objects: a woven bamboo basket (tenggok) filled with banana hearts, a pair of muddy rubber boots, and a wooden crate."
            ),
            "Pojok Bengkel Motor Desa": (
                "Sitting on an old tire in front of a small, cluttered village motorcycle repair shop. "
                "The background is a dark interior filled with hanging spare parts, tools, and oily rags. "
                "The ground is dark, oil-stained cement with scattered metal scraps and bolts. "
                "Surrounding objects: a stack of used tires, a rusted air compressor, and an old calendar with a vintage motorbike picture."
            ),
            "Dermaga Kayu Kecil": (
                "Sitting on the edge of a weathered wooden jetty overlooking a calm river or lake. "
                "The background features a few small traditional wooden boats (sampan) moored nearby and a distant line of trees. "
                "The floor is made of grey, sun-bleached wood planks with visible gaps and rusted nails. "
                "Surrounding objects: a tangled fishing net, a plastic bucket, and a coil of frayed rope."
            ),
            "Pinggir Tambak Ikan": (
                "Sitting on a narrow grassy embankment between two large fish ponds (tambak). "
                "The background features the shimmering surface of the water reflecting the sky and a small bamboo hut for the caretaker. "
                "The ground is damp soil with patches of thick grass and small white stones. "
                "Surrounding objects: a bag of fish feed, a bamboo scoop net (seser), and a pair of muddy rubber sandals."
            ),
            "Jembatan Gantung Desa": (
                "Sitting at the entrance of a narrow suspension bridge with wooden slats and rusted cables. "
                "The background is a deep green valley with the tops of coconut trees visible below. "
                "The ground is a mix of hard dirt and large concrete anchor blocks for the bridge cables. "
                "Surrounding objects: a rusty bicycle leaning against the cable, a small wooden sign, and scattered dry leaves."
            ),
            "Pinggir Waduk / Bendungan": (
                "Sitting on a large concrete block at the edge of a massive village reservoir (waduk). "
                "The background is a vast expanse of still water with mountains or hills in the far distance under a soft haze. "
                "The ground is dry, cracked earth near the water's edge with small shells and pebbles. "
                "Surrounding objects: a simple bamboo fishing rod, a plastic bottle, and an old hat resting on the concrete."
            ),
            "Tanggul Sungai Besar": (
                "Sitting on a grassy slope of a high river embankment (tanggul). "
                "The background shows a wide brown river flowing below and the roofs of village houses on the other side. "
                "The ground is covered in wild, overgrown grass and small purple wildflowers. "
                "Surrounding objects: a grazing goat tied to a wooden stake, a pile of harvested grass, and a simple wooden bench."
            ),
            "Halaman Belakang Pabrik Tahu": (
                "Sitting on a low stool near a small drainage canal behind a traditional village tofu factory. "
                "The background features white steam rising from the building and stacks of firewood. "
                "The floor is wet, dark cement with a thin layer of white soy residue and moss. "
                "Surrounding objects: several large plastic barrels, a stack of wooden molds, and a bicycle parked nearby."
            ),
            "Puing Bangunan Tua (Rumah Roboh)": (
                "Sitting on a pile of mossy red bricks from a ruined house. "
                "The background is a solid wall of weathered bricks and twisted rusted rebars partially covered by overgrown vines and wild shrubs. "
                "The ground is a mix of broken tiles (pecahan genteng), dry mortar dust, and weeds. "
                "Surrounding objects: an old wooden door leaning against the debris, a cracked clay pot, and a few lizards on the stones."
            ),
            "Pinggir Hutan Jati (Musim Gugur)": (
                "Sitting on a fallen teak log at the edge of a dry teak forest. "
                "The background is a dense vertical line of grey teak trunks with no leaves, creating a stark, moody atmosphere. "
                "The ground is completely buried under a thick layer of large, crunchy brown teak leaves. "
                "Surrounding objects: a pile of gathered dry branches, a rusted axe (kapak), and a small bamboo basket for mushrooms."
            ),
            "Pinggir Tambang Pasir Manual": (
                "Sitting on a wooden crate at the edge of a small village sand mine by the river. "
                "The background is a steep wall of layered grey sand and river stones with visible shovel marks. "
                "The ground is fine, loose grey sand with scattered pebbles and deep tire tracks from a truck. "
                "Surrounding objects: a large sieve for sand (ayakan), a rusty shovel, and a plastic jug of water."
            ),
            "Jemuran Daun Pisang": (
                "Sitting on a bamboo mat in a clearing surrounded by banana trees. "
                "The background features several large, fresh banana leaves laid out on the ground or leaning against a fence to dry. "
                "The floor is a mix of dry soil and scattered banana leaf stalks (pelepah). "
                "Surrounding objects: a bundle of tied banana leaves, and a traditional conical hat (caping) resting on the ground."
            ),
            "Gubuk Tambak Udang/Ikan": (
                "Sitting on a fragile wooden jetty of a small bamboo hut (saung) over a vast brackish water pond. "
                "The background features the open water of the pond with a few wooden aerators (kincir air) in the distance. "
                "The floor is made of old, sun-bleached timber planks with salt crusts and small dried algae. "
                "Surrounding objects: a large fishing net (jala), a plastic bucket for fish feed, and an old lifebuoy hanging on a bamboo post."
            ),
            "Pinggir Kolam Ikan Koi": (
                "Sitting on a flat decorative river stone at the edge of a clear garden pond. "
                "The background is the water surface filled with vibrant, colorful Koi fish (orange, white, and calico) swimming near the surface. "
                "The floor is a mix of smooth pebbles, green mossy rocks, and small water plants like lilies. "
                "Surrounding objects: a small wooden bridge in the distance, a ceramic bowl of fish food, and a pair of traditional wooden clogs (gapyak)."
            ),
            "Belakang Aquarium Ikan Hias": (
                "Sitting on a small stool directly behind a massive, long glass aquarium filled with colorful tropical fish. "
                "The background is the interior of the tank with green aquatic plants, white sand, and glowing neon fish swimming across. "
                "The floor is clean indoor tiles with a small rug. "
                "Surrounding objects: an air pump with bubbling sounds (visualized as bubbles), a fish net, and containers of fish flakes on a side table."
            ),
            "Pojok Kolam Ikan Hias": (
                "Sitting on a low concrete ledge next to a small backyard pond with a mini waterfall feature. "
                "The background features colorful goldfish and comets darting through floating duckweed (mata lele). "
                "The floor is wet terracotta tiles with realistic water splashes and damp patches. "
                "Surrounding objects: a stone statue of a frog, a watering can, and a small bamboo water fountain (shishi-odoshi)."
            ),
            "Bengkel Kayu Tradisional": (
                "Sitting on a thick, unfinished timber block inside a rustic carpentry workshop. "
                "The background is a solid wall of hanging hand tools: saws, chisels, and wooden mallets on a pegboard. "
                "The floor is buried under a thick layer of curly wood shavings (tatal) and fine sawdust. "
                "Surrounding objects: a half-finished wooden chair, a bottle of wood glue, and a pile of teak planks."
            ),
            "Pojok Anyaman Bambu": (
                "Sitting on a woven bamboo mat surrounded by hundreds of thin bamboo strips (atan). "
                "The background features several half-finished 'besek' and 'tampah' stacked against a gedek wall. "
                "The floor is covered in small bamboo fibers and offcuts. "
                "Surrounding objects: a bundle of raw bamboo poles, and a bowl of water for soaking the strips."
            ),
            "Gudang Barang Antik Desa": (
                "Sitting on an old dusty trunk in a dark corner filled with forgotten village heirlooms. "
                "The background features a stack of old clay jars (gentong), a rusted manual sewing machine, and a vintage bicycle. "
                "The floor is dark stone with layers of realistic dust and cobwebs. "
                "Surrounding objects: an old kerosene lantern, a pile of vintage batik cloths, and a moth-eaten wooden cupboard."
            ),
            "Pinggir Rel Kereta Desa": (
                "Sitting on a large ballast stone near a quiet, single-track railway line passing through a village. "
                "The background features the perspective of the iron rails disappearing into the green bushes. "
                "The floor is a mix of coarse grey gravel (ballast), dry grass, and rusted iron scraps. "
                "Surrounding objects: an old signal post, a discarded plastic bottle, and a small wildflower patch between the tracks."
            ),
            "Halaman Jemuran Kerupuk": (
                "Sitting on a low stool in a vast yard filled with hundreds of wooden trays (widik) drying colorful raw crackers. "
                "The background is a sea of pink, yellow, and white crackers arranged in geometric rows. "
                "The floor is dry, swept cement with realistic cracks. "
                "Surrounding objects: a large bamboo pole for carrying the trays, a stray chicken, and a conical hat (caping) on a post."
            ),
            "Pojok Pasar Desa": (
                "Sitting on a low wooden bench in a quiet corner of a traditional village market. "
                "The background features stacks of empty wooden crates, woven bamboo baskets (bronjong), and old burlap sacks. "
                "The floor is a mix of damp cement and scattered organic waste like onion skins and dry corn husks. "
                "Surrounding objects: a rusted manual scale, a stray cat, and a discarded cardboard box for 'Mie Instan'."
            ),
            "Gubuk Pandai Besi": (
                "Sitting on a soot-covered wooden stump inside a traditional blacksmith workshop. "
                "The background features a large stone furnace, a heavy iron anvil, and various raw iron scraps. "
                "The floor is covered in a thick layer of black charcoal dust, fine iron filings, and grey ash. "
                "Surrounding objects: a heavy hammer, and a bucket of dark cooling water."
            ),
            "Teras Rumah Panggung Kayu": (
                "Sitting on the top step of a weathered wooden staircase leading to a traditional stilt house. "
                "The background is a solid wall of dark, unpainted timber planks with deep wood grain and lichen. "
                "The floor (the steps) shows realistic wear-and-tear and mud-stained footprints. "
                "Surrounding objects: a pair of old wooden clogs (bakiak), a broom made of palm leaf ribs (sapu lidi), and a plastic basin for washing feet."
            ),
            "Pojok Penggilingan Padi": (
                "Sitting on a stack of plastic sacks inside a noisy rice mill shed. "
                "The background is filled with massive piles of rice husks (sekam) and heavy machinery parts. "
                "The air is hazy with floating fine rice dust, and the floor is covered in golden husks and white flour particles. "
                "Surrounding objects: a large metal funnel, a plastic shovel, and a tattered sarong used as a dust mask."
            ),
            "Gunung Sampah TPA": (
                "Sitting on a flattened cardboard box at the base of a massive mountain of assorted waste. "
                "The background is a solid wall of colorful but faded plastic bags, crushed plastic bottles, and organic waste layers. "
                "The floor is a mix of dark, muddy soil and scattered colorful scrap fragments. "
                "Surrounding objects: a long bamboo hook (pengait sampah), a large woven plastic sack (karung rongsok), and a swarm of out-of-focus flies."
            ),
            "Gudang Pengepul Rongsok": (
                "Sitting on a rusted oil drum inside a cluttered scrap metal yard. "
                "The background is a solid wall of stacked rusted iron pipes, old bicycle frames, and crumpled sheet metal. "
                "The floor is dark, oil-stained concrete with scattered rusty nails and metallic dust. "
                "Surrounding objects: a heavy manual scale, a pile of copper wires, and a pair of thick industrial gloves."
            ),
            "Pojok Tumpukan Botol Plastik": (
                "Sitting on a low stool surrounded by thousands of transparent and colorful plastic bottles packed in large nets. "
                "The background is a translucent wall of plastic textures, showing realistic reflections and crinkled surfaces. "
                "The floor is swept cement with scattered plastic caps and labels. "
                "Surrounding objects: a manual bottle crusher, a large white plastic sack, and an old radio on a wooden crate."
            ),
            "Bawah Pohon Samping TPA": (
                "Sitting on the dry ground at the edge of a landfill under a dusty tree. "
                "The background features the silhouette of an excavator and a pile of old discarded tires. "
                "The floor is dry dirt mixed with small bits of windblown plastic and dry leaves. "
                "Surrounding objects: a tattered umbrella, a plastic water gallon, and a pair of worn-out boots with holes."
            ),
            "Gudang Kardus Bekas": (
                "Sitting on a low stack of flattened cardboard boxes. "
                "The background is a solid wall of towering, neatly tied stacks of brown corrugated cardboard boxes with visible shipping labels and torn tape. "
                "The floor is covered in fine paper dust, cardboard scraps, and loose packing strings. "
                "Surrounding objects: a large manual weighing scale, and a pile of old newspapers used as padding."
            ),
            "Pojok Tumpukan Koran": (
                "Sitting on a wooden crate surrounded by yellowed, dusty stacks of old newspapers and vintage magazines. "
                "The background features walls of paper bundles tied with plastic twine, showing realistic frayed edges and ink-stained textures. "
                "The floor is dark cement with scattered loose pages and paper confetti. "
                "Surrounding objects: an old pair of glasses, a glass of black coffee on a stack of newsprint, and a small hand-trolley (hand-truck)."
            ),
            "Lapak Rongsok Campuran": (
                "Sitting in a crowded yard filled with a chaotic mix of scrap materials. "
                "The background features a wall of compressed plastic blocks, tangled copper wires, and old electronic circuit boards. "
                "The floor is gritty soil mixed with metallic fragments, plastic caps, and small rusted bolts. "
                "Surrounding objects: a large magnetic wand for sorting metal, a massive white sack (karung jumbo) filled with cans, and a rusted bicycle frame."
            ),
            "Gubuk Sortir Sampah Kertas": (
                "Sitting inside a small open-air hut dedicated to sorting scrap paper. "
                "The background features various types of paper waste: egg cartons, cement bags, and office paper piles. "
                "The floor is a mix of packed earth and layers of discarded paper fibers. "
                "Surrounding objects: a large bamboo basket (tenggok) for sorting, a plastic water gallon, and a pair of worn-out work gloves."
            ),
            "Teras Samping Toko Kelontong": (
                "Sitting on a wooden bench on the side of a small village 'Warung'. "
                "The background features stacks of empty glass soda bottles in plastic crates and a few hanging snack sachets. "
                "The floor is grey cement with realistic wear-and-tear. "
                "Surrounding objects: a vintage bicycle leaning against the wall, a wooden crate, and an old glass jar filled with crackers (peyek)."
            ),
            "Pojok Perpustakaan Desa": (
                "Sitting on the floor in a small, humble community reading corner. "
                "The background is a simple wooden bookshelf filled with old, mismatched books and magazines. "
                "The floor is covered in a clean, cheap plastic carpet with a simple pattern. "
                "Surrounding objects: a small desk, a pair of reading glasses, and a stack of newspapers."
            ),
            "Taman Bunga Depan Rumah": (
                "Sitting on a low wooden bench surrounded by dozens of colorful plants in recycled containers. "
                "The background features bright red hibiscus, yellow marigolds, and pink bougainvillea. "
                "The floor is swept gravel and small white stones with realistic sandy textures. "
                "Surrounding objects: potted plants in old tin biscuit cans, a plastic watering can, and a small bamboo fence."
            ),
            "Taman Tanaman Obat": (
                "Sitting on a flat stone in a small backyard 'Apotek Hidup' (herbal garden). "
                "The background is a lush mix of ginger plants, turmeric leaves, and tall lemongrass stalks. "
                "The floor is rich, dark damp soil with patches of green moss and fallen leaves. "
                "Surrounding objects: a small clay mortar and pestle (ulekan), and a woven basket for gathering herbs."
            ),
            "Sudut Taman Pot Gantung": (
                "Sitting on a plastic stool under a wooden trellis filled with hanging plants like 'Anggrek' (orchids) and ferns. "
                "The background features several hanging pots made of halved coconut shells and plastic bottles. "
                "The floor is clean grey cement with realistic water stains from plant irrigation. "
                "Surrounding objects: a wooden birdcage hanging nearby, a small glass of tea on a table, and a pile of potting soil in a sack."
            ),
            "Taman Sayur Mini": (
                "Sitting on a wooden crate next to small patches of chili plants, mustard greens (sawi), and spring onions. "
                "The background is a mix of vibrant green leafy vegetables and vertical bamboo stakes (ajir). "
                "The ground is covered in dark compost and dry rice husks (sekam). "
                "Surrounding objects: a small hand trowel, a plastic bucket, and several red chili peppers drying on a bamboo tray (tampah)."
            ),
            "Gubuk Pinggir Rel Kereta Kota": (
                "Sitting on a wooden crate next to a railway track in a crowded city slum. "
                "The background features a solid wall of rusted corrugated iron sheets (seng) and graffiti-covered concrete. "
                "The floor is a mix of coarse grey gravel, oil-stained soil, and scattered plastic trash. "
                "Surrounding objects: a pile of old tires, a plastic gallon of water, and overhead messy electrical wires."
            ),
            "Teras Kontrakan Sempit": (
                "Sitting on a thin floor mat in a very narrow city alleyway (gang sempit). "
                "The background is a solid wall of unpainted cement bricks with mossy water leaks from upper floors. "
                "The floor is cracked, uneven asphalt with small puddles of soapy water. "
                "Surrounding objects: a row of laundry hanging on a plastic rope, a gas cylinder (LPG 3kg), and a pair of worn-out sneakers."
            ),
            "Kolong Jembatan Beton": (
                "Sitting on a flattened cardboard box under a massive, weathered concrete bridge structure. "
                "The background features the grey, stained pillars of the bridge with realistic soot and exhaust smoke marks. "
                "The floor is dusty, dry dirt mixed with broken glass and old newspapers. "
                "Surrounding objects: a makeshift bed made of sacks, an old bicycle, and a small portable stove."
            ),
            "Taman Mawar & Melati": (
                "Sitting on a white-painted vintage bench surrounded by dense bushes of red roses and white jasmine. "
                "The background is a vibrant wall of flowers with soft petals and green leaves. "
                "The floor is covered in fallen white and red petals with clean stone paths. "
                "Surrounding objects: a classic watering can, a small butterfly net, and a wooden basket of freshly cut flowers."
            ),
            "Kebun Bunga Warna-Warni": (
                "Sitting on a flat stone in the middle of a field of sunflowers, zinnias, and lavender. "
                "The background is a chaotic but beautiful explosion of yellow, purple, and orange blooms. "
                "The floor is a mix of rich brown soil and small pebbles. "
                "Surrounding objects: a wide-brimmed straw hat with a ribbon, a glass of iced tea, and a small garden shovel."
            ),
            "Sudut Taman Anggrek": (
                "Sitting on a low stool under a wooden trellis draped with various hanging orchids. "
                "The background features hanging coconut shell pots and mossy wooden slabs where orchids grow. "
                "The floor is damp grey cement with realistic water reflections. "
                "Surrounding objects: a mist sprayer bottle, a small wooden birdcage, and a pile of charcoal for planting."
            ),
            "Pinggiran Rel Kereta Jakarta": (
                "Sitting on a stack of old tires near a busy railway track in a crowded Jakarta district. "
                "The background is a solid wall of rusted corrugated iron sheets and grey concrete walls with peeling posters. "
                "The floor is coarse grey gravel mixed with plastic scrap and oil stains. "
                "Surrounding objects: messy overhead electrical cables, a plastic water gallon, and a discarded 'Mie Instan' box."
            ),
            "Gang Sempit Jakarta": (
                "Sitting on a thin mat in a very narrow alleyway between tall, unpainted brick buildings. "
                "The background is a wall of messy pipes, air conditioning units, and colorful laundry hanging overhead. "
                "The floor is cracked, uneven asphalt with puddles of soapy water. "
                "Surrounding objects: a 3kg LPG gas cylinder, a row of worn-out sandals, and a bucket of washing water."
            ),
            "Teras Kontrakan Padat": (
                "Sitting on a small wooden bench in a very narrow, sunless alleyway (gang sempit) between tall brick houses. "
                "The background is a wall of messy AC outdoor units, tangled cables, and damp mossy patches near the drainage. "
                "The floor is cracked asphalt with small soapy puddles from nearby laundry. "
                "Surrounding objects: a 3kg LPG cylinder, a row of worn-out sandals, and a bucket of washing water."
            ),
            "Puncak Gunung Berkabut": (
                "Sitting on a jagged volcanic rock at the edge of a high mountain peak. "
                "The background is a vast sea of white clouds (samudera awan) with silhouettes of distant peaks. "
                "The floor is dark volcanic sand and small pumice stones with realistic dry, gritty textures. "
                "Surrounding objects: a small camping stove, a metal mug with steam, and a sturdy wooden hiking pole."
            ),
            "Hutan Pinus Pegunungan": (
                "Sitting on a fallen pine trunk in a dense, misty forest. "
                "The background is a wall of tall, slender pine trees disappearing into thick white fog. "
                "The floor is covered in a thick, crunchy layer of dry pine needles and small pine cones. "
                "Surrounding objects: a kerosene lantern, a small stack of firewood, and an old wool blanket."
            ),
            "Lereng Gunung Berbatu": (
                "Sitting on a large boulder on a steep, treeless mountain slope. "
                "The background is a vast view of a valley below with tiny, twinkling village lights in the far distance. "
                "The ground is rough grey gravel and yellowed mountain grass (edelweiss style). "
                "Surrounding objects: a worn-out backpack, a pair of heavy boots, and a small handheld radio."
            )
        }
        # --- 4. MASTER AUDIO & SOULFUL EXPRESSION (ANTI-ASMA & HIGH-VULNERABILITY) ---
        MASTER_AUDIO_STYLE = {
            "Logat": [
                "RUH LELUHUR (85th+): Extremely thin, weightless, and ghostly. Voice frequently 'cuts out' due to very short breath. High-pitched with a wide, slow-motion tremolo. Sounds like a faint vibration of a 90-year-old soul. NO chest power.",
                "SERAK KERTAS KERING (80th+): High-pitched, scratchy voice like old paper rubbing together. Features 'vocal fry' and a dry, raspy texture in every syllable. Very brittle and sharp, showing extreme vocal cord dehydration.",
                "GUMAM MENDEM (75th+): Low-frequency, muffled mumble from deep inside a shrunken mouth. Sound is 'recessed' (mendem). Articulation is blurred and slow, typical of very weak facial muscles. Heavy Javanese lilt.",
                "SIULAN OMPONG (85th+): High-pitched and tiny. Mandatory 'slushy' whistling texture on S, T, and C sounds. Voice is soft and lacks resonance due to collapsed mouth structure from missing teeth. Pure vulnerability.",     
                "SESEPUH BATU (80th+): Deep, stony, and 'grainy' bass. It doesn't boom; it 'grinds'. Like stones rubbing together. Very slow delivery with long pauses as if gathering strength to speak. No lung power.",
                "RINTIHAN GEMETER (75th+): Mid-to-high pitch voice that is perpetually 'breaking'. Unstable frequency with rapid micro-shaking. Sounds as if the speaker is perpetually on the verge of crying. High emotional vulnerability.",    
                "SULING BAMBU TUA (80th+): Cracked, 'flute-like' quality. Voice is breathy but very weak. Hollow timber, sounding like air passing through a dry bamboo pipe. Very weary, dusty, and unpolished raw texture.", 
                "ISAKAN BERAT (85th+): Thick, heavy, and 'congested' texture but without the strength to cough. Sounds 'clogged' and weary. Every word feels heavy and labored, carrying the weight of a century."
            ],
            "Mood": [
                "Nrimo & Tabah: A weary, static facial expression with deeply etched wrinkles. The lips are thin, pale, and pressed tightly in a flat line—strictly NO smile. Eyes are looking off-camera with a hollow, distant gaze, reflecting a soul that has endured too much in silence.",             
                "Pasrah & Lelah: A weather-beaten face showing heavy physical exhaustion. The eyelids are slightly drooping (half-closed), suggesting deep fatigue. The chin is slightly tucked down (menunduk), creating a humble and submissive silhouette that looks fragile and broken yet dignified.", 
                "Iba & Mengharap: A gentle but sorrowful expression with eyes looking slightly upward toward a faint light source. The pupils have a tiny, hopeful glimmer amidst a tired, weathered face. The mouth is slightly shrunken and closed, conveying a silent, desperate plea for grace without a single word.",
                "Nyesek & Lirih: A fragile, haunting expression. The eyes are intensely 'sayu' (melancholic) and glistening with heavy moisture (wet look)—but strictly NO tears falling. The brow is subtly furrowed in a permanent state of worry. The face is completely static, capturing a deep, hidden heartbreak."
            ],
            "Physical Action": [
                "Mengusap Lembut & Menunduk: Both frail hands are gently caressing the side of the finished mosque with deep affection. Then slowly dropping the head (menunduk lesu) in exhaustion before making a brief, watery eye contact with the camera.",             
                "Menopang Dagu & Menatap Kosong: Resting one shaky elbow on the table, supporting a weary chin with a veiny hand. The other hand rests on the mosque's base. Staring at the camera with a hollow, 'nrimo' gaze that tells a story of a lifetime of struggle.",
                "Merapikan Letak dengan Tenaga Sisa: Using both hands to very slowly and shakily push the miniature an inch forward as if offering it to the viewer. After the effort, the hands stay trembling on the table, and the eyes meet the camera with a soulful, pleading look.",
                "Menepis Debu Imajiner & Menghela Napas: A very slow, frail gesture of blowing slightly at the dome, followed by a visible, heavy shoulder slump (menghela napas berat). Looking at the camera with eyes that reflect a haunting, quiet heartbreak.",
                "Menyentuh Kubah & Menoleh Lambat: Resting the fingertips of one hand on the very top of the dome, not pointing, but just feeling it. Slowly turning the face from the mosque to the camera with a faint, desperate glimmer of hope and deeply weathered skin.",
                "Mendekap Sisi Miniatur: Placing both hands around the corners of the mosque as if to hug it or protect it from the world. Looking into the camera lens with intense, weary eye contact, conveying a silent message: 'This is all I have left'."
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
                label_obj = "PILIH KOLEKSI DIORAMA" if "Diorama" in modus_konten else "DETAIL OBJEK / KARYA"
                st.markdown(f'<p class="small-label">{label_obj}</p>', unsafe_allow_html=True)
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
                pilih_logat = st.selectbox("Pilih Logat", MASTER_AUDIO_STYLE["Logat"])
                pilih_mood = st.selectbox("Pilih Mood", MASTER_AUDIO_STYLE["Mood"])
                pilih_aksi = st.selectbox("Pilih Gerakan Tubuh", MASTER_AUDIO_STYLE["Physical Action"])

            st.write("")
            btn_gen = st.button("🚀 GENERATE VIDEO PROMPT", type="primary", use_container_width=True, key="btn_generate_video")

        # --- LOGIC GENERATOR (ANTI-HALUSINASI VERSION: GENDER & WARDROBE LOCK) ---
        if btn_gen:
            # 1. POSISI MATI LESEHAN (Tetap)
            posisi_nenek = "sitting cross-legged on the ground (lesehan)"
            
            # 2. KUNCI LIGHTING & VISUAL (Tetap)
            scene_context = (
                f"ULTRA-HD 8K RESOLUTION. HYPER-REALISTIC RAW CINEMATIC FOOTAGE. NO TEXT. "
                f"LIGHTING: Very soft, gentle 5 PM golden-hour side lighting. Delicate warm rim light on the elderly's wrinkled skin and the mosque's edges. "
                f"CONTRAST: Rich, deep contrast where the mosque's internal LED lights create an intense glowing focal point. "
                # Jarak diubah ke 1.5 - 2 meter (Medium Close-Up) agar lebih proporsional
                f"CAMERA: Medium Close-up at 2 meters distance. Eye-level shot. "
                # Menambahkan gerakan zoom yang sangat halus (slow-crawl) agar tidak kaku
                f"MOTION: Extremely subtle, almost imperceptible slow zoom-in toward the face, 0.1x speed. "
                f"DEEP FOCUS: F/11 Aperture, CRYSTAL CLEAR focus on both the elderly person and the miniature mosque, zero blur."
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
            is_perempuan = any(x in pilihan_user.lower() for x in ["nenek", "ibu", "juminah", "sikem", "dulah", "sartini", "tinah", "wati"])
            
            if is_perempuan:
                gender_lock = (
                    "PHYSICAL MANDATORY: Elderly Indonesian woman, 100% hairless face, NO BEARD, NO MUSTACHE, clean face. "
                    "SKIN TEXTURE: Deeply wrinkled and aged, naturally sagging skin, NO smoothing filters. "
                    "GENDER WARDROBE: Full Indonesian Hijab/Kerudung covering all hair and neck. Wearing a simple elderly woman's house dress (Daster) or Kebaya."
                )
            else:
                gender_lock = (
                    "PHYSICAL MANDATORY: Elderly Indonesian man, weathered skin, clean-shaven face or very sparse stubble. "
                    "SKIN TEXTURE: Deeply wrinkled, sun-parched leathery skin. "
                    "GENDER WARDROBE: Traditional Indonesian Black Kopiah/Peci cap on head. Wearing a simple Koko shirt or a worn-out daily shirt. No hijab, no female daster."
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
            
            # Khusus Logat, karena ada embel-embel "Napas Tua (The Fading Echo):"
            # Kita split di titik dua paling akhir biar cuma dapet deskripsi Inggrisnya
            logat_final = pilih_logat.split(':')[-1].strip()
                
            # --- THE MAGIC INJECTION: ANTI-ASMA VERSION (75-80yo REALISM) ---
            if "Sedih" in pilih_mood or "Nyesek" in pilih_mood or "Lirih" in pilih_mood:
                # Fokus pada getaran pita suara yang hancur, bukan napas.
                audio_emotion = (
                    "MANDATORY AUDIO: Add a thick 'crying undertone' without audible sobbing. "
                    "The voice must be 'trembling' (slow tremolo) and 'brittle'. "
                    "Focus on a cracking, dry texture in the throat. STRICLTY NO heavy breathing or gasping. "
                    "The pace is painfully slow, with emotional weight in every word."
                )
            elif "Pasrah" in pilih_mood or "Nrimo" in pilih_mood:
                # Fokus pada suara yang tipis dan lelah (weary).
                audio_emotion = (
                    "MANDATORY AUDIO: Deliver with a weary, flat spiritual surrender. "
                    "Use a very thin, soft resonance. The voice sounds 'hollow' and 'recessed' (mendem). "
                    "Zero audible breathing. Focus on a faded, dusty vocal tone that is barely holding on."
                )
            elif "Iba" in pilih_mood or "Mengharap" in pilih_mood:
                # Fokus pada intonasi yang memohon (pleading).
                audio_emotion = (
                    "MANDATORY AUDIO: Use a gentle, 'pleading intonation' like a humble request. "
                    "The voice is very small, light, and high-pitched. "
                    "Add a faint 'emotional shimmer' (micro-shaking) at the end of sentences. "
                    "Avoid any heavy air intake, keep the sound pure and fragile."
                )
            else:
                audio_emotion = (
                    "MANDATORY AUDIO: Natural, steady elderly delivery. Calm and weary pacing with zero youthful energy."
                )

            # --- FINAL ASSEMBLY (V25: THE CHEST-LEVEL MASTERY) ---
            final_ai_prompt = (
                f"{scene_context} \n\n" 
                
                f"CHARACTER IDENTITY: {soul_desc}. {gender_lock} \n"
                f"ANATOMY LOCK: {ANATOMY_LOCK} \n"
                f"WARDROBE: {baju_desc}. \n"
                
                # --- KUNCI 1: Pastikan Environment nyebut MEJA TINGGI ---
                f"ENVIRONMENT: {env_detail}. A high rustic wooden table is positioned directly in front of the character's chest. \n\n"
                
                f"PERFORMANCE & INTERACTION: {aksi_final}. \n"
                f"MOOD & EMOTION: {mood_final}. Strictly focus on a soulful, humble, and pleading connection with the viewer. \n"
                
                # --- KUNCI 2: Pastikan Deskripsi Masjid nyebut POSISI DI MEJA ---
                f"THE MASTERPIECE: {deskripsi_teknis}. The 60cm mosque sits on the table at chest-height, sharing the frame with the character's torso and face. \n\n"
                
                f"AUDIO CONFIGURATION: \n"
                f"- Style & Age: {logat_final} \n"
                f"- Vocal Emotion: {audio_emotion} \n"
                f"- Dialog Content: '{user_dialog}' \n"
                f"- Delivery: Use long, heavy pauses. Focus on vocal cord tremors. STRICTLY NO gasping or heavy air intake. \n\n"
                
                # --- KUNCI 3: TECHNICAL SPEC UNTUK KOMPOSISI SEPERTI SS ---
                f"TECHNICAL SPEC: ARRI Alexa 65, 35mm lens, F/11, Eye-level. "
                f"FRAMING: Tight Medium-Shot (Bust to Waist). "
                f"COMPOSITION: The camera is close, capturing the elderly's face and the mosque at chest-level simultaneously. "
                f"Both hands must be visible touching or working on the mosque. Perfect balance between the person and the craft. \n\n"
                
                f"NEGATIVE PROMPT: beard on woman, mustache on woman, hijab on man, hair showing on woman, "
                f"smiling, laughing, teeth showing, aggressive expression, yelling, "
                f"wide shot, full body, legs showing, feet showing, top-down view, "
                f"thunderstorm, rain, cloudy grey, dark gloom, sunlight glare, harsh shadows, "
                f"blurry, heavy bokeh, shaky camera, artificial lighting, watermark, text, subtitles, captions, 3D render, cartoon, illustration."
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
