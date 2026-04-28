import streamlit as st

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Fr33zy Over Studio",
    page_icon="logo_officiel-FOS.png",  # Doit être identique au nom du fichier sur GitHub
    layout="wide"
)

# --- INITIALISATION DU SESSION STATE ---
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "QUI SOMMES-NOUS"
if 'current_profile' not in st.session_state:
    st.session_state.current_profile = None

# --- STYLE CSS (HARMONISATION TOTALE) ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: white; }
    .main-title { 
        color: #e67e22; text-align: center; font-weight: 800; 
        font-size: 3.5rem; margin-bottom: 20px;
    }

    /* STYLE UNIQUE POUR TOUS LES BOUTONS */
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
        background: #161b22; border: 1px solid #30363d;
        border-top: 4px solid #e67e22; border-radius: 12px;
        padding: 25px 10px; text-align: center; margin-top: 20px;
    }
    .img-profile-card {
        border-radius: 50%; border: 2px solid #30363d;
        margin-bottom: 15px; object-fit: cover;
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

# --- BASE DE DONNÉES (MISE À JOUR AVEC SÉRIES) ---
CREATEURS = {
    "Firnaeth": {
        "role": "Founding Member / Streameur",
        "img": "https://unavatar.io/youtube/firnaethYT",
        "desc": "Animateur à l'imagination débridée et fondateur du studio, je vous embarque dans un courant chaotique entre pixels, créations animées et réflexions absurdes. 🦴🌊",
        "jeux": ["Silent Hill 2", "The Elder Scrolls V: Skyrim", "Medieval Crafter: Blacksmith"],
        "series": [
            {"nom": "📜 Journal d’un forge-lol 🔨", "url": "https://youtube.com/playlist?list=PLgX-3H3ACJk5Rb3whj-89ANDgMXN-iaBf&si=imShezTIZrFKmWx_"},
            {"nom": "Lura : L’Héritière des Forges", "url": "https://www.youtube.com/playlist?list=PLgX-3H3ACJk40I098msu4YsPFX5fNPRDO"},
            {"nom": "Chroniques De Silent Hill 2", "url": "https://www.youtube.com/playlist?list=PLgX-3H3ACJk7l33I2euw_yEPJ7a4JEVx9"},
            {"nom": "Underground Garage", "url": "https://www.youtube.com/playlist?list=PLgX-3H3ACJk6exfv_mzqJ-IKSZJbhFuNe"}
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
            {"nom": "LE BUREAU DES PLAINTES", "url": "https://youtube.com/playlist?list=PLkBX3VXLbjxjTAXJeaohmW9G-F9Wne1c3&si=x-tq5dHrDOZiVO8z    "}
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
            {"nom": "Slime Rancher 2", "url": "https://www.youtube.com/playlist?list=PLD-GVWgeEc6diG7X1purupOBtHJqrZwnx"},
            {"nom": "L'Épopée Féline", "url": "https://www.youtube.com/playlist?list=PLD-GVWgeEc6fCdkCXg38Bcw7fm9YZcuzV"},
            {"nom": "Crime Scene Cleaner", "url": "https://www.youtube.com/playlist?list=PLD-GVWgeEc6dfycSPIsT9LmSuAa4rlSx9"}
        ],
        "liens": "https://www.youtube.com/@xannalanooblette",
        "twitch_id": "xannalanooblette",
        "insta": "https://instagram.com/xannalasedistemaispastrop",
        "discord": "https://discord.gg/votrelien",
    }
}

# --- NAVIGATION (MISE À JOUR : 6 COLONNES) ---
st.write("---")
cols_nav = st.columns(6) # Changé de 4 à 6
btns = ["QUI SOMMES-NOUS", "L'ÉQUIPE", "PROJETS", "SHOP", "CONTACT", "DON"]
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

# --- DÉBUT DU BLOC À COLLER ---
    if nom == "NICOLEGEEK":
        st.subheader("📅 PLANNING & ACTUALITÉS")
        st.write("NicoleGeek n'a pas de planning de stream fixe, mais il est très actif sur YouTube pour vous présenter ses dernières trouvailles rétro et ses consoles de collection !")
        
        # Le bouton identique aux autres
        st.markdown(f'''
            <a href="{m["liens"]}" target="_blank" style="text-decoration: none;">
                <div class="custom-button-link">
                    VOIR SES VIDÉOS SUR YOUTUBE
                </div>
            </a>
        ''', unsafe_allow_html=True)
    
    elif m.get('twitch_id'):
        st.subheader(f"📅 PLANNING DE {nom.upper()}")
        st.link_button(f"VOIR LE PLANNING SUR TWITCH", f"https://www.twitch.tv/{m['twitch_id']}/schedule", use_container_width=True)
        st.markdown(f'<iframe src="https://www.twitch.tv/popout/{m["twitch_id"]}/schedule" height="600" width="100%" frameborder="0"></iframe>', unsafe_allow_html=True)
    
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
        st.markdown('<a href="mailto:contact@fr33zyoverstudio.fr" class="custom-button-link">CONTACTER PAR EMAIL</a>',
                    unsafe_allow_html=True)
    with c2:
        st.markdown("### 💬 COMMUNAUTÉ")
        st.link_button("REJOINDRE LE DISCORD", "https://discord.gg/votrelien", use_container_width=True)

elif st.session_state.active_tab == "QUI SOMMES-NOUS":
    st.subheader("NOTRE HISTOIRE")

    # Présentation principale
    st.markdown("""
        <div style="background: #161b22; padding: 30px; border-radius: 15px; border: 1px solid #30363d;">
            <h2 style="color: #e67e22; margin-top: 0;">BIENVENUE CHEZ FR33ZY OVER STUDIO</h2>
            <p style="font-size: 1.1rem; line-height: 1.6; color: #e1e4e8;">
                Depuis 2012, nous partageons notre passion pour l'univers du gaming. 
                Anciennement connue sous le nom de <b>Over_1</b>, notre équipe évolue pour vous proposer 
                une expérience communautaire unique, mêlant expertise technique et amour du jeu.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Colonnes pour le contenu et les objectifs
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

elif st.session_state.active_tab == "DON":
    st.subheader("💎 SOUTIEN")
    st.write("")
    # Message d'attente stylisé
    st.info(
        "🚀 Le système de soutien via PayPal est en cours d'intégration. Revenez très bientôt pour soutenir l'aventure Fr33zy Over Studio !")

    # Optionnel : un petit visuel ou texte pour faire patienter
    st.markdown("""
        <div style="text-align: center; padding: 40px; border: 1px dashed #30363d; border-radius: 10px; opacity: 0.6;">
            <p style="font-size: 1.2rem; color: #e67e22;">🚧 MODULE EN MAINTENANCE 🚧</p>
            <p style="font-size: 0.9rem;">Nous préparons une plateforme sécurisée pour vos dons.</p>
        </div>
    """, unsafe_allow_html=True)
    
# Ajoute ces blocs avant le FOOTER :

if st.session_state.active_tab == "PROJETS":
    st.subheader("📁 NOS RÉALISATIONS")
    st.write("")

    # Message d'attente stylisé
    st.info(
        "🎬 Nos projets cinématographiques et créatifs sont actuellement en cours de montage. La page Projets sera mise à jour très prochainement !")

    # Bloc visuel "Work in Progress"
    st.markdown("""
            <div style="text-align: center; padding: 40px; border: 1px dashed #30363d; border-radius: 10px; opacity: 0.6; margin-top:20px;">
                <p style="font-size: 1.2rem; color: #e67e22;">🚧 PROJETS EN COURS DE DÉVELOPPEMENT 🚧</p>
                <p style="font-size: 0.9rem;">De la création vidéo aux archives du studio, préparez-vous pour du lourd.</p>
            </div>
        """, unsafe_allow_html=True)


elif st.session_state.active_tab == "SHOP":
    st.subheader("🛒 BOUTIQUE OFFICIELLE")
    st.write("Soutenez l'association en arborant nos couleurs !")
    st.write("")

    # Message d'attente identique à la page DON
    st.info(
        "🚀 La boutique officielle Fr33zy Over Studio est actuellement en cours de préparation. Vous y retrouverez bientôt nos vêtements et accessoires exclusifs !")

    # Bloc de maintenance visuel (comme sur ta page DON)
    st.markdown("""
            <div style="text-align: center; padding: 40px; border: 1px dashed #30363d; border-radius: 10px; opacity: 0.6; margin-top:20px;">
                <p style="font-size: 1.2rem; color: #e67e22;">🚧 MODULE BOUTIQUE EN CONSTRUCTION 🚧</p>
                <p style="font-size: 0.9rem;">Nous sélectionnons les meilleurs produits pour vous garantir une qualité premium.</p>
            </div>
        """, unsafe_allow_html=True)

# --- FOOTER AMÉLIORÉ ---
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; padding-top: 30px; border-top: 1px solid #30363d;">
        <p style="font-size: 0.9rem; color: white; margin-bottom: 5px; font-weight: 500;">
            © 2026 <span style="color: #e67e22; font-weight: bold;">FR33ZY OVER STUDIO</span>. TOUS DROITS RÉSERVÉS.
        </p>
        <p style="font-size: 0.7rem; color: #8b949e;">
            Version {VERSION} • {LICENSE}
        </p>
        <p style="font-size: 0.65rem; letter-spacing: 2px; color: #8b949e; text-transform: uppercase; opacity: 0.6;">
            Powered by OBS STUDIO &bull; DAVINCI RESOLVE &bull; STREAMLIT &bull; PHOTOSHOP
        </p>
    </div>
""", unsafe_allow_html=True)
