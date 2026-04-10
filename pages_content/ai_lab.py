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
        # --- 1. MASTER DNA MANUSIA ASLI (FULL BODY & NATURAL SKIN) ---
        MASTER_FAMILY_SOUL = {
            # ========================== KELOMPOK NENEK (Teduh & Berwibawa) ==========================
            "Nenek Juminah": (
                "An extremely lean and thin-faced Javanese elderly woman. "
                "Sunken cheeks with very prominent, high cheekbones and a sharp, bony jawline. "
                "Her skin is like parchment paper, tightly stretched over her facial structure but deeply creased with hundreds of fine, dry wrinkles. "
                "Visible hollows around the temples and eyes. Large, expressive but weary dark eyes with heavy crow's feet. "
                "Authentic weathered skin with deep sun-damage, fine moles, and uneven pigmentation. "
                "No soft volume, strictly bony and thin facial structure for a fragile look."
            ),
            "Nenek Sikem": (
                "An incredibly frail Javanese elder with a very small, shrunken facial structure. "
                "Her skin is extremely dry and flaky, with deep vertical fissures on her cheeks and forehead. "
                "Eyelids are severely drooping, creating a weary but resilient look. "
                "Visible salt-and-pepper peach fuzz on her chin and upper lip. "
                "The texture is raw and uneven, with prominent sun-spots and thick, leathery patches on the forehead. "
                "Neck skin is severely loose and sagging in thin, delicate folds. "
                "Masterpiece detail on the interaction between bone structure and sagging skin. No filters."
            ),
            "Nenek Dulah": (
                "An elderly Sundanese woman with a soft heart-shaped face that has significantly lost its firmness. "
                "The skin is pale and delicate, hanging in soft, heavy folds along the jawline. "
                "Distinct 'sayu' almond-shaped eyes with very thin, sparse eyebrows and heavy, drooping upper lids. "
                "Her nose is refined but the skin around the nostrils is deeply creased. "
                "Texture is focused on 'fine-cracked' wrinkles (like old porcelain) rather than deep canyons. "
                "Authentic age spots are faint but numerous. Her mouth is small, with a soft, trembling upper lip. "
                "No harsh edges, focusing on a fragile, soft, and aristocratic aged Sundanese look."
            ),
            "Nenek Sartini": (
                "An elderly Sundanese grandmother with a wider, rounder facial base and high, flat cheekbones. "
                "Significant sagging in the lower face, creating deep marionette lines that reach the chin. "
                "Her eyes are constantly moist and reddened, suggesting chronic fatigue, with puffy, dark eye bags. "
                "The skin texture is matte, slightly oily in the T-zone, with visible large pores and broken capillaries on the cheeks. "
                "A very realistic double-chin with loose, crepey skin texture. "
                "Her expression is one of deep, silent endurance. Raw and unpolished cinematic detail. "
                "Focusing on the heavy, sagging volume of an aged rural Sundanese face."
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
                "A tiny, terribly frail Sundanese grandmother appearing extremely fragile. "
                "Her small, oval face is consumed by deep, vertical worry lines and incredibly sagging jowls. "
                "Eyes are deeply recessed, looking intensely 'sayu', with heavily reddened and drooping eyelids that show significant bags. "
                "The skin texture is pale, translucent like porcelain, and covered in fine white, dry flakes. "
                "Her lips are thin and pressed tightly together, forming a melancholic, pensive line that emphasizes her quiet suffering. "
                "Neck skin is severely loose, forming multiple deep folds along her shrunken throat. "
                "Prominent blue veins on her temples. An almost ethereal presence of quiet heartbreak. "
                "No smoothing, 100% realistic tired face, looking deeply tired and exhausted."
            ),
            "Kakek Sableng": (
                "A distinguished elderly Indonesian man in his late 70s with a sharp, noble facial structure. "
                "High, prominent forehead with deep horizontal wisdom lines. His nose is straight and firm. "
                "The skin is like old leather, showing deep sun-damage, fine silver-white stubble on a strong jawline. "
                "Eyes are sharp but kind, with heavy lids and dark, realistic eye bags. "
                "Thin silver hair neatly combed back. No filters, strictly raw aged masculinity."
            ),
            "Kakek Sinto": (
                "An extremely aged Javanese man, appearing over 85 years old and very frail. "
                "His face is deeply sunken, showing significant muscle loss and a skeletal bone structure. "
                "Skin is paper-thin and translucent, covered in thousands of fine cross-hatched wrinkles and dark liver spots. "
                "Hollowed cheeks and temples. His eyes are cloudy with cataracts, looking tired and distant. "
                "A thin, wispy white beard and moustache. A profoundly vulnerable and heartbreaking elderly presence."
            ),
            "Kakek Wiryo": (
                "A sturdy, square-faced elderly man in his 60s with a rugged, leathery complexion. "
                "Broad nose and a very strong, thick jawline. His skin is deeply tanned and rough, with large visible pores and sweat-beads. "
                "Deep nasolabial folds and thick, calloused-looking skin on the neck. "
                "Short, messy salt-and-pepper hair. His expression is focused and resilient, showing a lifetime of physical labor. "
                "Raw, unpolished cinematic details focusing on grit and muscle definition."
            ),
            "Kakek Usman": (
                "An elderly grandfather with a small, narrow face contorted in deep grief. "
                "His most striking feature is his reddened, swollen eyes, glistening with heavy moisture and tears. "
                "The skin around his eyes and cheeks is puffy and inflamed from crying. "
                "Deeply furrowed brow and a trembling, quivering lower lip. "
                "Thin, disheveled white hair and a sparse beard. The look of a man who has lost everything. "
                "100% emotional realism, haunting and raw."
            )
        }

        # --- 2. MASTER WARDROBE (6 VARIAN PER KARAKTER - DAILY & NEAT HIJAB) ---
        MASTER_FAMILY_WARDROBE = {
            # --- KELOMPOK NENEK ---
            "Nenek Juminah": {
                "Kebaya Nenek Katun Jadul": "Wearing a very thin, semi-translucent white cotton kebaya with vintage embroidery patterns, fastened by three small rustic safety pins. The fabric shows significant aging and yellowing, paired with a dark brown batik sarong that has a rough, starched texture.",
                "Daster Rayon Kusut & Handuk Leher": "Wearing a limp, faded navy blue rayon daster with large blurry floral prints, showing heavy realistic wrinkles. A small, frayed white hand towel is draped around her neck, tucked slightly into her simple grey jersey bergo hijab.",
                "Baju Kurung Satin Kusam & Kain Lilit": "Wearing a modest, oversized long-sleeved baju kurung made of dull, non-shiny vintage satin in muted olive. The fabric has visible snags and pulls. Paired with a thick, hand-woven cotton cloth wrapped simply over her head as a rustic village hijab.",
                "Kaos Haji Putih & Sarung Lawasan": "Wearing a classic Indonesian 'Kaos Haji' (white long-sleeved undershirt with a small pocket) that looks grayish from many washes. Paired with an extremely faded 'Lawasan' batik sarong and a thin, breathable white instant hijab pinned tightly under the chin.",
                "Tunik Katun Plisket & Bergo Renda": "Wearing a front-buttoned tunic with a unique pleated (plisket) texture in a dusty rose color. The fabric is stiff and weathered. Paired with an old-fashioned instant bergo hijab that has small, yellowed lace (renda) edges around the face.",
                "Daster Kaos Melar & Kerudung Segi Empat": "Wearing an oversized, stretched-out (melar) soft cotton t-shirt style daster in faded maroon. Complemented by a simple square cotton hijab (hijab segi empat) that is folded haphazardly and tied loosely behind her neck, showing a very casual home-stay look."
            },
            "Nenek Sikem": {
                "Kebaya Lurik Kasar & Jarik Lawas": "Wearing a heavy, hand-woven striped 'Lurik' cotton kebaya in dark brown and black, showing a rough and stiff fabric texture. Paired with an extremely weathered, nearly white-faded 'Lawasan' batik jarik and a thin, crumpled cotton scarf wrapped as a makeshift hijab.",
                "Kaos Kerah & Rompi Rajut Tua": "Wearing a modest long-sleeved polo shirt with a collar, layered with a pilling, hand-knitted wool vest in a faded moss green. Complemented by a simple jersey bergo hijab and a thick batik sarong tied high at the waist.",
                "Daster Kancing & Jaket Usang": "Wearing a front-buttoned floral daster, layered with an oversized, thin vintage parachute jacket in a faded navy color. The jacket shows realistic salt-stains and creases. Paired with a simple black instant hijab tucked inside the jacket.",
                "Baju Kurung Beludru Kusam & Kain Lilit": "Wearing a rare, old-fashioned dull velvet (beludru) baju kurung in dark maroon that has lost its shine. The fabric shows heavy wear at the elbows. Paired with a simple thin calico cloth wrapped loosely around her head as a daily hijab.",
                "Kaos Double-Layer & Jarik Cokelat": "Wearing two layers of thin cotton shirts (white inside, faded yellow outside) showing realistic overlapping collars. Paired with a dark chocolate-toned batik jarik with a dense, small-scale pattern and a practical jersey instant bergo.",
                "Kebaya Kutu Baru Polos & Selendang ": "Wearing a very plain, dyed cotton Kutu Baru kebaya in a deep forest green, fastened with a large rusted brooch. A long, frayed 'Slendang' batik cloth is draped diagonally across her chest and shoulder, over her simple white hijab."
            },
            "Nenek Dulah": {
                "Daster Kaos Bertekstur & Handuk Kecil": "Wearing a thick, oversized daily cotton-jersey daster in a faded mustard yellow with tiny pilling textures. A small, well-worn blue hand towel is draped around her neck, tucked into a simple grey instant jersey hijab that shows realistic fabric weight.",
                "Kebaya Nenek Motif Garis & Sarung": "Wearing a very simple, old-fashioned short-sleeved cotton kebaya with thin vertical stripes (motif garis), fastened by a single large silver safety pin. Paired with a dark, mud-stained batik sarong and a thin cotton scarf wrapped tightly around her head.",
                "Kaos Kerah Lengan Panjang & Celana Batik": "Wearing a modest long-sleeved polo shirt in a faded sage green color with a slightly stretched collar. Paired with loose, comfortable batik-patterned cotton trousers and a practical white instant hijab that looks soft and well-washed.",
                "Daster Rayon Kancing & Kerudung Bawal": "Wearing a loose, front-buttoned rayon daster in a dark floral print that has a limp and heavily wrinkled texture. Complemented by a simple square cotton 'bawal' hijab folded into a triangle and tied loosely under her chin, showing a traditional village look.",
                "Tunik Katun Oxford & Sarung Lawasan": "Wearing a sturdy but aged long-sleeved tunic made of thick Oxford cotton in a faded sky blue. Paired with a weathered, yellowish-faded 'Lawasan' batik sarong and a simple black jersey hijab that covers her chest.",
                "Baju Kurung Katun Kasar & Jilbab Slup": "Wearing a humble, loose-fitting baju kurung made of raw, unbleached cotton (katun kasar) in off-white. The fabric shows natural husks and textures. Paired with a practical dark brown 'slup' instant hijab for a quiet, grandmotherly home-stay vibe."
            },
            "Nenek Sartini": {
                "Baju Kurung Teluk Belanga Usang": "Wearing an old-school, faded Baju Kurung Teluk Belanga made of stiff, weathered cotton in a muted mustard color. The neckline shows minor fraying. Paired with a dark, hand-woven songket sarong that has lost its gold-glitter and a simple white cotton bawal hijab pinned tightly.",
                "Kebaya Labuh Brokat Berudul": "Wearing a long, modest Kebaya Labuh made of old-fashioned heavy brocade fabric that is visibly 'berudul' (pilling and fuzzy). The fabric is a dusty lavender color, paired with a faded floral sarong and a thin georgette scarf wrapped loosely around her head.",
                "Tunik Viskosa Kusut & Hijab Bergo": "Wearing a long-sleeved tunic made of limp, heavily wrinkled viscose fabric in a dark forest green. The fabric has a slight oily sheen. Paired with a simple, well-worn grey jersey bergo hijab and a thick cotton sarong wrapped at the waist.",
                "Baju Kurung Pesak Motif Tabur": "Wearing a classic loose Baju Kurung Pesak with a small 'motif tabur' (scattered floral) pattern that has almost faded away. Made of soft, thin cotton. Complemented by a practical black instant hijab that shows a matte, dusty texture.",
                "Kaos Haji Panjang & Kain Panjang Lilit": "Wearing a modest long-sleeved white cotton Kaos Haji (undershirt) showing yellowish sweat stains around the collar. Paired with a dark-toned kain panjang lilit and a simple, breathable white instant hijab pinned under the chin.",
                "Daster Kaos Melayu & Kerudung Bawal Slup": "Wearing a very loose long-sleeved cotton-jersey daster with traditional bold patterns in faded maroon. Paired with a square 'bawal' hijab that is already stitched under the chin (slup style), made of stiff, semi-transparent voile fabric."
            },
            "Nenek Tinah": {
                "Baju Kurung Tulang Belut & Sarung Pudar": "Wearing an old-school Baju Kurung with 'Tulang Belut' stitching around the neck, made of thin, faded cotton in a dusty teal color. The fabric is so worn it looks slightly shiny at the seams. Paired with a red-toned batik sarong that has almost lost its pattern from years of washing.",
                "Kaos Lengan Panjang Melar & Jilbab Slup": "Wearing an oversized, stretched-out (melar) long-sleeved cotton t-shirt in a faded cream color with a small, cracked graphic print on the chest. Paired with a simple black 'slup' instant hijab and a dark-colored daily sarong tied loosely at her waist.",
                "Kebaya Labuh Katun Kasar & Kain Lilit": "Wearing a long-length, modest Kebaya Labuh made of thick but soft raw cotton (katun kasar) in a muted mustard shade. The fabric shows a prominent weave texture. Paired with a thin cotton scarf wrapped twice around her head as a simple, rustic village hijab.",
                "Tunik Rayon Floral & Bergo Kaos": "Wearing a limp, heavily wrinkled rayon tunic with a blurry floral motif in faded purple. The material hangs loosely on her fragile body. Paired with a well-worn grey instant bergo hijab that has a small, faded watermark on the side.",
                "Baju Kurung Pesak & Selendang Batik": "Wearing a classic, wide-fitting Baju Kurung Pesak in a solid, dusty olive color. Instead of a modern hijab, a long, thin batik 'selendang' is wrapped meticulously around her head and pinned under the chin in an old-fashioned way.",
                "Daster Kaos & Jaket Kardigan Tua": "Wearing a daily cotton daster, layered with an old, pilling knitted cardigan in a faded charcoal color. The cardigan has one missing button. Paired with a simple white jersey hijab tucked inside the cardigan, looking very humble and realistic."
            },
            "Nenek Wati": {
                "Daster Kaos & Celemek Kain Usang": "Wearing a thick cotton-jersey daster in a faded brick-red color, covered by a handmade waist apron (celemek) made from a recycled flour sack with faded blue markings. The daster shows heavy pilling and realistic fabric folds at the lap.",
                "Kaos Polo Pudar & Sarung Kotak": "Wearing a modest long-sleeved polo shirt in a deeply faded charcoal color with a frayed collar. Paired with a thick, traditional checked 'sarung pelikat' in dark green and a simple grey instant jersey hijab that covers her shoulders.",
                "Kebaya Nenek Motif Polkadot & Handuk Kecil": "Wearing a very old-fashioned short-sleeved cotton kebaya with a faded white polkadot pattern on a navy base, fastened by a rusty gold brooch. A small, well-worn white hand towel is draped over her shoulder, paired with a thin cotton hijab.",
                "Tunik Katun Oxford & Kerudung Ikat": "Wearing a sturdy but heavily wrinkled long-sleeved tunic made of thick Oxford cotton in a faded olive green. Instead of an instant hijab, she wears a square cotton scarf wrapped and tied haphazardly behind her neck, showing a very authentic rural home look.",
                "Baju Kurung Rayon & Jilbab Slup": "Wearing a limp, semi-translucent baju kurung made of old rayon fabric in a blurry floral print. The fabric has visible snags and a slight oily sheen from age. Paired with a simple black 'slup' instant hijab that looks soft and well-washed.",
                "Kaos Haji & Rompi Katun Tua": "Wearing a classic white 'Kaos Haji' (long-sleeved undershirt) with a visible small pocket, layered with a thin, faded tan cotton vest. Paired with a dark-brown batik sarong and a simple, breathable white instant hijab pinned tightly under her chin."
            },

            # --- KELOMPOK KAKEK ---
            "Kakek Sableng": {
                "Kemeja Batik Sogan & Peci": "Wearing an old, long-sleeved batik shirt with a faded brown Sogan pattern, looking stiff and weathered. Paired with a classic black velvet Peci that shows signs of dust, and a dark sarong tied high.",
                "Baju Koko Putih & Sajadah Bahu": "Wearing a humble white cotton Baju Koko with subtle embroidery, fabric showing grayish discoloration from age. A thin green prayer mat is draped over his left shoulder, paired with a black Peci.",
                "Jas Tua (Vintage) & Sarung": "Wearing an oversized, dusty dark vintage blazer over a plain white undershirt. The sleeves are slightly too long for his thin arms, paired with a faded checked sarong, looking dignified but lonely.",
                "Kaos Haji & Sorban Sampir": "Wearing a classic white 'Kaos Haji' with a small front pocket. A long, thin white turban (sorban) is loosely draped over his shoulders. Paired with a dark-toned sarong, looking very spiritual and elderly.",
                "Tunik Katun & Celana Komprang": "Wearing a modest, loose-fitting long-sleeved cotton tunic in faded tan. Paired with traditional black loose trousers (komprang) and a weathered sarong slung over his shoulder.",
                "Baju Kurung Lelaki & Peci Putih": "Wearing a very simple, loose-fitting Malay-style Baju Kurung in a faded olive color. Paired with a simple white prayer cap (kupluk) and a dark batik sarong, looking fatherly."
            },
            "Kakek Sinto": {
                "Kaos Singlet Kuning & Sarung": "Wearing a thin, yellowed-white ribbed singlet (singlet swan) that shows his fragile collarbones and bony shoulders. Paired with a soft, extremely faded 'Lawasan' batik sarong wrapped high around his chest.",
                "Kaos Haji & Kupluk Putih": "Wearing a grayish, well-worn white 'Kaos Haji' showing pilling textures. Paired with a thin white knitted prayer cap (kupluk) and a simple brown sarong that looks too large for his shrunken frame.",
                "Kemeja Katun Tipis & Peci Miring": "Wearing a very thin, short-sleeved cotton shirt in faded beige with one button missing. A weathered black Peci is perched slightly tilted on his head, showing a weary and fragile village look.",
                "Sarung Sampir & Dada Terbuka": "He is shirtless but has an old, faded batik cloth draped over his thin shoulders like a shawl. Paired with a weathered sarong tied with a simple piece of plastic string at the waist.",
                "Baju Lurik Usang & Caping": "Wearing an old, dark-striped 'Lurik' jacket with frayed cuffs. He holds a traditional straw 'caping' hat. The fabric looks rough and heavy on his thin body, paired with a faded dark sarong.",
                "Kaos Panjang Melar & Sarung Pelikat": "Wearing a charcoal grey long-sleeved t-shirt with a stretched-out (melar) collar. Paired with a patterned 'sarung pelikat' in muted blue and green checks that looks dusty and worn-out."
            },
            "Kakek Wiryo": {
                "Kaos Oblong Abu & Handuk Leher": "Wearing a sweat-stained charcoal grey cotton t-shirt with visible pilling. A small, frayed red-and-white checkered towel is draped around his neck. Paired with a thick, dark-colored sarong.",
                "Kemeja Flanel & Sarung Wadimor": "Wearing a rugged, short-sleeved plaid flannnel shirt in faded red and black checks. Paired with a patterned 'Wadimor' daily sarong in dark blue tied tightly at his waist, looking resilient.",
                "Baju Koko Putih & Peci Hitam": "Wearing a sturdy but stained white Baju Koko showing grease marks from work. Paired with a classic black Peci and a dark checked sarong, showing the look of a hardworking grandfather.",
                "Kaos Kerah & Jaket Parka Tua": "Wearing a faded navy polo shirt layered with an old, thin vintage parka jacket in olive green. The jacket shows realistic salt-stains and creases, paired with a sturdy dark sarong.",
                "Kemeja Safari & Peci Haji": "Wearing a short-sleeved khaki safari shirt with multiple pockets, looking very old-school. Paired with a simple white prayer cap and a patterned sarong in muted brown tones.",
                "Kaos Putih & Sarung Gajah Duduk": "Wearing a simple plain white cotton t-shirt that looks thin and grayish. Paired with a classic 'Gajah Duduk' checked sarong in muted green and orange tied traditionally at the waist."
            },
            "Kakek Usman": {
                "Baju Koko Biru & Peci Berdebu": "Wearing a heavily wrinkled, dark blue Baju Koko made of soft rayon fabric. His black Peci looks dusty and misshapen. Paired with a dark-toned sarong that looks disheveled and untidy.",
                "Kemeja Cokelat & Tasbih Kayu": "Wearing a plain, faded brown cotton shirt with two missing buttons. He holds a string of dark wooden prayer beads (tasbih) in his trembling hands. Paired with a weathered, dark-grey sarong.",
                "Kaos Panjang Putih & Jilbab Sampir": "Wearing a grayish, well-worn white long-sleeved t-shirt. A faded batik cloth is draped over his head and shoulders like a makeshift shawl, emphasizing his deep vulnerability and grief.",
                "Tunik Katun Kusut & Sarung Pudar": "Wearing a long-sleeved cotton tunic in a faded charcoal color that hangs loosely. Paired with an extremely faded, soft batik sarong that has lost its pattern, looking very poor and sad.",
                "Daster Kaos & Jaket Rajut Tua": "Wearing a simple daily cotton daster (unisex home wear), layered with an old, pilling knitted cardigan in a faded charcoal color. Paired with a simple white Peci, looking very humble and lonely.",
                "Kaos Oblong Putih & Sarung Melintir": "Wearing a thin, grayish white oblong t-shirt with a stretched collar. His sarong is tied haphazardly and looks twisted (melintir) at the waist. His expression is one of complete despair."
            }
        }

        # --- 3. MASTER BAHAN (ARCHITECTURAL PRECISION: FRUIT LUXURY EDITION) ---
        MASTER_KONTEN_ALL = {
            "🕌 Miniatur Masjid": {
                "Buah Semangka": (
                    "A monumental 1-meter mosque diorama built with architectural precision from watermelon anatomy. "
                    "The walls are composed of millions of pressurized, ruby-red watermelon cubes with a glistening, high-moisture finish. "
                    "The main dome is a sphere of translucent, polished watermelon flesh, glowing with a soft, internal 'Ember Amber' LED light that reveals the organic cellular structure. "
                    "Inside the dome, thousands of black seeds are meticulously arranged in sacred geometric patterns, silhouetted against the warm internal glow. "
                    "Minarets of dark-green striped rind are subtly traced with thin, steady warm-white fiber-optic lines, avoiding aggressive flickering. "
                    "The lighting is cinematic and moody, seeping through the red fruit like a glowing hearth."
                ),
                "Buah Strawberry": (
                    "A gigantic 1-meter mosque model constructed from high-density strawberry slices. "
                    "The facade is a masterwork of texture, featuring the pitted red skin of the fruit with thousands of tiny yellow seeds acting as natural golden rivets. "
                    "The colossal dome is made of translucent strawberry-infused crystal gelatin, illuminated by a deep 'Crimson Dusk' internal wash light that creates a soft, diffused halo. "
                    "Instead of bright neon, the arches are outlined with a dim, steady rose-gold glow that accentuates the fruit's natural curves. "
                    "The minarets are capped with fresh green leaves, illuminated from below by subtle warm-white spotlights, creating a sophisticated and organic masterpiece."
                ),
                "Buah Nanas": (
                    "A grand 1-meter standalone mosque object built from interlocking geometric pineapple rind segments. "
                    "The diamond-patterned skin creates a rugged, golden-brown architectural armor. "
                    "The main dome is a massive sphere of carved, succulent yellow pineapple, glowing with a 'Champagne Solar' internal LED that highlights the fibrous golden veins of the fruit. "
                    "The sharp, spiked green crowns of the pineapple form the minaret towers, lit with a very dim, steady emerald-green wash from the base. "
                    "No neon strips; instead, the light 'bleeds' naturally through the gaps in the rind, creating a rhythmic and high-luxury play of light and shadow."
                ),
                "Buah Melon": (
                    "A colossal 1-meter diorama built from honeydew and cantaloupe melon. "
                    "The walls showcase the intricate, reticulated 'net' texture of the rind, looking like aged ivory carvings. "
                    "The colossal main dome is made of translucent pale-jade melon flesh, filled with a 'Starlight Mint' internal lighting scheme—thousands of micro-fiber optic points that twinkle like a distant galaxy. "
                    "The minarets are smooth, polished rinds with a soft, steady turquoise glow emanating from the window slits. "
                    "The overall lighting is soft, ethereal, and diffused, making the mosque appear like a glowing emerald sanctuary in a quiet, twilight atmosphere."
                ),
                "Buah Naga": (
                    "A monumental 1-meter mosque object built from the vibrant anatomy of Dragonfruit. "
                    "The walls are covered in overlapping magenta rind scales with lime-green tips, creating a futuristic 'organic armor' look. "
                    "The colossal main dome is a sphere of translucent white dragonfruit flesh, embedded with millions of tiny black seeds that create a natural 'stardust' texture. "
                    "Inside, a 'Cyber-Violet' internal LED glow pulses slowly, making the seeds look like a floating galaxy trapped in ice. "
                    "Minarets are built from twisted magenta rinds, illuminated with thin, steady electric-pink fiber-optic lines that accentuate the sharp scales."
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
                "Buah Pisang": (
                    "A monumental 1-meter mosque diorama built from the complete anatomy of a banana tree. "
                    "The walls are crafted from layers of fresh, waxy green banana leaves with deep, parallel ribbing textures. "
                    "The colossal main dome is a sphere made of thousands of curved, bright yellow banana slices, glowing from within with a 'Soft Canary' LED scheme that highlights the tiny black seeds in the center. "
                    "Tall minarets are built from the textured, fibrous stalks of the banana bunch, wrapped in steady warm-white fiber-optic lines. "
                    "All entrance arches are outlined with a dim, steady lime-green neon glow, reflecting off the glossy, organic surface of the leaves."
                ),
                "Buah Manggis": (
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
                "Kelapa": (
                    "A monumental 1-meter mosque diorama built from the rugged anatomy of Coconuts. "
                    "The walls feature the raw, fibrous brown texture of coconut husks (sabut) and polished dark-brown coconut shells (batok). "
                    "The colossal main dome is made of translucent, snowy-white coconut flesh with a high-gloss finish, glowing from within with a 'Crystal White' LED that highlights the organic ridges. "
                    "Minarets are crafted from stacked coconut shells, wrapped in steady warm-white fiber-optic lines that accentuate the rough fibers. "
                    "The lighting is humble yet dignified, seeping through the fibrous cracks of the husk against a dark, moody background."
                ),
                "Buah Markisa": (
                    "A gigantic 1-meter mosque model built from Passionfruit anatomy. "
                    "The exterior walls are made of dark, shriveled purple skins showing intense, realistic organic wrinkles. "
                    "The colossal main dome is a sphere of translucent orange passionfruit pulp, where millions of crunchy black seeds are suspended like a swirling galaxy. "
                    "Inside, a 'Solar Flare' golden LED scheme makes the seeds look like a floating nebula trapped in glass. "
                    "Every minaret is a pillar of purple rind wrapped in thin, steady violet neon strips, casting a powerful, saturated glow over the wet, glossy fruity interior."
                ),
                "Daun Pisang": (
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
                "Daun Kelapa": (
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
                "Anyaman Bambu": (
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
                "Tanah Liat": (
                    "A monumental 1-meter mosque built from raw, sun-dried clay and coconut fibers. "
                    "The walls feature intense, hyper-detailed 'Cracked Earth' textures with realistic fissures and dusty debris. "
                    "The main dome is a sphere of baked terracotta, glowing with a 'Smoldering Ember' red LED seeping through the cracks. "
                    "The look is ancient, rugged, and deeply connected to the land, matching the weary faces of the elderly characters."
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
                "Bungkus Mie Bekas": (
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
            "Sudut Dapur Tungku": (
                "Sitting on a low wooden stool (dingklik) next to a traditional clay wood-fire stove (tungku). "
                "The background is a solid wall of soot-covered bricks (tembok pawon) with deep black carbon stains. "
                "The floor is hard-packed earth with scattered wood ash and charcoal bits. "
                "Surrounding objects: a soot-blackened kettle, a pile of dry firewood, and an old coconut shell dipper (gayung batok). "
                "Atmospheric smoky haze with thin light beams (God rays) hitting the dust particles."
            ),
            "Teras Bambu Remang": (
                "Sitting on an old, creaky bamboo platform (lincak) under a low-hanging thatched roof. "
                "The background is a dark, out-of-focus village garden with banana leaf silhouettes. "
                "Next to her is a dim kerosene lamp (lampu templok) casting a soft amber glow on the diorama. "
                "Surrounding objects: an old sarong draped on the rail, a coil of mosquito coil (obat nyamuk bakar) with its ash, and a chipped enamel mug. "
                "Focus on the 'Wet-Look' of the village air after rain."
            ),
            "Gudang Kayu Tua": (
                "Sitting on the floor of a dark wooden shed filled with antique farm tools. "
                "The background is a solid wall of rough-hewn timber planks with visible woodworms and cobwebs in the corners. "
                "The floor is covered in a layer of fine sawdust and dry teak leaves. "
                "Surrounding objects: a rusted sickle (arit), a pile of old burlap sacks (karung goni), and a broken wooden ladder. "
                "The lighting is a single dramatic spotlight from a hole in the roof, hitting the diorama mosque."
            ),
            "Lantai Ubin Motif Jadul": (
                "Sitting on a classic 'Ubin PC' (vintage cement tiles) with faded floral patterns and weathered cracks. "
                "The background is a solid whitewashed wall with peeling paint and mossy damp patches (rembesan air). "
                "Next to her is a small wooden radio playing static, a plate of steamed bananas, and an old pair of 'Sandal Jepit' with a wire repair. "
                "Focus on the contrast between the cold patterned floor and the humble handcrafted diorama."
            ),
            "Bawah Pohon Sawo": (
                "Sitting directly on the ground under the deep shade of an old fruit tree. "
                "The floor is a mix of dry soil, small river stones, and fallen brown leaves. "
                "The background is the thick, gnarled trunk of the tree with realistic bark texture. "
                "Surrounding objects: a bamboo rake (garu), an old plastic bucket filled with water, and a few chickens scratching the dirt nearby. "
                "Natural, high-contrast sunlight filtered through leaves (bokeh effect)."
            )
        }
        # --- 4. MASTER AUDIO & SOULFUL EXPRESSION (FIXED WORKSHOP INTERACTION) ---
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
            # --- BARIS 1: MODUS KONTEN (OTAK UTAMA) ---
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

                # 4. TEXT AREA (Kuncinya di parameter 'key')
                user_dialog = st.text_area(
                    "Input Dialog", 
                    placeholder=f"Tulis dialog {char_key.split(' (')[0]} di sini...",
                    height=250, 
                    label_visibility="collapsed",
                    key="input_dialog_key" # Ini nyambung ke handle_kocok
                )  
                # Update state biar sinkron
                st.session_state.current_dialog = user_dialog

            with c6:
                st.markdown('<p class="small-label">ACTING & PERFORMANCE</p>', unsafe_allow_html=True)
                pilih_logat = st.selectbox("Pilih Logat", MASTER_AUDIO_STYLE["Logat"])
                pilih_mood = st.selectbox("Pilih Mood", MASTER_AUDIO_STYLE["Mood"])
                
                # --- GANTI DI SINI: Dari random jadi selectbox ---
                pilih_aksi = st.selectbox("Pilih Gerakan Tubuh", MASTER_AUDIO_STYLE["Physical Action"])

            st.write("")
            btn_gen = st.button(
                "🚀 GENERATE VIDEO PROMPT", 
                type="primary", 
                use_container_width=True, 
                key="btn_generate_video"
            )
        # --- LOGIC GENERATOR (TOTAL REBUILD: ULTRA SHARP & CLEAN VISUAL) ---
        if btn_gen:
            # 1. POSISI MATI LESEHAN
            posisi_nenek = "sitting cross-legged on the ground (lesehan)"
            
            # 2. KUNCI KETAJAMAN & CLEAN STATIC VISUAL (MENDUNG NATURAL)
            scene_context = (
                f"ULTRA-HD 8K RESOLUTION. HYPER-REALISTIC RAW PHOTO. "
                f"MANDATORY: NO TEXT, NO SUBTITLES, NO CAPTIONS. "
                # --- UPDATE LIGHTING: MENDUNG SORE NATURAL ---
                f"LIGHTING: 4 PM late afternoon with a soft dark-grey overcast sky, subtle thin cloud layers, no harsh sun. "
                f"CONTRAST: Intense glowing LED light contrast against dark cloudy sky, making the colors pop intensely. " # <-- Kalimat sakti lo!
                # --- POSITIONING: JARAK 1 METER & URUTAN LURUS ---
                f"CAMERA DISTANCE: Close-up 1 meter distance from lens to mosque. "
                f"ALIGNMENT: Strictly symmetrical. Mosque is in foreground center, {posisi_nenek} is directly behind the mosque. "
                # --- CAMERA: STATIS TOTAL ---
                f"CAMERA MOVEMENT: Strictly STATIC camera, zero movement, zero shake, zero zoom, zero slide. "
                f"FIXED AXIS: Perfectly level 0-degree eye level, locked tripod position. "
                # --- SHARPNESS: ANTI BLUR ---
                f"DEEP FOCUS: F/16 Aperture, everything from mosque to background is CRYSTAL CLEAR, zero blur, zero bokeh."
            )

            # 3. AMBIL DATA MASTER
            env_detail = MASTER_GRANDMA_SETTING.get(pilihan_set, "Natural outdoor setting.")
            soul_desc = MASTER_FAMILY_SOUL.get(pilihan_user, "An Indonesian person.")
            wardrobe_dict = MASTER_FAMILY_WARDROBE.get(char_key, {})
            baju_desc = wardrobe_dict.get(baju_pilihan, "Simple modest clothes.")
            
            # 4. KUNCI ANATOMI & HIJAB
            ANATOMY_LOCK = "STRICTLY TWO HUMAN HANDS, five fingers each. No ghost limbs."
            MANDATORY_LOCK = "MANDATORY: FULL HIJAB. NO HAIR SHOWING. FULLY COVERED MODEST CLOTHING."

            # --- 4.5 FILTER PEMBERSIH (HANYA AMBIL DALAM KURUNG) ---
            # Kode ini bakal buang teks Indo dan cuma ambil teks Inggris di dalam kurung
            aksi_final = pilih_aksi.split('(')[-1].strip(')') if '(' in pilih_aksi else pilih_aksi
            mood_final = pilih_mood.split('(')[-1].strip(')') if '(' in pilih_mood else pilih_mood
            logat_final = pilih_logat.split('(')[-1].strip(')') if '(' in pilih_logat else pilih_logat
                
            # 5. FINAL ASSEMBLY (FIXED: STATIC, SHARP, & MOODY NATURAL)
            final_ai_prompt = (
                f"{scene_context} \n\n"
                f"CHARACTER DNA: {soul_desc}. {ANATOMY_LOCK} {MANDATORY_LOCK} \n"
                f"WARDROBE: {baju_desc}. \n"
                f"ENVIRONMENT: {env_detail}. \n"
                f"PERFORMANCE: {aksi_final}. Mood: {mood_final}. \n" 
                f"THE MASTERPIECE: {deskripsi_teknis}. \n"
                f"DIALOG CONTEXT: '{user_dialog}' delivered with {logat_final} accent. \n\n"
                # --- TECHNICAL: KUNCI STATIS, TAJAM, & ANTI-BADAII ---
                f"TECHNICAL SPECS: Shot on ARRI Alexa 65, 24mm lens, F/16 Aperture, Deep Focus. "
                f"CAMERA LOGIC: Strictly STATIC camera, zero movement, perfectly level 0-degree eye-level angle. " 
                f"VISUAL: Ultra-sharp 8K, high-contrast colors, zero motion blur, global shutter. "
                # --- NEGATIVE PROMPT: BUANG SEMUA SAMPAH VISUAL ---
                f"NEGATIVE PROMPT: thunderstorm, heavy black clouds, storm, rain, " # <-- Anti kiamat
                f"blurry, bokeh, depth of field, out of focus, shaky, motion blur, " 
                f"chair, table, furniture, text, watermark, side-view, tilted, distorted."
            )

            # --- 7. TAMPILKAN HASIL ---
            st.success("🔥 PROMPT MASJID READY!")
            st.markdown('<p class="small-label">SALIN PROMPT DI BAWAH INI:</p>', unsafe_allow_html=True)
            st.code(final_ai_prompt, language="text")
                
    # ==========================================================================
    # TAB 2: MASJID VERSI BARU
    # ==========================================================================
    with t_masjid_v2:
        st.status("Sedang proses pembuatan...", expanded=False)

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
