import streamlit as st
import requests

# ────────────────────────────────────────────────
# Page config: centered, mobile-like
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="Prompt Generator • Grok Style",
    layout="centered",
    initial_sidebar_state="collapsed"   # Sidebar disembunyikan dulu biar lebih clean
)

# ────────────────────────────────────────────────
# True black + Gemini-like dark theme CSS
# ────────────────────────────────────────────────
st.markdown("""
    <style>
    /* True black background seperti Gemini 2025-2026 */
    .stApp {
        background-color: #000000;
        color: #e0e0ff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    /* Hilangkan padding berlebih biar lebih mobile-like */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 680px;  /* Lebar mirip app mobile */
    }
    /* Greeting sparkle style */
    .greeting {
        font-size: 2.2rem;
        font-weight: 600;
        text-align: center;
        margin: 2rem 0 1.5rem;
        color: #ffffff;
    }
    .sparkle {
        font-size: 2.8rem;
        vertical-align: middle;
        margin-right: 0.5rem;
    }
    /* Prompt input besar & rounded */
    .stTextArea > div > div > textarea {
        background-color: #111114;
        color: #f0f0ff;
        border: 1px solid #333338;
        border-radius: 24px !important;
        padding: 16px 20px !important;
        font-size: 1.1rem;
        min-height: 120px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.6);
    }
    /* Suggestion chips */
    .chip-button {
        background-color: #1a1a2e;
        color: #8ab4f8;
        border: 1px solid #333366;
        border-radius: 999px;
        padding: 10px 20px;
        margin: 6px;
        font-size: 0.95rem;
        cursor: pointer;
        display: inline-block;
        text-align: center;
        transition: all 0.2s;
    }
    .chip-button:hover {
        background-color: #2a2a4a;
        border-color: #5060ff;
    }
    /* Generate button */
    .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #0066ff, #00aaff);
        color: white;
        border: none;
        border-radius: 999px;
        padding: 14px 32px;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 1.5rem auto;
        display: block;
        width: 80%;
        max-width: 320px;
    }
    hr {
        border-color: #222;
        margin: 2rem 0;
    }
    /* Sidebar minimal */
    section[data-testid="stSidebar"] {
        background-color: #0a0a0a;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Greeting mirip Gemini
# ────────────────────────────────────────────────
st.markdown('<div class="greeting"><span class="sparkle">✨</span> Halo Pintar</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#a0a0ff; margin-bottom:2rem;">Sebaiknya kita mulai dari mana?</p>', unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Sidebar: API Key & Settings (collapsed by default)
# ────────────────────────────────────────────────
with st.sidebar:
    st.header("Pengaturan")
    api_key = st.text_input("xAI API Key", type="password", help="Dapatkan di https://console.x.ai")
    model = st.selectbox("Model Grok", ["grok-4", "grok-beta"], index=0)
    max_tokens = st.slider("Max tokens", 150, 500, 300)

# ────────────────────────────────────────────────
# Main prompt area
# ────────────────────────────────────────────────
user_input = st.text_area(
    "",
    height=140,
    placeholder="Minta prompt gambar/video yang kamu mau...",
    key="prompt_input",
    label_visibility="collapsed"
)

# ────────────────────────────────────────────────
# Suggestion chips (mirip Gemini suggestions)
# ────────────────────────────────────────────────
st.markdown("### Ide cepat")
chips = [
    "Buat Gambar", "Buat Video", "Buat hari ini lebih produktif",
    "Tulis apa saja", "Bantu belajar", "Cerita horor malam ini"
]

cols = st.columns(2)
for i, chip in enumerate(chips):
    with cols[i % 2]:
        if st.button(chip, key=f"chip_{i}", use_container_width=True, type="secondary"):
            # Contoh: auto-fill prompt input (bisa dikembangkan)
            st.session_state.prompt_input = f"Generate prompt untuk {chip.lower()} yang keren dan detail"
            st.rerun()

# ────────────────────────────────────────────────
# Generate logic
# ────────────────────────────────────────────────
if st.button("Generate Prompt", type="primary"):
    if not api_key:
        st.error("Masukkan API Key dulu di sidebar ya")
    elif not user_input.strip():
        st.warning("Tulis dulu idenya...")
    else:
        with st.spinner("Grok sedang memasak prompt terbaik..."):
            try:
                headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
                payload = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "Kamu ahli prompt engineering untuk gambar & video AI. Buat prompt super detail dalam bahasa Inggris, optimal untuk Flux/Midjourney/Runway/Kling dll. Jawab HANYA prompt-nya saja, tanpa intro."},
                        {"role": "user", "content": user_input}
                    ],
                    "max_tokens": max_tokens,
                    "temperature": 0.75
                }
                resp = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=payload, timeout=40)
                resp.raise_for_status()
                prompt_result = resp.json()["choices"][0]["message"]["content"].strip()

                st.success("Prompt siap!")
                st.markdown("**Prompt yang dihasilkan:**")
                st.code(prompt_result, language=None)

                st.download_button("Simpan sebagai .txt", prompt_result, "prompt-kreatif.txt")

            except Exception as e:
                st.error(f"Ada masalah: {str(e)}")

# Footer kecil
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Powered by Grok • Dibuat dengan Streamlit • 2026")
