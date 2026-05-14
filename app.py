import streamlit as st
import streamlit.components.v1 as components  # Ajout crucial pour les timelines

# --- DEFINITION DES INFOS TECHNIQUES ---
VERSION = "0.0.1"
LICENSE = "© 2026 FR33ZY OVER STUDIO - TOUS DROITS RÉSERVÉS"
TOOLS = "POWERED BY OBS STUDIO • DAVINCI RESOLVE • KDENLIVE • PHOTOSHOP • GIMP • STREAMLIT • "

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Fr33zy Over Studio",
    page_icon="logo_officiel-FOS.png",
    layout="wide"
)

# --- INITIALISATION DU SESSION STATE ---
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "QUI SOMMES-NOUS"
if 'current_profile' not in st.session_state:
    st.session_state.current_profile = None

# --- STYLE CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: white; }
    .main-title { 
        color: #e67e22; text-align: center; font-weight: 800; 
        font-size: 3.5rem; margin-bottom: 20px;
    }
    .stButton > button, .stLinkButton > a, .custom-button-link {
        border: 1px solid #30363d !important;
        background-color: #1c2128 !important;
        color: #e67e22 !important;
        transition: all 0.3s ease !important;
        height: 50px !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: bold !important;
        border-radius: 5px !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
        font-size: 0.9rem !important;
    }
    .stButton > button:hover, .stLinkButton > a:hover, .custom-button-link:hover {
        border-color: #ff6600 !important;
        box-shadow: 0 0 15px rgba(255, 102, 0, 0.4) !important;
        color: white !important;
    }
    .member-card {
        background: #161b22; 
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 25px 15px; 
        text-align: center; 
        margin-top: 20px;
        transition: transform 0.3s ease;
    }
    .member-card:hover {
        border-color: #e67e22;
        transform: translateY(-5px);
    }
    .network-bar {
        text-align: center; margin-top: 10px; 
        border-bottom: 1px solid #30363d; padding-bottom: 20px;
        margin-bottom: 20px;
    }
    .network-link {
        color: white; text-decoration: none; letter-spacing: 3px; 
        font-size: 0.8rem; font-weight: 300; opacity: 0.7; transition: 0.3s;
    }
    .network-link:hover { opacity: 1; color: #e67e22; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">FR33ZY OVER STUDIO</h1>', unsafe_allow_html=True)

# --- BASE DE DONNÉES ---
CREATEURS = {
    "Firnaeth": {
        "role": "Founding Member / Streameur",
        "img": "https://unavatar.io/youtube/firnaethYT",
        "desc": "Animateur à l'imagination débridée et fondateur du studio, je vous embarque dans un courant chaotique entre pixels, créations animées et réflexions absurdes. 🦴🌊",
        "jeux": ["Silent Hill 2", "The Elder Scrolls V: Skyrim", "Medieval Crafter: Blacksmith"],
        "series": [
            {"nom": "📜 Journal d’un forge-lol 🔨",
             "url": "https://youtube.com/playlist?list=PLgX-3H3ACJk5Rb3whj-89ANDgMXN-iaBf"},
            {"nom": "Lura : L’Héritière des Forges",
             "url": "https://www.youtube.com/playlist?list=PLgX-3H3ACJk40I098msu4YsPFX5fNPRDO"},
            {"nom": "Chroniques De Silent Hill 2",
             "url": "https://www.youtube.com/playlist?list=PLgX-3H3ACJk7l33I2euw_yEPJ7a4JEVx9"},
            {"nom": "Underground Garage",
             "url": "https://www.youtube.com/playlist?list=PLgX-3H3ACJk6exfv_mzqJ-IKSZJbhFuNe"}
        ],
        "liens": "https://www.youtube.com/@firnaethYT",
        "twitch_id": "firnaeth",
        "insta": "https://instagram.com/firnaeth_yt",
        "thread_url": "https://www.threads.com/@firnaeth_yt",
        "discord": "https://discord.gg/votrelien",
    },
    "NICO LE GEEK": {
        "role": "Founding Member / Geek",
        "img": "https://unavatar.io/youtube/NICOLEGEEK",
        "desc": "Un vrai mordu de culture geek, grand collectionneur de consoles et de jeux rétro. Toujours prêt pour une partie sur les classiques qui ont marqué l'histoire.",
        "jeux": ["Retro Gaming", ""],
        "series": [
            {"nom": "LE BUREAU DES PLINTHES",
             "url": "https://youtube.com/playlist?list=PLkBX3VXLbjxjTAXJeaohmW9G-F9Wne1c3"}
        ],
        "liens": "https://www.youtube.com/@NICOLEGEEK",
        "twitch_id": None,
        "discord": "https://discord.gg/votrelien",
    },
    "Xanna La Nooblette": {
        "role": "Founding Member / Streameuse",
        "img": "https://unavatar.io/youtube/xannalanooblette",
        "desc": "Entre humour, fails épiques et aventures virtuelles, je transforme mes galères en gameplay pour vous offrir le meilleur du gaming (et du gâteau) avec style ! 🍰🎮",
        "jeux": ["Slime Rancher 2", "The Elder Scrolls V: Skyrim"],
        "series": [
            {"nom": "Subnautica",
             "url": "https://www.youtube.com/playlist?list=PLD-GVWgeEc6cWHG8Cg0liIoEaluph5mS0"},
            {"nom": "L'Épopée Féline",
             "url": "https://www.youtube.com/playlist?list=PLD-GVWgeEc6fCdkCXg38Bcw7fm9YZcuzV"},
            {"nom": "Crime Scene Cleaner",
             "url": "https://www.youtube.com/playlist?list=PLD-GVWgeEc6dfycSPIsT9LmSuAa4rlSx9"},
            {"nom": "Slime Rancher 2",
             "url": "https://www.youtube.com/playlist?list=PLD-GVWgeEc6diG7X1purupOBtHJqrZwnx"}
        ],
        "liens": "https://www.youtube.com/@xannalanooblette",
        "twitch_id": "xannalanooblette",
        "insta": "https://instagram.com/xannalasedistemaispastrop",
        "discord": "https://discord.gg/votrelien",
    }
}

# --- NAVIGATION (MISE À JOUR : 6 COLONNES) ---
st.write("---")
cols_nav = st.columns(6)  # Changé de 4 à 7
btns = ["QUI SOMMES-NOUS", "L'ÉQUIPE", "PROJETS", "SHOP", "CONTACT", "DON"] # "PHOTOS" est caché ici
for i, btn in enumerate(btns):
    with cols_nav[i]:
        if st.button(btn, key=f"nav_{btn}", use_container_width=True):
            st.session_state.active_tab = btn
            st.session_state.current_profile = None
            st.rerun()
st.write("---")

# --- LOGIQUE DES PAGES ---

if st.session_state.current_profile:
    nom = st.session_state.current_profile
    m = CREATEURS[nom]

    if st.button("⬅ RETOUR À L'ÉQUIPE"):
        st.session_state.current_profile = None
        st.rerun()

    st.write("")
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown(f'<img src="{m["img"]}" style="border-radius:20px; width:100%; border:1px solid #30363d;">',
                    unsafe_allow_html=True)
    with c2:
        st.markdown(f"<h1 style='color:white; margin-bottom:0; font-size:4rem;'>{nom.upper()}</h1>",
                    unsafe_allow_html=True)
        st.markdown(
            f"<p style='font-size:1.4rem; color:#e67e22; font-weight:bold; margin-top:-10px;'>{m['role'].upper()}</p>",
            unsafe_allow_html=True)

        # 1. RÉSEAUX
        liens_html = []
        if m.get('liens'): liens_html.append(f'<a href="{m["liens"]}" class="network-link" target="_blank">YOUTUBE</a>')
        if m.get('twitch_id'): liens_html.append(
            f'<a href="https://twitch.tv/{m["twitch_id"]}" class="network-link" target="_blank">TWITCH</a>')
        if m.get('insta'): liens_html.append(
            f'<a href="{m["insta"]}" class="network-link" target="_blank">INSTAGRAM</a>')
        if m.get('thread_url'): liens_html.append(
            f'<a href="{m["thread_url"]}" class="network-link" target="_blank">THREADS</a>')
        if m.get('discord'): liens_html.append(
            f'<a href="{m["discord"]}" class="network-link" target="_blank">DISCORD</a>')
        if liens_html:
            st.markdown(f'<div class="network-bar">' + " &nbsp; &bull; &nbsp; ".join(liens_html) + '</div>',
                        unsafe_allow_html=True)

        # 2. BIO
        st.markdown(f"### 📝 BIO\n{m['desc']}")

        # 3. NOUVEAU : SÉRIES PHARES (YOUTUBE)
        if m.get('series'):
            st.write("")
            st.markdown(f"<p style='color:#8b949e; font-size:0.8rem; margin-bottom:10px;'>SÉRIES PHARES (YOUTUBE)</p>",
                        unsafe_allow_html=True)
            # Affichage des séries sur deux colonnes pour gagner de la place
            cols_s = st.columns(2)
            for idx, serie in enumerate(m['series']):
                with cols_s[idx % 2]:
                    st.link_button(serie['nom'], serie['url'], use_container_width=True)

        # 4. JEUX DU MOMENT
        st.divider()
        st.markdown(
            f"<p style='color:#8b949e; font-size:0.8rem; margin-bottom:0;'>JEUX DU MOMENT</p><p style='font-size:1.1rem; font-weight:bold;'>{', '.join(m['jeux'])}</p>",
            unsafe_allow_html=True)

    # --- NICOG33K ---
    if nom == "NICOLEGEEK":
        st.subheader("📅 PLANNING & ACTUALITÉS")
        st.write(
            "NicoleGeek n'a pas de planning de stream fixe, mais il est très actif sur YouTube pour vous présenter ses dernières trouvailles rétro et ses consoles de collection !")

        st.markdown(f'''
            <a href="{m["liens"]}" target="_blank" style="text-decoration: none;">
                <div class="custom-button-link">
                    VOIR SES VIDÉOS SUR YOUTUBE
                </div>
            </a>
        ''', unsafe_allow_html=True)

    elif m.get('twitch_id'):
        st.subheader(f"📅 PLANNING DE {nom.upper()}")
        st.link_button(f"VOIR LE PLANNING SUR TWITCH", f"https://www.twitch.tv/{m['twitch_id']}/schedule",
                       use_container_width=True)
        st.markdown(
            f'<iframe src="https://www.twitch.tv/popout/{m["twitch_id"]}/schedule" height="600" width="100%" frameborder="0"></iframe>',
            unsafe_allow_html=True)

    else:
        st.subheader("📅 PLANNING")
        st.write("Planning bientôt disponible pour ce membre.")

elif st.session_state.active_tab == "L'ÉQUIPE":
    st.subheader("🎬 NOTRE ÉQUIPE")
    cols = st.columns(3)
    for i, (nom, info) in enumerate(CREATEURS.items()):
        with cols[i]:
            st.markdown(f"""<div class="member-card">
                <img src="{info["img"]}" class="img-profile-card" width="110" height="110">
                <h4 style="color:white; margin-bottom:5px;">{nom}</h4>
                <p style="color:#e67e22; font-size:0.85rem; font-weight:bold;">{info["role"]}</p>
                </div>""", unsafe_allow_html=True)
            st.write("")
            if st.button("VOIR LE PROFIL", key=f"btn_{nom}", use_container_width=True):
                st.session_state.current_profile = nom
                st.rerun()

elif st.session_state.active_tab == "CONTACT":
    st.subheader("📩 NOUS CONTACTER")
    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 📧 EMAIL")
        st.markdown(
            '<a href="mailto:contact.fr33zy0verstudio@gmail.com" class="custom-button-link">CONTACTER PAR EMAIL</a>',
            unsafe_allow_html=True)
    with c2:
        st.markdown("### 💬 COMMUNAUTÉ")
        st.link_button("REJOINDRE LE DISCORD", "https://discord.gg/h4r2MSgJSk", use_container_width=True)

# --- DANS LA SECTION : QUI SOMMES-NOUS ---
elif st.session_state.active_tab == "QUI SOMMES-NOUS":
    st.subheader("NOTRE HISTOIRE")
    st.markdown("""
        <div style="background: #161b22; padding: 30px; border-radius: 15px; border: 1px solid #30363d; margin-bottom: 20px;">
            <h2 style="color: #e67e22; margin-top: 0;">BIENVENUE CHEZ FR33ZY OVER STUDIO</h2>
            <p style="font-size: 1.1rem; line-height: 1.6; color: #e1e4e8;">
                Depuis 2012, nous partageons notre passion pour l'univers du gaming, notre équipe évolue pour vous proposer une expérience communautaire unique, mêlant expertise technique et amour du jeu</b>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- PAGE : QUI SOMMES-NOUS (Style Image + Pop-up interactive) ---
    if st.session_state.active_tab == "QUI SOMMES-NOUS":
        st.subheader("📜 NOTRE PARCOURS !")

        html_timeline = """
            <style>
                .timeline-container { 
                    background-color: #0d1117; 
                    padding: 80px 15px; /* Plus d'espace en haut pour la pop-up */
                    font-family: sans-serif; 
                }
                .timeline-wrapper { 
                    position: relative; 
                    width: 100%; 
                    max-width: 1500px; 
                    margin: 0 auto; 
                    display: flex; 
                    justify-content: space-between; 
                }

                .line { 
                    position: absolute; 
                    top: 12px; 
                    left: 0; 
                    right: 0; 
                    height: 4px; 
                    background: #e67e22; 
                    z-index: 1; 
                }

                .step { 
                    z-index: 5; 
                    position: relative; 
                    display: flex; 
                    flex-direction: column; 
                    align-items: center; 
                    flex: 1; 
                }

                .dot { 
                    width: 22px; 
                    height: 22px; 
                    background: #0d1117; 
                    border: 4px solid #e67e22; 
                    border-radius: 50%; 
                    outline: 8px solid #0d1117; 
                    transition: all 0.3s ease;
                    cursor: pointer;
                }

                /* Effet au survol du point ou de la carte */
                .step:hover .dot { 
                    background: #e67e22; 
                    transform: scale(1.3); 
                }

                .card {
                    margin-top: 40px; 
                    width: 85%; 
                    background: #161b22; 
                    border: 1px solid #30363d; 
                    border-radius: 8px; 
                    padding: 15px; 
                    text-align: center; 
                    transition: 0.3s;
                    cursor: pointer;
                }
                .step:hover .card { border-color: #e67e22; }
                .card b { color: #e67e22; display: block; font-size: 1.1rem; }
                .card span { color: #8b949e; font-size: 0.85rem; }

                /* LA POP-UP (Correction de la visibilité) */
                .popup {
                    position: absolute;
                    bottom: 60px; /* Positionnée au-dessus du point */
                    left: 50%;
                    transform: translateX(-50%) translateY(10px);
                    width: 260px;
                    background-color: #1c2128;
                    color: #fff;
                    border: 1px solid #e67e22;
                    border-radius: 8px;
                    padding: 15px;
                    font-size: 0.85rem;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.8);
                    z-index: 9999; /* Force l'affichage au premier plan */
                    opacity: 0;
                    visibility: hidden;
                    transition: all 0.3s ease;
                    pointer-events: none; /* Évite de bloquer la souris */
                }

                /* Affichage lors du survol de TOUTE l'étape */
                .step:hover .popup {
                    opacity: 1;
                    visibility: visible;
                    transform: translateX(-50%) translateY(0px);
                }

                /* Triangle */
                .popup::after {
                    content: "";
                    position: absolute;
                    top: 100%;
                    left: 50%;
                    margin-left: -5px;
                    border-width: 5px;
                    border-style: solid;
                    border-color: #e67e22 transparent transparent transparent;
                }
            </style>

            <div class="timeline-container">
                <div class="timeline-wrapper">
                    <div class="line"></div>

                    <div class="step">
                        <div class="popup">
                            <b style="color:#e67e22">PROGRAMMES 2012</b><br><br>
                            • 📺 Le JT & Best-off<br>
                            • 📺 L'OverZone 90's<br>
                            • 👍 J'aime / J'aime pas<br>
                            • 🧠 Qui veut passer pour un inculte ?<br>
                            • 🛡️ Bureau des Plinthes
                        </div>
                        <div class="dot"></div>
                        <div class="card"><b>2012</b><span>Création d'Over_1</span></div>
                    </div>

                    <div class="step">
                        <div class="popup">
                            <b style="color:#e67e22">L'ALLIANCE</b><br><br>
                            Arrivée de Xanna. Début du trio emblématique et expansion des formats.
                        </div>
                        <div class="dot"></div>
                        <div class="card"><b>2016</b><span>+1, Xanna La Nooblette</span></div>
                    </div>

                    <div class="step">
                        <div class="popup">
                            <b style="color:#e67e22">NOUVELLE ÈRE</b><br><br>
                            Transition vers Fr33zy Over Studio (F.O.S).
                        </div>
                        <div class="dot"></div>
                        <div class="card"><b>2024</b><span>Over_1 => F.O.S</span></div>
                    </div>

                    <div class="step">
                        <div class="popup">
                            <b style="color:#e67e22">OBJECTIF 2026</b><br><br>
                            Lancement du Site et du Hub Communautaire.
                        </div>
                        <div class="dot" style="background: #e67e22;"></div>
                        <div class="card" style="border-color: #e67e22;"><b>2026</b><span>Site Officiel</span></div>
                    </div>

                </div>
            </div>
            """
        components.html(html_timeline, height=320)

    col_content, col_goal = st.columns(2)
    with col_content:
        st.markdown("### 🔥 AU PROGRAMME")
        st.markdown("""
        - **Let’s Plays** : Des découvertes sur titres récents et classiques.
        - **Replays Twitch** : Ne manquez rien de nos directs 📡.
        - **Analyses & News** : Discussions sur les dernières sorties 🆕.
        - **Highlights** : Le meilleur du gameplay et des moments forts 🎯.
        """)

    with col_goal:
        st.markdown("### 🎯 NOTRE VISION")
        st.info(
            "Partager, découvrir et vivre le gaming ensemble. Notre objectif est de fédérer une communauté de passionnés autour d'une aventure humaine et numérique.")
        st.write("")
        st.markdown(
            '<a href="https://www.youtube.com/@Fr33zyOverStudio" class="custom-button-link">S\'ABONNER SUR YOUTUBE</a>',
            unsafe_allow_html=True)

elif st.session_state.active_tab == "PROJETS":
    st.subheader("🚀 NOS PROJETS & VISION")
    st.info("🚀 Ce module est en cours de construction. Revenez très bientôt !")

    st.markdown(
        '<div style="text-align: center;"><h4>"Construire l\'avenir de la communauté, un pixel à la fois."</h4></div>',
        unsafe_allow_html=True)

    html_vertical_inverted_dates = """
        <style>
            .main-container {
                display: flex;
                justify-content: center;
                background-color: #0d1117;
                padding: 40px 0;
                font-family: sans-serif;
                position: relative;
            }

            .v-line {
                position: absolute;
                left: 50%;
                transform: translateX(-50%);
                top: 0;
                bottom: 0;
                width: 4px;
                background: #e67e22;
                z-index: 1;
            }

            .v-wrapper {
                width: 100%;
                max-width: 900px;
                display: flex;
                flex-direction: column;
                gap: 50px;
            }

            .v-step {
                display: flex;
                align-items: center;
                width: 100%;
                position: relative;
                z-index: 2;
            }

            .v-dot {
                position: absolute;
                left: 50%;
                transform: translateX(-50%);
                width: 20px;
                height: 20px;
                background: #0d1117;
                border: 4px solid #e67e22;
                border-radius: 50%;
                outline: 8px solid #0d1117;
                transition: 0.3s;
            }
            .v-step:hover .v-dot {
                background: #e67e22;
                transform: translateX(-50%) scale(1.3);
            }

            .v-card {
                width: 40%;
                margin-right: auto;
                background: #161b22;
                border: 1px solid #30363d;
                border-radius: 8px;
                padding: 15px;
                text-align: right;
                transition: 0.3s;
                cursor: pointer;
            }
            .v-step:hover .v-card {
                border-color: #e67e22;
            }
            .v-card b { color: #e67e22; display: block; font-size: 1.1rem; }
            .v-card span { color: #8b949e; font-size: 0.85rem; }

            .v-popup {
                position: absolute;
                left: 55%;
                width: 280px;
                background: #1c2128;
                border: 1px solid #e67e22;
                border-radius: 8px;
                padding: 15px;
                color: white;
                font-size: 0.85rem;
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease;
                box-shadow: 0 5px 15px rgba(0,0,0,0.5);
                transform: translateX(20px);
            }
            .v-step:hover .v-popup {
                visibility: visible;
                opacity: 1;
                transform: translateX(0px);
            }

            .v-popup::before {
                content: "";
                position: absolute;
                top: 15px;
                right: 100%;
                border-width: 8px;
                border-style: solid;
                border-color: transparent #e67e22 transparent transparent;
            }
        </style>

        <div class="main-container">
            <div class="v-line"></div>
            <div class="v-wrapper">

                <!-- 2026 (EN HAUT MAINTENANT) -->
                <div class="v-step">
                    <div class="v-card" style="border-color: #e67e22;"><b>2026</b><span>Site Officiel</span></div>
                    <div class="v-dot" style="background: #e67e22;"></div>
                    <div class="v-popup">
                        <b>VISION 2026 :</b><br>
                        Lancement du Hub communautaire, du shop et de l'expérience membre. C'est l'objectif actuel !
                    </div>
                </div>

                <!-- 2024 -->
                <div class="v-step">
                    <div class="v-card"><b>2024</b><span>Over_1 => F.O.S</span></div>
                    <div class="v-dot"></div>
                    <div class="v-popup">
                        <b>REBRANDING :</b><br>
                        Transition vers Fr33zy Over Studio pour une identité plus forte.
                    </div>
                </div>

            </div>
        </div>
        """
    components.html(html_vertical_inverted_dates, height=700)

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

elif st.session_state.active_tab == "CONTACT":
    st.subheader("📩 NOUS CONTACTER")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<a href="mailto:contact@fr33zyoverstudio.fr" class="custom-button-link">CONTACT PAR EMAIL</a>',
                    unsafe_allow_html=True)
    with c2:
        st.link_button("REJOINDRE LE DISCORD", "https://discord.gg/h4r2MSgJSk", use_container_width=True)

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

st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; padding-top: 30px; border-top: 1px solid #30363d;">
        <p style="font-size: 0.9rem; color: white; margin-bottom: 5px; font-weight: 500;">
            © 2026 <span style="color: #e67e22; font-weight: bold;">FR33ZY OVER STUDIO</span>.
            <span style="color: #8b949e; font-size: 0.7rem; font-weight: normal; margin-left: 10px;">v{VERSION}</span>
        </p>
        <p style="font-size: 0.65rem; letter-spacing: 2px; color: #8b949e; text-transform: uppercase; opacity: 0.6;">
            {TOOLS}
        </p>
    </div>
""", unsafe_allow_html=True)
