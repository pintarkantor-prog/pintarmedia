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
            "Kebun Semangka Colossal": (
                "The character is seated on a low weathered wooden crate behind the workspace. "
                "The setting is a vast outdoor Indonesian watermelon farm under the natural golden hour daylight. "
                "Background: rows of monumental, colossal watermelons still attached to thick tangled green vines spread across the frame. "
                "The diorama is positioned exactly between the elderly Indonesian carver and the camera, filling the straight-on horizontal frame. "
                "The long wooden table is heavily cluttered only with realistic construction debris from the carving: thousands of fresh, glistening rich-ruby-red watermelon flesh chunks, large fragments of removed green rind, curled shavings, and loose seeds with wet marks and moist juice. "
                "Strictly no whole watermelons, no sharp objects, no knives, no carving tools, and no metal on the table. Only raw fruit material debris. No text or calligraphy. "
                "The structure's deeply recessed entrances show the dense, glistening ruby-red interior flesh reflecting the soft, natural golden hour sunlight. No internal lighting Mechanisms. "
                "The floor is hard-packed grey earth with natural uneven textures and dry leaves."
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
