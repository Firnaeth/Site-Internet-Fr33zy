import streamlit as st
import streamlit.components.v1 as components

# =========================================================================
# 📦 ÉTAPE 1 : CONFIGURATION DE LA PAGE & INITIALISATION MÉMOIRE
# =========================================================================
st.set_page_config(
    page_title="Fr33zy Over Studio",
    page_icon="logo_officiel-FOS.png",
    layout="wide"
)

# Initialisation immédiate et sécurisée de TOUTES les variables d'état
if "theme" not in st.session_state:
    st.session_state.theme = "Subnautica_2"
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "QUI SOMMES-NOUS"
if "current_profile" not in st.session_state:
    st.session_state.current_profile = None
if "Subnautica_2_story_year" not in st.session_state:
    st.session_state.Subnautica_2_story_year = "2012"
if "Subnautica_2_project_year" not in st.session_state:
    st.session_state.Subnautica_2_project_year = "2024"

# --- DÉFINITION DES INFOS TECHNIQUES ---
VERSION = "v0.0.1"
LICENSE_TEXT_WHITE = "© 2026 "
STUDIO_NAME = "FR33ZY OVER STUDIO."
TOOLS = "POWERED BY OBS STUDIO • DAVINCI RESOLVE • KDENLIVE • PHOTOSHOP • GIMP • STREAMLIT"

# =========================================================================
# 🎨 STRUCTURE DES AMBIANCES CSS (ORANGE CLASSIQUE VS Subnautica_2 CYAN)
# =========================================================================
if st.session_state.theme == "Subnautica_2":
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght=500;700;900&display=swap');

        /* 🎯 POLICE GLOBALE EN MODE SUBNAUTICA (ORBITRON) */
        body, .stApp, p, span, div, button, h1, h2, h3, h4 { 
            font-family: 'Orbitron', sans-serif !important; 
            color: white; 
        }

        /* Boutons Subnautica_2 HUD */
        .stButton > button, .stLinkButton > a {
            border: 1px solid rgba(0, 210, 255, 0.3) !important;
            background-color: #121820 !important;
            color: #00d2ff !important;
            font-family: 'Orbitron', sans-serif !important;
            letter-spacing: 2px;
            font-weight: bold !important;
            border-radius: 4px !important;
            font-size: 0.85rem !important;
            transition: all 0.3s ease !important;
        }
        .stButton > button:hover, .stLinkButton > a:hover {
            border-color: #00d2ff !important;
            box-shadow: 0 0 12px rgba(0, 210, 255, 0.4) !important;
            color: white !important;
        }
        
        .hud-social-container {
        margin: 0;
        font-size: 0.62rem;
        color: #475569;
        letter-spacing: 2px;
        font-weight: 500;
        margin-top: 4px;
        font-family: 'Orbitron', sans-serif;
    }
    .hud-social-link {
        color: #00d2ff !important; /* Devient cyan comme sur ton image (mets #d37c2e pour l'orange) */
        text-decoration: none !important; /* Supprime le soulignement */
        transition: color 0.2s ease;
    }
    .hud-social-link:hover {
        color: #ffffff !important; /* Passe en blanc propre au survol */
    }
    .hud-social-container span {
        color: #475569;
        margin: 0 8px;
    }

        /* Cartouches d'équipe */
        .member-card { 
            background: #121820; 
            border: 1px solid rgba(0, 210, 255, 0.2); 
            border-radius: 6px; 
            padding: 25px; 
            margin-top: 20px;
            text-align: center; 
            min-height: 230px;
        }
        .member-card:hover { border-color: #00d2ff; }

        /* Qui sommes-nous & Cartes Globales */
        .orange-card-classic { background-color: #121820; border: 1px solid rgba(0, 210, 255, 0.4); border-radius: 6px; padding: 20px; margin-bottom: 25px; }
        .orange-title-classic { color: #00d2ff !important; font-weight: bold; font-size: 1.2rem; margin-bottom: 10px; font-family: 'Orbitron', sans-serif; }
        .orange-text-classic { color: #cbd5e1 !important; font-size: 0.95rem; line-height: 1.6; }

        .Subnautica_2-box { background-color: #121820; border: 1px solid rgba(0, 210, 255, 0.4); border-radius: 6px; padding: 20px; margin-bottom: 25px; }
        .Subnautica_2-h1 { color: #00d2ff !important; font-family: 'Orbitron', sans-serif; font-weight: 700; font-size: 1rem; margin-bottom: 10px; }
        .Subnautica_2-p { color: #cbd5e1 !important; font-size: 0.95rem; line-height: 1.6; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        /* 🎯 POLICE GLOBALE EN MODE CLASSIC (SANS-SERIF DE BASE) */
        body, .stApp, p, span, div, button, h1, h2, h3, h4 { 
            font-family: sans-serif !important; 
            color: white;
        }
        
        /* Tes autres styles du thème Orange restent ici... */

        /* Boutons Orange d'origine */
        .stButton > button, .stLinkButton > a {
            border: 1px solid #242c34 !important;
            background-color: #121820 !important;
            color: #d37c2e !important;
            font-family: 'Orbitron', sans-serif !important;
            letter-spacing: 2px;
            font-weight: bold !important;
            border-radius: 4px !important;
            font-size: 0.85rem !important;
            transition: all 0.3s ease !important;
        }
        .stButton > button:hover, .stLinkButton > a:hover {
            border-color: #ff8c2e !important;
            box-shadow: 0 0 12px rgba(255, 140, 46, 0.3) !important;
            color: white !important;
        }

        /* Cartouches d'équipe */
        .member-card { 
            background: #121820; 
            border: 1px solid #242c34; 
            border-radius: 6px; 
            padding: 25px; 
            margin-top: 20px;
            text-align: center; 
            min-height: 230px;
        }
        .member-card:hover { border-color: #d37c2e; }

        /* Qui sommes-nous & Cartes Globales */
        .orange-card-classic { background-color: #121820; border: 1px solid #242c34; border-radius: 6px; padding: 20px; margin-bottom: 25px; }
        .orange-title-classic { color: #d37c2e !important; font-weight: bold; font-size: 1.2rem; margin-bottom: 10px; font-family: 'Orbitron', sans-serif; }
        .orange-text-classic { color: #94a3b8 !important; font-size: 0.95rem; line-height: 1.6; }
        </style>
    """, unsafe_allow_html=True)

# =========================================================================
# 🧭 ÉTAPE 2 : EN-TÊTE DU SITE (TITRE, ACTU HUD CONNECTÉE & SÉPARATION)
# =========================================================================

st.markdown(
    '<h1 style="text-align: left; font-family: \'Orbitron\', sans-serif; font-weight: 700; color: #ffffff; letter-spacing: 3px; margin-top:20px; margin-bottom:30px;">FR33ZY OVER STUDIO</h1>',
    unsafe_allow_html=True)

if "action" in st.query_params and st.query_params["action"] == "go_to_projets":
    st.session_state.active_tab = "PROJETS"
    st.query_params.clear()
    st.rerun()

if st.session_state.theme == "Subnautica_2":
    st.markdown(
        "<style>@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght=500;700;900&display=swap');.Subnautica_2-actu-container { max-width: 950px; margin-bottom: 25px; font-family: 'Orbitron', sans-serif; position: relative; display: block; }.Subnautica_2-banner-box { background: linear-gradient(90deg, #51e5ff 0%, #176087 40%, #0c2340 100%); border-radius: 20px; padding: 22px 35px; display: flex; align-items: center; box-shadow: 0 0 25px rgba(23, 96, 135, 0.4); border: 1px solid rgba(81, 229, 255, 0.3); }.Subnautica_2-left-part { display: flex; align-items: center; gap: 15px; min-width: 320px; color: #0c2340; font-weight: 900; font-size: 1.35rem; letter-spacing: 1px; }.Subnautica_2-bell-icon { font-size: 1.9rem; }.Subnautica_2-right-part { color: #ffffff; font-size: 1.2rem; font-weight: 500; padding-left: 30px; border-left: 2px solid rgba(255, 255, 255, 0.2); line-height: 1.4; }.Subnautica_2-bold-text { font-weight: 700; }.Subnautica_2-interactive-row { display: flex; align-items: center; height: 38px; margin-top: -2px; }.Subnautica_2-connector-line { width: 250px; height: 19px; border-left: 2px solid #51e5ff; border-bottom: 2px solid #51e5ff; margin-left: 120px; border-bottom-left-radius: 12px; flex-shrink: 0; box-sizing: border-box; }.Subnautica_2-custom-button { background: rgba(12, 35, 64, 0.7); color: #51e5ff; border: 2px solid #51e5ff; padding: 0px 24px; font-family: 'Orbitron', sans-serif; font-size: 0.95rem; font-weight: bold; border-radius: 8px; cursor: pointer; display: inline-flex; align-items: center; text-decoration: none; transition: all 0.3s ease; box-sizing: border-box; height: 38px; margin-top: 19px; }.Subnautica_2-custom-button:hover { background: #51e5ff !important; color: #0c2340 !important; box-shadow: 0 0 20px #51e5ff !important; }</style>",
        unsafe_allow_html=True)
    st.markdown(
        '<div class="Subnautica_2-actu-container"><div class="Subnautica_2-banner-box"><div class="Subnautica_2-left-part"><span class="Subnautica_2-bell-icon">📢</span><div>DERNIÈRE ACTU<br>STUDIO :</div></div><div class="Subnautica_2-right-part">Firnaeth. & Xanna La Nooblette, plongent dans les abysses de <span class="Subnautica_2-bold-text">Subnautica 2 ! 🤿</span></div></div><div class="Subnautica_2-interactive-row"><div class="Subnautica_2-connector-line"></div><a href="?action=go_to_projets" target="_self" class="Subnautica_2-custom-button">Voir les Actualités</a></div></div>',
        unsafe_allow_html=True)

st.markdown('<hr style="border-color: #242c34; margin-top: 15px; margin-bottom: 30px;">', unsafe_allow_html=True)

# --- 3. ONGLETS DE NAVIGATION ---
tabs = ["QUI SOMMES-NOUS", "L'ÉQUIPE", "PROJETS", "SHOP", "CONTACT", "DON"] # "PHOTOS" est caché ici
cols_nav = st.columns(6) # Changé de 4 à 7

for i, btn_name in enumerate(tabs):
    with cols_nav[i]:
        if st.session_state.active_tab == btn_name:
            accent_nav = "#00d2ff" if st.session_state.theme == "Subnautica_2" else "#ff8c2e"
            st.markdown(f"""
                <style>
                div[data-testid="stColumn"]:nth-of-type({i + 1}) button {{
                    border-color: {accent_nav} !important;
                    color: #ffffff !important;
                }}
                </style>
            """, unsafe_allow_html=True)

        if st.button(btn_name, key=f"nav_main_{btn_name}", use_container_width=True):
            st.session_state.active_tab = btn_name
            st.session_state.current_profile = None
            st.rerun()

st.markdown('<hr style="border-color: #242c34; margin-top: 15px; margin-bottom: 30px;">', unsafe_allow_html=True)

# =========================================================================
# 💾 DONNÉES DES MEMBRES
# =========================================================================
CREATEURS = {
    "Firnaeth": {
        "role": "Founding Member / Streameur",
        "img": "https://unavatar.io/youtube/firnaethYT",
        "desc": "Animateur à l'imagination debridée et fondateur du studio, je vous embarque dans un courant chaotique entre pixels, créations animées et réflexions absurdes. ⚓🌊",
        "youtube": "https://www.youtube.com/@firnaethYT",
        "twitch": "https://twitch.tv/firnaeth",
        "instagram": "https://instagram.com/firnaeth_yt",
        "threads": "https://www.threads.com/@firnaeth_yt",
        "discord": "https://discord.gg/h4r2MSgJSk",
        "series": [
            ("📜 Journal d’un forge-lol 🔨", "https://youtube.com/playlist?list=PLgX-3H3ACJk5Rb3whj-89ANDgMXN-iaBf"),
            ("⚔️ Lura : L’Héritière des Forges", "https://www.youtube.com/playlist?list=PLgX-3H3ACJk40I098msu4YsPFX5fNPRDO"),
            ("Chroniques De Silent Hill 2", "https://www.youtube.com/playlist?list=PLgX-3H3ACJk7l33I2euw_yEPJ7a4JEVx9"),
            ("Underground Garage", "https://www.youtube.com/playlist?list=PLgX-3H3ACJk6exfv_mzqJ-IKSZJbhFuNe")
        ],
        "jeux": "Silent Hill 2, The Elder Scrolls V: Skyrim, Medieval Crafter: Blacksmith",
        "planning_text": "VOIR LE PLANNING SUR TWITCH",
        "planning_url": "https://twitch.tv/firnaeth/schedule"
    },
    "NICO LE GEEK": {
        "role": "Founding Member / Geek",
        "img": "https://unavatar.io/youtube/NICOLEGEEK",
        "desc": "Un vrai mordu de culture geek, grand collectionneur de consoles et de jeux rétro. Toujours prêt pour une partie sur les classiques qui ont marqué l'histoire.",
        "youtube": "https://www.youtube.com/@NICOLEGEEK",
        "twitch": None,
        "instagram": "https://instagram.com",
        "threads": None,
        "discord": "https://discord.gg/h4r2MSgJSk",
        "series": [
            ("LE BUREAU DES PLINTHES", "https://youtube.com/playlist?list=PLkBX3VXLbjxjTAXJeaohmW9G-F9Wne1c3")
        ],
        "jeux": "🕹️ Resident Evil 0-9",
        "planning_text": "PAS DE PLANNING FIXE ACTUELLEMENT",
        "planning_url": "None"
    },
    "Xanna La Nooblette": {
        "role": "Founding Member / Streameuse",
        "img": "https://unavatar.io/youtube/xannalanooblette",
        "desc": "Entre humour, fails épiques et avantures virtuelles, je transforme mes galères en gameplay pour vous offerir le meilleur du gaming avec style ! 🍰🎮",
        "youtube": "https://www.youtube.com/@xannalanooblette",
        "twitch": "https://twitch.tv/xannalanooblette",
        "instagram": "https://instagram.com/xannalasedistemaispastrop",
        "threads": None,
        "discord": "https://discord.gg/h4r2MSgJSk",
        "series": [
            ("Subnautica 2", "https://www.youtube.com/playlist?list=PLD-GVWgeEc6cWHG8Cg0liIoEaluph5mS0"),
            ("L'Épopée Féline", "https://www.youtube.com/playlist?list=PLD-GVWgeEc6fCdkCXg38Bcw7fm9YZcuzV"),
            ("Crime Scene Cleaner", "https://www.youtube.com/playlist?list=PLD-GVWgeEc6dfycSPIsT9LmSuAa4rlSx9"),
            ("Slime Rancher 2", "https://www.youtube.com/playlist?list=PLD-GVWgeEc6diG7X1purupOBtHJqrZwnx")
        ],
        "jeux": "Subnautica 2, The Elder Scrolls V: Skyrim, Crime Scene Cleaner",
        "planning_text": "VOIR LE PLANNING SUR TWITCH",
        "planning_url": "https://twitch.tv/xannalanooblette/schedule"
    }
}

# =========================================================================
# 🎭 ÉTAPE 3 : LOGIQUE INTERNE DES PAGES INTERACTIVES
# =========================================================================

# --- 📜 ONGLET QUI SOMMES-NOUS ---
if st.session_state.active_tab == "QUI SOMMES-NOUS":
    accent_color = "#00d2ff" if st.session_state.theme == "Subnautica_2" else "#d37c2e"

    st.markdown(f"""
    <div class="orange-card-classic">
        <div class="orange-title-classic">BIENVENUE CHEZ FR33ZY OVER STUDIO</div>
        <div class="orange-text-classic">Depuis 2012, nous partageons notre passion pour l'univers du gaming. Notre équipe évolue pour vous proposer une expérience communautaire unique, mêlant expertise technique et amour du jeu.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f'<h4 style="font-family:\'Orbitron\', sans-serif; color:{accent_color}; margin-top:20px; margin-bottom:25px;">📜 NOTRE PARCOURS</h4>',
        unsafe_allow_html=True)

    if st.session_state.theme == "Subnautica_2":
        story_cols = st.columns(3)
        years = ["2012", "2016", "2024"]
        labels = ["🚀 ORIGINES (2012)", "👥 L'ALLIANCE (2016)", "⚓ NOUVELLE ÈRE (2024)"]

        for idx, yr in enumerate(years):
            with story_cols[idx]:
                is_selected = st.session_state.Subnautica_2_story_year == yr
                st.markdown(f"""
                    <style>
                    div[data-testid='stColumn']:nth-of-type({idx + 1}) button {{
                        border-color: {'#00d2ff !important' if is_selected else 'rgba(0, 210, 255, 0.3) !important'};
                        color: {'#ffffff !important' if is_selected else '#00d2ff !important'};
                        box-shadow: {'0 0 10px rgba(0, 210, 255, 0.4) !important' if is_selected else 'none !important'};
                    }}
                    </style>
                """, unsafe_allow_html=True)
                if st.button(labels[idx], key=f"btn_story_{yr}", use_container_width=True):
                    st.session_state.Subnautica_2_story_year = yr
                    st.rerun()

        st.write("")
        if st.session_state.Subnautica_2_story_year == "2012":
            st.markdown(
                '<div class="Subnautica_2-box" style="border-left: 3px solid #00d2ff;"><div class="Subnautica_2-h1">📂 ARCHIVE_2012 : CRÉATION DE LA CHAÎNE</div><div class="Subnautica_2-p">• 📺 Programmes d\'époque : Le JT & Best-off, L\'OverZone 90\'s.<br>• 🧠 Concepts historiques : Qui veut passer pour un inculte ?, Bureau des Plinthes.</div></div>',
                unsafe_allow_html=True)
        elif st.session_state.Subnautica_2_story_year == "2016":
            st.markdown(
                '<div class="Subnautica_2-box" style="border-left: 3px solid #00d2ff;"><div class="Subnautica_2-h1">📂 ARCHIVE_2016 : ALLIANCE</div><div class="Subnautica_2-p">• Arrivée de Xanna. Début du trio emblématique <br>• Expansion des formats.</div></div>',
                unsafe_allow_html=True)
        elif st.session_state.Subnautica_2_story_year == "2024":
            st.markdown(
                '<div class="Subnautica_2-box" style="border-left: 3px solid #00d2ff;"><div class="Subnautica_2-h1">📂 ARCHIVE_2024 : FR33ZY OVER STUDIO MODERN V1</div><div class="Subnautica_2-p">• 🚀 Refonte graphique intégrale, nouveau logo officiel.<br></div></div>',
                unsafe_allow_html=True)
    else:
        # Configuration de la couleur orange d'origine pour la frise
        dot_color = "#d37c2e"
        dot_hover_color = "#ff8c2e"

        html_timeline_fixed_popups = f"""
        <style>
            .timeline-container {{ font-family: 'Orbitron', sans-serif; color: white; background: #0b0f14; padding: 20px 15px; border-radius: 6px; }}
            .timeline-wrapper {{ display: flex; justify-content: space-between; align-items: flex-start; position: relative; min-width: 600px; }}
            .timeline-line {{ position: absolute; top: 7px; left: 12%; right: 12%; height: 2px; background: #242c34; z-index: 1; }}
            .timeline-node {{ text-align: center; width: 33%; position: relative; z-index: 2; cursor: pointer; }}

            /* RE-CORRECTION DES POINTS ABSENTS POUR LE SITE ORANGE */
            .timeline-dot {{ 
                display: block !important;
                width: 14px !important; 
                height: 14px !important; 
                background-color: {dot_color} !important; 
                border-radius: 50% !important; 
                margin: 0 auto 10px auto !important; 
                position: relative !important;
                z-index: 5 !important;
                box-shadow: 0 0 10px {dot_color}; 
                transition: transform 0.2s ease, background-color 0.2s; 
            }}

            .timeline-node:hover .timeline-dot {{ transform: scale(1.3); background-color: {dot_hover_color} !important; box-shadow: 0 0 15px {dot_hover_color}; }}
            .timeline-year {{ font-weight: bold; color: {dot_color}; font-size: 0.95rem; letter-spacing: 1px; }}
            .timeline-node .popup-box {{ visibility: hidden; width: 260px; background-color: #121820; color: #cbd5e1; text-align: left; border: 1px solid {dot_color}; border-radius: 6px; padding: 12px; position: absolute; z-index: 10; top: 110%; left: 50%; transform: translateX(-50%); opacity: 0; transition: opacity 0.2s ease, transform 0.2s ease; font-family: sans-serif; font-size: 0.8rem; line-height: 1.4; box-shadow: 0 4px 15px rgba(0,0,0,0.6); }}
            .timeline-node .popup-box::after {{ content: ""; position: absolute; bottom: 100%; left: 50%; margin-left: -6px; border-width: 6px; border-style: solid; border-color: transparent transparent {dot_color} transparent; }}
            .popup-title {{ font-family: 'Orbitron', sans-serif; color: {dot_color}; font-weight: bold; margin-bottom: 6px; font-size: 0.85rem; }}
            .timeline-node:hover .popup-box {{ visibility: visible; opacity: 1; transform: translateX(-50%) translateY(5px); }}
        </style>
        <div class="timeline-container">
            <div class="timeline-wrapper">
                <div class="timeline-line"></div>
                <div class="timeline-node">
                    <div class="timeline-dot"></div>
                    <div class="timeline-year">2012</div>
                    <div class="popup-box">
                        <div class="popup-title">🚀 ORIGINES (2012)</div>
                            • 📺 Le JT & Best-off<br>
                            • 📺 L'OverZone 90's<br>
                            • 👍 J'aime / J'aime pas<br>
                            • 🧠 Qui veut passer pour un inculte ?<br>
                            • 🛡️ Bureau des Plinthes
                        </div>
                </div>
                <div class="timeline-node">
                    <div class="timeline-dot"></div>
                    <div class="timeline-year">2016</div>
                    <div class="popup-box">
                        <div class="popup-title">👥 L'ALLIANCE (2016)</div>
                        • Arrivée de Xanna. Début du trio emblématique. <br>
                        • 🎮 Expansion des formats.
                    </div>
                </div>
                <div class="timeline-node">
                    <div class="timeline-dot"></div>
                    <div class="timeline-year">2024</div>
                    <div class="popup-box">
                        <div class="popup-title">⚓ NOUVELLE ÈRE (2024)</div>
                        Transition vers Fr33zy Over Studio (F.O.S).
                    </div>
                </div>
            </div>
        </div>
        """
        st.components.v1.html(html_timeline_fixed_popups, height=220)

    # --- RÉINTÉGRATION DES BLOCS INFERIEURS : AU PROGRAMME & NOTRE VISION ---
    st.markdown('<hr style="border-color: #242c34; margin-top: 30px; margin-bottom: 30px;">', unsafe_allow_html=True)

    col_prog, col_vision = st.columns(2)

    with col_prog:
        st.markdown(f'### 🔥 AU PROGRAMME')
        st.markdown("""
        * **Let's Plays :** Des découvertes sur titres récents et classiques.
        * **Replays Twitch :** Ne manquez rien de nos directs 🎬.
        * **Analyses & News :** Discussions sur les dernières sorties 📰.
        * **Highlights :** Le meilleur du gameplay et des moments forts 🎯.
        """)

    with col_vision:
        st.markdown(f'### 🎯 NOTRE VISION')
        st.markdown(f"""
        <div style="background-color: #121820; border: 1px solid {accent_color}66; border-radius: 6px; padding: 20px; margin-bottom: 20px;">
            <p style="color: #cbd5e1; margin: 0; font-size: 0.95rem; line-height: 1.6;">
            Partager, découvrir et vivre le gaming ensemble. Notre objectif est de fédérer une communauté de passionnés autour d'une aventure humaine et numérique.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("S'ABONNER SUR YOUTUBE", "https://www.youtube.com/@Fr33zyOverStudio", use_container_width=True)

# --- 👥 ONGLET L'ÉQUIPE ---
elif st.session_state.active_tab == "L'ÉQUIPE":

    # SI UN PROFIL INDIVIDUEL EST SÉLECTIONNÉ
    if st.session_state.current_profile:
        nom = st.session_state.current_profile
        m = CREATEURS[nom]

        if st.button("⬅ RETOUR À L'ÉQUIPE"):
            st.session_state.current_profile = None
            st.rerun()

        st.write("")
        accent = "#00d2ff" if st.session_state.theme == "Subnautica_2" else "#d37c2e"
        accent_dim = "rgba(0, 210, 255, 0.4)" if st.session_state.theme == "Subnautica_2" else "#64748b"

        col_avatar, col_infos = st.columns([1, 2])
        with col_avatar:
            st.markdown(
                f'<img src="{m["img"]}" style="width:100%; border-radius:8px; border:3px solid {accent}; box-shadow: 0 0 15px {accent}33;">',
                unsafe_allow_html=True)

        with col_infos:
            st.markdown(
                f"<h1 style='font-family:\"Orbitron\", sans-serif; font-size:3.2rem; font-weight:900; color:white; margin:0;'>{nom.upper()}</h1>",
                unsafe_allow_html=True)
            st.markdown(
                f"<p style='font-family:\"Orbitron\", sans-serif; color:{accent}; font-weight:bold; font-size:1.05rem; margin-top:5px; margin-bottom:10px;'>{m['role'].upper()}</p>",
                unsafe_allow_html=True)

            # --- LES RÉSEAUX SOCIAUX ---
            couleur_liens = "#38bdf8" if st.session_state.theme == "Subnautica_2" else "#d37c2e"

            st.markdown(f"""
                <style>
                .hud-social-container {{
                    display: flex !important;
                    justify-content: center !important;
                    align-items: center !important;
                    width: 100% !important;
                    margin-top: 5px !important;
                    margin-bottom: 15px !important;
                    flex-wrap: wrap !important;
                }}
                .hud-social-link {{
                    color: {couleur_liens} !important;
                    text-decoration: none !important;
                    font-family: 'Orbitron', sans-serif !important;
                    font-weight: bold !important;
                    font-size: 0.82rem !important;
                    letter-spacing: 1.5px !important;
                    transition: color 0.2s ease !important;
                }}
                .hud-social-link:hover {{
                    color: #ffffff !important;
                }}
                .hud-social-dot {{
                    color: #ffffff !important;
                    margin: 0 10px !important;
                    font-size: 0.85rem !important;
                    user-select: none !important;
                }}
                </style>
            """, unsafe_allow_html=True)

            # 1. Ta liste de liens brute (sans ajouter de classe compliquée)
            liens_list = []
            if m['youtube']: liens_list.append(f'<a href="{m["youtube"]}" target="_blank">YOUTUBE</a>')
            if m['twitch']: liens_list.append(f'<a href="{m["twitch"]}" target="_blank">TWITCH</a>')
            if m['instagram']: liens_list.append(f'<a href="{m["instagram"]}" target="_blank">INSTAGRAM</a>')
            if m['threads']: liens_list.append(f'<a href="{m["threads"]}" target="_blank">THREADS</a>')
            if m['discord']: liens_list.append(f'<a href="{m["discord"]}" target="_blank">DISCORD</a>')

            # 2. Le petit triangle blanc pour la séparation
            separateur = " ▾ "

            # 3. La structure HTML qui applique ton style exact au bloc tout en gérant les liens et les séparateurs
            barre_html = f"""
            <style>
                .hud-container-final {{
                    margin: 0;
                    font-size: 0.62rem;
                    letter-spacing: 2px;
                    font-weight: 500;
                    margin-top: 4px;
                    font-family: 'Orbitron', sans-serif;
                    color: #475569; /* Applique le gris uniquement aux petits triangles '▾' */
                    text-align: center; /* ALIGNE TOUT LE BLOC AU MILIEU */
                }}
                .hud-container-final a {{
                    color: inherit; /* Permet au lien de prendre la couleur active du thème ou du texte */
                    text-decoration: underline; /* Garde le soulignement épuré d'origine */
                }}
                .hud-container-final a:hover {{
                    color: #ffffff !important; /* Devient blanc propre au survol */
                }}
            </style>

            <div class="hud-container-final">
                {separateur.join(liens_list)}
            </div>
            """

            # 4. Injection dans ton Streamlit
            st.markdown(barre_html, unsafe_allow_html=True)

            st.markdown(
                f'<hr style="border-color: {accent_dim if st.session_state.theme == "Subnautica_2" else "#242c34"}; margin-top: 5px; margin-bottom: 15px;">',
                unsafe_allow_html=True)

            st.markdown(
                f'<h3 style="font-family:\'Orbitron\', sans-serif; font-size:1.1rem; color:white; margin-bottom:10px;">📝 BIO</h3>',
                unsafe_allow_html=True)
            st.markdown(
                f'<p style="color:#cbd5e1; font-size:0.95rem; line-height:1.6; margin:0; margin-bottom:25px;">{m["desc"]}</p>',
                unsafe_allow_html=True)

            st.markdown(
                f"<p style='font-size:0.75rem; color:{accent_dim}; font-weight:bold; font-family:\"Orbitron\", sans-serif; letter-spacing:1px; margin-bottom:12px;'>SÉRIES PHARES (YOUTUBE)</p>",
                unsafe_allow_html=True)

            nb_series = len(m["series"])
            if nb_series > 0:
                cols_grid = st.columns(2)
                for idx, (titre_serie, url_serie) in enumerate(m["series"]):
                    with cols_grid[idx % 2]:
                        st.link_button(titre_serie, url_serie, use_container_width=True)

            st.write("")
            st.markdown(
                f"<p style='font-size:0.75rem; color:{accent_dim}; font-weight:bold; font-family:\"Orbitron\", sans-serif; letter-spacing:1px; margin-bottom:5px;'>JEUX DU MOMENT</p>",
                unsafe_allow_html=True)
            st.markdown(f"<p style='color:white; font-size:0.95rem; font-weight:500; margin:0;'>{m['jeux']}</p>",
                        unsafe_allow_html=True)

        st.write("")
        st.markdown(
            f"<h3 style='font-family:\"Orbitron\", sans-serif; font-size:1.1rem; color:white; margin-bottom:15px;'>🗓️ PLANNING DE {nom.upper()}</h3>",
            unsafe_allow_html=True)
        st.link_button(m["planning_text"], m["planning_url"], use_container_width=True)

    # RESTE DE L'ONGLET L'ÉQUIPE GÉNÉRAL
    else:
        st.markdown('<h3 style="font-family:\'Orbitron\', sans-serif; font-weight:500;">🎬 NOTRE ÉQUIPE</h3>',
                    unsafe_allow_html=True)
        liste_membres = list(CREATEURS.items())

        for i in range(0, len(liste_membres), 3):
            groupe_de_3 = liste_membres[i:i + 3]
            cols = st.columns(3)

            for idx, (nom_membre, info) in enumerate(groupe_de_3):
                with cols[idx]:
                    accent_txt = "#00d2ff" if st.session_state.theme == "Subnautica_2" else "#d37c2e"
                    st.markdown(f"""<div class="member-card">
                        <img src="{info["img"]}" width="100" height="100" style="border-radius:6px; border:1px solid #242c34; margin-bottom:15px; object-fit: cover;">
                        <h4 style="color:white; font-family:'Orbitron', sans-serif; margin:5px 0;">{nom_membre}</h4>
                        <p style="color:{accent_txt}; font-size:0.8rem; font-weight:bold; margin-bottom:15px;">{info["role"]}</p>
                        </div>""", unsafe_allow_html=True)
                    st.write("")
                    if st.button("VOIR LE PROFIL", key=f"profile_view_{nom_membre}", use_container_width=True):
                        st.session_state.current_profile = nom_membre
                        st.rerun()

# =========================================================================
# 📁 ONGLET : PROJETS
# =========================================================================
elif st.session_state.active_tab == "PROJETS":
    st.markdown(f'### 📂 NOS PROJETS & VISION')

    if st.session_state.theme == Subnautica_2
        cols_p = st.columns(3)
        proj_milestones = [("2024", "🌐 SITE V1"), ("2025", "🎬 CROSSOVER"), ("2026", "🛒 SHOP")]
        for idx, (yr, label) in enumerate(proj_milestones):
            with cols_p[idx]:
                if st.button(label, key=f"proj_btn_{yr}", use_container_width=True):
                    st.session_state.subnautica_project_year = yr
        
        st.write("")
        p_texts = {
            "2024": "Déploiement du PDA interactif Streamlit pour centraliser l'équipe.",
            "2025": "Lancement des premières séries collaboratives unifiées entre membres.",
            "2026": "Ouverture de la boutique officielle Fr33zy Over Studio."
        }
        st.markdown(f'<div class="subnautica-box"><b>OBJECTIF_{st.session_state.subnautica_project_year} :</b><br>{p_texts[st.session_state.subnautica_project_year]}</div>', unsafe_allow_html=True)

    # 🎯 CORRECTION ICI : On utilise 'elif' au lieu de 'else' pour ne pas bloquer les onglets suivants
    elif st.session_state.theme != NOM_THEME_CYAN:
        dot_color = "#d37c2e"
        html_v_timeline = f"""
        <style>
            .tl-v-cont {{ 
                position: relative; 
                padding: 20px 40px; 
                background: transparent; 
                font-family: sans-serif; 
            }}
            .tl-v-line {{ position: absolute; top: 10px; bottom: 10px; left: 46px; width: 2px; background: #242c34; }}
            .tl-v-node {{ position: relative; padding-left: 40px; margin-bottom: 40px; }}
            .tl-v-dot {{ position: absolute; left: 0; top: 4px; width: 14px; height: 14px; background: {dot_color}; border-radius: 50%; box-shadow: 0 0 10px {dot_color}; z-index: 2; }}
            .tl-v-year {{ color: {dot_color}; font-weight: bold; margin-bottom: 5px; font-size: 1rem; }}
            .tl-v-desc {{ color: #cbd5e1; font-family: sans-serif; font-size: 0.9rem; line-height: 1.4; max-width: 500px; }}
        </style>
        <div class="tl-v-cont"><div class="tl-v-line"></div>
            <div class="tl-v-node"><div class="tl-v-dot"></div><div class="tl-v-year">2026</div><div class="tl-v-desc"><b>SITE WEB V1 :</b> Lancement du Hub communautaire, du shop et de l'expérience membre. C'est l'objectif actuel !</div></div>
            <div class="tl-v-node"><div class="tl-v-dot"></div><div class="tl-v-year">2024</div><div class="tl-v-desc"><b>TRANSITION :</b> Over_1 vers Fr33zy Over Studio pour une identity plus forte.</div></div>
        </div>
        """
        components.html(html_v_timeline, height=250)

# --- 👥 ONGLET L'ÉQUIPE ---
elif st.session_state.active_tab == "L'ÉQUIPE":
    if st.session_state.current_profile:
        nom = st.session_state.current_profile
        m = CREATEURS[nom]
        if st.button("⬅ RETOUR"):
            st.session_state.current_profile = None
            st.rerun()

        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(m["img"], use_container_width=True)
        with col2:
            st.title(nom.upper())
            st.subheader(m["role"])
            st.write(m["desc"])
            st.write(f"🎮 **Jeux :** {m['jeux']}")
    else:
        st.markdown('### 🎬 NOTRE ÉQUIPE')
        cols = st.columns(2)
        for i, (nom, info) in enumerate(CREATEURS.items()):
            with cols[i % 2]:
                st.markdown(f'<div class="member-card"><h4>{nom}</h4><p>{info["role"]}</p></div>',
                            unsafe_allow_html=True)
                if st.button(f"VOIR {nom.upper()}", key=nom):
                    st.session_state.current_profile = nom
                    st.rerun()

# =========================================================================
# 📩 ONGLET : PHOTOS
# =========================================================================
elif st.session_state.active_tab == "PHOTOS":
    st.subheader("📸 GALERIE F.O.S")
    st.write("Retrouvez ici les moments forts du studio et nos visuels officiels.")

    # On crée des colonnes pour organiser les photos
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://via.placeholder.com/400x300", caption="Moment culte #1", use_container_width=True)
        st.image("https://via.placeholder.com/400x500", caption="Le Studio en 2024", use_container_width=True)

    with col2:
        st.image("https://via.placeholder.com/400x600", caption="Setup Stream", use_container_width=True)
        st.image("https://via.placeholder.com/400x300", caption="Logo Over_1 (Archives)", use_container_width=True)

    with col3:
        st.image("https://via.placeholder.com/400x300", caption="Xanna & Fr33zy", use_container_width=True)
        st.image("https://via.placeholder.com/400x400", caption="Projet 2026", use_container_width=True)

    # Petite astuce : tu peux aussi ajouter un bouton pour ouvrir ton Instagram ou Flickr
    st.divider()
    st.link_button("Voir plus de photos sur Instagram", "https://instagram.com/ton_compte")

# =========================================================================
# 📩 ONGLET : CONTACT (REMIS EN PLACE ET CORRIGÉ)
# =========================================================================
elif st.session_state.active_tab == "CONTACT":
    st.markdown('### 📥 NOUS CONTACTER')

    col_mail, col_discord = st.columns(2)

    with col_mail:
        st.markdown('### 📧 EMAIL')
        st.link_button("CONTACTER PAR EMAIL", "mailto:contact.fr33zy0verstudio@gmail.com", use_container_width=True)

    with col_discord:
        st.markdown('### 💬 COMMUNAUTÉ')
        st.link_button("REJOINDRE LE DISCORD", "https://discord.gg/h4r2MSgJSk", use_container_width=True)

# --- 🛒 LES AUTRES ONGLETS ---
elif st.session_state.active_tab == "SHOP" or st.session_state.active_tab == "DON":
    st.subheader(f"💎 {st.session_state.active_tab}")
    st.info("🚀 Ce module est en cours de construction. Revenez très bientôt !")

    # Bloc de maintenance visuel (comme DON)
    st.markdown("""
            <div style="text-align: center; padding: 40px; border: 1px dashed #30363d; border-radius: 10px; opacity: 0.6; margin-top:20px;">
                <p style="font-size: 1.2rem; color: #e67e22;">🚧 MODULE EN CONSTRUCTION 🚧</p>
                <p style="font-size: 0.9rem;">Nous sélectionnons les meilleurs produits pour vous garantir une qualité premium.</p>
            </div>
        """, unsafe_allow_html=True)

    # Injection CSS pour forcer l'alignement des gros boutons d'action du bas en Cyan permanent
    st.markdown("""
        <style>
        /* On isole l'ID de la zone basse pour appliquer le cyan aux boutons d'action */
        .cyan-action-box button, .cyan-action-box a {
            border: 1px solid rgba(0, 210, 255, 0.4) !important;
            color: #00d2ff !important;
        }
        .cyan-action-box button:hover, .cyan-action-box a:hover {
            border-color: #00d2ff !important;
            box-shadow: 0 0 12px rgba(0, 210, 255, 0.4) !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)


# --- ✉️ ONGLET CONTACT ---
elif st.session_state.active_tab == "CONTACT":
    st.markdown('<h3 style="font-family:\'Orbitron\', sans-serif; font-weight:500;">📩 NOUS CONTACTER</h3>',
                unsafe_allow_html=True)
    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<h4 style="font-family:\'Orbitron\', sans-serif; font-weight:500;">📧 EMAIL</h4>',
                    unsafe_allow_html=True)
        st.link_button("CONTACTER PAR EMAIL", "mailto:contact.fr33zy0verstudio@gmail.com", use_container_width=True)
    with c2:
        st.markdown('<h4 style="font-family:\'Orbitron\', sans-serif; font-weight:500;">💬 COMMUNAUTÉ</h4>',
                    unsafe_allow_html=True)
        st.link_button("REJOINDRE LE DISCORD", "https://discord.gg/h4r2MSgJSk", use_container_width=True)


# --- 🛍️ ONGLET SHOP (AVEC LA STRUCTURATION REPRODUITE) ---
elif st.session_state.active_tab == "SHOP" or st.session_state.active_tab == "DON":
    st.subheader(f"💎 {st.session_state.active_tab}")
    st.info("🚀 Ce module est en cours de construction. Revenez très bientôt !")

    # Bloc de maintenance visuel (comme DON)
    st.markdown("""
            <div style="text-align: center; padding: 40px; border: 1px dashed #30363d; border-radius: 10px; opacity: 0.6; margin-top:20px;">
                <p style="font-size: 1.2rem; color: #e67e22;">🚧 MODULE EN CONSTRUCTION 🚧</p>
                <p style="font-size: 0.9rem;">Nous sélectionnons les meilleurs produits pour vous garantir une qualité premium.</p>
            </div>
        """, unsafe_allow_html=True)

# =========================================================================
# ⚙️ FOOTER TECHNIQUE & SÉLECTEUR DE THÈME (TEXTE À GAUCHE / BOUTON À DROITE)
# =========================================================================
st.markdown("<br><hr style='border-color: #242c34; margin-bottom: 20px;'>", unsafe_allow_html=True)

# Division de l'espace : la grosse partie pour le texte à gauche (8), la petite pour le bouton à droite (2)
col_footer_txt, col_footer_btn = st.columns([8, 2])

with col_footer_txt:
    # Changement dynamique de la couleur du nom du studio selon le thème actif
    current_accent = "#00d2ff" if st.session_state.theme == "Subnautica_2" else "#d37c2e"

    st.markdown(f"""
        <div style="text-align: left; font-family: 'Orbitron', sans-serif; line-height: 1.8;">
            <p style="margin: 0; font-size: 0.88rem; font-weight: bold; letter-spacing: 0.5px;">
                <span style="color: #ffffff;">{LICENSE_TEXT_WHITE}</span><span style="color: {current_accent};">{STUDIO_NAME}</span>
                <span style="color: #475569; font-size: 0.72rem; font-weight: normal; margin-left: 8px; font-family: sans-serif;">{VERSION}</span>
            </p>
            <p style="margin: 0; font-size: 0.62rem; color: #475569; letter-spacing: 2px; font-weight: 500; margin-top: 4px;">
                {TOOLS}
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_footer_btn:
    # Le menu déroulant du thème s'affiche ici, aligné tout à droite
    theme_choice = st.selectbox("Ambiance :", ["Orange", "Subnautica_2"],
                                index=0 if st.session_state.theme == "Orange" else 1, label_visibility="collapsed")
    if theme_choice != st.session_state.theme:
        st.session_state.theme = theme_choice
        st.rerun()
