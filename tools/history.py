"""Historique synthétique de Kastideo (Mac), par version X.Y : les versions X.Y.n sont regroupées.

À compléter à chaque nouvelle version X.Y (la dernière version, elle, est lue en direct sur GitHub).
(version, date de la X.Y.0, texte FR, texte EN)
"""

HISTORY = [
    ("1.16", "2026-11-07", "Enregistrements (Mac) : durée réglable après le démarrage (15 min à 4 h, heure précise ou sans limite), durée par défaut et temps restant affiché. Le fichier d'origine est conservé si la conversion perdait l'image.",
     "Recordings (Mac): duration adjustable after starting (15 min to 4 h, exact time or no limit), default duration and remaining time shown. The original file is kept if conversion would lose the picture."),
    ("1.15", "2026-11-07", "Retirer un contenu de « Reprendre la lecture », avec annulation possible.",
     "Remove an item from “Continue watching”, with undo."),
    ("1.14", "2026-11-06", "Enregistrements (Mac) : retirer un, plusieurs ou tous les enregistrements de la liste, avec ou sans suppression des fichiers.",
     "Recordings (Mac): remove one, several or all recordings from the list, with or without deleting the files."),
    ("1.13", "2026-11-03", "MultiVue repensée pour plusieurs abonnements : nombre d'écrans, dispositions, vrai PIP à vignettes déplaçables, nouveau sélecteur de chaînes et accès plus visibles.",
     "MultiView redesigned for several subscriptions: number of screens, layouts, a real PIP with movable tiles, new channel picker and more visible entry points."),
    ("1.12", "2026-11-03", "Mes vidéos : filtres (source, pays, langue, qualité, état) et tris mémorisés. MultiVue avec plusieurs sources et image dans l'image pendant un direct.",
     "My videos: filters (source, country, language, quality, status) and remembered sorting. MultiView with several sources and picture in picture during live TV."),
    ("1.11", "2026-11-03", "Corriger la fiche d'un film ou d'une série par son code TMDB, ou la personnaliser à la main, y compris pour l'abonnement IPTV.",
     "Fix a movie or series page using its TMDB code, or customise it by hand, including for the IPTV subscription."),
    ("1.10", "2026-11-02", "Plusieurs comptes IPTV : menu Source, fusion des doublons et diagnostic de la source. Affiches et résumés pour vos vidéos personnelles.",
     "Several IPTV accounts: Source menu, duplicate merging and source diagnostics. Posters and summaries for your personal videos."),
    ("1.9", "2026-10-31", "Kastideo arrive sur Android et Android TV (aperçu). Aide de l'accueil refaite, textes sur la gratuité et mention légale.",
     "Kastideo arrives on Android and Android TV (preview). Home screen help rewritten, text about being free and legal notice."),
    ("1.8", "2026-10-31", "Page de départ au choix pour Direct, Films et Séries. Repli automatique en décodage logiciel pour les chaînes dont l'image se fige.",
     "Choice of start page for Live, Movies and Series. Automatic fallback to software decoding for channels whose picture freezes."),
    ("1.7", "2026-10-30", "Diffusion vers un téléviseur : Chromecast, Google TV, TV Android et Apple TV. YouTube sur le téléviseur, bouton Arrêt dans la barre de lecture.",
     "Casting to a TV: Chromecast, Google TV, Android TV and Apple TV. YouTube on the TV, Stop button in the playback bar."),
    ("1.6", "2026-10-30", "Aide refaite de A à Z : fenêtre dédiée avec recherche, bouton « ? » qui ouvre la page de l'écran en cours, pas à pas.",
     "Help rebuilt from scratch: dedicated window with search, a “?” button that opens the page for the current screen, step by step."),
    ("1.5", "2026-10-30", "YouTube intégré : navigateur, recherche, lecteur, « à regarder plus tard » et import de vos abonnements.",
     "YouTube built in: browser, search, player, “watch later” and import of your subscriptions."),
    ("1.4", "2026-10-29", "Replay : revoir un programme déjà diffusé depuis le guide TV. Soutien facultatif (Offrir un café).",
     "Replay: watch an already broadcast programme from the TV guide. Optional support (Buy me a coffee)."),
    ("1.3", "2026-10-26", "Nouvelles sources : dossiers, disques et NAS, serveurs Jellyfin, Emby et Plex. Tuile Mes vidéos, journal de diagnostic par sujets, guide TV plus juste.",
     "New sources: folders, drives and NAS, Jellyfin, Emby and Plex servers. My videos tile, diagnostic log by topic, more accurate TV guide."),
    ("1.2", "2026-10-25", "Sauvegarde et transfert de la configuration, gestion des catégories, pays et langues des rangées Cinéma.",
     "Backup and transfer of the configuration, category management, countries and languages of the Cinema rows."),
    ("1.1", "2026-10-23", "Direct en différé (timeline, vitesse, retour au direct). Relais de flux et corrections des chaînes sans son ou à l'image figée, journal de lecture.",
     "Live timeshift (timeline, speed, back to live). Stream relay and fixes for channels with no sound or a frozen picture, playback log."),
    ("1.0", "2026-10-22", "Première version stable. Modifier une chaîne (nom, numéro, logo), thèmes « En ce moment », changement de chaîne plus fiable.",
     "First stable version. Edit a channel (name, number, logo), “Right now” themes, more reliable channel switching."),
    ("0.15", "2026-10-22", "Nouveaux thèmes, sport par discipline, contenus adultes masqués par défaut.",
     "New themes, sport by discipline, adult content hidden by default."),
    ("0.14", "2026-10-22", "Direct par thème (En ce moment, Ce soir), une seule version par chaîne selon la qualité de votre connexion.",
     "Live by theme (Right now, Tonight), one version per channel depending on your connection quality."),
    ("0.13", "2026-10-21", "MultiVue (plusieurs chaînes à l'écran) et mises à jour automatiques, jamais pendant un visionnage.",
     "MultiView (several channels on screen) and automatic updates, never during viewing."),
    ("0.12", "2026-10-21", "Lecteur repensé : mini-timeline, panneau Informations, choix de la piste audio et des sous-titres.",
     "Redesigned player: mini timeline, Information panel, choice of audio track and subtitles."),
    ("0.11", "2026-10-21", "Gestion des catégories (réordonner, masquer, renommer), écran d'accueil et bandeau « à la une » améliorés.",
     "Category management (reorder, hide, rename), improved home screen and “featured” banner."),
    ("0.10", "2026-10-21", "Bandeau « à la une » avec les tendances TMDB, boutons Lire et Reprendre, bande-annonce.",
     "“Featured” banner with TMDB trends, Play and Resume buttons, trailer."),
    ("0.9", "2026-10-20", "Fiches films et séries (TMDB), enregistrement du direct fiabilisé, guide TV de secours, aide intégrée.",
     "Movie and series pages (TMDB), more reliable live recording, backup TV guide, built-in help."),
    ("0.8", "2026-10-20", "Écran d'accueil, plein écran, enregistrements dans le dossier de votre choix.",
     "Home screen, full screen, recordings in the folder of your choice."),
    ("0.7", "2026-10-19", "Guide TV en grille, programmation des enregistrements, reprise de la lecture.",
     "Grid TV guide, recording scheduling, resume playback."),
    ("0.6", "2026-10-19", "Interface TV pour le direct : chaîne en plein cadre et zapping au clavier.",
     "TV interface for live viewing: full-frame channel and keyboard zapping."),
    ("0.5", "2026-10-19", "Interface Cinéma, avec une interface au choix par type de contenu.",
     "Cinema interface, with a choice of interface per content type."),
    ("0.4", "2026-10-18", "Enregistrement du direct, enregistrements programmés, téléchargement de films et d'épisodes, direct en différé.",
     "Live recording, scheduled recordings, movie and episode downloads, live timeshift."),
    ("0.3", "2026-10-18", "Lecture des flux MPEG-TS et MKV, mode cinéma, journal de lecture.",
     "Playback of MPEG-TS and MKV streams, cinema mode, playback log."),
    ("0.2", "2026-10-18", "Mises à jour automatiques, reconnaissance des adresses get.php comme abonnement Xtream Codes.",
     "Automatic updates, get.php addresses recognised as an Xtream Codes subscription."),
    ("0.1", "2026-10-18", "Première version.", "First version."),
]

MONTHS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
MONTHS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def date_label(iso, lang):
    y, m, d = (int(x) for x in iso.split("-"))
    if lang == "fr":
        return f"{'1er' if d == 1 else d} {MONTHS_FR[m - 1]} {y}"
    return f"{d} {MONTHS_EN[m - 1]} {y}"


def history_html(lang):
    items = "\n".join(
        f'      <li><span class="hv">{v}</span><time datetime="{d}">{date_label(d, lang)}</time><span class="ht">{fr if lang == "fr" else en}</span></li>'
        for v, d, fr, en in HISTORY)
    return f'    <ol class="history">\n{items}\n    </ol>\n'
