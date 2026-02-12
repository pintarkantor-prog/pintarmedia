import streamlit as st
import requests
import json

# ────────────────────────────────────────────────
# Custom styling mirip Grok / xAI (dark & clean)
# ────────────────────────────────────────────────
st.set_page_config(page_title="Prompt Generator • Grok Style", layout="centered")

st.markdown("""
    <style>
    /* Dark theme base */
    .stApp {
        background-color: #0f0f11;
        color: #e0e0e0;
    }
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111113;
    }
    /* Text input & textarea */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #1a1a1e;
        color: #f0f0f0;
        border: 1px solid #333338;
        border-radius: 6px;
    }
    /* Button */
    .stButton > button {
        background-color: #0066ff;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.6rem 1.4rem;
        font-weight: 500;
    }
    .stButton > button:hover {
        background-color: #0055dd;
    }
    .stButton > button:active {
        background-color: #0044bb;
    }
    /* Headers & text */
    h1, h2, h3 {
        color: #ffffff;
    }
    hr {
        border-color: #333;
    }
    /* Expander & other elements */
    .stExpander {
        background-color: #16161a;
        border: 1px solid #2a2a2f;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Header & Intro
# ────────────────────────────────────────────────
st.title("Prompt Generator")
st.caption("Buat prompt gambar & video yang optimal — powered by Grok")

st.markdown("---")

# ────────────────────────────────────────────────
# Sidebar (API Key & Settings)
# ────────────────────────────────────────────────
with st.sidebar:
    st.header("Settings")
    
    api_key = st.text_input(
        "xAI API Key (SuperGrok)",
        type="password",
        help="Dapatkan dari https://console.x.ai"
    )
    
    model = st.selectbox(
        "Model",
        ["grok-4", "grok-beta"],
        index=0
    )
    
    max_tokens = st.slider("Max tokens", 100, 600, 350)

# ────────────────────────────────────────────────
# Main Form
# ────────────────────────────────────────────────
col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_area(
        "Deskripsikan gambar atau video yang kamu inginkan",
        height=160,
        placeholder="Contoh:\nSeorang samurai cyberpunk berdiri di atap gedung neon Tokyo malam hari, hujan deras, sangat detail, sinematik, 8k"
    )

with col2:
    prompt_type = st.radio(
        "Tipe",
        ["Gambar", "Video"],
        index=0,
        horizontal=False
    )

    aspect_ratio = st.selectbox(
        "Aspect Ratio",
        ["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "Custom"],
        index=1
    )

    style_preset = st.selectbox(
        "Gaya (opsional)",
        ["", "Photorealistic", "Cinematic", "Anime", "Cyberpunk", "Studio Ghibli", "Surreal", "Oil Painting", "3D Render", "Minimalist"],
        index=0
    )

# ────────────────────────────────────────────────
# Generate Button & Logic
# ────────────────────────────────────────────────
if st.button("Generate Prompt", type="primary", use_container_width=True):
    
    if not api_key.strip():
        st.error("Masukkan xAI API Key terlebih dahulu di sidebar")
        st.stop()
    
    if not user_input.strip():
        st.warning("Tulis deskripsi dulu ya...")
        st.stop()

    # ─── Prepare system prompt ───────────────────────
    system_prompt = """Kamu adalah ahli prompt engineering untuk AI gambar dan video (Midjourney, Flux, Runway, Kling, Luma, Pika, dll).
Buat prompt yang sangat detail, deskriptif, terstruktur, dan powerful dalam bahasa Inggris.
Gunakan kata-kata visual yang kuat, lighting, komposisi, mood, warna, detail tekstur, dan kualitas tinggi."""

    if prompt_type == "Video":
        system_prompt += "\nKarena ini untuk video: tambahkan elemen gerakan, camera movement, timing, dan dinamika scene."

    if style_preset:
        system_prompt += f"\nGunakan gaya {style_preset}."

    if aspect_ratio != "Custom":
        system_prompt += f"\nGunakan aspect ratio {aspect_ratio}."

    user_message = f"""Buat prompt terbaik berdasarkan deskripsi berikut:

{user_input}

Jawab HANYA dengan prompt-nya saja, tanpa pengantar, tanpa tanda kutip, tanpa penjelasan tambahan."""

    # ─── Call xAI API ────────────────────────────────
    with st.spinner("Meminta Grok membuat prompt terbaik..."):
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                "temperature": 0.7,
                "max_tokens": max_tokens
            }

            response = requests.post(
                "https://api.x.ai/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=45
            )

            response.raise_for_status()
            result = response.json()

            generated_prompt = result["choices"][0]["message"]["content"].strip()

            # Tampilkan hasil
            st.success("Prompt berhasil dibuat!")
            st.markdown("### Prompt yang siap dipakai")
            st.code(generated_prompt, language=None)

            # Tombol copy (Streamlit 1.38+ mendukung ini)
            st.download_button(
                label="Download .txt",
                data=generated_prompt,
                file_name="prompt.txt",
                mime="text/plain"
            )

        except requests.exceptions.RequestException as e:
            st.error(f"Error koneksi ke xAI API:\n{str(e)}")
        except KeyError:
            st.error("Format response API tidak sesuai. Coba lagi atau ganti model.")
        except Exception as e:
            st.error(f"Terjadi kesalahan:\n{str(e)}")

# Footer
st.markdown("---")
st.caption("Made with Streamlit • Powered by Grok (xAI) • 2026")
