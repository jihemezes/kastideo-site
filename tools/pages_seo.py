"""Pages de comparaison et questions fréquentes (FR et EN).

Ton factuel : seules des affirmations prudentes sont faites sur les autres logiciels,
et les fonctions de Kastideo sont celles décrites dans l'aide de l'application.
"""

NOTE_FR = ("Comparaison établie en novembre 2026 à partir des versions publiques de chaque logiciel. Les fonctions évoluent : "
           "vérifiez toujours auprès de l'éditeur concerné. {name} est une marque de son propriétaire, et Kastideo n'est affilié à aucun éditeur cité.")
NOTE_EN = ("Comparison made in November 2026 from the public versions of each software. Features change: "
           "always check with the publisher concerned. {name} is a trademark of its owner, and Kastideo is not affiliated with any publisher mentioned.")


def table(rows, head, lang):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "\n".join("          <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    label = "Comparaison" if lang == "fr" else "Comparison"
    return (f'    <div class="table-wrap" role="region" aria-label="{label}" tabindex="0">\n'
            f'      <table class="ver-table">\n        <thead><tr>{th}</tr></thead>\n        <tbody>\n{tr}\n        </tbody>\n      </table>\n    </div>\n')


# --------------------------------------------------------------------------- VLC
VLC_FR = f"""    <h1>Alternative à VLC pour regarder l'IPTV</h1>
    <p class="page-lead">VLC est un excellent lecteur de fichiers vidéo, et il sait ouvrir une playlist M3U. Kastideo, lui, est construit autour de la télévision par IPTV : voici ce qui change au quotidien.</p>

    <h2 id="difference">La différence en une phrase</h2>
    <p>Avec VLC, une playlist IPTV est une longue liste d'adresses à parcourir. Avec Kastideo, c'est un téléviseur : des chaînes classées par thème, un guide TV en grille, un replay, des enregistrements, et vos films et séries rangés à part.</p>

{table([
    ["Ouvrir une playlist M3U", "Oui, comme une liste de lecture", "Oui, entrées classées en direct, films et séries, avec leurs catégories"],
    ["Abonnement Xtream Codes", "Par l'adresse de la playlist", "Identifiants, test de connexion, état du compte et guide TV du serveur"],
    ["Guide TV en grille", "Pas de grille de guide pour une playlist IPTV", "Grille 2, 3 ou 6 heures, thèmes, vue Ce soir, alertes"],
    ["Replay d'un programme passé", "Non", "Oui, si votre fournisseur conserve une archive"],
    ["Enregistrement", "Enregistrement manuel", "Immédiat ou programmé depuis le guide, avec répétition (Windows, Linux, Android)"],
    ["Films et séries", "Fichiers et adresses", "Affiches, fiches TMDB, saisons, épisodes et reprise de lecture"],
    ["Plusieurs chaînes à l'écran", "Une fenêtre par instance", "MultiVue jusqu'à 4 chaînes, son sur la vignette active"],
    ["Prix", "Gratuit", "Gratuit"],
], ["Besoin", "VLC", "Kastideo"], "fr")}
    <h2 id="rester">Quand rester sur VLC</h2>
    <p>VLC reste le bon outil pour lire presque n'importe quel fichier vidéo ou audio, convertir un format ou ouvrir un flux réseau ponctuel. Kastideo ne cherche pas à le remplacer : il s'adresse à ceux qui regardent chaque jour la télévision par IPTV et veulent un vrai confort d'usage.</p>

    <h2 id="essayer">Essayer Kastideo</h2>
    <p>Kastideo ne fournit aucune chaîne : vous gardez vos sources et vous les ajoutez dans les réglages. Voir <a href="sources.html">Vos sources</a>, le <a href="guide-tv.html">guide TV</a> et le <a href="replay.html">replay</a>, ou <a href="telecharger.html">télécharger l'application</a>.</p>
    <p class="note">{NOTE_FR.format(name="VLC")}</p>
"""
VLC_EN = f"""    <h1>VLC alternative for watching IPTV</h1>
    <p class="page-lead">VLC is an excellent video file player, and it can open an M3U playlist. Kastideo is built around IPTV television: here is what changes day to day.</p>

    <h2 id="difference">The difference in one sentence</h2>
    <p>With VLC, an IPTV playlist is a long list of addresses to browse. With Kastideo, it is a television: channels sorted by theme, a grid TV guide, replay, recordings, and your movies and series kept apart.</p>

{table([
    ["Open an M3U playlist", "Yes, as a playlist", "Yes, entries sorted into live, movies and series, with their categories"],
    ["Xtream Codes subscription", "Through the playlist address", "Credentials, connection test, account status and the server's TV guide"],
    ["Grid TV guide", "No guide grid for an IPTV playlist", "2, 3 or 6 hour grid, themes, Tonight view, alerts"],
    ["Replay of a past programme", "No", "Yes, if your provider keeps an archive"],
    ["Recording", "Manual recording", "Immediate or scheduled from the guide, with repeat (Windows, Linux, Android)"],
    ["Movies and series", "Files and addresses", "Posters, TMDB pages, seasons, episodes and resume playback"],
    ["Several channels on screen", "One window per instance", "MultiView up to 4 channels, sound on the active tile"],
    ["Price", "Free", "Free"],
], ["Need", "VLC", "Kastideo"], "en")}
    <h2 id="rester">When to stay with VLC</h2>
    <p>VLC remains the right tool to play almost any video or audio file, convert a format or open a one-off network stream. Kastideo does not try to replace it: it is for people who watch IPTV television every day and want real comfort of use.</p>

    <h2 id="essayer">Try Kastideo</h2>
    <p>Kastideo provides no channels: you keep your sources and add them in the settings. See <a href="sources.html">Your sources</a>, the <a href="guide-tv.html">TV guide</a> and <a href="replay.html">replay</a>, or <a href="telecharger.html">download the app</a>.</p>
    <p class="note">{NOTE_EN.format(name="VLC")}</p>
"""

# ----------------------------------------------------------------------- TiviMate
TIVI_FR = f"""    <h1>Alternative à TiviMate sur Mac, Windows et Linux</h1>
    <p class="page-lead">TiviMate est une application d'IPTV appréciée sur Android TV. Kastideo vise le même confort, avec une différence : il est gratuit et il existe aussi sur Mac, Windows et Linux.</p>

    <h2 id="difference">Ce qui diffère</h2>
    <ul>
      <li><b>Les appareils.</b> TiviMate est conçu pour Android TV, Fire TV et Android. Kastideo fonctionne sur Mac, Windows, Linux, Android et Android TV : le même guide, les mêmes catégories et la même configuration d'un appareil à l'autre.</li>
      <li><b>Le prix.</b> Certaines fonctions de TiviMate sont réservées à son offre Premium payante. Kastideo est gratuit, sans compte, et le reste.</li>
      <li><b>La maturité.</b> TiviMate est très abouti sur Android TV. La version Android et Android TV de Kastideo est encore en aperçu, tandis que la version Mac est stable.</li>
    </ul>

{table([
    ["Appareils", "Android TV, Fire TV, Android", "Mac, Windows, Linux, Android, Android TV"],
    ["Guide TV en grille", "Oui", "Oui, avec thèmes et vue Ce soir"],
    ["Replay du fournisseur", "Selon le fournisseur", "Oui, depuis le guide TV, si une archive existe"],
    ["Enregistrement programmé", "Oui, selon l'offre", "Oui, avec répétition (Windows, Linux, Android)"],
    ["Plusieurs chaînes à l'écran", "Selon l'offre", "MultiVue jusqu'à 4 chaînes"],
    ["Films et séries (Xtream)", "Oui", "Oui, avec fiches TMDB et reprise de lecture"],
    ["Prix", "Offre gratuite et offre Premium payante", "Gratuit"],
], ["Besoin", "TiviMate", "Kastideo"], "fr")}
    <h2 id="choisir">Lequel choisir</h2>
    <p>Si vous regardez uniquement sur un téléviseur Android TV ou un Fire TV et que vous êtes satisfait, rien ne presse. Si vous voulez regarder aussi sur ordinateur, sans payer, avec la même organisation partout, Kastideo mérite un essai. Vos sources se transfèrent d'un appareil à l'autre par un fichier de sauvegarde : voir <a href="interfaces.html#sauvegarde">Interfaces et personnalisation</a>.</p>
    <p>Pour le détail : <a href="guide-tv.html">guide TV</a>, <a href="replay.html">replay</a>, <a href="multivue.html">MultiVue</a>, <a href="enregistrer.html">enregistrement</a>, ou <a href="android.html">Kastideo sur Android TV</a>.</p>
    <p class="note">{NOTE_FR.format(name="TiviMate")}</p>
"""
TIVI_EN = f"""    <h1>TiviMate alternative on Mac, Windows and Linux</h1>
    <p class="page-lead">TiviMate is an IPTV app well liked on Android TV. Kastideo aims for the same comfort, with one difference: it is free and also runs on Mac, Windows and Linux.</p>

    <h2 id="difference">What differs</h2>
    <ul>
      <li><b>Devices.</b> TiviMate is designed for Android TV, Fire TV and Android. Kastideo runs on Mac, Windows, Linux, Android and Android TV: the same guide, categories and configuration from one device to another.</li>
      <li><b>Price.</b> Some TiviMate features are reserved for its paid Premium offer. Kastideo is free, needs no account, and stays that way.</li>
      <li><b>Maturity.</b> TiviMate is very polished on Android TV. Kastideo's Android and Android TV version is still a preview, while the Mac version is stable.</li>
    </ul>

{table([
    ["Devices", "Android TV, Fire TV, Android", "Mac, Windows, Linux, Android, Android TV"],
    ["Grid TV guide", "Yes", "Yes, with themes and Tonight view"],
    ["Provider replay", "Depends on the provider", "Yes, from the TV guide, if an archive exists"],
    ["Scheduled recording", "Yes, depending on the offer", "Yes, with repeat (Windows, Linux, Android)"],
    ["Several channels on screen", "Depends on the offer", "MultiView up to 4 channels"],
    ["Movies and series (Xtream)", "Yes", "Yes, with TMDB pages and resume playback"],
    ["Price", "Free offer and paid Premium offer", "Free"],
], ["Need", "TiviMate", "Kastideo"], "en")}
    <h2 id="choisir">Which to choose</h2>
    <p>If you only watch on an Android TV or a Fire TV and are happy, there is no rush. If you also want to watch on a computer, without paying, with the same organisation everywhere, Kastideo deserves a try. Your sources move between devices through a backup file: see <a href="interfaces.html#sauvegarde">Interfaces and personalisation</a>.</p>
    <p>For details: <a href="guide-tv.html">TV guide</a>, <a href="replay.html">replay</a>, <a href="multivue.html">MultiView</a>, <a href="enregistrer.html">recording</a>, or <a href="android.html">Kastideo on Android TV</a>.</p>
    <p class="note">{NOTE_EN.format(name="TiviMate")}</p>
"""

# ------------------------------------------------------------------------ Smarters
SMART_FR = f"""    <h1>Alternative à IPTV Smarters Pro</h1>
    <p class="page-lead">IPTV Smarters Pro est l'une des applications les plus répandues pour lire un abonnement IPTV, souvent proposée par les fournisseurs sous leur propre marque. Kastideo prend le chemin inverse : un lecteur indépendant, qui ne dépend d'aucun fournisseur.</p>

    <h2 id="difference">Ce qui diffère</h2>
    <ul>
      <li><b>L'indépendance.</b> Kastideo n'est lié à aucun fournisseur, ne fournit aucune chaîne et n'affiche aucune marque d'abonnement. Vous changez de fournisseur sans changer d'application.</li>
      <li><b>L'organisation.</b> Trois interfaces au choix (Classique, Cinéma, TV), un guide TV en grille avec thèmes, une MultiVue, un replay intégré au guide et des téléchargements en file d'attente.</li>
      <li><b>Vos données.</b> Aucun compte à créer et aucune statistique d'usage : vos identifiants restent sur votre appareil, dans le coffre sécurisé du système. Voir la <a href="confidentialite.html">politique de confidentialité</a>.</li>
    </ul>

{table([
    ["Sources", "Xtream Codes, M3U", "Xtream Codes, M3U, dossiers et NAS, Jellyfin, Emby, Plex, YouTube"],
    ["Appareils", "Plusieurs plateformes mobiles, TV et ordinateur", "Mac, Windows, Linux, Android, Android TV"],
    ["Guide TV en grille", "Oui", "Oui, avec thèmes, vue Ce soir et alertes"],
    ["Replay du fournisseur", "Selon le fournisseur", "Oui, depuis le guide, si une archive existe"],
    ["Interfaces au choix", "Non précisé", "Classique, Cinéma, TV, par type de contenu"],
    ["Enregistrement et téléchargement", "Selon la version", "Oui, immédiat, programmé, file de téléchargements"],
    ["Prix", "Selon la version et le fournisseur", "Gratuit"],
], ["Besoin", "IPTV Smarters Pro", "Kastideo"], "fr")}
    <h2 id="choisir">Pour qui</h2>
    <p>Si l'application fournie par votre fournisseur vous convient, vous pouvez la garder. Si vous préférez un lecteur neutre, plus complet et identique sur ordinateur et sur téléviseur, essayez Kastideo avec vos propres identifiants Xtream Codes ou votre playlist M3U : voir <a href="sources.html">Vos sources</a>.</p>
    <p>Kastideo ne fournit aucun contenu et vous devez vérifier que vos sources sont légales. Voir les <a href="mentions-legales.html">mentions légales</a>.</p>
    <p class="note">{NOTE_FR.format(name="IPTV Smarters Pro")}</p>
"""
SMART_EN = f"""    <h1>IPTV Smarters Pro alternative</h1>
    <p class="page-lead">IPTV Smarters Pro is one of the most widespread apps for playing an IPTV subscription, often offered by providers under their own brand. Kastideo takes the opposite path: an independent player, tied to no provider.</p>

    <h2 id="difference">What differs</h2>
    <ul>
      <li><b>Independence.</b> Kastideo is tied to no provider, provides no channels and shows no subscription branding. You change provider without changing app.</li>
      <li><b>Organisation.</b> Three interfaces to choose from (Classic, Cinema, TV), a grid TV guide with themes, MultiView, replay built into the guide and queued downloads.</li>
      <li><b>Your data.</b> No account to create and no usage statistics: your credentials stay on your device, in the system's secure store. See the <a href="confidentialite.html">privacy policy</a>.</li>
    </ul>

{table([
    ["Sources", "Xtream Codes, M3U", "Xtream Codes, M3U, folders and NAS, Jellyfin, Emby, Plex, YouTube"],
    ["Devices", "Several mobile, TV and computer platforms", "Mac, Windows, Linux, Android, Android TV"],
    ["Grid TV guide", "Yes", "Yes, with themes, Tonight view and alerts"],
    ["Provider replay", "Depends on the provider", "Yes, from the guide, if an archive exists"],
    ["Interfaces to choose from", "Not specified", "Classic, Cinema, TV, per content type"],
    ["Recording and downloading", "Depends on the version", "Yes, immediate, scheduled, download queue"],
    ["Price", "Depends on the version and provider", "Free"],
], ["Need", "IPTV Smarters Pro", "Kastideo"], "en")}
    <h2 id="choisir">Who it is for</h2>
    <p>If the app supplied by your provider suits you, you can keep it. If you prefer a neutral player, more complete and identical on computer and TV, try Kastideo with your own Xtream Codes credentials or M3U playlist: see <a href="sources.html">Your sources</a>.</p>
    <p>Kastideo provides no content and you must check that your sources are legal. See the <a href="mentions-legales.html">legal notice</a>.</p>
    <p class="note">{NOTE_EN.format(name="IPTV Smarters Pro")}</p>
"""

# --------------------------------------------------------------------------- FAQ
FAQ_FR = """    <h1>Questions fréquentes</h1>
    <p class="page-lead">Les réponses aux questions qu'on nous pose le plus souvent sur Kastideo.</p>

    <h2 id="chaines">Kastideo fournit-il des chaînes ou un abonnement IPTV ?</h2>
    <p>Non. Kastideo est un lecteur : il ne fournit, n'héberge ni ne vend aucune chaîne, aucun film ni aucun abonnement. Vous apportez vos propres sources et vous êtes responsable de leur légalité. Voir <a href="sources.html">Vos sources</a>.</p>

    <h2 id="gratuit">Kastideo est-il vraiment gratuit ?</h2>
    <p>Oui. Aucune fonction n'est payante, aucun compte n'est demandé et aucune publicité n'est affichée. Un soutien est possible, entièrement facultatif : <a href="soutenir.html">Soutenir le projet</a>.</p>

    <h2 id="appareils">Sur quels appareils fonctionne-t-il ?</h2>
    <p>Sur Mac (version stable), et en aperçu sur Windows 10 et 11, Linux (Zorin OS, Ubuntu, Raspberry Pi) et Android, y compris Android TV. Voir <a href="telecharger.html">Télécharger</a>.</p>

    <h2 id="sources">Quelles sources sait-il lire ?</h2>
    <p>Un abonnement Xtream Codes, une playlist M3U, des dossiers de vos disques ou de votre NAS, des serveurs Jellyfin, Emby et Plex, et YouTube.</p>

    <h2 id="connexion">Pourquoi une seule chaîne à la fois ?</h2>
    <p>La plupart des abonnements IPTV n'autorisent qu'une connexion simultanée. Kastideo ferme le flux en cours avant d'en ouvrir un autre pour éviter de dépasser votre limite. Avec un abonnement à plusieurs connexions, la <a href="multivue.html">MultiVue</a> affiche jusqu'à quatre chaînes.</p>

    <h2 id="replay">Comment fonctionne le replay ?</h2>
    <p>Il s'appuie sur l'archive de votre fournisseur : quand elle existe, les programmes passés apparaissent dans le guide TV et se relancent d'un clic. Voir <a href="replay.html">Replay des programmes</a>.</p>

    <h2 id="replay-absent">Pourquoi je ne vois pas le replay alors que mon fournisseur le propose ?</h2>
    <p>Le replay n'apparaît que si Kastideo détecte une archive pour la chaîne : l'icône ↺ s'affiche alors à côté d'elle. Vérifiez dans l'ordre :</p>
    <ul>
      <li><b>Le replay est activé</b> : Réglages &gt; Général &gt; Replay.</li>
      <li><b>L'archive existe pour cette chaîne</b> : certains abonnements conservent les chaînes jusqu'à 14 jours, mais pas toutes.</li>
      <li><b>Le guide contient les programmes passés</b> : augmentez le nombre de jours conservés dans le guide (Réglages &gt; Général &gt; Replay), puis rechargez le guide. Plus de jours demandent plus de mémoire.</li>
      <li><b>Le décalage horaire</b> : réglez-le si le programme lancé ne correspond pas à celui choisi.</li>
      <li><b>Une seule connexion</b> : le replay compte comme une connexion, fermez les autres lectures et appareils.</li>
    </ul>
    <p>Si le programme ne démarre pas, ouvrez le Journal de lecture, sujet « Lecture et relais » : il indique l'adresse d'archive demandée. Voir <a href="replay.html">Replay des programmes</a>.</p>

    <h2 id="windows">Windows affiche « Windows a protégé votre ordinateur », que faire ?</h2>
    <p>La version Windows n'est pas encore signée. Cliquez sur Informations complémentaires, puis sur Exécuter quand même. Voir <a href="windows.html">Kastideo pour Windows</a>.</p>

    <h2 id="android-tv">Comment installer Kastideo sur Android TV ?</h2>
    <p>Hors Google Play, avec l'application Downloader, une clé USB ou l'envoi depuis un téléphone. Voir <a href="guide-android-tv.html">Installer Kastideo sur Android TV</a>.</p>

    <h2 id="donnees">Que devient mon mot de passe ?</h2>
    <p>Vos identifiants restent sur votre appareil, dans le coffre sécurisé du système, et ne sont envoyés qu'aux services que vous configurez. Kastideo ne collecte aucune statistique d'usage. Voir la <a href="confidentialite.html">politique de confidentialité</a>.</p>

    <h2 id="probleme">Une chaîne ne démarre pas, que faire ?</h2>
    <p>Coupez d'abord un éventuel VPN, vérifiez qu'aucun autre appareil n'utilise votre abonnement, puis consultez le Journal de lecture. Voir <a href="fiabilite.html#journal">Rapide, stable et sobre</a>.</p>

    <h2 id="contact">Comment vous contacter ?</h2>
    <p>Par e-mail à <code>contact@kastideo.com</code>, ou sur <a href="https://github.com/jihemezes/kastideo/issues" target="_blank" rel="noopener">GitHub</a> pour un problème ou une idée.</p>
"""
FAQ_EN = """    <h1>Frequently asked questions</h1>
    <p class="page-lead">Answers to the questions we are asked most often about Kastideo.</p>

    <h2 id="chaines">Does Kastideo provide channels or an IPTV subscription?</h2>
    <p>No. Kastideo is a player: it does not provide, host or sell any channel, movie or subscription. You bring your own sources and you are responsible for their legality. See <a href="sources.html">Your sources</a>.</p>

    <h2 id="gratuit">Is Kastideo really free?</h2>
    <p>Yes. No feature is paid, no account is asked and no ads are shown. Support is possible and entirely optional: <a href="soutenir.html">Support the project</a>.</p>

    <h2 id="appareils">Which devices does it run on?</h2>
    <p>On Mac (stable version), and as a preview on Windows 10 and 11, Linux (Zorin OS, Ubuntu, Raspberry Pi) and Android, including Android TV. See <a href="telecharger.html">Download</a>.</p>

    <h2 id="sources">Which sources can it play?</h2>
    <p>An Xtream Codes subscription, an M3U playlist, folders on your drives or NAS, Jellyfin, Emby and Plex servers, and YouTube.</p>

    <h2 id="connexion">Why only one channel at a time?</h2>
    <p>Most IPTV subscriptions allow only one simultaneous connection. Kastideo closes the current stream before opening another to avoid exceeding your limit. With a multi-connection subscription, <a href="multivue.html">MultiView</a> shows up to four channels.</p>

    <h2 id="replay">How does replay work?</h2>
    <p>It relies on your provider's archive: when one exists, past programmes appear in the TV guide and play in one click. See <a href="replay.html">Programme replay</a>.</p>

    <h2 id="replay-absent">Why can't I see replay when my provider offers it?</h2>
    <p>Replay only appears if Kastideo detects an archive for the channel: the ↺ icon then shows next to it. Check in this order:</p>
    <ul>
      <li><b>Replay is enabled</b>: Settings &gt; General &gt; Replay.</li>
      <li><b>The archive exists for this channel</b>: some subscriptions keep channels for up to 14 days, but not all of them.</li>
      <li><b>The guide contains past programmes</b>: increase the number of days kept in the guide (Settings &gt; General &gt; Replay), then reload the guide. More days need more memory.</li>
      <li><b>The time offset</b>: adjust it if the programme that starts is not the one you chose.</li>
      <li><b>A single connection</b>: replay counts as one connection, close other playbacks and devices.</li>
    </ul>
    <p>If the programme does not start, open the playback log, topic “Playback and relay”: it shows the archive address requested. See <a href="replay.html">Programme replay</a>.</p>

    <h2 id="windows">Windows shows “Windows protected your PC”, what should I do?</h2>
    <p>The Windows version is not signed yet. Click More info, then Run anyway. See <a href="windows.html">Kastideo for Windows</a>.</p>

    <h2 id="android-tv">How do I install Kastideo on Android TV?</h2>
    <p>Outside Google Play, with the Downloader app, a USB stick or by sending it from a phone. See <a href="guide-android-tv.html">Install Kastideo on Android TV</a>.</p>

    <h2 id="donnees">What happens to my password?</h2>
    <p>Your credentials stay on your device, in the system's secure store, and are sent only to the services you configure. Kastideo collects no usage statistics. See the <a href="confidentialite.html">privacy policy</a>.</p>

    <h2 id="probleme">A channel does not start, what should I do?</h2>
    <p>First turn off any VPN, check that no other device uses your subscription, then look at the playback log. See <a href="fiabilite.html#journal">Fast, stable and frugal</a>.</p>

    <h2 id="contact">How can I contact you?</h2>
    <p>By e-mail at <code>contact@kastideo.com</code>, or on <a href="https://github.com/jihemezes/kastideo/issues" target="_blank" rel="noopener">GitHub</a> for a problem or an idea.</p>
"""

COMPARE = [
    {"slug": "alternative-vlc", "title_fr": "Alternative à VLC", "title_en": "VLC alternative",
     "blurb_fr": "Kastideo ou VLC pour regarder l'IPTV : ce qui change au quotidien.",
     "blurb_en": "Kastideo or VLC for watching IPTV: what changes day to day.", "fr": VLC_FR, "en": VLC_EN},
    {"slug": "alternative-tivimate", "title_fr": "Alternative à TiviMate", "title_en": "TiviMate alternative",
     "blurb_fr": "Un lecteur gratuit qui existe aussi sur Mac, Windows et Linux.",
     "blurb_en": "A free player that also runs on Mac, Windows and Linux.", "fr": TIVI_FR, "en": TIVI_EN},
    {"slug": "alternative-iptv-smarters", "title_fr": "Alternative à IPTV Smarters Pro", "title_en": "IPTV Smarters Pro alternative",
     "blurb_fr": "Un lecteur indépendant, sans marque de fournisseur.",
     "blurb_en": "An independent player, with no provider branding.", "fr": SMART_FR, "en": SMART_EN},
    {"slug": "faq", "title_fr": "Questions fréquentes", "title_en": "Frequently asked questions",
     "blurb_fr": "Gratuit ? Sources ? Appareils ? Les réponses courtes.",
     "blurb_en": "Free? Sources? Devices? Short answers.", "fr": FAQ_FR, "en": FAQ_EN},
]
