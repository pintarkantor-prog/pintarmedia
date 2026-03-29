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
    izin_akses = ["OWNER", "ADMIN", "STAFF"]
    
    if user_level not in izin_akses:
        st.error(f"🚫 Maaf {user_aktif}, Area ini terbatas untuk tim internal.")
        st.stop()

    # --- 2. TAMPILAN UTAMA ---
    st.title("🧠 PINTAR AI LAB")
    st.markdown(f"**{user_aktif}** | 📅 {nama_hari}, {tgl} {nama_bulan} {tahun}")

    # --- 3. TABS MENU ---
    t_masjid, t_bamboo, t_anatomi, t_transform, t_random = st.tabs([
        "🕌 MASJID", "🎋 BAMBOO CRAFT", "🦴 ANATOMY", "⚡ TRANSFORMATION", "🎲 RANDOM"
    ])
                
    # ==========================================================================
    # TAB: THE FAMILY LEGACY (REAL HUMAN - NATURAL WIDE SHOT VERSION)
    # ==========================================================================
    with t_masjid:
        # --- 1. MASTER DNA MANUSIA ASLI (FULL BODY & NATURAL SKIN) ---
        MASTER_FAMILY_SOUL = {
            # ========================== KELOMPOK NENEK (Teduh & Berwibawa) ==========================
            "Nenek (The Matriarch)": (
                "An elderly woman with a fuller, rounded facial structure where gravity has taken its toll. "
                "Deep nasolabial folds and heavy jowls that sag past the jawline. "
                "Her eyelids are thick and drooping, almost covering her eyes, with large, soft bags underneath. "
                "The skin texture is thick, porous, and covered in large age spots and liver spots. "
                "A double chin with soft, folded skin textures. No filters, authentic aged volume."
            ),
            "Nenek Simbah": (
                "An extremely elderly Javanese woman, easily appearing over 80 years old. "
                "Her face is a dense and chaotic network of profound, deep wrinkles that completely consume her visage. "
                "Heavy crow's feet, prominent forehead furrows, and sagging skin folds around her neck and jawline, showing significant volume loss. "
                "Authentic weathered skin texture with prominent age spots, visible pores, and raw, uneven pigmentation. "
                "Her expression is deeply weary and sorrowful, with half-lidded, cloudy eyes looking down. "
                "Her lower lip is downturned with a visible quiver, pressed thin against her toothless gums. "
                "Raw, unpolished cinematic skin details. No smooth filters. 100% authentic aged Javanese look."
            ),
            "Nenek Sunda": (
                "A frail and very aged Sundanese grandmother, her face deeply marked by extreme age and sorrow. "
                "An intensely wrinkled forehead with heavy vertical creases between her brows, indicating deep worry and heartbreak. "
                "The skin around her eyes is exceptionally sagging, with heavy dark circles and prominent sagging folds. "
                "Visible skin pores, realistic dry patches, and authentic elderly skin texture with a dull, matte finish. "
                "A deeply melancholic and pensive 'sayu' expression, looking forward with a profoundly sad gaze. "
                "Her lips are pressed together tightly, showing deep, fine lines and natural wrinkles. "
                "Raw elderly skin texture showing authentic sagging and realistic muscle loss in the face. "
                "No smoothing, 100% realistic tired Sundanese face."
            ),
            "Nenek Melayu": (
                "A profoundly elderly Melayu woman, her face a map of extreme age and sorrow. "
                "Her entire countenance is consumed by heavy, sagging wrinkles and deep facial lines. "
                "Her eyes are bright with unshed tears, glistening with unshed tears, showing heavy, reddened eyelids. "
                "The skin around her jaw and neck is severely sagging, showing realistic volume loss and fragility. "
                "Visible age spots, prominent blue veins on her hands and temples, and authentic aged skin texture with clear pores. "
                "Her downturned mouth has a subtle, realistic quiver in her lower lip, emphasizing her grief. "
                "Raw, high-definition skin texture showing authentic age spots and visible pores dampened by a thin layer of cold sweat. "
                "100% high-definition real elderly face, cinematic and hauntingly emotional."
            ),
            "Gadis Desa (The Natural)": (
                "A beautiful young Indonesian woman in her early 20s of Javanese descent. "
                "She has soft, rounded facial features and a genuinely sweet, 'adem' smile. " # Fitur lembut, senyum adem
                "Medium-tan, warm golden skin with natural skin pores and a healthy texture. " # Kulit sawo matang golden
                "Her eyes are dark, kind, and expressive with naturally thick dark lashes. " # Mata gelap, ekspresif
                "Long, wavy black hair loosely tied or flowing naturally. " # Rambut hitam bergelombang
                "Raw, unpolished cinematic skin details showing authentic pores and light, natural imperfections. No smooth filters." # Detail kulit asli
            ),
            "Gadis Rumi (The Dreamer)": (
                "A stunning young Indonesian woman in her early 20s of Malay or Sumatran descent. "
                "She has a more defined jawline, higher cheekbones, and an elegant presence. " # Rahang tegas, tulang pipi tinggi
                "Light olive or fair skin with warm undertones and natural skin texture. " # Kulit kuning langsat/olive light
                "Her eyes are sharp, confident, and almond-shaped with dark eyebrows. " # Mata tajam, almond
                "Straight, sleek black hair cascading down her shoulders. " # Rambut hitam lurus, jatuh
                "MASTERPIECE realism with high-fidelity skin details, natural pores, and authentic, unedited skin look." # Realisme tinggi
            ),
            "Gadis Melati (The Fresh)": (
                "A beautiful and cheerful young Indonesian woman in her early 20s. "
                "Her face is radiating with a broad, genuine, and joyful smile that crinkles her whole face. " # Senyum lebar, ceria
                "Light, healthy, warm yellow-undertone skin (kuning langsat) with natural rosy cheeks and a fresh, dewy texture. " # Kulit kuning langsat fresh
                "Her eyes are bright, sparkling with happiness, and often in a playful or winking expression. " # Mata berbinar, playful
                "Messy, voluminous dark brown or black hair tied up loosely in a ponytail or bun, with loose strands. " # Rambut kuncir, Messy
                "Authentic young skin texture with natural pores, light freckles, and a healthy, unprocessed look. No smooth filters." # Tekstur kulit muda fresh
                "A positive, energetic, energetic, and motherly warmth presence."
            ),
            "Gadis Anisa (The Modest)": (
                "A breathtakingly beautiful young Indonesian woman in her early 20s of Papuan or Melanesian descent. "
                "She has distinct, strong facial features and a wide, confident, and joyful smile. " # Fitur kuat, senyum lebar
                "Deep, dark caramel or rich cocoa skin with glowing, natural skin texture and pores. " # Kulit gelap/cokelat tua
                "Her eyes are big, bright, warm, and sparkling with energetic life. " # Mata besar, berbinar
                "Beautifully textured, voluminous, tight curly black hair flowing naturally. " # Rambut hitam keriting bervolume
                "RAW cinematic details focusing on authentic skin pores, textures, and rich, deep skin tones. No filters." # Fokus pada tekstur kulit gelap
            ),
            "Kakek (The Wise)": (
                "A very elderly Indonesian man in his late 70s with a fragile but dignified look. "
                "His face is a landscape of deep, sagging wrinkles, heavy eye bags, and prominent age spots. "
                "Paper-thin, weathered skin with visible pores and fine veins. " # Kulit setipis kertas
                "Thin white hair and a sparse, long white beard that adds to his ancient wisdom look. " # Jenggot putih tipis
                "Deeply recessed eyes that look tired but peaceful. "
                "Authentic elderly skin texture, raw and unpolished, no smoothing filters."
            ),
            "Kakek Wiryo (The Artisan)": (
                "A sturdy elderly Indonesian man in his 60s with a tough, hardworking physique. "
                "He has sun-darkened, leathery skin with deep creases on his forehead and around his mouth. " # Kulit leathery (seperti kulit samak)
                "Large, strong hands with thick knuckles, prominent veins, and rough skin texture. " # Tangan kuat khas pekerja
                "Short, thick salt-and-pepper hair and a neat white mustache. " # Kumis putih rapi
                "A focused, sharp, and resilient expression. "
                "Realistic skin details showing sweat and authentic grit. Masterpiece realism."
            ),
            "Kakek Joyo (The Farmer)": (
                "A warm and friendly Indonesian grandfather in his 60s with a constant gentle smile. "
                "His eyes are bright and twinkling behind deep laugh lines (crow's feet). " # Mata berbinar
                "Healthy, warm-toned elderly skin with natural aging marks and a kind, fatherly glow. "
                "Full, soft white hair and a clean-shaven, approachable face. "
                "His expression is one of pure contentment, 'syahdu', and spiritual peace. "
                "Natural young-at-heart elderly look, 100% realistic skin textures without filters."
            ),
            "Kakek Usman (The Silent)": (
                "An elderly Indonesian grandfather in his late 60s, visibly heartbroken and deeply saddened. "
                "His face is contorted in grief, with tears streaming down his heavily wrinkled cheeks and jawline. " # Air mata mengalir, keriput bengkak
                "His eyes are red, swollen from crying, half-closed, and glistening with glistening moisture. " # Mata merah, bengkak, glistening
                "A trembling lip, quivering chin, and a deeply furrowed brow expressing profound sorrow and despair. " # Bibir gemetar, dagu bergetar, alis berkerut sedih
                "Thin white hair and a disheveled white beard, adding to his fragile and neglected appearance. " # Rambut/jenggot acak-acakan, ringkih
                "Authentic elderly skin texture with a healthy, unprocessed look, showing natural pores and age lines. No smooth filters." # Tekstur kulit muda fresh
                "A profoundly vulnerable, heartbreaking, and raw emotional presence."
            )
        }

        # --- 2. MASTER WARDROBE (6 VARIAN PER KARAKTER - DAILY & NEAT HIJAB) ---
        MASTER_FAMILY_WARDROBE = {
            # --- KELOMPOK NENEK ---
            "Nenek (The Matriarch)": {
                "Daster Batik & Bergo Instan": "Wearing a faded daily batik floral daster with short sleeves, paired with a simple, well-worn comfortable instant jersey bergo hijab covering her head and neck.",
                "Kaos Panjang & Jilbab Kaos": "Wearing a modest, oversized long-sleeved cotton house shirt in faded neutral colors, paired with a simple daily instant jersey hijab and a cotton sarong tied at the waist.",
                "Daster Lowo & Kerudung Lilit": "Wearing a loose, wide 'bat-wing' (lowo) batik patterned daster with a simple thin cotton scarf wrapped loosely and comfortably around her head as a daily hijab.",
                "Baju Kurung Katun & Hijab Slup": "Wearing a simple, humble Indonesian-style modest cotton baju kurung with a practical jersey instant hijab for a neat, grandmotherly home look.",
                "Tunik Kancing & Bergo Tali": "Wearing a front-buttoned cotton tunic shirt with minor wrinkles, paired with an instant bergo hijab that has simple ties at the back of the head.",
                "Setelan Celana Kaos & Jilbab": "Wearing a matching daily pajama set of a long-sleeved cotton tunic and loose trousers in faded colors, paired with a breathable instant jersey hijab."
            },
            "Nenek Simbah": {
                "Kebaya Kutubaru & Jarik Parang": "Wearing a daily-worn, faded floral cotton kebaya kutubaru fastened with a vintage safety pin, paired with a dark-brown batik jarik cloth in Parang motif and a thin cotton scarf loosely wrapped as a hijab.",
                "Daster Batik Solo & Bergo Tali": "Wearing an authentic brown Batik Solo daster with a classic 'Sogan' pattern, paired with a simple jersey instant hijab that has ties at the back, showing a traditional home look.",
                "Kaos Lengan Panjang & Jarik Lawasan": "Wearing a modest long-sleeved cotton shirt in earth tones, paired with a weathered, well-washed 'Lawasan' batik jarik cloth and a simple instant hijab tied neatly under the chin.",
                "Daster Lowo (Kalong) & Kerudung Lilit": "Wearing a loose, oversized 'bat-wing' (lowo) batik daster with a large traditional motif, complemented by a thin cotton scarf wrapped comfortably around her head in a simple village style.",
                "Kebaya Kartini Katun & Sarung": "Wearing a very simple, non-formal cotton Kebaya Kartini in a faded solid color, paired with a comfortable batik sarong and a daily instant bergo hijab for a humble appearance.",
                "Setelan Celana Batik & Jilbab Kaos": "Wearing a matching daily batik pajama set consisting of a long-sleeved tunic and loose trousers, paired with a breathable instant jersey hijab in a matching muted earth tone."
            },
            "Nenek Sunda": {
                "Daster Floral & Bergo Kaos": "Wearing a bright but faded floral-patterned Sundanese-style daster with a soft, well-washed instant jersey bergo hijab that looks comfortable for daily house chores.",
                "Kebaya Bordir Katun & Sarung": "Wearing a simple, humble cotton kebaya with subtle embroidery (bordir) on the edges, paired with a faded floral sarong and a thin cotton scarf loosely draped as a hijab.",
                "Setelan Celana Kaos & Jilbab Instan": "Wearing a modest long-sleeved cotton pajama set with small floral motifs, paired with a simple daily instant jersey hijab in a soft, matching pastel color.",
                "Daster Kancing Depan & Bergo Tali": "Wearing a practical front-buttoned cotton daster in a light color, paired with a simple instant bergo hijab that has ties at the back, perfect for an elderly grandmother's daily look.",
                "Tunik Katun & Sarung Batik": "Wearing a loose, breathable cotton tunic shirt paired with a faded West Javanese batik sarong and a simple daily instant hijab tied neatly under the chin.",
                "Daster Lowo Floral & Kerudung Lilit": "Wearing a wide 'bat-wing' (lowo) daster with a vibrant but aged floral print, complemented by a thin pashmina-style cotton scarf wrapped simply and loosely around her head."
            },
            "Nenek Melayu": {
                "Baju Kurung Kedah & Sarung": "Wearing a traditional short-cut daily Baju Kurung Kedah made of soft faded cotton with floral prints, paired with a matching batik sarong and a simple cotton bawal hijab pinned under the chin.",
                "Baju Kurung Pesak & Tudung Sarung": "Wearing a classic loose-fitting Baju Kurung Pesak in a muted solid color, paired with a practical 'tudung sarung' (instant jersey hijab) that covers the chest comfortably.",
                "Daster Panjang & Hijab Instan": "Wearing a modest long-sleeved cotton daster with traditional Melayu floral motifs, complemented by a simple daily instant jersey hijab in a matching faded tone.",
                "Kaos Tunik & Sarung Pelikat": "Wearing a long-sleeved cotton tunic shirt paired with a faded cotton sarong and a simple bawal hijab loosely draped over her head, showing a relaxed home-stay vibe.",
                "Baju Kurung Moden & Bergo Tali": "Wearing a very simple daily Baju Kurung Moden made of breathable rayon fabric, paired with a simple instant bergo hijab that has ties at the back for comfort.",
                "Kebaya Labuh & Hijab Slup": "Wearing a modest, long-length daily Kebaya Labuh made of lightweight cotton, paired with a faded floral sarong and a practical instant jersey hijab for a neat grandmotherly look."
            },

            # --- KELOMPOK GADIS ---
            "Gadis Desa (The Natural)": {
                "Kaos Putih & Pashmina Abu": "Wearing a trendy white long-sleeved oversized cotton t-shirt paired with a soft grey pashmina shawl wrapped stylishly around her head.",
                "Kaos Abu & Hijab Putih": "Wearing a fresh light grey long-sleeved t-shirt with a clean white square hijab neatly tucked and pinned under her chin.",
                "Hoodie Putih & Hijab Abu": "Wearing a comfortable white oversized hoodie and a simple grey jersey hijab tucked inside the collar for a modern modest look.",
                "Kaos Abu & Pashmina Hitam": "Wearing a charcoal grey long-sleeved shirt with a black pashmina loosely draped around her shoulders and head for a casual aesthetic.",
                "Daster Putih & Bergo Abu": "Wearing a modern white cotton homedress with subtle lace details paired with a simple soft grey instant jersey hijab.",
                "Daster Abu & Pashmina Putih": "Wearing a comfortable light grey floral patterned daster and a white pashmina loosely wrapped around her head for a fresh home look.",
                "Kaos Panjang Putih & Rok Abu": "Wearing a plain white long-sleeved t-shirt tucked into a long grey flowy skirt with a matching grey jersey hijab.",
                "Homedress Abu & Hijab Putih": "Wearing a stylish charcoal grey homedress with long sleeves and a clean white square hijab neatly pinned, looking fresh and happy."
            },
            "Gadis Rumi (The Dreamer)": {
                "Kaos Putih & Pashmina Abu": "Wearing a trendy white long-sleeved oversized cotton t-shirt paired with a soft grey pashmina shawl wrapped stylishly around her head.",
                "Kaos Abu & Hijab Putih": "Wearing a fresh light grey long-sleeved t-shirt with a clean white square hijab neatly tucked and pinned under her chin.",
                "Hoodie Putih & Hijab Abu": "Wearing a comfortable white oversized hoodie and a simple grey jersey hijab tucked inside the collar for a modern modest look.",
                "Kaos Abu & Pashmina Hitam": "Wearing a charcoal grey long-sleeved shirt with a black pashmina loosely draped around her shoulders and head for a casual aesthetic.",
                "Daster Putih & Bergo Abu": "Wearing a modern white cotton homedress with subtle lace details paired with a simple soft grey instant jersey hijab.",
                "Daster Abu & Pashmina Putih": "Wearing a comfortable light grey floral patterned daster and a white pashmina loosely wrapped around her head for a fresh home look.",
                "Kaos Panjang Putih & Rok Abu": "Wearing a plain white long-sleeved t-shirt tucked into a long grey flowy skirt with a matching grey jersey hijab.",
                "Homedress Abu & Hijab Putih": "Wearing a stylish charcoal grey homedress with long sleeves and a clean white square hijab neatly pinned, looking fresh and happy."
            },
            "Gadis Melati (The Fresh)": {
                "Kaos Putih & Pashmina Abu": "Wearing a trendy white long-sleeved oversized cotton t-shirt paired with a soft grey pashmina shawl wrapped stylishly around her head.",
                "Kaos Abu & Hijab Putih": "Wearing a fresh light grey long-sleeved t-shirt with a clean white square hijab neatly tucked and pinned under her chin.",
                "Hoodie Putih & Hijab Abu": "Wearing a comfortable white oversized hoodie and a simple grey jersey hijab tucked inside the collar for a modern modest look.",
                "Kaos Abu & Pashmina Hitam": "Wearing a charcoal grey long-sleeved shirt with a black pashmina loosely draped around her shoulders and head for a casual aesthetic.",
                "Daster Putih & Bergo Abu": "Wearing a modern white cotton homedress with subtle lace details paired with a simple soft grey instant jersey hijab.",
                "Daster Abu & Pashmina Putih": "Wearing a comfortable light grey floral patterned daster and a white pashmina loosely wrapped around her head for a fresh home look.",
                "Kaos Panjang Putih & Rok Abu": "Wearing a plain white long-sleeved t-shirt tucked into a long grey flowy skirt with a matching grey jersey hijab.",
                "Homedress Abu & Hijab Putih": "Wearing a stylish charcoal grey homedress with long sleeves and a clean white square hijab neatly pinned, looking fresh and happy."
            },
            "Gadis Anisa (The Modest)": {
                "Kaos Putih & Pashmina Abu": "Wearing a trendy white long-sleeved oversized cotton t-shirt paired with a soft grey pashmina shawl wrapped stylishly around her head.",
                "Kaos Abu & Hijab Putih": "Wearing a fresh light grey long-sleeved t-shirt with a clean white square hijab neatly tucked and pinned under her chin.",
                "Hoodie Putih & Hijab Abu": "Wearing a comfortable white oversized hoodie and a simple grey jersey hijab tucked inside the collar for a modern modest look.",
                "Kaos Abu & Pashmina Hitam": "Wearing a charcoal grey long-sleeved shirt with a black pashmina loosely draped around her shoulders and head for a casual aesthetic.",
                "Daster Putih & Bergo Abu": "Wearing a modern white cotton homedress with subtle lace details paired with a simple soft grey instant jersey hijab.",
                "Daster Abu & Pashmina Putih": "Wearing a comfortable light grey floral patterned daster and a white pashmina loosely wrapped around her head for a fresh home look.",
                "Kaos Panjang Putih & Rok Abu": "Wearing a plain white long-sleeved t-shirt tucked into a long grey flowy skirt with a matching grey jersey hijab.",
                "Homedress Abu & Hijab Putih": "Wearing a stylish charcoal grey homedress with long sleeves and a clean white square hijab neatly pinned, looking fresh and happy."
            },

            # --- KELOMPOK KAKEK ---
            "Kakek (The Wise)": {
                "Kaos Putih & Peci Hitam": "Wearing a simple plain white cotton t-shirt with a classic black velvet Peci (songkok) on his head for a humble daily look.",
                "Baju Koko Abu & Peci": "Wearing a daily light grey Baju Koko with subtle embroidery on the chest and a neat black Peci on his head.",
                "Kaos Abu & Sarung Putih": "Wearing a comfortable charcoal grey long-sleeved t-shirt paired with a white patterned sarong wrapped around his waist.",
                "Kemeja Putih & Peci": "Wearing an old, well-worn short-sleeved white button-down shirt and a classic black Peci, looking dignified and fatherly."
            },
            "Kakek Wiryo (The Artisan)": {
                "Kaos Putih & Peci Hitam": "Wearing a simple plain white cotton t-shirt with a classic black velvet Peci (songkok) on his head for a humble daily look.",
                "Baju Koko Abu & Peci": "Wearing a daily light grey Baju Koko with subtle embroidery on the chest and a neat black Peci on his head.",
                "Kaos Abu & Sarung Putih": "Wearing a comfortable charcoal grey long-sleeved t-shirt paired with a white patterned sarong wrapped around his waist.",
                "Kemeja Putih & Peci": "Wearing an old, well-worn short-sleeved white button-down shirt and a classic black Peci, looking dignified and fatherly."
            },
            "Kakek Joyo (The Farmer)": {
                "Kaos Putih & Peci Hitam": "Wearing a simple plain white cotton t-shirt with a classic black velvet Peci (songkok) on his head for a humble daily look.",
                "Baju Koko Abu & Peci": "Wearing a daily light grey Baju Koko with subtle embroidery on the chest and a neat black Peci on his head.",
                "Kaos Abu & Sarung Putih": "Wearing a comfortable charcoal grey long-sleeved t-shirt paired with a white patterned sarong wrapped around his waist.",
                "Kemeja Putih & Peci": "Wearing an old, well-worn short-sleeved white button-down shirt and a classic black Peci, looking dignified and fatherly."
            },
            "Kakek Usman (The Silent)": {
                "Kaos Putih & Peci Hitam": "Wearing a simple plain white cotton t-shirt with a classic black velvet Peci (songkok) on his head for a humble daily look.",
                "Baju Koko Abu & Peci": "Wearing a daily light grey Baju Koko with subtle embroidery on the chest and a neat black Peci on his head.",
                "Kaos Abu & Sarung Putih": "Wearing a comfortable charcoal grey long-sleeved t-shirt paired with a white patterned sarong wrapped around his waist.",
                "Kemeja Putih & Peci": "Wearing an old, well-worn short-sleeved white button-down shirt and a classic black Peci, looking dignified and fatherly."
            }
        }

        # --- 3. MASTER BAHAN (ARCHITECTURAL PRECISION: 90% PROGRESS INTERACTIVE) ---
        MASTER_KONTEN_ALL = {
            "🕌 Miniatur Masjid": {
                "Permen Kristal": "A monumental, large-scale 1-meter mosque diorama built entirely from millions of glossy pink bubblegum pieces and turquoise taffy blocks. The architecture looks massive and grand, with tiny detailed sugar-texture patterns that suggest a giant scale. The main dome is a colossal, translucent strawberry jelly sphere filled with a vast galaxy of thousands of twinkling fiber-optic star lights. Every entrance arch is lined with hundreds of tiny, flickering multi-colored sugar-drop LEDs. The shot is a straight-on, eye-level view of the massive candy building, showing its immense size and intricate sugary craftsmanship against a dark background, making the building look like a giant glowing sugary cathedral.",
                "Cokelat Lumer": "A colossal, large-scale 1-meter mosque diorama built entirely from rich, glossy dark chocolate and gold-dusted milk chocolate slabs. The structure is massive and grand, with intricate textures suggesting an immense architectural scale. The main dome is a sphere of smooth, melted chocolate glaze, with powerful multi-colored LED wash lights from beneath (cyan, magenta, yellow) reflecting and swirling on its surface. The tall minarets are wrapped in tightly packed, intensely flickering colorful sugar-fairy lights. All entrance arches are outlined with dancing, vibrant RGB neon strips, casting a magical, colorful glow against the dark, high-contrast background.",
                "Wafer Lego": "A monumental, large-scale 1-meter mosque model constructed from hundreds of layers of vibrant colored wafer sheets and Lego-like plastic blocks. The building is massive, with sharp geometric patterns and intricate details highlighting its giant size. The main dome is made of translucent Lego bricks with dynamic, rapidly pulsing internal multi-colored LED matrix (RGB), creating a colorful disco-like pattern. All minarets are topped with intense multi-colored laser pointers. Every edge and arch of the massive structure is lined with flickering, intensely saturated colorful strip-lights, making the mosque look like a giant glowing toy city under a dark environment.",
                "Jeli & Marshmallow": "A gigantic, large-scale 1-meter mosque diorama built entirely from massive translucent grape-jelly blocks and soft pink marshmallow textures. The structure has a glowing, slightly wobbly look that suggests an enormous scale. The colossal main dome is a sphere of clear gelatin with powerful, colorful fiber-optic lines (purple, green, blue) swirling inside like a galaxy. Every minaret is a tall pillar made of striped colorful candy cane, wrapped in intensely bright, rapidly flickering colorful sugar- fairy lights. The entrance arches are framed by intense colorful (RGB) neon tubing, casting a powerful, saturated multi-colored wash over the entire glossy jelly surface against a dark, high-contrast environment.",
                "Lapis Legit": "A gigantic, large-scale 1-meter mosque model built from hundreds of layers of brown and gold buttery cake textures and glossy syrup glazes. The building is monumental and grand, featuring intricate layered patterns that suggest a massive architectural size. The colossal main dome is a sphere of glowing golden honey with intense internal multi-colored LED wash lights. Every minaret is wrapped in tightly packed, rapidly pulsing colorful fairy lights, with entrance arches outlined in vibrant, dancing RGB neon tubing.",
                "Es Krim Pelangi": "A colossal, large-scale 1-meter mosque diorama made of dense, glossy rainbow-colored ice cream scoops and frozen fruit-syrup layers. The structure looks massive and solid, with a cold, frosted texture suggesting a monumental scale. The main dome is a gigantic sphere of translucent pink-grape jelly filled with thousands of twinkling fiber-optic lights. Every pillar is wrapped in intensely flickering multi-colored fairy lights, while all arches are outlined with vibrant, saturated RGB neon strips that glow powerfully against the dark background.",
                "Keramik Mozaik": "A monumental, large-scale 1-meter mosque diorama constructed from thousands of tiny, glossy multi-colored ceramic tiles and iridescent glass pieces. The architecture is grand and massive, with complex mosaic patterns suggesting a giant scale. The main dome is a colossal sphere of polished turquoise porcelain, glowing from within with powerful multi-colored LED lights. The entire 1-meter structure is traced with intensely bright, flickering RGB neon lines and colorful sugar-drop LEDs around every entrance, creating a magical glowing masterpiece.",
                "Buah Melon": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of glossy cantaloupe melon pieces and translucent green rind blocks. The architecture is massive with a colossal main dome made of polished melon flesh segments glowing with internal multi-colored LED wash lights. Tall minarets crafted from melon rinds are wrapped in intensely flickering colorful LED fairy lights. All entrance arches are outlined with dancing, vibrant RGB neon strips.",
                "Buah Strawberyy": "A gigantic, large-scale 1-meter standalone mosque object built entirely from millions of vibrant red strawberry flesh slices and glossy whipped cream textures. Featuring a colossal main dome made of densely packed strawberry slices with intense internal multi-colored LED wash lights. Every minaret is a tall pillar wrapped in rapidly pulsing colorful fairy lights, with entrance arches outlined in vibrant, dancing RGB neon tubing.",
                "Buah Semangka": "A monumental, large-scale 1-meter standalone mosque object constructed from millions of vibrant red watermelon cubes and glossy green-striped rind blocks. The colossal main dome is a sphere made of densely packed watermelon flesh with thousands of twinkling multi-colored fiber-optic star lights. Every pillar and minaret is wrapped in intensely flickering colorful LED fairy lights and vibrant multi-colored neon strips.",
                "Buah Naga": "A colossal, large-scale 1-meter standalone mosque object built entirely from high-gloss white dragonfruit pieces with black seeds and bright magenta rind slabs. The colossal main dome is a sphere of polished dragonfruit flesh with colorful fiber-optic lines swirling inside. Every minaret is a tall pillar wrapped in intensely bright, flickering colorful LED fairy lights and framed by intense RGB neon tubing.",
                "Buah Pepaya": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of vibrant orange papaya flesh cubes and glossy green-striped rind blocks. The architecture is massive with a colossal main dome made of densely packed, polished papaya segments with black seeds integrated, glowing from within with powerful rotating multi-colored LED wash lights. Tall minarets are crafted from pepaya rinds, wrapped in intensely flickering colorful LED fairy lights. All entrance arches are outlined with dancing, vibrant RGB neon strips.",
                "Buah Jeruk": "A gigantic, large-scale 1-meter standalone mosque object built entirely from millions of vibrant orange citrus pulp sacs and translucent orange rind segments. The building is monumental with a colossal main dome made of thousands of interlocking, glossy orange wedges with powerful internal multi-colored LED wash lights reflecting on its juicy texture. Every minaret is a tall pillar made of tightly packed citrus sacs wrapped in rapidly pulsing colorful fairy lights, with entrance arches outlined in vibrant, dancing RGB neon tubing.",
                "Buah Anggur": "A monumental, large-scale 1-meter standalone mosque object constructed from thousands of glossy purple and green grape halves and intricate grape-vine textures. The colossal main dome is a sphere made of densely packed, translucent grape halves with thousands of twinkling multi-colored fiber-optic star lights integrated into the seeds. Every pillar and minaret is a tall stack of variegated grapes wrapped in intensely flickering colorful LED fairy lights. The entrance arches are framed by intense colorful RGB neon tubing, casting a powerful, saturated multi-colored wash over the entire glossy fruity surface.",
                "Buah Tomat": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of vibrant red tomato halves and translucent green stem segments. The architecture is massive with a colossal main dome made of densely packed, polished tomato flesh with black seeds integrated, glowing from within with powerful rotating multi-colored LED wash lights. Tall minarets are crafted from green stem segments, wrapped in intensely flickering colorful LED fairy lights. All entrance arches are outlined with dancing, vibrant RGB neon strips.",
                "Buah Wortel": "A gigantic, large-scale 1-meter standalone mosque object built entirely from millions of vibrant orange carrot sticks and translucent orange carrot peel segments. The building is monumental with a colossal main dome made of thousands of interlocking, glossy orange wedges with powerful internal multi-colored LED wash lights reflecting on its textured surface. Every minaret is a tall pillar made of tightly packed carrot sticks wrapped in rapidly pulsing colorful fairy lights, with entrance arches outlined in vibrant, dancing RGB neon tubing.",
                "Buah Pisang": "A monumental, large-scale 1-meter standalone mosque object constructed from thousands of glossy yellow banana slices and intricate banana-leaf textures. The colossal main dome is a sphere made of densely packed, translucent banana slices with thousands of twinkling multi-colored fiber-optic star lights integrated into the seeds. Every pillar and minaret is a tall stack of variegated bananas wrapped in intensely flickering colorful LED fairy lights. The entrance arches are framed by intense colorful RGB neon tubing, casting a powerful, saturated multi-colored wash over the entire glossy fruity surface.",
                "Buah Durian": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of sharp, golden durian thorns and creamy yellow durian flesh. The architecture looks massive and aggressive, with a colossal main dome made of smooth durian pulp segments glowing from within with powerful multi-colored LED wash lights. Tall minarets are crafted from thorny rinds, wrapped in intensely flickering colorful LED fairy lights. All entrance arches are outlined with dancing, vibrant RGB neon strips.",
                "Buah Markisa": "A gigantic, large-scale 1-meter standalone mosque object built entirely from translucent orange passionfruit pulp and millions of crunchy black seeds. The main dome is a colossal sphere of glossy passionfruit juice with powerful internal multi-colored LED wash lights that make the seeds look like a swirling galaxy. Every minaret is a tall pillar made of hard purple markisa skins wrapped in rapidly pulsing colorful fairy lights, with entrance arches outlined in vibrant, dancing RGB neon tubing.",
                "Buah Kiwi": "A monumental, large-scale 1-meter standalone mosque object constructed from millions of vibrant green kiwi slices and fuzzy brown skin textures. The colossal main dome is a sphere made of polished green kiwi flesh with its ring of black seeds glowing from within using thousands of twinkling multi-colored fiber-optic star lights. Every pillar is a stack of kiwi slices wrapped in intensely flickering colorful LED fairy lights, with entrance arches framed by intense colorful RGB neon tubing.",
                "Buah Salak": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of glossy, dark-brown snake-fruit (salak) scales and polished white salak flesh. The architecture looks grand and ancient, with a colossal main dome made of overlapping salak scales, glowing from within with powerful multi-colored LED wash lights that reflect on the scaly texture. Tall minarets are crafted from salak skin, wrapped in intensely flickering colorful LED fairy lights. All entrance arches are outlined with dancing, vibrant RGB neon strips.",
                "Buah Manggis": "A gigantic, large-scale 1-meter standalone mosque object built entirely from deep purple, thick mangosteen rinds and snow-white mangosteen flesh segments. The main dome is a colossal sphere made of polished white mangosteen segments, glowing from within with powerful internal multi-colored LED wash lights that make the white flesh look like glowing porcelain. Every minaret is a tall pillar made of dark purple rinds wrapped in rapidly pulsing colorful fairy lights, with entrance arches outlined in vibrant, dancing RGB neon tubing.",
                "Buah Alpukat": "A monumental, large-scale 1-meter standalone mosque object constructed from millions of creamy green avocado flesh cubes and dark, pebbled avocado skin textures. The colossal main dome is a sphere made of polished green avocado segments with a large brown avocado seed at the very top, glowing from within with thousands of twinkling multi-colored fiber-optic star lights. Every pillar is a stack of dark-skinned avocado segments wrapped in intensely flickering colorful LED fairy lights, with entrance arches framed by intense colorful RGB neon tubing.",
                "Daun Talas": "A monumental, large-scale 1-meter standalone mosque object built entirely from massive, glossy green taro leaves (talas) with thick, prominent veins. The architecture is grand with a colossal main dome made of overlapping fresh green leaves, glowing from within with powerful multi-colored LED wash lights that highlight the intricate natural vein patterns. Tall minarets are crafted from rolled leaf stalks, wrapped in intensely flickering colorful LED fairy lights. All entrance arches are outlined with dancing, vibrant RGB neon strips.",
                "Daun Jati": "A gigantic, large-scale 1-meter standalone mosque object built entirely from broad, textured teak leaves (jati) with a rustic, organic feel. The main dome is a colossal sphere made of dried golden-brown teak leaves, glowing from within with powerful internal multi-colored LED wash lights that create a warm, magical atmosphere. Every minaret is a tall pillar made of layered leaf textures wrapped in rapidly pulsing colorful fairy lights, with entrance arches outlined in vibrant, dancing RGB neon tubing.",
                "Daun Keladi": "A monumental, large-scale 1-meter standalone mosque object constructed from millions of vibrant, multi-colored caladium leaves (keladi) with intense pink, white, and green patterns. The colossal main dome is a sphere of translucent leaf tissues with thousands of twinkling multi-colored fiber-optic star lights reflecting off the natural leaf pigments. Every pillar is a stack of variegated leaves wrapped in intensely flickering colorful LED fairy lights, with entrance arches framed by intense colorful RGB neon tubing.",
                "Daun Pisang": "A monumental, large-scale 1-meter standalone mosque object built entirely from fresh, glossy green banana leaves (daun pisang) and thick, brown textured banana trunks. The architecture is grand with a colossal main dome made of millions of intricately woven green banana leaf pieces, glowing from within with powerful rotating multi-colored LED wash lights that reflect on the glossy, waxy surface. Tall minarets are crafted from rolled banana leaves and trunks, wrapped in intensely flickering colorful LED fairy lights. All entrance arches are outlined with dancing, vibrant RGB neon strips.",
                "Daun Palem": "A gigantic, large-scale 1-meter standalone mosque object built entirely from millions of dry, golden-brown palm fronds (daun palem) and hard, textured palm seeds. The main dome is a colossal sphere made of thousands of interlocking, dry palm leaves with powerful internal multi-colored LED wash lights that create a warm, magical, and rustic atmosphere. Every minaret is a tall pillar made of tightly packed, interwoven palm fronds wrapped in rapidly pulsing colorful fairy lights, with entrance arches outlined in vibrant, dancing RGB neon tubing.",
                "Daun Pakis": "A monumental, large-scale 1-meter standalone mosque object constructed from thousands of vibrant green, feathery fern fronds (daun pakis) and fuzzy brown fern spores. The colossal main dome is a sphere made of densely packed, overlapping fern fronds with thousands of twinkling multi-colored fiber-optic star lights integrated into the delicate, intricate pakis patterns. Every pillar and minaret is a tall stack of variegated, feathery ferns wrapped in intensely flickering colorful LED fairy lights. The entrance arches are framed by intense colorful RGB neon tubing, casting a powerful, saturated multi-colored wash over the entire lush, leafy surface.",
                "Daun Kelapa": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of woven green janur leaves. The architecture features an intricate diamond-weave pattern. The colossal main dome glows from within with a 'Tropical Sunset' LED scheme (warm orange, deep violet, and lime green) seeping through the weave. Tall minarets are wrapped in flickering amber and teal fairy lights, with entrance arches outlined in pulsing electric-blue neon strips.",
                "Jerami": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from millions of dry, golden rice straws. The colossal main dome is a sphere of straw with a 'Midnight Gold' LED scheme (warm gold, deep blue, and white) twinkling like stars through the fiber. Every minaret is wrapped in rapidly pulsing ice-white fairy lights, with entrance arches outlined in vibrant violet and gold RGB neon tubing.",
                "Bambu Anyam": "A monumental, large-scale 1-meter standalone mosque object built from thousands of glossy bamboo strips. The architecture features complex woven geometries. The colossal main dome glows with a 'Cyber-Forest' LED scheme (neon green, cyan, and magenta) pulsing from the inside. Every pillar is wrapped in intensely flickering emerald-green fairy lights, with entrance arches outlined in dancing, high-contrast pink neon strips.",
                "Daun Kering": "A monumental, large-scale 1-meter standalone mosque object built from thousands of crunchy, brown autumn leaves. The colossal main dome features a 'Volcanic Glow' LED scheme (fire red, burning orange, and sulfur yellow) creating a powerful internal heat effect. Tall minarets are wrapped in flickering red and orange fairy lights, with entrance arches outlined in intense, steady warm-white neon strips for a dramatic look.",
                "Daun Pandan": "A monumental, large-scale 1-meter standalone mosque object built from thousands of long, slender green pandan leaves woven in a herringbone pattern. The colossal main dome glows with a 'Neon Mint' LED scheme (electric lime, soft mint, and bright white) pulsing through the leaf gaps. Tall minarets are wrapped in flickering forest-green fairy lights, with entrance arches outlined in vibrant, dancing turquoise neon strips.",
                "Daun Sirih": "A gigantic, large-scale 1-meter standalone mosque model constructed from millions of glossy, heart-shaped betel leaves (sirih). The architecture is grand with a colossal main dome made of overlapping dark green leaves, glowing with a 'Deep Emerald' LED scheme (emerald green, violet, and gold). Every minaret is wrapped in rapidly pulsing purple fairy lights, with entrance arches outlined in intense gold and green RGB neon tubing.",
                "Daun Suji": "A monumental, large-scale 1-meter standalone mosque object built from dense, dark-green suji leaves. The colossal main dome features a 'Radioactive Glow' LED scheme (neon green, cyan, and lemon yellow) creating an intense internal light effect. Tall minarets are wrapped in flickering cyan fairy lights, with entrance arches outlined in steady, high-contrast pink and green neon strips for a pop-art look.",
                "Daun Paku": "A monumental, large-scale 1-meter standalone mosque object made from thousands of feathery, intricate fern leaves (daun paku). The colossal main dome looks like a lush green galaxy with a 'Starlight Forest' LED scheme (soft blue, magenta, and warm white) twinkling through the delicate fronds. Every pillar is wrapped in intensely flickering multi-colored fairy lights, with entrance arches outlined in vibrant, saturated rainbow neon strips.",
                "Rotan Anyam": "A monumental, large-scale 1-meter standalone mosque object built from thousands of glossy, woven rattan strips in a complex 3D pattern. The architecture is grand with a colossal main dome made of interwoven young rattan. The dome and main walls are adorned with intricate, embossed Thuluth-style calligraphy carved directly into wide rattan bands, featuring a 'Sunset Amber' LED scheme (deep orange, warm gold, and soft red) glowing through the calligraphy and weave. Tall minarets are wrapped in flickering amber fairy lights, with entrance arches outlined in pulsing electric-blue neon strips.",
                "Jati Ukir": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from rich, dark-brown teak wood blocks and slabs. The building is monumental and heavy, with intricate patterns suggesting an immense scale. The entire facade and the colossal main dome are covered in deep, precise Kufic-style calligraphy and floral ukiran timbul, glowing from within with powerful internal 'Volcanic Glow' LED wash lights (fire red, burning orange, and sulfur yellow) highlighting the carved edges. Every minaret is a tall pillar of carved teak wrapped in rapidly pulsing ice-white fairy lights, with entrance arches outlined in vibrant gold RGB neon tubing.",
                "Bambu Kaligrafi": "A monumental, large-scale 1-meter standalone mosque object built from thousands of fine, glossy bamboo strips and sturdy bamboo poles. The architecture features complex woven geometries. The colossal main dome features intricate Diwani-style calligraphy intricately woven with dark bamboo threads against a lighter bamboo background, pulsing with a 'Cyber-Forest' LED scheme (neon green, cyan, and magenta) from the inside. Every pillar is wrapped in intensely flickering emerald-green fairy lights, with entrance arches outlined in dancing, high-contrast pink neon strips.",
                "Kayu Cendana": "A monumental, large-scale 1-meter standalone mosque object made from polished, light-brown sandalwood. The building looks extremely delicate with a high-gloss finish suggesting a monumental architectural scale. The colossal main dome is a sphere covered in intricate, elegant Naskh-style calligraphy carved with extreme precision and gold leaf inlays, featuring thousands of twinkling multi-colored fiber-optic star lights integrated into the calligraphy dots and a soft, warm internal 'Royal White' LED glow. Every pillar is wrapped in intensely flickering colorful fairy lights, with entrance arches framed by intense colorful RGB neon tubing.",
                "Kaleng Bekas": "A monumental, large-scale 1-meter standalone mosque object built from thousands of crushed and polished aluminum soda cans. The architecture features a metallic mosaic texture with embossed Kufic calligraphy hammered into the metal surfaces. The colossal main dome glows with a 'Cyber-Steel' LED scheme (ice blue, violet, and silver white) reflecting off the sharp metallic edges. Tall minarets are wrapped in flickering cyan fairy lights, with entrance arches outlined in pulsing magenta neon strips.",
                "Botol Plastik": "A gigantic, large-scale 1-meter standalone mosque model constructed from millions of shredded clear and blue plastic bottles. The structure is translucent with intricate Thuluth-style calligraphy etched into the plastic layers. The colossal main dome is a sphere of melted recycled plastic with a 'Toxic Neon' LED scheme (lime green, electric yellow, and cyan) glowing from within like a radioactive jewel. Every minaret is wrapped in rapidly pulsing green fairy lights, with entrance arches outlined in vibrant orange RGB neon tubing.",
                "Kardus Retro": "A monumental, large-scale 1-meter standalone mosque object built from thousands of layers of corrugated brown cardboard and recycled paper pulp. The architecture features deep, laser-cut Naskh-style calligraphy that reveals the internal honeycomb structure of the cardboard. The colossal main dome features a 'Warm Industrial' LED scheme (incandescent yellow, deep amber, and soft red) glowing through the calligraphy cuts. Every pillar is wrapped in flickering warm-white fairy lights, with entrance arches framed by intense copper-colored neon strips.",
                "Komponen Elektronik": "A colossal, large-scale 1-meter standalone mosque object made from thousands of recycled circuit boards (PCBs), copper wires, and microchips. The architecture is incredibly complex with Diwani-style calligraphy formed by intricate gold-plated wire paths. The colossal main dome pulses with a 'Digital Matrix' LED scheme (neon green, bright white, and deep purple) following the circuit patterns. Every minaret is a tall pillar of stacked microchips wrapped in intensely flickering colorful LED fairy lights and framed by intense RGB neon tubing.",
                "Kaca Patri": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of jagged, iridescent stained-glass shards and lead frames. The architecture is sharp and crystalline with intricate Thuluth-style calligraphy etched into the glass. The colossal main dome glows with a 'Prism Galaxy' LED scheme (rainbow colors, deep violet, and bright cyan) reflecting and refracting through every glass edge. Tall minarets are wrapped in flickering white-starlight fairy lights, with entrance arches outlined in vibrant, dancing neon-purple strips.",
                "Tembaga Bakar": "A gigantic, large-scale 1-meter standalone mosque model constructed from hammered, heat-treated copper plates and brass wires. The building has a rustic but metallic texture with deep, embossed Kufic-style calligraphy. The colossal main dome features a 'Magma Amber' LED scheme (burning orange, deep red, and warm gold) glowing through the calligraphy punch-holes. Every minaret is a tall pillar of twisted copper wrapped in rapidly pulsing amber fairy lights, with entrance arches outlined in intense warm-white neon tubing.",
                "Sutra Tenun": "A monumental, large-scale 1-meter standalone mosque object built from millions of vibrant silk threads and hand-woven songket fabrics with gold threads. The architecture is soft but structured with elegant Diwani-style calligraphy embroidered in gold leaf. The colossal main dome pulses with a 'Royal Velvet' LED scheme (deep magenta, royal blue, and golden yellow) glowing from behind the translucent silk layers. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense, saturated RGB neon tubing.",
                "Batu Alam": "A colossal, large-scale 1-meter standalone mosque object made from thousands of tiny slabs of polished marble, black obsidian, and white quartz. The architecture is heavy and grand with Naskh-style calligraphy carved deep into the stone. The colossal main dome features a 'Moonlight Quartz' LED scheme (ice blue, soft white, and pale lilac) glowing through the translucent stone veins. Every minaret is a stack of carved marble wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Koran Bekas": "A monumental, large-scale 1-meter standalone mosque object built from millions of rolled and folded recycled newspaper strips. The architecture features a dense grayscale texture of printed text and news-photos. Intricate Thuluth-style calligraphy is laser-cut through the paper layers, glowing with a 'News-Flash' LED scheme (bright white, pale cyan, and amber) seeping through the text-filled walls. Tall minarets are crafted from tightly rolled newspaper tubes, wrapped in flickering cool-white fairy lights, with entrance arches outlined in pulsing electric-blue neon strips.",
                "Bungkus Kopi": "A gigantic, large-scale 1-meter standalone mosque model constructed from thousands of glossy, metallic recycled coffee sachets and snack wrappers. The building is incredibly vibrant and reflective with a patchwork mosaic texture. Embossed Kufic-style calligraphy is hammered into the silver-foil insides of the wrappers. The colossal main dome pulses with a 'Pop-Art' LED scheme (vibrant magenta, electric lime, and bright orange) reflecting off the metallic foil. Every minaret is wrapped in rapidly pulsing rainbow fairy lights, with entrance arches outlined in intense neon-green tubing.",
                "Majalah": "A monumental, large-scale 1-meter standalone mosque object built from thousands of shredded high-gloss fashion magazines. The architecture features a colorful, fragmented texture with a high-shine finish. Elegant Diwani-style calligraphy is formed by raised layers of colorful paper pulp. The colossal main dome features a 'Prismatic Gloss' LED scheme (violet, hot pink, and sky blue) glowing through the glossy paper edges. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense, saturated RGB neon tubing.",
                "Kardus Bekas": "A colossal, large-scale 1-meter standalone mosque object made from raw, corrugated brown cardboard and recycled egg cartons. The architecture features a heavy, industrial texture with deep Naskh-style calligraphy carved to reveal the honeycomb interior. The colossal main dome glows with an 'Industrial Hearth' LED scheme (fire red, deep orange, and warm tungsten yellow) creating a powerful internal glow. Every minaret is a tall pillar of stacked cardboard rings wrapped in flickering warm-white fairy lights and framed by intense copper-colored neon strips.",
                "Tutup Botol": "A monumental, large-scale 1-meter standalone mosque object built from millions of colorful recycled plastic bottle caps. The architecture features a vibrant, circular-pixelated texture. Intricate Thuluth-style calligraphy is embossed into the plastic surfaces. The colossal main dome glows with a 'Neon Carnival' LED scheme (vibrant magenta, lime green, and electric blue) pulsing through the gaps between the caps. Tall minarets are crafted from stacks of translucent caps, wrapped in flickering multi-colored fairy lights, with entrance arches outlined in dancing, high-contrast pink neon strips.",
                "Sedotan Plastik": "A gigantic, large-scale 1-meter standalone mosque model constructed from thousands of colorful, interlocking plastic straws. The building features a unique tubular, honeycomb-like texture. Intricate Kufic-style calligraphy is formed by the tips of the straws. The colossal main dome pulses with a 'Cyber-Fiber' LED scheme (neon cyan, bright violet, and silver-white) flowing through the straws like data cables. Every minaret is wrapped in rapidly pulsing ice-white fairy lights, with entrance arches outlined in vibrant teal RGB neon tubing.",
                "Kabel": "A monumental, large-scale 1-meter standalone mosque object built from miles of tangled, colorful recycled copper wires and black rubber cables. The architecture looks like a high-tech machine with intricate Diwani-style calligraphy formed by gold-plated wire paths. The colossal main dome features a 'Matrix Pulse' LED scheme (electric green, bright orange, and deep purple) following the wire patterns. Every pillar is wrapped in intensely flickering emerald-green fairy lights, with entrance arches framed by intense copper-colored neon strips.",
                "Ban Bekas": "A colossal, large-scale 1-meter standalone mosque object made from thousands of shredded and carved recycled black tires. The architecture is heavy and industrial with deep, rugged textures and Naskh-style calligraphy carved directly into the thick rubber treads. The colossal main dome glows with a 'Volcanic Ember' LED scheme (lava red, burning amber, and dark violet) glowing through the deep carvings. Every minaret is a stack of carved rubber rings wrapped in flickering warm-red fairy lights and framed by intense, steady warm-white neon strips.",
                "Kancing Baju": "A monumental, large-scale 1-meter standalone mosque object built from millions of multi-colored plastic and pearl buttons of various sizes. The architecture features a dense, circular-patterned texture. Elegant Diwani-style calligraphy is formed by raised rows of tiny black buttons. The colossal main dome features a 'Prismatic Sewing' LED scheme (rainbow colors, magenta, and teal) glowing through the button holes. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense, saturated RGB neon tubing.",
                "Spons Cuci Piring": "A colossal, large-scale 1-meter standalone mosque object made from thousands of porous yellow and green recycled sponges. The architecture looks soft and cellular with a unique matte texture. Naskh-style calligraphy is carved deep into the sponge layers. The colossal main dome glows with a 'Bubble Glow' LED scheme (neon green, electric lemon, and soft cyan) creating a powerful internal light effect. Every minaret is a tall pillar of stacked sponges wrapped in flickering cyan fairy lights and framed by intense, steady neon-pink strips.",
                "Kulit Telur": "A gigantic, large-scale 1-meter standalone mosque model constructed from millions of tiny, fragile white and brown eggshell fragments. The structure has a delicate, cracked porcelain texture with intricate Kufic-style calligraphy formed by dark shell pieces. The colossal main dome pulses with a 'Golden Yolk' LED scheme (warm yellow, soft orange, and cream white) glowing through the thin shell layers. Every minaret is wrapped in rapidly pulsing amber fairy lights, with entrance arches outlined in vibrant gold RGB neon tubing.",
                "Sendok Garpu": "A monumental, large-scale 1-meter standalone mosque object built from thousands of polished stainless-steel spoons, forks, and knives. The architecture is a metallic mosaic with sharp, reflective surfaces. Intricate Thuluth-style calligraphy is etched into the spoon bowls. The colossal main dome glows with a 'Mercury Mirror' LED scheme (ice blue, bright silver, and violet) reflecting wildly off the steel. Tall minarets are crafted from stacked forks, wrapped in flickering cool-white fairy lights, with entrance arches outlined in pulsing cyan neon strips.",
                "Mur Baut": "A monumental, large-scale 1-meter standalone mosque object built from thousands of heavy, galvanized steel nuts, bolts, and washers. The architecture is rugged and industrial with a metallic honeycomb texture. Intricate Kufic-style calligraphy is formed by precisely aligned brass bolts. The colossal main dome glows with a 'Heavy Metal' LED scheme (deep violet, electric blue, and cold white) reflecting off the oily steel surfaces. Tall minarets are stacks of giant gears, wrapped in flickering cyan fairy lights, with entrance arches outlined in pulsing magenta neon strips.",
                "Sikat Cuci": "A gigantic, large-scale 1-meter standalone mosque model constructed from thousands of stiff nylon bristles from recycled scrubbing brushes. The structure looks feathery but sharp, with a unique linear texture. Intricate Thuluth-style calligraphy is carved into the wooden handles of the brushes. The colossal main dome pulses with a 'Fiber-Optic Glow' LED scheme (neon pink, bright turquoise, and lemon yellow) shining through the translucent bristles. Every minaret is a tall pillar of bristles wrapped in rapidly pulsing rainbow fairy lights, with entrance arches outlined in vibrant green RGB neon tubing.",
                "Korek Api": "A monumental, large-scale 1-meter standalone mosque object built from millions of used wooden matchsticks with colorful tips. The architecture features a dense, rhythmic wooden texture. Elegant Diwani-style calligraphy is formed by charred matchstick heads. The colossal main dome features a 'Burning Ember' LED scheme (fire red, charcoal orange, and sulfur yellow) glowing through the matchstick gaps. Every pillar is wrapped in intensely flickering warm-white fairy lights, with entrance arches framed by intense copper-colored neon strips.",
                "Keramik Pecah": "A colossal, large-scale 1-meter standalone mosque object made from thousands of jagged shards of recycled bathroom tiles and white porcelain toilets. The architecture is a sharp, glossy mosaic with Naskh-style calligraphy etched into the glazed surfaces. The colossal main dome features a 'Frozen Porcelain' LED scheme (ice blue, soft lilac, and bright silver) reflecting off the sharp ceramic edges. Every minaret is a stack of broken tiles wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "MPensil": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of sharpened and colored recycled pencils and pencil shavings. The architecture features a rhythmic wooden and multi-colored striped texture. Intricate Thuluth-style calligraphy is carved into the pencil wood bodies, glowing with a 'Pencil-Popsicle' LED scheme (lime green, bright orange, and cyan) seeping through the pencil gaps. Tall minarets are crafted from stacks of sharpened pencils, wrapped in flickering cool-white fairy lights, with entrance arches outlined in pulsing electric-blue neon strips.",
                "Pulpen": "A gigantic, large-scale 1-meter standalone mosque model constructed from thousands of glossy recycled plastic pen caps and pen bodies. The building is incredibly vibrant and translucent with a patchwork mosaic texture. Embossed Kufic-style calligraphy is formed by raised layers of colorful pen caps. The colossal main dome pulses with a 'Pop-Art' LED scheme (vibrant magenta, electric lime, and bright orange) reflecting off the metallic pen-clip inside. Every minaret is wrapped in rapidly pulsing rainbow fairy lights, with entrance arches outlined in intense neon-green tubing.",
                "Sabun": "A monumental, large-scale 1-meter standalone mosque object built from thousands of carved recycled white, pink, and blue soap bars. The architecture features a delicate, cracked porcelain texture with intricate Kufic-style calligraphy formed by dark soap pieces. The colossal main dome pulses with a 'Yolk-Yellow' LED scheme (warm yellow, soft orange, and cream white) glowing through the thin shell layers. Every minaret is wrapped in rapidly pulsing amber fairy lights, with entrance arches outlined in vibrant gold RGB neon tubing.",
                "Jerami & Koran": "A monumental, large-scale 1-meter standalone mosque object. The main body, walls, and minarets are built from millions of densely packed, raw golden rice straws (jerami), creating a thick, rustic texture. Embossed Kufic-style calligraphy made of charred straw adorns the walls. The colossal main dome is constructed entirely from thousands of crumpled and lacquered newspaper pages, glowing from within with a 'News-Flash' LED scheme (bright white, amber, and electric blue) seeping through the text-filled paper. Minarets are wrapped in flickering warm-white fairy lights, with entrance arches outlined in pulsing electric-blue neon strips.",
                "Kardus & Serabut Kelapa": "A gigantic, large-scale 1-meter standalone mosque model. The main structure and minarets are built from hundreds of layers of raw, corrugated brown cardboard, revealing its honeycomb texture, covered in laser-cut Thuluth-style calligraphy. The colossal main dome is covered entirely in a thick, feathery layer of brown coconut fiber (serabut kelapa), glowing from within with a 'Volcanic Ember' LED scheme (fire red, burning orange, and sulfur yellow) creating a powerful internal heat effect. Every pillar is wrapped in flickering warm-white fairy lights, with entrance arches framed by intense copper-colored neon strips.",
                "Tutup Botol & Sedotan": "A monumental, large-scale 1-meter standalone mosque object. The main body is constructed from millions of colorful recycled plastic bottle caps, creating a vibrant, pixelated mosaic with Diwani-style calligraphy formed by black caps. The colossal main dome is made of thousands of interlocking, translucent plastic straws, glowing with a 'Toxic Neon' LED scheme (lime green, electric yellow, and cyan) flowing through the straws like data cables. Tall minarets of stacked caps are wrapped in rapidly pulsing green fairy lights, with entrance arches outlined in vibrant orange RGB neon tubing.",
                "Koran Bekas & Ban": "A colossal, large-scale 1-meter standalone mosque object. The main structure and walls are built from millions of rolled grayscale newspaper strips with Naskh-style calligraphy carved through the paper layers. The colossal main dome is crafted from shredded and carved recycled black tire rubber, glowing with a 'Heavy Metal Matrix' LED scheme (neon green, bright white, and deep purple) seeping through the deep tire carvings. Tall minarets of paper tubes are wrapped in intensely flickering emerald-green fairy lights and framed by intense, steady warm-white neon strips.",
                "Daun Pisang & Bambu": "A monumental, large-scale 1-meter standalone mosque object. The main body, walls, and minarets are built from millions of vibrant green, fresh banana leaf pieces (daun pisang) and thick, brown textured banana trunks. Elegant Diwani-style calligraphy is intricately woven with dark bamboo threads into wide banana leaf bands, glowing with a 'Neon Mint' LED scheme (electric lime, soft mint, and bright white) pulsing through the leaf gaps. The colossal main dome is made of thousands of glossy, woven rattan strips, wrapped in flickering cool-white fairy lights, with entrance arches outlined in pulsing electric-blue neon strips.",
                "Kertas Majalah & Kardus": "A monumental, large-scale 1-meter standalone mosque object. The main body is constructed from thousands of shredded high-gloss fashion magazines. Elegant Diwani-style calligraphy is formed by raised layers of colorful paper pulp, glowing with a 'Industrial Hearth' LED scheme (fire red, deep orange, and warm tungsten yellow) creating a powerful internal glow. The colossal main dome is built from thousands of layers of corrugated brown cardboard and recycled paper pulp, wrapped in rapidly pulsing ice-white fairy lights, with entrance arches outlined in vibrant gold RGB neon tubing.",
                "Sabun & Keramik": "A colossal, large-scale 1-meter standalone mosque object. The main structure and walls are built from thousands of carved recycled white, pink, and blue soap bars. Intricate Kufic-style calligraphy is formed by dark soap pieces, glowing with a 'Prismatic Gloss' LED scheme (violet, hot pink, and sky blue) glowing through the glossy paper edges. The colossal main dome is made from thousands of jagged shards of recycled bathroom tiles and white porcelain toilets, wrapped in flickering cool-white fairy lights, with entrance arches outlined in pulsing electric-blue neon strips.",
                "Daun Pisang & Kaleng": "A monumental, large-scale 1-meter standalone mosque object. The main body and minarets are wrapped in millions of fresh, waxy green banana leaves with deep ribbing. The colossal main dome is built from thousands of crushed and polished silver aluminum cans, glowing from within with a 'Bio-Cyber' LED scheme (lime green, ice blue, and silver white) reflecting off the metallic dome. Intricate Thuluth-style calligraphy is embossed into the metal dome and carved into the leaf-covered walls. All arches are outlined in pulsing turquoise neon strips.",
                "Jerami & Botol Plastik": "A gigantic, large-scale 1-meter standalone mosque model. The structure is built from millions of golden-brown rice straws (jerami) bundled tightly. The colossal main dome is a sphere made of thousands of translucent recycled blue plastic bottle bases, glowing with a 'Deep Sea Gold' LED scheme (warm amber, ocean blue, and violet) shining through the plastic like a jewel. Elegant Kufic calligraphy is formed by dark brown seeds against the straw. Minarets are wrapped in flickering amber fairy lights, with entrance arches outlined in vibrant blue neon tubing.",
                "Kulit Kelapa & Kabel": "A monumental, large-scale 1-meter standalone mosque object. The main body is constructed from thousands of rough, dark-brown coconut shells (batok kelapa) with deep textures. The colossal main dome is made of thousands of tangled, colorful recycled copper wires and black cables, glowing with a 'Circuit Jungle' LED scheme (neon green, bright orange, and magenta) pulsing like electricity. Diwani-style calligraphy is formed by polished gold-plated wires on the shell surfaces. Every pillar is wrapped in intensely flickering emerald-green fairy lights.",
                "Koran & Ranting Kayu": "A colossal, large-scale 1-meter standalone mosque object. The main structure is built from millions of rolled grayscale newspaper strips. The colossal main dome is constructed from thousands of interlocking dry tree branches and twigs, glowing with an 'Ancient Future' LED scheme (fire red, charcoal violet, and soft white) creating a dramatic internal glow. Naskh-style calligraphy is laser-cut through the paper walls. Every minaret is a stack of paper tubes and twigs wrapped in flickering warm-red fairy lights and framed by intense teal neon strips.",
                "Melon & Strawberry": "A monumental, large-scale 1-meter standalone mosque object. The main body and minarets are built from millions of glossy cantaloupe melon pieces and translucent green rind blocks. The colossal main dome is constructed entirely from thousands of dense, vibrant red strawberry halves. Intricate Thuluth-style calligraphy is carved directly into the melon-flesh walls, glowing with a 'Ruby-Mint' LED scheme (lime green, bright red, and soft white) seeping through the fruit textures. All entrance arches are outlined in pulsing magenta neon strips.",
                "Semangka & Jeruk": "A gigantic, large-scale 1-meter standalone mosque model. The main structure is built from millions of vibrant red watermelon cubes and dark seeds. The colossal main dome is a sphere made of thousands of glossy orange wedges and translucent citrus rinds. Elegant Kufic calligraphy is formed by black watermelon seeds against the red flesh, glowing with a 'Tropical Fire' LED scheme (vibrant orange, deep red, and gold). Every minaret is wrapped in flickering amber fairy lights.",
                "Buah Naga & Kiwi": "A monumental, large-scale 1-meter standalone mosque object. The main body, walls, and minarets are built from millions of vibrant magenta dragonfruit rind slabs and polished white dragonfruit flesh with embedded black seeds. The colossal main dome is constructed entirely from thousands of interlocking, translucent green kiwi slices. Elegant Diwani-style calligraphy is intricately carved directly into wide bands of kiwi flesh, glowing with a 'Neon Emerald' LED scheme (lime green, cyan, and deep violet) seeping through the fruit textures. All entrance arches are outlined in pulsing electric-pink neon strips.",
                "Manggis & Rambutan": "A gigantic, large-scale 1-meter standalone mosque model. The main structure and minarets are built from rich, deep purple mangosteen rinds and snow-white mangosteen flesh segments. The entire facade is adorned with intricate, raised Kufic-style calligraphy formed by red rambutan skins and hairs against the purple walls. The colossal main dome is a sphere made of thousands of glossy, white rambutan flesh spheres, glowing from within with a 'Deep Royal' LED scheme (deep magenta, royal blue, and gold) reflecting off the juicy fruit. Minarets are wrapped in flickering warm-amber fairy lights, with entrance arches framed by intense gold RGB neon tubing.",
                "Nanas & Anggur": "A monumental, large-scale 1-meter standalone mosque object. The main body is constructed from thousands of glossy, geometric pineapple rind blocks and spiky leaves. The colossal main dome is a sphere made of densely packed, translucent green and purple grape halves. Elegant Diwani-style calligraphy is intricately carved into wide pineapple rind bands, glowing with a 'Sunset Gold' LED scheme (deep orange, warm gold, and royal purple) pulsing from the inside. Every pillar is wrapped in intensely flickering emerald-green fairy lights, with entrance arches framed by intense colorful RGB neon tubing.",
                "Alpukat & Leci": "A colossal, large-scale 1-meter standalone mosque object. The main structure and walls are built from millions of creamy green avocado flesh cubes and dark, pebbled avocado skin textures. The colossal main dome is made of thousands of translucent, white lychee flesh spheres. Elegant Kufic-style calligraphy is formed by polished, dark avocado seeds against the green walls, glowing with a 'Moonlight Quartz' LED scheme (ice blue, soft white, and pale lilac) glowing through the translucent lychee fruit. Minarets are wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Salak & Kelapa": "A monumental, large-scale 1-meter standalone mosque object. The main body and minarets are built from thousands of glossy, dark-brown snake-fruit (salak) scales, creating a natural armored-plate texture. The colossal main dome is a massive sphere made of polished white coconut meat (daging kelapa) segments. Intricate Thuluth-style calligraphy is carved directly into the white coconut dome, glowing with a 'Tropical Moonlight' LED scheme (ice blue, soft white, and deep violet) seeping through the carvings. All entrance arches are outlined in pulsing electric-blue neon strips.",
                "Durian & Nangka": "A gigantic, large-scale 1-meter standalone mosque model. The main structure and walls are built from thousands of sharp, golden durian thorns, giving it a grand and aggressive texture. The colossal main dome is constructed from thousands of glossy, yellow jackfruit (nangka) pods. Elegant Kufic-style calligraphy is formed by dark jackfruit seeds embedded into the walls, glowing with a 'Golden Magma' LED scheme (fire red, burning orange, and warm gold). Every minaret is wrapped in flickering amber fairy lights.",
                "Markisa & Delima": "A monumental, large-scale 1-meter standalone mosque object. The main body is built from millions of translucent orange passionfruit (markisa) pulp and crunchy black seeds. The colossal main dome is a sphere made of thousands of glistening, ruby-red pomegranate (delima) seeds. Elegant Diwani-style calligraphy is formed by patterns of pomegranate seeds, glowing with a 'Ruby Galaxy' LED scheme (vibrant magenta, deep red, and soft pink) shining through the pulp. Entrance arches are outlined in vibrant, dancing RGB neon tubing.",
                "Pepaya & Jambu Air": "A colossal, large-scale 1-meter standalone mosque object. The main structure is built from millions of vibrant orange papaya flesh cubes. The colossal main dome is constructed from thousands of translucent, bell-shaped pink water apples (jambu air). Elegant Naskh-style calligraphy is carved into the papaya walls, glowing with a 'Coral Sunset' LED scheme (warm peach, soft pink, and lime green) reflecting off the juicy textures. Minarets are wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Kardus & Botol Aqua": "A monumental, large-scale 1-meter standalone mosque object. The main body and minarets are built from hundreds of layers of raw, corrugated brown cardboard, revealing its honeycomb texture. The colossal main dome is constructed from thousands of interlocking clear recycled plastic Aqua water bottles with visible blue labels. Intricate Thuluth-style calligraphy is laser-cut through the cardboard walls, glowing with a 'Deep Sea Industrial' LED scheme (ice blue, amber, and silver-white) seeping through the gaps and bottles. Entrance arches are outlined in pulsing blue neon strips.",
                "Koran & Tutup Botol": "A gigantic, large-scale 1-meter standalone mosque model. The main structure is built from millions of rolled grayscale newspaper strips. The colossal main dome is a vibrant sphere made of thousands of colorful recycled plastic bottle caps. Elegant Diwani-style calligraphy is formed by raised rows of black caps against the newspaper-textured walls, glowing with a 'News-Pop' LED scheme (bright white, neon green, and magenta). Every minaret is wrapped in rapidly pulsing rainbow fairy lights.",
                "Beras Putih": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of polished white jasmine rice grains. The architecture features a seamless, pearlescent texture with intricate Thuluth-style calligraphy formed by slightly raised layers of the same rice grains. The colossal main dome glows with a 'Pure Moonlight' LED scheme (cool white, pale silver, and soft ice-blue) seeping through the microscopic gaps between the grains. Tall minarets are solid pillars of rice, wrapped in flickering cool-white fairy lights, with entrance arches outlined in pulsing electric-white neon strips.",
                "Ketan Hitam": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from millions of matte-black glutinous rice grains. The building has a dark, obsidian-like texture that absorbs light. Elegant Kufic-style calligraphy is carved deep into the black grain layers, glowing from within with a 'Deep Nebula' LED scheme (violet, magenta, and electric blue) creating a high-contrast cosmic effect. Every minaret is a tall pillar of black rice wrapped in rapidly pulsing purple fairy lights, with entrance arches outlined in vibrant blue neon tubing.",
                "Bunga Lawang": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of interlocking, star-shaped star anise (bunga lawang). The architecture is incredibly intricate with a natural woody, star-patterned texture. Elegant Diwani-style calligraphy is embossed using the tips of the star anise pods. The colossal main dome features a 'Mystic Amber' LED scheme (warm gold, deep orange, and amber) glowing through the thousands of star-shaped gaps. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense, steady warm-white neon strips.",
                "Kayu Manis": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of curled, textured cinnamon sticks (kayu manis). The architecture features a rhythmic, vertical tubular texture with a rich brown organic finish. Naskh-style calligraphy is carved directly into the bark of the large cinnamon sticks on the facade. The colossal main dome glows with a 'Hearth Fire' LED scheme (burning orange, crimson red, and soft gold) seeping through the cinnamon rolls. Every minaret is a stack of cinnamon tubes wrapped in flickering orange fairy lights and framed by intense copper-colored neon strips.",
                "Kacang Merah": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of glossy, deep-red kidney beans. The architecture features a smooth, organic pebble-like texture. Intricate Thuluth-style calligraphy is formed by raised layers of polished red beans. The colossal main dome glows with a 'Ruby Magma' LED scheme (vibrant red, deep crimson, and warm orange) seeping through the gaps between the beans. Tall minarets are solid pillars of red beans, wrapped in flickering amber fairy lights, with entrance arches outlined in pulsing scarlet neon strips.",
                "Kacang Hijau": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from millions of tiny, matte-green mung beans. The structure has a dense, fine-grained mossy texture. Elegant Kufic-style calligraphy is carved deep into the green bean layers, glowing from within with a 'Radioactive Emerald' LED scheme (neon green, lime, and bright cyan) creating an intense glowing effect. Every minaret is wrapped in rapidly pulsing green fairy lights, with entrance arches outlined in vibrant electric-green neon tubing.",
                "Kacang Kedelai": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of smooth, pale-yellow soybeans. The architecture features a clean, cream-colored minimalist texture. Elegant Diwani-style calligraphy is embossed using slightly darker roasted soybeans for contrast. The colossal main dome features a 'Golden Silk' LED scheme (warm yellow, soft gold, and white) glowing through the thousands of tiny bean gaps. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense, steady warm-white neon strips.",
                "Ketumbar": "A colossal, large-scale 1-meter standalone mosque object made entirely from millions of tiny, spherical coriander seeds (ketumbar). The architecture looks like it's covered in golden micro-beads with a high-detail grainy texture. Naskh-style calligraphy is intricately formed by the arrangement of the seeds. The colossal main dome glows with a 'Vintage Amber' LED scheme (deep amber, copper, and soft violet) seeping through the microscopic seed gaps. Every minaret is a stack of coriander beads wrapped in flickering warm-white fairy lights and framed by intense copper-colored neon strips.",
                "Cabe Merah": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of glossy, vibrant red chili peppers (cabe merah). The architecture features a sleek, rhythmic vertical texture from the curved shapes of the chilies. Intricate Thuluth-style calligraphy is formed by the green chili stems, glowing with a 'Crimson Inferno' LED scheme (deep red, fire orange, and bright white) seeping through the gaps. Tall minarets are bundles of long chilies wrapped in flickering red fairy lights, with entrance arches outlined in pulsing scarlet neon strips.",
                "Tomat": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of plump, glossy red cherry tomatoes. The structure has a bubbly, high-gloss 'organic pearl' texture. Elegant Kufic-style calligraphy is carved into the tomato skins, glowing from within with a 'Golden Pulp' LED scheme (warm orange, honey yellow, and soft red) creating a translucent glowing effect. Every minaret is a stack of tomatoes wrapped in rapidly pulsing amber fairy lights, with entrance arches outlined in vibrant gold neon tubing.",
                "Bawang Putih": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of white garlic bulbs and their papery skins. The architecture features a delicate, multi-layered ivory texture. Elegant Diwani-style calligraphy is embossed using the purple-streaked garlic cloves. The colossal main dome features a 'Moonlight Garlic' LED scheme (cool white, pale lilac, and soft silver) glowing through the translucent papery skins. Every pillar is wrapped in intensely flickering silver fairy lights, with entrance arches framed by intense white neon strips.",
                "Jagung": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of golden-yellow corn cobs and individual kernels. The architecture features a dense, geometric 'golden grid' texture. Naskh-style calligraphy is formed by rows of dark-purple corn kernels against the yellow background. The colossal main dome glows with a 'Solar Flare' LED scheme (bright yellow, electric orange, and warm amber) seeping through the kernels. Every minaret is a tall corn cob wrapped in flickering gold fairy lights and framed by intense teal neon tubing.",
                "Jahe": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of interlocking, gnarled ginger roots (jahe). The architecture features a rugged, tan-colored organic texture with complex natural joints. Intricate Thuluth-style calligraphy is carved deep into the fibrous ginger skin, glowing with a 'Mystic Earth' LED scheme (warm amber, soft orange, and deep violet) seeping through the carvings. Tall minarets are stacked ginger segments wrapped in flickering warm-white fairy lights, with entrance arches outlined in pulsing copper neon strips.",
                "Kunyit": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of polished turmeric roots (kunyit). The structure has a vibrant, deep-orange earthy texture. Elegant Kufic-style calligraphy is formed by scraping the skin to reveal the intense bright orange interior, glowing from within with a 'Solar Saffron' LED scheme (electric yellow, burning orange, and gold) creating a powerful radioactive glow. Every minaret is wrapped in rapidly pulsing gold fairy lights, with entrance arches outlined in vibrant orange neon tubing.",
                "Bawang Merah": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of glossy, purple-skinned shallots (bawang merah). The architecture features a layered, teardrop-shaped texture with a high-shine finish. Elegant Diwani-style calligraphy is embossed using the white inner layers of the shallots. The colossal main dome features a 'Amethyst Glow' LED scheme (deep magenta, royal purple, and soft pink) glowing through the translucent purple skins. Every pillar is wrapped in intensely flickering violet fairy lights, with entrance arches framed by intense magenta neon strips.",
                "Kemiri": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of hard, cream-colored candlenuts (kemiri). The architecture features a lumpy, stone-like ivory texture. Naskh-style calligraphy is intricately carved into the hard nuts. The colossal main dome glows with a 'Vanilla Moonlight' LED scheme (soft cream, pale gold, and ice white) creating a smooth, diffused glow from within the nut clusters. Every minaret is a stack of polished candlenuts wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Lego": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of interlocking plastic bricks. The architecture features a perfect voxelated, studded texture with sharp geometric precision. Intricate Kufic-style calligraphy is formed by precisely arranged 1x1 studs, glowing with a 'Cyber-Block' LED scheme (neon yellow, electric blue, and hot pink) pulsing through the brick seams. Tall minarets are tall towers of stacked bricks, wrapped in flickering multi-colored fairy lights, with entrance arches outlined in vibrant cyan neon strips.",
                "Kelereng": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of clear and cat-eye glass marbles (kelereng). The structure has a bubbly, crystalline, and highly refractive texture. Elegant Thuluth-style calligraphy is etched deep into the glass spheres, glowing from within with a 'Prism Galaxy' LED scheme (rainbow colors, deep violet, and bright silver) refracting through every marble. Every minaret is a stack of glass spheres wrapped in rapidly pulsing white-starlight fairy lights, with entrance arches outlined in vibrant purple neon tubing.",
                "Kartu Remi": "A monumental, large-scale 1-meter standalone mosque object built from thousands of glossy, laminated playing cards folded into complex 3D structures. The architecture features a sharp, layered, and paper-thin geometric texture. Elegant Diwani-style calligraphy is formed by laser-cut patterns on the card faces, glowing with a 'Royal Casino' LED scheme (velvet red, gold, and bright white) seeping through the card layers. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense scarlet neon strips.",
                "Balon": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of tiny, tightly twisted glossy latex balloons. The architecture features a soft, bulbous, and high-shine 'inflatable' texture. Naskh-style calligraphy is printed in metallic gold on the balloon surfaces. The colossal main dome glows with a 'Candy Glow' LED scheme (bubblegum pink, electric lime, and soft cyan) creating a diffused, translucent light effect. Every minaret is a tall twist of balloons wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Pipa Paralon": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of short-cut white PVC pipes of various diameters. The architecture features a unique 'tubular honeycomb' or 'bubble-wrap' geometric texture. Naskh-style calligraphy is formed by the empty circles of the pipe ends. The colossal main dome glows with a 'Toxic Neon' LED scheme (neon green, electric lemon, and soft cyan) creating a powerful internal light effect through the tubes. Every minaret is a tall bundle of pipes wrapped in flickering green fairy lights and framed by intense teal neon tubing.",
                "Rubik Cube": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of interlocked Rubik's cubes. The architecture features a voxelated, colorful, and glossy grid texture. Complex Kufic-style calligraphy is formed by precisely twisting the cubes to create patterns on the facade, glowing with a 'Retro-Arcade' LED scheme (neon pink, cyan, yellow, and magenta) pulsing through the cube seams. Tall minarets are stacked 2x2 Rubik's cubes wrapped in flickering multi-colored fairy lights, with entrance arches outlined in pulsing electric-blue neon strips.",
                "Hot Wheels": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of glossy, metallic-diecast toy cars. The structure has a chaotic but shimmering patchwork mosaic texture of paint and metal. Elegant Thuluth-style calligraphy is formed by precisely aligning rare-color cars against the body, glowing from within with a 'Mercury Mirror' LED scheme (ice blue, bright silver, and neon violet) reflecting wildly off the car bodies. Every minaret is a stack of vertical sports cars wrapped in rapidly pulsing cool-white fairy lights, with entrance arches outlined in vibrant gold neon tubing.",
                "Dadu": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of white dice with black pips. The architecture features a dense, rhythmic pattern of black dots on an ivory-white matte texture. Elegant Diwani-style calligraphy is formed by patterns of the dice pips, glowing with a 'Lucky 7' LED scheme (velvet red, deep black, and amber) shining through the pips. Every pillar is wrapped in intensely flickering warm-white fairy lights, with entrance arches framed by intense copper neon strips.",
                "Kartu Pokemon": "A colossal, large-scale 1-meter standalone mosque object made from thousands of glossy, holographic Pokémon cards. The architecture features a sharp, layered, and iridescent paper texture that flashes with rainbows. Naskh-style calligraphy is laser-cut through the card layers, revealing the internal light. The colossal main dome glows with a 'Prism Galaxy' LED scheme (vibrant rainbow colors, electric lime, and hot pink) refracting through the holographic surfaces. Every minaret is a twist of cards wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Tamiya": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of unassembled and assembled plastic 4WD model car parts (Tamiya). The architecture features a hyper-detailed mechanical texture of gears, chassis, and rollers. Intricate Thuluth-style calligraphy is formed by precisely aligned gold-plated motor gears, glowing with a 'Nitro-Electric' LED scheme (neon blue, bright white, and racing orange) pulsing through the mechanical gaps. Tall minarets are stacks of colorful plastic wheels, wrapped in flickering cyan fairy lights, with entrance arches outlined in pulsing electric-blue neon strips.",
                "Puzzle": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from millions of interlocking jigsaw puzzle pieces. The structure has a fragmented, organic mosaic texture with a slightly matte finish. Elegant Kufic-style calligraphy is formed by removing specific pieces to reveal the internal light, glowing with a 'Prismatic Logic' LED scheme (violet, magenta, and cyan) shining through the gaps. Every minaret is a tall pillar of vertical puzzle layers wrapped in rapidly pulsing white-starlight fairy lights, with entrance arches outlined in vibrant gold neon tubing.",
                "Shuttlecock": "A monumental, large-scale 1-meter standalone mosque object built from thousands of white feathered badminton shuttlecocks. The architecture features a soft, feathery, and rhythmic linear texture. Elegant Diwani-style calligraphy is formed by the dark cork bases of the shuttlecocks against the white feathers, glowing with a 'Cloud Sanctuary' LED scheme (soft lavender, ice blue, and pearl white) diffusing through the feathers. Every pillar is wrapped in intensely flickering silver fairy lights, with entrance arches framed by intense teal neon strips.",
                "Beyblade": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of metallic and plastic spinning tops (Beyblades). The architecture features a heavy, layered circular texture with sharp metallic edges. Naskh-style calligraphy is etched into the central 'Bit-Chips' of the Beyblades. The colossal main dome glows with a 'Galaxy Spin' LED scheme (deep purple, electric green, and silver) reflecting off the spinning metal discs. Every minaret is a stack of metallic attack-rings wrapped in flickering emerald-green fairy lights and framed by intense magenta neon strips.",
                "Kancing Mutiara": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of iridescent mother-of-pearl buttons. The architecture features a shimmering, high-gloss pearlescent texture. Intricate Thuluth-style calligraphy is formed by raised layers of tiny black pearl buttons, glowing with a 'Royal Moonlight' LED scheme (soft white, pale violet, and silver) refracting through the pearl surfaces. Tall minarets are stacked pillars of buttons, wrapped in flickering white-starlight fairy lights, with entrance arches outlined in pulsing electric-purple neon strips.",
                "Kancing Kayu": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of rustic brown wooden buttons of various sizes. The structure has a warm, organic, and matte-textured finish. Elegant Kufic-style calligraphy is carved deep into the wooden buttons, glowing from within with a 'Hearth Fire' LED scheme (burning orange, deep amber, and soft red) seeping through the button holes. Every minaret is a tall stack of large wooden discs wrapped in rapidly pulsing amber fairy lights, with entrance arches outlined in vibrant copper neon tubing.",
                "Kancing Warna-Warni": "A monumental, large-scale 1-meter standalone mosque object built from millions of vibrant, multi-colored plastic buttons arranged in a complex color-gradient mosaic. The architecture features a dense, playful, and high-contrast texture. Elegant Diwani-style calligraphy is formed by rows of glossy black buttons against the colorful background, glowing with a 'Neon Carnival' LED scheme (vibrant magenta, lime green, and electric blue) pulsing through every button hole. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense colorful RGB neon tubing.",
                "Kancing Logam": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of polished gold and silver metal blazer buttons with embossed crests. The architecture features a heavy, metallic, and royal texture. Naskh-style calligraphy is formed by the arrangement of the silver buttons against a gold-button facade. The colossal main dome glows with a 'Mercury Gold' LED scheme (bright gold, ice white, and warm amber) reflecting wildly off the metallic surfaces. Every minaret is a stack of gold buttons wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Peniti Warna-Warni": "A colossal, large-scale 1-meter standalone mosque object made from millions of colorful enamel-coated safety pins (neon pink, lime green, electric blue). The architecture features a vibrant, high-contrast 'punk-rock' mosaic texture. Naskh-style calligraphy is formed by rows of black pins against the colorful background. The colossal main dome glows with a 'Cyber-Pop' LED scheme (vibrant magenta, bright yellow, and cyan) pulsing through the pin gaps. Every minaret is wrapped in flickering multi-colored fairy lights and framed by intense teal neon strips.",
                "Peniti Berkarat": "A monumental, large-scale 1-meter standalone mosque object built from millions of oxidized, rusty iron safety pins for a raw industrial look. The architecture features a dark brown, gritty, and sharp 'Post-Apocalyptic' texture. Elegant Diwani-style calligraphy is formed by new, shiny brass pins for a high-contrast effect. The colossal main dome glows with a 'Volcanic Ember' LED scheme (fire red, burning orange, and sulfur yellow) glowing through the rusty pin layers. Every pillar is wrapped in intensely flickering orange fairy lights.",
                "Lidi Kelapa": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from millions of light-tan coconut leaf ribs (lidi kelapa). The structure has a raw, straw-like, and highly detailed organic texture. Elegant Kufic-style calligraphy is formed by charred lidi tips against the pale background, glowing from within with a 'Solar Flare' LED scheme (bright yellow, electric orange, and warm white) creating a powerful internal glow through the ribbed walls. Every minaret is wrapped in rapidly pulsing gold fairy lights, with entrance arches outlined in vibrant gold neon tubing.",
                "Lidi Aren": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of dark-brown, polished palm fiber sticks (lidi aren). The architecture features a dense, vertical linear texture. Intricate Thuluth-style calligraphy is formed by weaving lighter-colored bamboo splints into the lidi walls, glowing with a 'Mystic Amber' LED scheme (deep orange, warm gold, and soft red) seeping through the thousands of thin vertical gaps. Tall minarets are bundles of lidi wrapped in flickering amber fairy lights, with entrance arches outlined in pulsing copper neon strips.",
                "Lidi Bakar": "A colossal, large-scale 1-meter standalone mosque object made entirely from millions of charred, blackened lidi sticks with burnt tips. The architecture features a dark, carbonized, and sharp 'monolithic' texture. Naskh-style calligraphy is carved to reveal the inner light wood color of the sticks. The colossal main dome glows with a 'Volcanic Ember' LED scheme (fire red, deep orange, and sulfur yellow) glowing intensely through the charcoal-like gaps. Every minaret is a bundle of burnt lidi wrapped in flickering red fairy lights and framed by intense teal neon strips.",
                "Stik Eskrim": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of raw, natural-wood ice cream sticks. The structure has a rustic, layered, and interlocking 'woven' texture with sharp geometric edges. Elegant Kufic-style calligraphy is carved deep into the wooden sticks, glowing from within with a 'Deep Amber Hearth' LED scheme (warm gold, deep orange, and soft amber) seeping through the thousands of vertical gaps. Every minaret is a tall stack of interlocking sticks wrapped in rapidly pulsing gold fairy lights, with entrance arches outlined in vibrant copper neon tubing.",
                "Pecahan Keramik": "A monumental, large-scale 1-meter standalone mosque object built from thousands of jagged, iridescent glazed ceramic tile shards arranged in a dense, multi-colored mosaic. The architecture features a sharp, shattered, and highly reflective texture like a broken rainbow mirror. Elegant Diwani-style calligraphy is formed by aligning glossy black ceramic shards against the colorful background, glowing with a 'Prism Galaxy' LED scheme (rainbow colors, deep violet, and electric silver) reflecting and refracting through every jagged edge. Entrance arches are outlined in vibrant colorful RGB neon tubing.",
                "Pecahan Keramik Putih": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of pure white porcelain and china shards. The architecture features a sharply broken, brilliant white texture resembling a shattered iceberg. Naskh-style calligraphy is formed by outlining the shapes of the white shards with gold-leaf gaps. The colossal main dome glows with a 'Moonlight Quartz' LED scheme (ice blue, soft white, and pale silver) creating a smooth, diffused glow refracted through the ceramic shards. Every minaret is a stack of white porcelain shards wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Donat Glazed": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of glossy, sugar-glazed donuts. The architecture features a bubbly, rounded, and high-shine organic texture. Intricate Thuluth-style calligraphy is formed by vibrant multi-colored chocolate sprinkles (meses) on the donut surfaces, glowing with a 'Candy Rush' LED scheme (bubblegum pink, electric violet, and bright gold) reflecting off the sugar glaze. Tall minarets are stacks of donuts wrapped in flickering magenta fairy lights, with entrance arches outlined in pulsing neon-pink strips.",
                "Roti Tawar": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of soft, white bread slices. The structure has a porous, spongy, and matte-white texture. Elegant Kufic-style calligraphy is scorched directly onto the bread surfaces (toast effect), glowing from within with a 'Golden Toasted' LED scheme (warm amber, honey yellow, and soft orange) seeping through the bread's airy pores. Every minaret is a tall stack of bread slices wrapped in rapidly pulsing gold fairy lights, with entrance arches outlined in vibrant copper neon tubing.",
                "Croissant": "A monumental, large-scale 1-meter standalone mosque object built from thousands of flaky, golden-brown buttery croissants. The architecture features a highly layered, crispy, and spiral-curved texture. Elegant Diwani-style calligraphy is formed by patterns of powdered sugar dusted over the flaky layers, glowing with a 'Butter Gold' LED scheme (bright gold, warm tungsten, and soft cream) pulsing from the gaps between the pastry layers. Every pillar is wrapped in intensely flickering warm-white fairy lights, with entrance arches framed by intense gold neon strips.",
                "Biskuit Crackers": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of rectangular golden-brown crackers with visible pin-holes. The architecture features a crisp, geometric, and perforated grid texture. Naskh-style calligraphy is formed by the arrangement of the cracker holes, glowing with a 'Solar Biscuit' LED scheme (electric orange, amber, and pale yellow) shining through the thousands of tiny holes. Every minaret is a square stack of crackers wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Bungkus Indomie": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of shiny, crinkled plastic Indomie instant noodle wrappers. The architecture features a vibrant patchwork of red, yellow, and white plastic textures with high-gloss reflections. Intricate Thuluth-style calligraphy is formed by precisely aligning the 'Indomie' logos, glowing with a 'Microwave Neon' LED scheme (bright red, electric yellow, and white) pulsing through the plastic folds. Tall minarets are cylinders of wrapped plastic, wrapped in flickering multi-colored fairy lights.",
                "Alumunium Foil": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of crumpled silver and gold alumunium foil wrappers from chocolate bars. The structure has a sharp, metallic, and highly faceted texture like a silver mountain. Elegant Kufic-style calligraphy is embossed directly into the foil, glowing from within with a 'Mercury Mirror' LED scheme (ice blue, bright silver, and violet) reflecting wildly off the crinkled metal. Every minaret is a stack of metallic foil wrapped in rapidly pulsing white fairy lights.",
                "Bungkus Keripik": "A monumental, large-scale 1-meter standalone mosque object built from thousands of turned-inside-out snack bags (silver interior). The architecture features a blindingly reflective, chrome-like silver texture. Elegant Diwani-style calligraphy is etched into the silver surface, glowing with a 'Cyber-Chrome' LED scheme (neon green, electric blue, and magenta) creating a high-tech metallic glow. Every pillar is wrapped in intensely flickering emerald-green fairy lights, with entrance arches framed by intense teal neon strips.",
                "Kertas Cokelat": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of oil-stained, crumpled brown fast-food paper bags. The architecture features a dark, translucent, and 'vintage-grunge' organic texture. Naskh-style calligraphy is laser-cut through the paper layers, revealing the internal light. The colossal main dome glows with a 'Golden Grease' LED scheme (warm amber, deep orange, and soft tungsten) shining through the oily paper. Every minaret is a tall roll of brown paper wrapped in flickering warm-white fairy lights.",
                "Sachet Kopi": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of interlocking colorful coffee sachets (maroon, gold, and black). The architecture features a dense, shingled texture like dragon scales. Intricate Thuluth-style calligraphy is formed by the brand logos on the sachets, glowing with a 'Caffeine Gold' LED scheme (deep amber, espresso brown, and bright gold) pulsing through the foil seams. Tall minarets are cylinders of tightly rolled sachets wrapped in flickering warm-white fairy lights, with entrance arches outlined in pulsing copper neon strips.",
                "Plastik Kresek": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of layered and melted colorful plastic grocery bags (kantong kresek). The structure has a soft, flowing, and semi-translucent 'drapery' texture with organic folds. Elegant Kufic-style calligraphy is melted into the plastic surface, glowing from within with a 'Toxic Rainbow' LED scheme (neon green, hot pink, and electric blue) shining through the translucent plastic layers. Every minaret is a tall twist of plastic wrapped in rapidly pulsing white fairy lights.",
                "Kaleng Soda": "A monumental, large-scale 1-meter standalone mosque object built from thousands of crushed and flattened aluminum soda cans. The architecture features a sharp, jagged, and highly metallic patchwork texture. Elegant Diwani-style calligraphy is embossed using the colorful pull-tabs of the cans, glowing with a 'Fizzy Silver' LED scheme (bright silver, ice blue, and crimson red) reflecting wildly off the metallic shards. Every pillar is wrapped in intensely flickering silver fairy lights, with entrance arches framed by intense scarlet neon strips.",
                "Bungkus Permen": "A colossal, large-scale 1-meter standalone mosque object made entirely from millions of tiny, transparent and metallic candy wrappers. The architecture features a sparkling, 'jewel-box' texture with thousands of small reflections. Naskh-style calligraphy is formed by the colorful patterns of the wrappers, glowing with a 'Sugar Prism' LED scheme (rainbow colors, soft violet, and bright yellow) refracting through the clear plastic. Every minaret is a stack of candy-wrap spheres wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Bungkus Taro": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of glossy, purple 'Taro' snack wrappers. The architecture features a vibrant deep-purple plastic texture with high-gloss reflections. Intricate Thuluth-style calligraphy is formed by the silver interior of the wrappers, glowing with a 'Deep Amethyst' LED scheme (neon purple, electric blue, and bright silver) pulsing through the plastic folds. Tall minarets are cylinders of wrapped purple foil wrapped in flickering violet fairy lights, with entrance arches outlined in pulsing cyan neon strips.",
                "Bungkus Chiki": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of bright yellow 'Chiki Balls' wrappers. The structure has a saturated, sunny-yellow texture with high-reflectivity. Elegant Kufic-style calligraphy is formed by aligning the iconic Chiki mascot patterns, glowing from within with a 'Solar Flare' LED scheme (bright yellow, electric orange, and warm white) creating a powerful internal glow. Every minaret is a tall pillar of yellow foil wrapped in rapidly pulsing gold fairy lights, with entrance arches outlined in vibrant gold neon tubing.",
                "Bungkus Cheetos": "A monumental, large-scale 1-meter standalone mosque object built from thousands of vibrant orange and red 'Cheetos' wrappers. The architecture features a fiery, high-contrast patchwork texture. Elegant Diwani-style calligraphy is etched using the silver foil side of the packaging, glowing with a 'Flaming Ember' LED scheme (fire red, burning orange, and sulfur yellow) reflecting wildly off the crinkled metallic surfaces. Every pillar is wrapped in intensely flickering orange fairy lights, with entrance arches framed by intense scarlet neon strips.",
                "Bungkus Chitato": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of dark-blue and silver 'Chitato' potato chip bags. The architecture features a deep-colored, premium metallic plastic texture. Naskh-style calligraphy is formed by laser-cut patterns through the dark blue plastic to reveal the internal light. The colossal main dome glows with a 'Sapphire Spark' LED scheme (deep ocean blue, ice silver, and soft white) refracting through the metallic layers. Every minaret is wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Umbul": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of colorful vintage 'Gambar Umbul' paper cards (mainan jadul). The architecture features a vibrant, dense, and slightly glossy patchwork texture of mismatched retro characters (superheroes, anime, movie scenes). Elegant Thuluth-style calligraphy is formed by precisely aligning the card borders, glowing with a 'Retro Pixel' LED scheme (neon pink, bright yellow, and cyan) pulsing through the paper seams. Tall minarets are stacked cylinders of cards wrapped in flickering multi-colored fairy lights, with entrance arches outlined in pulsing cyan neon strips.",
                "Umbul Hologram": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of special-edition 'Gambar Umbul' cards with holographic and iridescent finishes. The architecture features a hyper-reflective, prism-like texture that flashes rainbows. Naskh-style calligraphy is laser-cut through the cards, revealing the internal light. The colossal main dome glows with a 'Sugar Prism' LED scheme (rainbow colors, soft violet, and bright yellow) refracting through the holographic surfaces. Every minaret is a stack of holographic cards wrapped in flickering silver fairy lights.",
                "Platinum Berlian": "A monumental, large-scale 1-meter standalone mosque object built entirely from polished solid platinum blocks. The architecture features a heavy, cool-toned silver-metallic texture with mirror-finish surfaces. Intricate Thuluth-style calligraphy is inlaid with millions of micro-cut black diamonds, glowing with a 'Starlight Void' LED scheme (ice blue, deep violet, and silver white) reflecting off the metallic body. Tall minarets are solid platinum pillars wrapped in flickering cool-white fairy lights, with entrance arches outlined in pulsing electric-blue neon strips.",
                "Kristal Safir": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of faceted Swarovski crystals and deep-blue sapphires. The structure has a hyper-reflective, transparent, and prismatic texture. Elegant Kufic-style calligraphy is formed by internal laser-etching inside the sapphire stones, glowing from within with a 'Deep Ocean Prism' LED scheme (vibrant blue, bright cyan, and silver) refracting through every facet. Every minaret is a stack of giant crystals wrapped in rapidly pulsing white-starlight fairy lights, with entrance arches outlined in vibrant purple neon tubing.",
                "Emas Merah": "A monumental, large-scale 1-meter standalone mosque object built from polished 18K rose gold and thousands of glowing red rubies. The architecture features a warm, pinkish-gold metallic texture with a high-gloss finish. Elegant Diwani-style calligraphy is formed by raised layers of blood-red rubies, glowing with a 'Royal Hearth' LED scheme (vibrant red, warm amber, and rose-gold spark) pulsing through the precious stones. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense magenta neon strips.",
                "Gading Putih": "A colossal, large-scale 1-meter standalone mosque object made from polished ivory-textured marble and intricate 24K gold filigree wire-work. The architecture features a smooth, cream-colored base covered in complex, lace-like golden patterns. Naskh-style calligraphy is formed by woven gold threads, glowing with a 'Champagne Solar' LED scheme (warm gold, pale cream, and soft tungsten) creating a majestic, diffused glow. Every minaret is a masterpiece of gold wire-work wrapped in flickering silver fairy lights and framed by intense warm-white neon strips.",
                "Ukiran Jati": "A monumental, large-scale 1-meter standalone mosque object crafted from deep dark-brown aged teak wood. The entire facade is covered in intricate, deep-relief floral 'Jepara-style' carvings and complex Thuluth-style calligraphy. The colossal main dome is made of solid, mirror-polished 24K gold, glowing with a 'Solar Royalty' LED scheme (warm gold, deep amber, and white-hot spark) reflecting off the gold. Tall minarets are carved wood pillars with gold-plated balconies wrapped in flickering golden fairy lights, with entrance arches outlined in pulsing champagne-gold neon strips.",
                "Kayu Hitam": "A gigantic, large-scale 1-meter standalone mosque model built from jet-black Ebony wood with a high-gloss polished finish. Elegant Kufic-style calligraphy is inlaid with white-gold (platinum) filigree along the walls. The colossal main dome is a sphere of brushed white gold, glowing from within with a 'Moonlight Silver' LED scheme (ice blue, pale silver, and bright white) reflecting off the dark wood. Every minaret is a masterpiece of dark wood carving wrapped in rapidly pulsing white-starlight fairy lights, with entrance arches outlined in vibrant purple neon tubing.",
                "Kayu Gaharu": "A monumental, large-scale 1-meter standalone mosque object made from rare, textured agarwood (gaharu). The architecture features a rugged, organic wood texture with deep-etched Diwani-style calligraphy filled with liquid gold. The colossal main dome is a massive dome of hammered gold leaf, glowing with a 'Mystic Amber' LED scheme (vibrant orange, warm gold, and royal purple) seeping through the wood grains. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense warm-white neon strips.",
                "Kayu Cendana": "A colossal, large-scale 1-meter standalone mosque object carved from aromatic sandalwood (cendana) with a pale-tan matte texture. The architecture is covered in a delicate mesh of 22K gold filigree ukiran. Naskh-style calligraphy is embossed in solid gold on the wood facade. The colossal main dome is a brilliant gold-lattice structure glowing with a 'Champagne Glow' LED scheme (soft cream, pale gold, and warm tungsten). Every minaret is a stack of carved sandalwood cylinders wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Giok Hijau": "A monumental, large-scale 1-meter standalone mosque object carved from deep imperial green jade (giok). The architecture features a smooth, translucent stone texture with natural veins. Intricate Thuluth-style calligraphy is inlaid with rare black South Sea pearls, glowing with an 'Emerald Moonlight' LED scheme (mint green, soft teal, and pale silver) shining through the jade body. Tall minarets are solid jade pillars wrapped in flickering silver fairy lights, with entrance arches outlined in pulsing electric-purple neon strips.",
                "Mutiara Putih": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from millions of iridescent white pearls and polished white jade. The structure has a shimmering, creamy, and high-gloss 'organic pearl' texture. Elegant Kufic-style calligraphy is embossed using tiny golden pearls, glowing from within with a 'Champagne Mist' LED scheme (pale gold, soft cream, and ice white) refracting through the pearl layers. Every minaret is a stack of giant pearls wrapped in rapidly pulsing white-starlight fairy lights, with entrance arches outlined in vibrant gold neon tubing.",
                "Giok Merah": "A monumental, large-scale 1-meter standalone mosque object built from rare red jade and inlaid with golden South Sea pearls. The architecture features a warm, translucent crimson texture. Elegant Diwani-style calligraphy is formed by rows of perfectly round gold pearls, glowing with a 'Royal Ember' LED scheme (vibrant red, warm amber, and honey yellow) pulsing from the heart of the jade. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense scarlet neon strips.",
                "Mosaik Giok": "A colossal, large-scale 1-meter standalone mosque object made from a complex mosaic of various jade shades (lavender, green, white) and iridescent abalone pearl shells. The architecture features a sharp, shattered, and multi-colored gemstone texture. Naskh-style calligraphy is laser-etched into the abalone surfaces. The colossal main dome glows with a 'Prism Sanctuary' LED scheme (rainbow colors, soft violet, and bright silver) refracting through the translucent stones and shells. Every minaret is wrapped in flickering silver fairy lights and framed by intense teal neon tubing.",
                "Batu Zamrud": "A monumental, large-scale 1-meter standalone mosque object carved from a single colossal deep-green emerald crystal. The architecture features sharp crystalline facets and natural internal 'jardin' inclusions. Intricate Thuluth-style calligraphy is etched deep and filled with liquid platinum, glowing with a 'Verdan Sanctuary' LED scheme (intense neon green, forest emerald, and bright silver) refracting through the translucent green stone. Tall minarets are faceted crystal pillars wrapped in flickering silver fairy lights, with entrance arches outlined in pulsing teal neon strips.",
                "Batu Safir Biru": "A gigantic, large-scale 1-meter standalone mosque model constructed from thousands of royal blue sapphires. The structure has a deep, velvety blue crystalline texture. Elegant Kufic-style calligraphy is formed by white diamonds inlaid into the sapphire walls, glowing from within with a 'Deep Ocean Prism' LED scheme (vibrant sapphire blue, electric cyan, and ice white) shattering light into thousands of blue rays. Every minaret is a stack of raw sapphire crystals wrapped in rapidly pulsing white-starlight fairy lights, with entrance arches outlined in vibrant gold neon tubing.",
                "Batu Kecubung": "A monumental, large-scale 1-meter standalone mosque object built from massive purple amethyst geodes with exposed raw crystals inside. The architecture features a rugged exterior and a sparkling, jagged violet interior. Elegant Diwani-style calligraphy is laser-carved into the crystal points, glowing with an 'Amethyst Galaxy' LED scheme (deep purple, magenta, and soft lilac) pulsing from the heart of the geode. Every pillar is a cluster of purple crystals wrapped in intensely flickering violet fairy lights, with entrance arches framed by intense magenta neon strips.",
                "Berlian Pink": "A colossal, large-scale 1-meter standalone mosque object made entirely from rare pink diamonds set in a delicate white-gold (platinum) frame. The architecture features a hyper-reflective, soft-pink crystalline texture. Naskh-style calligraphy is formed by rows of tiny white diamonds, glowing with a 'Rose Aurora' LED scheme (soft pink, champagne, and bright silver) creating a blindingly beautiful shimmer. Every minaret is a masterpiece of diamond-setting wrapped in flickering silver fairy lights and framed by intense warm-white neon strips.",
                "Bulu Merak": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of vibrant peacock feathers. The architecture features a soft, iridescent, and feathery texture dominated by the 'eye' patterns of the feathers. Intricate Thuluth-style calligraphy is formed by the deep-blue quill fibers, glowing with a 'Peacock Nebula' LED scheme (electric lime, deep violet, and shimmering teal) seeping through the soft barbs. Tall minarets are bundles of long feathers wrapped in flickering emerald fairy lights, with entrance arches outlined in pulsing magenta neon strips.",
                "Sisik Ikan": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of large, metallic-pearlized scales of a Super Red Arowana fish. The structure has a heavy, layered, and high-gloss 'dragon scale' texture. Elegant Kufic-style calligraphy is etched into the scales, glowing from within with a 'Crimson Pearl' LED scheme (fire red, soft pink, and bright silver) reflecting off the iridescent surfaces. Every minaret is a stack of scales wrapped in rapidly pulsing red fairy lights, with entrance arches outlined in vibrant gold neon tubing.",
                "Cangkang Kerang": "A monumental, large-scale 1-meter standalone mosque object built from thousands of rough-textured oyster shells with polished nacre interiors. The architecture features a contrast between rugged gray exteriors and shimmering rainbow interiors. Elegant Diwani-style calligraphy is carved to reveal the pearlescent inner layers, glowing with a 'Moonlight Nacre' LED scheme (pale violet, ice blue, and soft cream) refracting through the calcium layers. Every pillar is wrapped in intensely flickering silver fairy lights, with entrance arches framed by intense teal neon tubing.",
                "Sarang Lebah": "A colossal, large-scale 1-meter standalone mosque object made entirely from golden-yellow natural beeswax and hexagonal honeycomb structures. The architecture features a perfect geometric grid texture with a translucent, waxy finish. Naskh-style calligraphy is formed by filling specific hexagonal cells with dark forest honey. The colossal main dome glows with a 'Liquid Amber' LED scheme (bright honey yellow, deep orange, and warm gold) shining through the translucent wax walls. Every minaret is a hexagonal tower wrapped in flickering gold fairy lights.",
                "Terumbu Karang": "A monumental, large-scale 1-meter standalone mosque object carved from a single massive block of white brain coral. The architecture features an incredibly complex, labyrinthine organic groove texture. Intricate Thuluth-style calligraphy is formed by the natural brain-like ridges of the coral, glowing with a 'Deep Sea Bio-Lume' LED scheme (soft cyan, electric lime, and ultraviolet) seeping through the deep grooves. Tall minarets are towers of porous coral wrapped in flickering turquoise fairy lights, with entrance arches outlined in pulsing neon-white strips.",
                "Fosil Kayu": "A colossal, large-scale 1-meter standalone mosque object made from polished slabs of millions-of-years-old petrified wood. The architecture features a unique stone-meets-wood texture with deep rings and mineralized grain patterns. Naskh-style calligraphy is formed by the natural agate and quartz veins inside the fossil. The colossal main dome glows with a 'Primal Earth' LED scheme (deep violet, emerald green, and golden brown) reflecting off the mirror-polished stone surface. Every minaret is a tall pillar of fossilized wood wrapped in flickering silver fairy lights.",
                "Kristal Garam": "A monumental, large-scale 1-meter standalone mosque object built from massive blocks of raw pink Himalayan salt crystals. The architecture features a jagged, crystalline, and semi-transparent texture with natural mineral veins. Elegant Diwani-style calligraphy is etched into the salt blocks, glowing from within with a 'Peach Sunset' LED scheme (warm orange, soft pink, and deep amber) creating a massive diffused glow throughout the structure. Every pillar is wrapped in intensely flickering orange fairy lights, with entrance arches framed by intense copper neon strips.",
                "Tanah Liat": "A monumental, large-scale 1-meter standalone mosque object sculpted from raw, burnt-orange terracotta clay. The architecture features a smooth but hand-crafted organic texture with visible thumbprints and sculpting marks. Intricate Thuluth-style calligraphy is carved deep into the wet clay before hardening, glowing with a 'Molten Core' LED scheme (fire red, deep orange, and warm amber) seeping through the cracks. Tall minarets are tapered clay pillars wrapped in flickering orange fairy lights, with entrance arches outlined in pulsing copper neon strips.",
                "Serbuk Kayu": "A gigantic, large-scale 1-meter standalone mosque model constructed from compressed millions of fine golden-brown sawdust particles. The structure has a soft, fuzzy, and highly textured matte finish. Elegant Kufic-style calligraphy is formed by burning the sawdust surface (pyrography), glowing from within with a 'Golden Dust' LED scheme (honey yellow, soft gold, and warm white) shining through the porous compressed particles. Every minaret is a tall cylinder of pressed wood-dust wrapped in rapidly pulsing amber fairy lights.",
                "Pasir Pantai": "A monumental, large-scale 1-meter standalone mosque object built from millions of glistening, wet golden sand grains. The architecture features a dripping, 'melted' sandcastle texture with incredible granular detail. Elegant Diwani-style calligraphy is traced into the sand, glowing with a 'Coastal Glow' LED scheme (bright gold, pale cyan, and white) reflecting off the tiny quartz crystals in the sand. Every pillar is a stack of dripping sand wrapped in intensely flickering silver fairy lights, with entrance arches framed by intense teal neon strips.",
                "Batu Bata": "A colossal, large-scale 1-meter standalone mosque object made entirely from thousands of miniature, weathered red bricks and grey mortar. The architecture features a rough, geometric, and industrial-heritage texture. Naskh-style calligraphy is formed by protruding bricks, glowing with a 'Vintage Alley' LED scheme (soft red, warm tungsten, and amber) seeping through the mortar gaps. Every minaret is a tall brick tower wrapped in flickering warm-white fairy lights and framed by intense scarlet neon strips.",
                "Arang Kayu": "A monumental, large-scale 1-meter standalone mosque object built entirely from thousands of jagged, matte-black charred wood chunks. The architecture features a deep, carbonized, and highly porous texture. Intricate Thuluth-style calligraphy is carved to reveal the glowing core, featuring a 'Volcanic Ember' LED scheme (intense fire red, burning orange, and sulfur yellow) pulsing from within the black charcoal gaps. Tall minarets are stacks of burnt wood wrapped in flickering red fairy lights, with entrance arches outlined in pulsing copper neon strips.",
                "Batu Apung": "A gigantic, large-scale 1-meter standalone mosque model constructed from thousands of light-grey, highly aerated volcanic pumice stones. The structure has a sponge-like, rough, and perforated texture. Elegant Kufic-style calligraphy is formed by the natural holes in the stone, glowing from within with a 'Deep Sea Bio-Lume' LED scheme (soft cyan, electric lime, and ice white) shining through the thousands of tiny stone pores. Every minaret is a tall porous pillar wrapped in rapidly pulsing white fairy lights.",
                "Serbuk Kopi": "A colossal, large-scale 1-meter standalone mosque object made entirely from compressed, dark-roast coffee grounds. The architecture features a grainy, rich dark-brown, and oily matte texture. Naskh-style calligraphy is formed by stenciling with fine white sugar crystals. The colossal main dome glows with a 'Caffeine Aurora' LED scheme (deep violet, espresso brown, and soft magenta) creating a moody, diffused glow through the coffee particles. Every minaret is a cylinder of pressed coffee wrapped in flickering silver fairy lights.",
                "Lumut & Batu Kali": "A monumental, large-scale 1-meter standalone mosque object built from smooth river stones covered in thick, vibrant green moss. The architecture features a soft, velvety green texture contrasted with cold grey stone. Elegant Diwani-style calligraphy is formed by trimming the moss to reveal the stone underneath, glowing with a 'Forest Sanctuary' LED scheme (emerald green, soft lime, and golden amber) pulsing from behind the moss layers. Every pillar is wrapped in intensely flickering gold fairy lights, with entrance arches framed by intense teal neon strips.",
                "Tanah Lempung": "A gigantic, large-scale 1-meter standalone mosque model sculpted from grey river clay with a 'crackle-glaze' dried texture. The structure features millions of tiny, intricate fissures across the entire surface. Elegant Kufic-style calligraphy is formed by the deep cracks themselves, glowing from within with a 'Deep Magma' LED scheme (blood red, dark orange, and amber) seeping through the thousands of tiny mud gaps. Every minaret is a column of dried mud wrapped in rapidly pulsing red fairy lights, with entrance arches outlined in vibrant gold neon tubing.",
                "Kristal Kuarsa": "A monumental, large-scale 1-meter standalone mosque object built from massive, jagged clusters of raw white quartz crystals. The architecture features a sharp, semi-translucent, and icy geometric texture. Intricate Thuluth-style calligraphy is formed by natural mineral inclusions (veins) inside the crystals, glowing with a 'Glacial Prism' LED scheme (ice blue, soft violet, and bright silver) refracting through the crystal body. Tall minarets are jagged crystal points wrapped in flickering cool-white fairy lights, with entrance arches outlined in pulsing cyan neon strips.",
                "Batu Obsidian Hitam": "A monumental, large-scale 1-meter standalone mosque object carved from massive blocks of volcanic obsidian glass. The architecture features a razor-sharp, mirror-polished jet-black texture with conchoidal fractures. Elegant Diwani-style calligraphy is etched into the glass surface, glowing with a 'Void Spectrum' LED scheme (deep magenta, neon purple, and electric blue) reflecting off the pitch-black glass. Every pillar is wrapped in intensely flickering violet fairy lights, with entrance arches framed by intense teal neon strips.",
                "Kapur Tulis": "A colossal, large-scale 1-meter standalone mosque object built entirely from thousands of white and pastel-colored sticks of chalk and compressed chalk dust. The architecture features a soft, dusty, and ultra-matte texture. Naskh-style calligraphy is 'sketched' onto the surface with vibrant colored chalk. The colossal main dome glows with a 'Pastel Nebula' LED scheme (soft pink, mint green, and pale yellow) creating a hazy, diffused glow through the chalk dust. Every minaret is a stack of chalk sticks wrapped in flickering silver fairy lights.",
                "Es Krim Cone": "A monumental, large-scale 1-meter standalone mosque object built from thousands of stacked crispy waffle cones and giant scoops of vanilla ice cream. The architecture features a criss-cross waffle texture at the base and a soft, billowy 'cloud-like' texture for the domes. Intricate Thuluth-style calligraphy is drizzled in chocolate syrup, glowing with a 'Vanilla Gold' LED scheme (warm cream, bright gold, and soft white) reflecting off the melting surface. Tall minarets are stacked waffle cones wrapped in flickering amber fairy lights.",
                "Es Krim Magnum": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of premium chocolate-coated ice cream bars. The structure has a sharp, cracked-chocolate shell texture. Elegant Kufic-style calligraphy is etched into the dark chocolate to reveal the white vanilla interior, glowing from within with a 'Royal Cocoa' LED scheme (deep amber, copper, and bright white) seeping through the cracks. Every minaret is a tall ice cream bar wrapped in rapidly pulsing gold fairy lights.",
                "Sorbet Pelangi": "A monumental, large-scale 1-meter standalone mosque object built from millions of tiny, vibrant scoops of fruit sorbet (lime, raspberry, orange). The architecture features a frosty, grainy, and multi-colored icy texture. Elegant Diwani-style calligraphy is formed by frozen berries, glowing with a 'Neon Frost' LED scheme (vibrant pink, lime green, and electric orange) refracting through the icy sorbet particles. Every pillar is wrapped in intensely flickering silver fairy lights, with entrance arches framed by intense teal neon strips.",
                "Es Krim Cornetto": "A colossal, large-scale 1-meter standalone mosque object made from thousands of spiral-swirled soft-serve ice cream mounds and chocolate discs. The architecture features a rhythmic, swirling creamy texture with high-gloss chocolate accents. Naskh-style calligraphy is formed by silver sugar pearls (sprinkles). The colossal main dome glows with a 'Frozen Galaxy' LED scheme (pale violet, ice blue, and soft magenta) creating a dreamy, diffused glow through the creamy texture. Every minaret is wrapped in flickering silver fairy lights.",
                "Donat Mini Pelangi": "A monumental, large-scale 1-meter standalone mosque object built entirely from millions of tiny mini-donuts with vibrant, multi-colored sugar glazes (pink, purple, lime, and cyan). The architecture features a bubbly, rounded, and highly textured organic surface. Intricate Thuluth-style calligraphy is formed by precisely arranged rainbow sprinkles (meses) and silver sugar pearls, glowing with a 'Candy Neon' LED scheme (bubblegum pink, electric violet, and bright gold) reflecting off the glossy glaze. Tall minarets are stacks of mini donuts wrapped in flickering magenta fairy lights.",
                "Donat Cokelat": "A gigantic, large-scale 1-meter standalone mosque model constructed from thousands of mini donuts coated in thick, dark chocolate ganache and dusted with edible gold leaf. The structure has a rich, high-gloss, and luxurious texture. Elegant Kufic-style calligraphy is etched into the chocolate to reveal a white cream filling, glowing from within with a 'Royal Cocoa' LED scheme (warm amber, copper, and bright gold) seeping through the chocolate cracks. Every minaret is a tall stack of golden donuts wrapped in rapidly pulsing gold fairy lights.",
                "Donat Glazed": "A colossal, large-scale 1-meter standalone mosque object made from thousands of clear-glazed mini donuts covered in a dense layer of neon-colored chocolate sprinkles. The architecture features a hyper-detailed, granular, and shimmering texture. Naskh-style calligraphy is formed by the arrangement of dark chocolate sprinkles against a neon background. The colossal main dome glows with a 'Technicolor Dream' LED scheme (rainbow colors, bright yellow, and hot pink) refracting through the sugary glaze. Every minaret is wrapped in flickering multi-colored fairy lights.",
                "Lolipop Spiral": "A monumental, large-scale 1-meter standalone mosque object built from thousands of giant swirl lollipops. The architecture features a hard, translucent 'glass-candy' texture with vibrant spiral patterns (red, white, and lime). Intricate Thuluth-style calligraphy is etched into the hard candy surface, glowing with a 'Prism Pop' LED scheme (neon pink, bright yellow, and electric cyan) refracting through the translucent lollipop sticks. Tall minarets are long candy canes wrapped in flickering silver fairy lights, with entrance arches outlined in pulsing rainbow neon strips.",
                "Oreo & Cream": "A gigantic, large-scale 1-meter standalone mosque model constructed entirely from thousands of Oreo cookies. The structure features a dark-black cocoa-biscuit texture with white cream filling visible in the layers. Elegant Kufic-style calligraphy is carved into the black biscuit surface to reveal the snowy white cream underneath, glowing from within with a 'Midnight Milk' LED scheme (cool white, pale blue, and soft silver) seeping through the cookie gaps. Every minaret is a tall stack of Oreos wrapped in rapidly pulsing white fairy lights.",
                "Marshmallow Cloud": "A monumental, large-scale 1-meter standalone mosque object built from millions of soft, puffy marshmallows (pink, white, and yellow). The architecture features a spongy, matte, and 'cloud-like' organic texture. Elegant Diwani-style calligraphy is formed by drizzling melted chocolate over the soft surface, glowing with a 'Soft Pastel' LED scheme (bubblegum pink, mint green, and pale violet) creating a hazy, diffused glow through the marshmallows. Every pillar is wrapped in intensely flickering warm-white fairy lights, with entrance arches framed by intense gold neon strips.",
                "Gummy Bears & Jelly": "A colossal, large-scale 1-meter standalone mosque object made from thousands of translucent gummy bears and jelly beans. The architecture features a squishy, high-gloss, and semi-transparent fruit-gel texture. Naskh-style calligraphy is formed by arranging dark-purple gummies against a bright-yellow background. The colossal main dome glows with a 'Neon Jungle' LED scheme (vibrant green, hot pink, and electric orange) refracting through the gelatinous body. Every minaret is a stack of jelly beans wrapped in flickering multi-colored fairy lights."    
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
    # TAB: BAMBOO CRAFT SURREAL (LUXURY ARCHITECTURE & ANIMAL DNA)
    # ==========================================================================
    with t_bamboo:
        # --- 1. KAMUS DNA KHUSUS TAB BAMBOO (Lokal di dalam tab) ---
        MASTER_BAMBOO_SOUL = {
            "Kakek (The Master Artisan)": (
                "An elderly Indonesian man with deeply weathered, sun-baked tanned skin. "
                "His face is a map of deep wrinkles with prominent crow's feet and etched forehead lines. "
                "Wispy, long white hair and a thin, stringy white beard. "
                "Expression: Wide-eyed terror, mouth slightly agape, gasping in pure shock."
            ),
            "Nenek (The Village Matriarch)": (
                "An aged woman with thick, porous skin and visible age spots. "
                "Her silver hair is pulled back into a tight, authentic bun. "
                "She has heavy drooping eyelids and deep nasolabial folds. "
                "Expression: Intense fear, body tensed up, eyes darting in panic."
            )
        }

        MASTER_BAMBOO_HOUSE = {
            "Emerald Sanctuary": (
                "A colossal, modern multi-level luxury bamboo mansion made of fresh green bamboo. "
                "Intricate hexagonal weaving patterns and sweeping organic curves. "
                "Nestled in a lush, sun-drenched tropical rainforest with massive ferns and rising mist."
            )
        }

        MASTER_INTERIOR_DNA = {
            "Glass Palace & Koi Stream": (
                "luxury bamboo interior with high glass ceilings, indoor koi stream pond on the floor, "
                "marble accents, and modern furniture. Decor features {motif} patterns."
            ),
            "Royal Bamboo Bedroom": (
                "royal bedroom suite with massive bamboo pillars, silk sheets, and a giant glass wall. "
                "The room is decorated with {motif} sculptures."
            )
        }

        # --- 2. UI SELECTION (Droplist) ---
        c1, c2 = st.columns(2)
        with c1:
            char_key = st.selectbox("JIWA KARAKTER", list(MASTER_BAMBOO_SOUL.keys()))
            house_key = st.selectbox("ARSITEKTUR BAMBU", list(MASTER_BAMBOO_HOUSE.keys()))
            hewan_key = st.selectbox("ANCAMAN HEWAN", ["King Cobra", "Bengal Tiger", "Black Panther"])
        with col2:
            # Kita buat interior key di sini
            int_key = st.selectbox("INTERIOR KEJUTAN", list(MASTER_INTERIOR_DNA.keys()))
            # Tambahan buat baju (Identity Anchor)
            cloth_desc = st.text_input("DETAIL PAKAIAN", "tattered white t-shirt and faded brown sarong")

        st.divider()

        # --- 3. RAKIT PROMPT (THE LOGIC) ---
        if st.button("🚀 RAKIT BAMBOO STORYBOARD", type="primary", use_container_width=True):
            # Ambil data dari kamus lokal di atas
            c_dna = MASTER_BAMBOO_SOUL[char_key]
            h_dna = MASTER_BAMBOO_HOUSE[house_key]
            i_dna = MASTER_INTERIOR_DNA[int_key].format(motif=hewan_key.lower())
            
            # Identity Anchor
            anchor = f"{c_dna}. Wearing {cloth_desc}."

            # OUTPUT MASTER (FLUX/VEO)
            st.subheader("🖼️ MASTER KEYFRAMES (FLUX)")
            st.code(f"MASTER A (EXTERIOR): {anchor}. Porch of {h_dna}. Threatened by {hewan_key}. Cinematic 8k.", language="text")
            st.code(f"MASTER B (INTERIOR): {anchor}, safe. Inside {i_dna}. Sunbeams through glass ceiling, 8k.", language="text")

            # OUTPUT VIDEO CHAIN (GROK)
            st.subheader("📽️ VIDEO CHAIN (GROK)")
            s1 = f"SCENE 1: {char_key} gasps in shock as the {hewan_key} rises its head. {h_dna}."
            s2 = f"SCENE 2: {char_key} turns and rushes into the green bamboo doorway, slamming it shut."
            s3 = f"SCENE 3: Camera dives into the dark bamboo doorway, transitioning into the luxury {i_dna}."
            s4 = f"SCENE 4: 360 degree pan of the {i_dna}. {char_key} is seen safe by the window."
            
            for i, sc in enumerate([s1, s2, s3, s4]):
                st.info(f"Step {i+1}")
                st.code(sc)

    # ==========================================================================
    # TAB: ANATOMY (SULTAN IDENTITY LOCK - CLEAN ENGINE)
    # ==========================================================================
    with t_anatomi:
        # --- 1. DATABASE KARAKTER ---
        DB_KARAKTER_ANATOMY = {
            "Custom/None": {"physic": "", "base": "Manual Input"},
            "DIAN": {
                # Silet Analisa: Skeleton, Transparent Skin, 3D Protruding Eyes, Pixar Style.
                "physic": "a stylized human skeleton with clean white bones, encased in a thick volumetric transparent skin, Pixar animation style, large 3D protruding expressive eyes popping out from the sockets, high-gloss surface reflections, soft round edges, extremely clean aesthetic",
                "base": "Pixar Transparent Skeleton with Pop-Out Eyes"
            },
            "JUPRI": {
                "physic": "a stylized human skeleton, smooth clean white bones, wrapped in an ultra-thin super-clear transparent skin membrane, visible glowing blue electrical nerves glowing faintly beneath the thin skin, the skin tightly clings to the bone structure, no internal organs, large 3D protruding expressive eyes, Pixar animation style, wide skeletal smile with detailed glossy teeth",
                "base": "Thin Skin Skeleton + Blue Nerves"
            },
            "SULE": {
                "physic": "a stylized 10-year-old child skeleton, short and small bone structure, smooth clean white bones, large expressive 3D protruding eyes, encased in an ultra-thin super-clear transparent skin, barely visible translucent layer, Pixar animation style, soft round edges, extremely clean aesthetic, no organs, no veins",
                "base": "Child Skeleton with Paper-Thin Glass Skin"
            },
            "SAPRI": {
                "physic": "a stylized adult human skeleton with clean white bones, only visible internal heart and lungs suspended inside the ribcage, the heart is glowing vibrant neon red, the lungs are glowing vibrant neon blue, glowing organ effects, encased in an ultra-thin super-clear transparent skin, an thin faint electric blue light traces and glows faintly around the outer skin surface, Pixar animation style, large 3D protruding eyes, no blood, clean anatomical aesthetic",
                "base": "Skeleton with Glowing Organs & Neon-Outline Skin"
            }
        }

        # --- 2. LOGIKA UPDATE OTOMATIS (SESSION STATE) ---
        if 'k1_physic_ana' not in st.session_state: st.session_state.k1_physic_ana = ""
        if 'k2_physic_ana' not in st.session_state: st.session_state.k2_physic_ana = ""

        def update_physic_ana():
            st.session_state.k1_physic_ana = DB_KARAKTER_ANATOMY[st.session_state.k1_sel_ana]["physic"]
            st.session_state.k2_physic_ana = DB_KARAKTER_ANATOMY[st.session_state.k2_sel_ana]["physic"]

        # --- 3. WRAPPER UI: DASHBOARD CLEAN ---
        with st.expander("🦴 PINTAR ANATOMY ENGINE", expanded=True):
            col_k1, col_k2 = st.columns(2)
            with col_k1:
                st.markdown('<p class="small-label">👤 KARAKTER 1 (ACTOR_1)</p>', unsafe_allow_html=True)
                k1_sel = st.selectbox("Pilih K1:", list(DB_KARAKTER_ANATOMY.keys()), key="k1_sel_ana", on_change=update_physic_ana, label_visibility="collapsed")
                k1_name = st.text_input("Nama K1:", placeholder="Nama...", key="k1_name_manual_ana") if k1_sel == "Custom/None" else k1_sel
                k1_physic = st.text_area("Fisik K1:", key="k1_physic_ana", height=100, label_visibility="collapsed")
                k1_wear = st.text_input("Pakaian K1:", placeholder="Outfit K1...", key="k1_wear_ana", label_visibility="collapsed")

            with col_k2:
                st.markdown('<p class="small-label">👤 KARAKTER 2 (ACTOR_2)</p>', unsafe_allow_html=True)
                k2_sel = st.selectbox("Pilih K2:", list(DB_KARAKTER_ANATOMY.keys()), key="k2_sel_ana", on_change=update_physic_ana, label_visibility="collapsed")
                k2_name = st.text_input("Nama K2:", placeholder="Nama...", key="k2_name_manual_ana") if k2_sel == "Custom/None" else k2_sel
                k2_physic = st.text_area("Fisik K2:", key="k2_physic_ana", height=100, label_visibility="collapsed")
                k2_wear = st.text_input("Pakaian K2:", placeholder="Outfit K2...", key="k2_wear_ana", label_visibility="collapsed")

            st.divider()
            st.markdown('<p class="small-label">🎬 NASKAH VISUAL & AKSI</p>', unsafe_allow_html=True)
            naskah_visual = st.text_area("Aksi:", placeholder="Contoh: SAPRI mencabut KERIS di depan DIAN...", key="visual_script_ana", height=150, label_visibility="collapsed")

            col_s1, col_s2, col_s3 = st.columns(3)
            with col_s1: v_style = st.selectbox("Style:", ["Sangat Nyata", "Cinematic", "Anime"], key="v_style_ana")
            with col_s2: v_light = st.selectbox("Lighting:", ["Senja Cerah (Golden)", "Misty Night", "Studio Light"], key="v_light_ana")
            with col_s3: v_cam = st.selectbox("Camera:", ["Sejajar Mata", "Low Angle", "High Angle"], key="v_cam_ana")

            v_loc = st.text_input("📍 LOKASI SETTING", placeholder="Lokasi...", key="v_loc_ana")

            st.markdown('<p class="small-label">🗣️ DIALOG SYSTEM</p>', unsafe_allow_html=True)
            col_d1, col_d2 = st.columns(2)
            with col_d1: diag_k1 = st.text_input("Dialog K1:", placeholder=f"Ucapan {k1_name}...", key="diag_k1_ana")
            with col_d2: diag_k2 = st.text_input("Dialog K2:", placeholder=f"Ucapan {k2_name}...", key="diag_k2_ana")

            btn_gen_sultan = st.button("🚀 GENERATE VIDEO PROMPT", type="primary", use_container_width=True, key="btn_gen_ana")

        # --- 4. LOGIKA PROMPT ENGINE (THE GHOST GUARD) ---
        if btn_gen_sultan:
            if naskah_visual and v_loc:
                # GHOST NEGATIVE PROMPT (UNDER THE HOOD)
                GHOST_NEG = (
                    "blur, morphing, merging characters, sinking feet, vanishing props, "
                    "object transformation, weapon shifting wielder, extra limbs, "
                    "distorted object geometry, flickering items, floating accessories"
                )

                MAP_STYLE_ANATOMY = {
                    "Sangat Nyata": "hyper-realistic photorealism, 8k RAW photo, ultra-detailed textures on skin and all surfaces, sharp focus, extreme macro details, shot on 35mm lens, f/1.8, high contrast, ray-tracing, physically based rendering, masterpiece quality",
                    "Cinematic": "cinematic movie still shot on 70mm IMAX film, anamorphic lens flare, high dynamic range (HDR), dramatic theatrical shadows, cinematic color grading, atmospheric haze, deep black levels, cinematic grain, wide aspect ratio",
                    "Anime": "high-quality 3D animation style, Pixar and Disney aesthetic, stylized character design, soft global illumination, ray-traced reflections, subsurface scattering on skin, vibrant cinematic colors, 8k render, Unreal Engine 5 render look",
                }
                MAP_LIGHT_ANATOMY = {
                    "Senja Cerah (Golden)": "soft late afternoon light, pale gold ambient glow, neutral color temperature, muted warm tones, cinematic soft shadows, clear visibility, realistic outdoor lighting, subtle highlights",
                    "Misty Night": "clear moonlit night, soft diffused moonlight, neutral color temperature, cool silver glow on surfaces, sharp focus on all objects, high contrast shadows, bioluminescent accents on characters, realistic nocturnal outdoor lighting, subtle highlights, deep black levels",
                    "Studio Light": "professional cinematic studio lighting, high-key lighting setup, sharp dual-rim light to define edges, neutral color balance, soft shadows, 8k showcase quality, ray-traced reflections on transparent skin, clean white or dark studio background"
                }
                MAP_CAM_ANATOMY = {
                    "Sejajar Mata": "eye-level cinematic shot, 50mm prime lens, natural perspective, sharp focus on subjects, subtle background blur, stabilized camera, realistic human height viewpoint",
                    "Low Angle": "dramatic low angle shot, looking up from ground level, 35mm lens, heroic perspective, emphasizing height and power, clear floor-to-subject contact, majestic scale, sharp silhouettes against the sky",
                    "High Angle": "high angle cinematic perspective, looking down from above, 35mm lens, realistic depth, clear ground shadows, emphasizing the surrounding environment, sharp overhead focus, subjects clearly grounded on the floor",
                }

                # 3. IDENTITAS KARAKTER (LOGIKA SILET: ANTI-GANTUNG)
                prompt_actors = []
                
                # Cek Karakter 1
                if k1_name and k1_name.lower() in naskah_visual.lower():
                    desc_k1 = f"{k1_name} ({k1_physic})"
                    if k1_wear: # Hanya tambah 'wearing' kalau k1_wear ada isinya
                        desc_k1 += f" wearing {k1_wear}"
                    prompt_actors.append(desc_k1)
                
                # Cek Karakter 2
                if k2_name and k2_name.lower() in naskah_visual.lower():
                    desc_k2 = f"{k2_name} ({k2_physic})"
                    if k2_wear: # Hanya tambah 'wearing' kalau k2_wear ada isinya
                        desc_k2 += f" wearing {k2_wear}"
                    prompt_actors.append(desc_k2)
                
                final_actors = " and ".join(prompt_actors) if prompt_actors else "the characters"

                # IMAGE PROMPT (SULTAN REVISION - ANATOMY SYNC)
                final_img = (
                    f"A {MAP_STYLE_ANATOMY[v_style]} photo featuring {final_actors}. "
                    f"ACTION: {naskah_visual}. "
                    f"SETTING: {v_loc}. "
                    f"ENVIRONMENT: {MAP_LIGHT_ANATOMY[v_light]} with {MAP_CAM_ANATOMY[v_cam]}. "
                    f"TECHNICAL: Absolute object permanence, precise anatomical details, solid ground-to-feet contact, "
                    f"no clipping, high-fidelity textures, 8k resolution, ray-traced shadows. "
                    f"NEGATIVE: {GHOST_NEG}"
                )
                
                # VIDEO PROMPT
                dialog_fixed = f"Only {k1_name} speaks '{diag_k1}' while {k2_name} is silent." if diag_k1 and not diag_k2 else f"Only {k2_name} speaks '{diag_k2}' while {k1_name} listens." if diag_k2 and not diag_k1 else ""
                
                # VIDEO PROMPT (SULTAN PHYSICS ENGINE)
                final_vid = (
                    f"Start from the reference image. {naskah_visual}. {dialog_fixed} "
                    f"STRICT TEMPORAL CONSISTENCY: Maintain the exact visual identity of {k1_name} and {k2_name} throughout the video. "
                    f"STRICT PHYSICS: Solid ground contact, absolutely no sinking feet into the sand. "
                    f"OBJECT PERMANENCE: All handheld props and weapons must keep their original shape and category, DO NOT morph or transform. "
                    f"Fluid biological motion, realistic gravity, high-fidelity 4k. "
                    f"NEGATIVE: {GHOST_NEG}"
                )

                # DISPLAY
                res1, res2 = st.columns(2)
                with res1: st.code(final_img, language="markdown")
                with res2: st.code(final_vid, language="markdown")
            else:
                st.error("Lokasi dan Naskah Visual wajib diisi, Dian!")
                
    # ============================================================
    # --- TAB: ⚡ TRANSFORMATION ENGINE (ULTIMATE SULTAN EDITION) ---
    # ============================================================
    with t_transform:        
        with st.expander("⚡ PINTAR TRANFORMATION ENGINE", expanded=True):

            # --- 1. DATABASE & SULTAN MAPPING (ANATOMY GRADE) ---
            DB_TRANS_EFFECT = {
                "Energi (Super Saiyan/Aura)": "radiant golden aura, electrical sparks, hair standing up, glowing energy pulses",
                "Otot (Hulk/Monster)": "rapid muscle expansion, skin stretching, clothes ripping, massive physical growth",
                "Kostum (Spiderman/Armor)": "suit material crawling over skin, nanotech assembly, liquid metal covering the body",
                "Bakar (Embers)": "burning into glowing hot embers, skin turning into charcoal then flaking away",
                "Cair (Liquid Metal)": "melting into a fluid liquid silver metal, reflective chrome transition",
                "Pasir (Dust/Sand)": "disintegrating into fine particles, blown away by mystical wind",
                "Asap (Shadow/Mist)": "turning into dark thick smoke, swirling shadows, ethereal gaseous state"
            }

            MAP_STYLE_TRANS = {
                "Sangat Nyata": "hyper-realistic raw photorealism, 8k RAW photo, ultra-detailed skin textures, sharp focus, masterpiece quality, shot on 35mm lens, f/8, ray-tracing",
                "Cinematic": "cinematic movie still shot on 70mm IMAX film, anamorphic lens flare, theatrical shadows, cinematic color grading, deep black levels",
                "Anime": "high-quality 3D animation style, Pixar aesthetic, stylized character design, soft global illumination, vibrant cinematic colors",
            }

            MAP_GEAR_TRANS = {
                "ARRI Alexa LF": "shot on ARRI Alexa LF, cinematic color science, soft highlight roll-off, professional film look, natural skin tones",
                "RED V-Raptor": "shot on RED V-Raptor 8K, extreme sharpness, high dynamic range, digital cinema texture",
                "Sony A7S III (Vlog)": "shot on Sony A7S III, handheld feel, 4k digital video texture, realistic autofocus depth",
                "Vintage 16mm": "16mm film stock, vintage grainy texture, nostalgic color grading, retro aesthetic"
            }
            
            MAP_LIGHT_TRANS = {
                "Senja Cerah (Golden)": "soft late afternoon light, pale gold ambient glow, neutral color temperature, realistic outdoor lighting",
                "Misty Night": "clear moonlit night, diffused moonlight, cool silver glow, high contrast shadows, deep black levels",
                "Studio Light": "professional cinematic studio lighting, sharp dual-rim light, neutral color balance, 8k showcase quality"
            }

            MAP_CAM_TRANS = {
                "Sejajar Mata": "eye-level cinematic shot, 50mm prime lens, natural perspective, sharp focus on subjects",
                "Low Angle": "dramatic low angle shot, looking up from ground level, 35mm lens, heroic majestic scale",
                "High Angle": "high angle cinematic perspective, looking down from above, 35mm lens, realistic depth",
            }

            # --- 2. INPUT PANEL ---
            with st.container(border=True):
                col_c1, col_c2 = st.columns(2)
                with col_c1:
                    st.markdown('<p class="small-label">👤 KARAKTER UTAMA (IDENTITY LOCK)</p>', unsafe_allow_html=True)
                    v_char_name = st.text_input("Nama Utama:", placeholder="Nama...", key="tr_name", label_visibility="collapsed")
                    v_char_physic = st.text_input("Fisik Utama:", placeholder="Fisik (Contoh: Pria atletis)...", key="tr_physic", label_visibility="collapsed")
                    v_char_outfit = st.text_input("Outfit Utama:", placeholder="Pakaian Utama...", key="tr_outfit", label_visibility="collapsed")
                with col_c2:
                    st.markdown('<p class="small-label">👥 KARAKTER TAMBAHAN (OPTIONAL)</p>', unsafe_allow_html=True)
                    v_fig_name = st.text_input("Nama Figuran:", placeholder="Nama...", key="fig_name", label_visibility="collapsed")
                    v_fig_physic = st.text_input("Fisik Figuran:", placeholder="Fisik Figuran...", key="fig_physic", label_visibility="collapsed")
                    v_fig_outfit = st.text_input("Outfit Figuran:", placeholder="Pakaian Figuran...", key="fig_outfit", label_visibility="collapsed")

                st.divider()

                col_p1, col_p2 = st.columns(2)
                with col_p1:
                    st.markdown('<p class="small-label">🧬 WUJUD AKHIR (TARGET FORM)</p>', unsafe_allow_html=True)
                    v_char_target = st.text_input("Wujud Akhir:", placeholder="Contoh: Hulk, Transformer...", key="tr_target", label_visibility="collapsed")
                    st.markdown('<p class="small-label">⚡ PEMICU SPESIFIK (TRIGGER)</p>', unsafe_allow_html=True)
                    v_trigger = st.text_input("Aksi Pemicu:", placeholder="Contoh: saat loncat, saat berteriak...", key="tr_trigger", label_visibility="collapsed")
                with col_p2:
                    st.markdown('<p class="small-label">✨ EFEK TRANSISI</p>', unsafe_allow_html=True)
                    v_eff_type = st.selectbox("Efek:", list(DB_TRANS_EFFECT.keys()), key="tr_eff", label_visibility="collapsed")
                    st.markdown('<p class="small-label">⏱️ TIMING (DETIK)</p>', unsafe_allow_html=True)
                    v_timing = st.slider("Berubah Setelah:", 1.0, 15.0, 2.0, 0.5, key="tr_time")

                st.divider()

                st.markdown('<p class="small-label">🎬 NASKAH VISUAL (PISAHKAN DENGAN TITIK . UNTUK URUTAN AKSI)</p>', unsafe_allow_html=True)
                v_scene_detail = st.text_area("Urutan Adegan:", placeholder="Contoh: DIAN jalan. DIAN lari. DIAN loncat. DIAN berubah.", height=150, key="tr_scene", label_visibility="collapsed")
                
                col_d1, col_d2 = st.columns(2)
                with col_d1:
                    st.markdown(f'<p class="small-label">💬 DIALOG {v_char_name.upper() if v_char_name else "UTAMA"}</p>', unsafe_allow_html=True)
                    v_diag_a = st.text_area("Utama Bicara:", height=30, key="tr_diag_a", label_visibility="collapsed")
                with col_d2:
                    st.markdown(f'<p class="small-label">💬 DIALOG {v_fig_name.upper() if v_fig_name else "FIGURAN"}</p>', unsafe_allow_html=True)
                    v_fig_diag = st.text_area("Figuran Bicara:", height=30, key="tr_fig_diag", label_visibility="collapsed")

                st.divider()

                col_s1, col_s2 = st.columns(2)
                with col_s1:
                    st.markdown('<p class="small-label">🎨 STYLE & LIGHTING</p>', unsafe_allow_html=True)
                    v_style_choice = st.selectbox("Style:", list(MAP_STYLE_TRANS.keys()), key="tr_style", label_visibility="collapsed")
                    v_light_choice = st.selectbox("Lighting:", list(MAP_LIGHT_TRANS.keys()), key="tr_light", label_visibility="collapsed")
                with col_s2:
                    st.markdown('<p class="small-label">🎥 CAMERA GEAR & SHOT</p>', unsafe_allow_html=True)
                    v_gear_choice = st.selectbox("Camera Gear:", list(MAP_GEAR_TRANS.keys()), key="tr_gear", label_visibility="collapsed")
                    v_cam_choice = st.selectbox("Shot Angle:", list(MAP_CAM_TRANS.keys()), key="tr_cam", label_visibility="collapsed")

                v_loc = st.text_input("📍 Lokasi Kejadian:", placeholder="Lokasi...", key="tr_loc")

                btn_gen_trans = st.button("🚀 GENERATE PROMPT", type="primary", use_container_width=True)

            # --- 3. LOGIKA GENERATOR PROMPT (SULTAN ENGINE) ---
            if btn_gen_trans:
                if v_char_name and v_scene_detail and v_loc:
                    
                    def rakit_identitas_sultan(name, physic, outfit, is_master=False):
                        if not name: return ""
                        ref_tag = "refer to PHOTO #MASTER ONLY" if is_master else "visual description only"
                        return f"[[ CAST_SULTAN_{name.upper()} ({name}): {ref_tag}. PHYSIC: {physic}. WEAR: {outfit} ]]"

                    steps = [s.strip() for s in v_scene_detail.split('.') if len(s.strip()) > 2]
                    first_step_text = steps[0].upper() if steps else v_scene_detail.upper()
                    
                    fig_in_script = True if (v_fig_name and v_fig_name.upper() in v_scene_detail.upper()) else False
                    fig_in_first_frame = True if (v_fig_name and v_fig_name.upper() in first_step_text) else False

                    main_id = rakit_identitas_sultan(v_char_name, v_char_physic, v_char_outfit, is_master=True)
                    fig_id_full = " AND " + rakit_identitas_sultan(v_fig_name, v_fig_physic, v_fig_outfit) if fig_in_script else ""
                    fig_id_initial = " AND " + rakit_identitas_sultan(v_fig_name, v_fig_physic, v_fig_outfit) if fig_in_first_frame else ""

                    # --- LOGIKA DIALOG ---
                    target_phase = "Phase 2" if len(steps) > 1 else "Phase 1"
                    video_diag = ""
                    if v_diag_a or v_fig_diag:
                        video_diag = f"DIALOGUE EXECUTION: Mouth movement is ONLY allowed for the speaker. "
                        if v_diag_a and not v_fig_diag:
                            video_diag += f"In {target_phase}, {v_char_name} is the ONLY one speaking: '{v_diag_a}'. {v_fig_name} must keep mouth tightly closed."
                        elif v_fig_diag and not v_diag_a:
                            video_diag += f"In {target_phase}, {v_fig_name} is the ONLY one speaking: '{v_fig_diag}'. {v_char_name} must keep mouth tightly closed."
                        elif v_diag_a and v_fig_diag:
                            video_diag += f"In {target_phase}, {v_char_name} speaks first, then {v_fig_name} replies. No simultaneous talking."

                    # --- FIX ERROR: DEFINISI DULU BARU TAMBAH ---
                    ULTRA_SHARP = "extreme sharp focus, cinematic texture, visible skin pores, natural imperfections, 8k, masterpiece quality, no motion blur"
                    TRANS_NEG = "text, speech bubbles, subtitles, floating objects, extra limbs, plastic texture, airbrushed, cartoon, low quality, glitch, distorted hands"
                    
                    # Sekarang aman buat ditambahin karena TRANS_NEG sudah ada isinya
                    if v_fig_name:
                        TRANS_NEG += f", {v_fig_name} talking, simultaneous speaking, ghost lipsync, vibrating lips"

                    is_trans = True if (v_trigger and v_char_target) else False
                    trans_logic = (f"CHRONOLOGY: Maintain {v_char_outfit} form until {v_timing}s, then as {v_char_name} {v_trigger}, morph into {v_char_target}." if is_trans else "PURE ACTION.")

                    # --- FINAL OUTPUT ---
                    final_img = (
                        f"{main_id}{fig_id_initial}. SCENE START: {steps[0] if steps else v_scene_detail}. Neutral expression, closed mouth. "
                        f"VISUAL: {MAP_GEAR_TRANS[v_gear_choice]}, {MAP_CAM_TRANS[v_cam_choice]}, {MAP_STYLE_TRANS[v_style_choice]}, {MAP_LIGHT_TRANS[v_light_choice]}. "
                        f"TECHNICAL: {ULTRA_SHARP}. NEGATIVE: {TRANS_NEG}"
                    )
                    
                    final_vid = (
                        f"MANDATORY: START DIRECTLY FROM THE UPLOADED REFERENCE IMAGE. {main_id}{fig_id_full}. STORYLINE: {' -> '.join([f'Phase {i+1}: {s}' for i, s in enumerate(steps)])}. {video_diag} "
                        f"CINEMATOGRAPHY: {MAP_GEAR_TRANS[v_gear_choice]}, {MAP_STYLE_TRANS[v_style_choice]}, {MAP_LIGHT_TRANS[v_light_choice]}. "
                        f"{trans_logic} TECHNICAL: {ULTRA_SHARP}. Ensure 100% identity consistency for 20s. NEGATIVE: {TRANS_NEG}"
                    )

                    st.divider()
                    res1, res2 = st.columns(2)
                    with res1:
                        st.markdown('<p class="small-label">📸 1. GENERATE IMAGE INI</p>', unsafe_allow_html=True)
                        st.code(final_img, language="markdown")
                    with res2:
                        st.markdown(f'<p class="small-label">🎬 2. UPLOAD IMAGE KE VIDEO PROMPT INI</p>', unsafe_allow_html=True)
                        st.code(final_vid, language="markdown")
                else:
                    st.error("Minimal isi Nama Utama, Naskah, dan Lokasi!")

    with t_random:
        st.status("Sedang proses...", expanded=False)
