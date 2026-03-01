import streamlit as st

def halaman_cyber_generals():
    st.set_page_config(
        page_title="Pintar Digital | Cyber Command",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown("""
        <style>
        [data-testid="stHeader"], [data-testid="stSidebar"], footer {
            display: none !important;
        }
        
        .main {
            background-color: #010409;
            height: 100vh;
            overflow: hidden;
            position: relative;
        }

        /* --- STYLE AVATAR JENDERAL DIGITAL --- */
        .general-icon {
            position: absolute;
            width: 90px; height: 90px;
            z-index: 10;
            filter: drop-shadow(0 0 15px rgba(0, 242, 254, 0.5));
        }

        @keyframes patrol {
            0% { transform: translate(0,0) rotate(0deg); }
            25% { transform: translate(75vw, 10vh) rotate(15deg); }
            50% { transform: translate(40vw, 60vh) rotate(-15deg); }
            75% { transform: translate(-5vw, 30vh) rotate(10deg); }
            100% { transform: translate(0,0) rotate(0deg); }
        }

        /* Mapping Jenderal per Negara */
        .gen-us { animation: patrol 12s infinite linear; }
        .gen-isr { animation: patrol 15s infinite linear reverse; }
        .gen-ira { animation: patrol 20s infinite linear; }
        .gen-rus { animation: patrol 18s infinite linear; }
        .gen-nk  { animation: patrol 14s infinite linear reverse; }
        
        .rocket-fire { position: absolute; font-size: 45px; animation: patrol 9s infinite linear; z-index: 5; }

        /* --- FOOTER KOTA DIGITAL --- */
        .city-footer {
            position: fixed;
            bottom: 0; left: 0;
            width: 100%;
            height: 200px;
            background-image: linear-gradient(to top, #010409 20%, transparent 100%),
                              url('https://images.unsplash.com/photo-1519608487953-e999c86e7455?q=80&w=1600&auto=format&fit=crop');
            background-size: cover;
            background-position: bottom;
            z-index: 2;
            border-top: 2px solid #00f2fe;
        }
        </style>
        
        <img src="https://img.icons8.com/?size=100&id=103757&format=png" class="general-icon gen-us" title="US Cyber Command">
        <img src="https://img.icons8.com/?size=100&id=102553&format=png" class="general-icon gen-isr" title="ISR Mossad Unit">
        <img src="https://img.icons8.com/?size=100&id=A8oX9D20P5xV&format=png" class="general-icon gen-ira" title="IRA Cyber Unit">
        <img src="https://img.icons8.com/?size=100&id=63651&format=png" class="general-icon gen-rus" title="RUS Iron Fist">
        <img src="https://img.icons8.com/?size=100&id=103753&format=png" class="general-icon gen-nk" title="NK Missile Command">
        
        <div class="rocket-fire" style="top:50%; left:50%;">🚀</div>
        <div class="rocket-fire" style="top:20%; left:70%; animation-delay: 2s;">✈️</div>

        <div class="city-footer"></div>
    """, unsafe_allow_html=True)

    st.stop()

halaman_cyber_generals()
