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
                "Semangka": (
                    "A monumental 1-meter mosque diorama built with architectural precision from watermelon anatomy. "
                    "The walls are composed of millions of pressurized, ruby-red watermelon cubes with a glistening, high-moisture finish. "
                    "The main dome is a sphere of translucent, polished watermelon flesh, glowing with a soft, internal 'Ember Amber' LED light that reveals the organic cellular structure. "
                    "Inside the dome, thousands of black seeds are meticulously arranged in sacred geometric patterns, silhouetted against the warm internal glow. "
                    "Minarets of dark-green striped rind are subtly traced with thin, steady warm-white fiber-optic lines, avoiding aggressive flickering. "
                    "The lighting is cinematic and moody, seeping through the red fruit like a glowing hearth."
                ),
                "Strawberry": (
                    "A gigantic 1-meter mosque model constructed from high-density strawberry slices. "
                    "The facade is a masterwork of texture, featuring the pitted red skin of the fruit with thousands of tiny yellow seeds acting as natural golden rivets. "
                    "The colossal dome is made of translucent strawberry-infused crystal gelatin, illuminated by a deep 'Crimson Dusk' internal wash light that creates a soft, diffused halo. "
                    "Instead of bright neon, the arches are outlined with a dim, steady rose-gold glow that accentuates the fruit's natural curves. "
                    "The minarets are capped with fresh green leaves, illuminated from below by subtle warm-white spotlights, creating a sophisticated and organic masterpiece."
                ),
                "Nanas": (
                    "A grand 1-meter standalone mosque object built from interlocking geometric pineapple rind segments. "
                    "The diamond-patterned skin creates a rugged, golden-brown architectural armor. "
                    "The main dome is a massive sphere of carved, succulent yellow pineapple, glowing with a 'Champagne Solar' internal LED that highlights the fibrous golden veins of the fruit. "
                    "The sharp, spiked green crowns of the pineapple form the minaret towers, lit with a very dim, steady emerald-green wash from the base. "
                    "No neon strips; instead, the light 'bleeds' naturally through the gaps in the rind, creating a rhythmic and high-luxury play of light and shadow."
                ),
                "Melon": (
                    "A colossal 1-meter diorama built from honeydew and cantaloupe melon. "
                    "The walls showcase the intricate, reticulated 'net' texture of the rind, looking like aged ivory carvings. "
                    "The colossal main dome is made of translucent pale-jade melon flesh, filled with a 'Starlight Mint' internal lighting scheme—thousands of micro-fiber optic points that twinkle like a distant galaxy. "
                    "The minarets are smooth, polished rinds with a soft, steady turquoise glow emanating from the window slits. "
                    "The overall lighting is soft, ethereal, and diffused, making the mosque appear like a glowing emerald sanctuary in a quiet, twilight atmosphere."
                ),
            },
            # --- 3. MASTER KONTEN (🌍 WORLD MOSQUE DIORAMA - CRAFT SCALE EDITION) ---
            "🌍 Diorama Masjid": {
                "Masjidil Haram": "A hyper-detailed 1-meter standalone diorama of Masjidil Haram, frozen in a static moment of peak crowd. Millions of 2-millimeter scale static miniature figures in white robes are positioned in mid-stride, captured in a massive circular formation around the Kaaba. The figures are fixed, motionless plastic/resin models. The architecture is pure white polished marble with gold leaf. The Kaaba stands still in the center with its textured black silk Kiswah. Glowing with 'Champagne Solar' LED lights from the fixed minarets.",
                "Al-Aqsa": "A monumental 1-meter static diorama of the Al-Aqsa compound. Thousands of tiny, motionless figures are captured in various still poses: some walking through the arches, some standing in silent rows for prayer in the courtyard. Every figure is a fixed, non-moving miniature. The Dome of the Rock features a stationary hammered-gold surface with intense amber LED glow. The ancient limestone textures are sharp and frozen. The atmosphere is silent and still, illuminated by flickering (light-only) fairy lights on the fixed trees.",
                "Nabawi": "A colossal 1-meter static diorama of the Prophet's Mosque (Nabawi) in Madinah. Featuring the iconic Green Dome and the giant stationary mechanical umbrellas in an open position. Thousands of static miniature pilgrims are frozen in place throughout the vast marble courtyards. The green dome glows with a 'Sacred Emerald' LED scheme. Every architectural detail is captured in a silent, motionless state. High-contrast lighting between the white marble and the dark-green shadows.",
                "Masjidil Haram (Ottoman Era)": "A detailed 1-meter high diorama object depicting the historical Masjidil Haram complex during the Ottoman period (19th century). The Kaaba is central, surrounded by low-rise stone buildings with multiple small, lead-domed roofs and slender, pencil-shaped minarets. The courtyard is paved with ancient weathered stone. Hundreds of motionless miniature figures are praying in circles. The entire structure of ancient red brick and rough stone is wrapped in flickering warm-white fairy lights, glowing with 'Ancient Torchlight' amber LED light. A static, quiet, historical moment.",
                "Masjidil Haram (tahun 2030)": "A colossal, hyper-futuristic 1-meter standalone diorama of Masjidil Haram as envisioned in Vision 2030. The Kaaba is encircled by a massive, multi-tiered ring of modern architecture (Mataf Bridge) made of carbon fiber, glass, and polished gold. The roofs are kinetic, open-structure designs. Millions of static miniature pilgrims are frozen in place throughout the vast complex. Glowing with a 'Cyber-Neon Makkah' LED scheme (electric cyan, white-hot, and violet) reflecting off the glass and futuristic metallic surfaces. A static, breathtaking vision of the future.",
                "Masjidil Haram (tahun 90an)": "A grand, symmetrical 1-meter high diorama of Masjidil Haram after the King Fahd expansion. Featuring the massive white structure with its iconic two twin minarets and expansive white marble courtyards. Thousands of motionless pilgrims are frozen in various prayer poses. The architecture is pure white polished stone with elegant gold-filigree calligraphy. Illuminated by a 'Divine White' LED scheme (pure white, soft cream, and gold) reflecting off the smooth marble surfaces. A static, solemn, and grand moment from the 90s.",
                "Masjidil Haram (Zaman Nabi)": "A high-detailed 1-meter standalone diorama of Makkah during the early years of Islam. The central Kaaba is built from rough, jagged black mountain stones with a simple textured cover. Around it is a dusty desert courtyard (Mataf) made of dry golden sand. Surrounding the Kaaba are clusters of ancient Makkan houses built from mud-bricks, rough stones, and palm leaf roofs. Millions of tiny miniature figures are gathered in small groups. Glowing with a 'Desert Moonlight' LED scheme (pale moonlight white and dim amber oil-lamp flickers) reflecting off the sand and rough stones. The atmosphere is raw, ancient, and deeply spiritual.",
                "Kaaba Cut-Away (Interior Reveal)": "A unique 1-meter high cross-section diorama of the Holy Kaaba. One half of the Kaaba is a solid black silk-textured exterior, while the other half is sliced open to reveal the hyper-detailed interior. Inside features three tall, dark-wood pillars (teak), golden hanging lamps, and green-marble tiled floors with intricate Arabic calligraphy on the inner walls. The interior glows with an intense 'Golden Secret' LED scheme (bright 24K gold, warm amber) focused solely on the internal chamber, while the exterior remains in soft shadows. A static, educational architectural masterpiece.",
                "Masjidil Haram (The Golden Details)": "A monumental 1-meter high diorama focusing on the intricate details around the Kaaba. Features the hyper-detailed gold-lattice structure of Maqam Ibrahim and the smooth white marble curve of Hijr Ismail. The Kaaba stands majestic with its heavy gold-embroidered calligraphy on the black silk. Millions of tiny static pilgrims are filling the Mataf area. Illuminated by a 'Divine Gold' LED scheme (24K gold, warm amber, and white-hot spark) highlighting the golden ornaments and the texture of the Kiswah. A static masterpiece of sacred craftsmanship.",
                "Masjid Nabawi": "A magnificent 1-meter high standalone diorama of the Prophet's Mosque in Madinah. Featuring the iconic bright-green central dome and dozens of giant, static open hydraulic umbrellas with intricate cream-colored fabric textures. The architecture is built from white marble with golden floral inlays. Thousands of static miniature pilgrims are frozen in the vast courtyard. Glowing with a 'Sacred Emerald' LED scheme (vibrant green on the dome, warm amber under the umbrellas) reflecting off the polished floor. A static, breathtaking spiritual masterpiece.",
                "Sheikh Zayed Grand Mosque": "A colossal 1-meter high diorama made of pure white crystalline marble. Featuring 82 domes of various sizes and four 107-meter tall minarets. The courtyard features hyper-detailed floral marble mosaics. The entire structure is surrounded by static 'mirrored water' pools made of blue tinted glass. Glowing with a 'Lapis Lazuli' LED scheme (electric blue and cool white) that creates a celestial atmosphere. Thousands of tiny static figures are walking through the grand arches. High-luxury architectural detail.",
                "Masjid Agung Xi'an": "A unique 1-meter high diorama of the Great Mosque of Xi'an, featuring traditional Chinese Pagoda architecture. Built from dark aged wood, turquoise-glazed roof tiles, and intricate dragon-style carvings. Instead of domes, it features grand pavilions and Chinese gateways (Paifang). The walls are covered in Arabic calligraphy stylized in Chinese brush-stroke patterns. Glowing with an 'Oriental Zen' LED scheme (warm red, soft jade green, and dim gold) illuminating the wooden courtyards. A static, rare cultural fusion masterpiece.",
                "Masjid Istiqlal": "A monumental 1-meter high standalone diorama of the National Mosque of Indonesia, Istiqlal. The architecture features a massive stainless steel dome and a single tall minaret, built with a 'Brutalist-Grand' aesthetic using grey marble and steel. The interior is sliced open to show the 12 massive stainless steel pillars and the intricate geometric patterns on the dome's underside. Thousands of tiny static figures are frozen in the vast, open prayer halls. Glowing with a 'Modern Steel' LED scheme (cool white, pale silver, and bright industrial white) reflecting off the metal and marble surfaces. A static, solemn, and powerful masterpiece.",
                "Masjid Al-Jabbar": "A breathtaking 1-meter high standalone diorama of the 'floating' Al-Jabbar mosque. The architecture features a colossal, multi-layered roof shaped like a blooming geometric flower, built from thousands of interlocking glass panels. The structure is surrounded by a 'mirrored water' lake made of blue-tinted glass. Thousands of tiny static figures are walking across the bridges and courtyards. Glowing with a 'Techno-Religious' LED scheme (vibrant violet, electric blue, and warm gold) pulsing through the glass facets, creating a kaleidoscopic glow on the water. A static, futuristic, and colorful architectural marvel.",
                "Masjid Raya Solo": "A monumental 1-meter high standalone diorama of the Sheikh Zayed Grand Mosque in Solo. The architecture features a mini-version of the Abu Dhabi masterpiece with four tall minarets and dozens of white marble domes. The structure is built from pure white stone with intricate gold-leaf floral accents. The floors feature hyper-detailed batik-inspired marble mosaics. Thousands of tiny static figures are walking through the arched courtyards. Glowing with a 'Celestial Moon' LED scheme (icy white, soft lavender, and bright gold) reflecting off the polished marble. A static, high-luxury architectural marvel in the heart of Java.",
                "Masjid Keraton": "A high-detailed 1-meter standalone diorama of the historical Grand Mosque of the Surakarta Palace. The architecture features a traditional Javanese 'Tajug' multi-tiered roof made of dark weathered wood and clay tiles. The structure is supported by massive teak wood pillars (Soko Guru) with intricate 'Ultah' gold carvings. Features the iconic 'Gapura' entrance and a moat (parit) surrounding the mosque. Thousands of tiny static figures are frozen in traditional Javanese attire (Batik and Blangkon). Glowing with a 'Royal Heritage' LED scheme (warm amber, flickering torchlight, and deep gold) reflecting off the dark wood. A static, ancient, and deeply cultural masterpiece.",
                "Masjid Gedhe Kauman ": "A magnificent 1-meter high standalone diorama of the Great Mosque of the Yogyakarta Sultanate. The architecture features a grand triple-tiered Javanese 'Tajug' roof made of dark-brown ancient wood and traditional clay tiles, topped with a golden 'Mustaka' ornament. The structure is built with massive teak wood pillars and features a large front porch (Serambi) with intricate yellow and green royal carvings. Thousands of tiny static figures in traditional Javanese Batik and Beskap are frozen in prayer. Glowing with a 'Keraton Moonlight' LED scheme (warm amber, soft yellow, and dim flickering torchlight) illuminating the dark wood and white stone walls. A static, deeply spiritual, and historical masterpiece.",
                "Masjid Jogokariyan": "A high-detailed 1-meter standalone diorama of the iconic Masjid Jogokariyan in its vibrant evening atmosphere. The architecture features the famous green and cream facade with the prominent 'Masjid Jogokariyan' signage. The diorama captures the lively street-side atmosphere with hundreds of static miniature figures gathered for Iftar or prayers. The structure features a blend of modern and traditional Javanese elements. Glowing with a 'Community Glow' LED scheme (bright warm-white, festive green neon, and soft orange) creating a welcoming and busy urban-mosque vibe. A static masterpiece of modern Indonesian Islamic culture."
                    
            }
        }

        # --- 3. MASTER LOKASI (FIXED: NATURAL CLUTTER & SOLID BACKDROP) ---
        MASTER_GRANDMA_SETTING = {
            "Lantai Semen & Tembok Retak": (
                "Sitting cross-legged directly on a cold, unpolished grey cement floor (plesteran) with visible sandy textures and fine cracks. "
                "The background is a solid wall of raw, unpainted grey cement with weathered water stains and rough patches. "
                "Next to her is a glass of tea with a rusty metal lid, a pair of old rubber sandals (sandal jepit), and a small plastic plate with boiled cassava. "
                "Focus on the gritty concrete texture and the raw, unpolished stone-like environment."
            ),
            "Tikar Mendong & Dinding Gedek": (
                "Sitting cross-legged on a hand-woven natural 'Tikar Mendong' straw mat with frayed edges and organic fiber textures. "
                "The background is a solid wall of old, woven bamboo sheets (gedek) with dust particles trapped in the weaves and greyish fading fibers. "
                "Surrounding objects: a traditional hand-woven leaf fan (kipas bambu), an old analog radio, and a small tin box for betel nut (sirih). "
                "Focus on the organic, dry texture of the bamboo and straw."
            ),
            "Lantai Tanah & Dinding Bata": (
                "Sitting cross-legged on a flat, hardened earth floor (tanah liat) with dry, dusty surface textures. "
                "The background is a solid wall of exposed red bricks with thick, messy mortar and dark soot stains (jelaga). "
                "Next to her is a basket of unpeeled shallots, a small pile of dry rough firewood, and a stone mortar (cobek) with chili residue. "
                "Focus on the rough brick surfaces and the earthy, dusty soil texture."
            ),
            "Sajadah Tua & Tembok Kayu": (
                "Sitting cross-legged on a worn-out, faded velvet sajadah (prayer mat) placed directly over a dark, weathered wooden floor. "
                "The background is a solid wall of vertical dark teak wood planks with prominent deep grain and peeling varnish. "
                "Surrounding objects: a string of wooden prayer beads (tasbih), a small plain ceramic water jug, and a stack of old religious books with yellowing pages. "
                "Focus on the aged wood grain and the soft but thinning fabric texture of the mat."
            ),
            "Tikar Pandan & Tembok Cat Kusam": (
                "Sitting cross-legged on a pale-green 'Tikar Pandan' mat with a distinct cross-weave pattern. "
                "The background is a solid plastered wall with old, chalky white paint that is peeling and bubbling in several spots. "
                "Next to her is a large glass jar of crackers (kerupuk), a small bottle of eucalyptus oil, and a discarded newspaper from years ago. "
                "Focus on the brittle paint flakes and the ribbed texture of the pandan mat."
            ),
            "Lantai Tegel Kunci & Dinding Tua": (
                "Sitting cross-legged on vintage 'Tegel Kunci' cement tiles with a faded geometric floral pattern and matte finish. "
                "The background is a solid, thick masonry wall with visible dampness (rembes) and moss-green stains at the bottom. "
                "Surrounding objects: a brass tray with a single glass of tea, a small coil of mosquito incense (obat nyamuk bakar), and a worn-out batik sarong folded nearby. "
                "Focus on the smooth but aged stone feel of the tiles and the damp texture of the wall."
            ),
            "Pematang Sawah & Hamparan Padi": (
                "Sitting cross-legged on a narrow, hardened mud path (pematang). "
                "The background is a solid, vast expanse of ripening yellow rice stalks (padi) with heavy, drooping grains. "
                "Texture details: dried cracked mud on the path, rough husks of the rice, and dry straw stubble. "
                "Next to her: a worn-out 'caping' straw hat, a rusted sickle (arit), and a plastic water bottle wrapped in damp cloth. "
                "Focus on the organic yellow and brown textures of the harvest."
            ),
            "Bawah Pohon Bambu (Kebun)": (
                "Sitting cross-legged on a thick carpet of dry, fallen bamboo leaves. "
                "The background is a dense, impenetrable wall of green and yellow bamboo trunks (rumpun bambu) with dusty nodes. "
                "Texture details: crispy dry leaves, smooth but scarred bamboo skin, and loose dark soil. "
                "Next to her: a traditional woven bamboo basket (tenggok), a small pile of dry twigs, and an old analog radio. "
                "Focus on the layered textures of the forest floor."
            ),
            "Pinggir Sungai Batu Kali": (
                "Sitting cross-legged on a large, flat river stone with grey mineral deposits. "
                "The background is a steep riverbank made of stacked natural river rocks and exposed tree roots. "
                "Texture details: porous stone surfaces, damp moss, and gritty river sand. "
                "Next to her: a pair of old rubber sandals (sandal jepit), a simple ceramic teapot, and a small metal tray of crackers. "
                "Focus on the contrast between hard stone and soft moss."
            ),
            "Halaman Pasir & Semak Belukar": (
                "Sitting cross-legged on a patch of coarse grey volcanic sand (pasir urug). "
                "The background is a wild, dense thicket of tropical ferns and tall 'alang-alang' grass. "
                "Texture details: grainy sand, sharp edges of the grass blades, and dry twigs. "
                "Next to her: a traditional broom (sapu lidi), a small coil of mosquito incense (obat nyamuk), and a glass of tea with a metal lid. "
                "Focus on the gritty and bushy organic textures."
            ),
            "Kebun Singkong & Tanah Merah": (
                "Sitting cross-legged on firm, reddish-brown clay soil (tanah merah). "
                "The background is a row of tall cassava plants (pohon singkong) with large, hand-shaped leaves. "
                "Texture details: clumpy red earth, rough woody cassava stems, and dry fallen leaves. "
                "Next to her: a woven plastic sack, a small garden trowel, and a plate of boiled bananas. "
                "Focus on the deep earthy tones and woody textures."
            ),
            "Tepi Jalan Setapak & Pagar Bambu": (
                "Sitting cross-legged on a dusty dirt road with small pebbles and tire track imprints. "
                "The background is a long, rustic fence made of weathered, split bamboo poles (pagar salang). "
                "Texture details: fine grey dust, splintered bamboo fibers, and rusted wire ties. "
                "Next to her: a glass of coffee, a small tin box for betel nut (sirih), and a wandering village chicken nearby. "
                "Focus on the dry, dusty village atmosphere."
            ),
            "Gubuk Bambu & Lantai Tanah": (
                "Sitting cross-legged on a hard-packed, dusty earthen floor inside a small hut. "
                "The background is a wall made of old, frayed bamboo weaving (gedek) with visible gaps and hanging spiderwebs. "
                "Texture details: dusty dry soil, splintered bamboo fibers, and brittle organic matter. "
                "Next to her: a stack of dry firewood, a blackened clay stove (tungku) without fire, and a traditional woven bamboo basket. "
                "Focus on the greyish, dusty, and dilapidated bamboo textures."
            ),
            "Lantai Kayu Lapuk & Dinding Papan": (
                "Sitting cross-legged on a floor made of uneven, weathered wooden planks with large gaps and protruding rusty nails. "
                "The background is a solid wall of vertical dark wood boards with peeling bark and deep termite tracks. "
                "Texture details: rough wood grain, flaky dry wood rot, and metallic rust. "
                "Next to her: an old kerosene lamp (lampu templok) without glass, a small tin of betel nut, and a folded, faded sarong. "
                "Focus on the decaying timber and ancient wood textures."
            ),
            "Gubuk Sawah & Atap Rumbia": (
                "Sitting cross-legged on a low bamboo platform (amben) built close to the ground. "
                "The background features low-hanging eaves made of dried, shredded palm leaves (atap rumbia) and rough wooden poles. "
                "Texture details: crispy dried leaves, coarse grey wood, and dusty straw. "
                "Next to her: a rusted sickle (arit), a traditional 'caping' hat, and a glass of tea with a dusty metal lid. "
                "Focus on the dry, brittle textures of the palm leaves and old wood."
            ),
            "Sudut Gubuk & Tumpukan Karung": (
                "Sitting cross-legged on a piece of old, torn tarpaulin (terpal) over the dirt floor. "
                "The background is a stack of overflowing woven plastic sacks (karung goni) filled with harvested grains and dry husks. "
                "Texture details: rough plastic weave, fibrous burlap, and dusty grain particles. "
                "Next to her: a small plastic bucket, a bundle of tied dry corn husks, and a pair of broken rubber sandals. "
                "Focus on the industrial-agricultural clutter and messy textures."
            ),
            "Gubuk Kebun & Dinding Pelepah": (
                "Sitting cross-legged on a flat natural stone inside a makeshift shelter. "
                "The background is a wall constructed from dried coconut leaf stalks (pelepah) tied with rusted wire. "
                "Texture details: ribbed leaf stalks, coarse dry fibers, and oxidized wire. "
                "Next to her: a traditional broom (sapu lidi), a small clay water jug, and a plate of cold boiled sweet potatoes. "
                "Focus on the raw, unpolished organic construction materials."
            ),
            "Teras Gubuk & Pagar Rengkek": (
                "Sitting cross-legged on a dusty, cracked concrete slab at the entrance of a hut. "
                "The background is a rustic fence made of split bamboo branches and weathered sticks. "
                "Texture details: sharp splintered edges, fine dust covering everything, and dry moss. "
                "Next to her: a glass of black coffee, an old analog radio, and a wandering village chicken. "
                "Focus on the dry, splintery, and humble village textures."
            ),
            "Lembah Berkabut & Terasering Padi": (
                "Sitting cross-legged directly on hard-packed, cracked reddish clay soil (tanah merah). "
                "The background is a vast, expansive mountain range (pegunungan) with layered blue and green tones. "
                "The foreground features extensive rice paddy terraces (terasering) with textured mud dikes and young green stalks. "
                "Textural details: gritty soil, rough mud dikes, and dry straw stubble. "
                "Next to her: a woven bamboo basket (tenggok), a traditional 'caping' hat, and a glass of warm tea with a metal lid. "
                "Focus on the organic earth tones and agricultural textures against the mountain backdrop."
            ),
            "Puncak Bukit & Hutan Pinus": (
                "Sitting cross-legged on a thick carpet of dry, fallen pine needles and rough pebbles. "
                "The background is a solid wall of dense, tall dark-green pinus forest trunks (hutan pinus). "
                "Texture details: crispy dry needles, smooth but scarred pine bark, and loose forest floor soil. "
                "Next to her: an antique analogue radio, a bundle of dry twigs, and a simple ceramic water jug. "
                "Focus on the layered textures of the forest floor and tree bark."
            ),
            "Perkebunan Teh & Pagar Bambu": (
                "Sitting cross-legged on firm, greyish-brown clay soil mixed with fine tea leaf dust. "
                "The background is a dense, manicured hedge of low-growing tea plants (perkebunan teh) stretching into the horizon. "
                "Texture details: clumpy earth, rough tea stems, and dry fallen leaves. "
                "Next to her: a woven plastic sack, a small garden trowel, and a plate of boiled bananas. "
                "Focus on the deep earthy tones and woody textures of the tea plantation."
            ),
            "Sungai Pegunungan & Batu Kali": (
                "Sitting cross-legged on a large, flat river stone with grey mineral deposits and moss growth. "
                "The background is a steep riverbank made of stacked natural river rocks and exposed tree roots. "
                "Texture details: porous stone surfaces, damp moss, and gritty river sand. "
                "Next to her: a pair of old rubber sandals (sandal jepit), a simple ceramic teapot, and a small metal tray of crackers. "
                "Focus on the contrast between hard stone and soft moss."
            ),
            "Lereng Gunung & Tumpukan Karung": (
                "Sitting cross-legged on a piece of old, torn tarpaulin (terpal) over the dirt floor. "
                "The background is a stack of overflowing woven plastic sacks (karung goni) filled with harvested grains and dry husks. "
                "Texture details: rough plastic weave, fibrous burlap, and dusty grain particles. "
                "Next to her: a small plastic bucket, a bundle of tied dry corn husks, and a pair of broken rubber sandals. "
                "Focus on the industrial-agricultural clutter and messy textures on the slope."
            ),
            "Kebun Salak & Tanah Lembap": (
                "Sitting cross-legged on damp, dark soil covered in sharp, dry salak leaf debris. "
                "The background is a dense, thorny thicket of salak palms (pohon salak) with jagged, spiked fronds and clusters of brown snake-fruit. "
                "Texture details: scaly skin of the salak fruit, sharp thorny stems, and moist, clumpy earth. "
                "Next to her: a small bamboo basket (tenggok) filled with harvested salak, a rusty sickle, and a pair of old rubber sandals. "
                "Focus on the prickly, dark, and organic textures of the salak grove."
            ),
            "Bawah Pohon Mangga & Daun Kering": (
                "Sitting cross-legged on a thick layer of crispy, brown fallen mango leaves and small dry twigs. "
                "The background is the solid, gnarled trunk of an ancient mango tree with thick, textured grey bark. "
                "Texture details: rough deeply-fissured bark, brittle dry leaves, and small sap droplets. "
                "Next to her: a plastic bucket of green mangoes, a glass of warm tea with a metal lid, and a traditional hand-woven fan. "
                "Focus on the contrast between the rough bark and the crunchy leaf carpet."
            ),
            "Kebun Pisang & Tanah Becek": (
                "Sitting cross-legged on a piece of old, flattened cardboard over slightly muddy brown earth. "
                "The background is a solid wall of tall banana plants with huge, shredded green leaves and heavy bunches of green bananas (pisang kepok). "
                "Texture details: smooth but waxy banana trunks, torn fibrous leaves, and slippery mud patches. "
                "Next to her: a bundle of dried banana leaves (klaras), a sharp machete (golok), and a plate of boiled bananas. "
                "Focus on the tropical, lush, and slightly messy banana plantation vibe."
            ),
            "Bawah Pohon Rambutan": (
                "Sitting cross-legged on firm soil covered in scattered red rambutan skins and fallen yellowing leaves. "
                "The background features low-hanging branches laden with bright red, hairy rambutan fruits. "
                "Texture details: soft hairy spines of the fruit, thin woody branches, and gritty soil. "
                "Next to her: a large woven plastic sack, an old analog radio, and a string of wooden prayer beads (tasbih). "
                "Focus on the vibrant organic colors against the dry, dusty ground."
            ),
            "Kebun Durian & Akar Besar": (
                "Sitting cross-legged between massive, protruding wooden roots of an old durian tree. "
                "The background is a solid forest-like environment with tall durian trees and dense tropical foliage. "
                "Texture details: hard thorny shells of durian fruit on the ground, mossy giant roots, and dry forest mulch. "
                "Next to her: a small kerosene lamp (off), a bamboo water container, and a glass jar of crackers. "
                "Focus on the sharp, hard textures of the fruit and the prehistoric feel of the roots."
            ),
            "Kebun Pepaya & Pagar Bambu": (
                "Sitting cross-legged on a flat natural stone on the edge of a small papaya orchard. "
                "The background is a row of tall, thin papaya trees with hollow-looking trunks and large umbrella-like leaves. "
                "Texture details: scarred greyish trunks, soft orange fruit flesh (if cut), and a rustic split-bamboo fence. "
                "Next to her: a traditional broom (sapu lidi), a small tin box for betel nut, and a wandering village chicken. "
                "Focus on the tall vertical lines and the humble village garden textures."
            ),
            "Kebun Melon Gantung & Tanah Mulsa": (
                "Sitting cross-legged on a piece of dark, glossy silver-black plastic mulching film (mulsa) covering the soil. "
                "The background is a dense, impenetrable wall of green melon vines supported by vertical bamboo trellises. "
                "The vines are heavily laden with dozens of ripe green and yellow melons (cantaloupe) with highly detailed, intricate reticulated 'net' textures on their skins. "
                "The scene is overwhelmingly rimbun (lush). Textural details: rough net patterns, fuzzy leaves, and thick green vines. "
                "Next to her: a woven bamboo basket (tenggok) filled with harvested, high-detail melons, a pruning shear, and a glass of warm tea with a metal lid. "
                "Focus on the complex net textures and vibrant green and orange tones against the black plastic."
            ),
            "Kebun Semangka Tanah & Hamparan Daun": (
                "Sitting cross-legged on a hand-woven natural 'Tikar Mendong' straw mat with frayed edges. "
                "The background is a vast, dense ground-cover of thick green semangka (watermelon) leaves and sprawling vines. "
                "Dozens of large, heavy, round and oval watermelons are scattered among the rimbun leaves, showing highly detailed, prominent deep-green and pale-green striped patterns with high-gloss natural rind. "
                "Textural details: bold striped patterns, fuzzy green leaves, and wet mud patches on the fruit. "
                "Next to her: a classic brass betel nut box (sirih), a small coil of mosquito incense, and a pair of old rubber sandals. "
                "Focus on the high-contrast stripes and the wet, glossy look of the natural rind."
            ),
            "Kebun Strawberry & Mulsa Hitam": (
                "Sitting cross-legged on a heavy black plastic mulching film covering the elevated soil beds. "
                "The background features rows and rows of elevated strawberry plants (pohon strawberry) with dense green leaves and small white flowers. "
                "The scene is rimbun with thousands of ripe, bright red strawberry fruits, showing incredibly detailed surface textures with deep seed patterns and waxy, glossy finish. "
                "Textural details: highly intricate seed patterns, fuzzy leaves, and waxy fruit skin. "
                "Next to her: an old analogue radio with a telescopic antenna, a wooden mortal (cobek), and a pile of dry firewood. "
                "Focus on the incredibly sharp seed detail and the explosive bright red and green colors."
            ),
            "Kebun Anggur Teralis & Hamparan Tanah": (
                "Sitting cross-legged on a large, flat river stone with grey mineral deposits and moss growth. "
                "The background is a monumental, sprawling 'U'-shaped overhead bamboo and wire trellis system, dense and heavy with rimbun clusters of deep purple (kismis) and vibrant green (tanpa biji) grapes. "
                "Each grape bunch is hyper-detailed, with individual fruit showing highly rendered natural 'waxy bloom' (powdery substance) and translucent pulp when broken. "
                "Textural details: detailed grape skin pores, fuzzy green leaves, and old, knotty wood. "
                "Next to her: an antique brass betel nut box, a small tin box for betel nut (sirih), and a traditional broom (sapu lidi). "
                "Focus on the waxy bloom and the explosive purple, green, and orange colors."
            ),
            "Taman Paku-Pakuan & Tembok Berlumut": (
                "Sitting cross-legged on a patch of damp soil covered in thin green moss and scattered dry twigs. "
                "The background is a solid wall of dense, rimbun tropical ferns (pakis) and bird's nest ferns with jagged, vibrant green leaves. "
                "The wall behind the plants is old red brick covered in thick, dark-green velvety moss and water stains. "
                "Texture details: fuzzy moss, porous damp bricks, and the ribbed veins of fern leaves. "
                "Next to her: a weathered terracotta plant pot with cracks, a small rusty garden trowel, and a glass of tea with a metal lid. "
                "Focus on the deep green saturation and the damp, earthy textures."
            ),
            "Taman Bunga Kertas (Bougainvillea) & Pasir": (
                "Sitting cross-legged on a layer of coarse grey volcanic sand mixed with fallen flower petals. "
                "The background is a monumental, rimbun explosion of Bougainvillea (Bunga Kertas) in vibrant magenta and orange, with thorny woody stems intertwined. "
                "Texture details: paper-like flower petals, sharp woody thorns, and gritty sand particles. "
                "Next to her: a traditional broom (sapu lidi), a small plastic bucket, and a pair of old rubber sandals (sandal jepit). "
                "Focus on the high-contrast flower colors against the dry, grey sandy ground."
            ),
            "Taman Lidah Mertua & Lantai Semen": (
                "Sitting cross-legged on a rough, unpolished concrete floor with visible sand grains and thin cracks. "
                "The background is a dense row of tall, sharp Sansevieria (Lidah Mertua) plants with highly detailed yellow-green striped patterns on their stiff leaves. "
                "Texture details: leathery leaf surfaces, gritty concrete, and small pebbles. "
                "Next to her: a glass jar of crackers (kerupuk), an old analog radio, and a string of wooden prayer beads (tasbih). "
                "Focus on the sharp vertical lines and the waxy, striped texture of the leaves."
            ),
            "Taman Keladi & Kolam Batu": (
                "Sitting cross-legged on a large, flat natural river stone with a matte grey finish. "
                "The background is a lush, rimbun collection of Caladium (Keladi) plants with huge, heart-shaped leaves showing intricate red and white vein patterns. "
                "Nearby is the edge of a small pond made of stacked rough mountain stones with natural water splashes. "
                "Texture details: translucent leaf membranes, porous volcanic stones, and wet mineral deposits. "
                "Next to her: a brass tray with a teapot, a small tin box for betel nut, and a discarded old newspaper. "
                "Focus on the intricate leaf veins and the raw, wet stone textures."
            ),
            "Teras Semen & Kolam Air Jernih": (
                "Sitting cross-legged on a rough, unpolished concrete patio floor (plesteran) with visible sand grains and fine cracks. "
                "The background is a solid, weathered wall of rough-textured grey cement with faded water stains. "
                "The scene features the edge of a clean, pure water pond constructed from large, flat volcanic rocks with smooth but gritty surfaces. "
                "Inside the pond, hundreds of colorful Koi fish (Ogon, Shusui, Tancho) create a dense, rimbun wall of shimmering colors, including metallic gold, silver, bright yellow, and solid red. "
                "Texture details: gritty concrete surface, dusty cement patches, clear water clarity, and iridescent fish skin reflections. "
                "Next to her: a glass jar of crackers (kerupuk), an old analog radio, and a string of wooden prayer beads (tasbih). "
                "Focus on the gritty textures, the waxy waxy look of the cement, and the explosive iridescence of the fish."
            ),
            "Tikar Pandan & Kolam Pagar Bambu": (
                "Sitting cross-legged on a pale-green 'Tikar Pandan' mat with a distinct cross-weave pattern, placed near the pond's edge. "
                "The background is a rustic fence made of split bamboo poles and weathered sticks. "
                "The scene features a small, simple pond with clean, pure water, built from stacked irregular river stones with dry moss. "
                "Inside the pond, dozens of varied colorful Koi fish (Asagi, Bekko, Koromo) swim in rimbun groups, displaying highly rendered patterns of blue-grey scales, bold black spots, and intricate crimson red markings. "
                "Texture details: ribbed texture of the pandan mat, sharp splintered edges of bamboo, rough stone surfaces, and intricate fish scale patterns. "
                "Next to her: a traditional broom (sapu lidi), a small plastic bucket, and a pair of old rubber sandals (sandal jepit). "
                "Focus on the dry organic textures, the raw bamboo, and the detailed patterns of the fish."
            ),
            "Tembok Bata Berlumut & Kolam Teratai": (
                "Sitting cross-legged on a patch of damp soil covered in thin green moss and scattered dry twigs. "
                "The background is an old, weathered red brick wall covered in thick, dark-green velvety moss and water stains. "
                "The scene features the edge of a large, natural pond filled with pure, clear water and several rimbun clusters of pink and white water lilies (teratai). "
                "Inside the pond, hundreds of vibrant colorful Koi fish (Doitsu, Goromo, Goshiki) navigate through the lilies in rimbun formations, showing intricate scales in sharp patterns of deep purple, gold, crimson, and black. "
                "Texture details: fuzzy moss, porous damp bricks, translucent lily pads, and raw fish skin texture. "
                "Next to her: a brass tray with a teapot, a small tin box for betel nut, and a discarded old newspaper. "
                "Focus on the deep green saturation, the raw wet bricks, and the explosive patterns of the fish."
            ),
            "Pinggir Kolam Batu & Koi Kohaku": (
                "Sitting cross-legged on a large, flat, damp river stone at the very edge of the water. "
                "The background is a solid wall of dense tropical ferns and mossy rock formations. "
                "In front of her is a clear, deep pond filled with dozens of rimbun Koi fish, primarily 'Kohaku' with bold red and white patterns. "
                "The water is crystal clear, showing the high-detail scales of the fish and their fluid movements. "
                "Next to her: a brass bowl of fish food (pelet) and a glass of tea with a metal lid. "
                "Focus on the sharp contrast between the white-red fish and the dark mossy rocks."
            ),
            "Sudut Kolam Batu & Koi Biru-Perak": (
                "Sitting cross-legged on a cluster of flat natural stones. "
                "The background is a dense thicket of tall Sansevieria plants and thick garden bushes. "
                "The pond features rare 'Asagi' and 'Shusui' Koi fish with blue-grey and silver scales, creating a rimbun, shimmering effect underwater. "
                "Texture details: porous grey stone, sharp vertical plant lines, and highly rendered fish scale patterns. "
                "Next to her: a small copper teapot and a pair of old rubber sandals (sandal jepit). "
                "Focus on the cool-toned blue and silver fish colors against the rough garden textures."
            ),
            "Pinggir Kolam Batu & Koi Kohaku": (
                "Sitting cross-legged on a large, flat, damp river stone at the very edge of the water. "
                "The background is a solid wall of dense tropical ferns and mossy rock formations. "
                "In front of her is a clear, deep pond filled with dozens of rimbun Koi fish, primarily 'Kohaku' with bold red and white patterns. "
                "The water is crystal clear, showing the high-detail scales of the fish and their fluid movements. "
                "Next to her: a brass bowl of fish food (pelet) and a glass of tea with a metal lid. "
                "Focus on the sharp contrast between the white-red fish and the dark mossy rocks."
            ),
            "Pinggir Sungai Batu & Akar Pohon": (
                "Sitting cross-legged on a large, flat, damp river stone with green mineral deposits. "
                "The background is a solid wall of massive, tangled tropical tree roots and dense ferns hanging over the water. "
                "The river water is clear, showing submerged mossy rocks and small river fish in rimbun groups. "
                "Texture details: porous wet stone, slippery moss, and rough fibrous roots. "
                "Next to her: a glass of tea with a rusty metal lid and a pair of old rubber sandals (sandal jepit). "
                "Focus on the raw, wet textures and the dark organic tones of the riverbank."
            ),
            "Pesisir Laut & Akar Bakau (Mangrove)": (
                "Sitting cross-legged on a patch of coarse, wet grey volcanic sand mixed with broken seashells. "
                "The background is a dense, impenetrable wall of rimbun Mangrove roots (bakau) twisting above the water line. "
                "The sea water is calm and clear, revealing hyper-detailed textures of the sandy bottom and small crabs. "
                "Texture details: gritty sand, sharp shell fragments, and salt-crusted wood. "
                "Next to her: a traditional woven bamboo basket (tenggok) and a small tin box for betel nut (sirih). "
                "Focus on the high-detail grit and the complex, weathered mangrove textures."
            ),
            "Tepi Danau Berbatu & Alang-Alang": (
                "Sitting cross-legged on a cluster of flat, dry mountain stones at the edge of a vast lake. "
                "The background is a rimbun wall of tall, golden-brown 'alang-alang' grass and wild shrubs. "
                "The lake water is crystal clear, reflecting the high-detail textures of the surrounding greenery. "
                "Texture details: sharp grass blades, dry dusty stones, and clear water ripples. "
                "Next to her: an old analog radio and a small plastic plate with boiled bananas. "
                "Focus on the contrast between the dry, sharp grass and the deep clear water."
            ),
            "Bebatuan Karang & Ombak Tenang": (
                "Sitting cross-legged on a jagged, weathered coral rock formation with sharp edges and salt deposits. "
                "The background is a solid view of the deep blue sea with natural foam and clear water textures. "
                "The shallow water near the rocks is rimbun with colorful sea moss and small corals visible through the surface. "
                "Texture details: rough porous coral, dried salt crust, and waxy sea plants. "
                "Next to her: a simple ceramic teapot and a string of wooden prayer beads (tasbih). "
                "Focus on the harsh, sharp textures of the coral against the fluid clear water."
            ),
            "Muara Sungai & Tumpukan Kayu Apung": (
                "Sitting cross-legged on a large piece of smooth, sun-bleached driftwood on a muddy bank. "
                "The background is a rimbun thicket of nipah palms and tall river reeds with dense green foliage. "
                "The water is a mix of clear and silty textures, showing organic debris and floating leaves. "
                "Texture details: smooth worn-out wood, clumpy dark mud, and ribbed palm leaves. "
                "Next to her: a traditional 'caping' hat and a small glass jar of crackers (kerupuk). "
                "Focus on the earthy mud tones and the skeletal textures of the driftwood."
            ),
            "Danau Pegunungan & Lumut Hijau": (
                "Sitting cross-legged on a thick carpet of vibrant green moss over a flat stone at a high-altitude lake. "
                "The background is a solid wall of ancient, moss-covered trees and thick mountain mist (visualized as texture). "
                "The lake water is incredibly clear, showing the high-detail submerged logs and green algae. "
                "Texture details: velvety soft moss, decaying wood, and cold, still water. "
                "Next to her: a small brass teapot and a discarded old newspaper. "
                "Focus on the deep green saturation and the ancient, damp forest textures."
            ),
            "Gundukan Sampah Plastik (TPA)": (
                "Sitting cross-legged directly on a massive pile of compressed plastic waste and torn colorful trash bags. "
                "The background is a solid, rimbun wall of towering garbage mounds consisting of discarded packaging, weathered plastics, and organic waste. "
                "Texture details: crinkled plastic, gritty dust, torn synthetic fibers, and sticky organic stains. "
                "Next to her: a rusted metal hook (pengait sampah), a dirty plastic sack (karung), and a pair of broken rubber sandals. "
                "Focus on the overwhelming clutter of artificial waste and the dirty, unpolished textures."
            ),
            "Gudang Rongsok Logam Berkarat": (
                "Sitting cross-legged on a floor made of scrap metal sheets and rusted iron plates. "
                "The background is an impenetrable wall of stacked rusted car parts, old bicycle frames, and twisted corrugated iron (seng). "
                "Texture details: deep orange iron rust (karat), sharp metallic edges, peeling paint, and thick oily grime. "
                "Next to her: a large rusted hammer, a pile of tangled copper wires, and a glass of black coffee in a stained glass. "
                "Focus on the harsh, sharp, and oxidized metallic textures."
            ),
            "Tumpukan Kardus & Kertas Bekas": (
                "Sitting cross-legged on flattened, weathered cardboard boxes on a dusty concrete floor. "
                "The background is a rimbun wall of tightly bound stacks of old newspapers, yellowed books, and brown corrugated cardboard. "
                "Texture details: fibrous paper edges, brittle cardboard, dust particles, and damp water stains. "
                "Next to her: a roll of dirty plastic twine, a rusted cutter, and an old analog radio with a missing antenna. "
                "Focus on the dry, papery, and dusty organic clutter."
            ),
            "Kuburan Botol Kaca & Beling": (
                "Sitting cross-legged on a piece of thick, dirty plywood over a field of crushed glass. "
                "The background is a solid wall of thousands of stacked glass bottles in various colors (amber, green, clear) covered in thick dust. "
                "Texture details: smooth but dirty glass surfaces, sharp crystalline shards, and dried mud. "
                "Next to her: a plastic crate (keranjang), a small tin box for betel nut, and a discarded worn-out batik sarong. "
                "Focus on the crystalline reflections and the heavy, grimy dust layers."
            ),
            "Rongsok Elektronik & Kabel (E-Waste)": (
                "Sitting cross-legged on a pile of old circuit boards and broken plastic casings of vintage televisions. "
                "The background is a rimbun mountain of discarded electronic parts, tangled multi-colored wires, and shattered CRT glass. "
                "Texture details: green fiberglass PCBs, dusty copper coils, brittle aged plastic, and metallic solder points. "
                "Next to her: a pair of pliers, a small prayer beads (tasbih) string, and a glass of tea with a metal lid. "
                "Focus on the complex, technological decay and the grimy industrial textures."
            ),
            "Tumpukan Ban Bekas & Karet": (
                "Sitting cross-legged on the inner circle of a large, weathered truck tire. "
                "The background is a solid wall of stacked black rubber tires with worn-out treads and dried mud in the grooves. "
                "Texture details: matte black rubber, deep tread patterns, dry white powder on the surface, and cracked sidewalls. "
                "Next to her: a traditional broom (sapu lidi), a small bottle of eucalyptus oil, and a wandering village chicken. "
                "Focus on the heavy, dark, and industrial rubber textures."
            ),
            "Gudang Garam & Karung Goni": (
                "Sitting cross-legged on a floor covered in thick, coarse white salt crystals. "
                "The background is a solid wall of stacked, heavy burlap sacks (karung goni) with visible fibers and salt stains. "
                "Texture details: crystalline salt grains, rough fibrous burlap, and damp wooden pillars with white mineral crust. "
                "Next to her: a wooden salt shovel, a small plastic bucket, and a glass of tea with a metal lid. "
                "Focus on the white crystalline textures and the rough, brownish burlap."
            ),
            "Pabrik Genteng & Tumpukan Tanah Liat": (
                "Sitting cross-legged on a patch of fine, dry orange clay dust. "
                "The background is a rimbun wall of thousands of unbaked, matte-orange clay tiles (genteng) stacked in neat but dusty rows. "
                "Texture details: smooth but gritty clay surfaces, powdery orange dust, and rough wooden drying racks. "
                "Next to her: a traditional 'caping' hat, a small clay water jug, and a pair of old rubber sandals. "
                "Focus on the monochromatic orange tones and the dry, earthy textures."
            ),
            "Bengkel Kapal & Kayu Kapal Lapuk": (
                "Sitting cross-legged on a bed of dry wood shavings (tatal) and sawdust. "
                "The background is the massive, curved hull of an old wooden boat with peeling blue and white paint and thick barnacle crusts. "
                "Texture details: flaking paint, sharp salt-encrusted barnacles, and deep cracks in the aged timber. "
                "Next to her: a rusted iron anchor, a coil of thick frayed nautical rope, and a tin of betel nut. "
                "Focus on the industrial maritime decay and the rough, weathered wood."
            ),
            "Penggilingan Padi & Tumpukan Sekam": (
                "Sitting cross-legged on a vast mound of dry, golden-yellow rice husks (sekam). "
                "The background is a solid wall of old, rusted milling machinery with oily gears and thick layers of grain dust. "
                "Texture details: sharp paper-like husks, greasy metallic surfaces, and fine yellow dust covering everything. "
                "Next to her: a woven plastic sack, a small analog radio, and a string of wooden prayer beads. "
                "Focus on the overwhelming golden grain textures and the rusted industrial machinery."
            ),
            "Pasar Tradisional Bubrah (After Hours)": (
                "Sitting cross-legged on a wet, stained cement floor covered in discarded vegetable leaves and crushed fruit. "
                "The background is a rimbun mess of empty wooden crates (peti kayu), torn plastic tarps, and abandoned bamboo baskets. "
                "Texture details: slimy organic waste, rough splintered wood, and damp concrete stains. "
                "Next to her: a glass jar of crackers, a traditional broom (sapu lidi), and a wandering village chicken. "
                "Focus on the chaotic organic clutter and the gritty, damp market textures."
            ),
            "Reruntuhan Beton & Besi Rebar": (
                "Sitting cross-legged on a pile of broken concrete slabs and grey cement dust. "
                "The background is a solid wall of a collapsed building with exposed, twisted rusty iron rebar poking out like skeletons. "
                "Texture details: gritty concrete chunks, oxidized rusty metal, and layers of fine white limestone dust. "
                "Next to her: a dented aluminium teapot, a worn-out prayer rug (sajadah) covered in dust, and a single olive branch. "
                "Focus on the harsh, sharp edges of the rubble and the powdery grey textures."
            ),
            "Gundukan Bata Merah & Abu Bakaran": (
                "Sitting cross-legged on a mound of loose, shattered red bricks and dark grey ash. "
                "The background is the skeleton of a burnt-out house with blackened doorways and charred wooden beams. "
                "Texture details: brittle burnt wood, powdery black soot, and rough broken ceramic tiles. "
                "Next to her: an old kerosene lamp with cracked glass, a small copper tray, and a tattered family photo frame. "
                "Focus on the contrast between the red bricks and the black carbon soot."
            ),
            "Lorong Kota Tua Berdebu (Gaza Style)": (
                "Sitting cross-legged on a narrow stone pathway covered in fine yellow sand and debris. "
                "The background is a rimbun wall of ancient limestone buildings with collapsing balconies and dangling electrical wires. "
                "Texture details: eroded limestone surfaces, tangled copper wires, and dry desert sand accumulation. "
                "Next to her: a traditional woven basket, a small tin box for sewing kits, and a pair of old dusty leather sandals. "
                "Focus on the ancient architectural decay and the gritty, sandy textures."
            ),
            "Bangkai Kendaraan & Tembok Seng": (
                "Sitting cross-legged on a rusted car hood flattened on the ground. "
                "The background is a solid wall of a destroyed warehouse made of riddled corrugated iron (seng) and a burnt-out truck chassis. "
                "Texture details: flaky orange rust, bullet-pierced metal sheets, and greasy soot stains. "
                "Next to her: an empty ammunition crate used as a box, a plastic water jug, and a glass of black tea. "
                "Focus on the heavy metallic oxidation and the industrial ruins."
            ),
            "Halaman Masjid Hancur & Marmer Pecah": (
                "Sitting cross-legged on a shattered white marble floor with visible veins and deep cracks. "
                "The background is a row of damaged stone arches and piles of decorative tiles (zellige) mixed with rubble. "
                "Texture details: smooth but cracked marble, sharp ceramic shards, and thick grey dust. "
                "Next to her: a large old Quran with a torn cover, a small brass incense burner (off), and a rosary. "
                "Focus on the contrast between the elegant marble and the violent destruction."
            ),
            "Pojok Mushola Tua & Sajadah Usang": (
                "Sitting cross-legged on a faded green velvet prayer mat (sajadah) with thinning pile and visible fabric threads. "
                "The background is a solid wall of old, unpainted limestone with thick layers of peeling white chalk (kapur). "
                "Texture details: fuzzy worn-out velvet, chalky paint flakes, and damp stone patches at the bottom. "
                "Next to her: a string of large wooden prayer beads (tasbih), an old ceramic water jug (kendi), and a small wooden book stand (rehal). "
                "Focus on the spiritual silence and the brittle, dry textures of the wall."
            ),
            "Gudang Tenun & Benang Kusut": (
                "Sitting cross-legged on a floor covered in colorful lint, cotton scraps, and loose threads. "
                "The background is a rimbun wall of stacked wooden weaving frames (alat tenun) and hundreds of dusty spools of yarn. "
                "Texture details: fibrous cotton, rough hand-carved wood grain, and layers of fine lint dust. "
                "Next to her: a traditional weaving shuttle (torak), a small tin box for sewing kits, and a glass of warm tea. "
                "Focus on the complex interplay of soft fibers and hard, aged wood."
            ),
            "Lantai Kapal Kayu & Jaring Nelayan": (
                "Sitting cross-legged on a rough wooden deck made of wide, salt-crusted timber planks. "
                "The background is a massive, rimbun pile of tangled green and blue nylon fishing nets with attached lead sinkers. "
                "Texture details: dried salt crystals on wood, coarse nylon mesh, and rusted metal pulleys. "
                "Next to her: a small kerosene lamp (off), a bowl of dried fish, and a traditional 'caping' hat. "
                "Focus on the maritime grit and the complex, knotted textures of the nets."
            ),
            "Pabrik Jamu & Akar Kering": (
                "Sitting cross-legged on a floor covered in yellowish turmeric dust and dried herb particles. "
                "The background is a rimbun wall of hanging dried roots, barks, and baskets of medicinal plants. "
                "Texture details: rough woody roots, powdery herbal dust, and woven bamboo textures. "
                "Next to her: a stone mortar and pestle (lumpang), a small glass bottle of herbal oil, and a plate of traditional snacks. "
                "Focus on the earthy, organic apothecary vibe and the diverse botanical textures."
            ),
            "Gang Sempit & Tembok Lumut": (
                "Sitting cross-legged on a narrow asphalt path with numerous rough patches and potholes. "
                "The background is a solid, towering wall of unpainted bricks and damp cement covered in thick green moss and old graffiti. "
                "Texture details: gritty asphalt, damp velvety moss, and peeling posters on the wall. "
                "Next to her: a row of small potted plants in recycled plastic cans, a puddle of stagnant water, and a pair of old rubber sandals. "
                "Focus on the claustrophobic urban texture and the damp, gritty surfaces."
            ),
            "Depan Rumah (Teras Semen Kasar)": (
                "Sitting cross-legged on a rough grey cement terrace floor with visible sand grains and thin cracks. "
                "The background is a solid wall with faded paint, a simple wooden door with a rusty padlock, and a low-hanging tangled bunch of black electrical wires. "
                "Texture details: chalky wall paint, rough concrete, and the rubbery texture of the cables. "
                "Next to her: a glass jar of crackers (kerupuk), a traditional broom (sapu lidi), and a wandering village chicken. "
                "Focus on the humble, daily residential textures and the messy overhead clutter."
            ),
            "Belakang Rumah & Jemuran Kain": (
                "Sitting cross-legged on a piece of old, flattened cardboard over a dirt and gravel floor. "
                "The background is a rimbun wall of colorful laundry hanging on a simple plastic rope, featuring faded batik sarongs and towels. "
                "Texture details: fibrous cloth, rusty wire fence, and loose dry soil with small pebbles. "
                "Next to her: a plastic laundry basin, a stack of dry firewood, and a small glass of tea with a metal lid. "
                "Focus on the domestic clutter and the contrast between soft fabric and hard gravel."
            ),
            "Samping Rumah (Lorong Drainase)": (
                "Sitting cross-legged on a flat stone beside a narrow open drainage canal (selokan) made of cracked cement. "
                "The background is a solid wall of rough-textured grey stones and overgrown wild weeds. "
                "Texture details: slimy algae inside the canal, porous grey stone, and sharp edges of wild grass. "
                "Next to her: a small bottle of eucalyptus oil, a coil of mosquito incense (off), and an old analog radio. "
                "Focus on the damp, organic decay and the gritty stone textures."
            ),
            "Halaman Depan & Jemuran Gabah": (
                "Sitting cross-legged on a wide woven mat (tikar pandan) placed on a dusty concrete yard. "
                "The background is a simple house front with a corrugated iron roof (seng) and a pile of dry coconut shells. "
                "Texture details: ribbed texture of the mat, thousands of tiny yellow rice grains (gabah) drying in the sun, and rusted metal. "
                "Next to her: a traditional 'caping' hat, a wooden rake, and a plastic bucket of water. "
                "Focus on the agricultural-residential hybrid textures."
            ),
            "Bawah Pohon Depan Gang": (
                "Sitting cross-legged on a large, protruding tree root and dry leaves on the side of the road. "
                "The background is a rustic wooden fence and a stack of old, unused tires covered in dust. "
                "Texture details: rough tree bark, crispy dry leaves, and matte black rubber with deep treads. "
                "Next to her: a small glass of black coffee, an old tin box for betel nut, and a discarded newspaper. "
                "Focus on the dry, dusty roadside atmosphere and the raw organic textures."
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
