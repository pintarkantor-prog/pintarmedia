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
                    "A finished miniature mosque on a high wooden table at chest-level. "
                    "Architecture features precise geometric carving to create building facades. The central large dome is a smooth watermelon rind showing the distinctive green striped pattern. "
                    "The walls are dark green rind, but precisely carved with deep, recessed arched doorways and windows. The exposed surfaces within the doors and windows are juicy, glistening ruby-red flesh, **strictly with no etched text or calligraphy.** "
                    "Featuring multiple (at least four) smooth cylindrical minarets on different levels, topped with smaller green rind domes and tiny spires, connected by precise carved rind arches. "
                    "Table clutter: The wooden table surface is scattered with small, realistic glistening red flesh scraps, seed clusters, and fine green rind shavings. "
                    "The completed miniature is positioned right under the character's chin, sharing the frame with the character's torso and face. A full whole watermelon sits beside the miniature on the table. "
                    "Natural golden hour daylight focuses on the glistening moist texture of the red flesh, making it look organic and real. Zero LEDs, pure interaction with natural light."
                ),
                "Semangka: Kubah Kulit Hijau": (
                    "A completed miniature mosque on a high wooden table at chest-level. "
                    "Architecture features precise geometric carving to create clean facades. "
                    "The single massive central dome is a smooth watermelon rind showing the distinctive green striped pattern. "
                    "The walls are dark green rind, precisely carved with deep recessed arched doorways and windows showing juicy, glistening ruby-red flesh inside. **Strictly with no etched text or calligraphy.** "
                    "Table clutter: Small glistening red flesh fragments and green rind trimmings. "
                    "A full whole watermelon sits beside the miniature. Golden hour natural daylight focuses on the moist texture of the exposed red flesh in doorways."
                ),
                "Semangka: Kubah Daging Merah": (
                    "A finished miniature mosque on a high wooden table at chest-level. "
                    "Architecture features precise geometric carving to create building facades. The walls and minaret structures are made of smooth dark green rind, topped with smaller green rind domes. "
                    "The central main dome is a massive carved block of juicy, pulpy ruby-red watermelon flesh, polished to look glistening and moist, showing organic fibers. **Strictly with no etched text or calligraphy.** "
                    "Walls feature precisely carved out deep recessed arched doors and windows, revealing the juicy ruby-red flesh inside. "
                    "Table clutter: Scattering of glistening red flesh scraps, seed clusters, and fine green rind shavings scattered naturally on the table. "
                    "The completed miniature is positioned right under the character's chin, sharing the frame with the character's torso and face. A full whole watermelon sits beside the miniature. "
                    "Golden hour daylight focuses on the glistening moist texture of the main red flesh dome, making it glisten like gems. Zero LEDs, pure interaction with natural light."
                )

            },        
            "📦 Miniatur Bahan Sederhana": {
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
            },
            "✨ Miniatur Megah ( LED )": {
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
            
            # 2. KUNCI LIGHTING & VISUAL (REFINED FOR CLOSE-UP)
            scene_context = (
                f"ULTRA-HD 8K RESOLUTION. HYPER-REALISTIC RAW CINEMATIC FOOTAGE. "
                f"LIGHTING: Very soft, gentle 5 PM golden-hour side lighting. Delicate warm rim light on the elderly's wrinkled skin and the mosque's edges. "
                f"CONTRAST: Rich, deep contrast where the mosque's internal LED lights create an intense glowing focal point. "
                # Jarak dikunci 1.2 - 1.5 meter agar terasa intim tapi tidak memotong objek
                f"CAMERA: Tight Medium-Shot (Chest-up). Eye-level shot. "
                # Fokus pada "Chest-Level" agar Masjid & Wajah satu frame
                f"COMPOSITION: The miniature mosque is placed on the table at chest-height, sharing the frame 50/50 with the character's torso and face. "
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
