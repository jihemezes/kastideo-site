"""Pages de détail des fonctions (texte FR et EN).

Chaque page : slug, titres, courte description, texte FR et EN.
Le texte reprend l'aide intégrée de l'application (docs/help du dépôt kastideo).
"""

FEATURES = [
    # ------------------------------------------------------------------ DIRECT
    {
        "slug": "direct",
        "title_fr": "Regarder le direct",
        "title_en": "Watching live TV",
        "blurb_fr": "Démarrage rapide, santé du flux, différé, version de chaîne adaptée à votre connexion.",
        "blurb_en": "Fast start, stream health, timeshift, channel version matched to your connection.",
        "desc": "Le direct dans Kastideo : démarrage rapide, santé du flux, direct en différé et gestion des versions de chaînes.",
        "fr": """    <h1>Regarder le direct</h1>
    <p class="page-lead">Choisissez une chaîne et elle démarre, en moins d'une seconde en général. Kastideo garde ensuite la main : santé du flux, différé, version adaptée à votre connexion.</p>

    <h2 id="lancer">Lancer une chaîne</h2>
    <p>La lecture démarre dès que vous sélectionnez une chaîne. Pendant l'ouverture, le logo et le nom de la chaîne s'affichent, puis un badge « Prête en x s » indique le temps de démarrage. Les commandes apparaissent au survol : pause, volume, mode cinéma.</p>
    <p>Un double-clic passe en mode cinéma : la fenêtre se met en plein écran et seule la vidéo reste affichée. Échap en sort.</p>

    <h2 id="sante">Savoir si le flux est bon</h2>
    <p>Une pastille de santé indique la qualité de réception : verte (Excellent), orange (Correct) ou rouge (Instable), avec la définition de l'image (SD, HD, Full HD ou 4K). Au survol, vous voyez le débit, les images par seconde, les images perdues et les coupures de la dernière minute.</p>
    <p>Sur Mac, un panneau Informations affiche le programme en cours et à venir, le choix de la piste audio (langue, audiodescription) et des sous-titres.</p>

    <h2 id="differe">Direct en différé</h2>
    <p>Mettez une chaîne en pause : Kastideo continue de recevoir le flux et le garde en réserve. À la reprise, vous regardez en différé, signalé par un indicateur jaune (par exemple « DIFFÉRÉ −2:34 »).</p>
    <ul>
      <li>Une timeline va du moment de la pause (à gauche) jusqu'au direct (à droite). Glissez le curseur vers la droite : la lecture accélère jusqu'au point choisi, puis revient à vitesse normale.</li>
      <li>Les vitesses ×1,25, ×1,5 et ×2 permettent de grignoter le retard. Le bouton Rattraper accélère jusqu'au direct sans rien sauter.</li>
      <li>Retour au direct revient tout de suite à l'antenne.</li>
      <li>La durée maximale du différé se règle dans les réglages de lecture.</li>
    </ul>
    <div class="callout"><b class="label">À savoir</b><p>Le différé est stocké dans un dossier temporaire de l'application, effacé au changement de chaîne. Comptez 1 à 4 Go par heure selon la qualité du flux.</p></div>

    <h2 id="une-connexion">Une seule connexion à la fois</h2>
    <p>La plupart des abonnements IPTV n'autorisent qu'un flux simultané. Kastideo ferme toujours le flux en cours avant d'ouvrir le suivant : vous pouvez zapper sans risquer de dépasser votre limite. Avant d'interrompre un enregistrement, il vous demande votre accord.</p>
    <p>Si une chaîne ne démarre pas, vérifiez qu'aucun autre appareil (téléviseur, téléphone) n'utilise le même abonnement, et coupez un éventuel VPN.</p>

    <h2 id="versions-chaine">Plusieurs versions d'une même chaîne</h2>
    <p>Beaucoup de fournisseurs proposent une chaîne en plusieurs versions (4K, FHD, HD, SD). Dans la vue par thèmes, Kastideo n'en affiche qu'une et choisit la plus adaptée à votre connexion : il descend d'un cran après une lecture instable et remonte après trois lectures fluides. Un clic droit sur la chaîne permet de choisir une autre version.</p>

    <h2 id="retrouver">Retrouver et corriger vos chaînes</h2>
    <ul>
      <li><b>Favoris et récents</b> : une étoile ou un clic droit ajoute un favori. Les récents gardent les 60 derniers contenus regardés, avec suppression multiple et bouton Annuler.</li>
      <li><b>Recherche</b> : un seul champ cherche dans les chaînes, les films et les séries.</li>
      <li><b>Catégories</b> : réordonnez, masquez ou renommez celles de votre fournisseur, ou masquez par mot-clé. Fini les catégories de pays que vous ne regardez jamais.</li>
      <li><b>Corriger une chaîne</b> : un clic droit permet de changer son nom, son numéro, son logo et la chaîne du guide TV qui lui correspond.</li>
    </ul>
""",
        "en": """    <h1>Watching live TV</h1>
    <p class="page-lead">Pick a channel and it starts, usually in under a second. Kastideo then keeps you in control: stream health, timeshift, a version matched to your connection.</p>

    <h2 id="lancer">Starting a channel</h2>
    <p>Playback starts as soon as you select a channel. While it opens, the channel logo and name are shown, then a “Ready in x s” badge tells you the start time. Controls appear on hover: pause, volume, cinema mode.</p>
    <p>A double-click switches to cinema mode: the window goes full screen and only the video stays. Esc leaves it.</p>

    <h2 id="sante">Knowing if the stream is good</h2>
    <p>A health pill shows reception quality: green (Excellent), orange (Fair) or red (Unstable), with the picture definition (SD, HD, Full HD or 4K). On hover you see the bitrate, frames per second, dropped frames and interruptions from the last minute.</p>
    <p>On Mac, an Information panel shows the current and upcoming programme, the audio track (language, audio description) and subtitles.</p>

    <h2 id="differe">Live timeshift</h2>
    <p>Pause a channel: Kastideo keeps receiving the stream and stores it. When you resume, you watch time-shifted, shown by a yellow indicator (for example “DELAYED −2:34”).</p>
    <ul>
      <li>A timeline runs from the moment you paused (left) to live (right). Drag the cursor right: playback speeds up to the chosen point, then returns to normal speed.</li>
      <li>Speeds ×1.25, ×1.5 and ×2 let you eat into the delay. The Catch up button speeds up to live without skipping anything.</li>
      <li>Back to live returns to the broadcast immediately.</li>
      <li>The maximum timeshift length is set in the playback settings.</li>
    </ul>
    <div class="callout"><b class="label">Good to know</b><p>Timeshift is stored in a temporary folder of the app, cleared when you change channel. Allow 1 to 4 GB per hour depending on stream quality.</p></div>

    <h2 id="une-connexion">One connection at a time</h2>
    <p>Most IPTV subscriptions allow only one simultaneous stream. Kastideo always closes the current stream before opening the next: you can zap without risk of exceeding your limit. Before interrupting a recording, it asks for your approval.</p>
    <p>If a channel does not start, check that no other device (TV, phone) is using the same subscription, and turn off any VPN.</p>

    <h2 id="versions-chaine">Several versions of one channel</h2>
    <p>Many providers offer a channel in several versions (4K, FHD, HD, SD). In the themes view, Kastideo shows only one and picks the best fit for your connection: it steps down after an unstable playback and steps up after three smooth ones. A right-click on the channel lets you choose another version.</p>

    <h2 id="retrouver">Finding and fixing your channels</h2>
    <ul>
      <li><b>Favourites and recents</b>: a star or a right-click adds a favourite. Recents keep the last 60 items watched, with multiple deletion and an Undo button.</li>
      <li><b>Search</b>: one field searches channels, movies and series.</li>
      <li><b>Categories</b>: reorder, hide or rename your provider's categories, or hide by keyword. No more country categories you never watch.</li>
      <li><b>Fix a channel</b>: a right-click lets you change its name, number, logo and the TV guide channel it matches.</li>
    </ul>
""",
    },
    # ---------------------------------------------------------------- GUIDE TV
    {
        "slug": "guide-tv",
        "title_fr": "Guide TV et thèmes",
        "title_en": "TV guide and themes",
        "blurb_fr": "Guide en grille, chaînes classées par thème, « Ce soir », alertes avant vos émissions.",
        "blurb_en": "Grid guide, channels sorted by theme, “Tonight”, alerts before your shows.",
        "desc": "Le guide TV en grille de Kastideo, le classement des chaînes par thème, la vue Ce soir et les alertes de programme.",
        "fr": """    <h1>Guide TV et thèmes</h1>
    <p class="page-lead">Un guide en grille pour voir toute la soirée d'un coup d'œil, et un classement par thème pour trouver le sport, les films ou l'info du moment.</p>

    <h2 id="grille">Le guide en grille</h2>
    <p>Les chaînes sont en lignes, les heures en colonnes, avec un trait rouge sur l'heure actuelle. Les flèches décalent la grille, Maintenant revient à l'heure présente, et le menu de la date saute à un autre jour. La durée affichée se règle sur 2, 3 ou 6 heures.</p>
    <ul>
      <li>Filtrez par favoris, récents, catégorie ou thème, ou cherchez une chaîne.</li>
      <li>Un clic sur un programme ouvre sa fiche : description, bouton Regarder, Enregistrer (programme en cours) ou Programmer l'enregistrement (programme à venir).</li>
      <li>Un point rouge signale un enregistrement programmé, une cloche permet de se faire alerter au début.</li>
    </ul>

    <h2 id="secours">Un guide de secours quand celui du fournisseur est incomplet</h2>
    <p>Si le guide de votre fournisseur est vide ou lacunaire, Kastideo peut en charger un second (xmltvfr.fr) et associe automatiquement ses chaînes aux vôtres d'après leur nom. Vous pouvez aussi corriger l'association à la main, chaîne par chaîne.</p>

    <h2 id="themes">Les thèmes</h2>
    <p>Le direct est classé par thème : Sport, Auto-Moto, Films, Séries, Info, Documentaires, Nature, Jeunesse, Divertissement, Cuisine et Maison, Musique, Généralistes, Régional, International, Religion et Radio. Trois modes :</p>
    <ul>
      <li><b>En ce moment</b> : ce qui est diffusé maintenant, classé d'après le genre du programme dans le guide. Un film sur une chaîne généraliste apparaît donc dans « Films », avec sa progression.</li>
      <li><b>Ce soir</b> : les programmes qui commencent entre 20 h et 23 h.</li>
      <li><b>Chaînes</b> : les chaînes classées par spécialité. Le thème est déduit du nom de la chaîne, puis de ses programmes habituels, et se corrige d'un clic droit.</li>
    </ul>
    <p>Dans Sport, une seconde rangée filtre par discipline : football, rugby, tennis, basket, sports de combat, golf, cyclisme, handball, sports mécaniques, sports d'hiver, hippisme, athlétisme et natation. Les chaînes sans programme au guide restent proposées quand leur nom suffit à les classer (une chaîne de sport, par exemple).</p>
    <div class="callout"><b class="label">À savoir</b><p>Les contenus adultes sont masqués partout par défaut. Un réglage permet de les afficher.</p></div>

    <h2 id="alertes">Alertes de programme</h2>
    <p>Kastideo vous prévient deux minutes avant le début d'une émission : un programme précis, un titre qui contient un mot choisi (« Formule 1 », le nom d'une équipe), ou un thème sur vos chaînes favorites. Une notification et un bandeau Regarder apparaissent, même si la fenêtre était réduite.</p>
""",
        "en": """    <h1>TV guide and themes</h1>
    <p class="page-lead">A grid guide to see the whole evening at a glance, and a theme view to find sport, films or news right now.</p>

    <h2 id="grille">The grid guide</h2>
    <p>Channels are in rows, hours in columns, with a red line on the current time. Arrows shift the grid, Now returns to the present time, and the date menu jumps to another day. The displayed span can be 2, 3 or 6 hours.</p>
    <ul>
      <li>Filter by favourites, recents, category or theme, or search for a channel.</li>
      <li>A click on a programme opens its sheet: description, Watch button, Record (current programme) or Schedule recording (upcoming programme).</li>
      <li>A red dot marks a scheduled recording, and a bell lets you get an alert at the start.</li>
    </ul>

    <h2 id="secours">A backup guide when your provider's is incomplete</h2>
    <p>If your provider's guide is empty or patchy, Kastideo can load a second one (xmltvfr.fr) and automatically matches its channels to yours by name. You can also fix the match by hand, channel by channel.</p>

    <h2 id="themes">Themes</h2>
    <p>Live TV is sorted by theme: Sport, Motor, Films, Series, News, Documentaries, Nature, Kids, Entertainment, Cooking and Home, Music, General, Regional, International, Religion and Radio. Three modes:</p>
    <ul>
      <li><b>Now</b>: what is on right now, sorted by the programme's genre in the guide. A film on a general channel therefore appears under “Films”, with its progress.</li>
      <li><b>Tonight</b>: programmes starting between 8 pm and 11 pm.</li>
      <li><b>Channels</b>: channels sorted by specialty. The theme is deduced from the channel name, then from its usual programmes, and can be corrected with a right-click.</li>
    </ul>
    <p>Under Sport, a second row filters by discipline: football, rugby, tennis, basketball, combat sports, golf, cycling, handball, motor sports, winter sports, horse racing, athletics and swimming. Channels with no programme in the guide are still shown when their name is enough to classify them (a sports channel, for example).</p>
    <div class="callout"><b class="label">Good to know</b><p>Adult content is hidden everywhere by default. A setting lets you show it.</p></div>

    <h2 id="alertes">Programme alerts</h2>
    <p>Kastideo warns you two minutes before a show starts: a specific programme, a title containing a word you chose (“Formula 1”, a team name), or a theme on your favourite channels. A notification and a Watch banner appear, even if the window was minimised.</p>
""",
    },
    # -------------------------------------------------------------- INTERFACES
    {
        "slug": "interfaces",
        "title_fr": "Interfaces et personnalisation",
        "title_en": "Interfaces and personalisation",
        "blurb_fr": "Classique, Cinéma ou TV, au choix pour chaque type de contenu, et tout ce qui se règle.",
        "blurb_en": "Classic, Cinema or TV, chosen per content type, and everything you can adjust.",
        "desc": "Les trois interfaces de Kastideo (Classique, Cinéma, TV), l'apparence, la page de départ, les catégories et la sauvegarde de la configuration.",
        "fr": """    <h1>Interfaces et personnalisation</h1>
    <p class="page-lead">Kastideo se présente comme vous préférez, et peut même changer de visage selon ce que vous regardez : une interface pour le direct, une autre pour les films.</p>

    <h2 id="trois">Trois interfaces au choix</h2>
    <p>Le choix se fait séparément pour le direct, les films, les séries, et les favoris et récents.</p>
    <ul>
      <li><b>Classique</b> : trois colonnes, avec la barre latérale, la liste (et le programme en cours de chaque chaîne) et le lecteur ou la fiche à droite. C'est l'interface par défaut.</li>
      <li><b>Cinéma</b> : un grand bandeau « à la une » qui défile, puis des rangées horizontales : reprise de lecture, favoris et une rangée par catégorie. Les films et séries s'affichent en affiches, les chaînes en vignettes avec le programme en cours. Un clic sur un film ouvre sa fiche.</li>
      <li><b>TV</b> (direct uniquement) : la chaîne en plein cadre, comme sur un téléviseur. Flèches haut et bas pour zapper, chiffres pour saisir un numéro, flèche gauche pour la liste des chaînes, B pour revenir à la chaîne précédente, G pour le guide.</li>
    </ul>
    <p>Un exemple courant : TV pour le direct et Cinéma pour les films et les séries.</p>

    <h2 id="bandeau">Le bandeau « à la une »</h2>
    <p>En interface Cinéma, un carrousel pleine largeur met en avant des films et séries : une catégorie de votre choix, les tendances de la semaine (via TMDB) trouvées dans votre catalogue et les derniers ajouts de votre fournisseur. Pour le direct, il montre les programmes en cours de vos chaînes favorites et récentes. Vous réglez la hauteur, la pause au survol et le bouton bande-annonce, ou vous le masquez. Un filtre par pays et par langue permet de n'afficher que ce qui vous intéresse.</p>

    <h2 id="apparence">Apparence</h2>
    <ul>
      <li>Thème sombre, clair, ou celui du système.</li>
      <li>Couleur d'accent au choix : bleu, violet, rose, rouge, orange, vert ou turquoise.</li>
      <li>Densité des listes (compacte, standard, aérée) et taille des vignettes.</li>
      <li>Le lecteur, l'accueil, les fiches et l'interface TV restent sombres, pour le confort devant l'écran.</li>
    </ul>

    <h2 id="depart">Page de départ</h2>
    <p>Pour Direct, Films et Séries, choisissez ce qui s'affiche à l'ouverture : tout le catalogue, vos favoris, vos récents, le dernier contenu regardé ou une catégorie précise.</p>

    <h2 id="categories">Catégories et ordre</h2>
    <p>Une fenêtre dédiée permet de réordonner, masquer et renommer les catégories de chaque section, de les trier de A à Z et de masquer par mot-clé. Sur Windows, Linux et Android, vous pouvez aussi arranger l'ordre des chaînes elles-mêmes, par glisser-déposer, les déplacer vers une autre catégorie ou une liste personnelle, et rétablir l'ordre d'origine.</p>

    <h2 id="sauvegarde">Sauvegarde et transfert</h2>
    <p>Un fichier de configuration regroupe vos sources, favoris, récents, catégories, interfaces et clé TMDB, avec les mots de passe si vous le décidez. Le format est le même sur Mac, Windows, Linux et Android : vous passez d'un ordinateur à l'autre en un clic, ou vous retrouvez tout après un changement de machine.</p>
""",
        "en": """    <h1>Interfaces and personalisation</h1>
    <p class="page-lead">Kastideo looks the way you prefer, and can even change its face depending on what you watch: one interface for live TV, another for movies.</p>

    <h2 id="trois">Three interfaces to choose from</h2>
    <p>The choice is made separately for live TV, movies, series, and favourites and recents.</p>
    <ul>
      <li><b>Classic</b>: three columns, with the sidebar, the list (and each channel's current programme) and the player or details on the right. This is the default interface.</li>
      <li><b>Cinema</b>: a large scrolling “featured” banner, then horizontal rows: resume playback, favourites and one row per category. Movies and series appear as posters, channels as thumbnails with the current programme. A click on a movie opens its details page.</li>
      <li><b>TV</b> (live only): the channel full frame, like on a television. Up and down arrows to zap, digits to type a number, left arrow for the channel list, B to go back to the previous channel, G for the guide.</li>
    </ul>
    <p>A common setup: TV for live and Cinema for movies and series.</p>

    <h2 id="bandeau">The “featured” banner</h2>
    <p>In Cinema, a full-width carousel highlights movies and series: a category of your choice, weekly trends (via TMDB) found in your catalogue and your provider's latest additions. For live TV, it shows the current programmes of your favourite and recent channels. You set its height, pause on hover and the trailer button, or hide it. A country and language filter lets you show only what interests you.</p>

    <h2 id="apparence">Appearance</h2>
    <ul>
      <li>Dark, light, or system theme.</li>
      <li>Accent colour of your choice: blue, purple, pink, red, orange, green or teal.</li>
      <li>List density (compact, standard, airy) and thumbnail size.</li>
      <li>The player, home screen, details pages and TV interface stay dark, for comfort in front of the screen.</li>
    </ul>

    <h2 id="depart">Start page</h2>
    <p>For Live, Movies and Series, choose what is shown at launch: the whole catalogue, your favourites, your recents, the last item watched or a specific category.</p>

    <h2 id="categories">Categories and order</h2>
    <p>A dedicated window lets you reorder, hide and rename the categories of each section, sort them A to Z and hide by keyword. On Windows, Linux and Android, you can also arrange the order of the channels themselves by drag and drop, move them to another category or a personal list, and restore the original order.</p>

    <h2 id="sauvegarde">Backup and transfer</h2>
    <p>One configuration file gathers your sources, favourites, recents, categories, interfaces and TMDB key, with passwords if you decide so. The format is the same on Mac, Windows, Linux and Android: you move from one computer to another in one click, or restore everything after changing machines.</p>
""",
    },
    # --------------------------------------------------------------- MULTIVUE
    {
        "slug": "multivue",
        "title_fr": "MultiVue",
        "title_en": "MultiView",
        "blurb_fr": "Jusqu'à quatre chaînes à l'écran, avec le son sur la vignette active.",
        "blurb_en": "Up to four channels on screen, with sound on the active tile.",
        "desc": "La MultiVue de Kastideo : jusqu'à quatre chaînes en direct dans une fenêtre, si votre abonnement autorise plusieurs connexions.",
        "fr": """    <h1>MultiVue</h1>
    <p class="page-lead">Suivez plusieurs matchs, plusieurs chaînes d'info ou une soirée électorale sur un seul écran : jusqu'à quatre chaînes en direct, le son suit la vignette que vous choisissez.</p>

    <h2 id="principe">Comment ça marche</h2>
    <p>La MultiVue affiche de une à quatre chaînes : une en plein cadre, deux côte à côte, trois ou quatre en grille. Le son suit la vignette active, entourée d'orange. Cliquez sur une vignette, ou appuyez sur les touches 1 à 4, pour l'activer.</p>
    <ul>
      <li>Le bouton + ajoute une chaîne depuis vos favoris, vos récents ou la recherche.</li>
      <li>Au survol d'une vignette, vous pouvez changer sa chaîne ou la retirer. Le nom de la chaîne et le programme en cours s'affichent en bas.</li>
      <li>Tout arrêter coupe tous les flux.</li>
    </ul>
    <p>Vous choisissez le nombre d'écrans (de 1 à 4) et la disposition : côte à côte, empilé, grille, ou une grande image avec les autres en petites vignettes flottantes. Dans cette dernière, vous déplacez les vignettes, qui s'accrochent au coin le plus proche, et vous les échangez avec la grande par un double-clic. Sur Windows, Linux et Android, vous pouvez aussi mémoriser un groupe de chaînes sous un nom (par exemple « Multiplex foot ») pour le rouvrir d'un clic.</p>

    <!--shot:multivue-pip-->

    <h2 id="sources">Plusieurs abonnements ou listes publiques</h2>
    <p>Si vous avez plusieurs sources de direct, la MultiVue les mélange : deux abonnements, ou un abonnement et une liste de chaînes publiques. Chaque source a son propre nombre de connexions, par exemple 1 pour un abonnement limité et 4 pour une liste publique. Chaque écran est réservé à une source, et son sélecteur de chaînes ne propose que les chaînes de cette source. Le sélecteur reprend l'interface Classique : favoris, récents et catégories à gauche, chaînes avec leur programme en cours à droite.</p>

    <h2 id="pip">Image dans l'image</h2>
    <p>Pendant un direct, le bouton image dans l'image ouvre une seconde chaîne en miniature dans un coin du lecteur, sans le son. Un clic sur la miniature l'échange avec la chaîne principale. La seconde chaîne doit venir d'une source qui a une connexion libre : avec un seul abonnement limité à une connexion, choisissez une chaîne d'une liste publique ou d'un second abonnement.</p>

    <h2 id="connexions">Pourquoi elle est désactivée par défaut</h2>
    <p>Chaque chaîne utilise une connexion à votre fournisseur. Comme la plupart des abonnements n'en autorisent qu'une, la MultiVue reste désactivée tant que vous n'avez pas indiqué le nombre de connexions simultanées de votre abonnement, de 2 à 4, dans les réglages de lecture. Pour une source Xtream, le bouton Tester la connexion affiche ce nombre.</p>
    <div class="callout"><b class="label">À savoir</b><p>Un enregistrement ou un téléchargement occupe aussi une connexion. Si une vignette affiche « La chaîne ne répond pas », le fournisseur refuse probablement une connexion de plus : retirez une chaîne.</p></div>

    <h2 id="ouvrir">L'ouvrir</h2>
    <p>Par le menu Lecture, par un clic droit sur une chaîne (Ajouter à la MultiVue), ou par un raccourci clavier. La chaîne que vous regardiez devient la première vignette, et la lecture principale s'arrête pour libérer sa connexion, sauf si elle est en cours d'enregistrement.</p>
""",
        "en": """    <h1>MultiView</h1>
    <p class="page-lead">Follow several matches, several news channels or an election night on a single screen: up to four live channels, with sound following the tile you pick.</p>

    <h2 id="principe">How it works</h2>
    <p>MultiView shows one to four channels: one full frame, two side by side, three or four in a grid. Sound follows the active tile, outlined in orange. Click a tile, or press keys 1 to 4, to activate it.</p>
    <ul>
      <li>The + button adds a channel from your favourites, recents or search.</li>
      <li>On hover, you can change a tile's channel or remove it. The channel name and current programme are shown at the bottom.</li>
      <li>Stop all cuts every stream.</li>
    </ul>
    <p>You choose the number of screens (1 to 4) and the layout: side by side, stacked, grid, or one big picture with the others as small floating tiles. In the latter, you move the tiles, which snap to the nearest corner, and swap them with the big one by double-clicking. On Windows, Linux and Android, you can also save a group of channels under a name (for example “Football multiplex”) to reopen it in one click.</p>

    <!--shot:multivue-pip-->

    <h2 id="sources">Several subscriptions or public lists</h2>
    <p>If you have several live sources, MultiView mixes them: two subscriptions, or a subscription and a list of public channels. Each source has its own number of connections, for example 1 for a limited subscription and 4 for a public list. Each screen is reserved for one source, and its channel picker only offers that source's channels. The picker follows the Classic interface: favourites, recents and categories on the left, channels with their current programme on the right.</p>

    <h2 id="pip">Picture in picture</h2>
    <p>During live TV, the picture-in-picture button opens a second channel as a thumbnail in a corner of the player, without sound. A click on the thumbnail swaps it with the main channel. The second channel must come from a source with a free connection: with a single subscription limited to one connection, pick a channel from a public list or from a second subscription.</p>

    <h2 id="connexions">Why it is off by default</h2>
    <p>Each channel uses one connection to your provider. Since most subscriptions allow only one, MultiView stays disabled until you enter the number of simultaneous connections of your subscription, from 2 to 4, in the playback settings. For an Xtream source, the Test connection button shows this number.</p>
    <div class="callout"><b class="label">Good to know</b><p>A recording or a download also uses one connection. If a tile shows “The channel is not responding”, the provider probably refuses one more connection: remove a channel.</p></div>

    <h2 id="ouvrir">Opening it</h2>
    <p>From the Playback menu, with a right-click on a channel (Add to MultiView), or with a keyboard shortcut. The channel you were watching becomes the first tile, and main playback stops to free its connection, unless it is being recorded.</p>
""",
    },
    # -------------------------------------------------------------- ENREGISTRER
    {
        "slug": "enregistrer",
        "title_fr": "Enregistrer et télécharger",
        "title_en": "Recording and downloading",
        "blurb_fr": "Enregistrement immédiat ou programmé, téléchargement de films et séries, même la nuit.",
        "blurb_en": "Immediate or scheduled recording, movie and series downloads, even overnight.",
        "desc": "Enregistrer le direct, programmer un enregistrement, répéter, télécharger des films et des séries, avec les règles de connexion unique.",
        "fr": """    <h1>Enregistrer et télécharger</h1>
    <p class="page-lead">Gardez une émission pour plus tard, ou téléchargez un film pendant la nuit pour le regarder sans connexion. Tout se retrouve dans la section Enregistrements.</p>

    <h2 id="direct">Enregistrer le direct</h2>
    <p>Un bouton rouge dans la barre du lecteur lance l'enregistrement de la chaîne regardée. Il s'arrête à la fin du programme en cours (d'après le guide TV, plus une marge) ou quand vous l'arrêtez. L'enregistrement utilise la même connexion que la lecture : il ne consomme rien de plus sur votre abonnement.</p>
    <p>Un clic droit sur une autre chaîne permet de l'enregistrer en arrière-plan : si vous en regardez une autre, Kastideo demande s'il faut arrêter la lecture.</p>
    <ul>
      <li>Sur Mac, le fichier est visible et grossit dans un sous-dossier « En cours » pendant l'enregistrement. À la fin, il est converti sans perte en MP4, lisible par QuickTime, l'iPhone et l'iPad.</li>
      <li>Sur Windows et Linux, le flux est recopié tel quel puis converti sans perte en MKV, ou gardé en .ts si la conversion échoue.</li>
    </ul>

    <h2 id="programmer">Programmer un enregistrement</h2>
    <p>Depuis le guide TV ou par un clic droit sur une chaîne, programmez un programme du guide ou une plage horaire libre. Des marges avant et après (2 et 5 minutes par défaut sur Mac) évitent de rater le début ou la fin. Sur Windows, Linux et Android, vous pouvez répéter : une seule fois, tous les jours, du lundi au vendredi ou chaque semaine.</p>
    <div class="callout"><b class="label">À savoir</b><p>Kastideo doit être ouvert, et l'appareil allumé, à l'heure prévue. Sur Mac, il empêche la mise en veille automatique pendant l'activité. Sur Windows et Linux, un réglage le lance à l'ouverture de session.</p></div>

    <h2 id="telecharger">Télécharger un film ou une série</h2>
    <p>Un clic droit sur un film ou un épisode propose Télécharger, ou Télécharger cette nuit (à 2 h par défaut, réglable). Pour une série, la fiche permet de télécharger la saison affichée ou toute la série.</p>
    <ul>
      <li>Les téléchargements passent l'un après l'autre, avec pause, reprise après une coupure et annulation.</li>
      <li>Un indicateur permanent montre l'avancement, l'épisode en cours, la vitesse et le temps restant estimé.</li>
    </ul>

    <h2 id="priorite">Qui a la priorité ?</h2>
    <p>Comme votre abonnement n'autorise le plus souvent qu'une connexion, Kastideo ne fait qu'une chose à la fois et vous demande toujours avant d'interrompre quelque chose. Changer de chaîne pendant un enregistrement demande si l'enregistrement doit s'arrêter. Lancer une lecture pendant un téléchargement met celui-ci en pause : il reprend tout seul ensuite.</p>

    <h2 id="fichiers">Vos fichiers</h2>
    <p>Les enregistrements sont rangés dans un dossier de votre choix (par défaut Films/Kastideo sur Mac, Vidéos/Kastideo sur Windows et Linux), avec des noms automatiques comme « TF1 – Le goût du détail – 2026-10-18 20h50 ». Un nettoyage automatique facultatif met à la corbeille les anciens enregistrements, et une alerte prévient quand l'espace disque devient faible.</p>
    <p>Les enregistrements sont réservés à un usage privé, dans les limites de la loi de votre pays.</p>
""",
        "en": """    <h1>Recording and downloading</h1>
    <p class="page-lead">Keep a show for later, or download a movie overnight to watch it offline. Everything is found in the Recordings section.</p>

    <h2 id="direct">Recording live TV</h2>
    <p>A red button in the player bar starts recording the channel you are watching. It stops at the end of the current programme (from the TV guide, plus a margin) or when you stop it. Recording uses the same connection as playback: it consumes nothing more on your subscription.</p>
    <p>A right-click on another channel lets you record it in the background: if you are watching a different one, Kastideo asks whether to stop playback.</p>
    <ul>
      <li>On Mac, the file is visible and grows in an “In progress” sub-folder during recording. At the end, it is converted without loss to MP4, playable by QuickTime, iPhone and iPad.</li>
      <li>On Windows and Linux, the stream is copied as-is then converted without loss to MKV, or kept as .ts if conversion fails.</li>
    </ul>

    <h2 id="programmer">Scheduling a recording</h2>
    <p>From the TV guide or with a right-click on a channel, schedule a guide programme or a free time slot. Margins before and after (2 and 5 minutes by default on Mac) avoid missing the start or the end. On Windows, Linux and Android, you can repeat: once, every day, Monday to Friday or every week.</p>
    <div class="callout"><b class="label">Good to know</b><p>Kastideo must be open, and the device on, at the scheduled time. On Mac, it prevents automatic sleep during activity. On Windows and Linux, a setting launches it at sign-in.</p></div>

    <h2 id="telecharger">Downloading a movie or a series</h2>
    <p>A right-click on a movie or an episode offers Download, or Download tonight (at 2 am by default, adjustable). For a series, the details page lets you download the displayed season or the whole series.</p>
    <ul>
      <li>Downloads run one after another, with pause, resume after an interruption and cancel.</li>
      <li>A permanent indicator shows progress, the current episode, speed and estimated time left.</li>
    </ul>

    <h2 id="priorite">Who has priority?</h2>
    <p>Since your subscription usually allows only one connection, Kastideo does one thing at a time and always asks before interrupting something. Changing channel during a recording asks whether the recording should stop. Starting playback during a download pauses it: it resumes by itself afterwards.</p>

    <h2 id="fichiers">Your files</h2>
    <p>Recordings are stored in a folder of your choice (by default Movies/Kastideo on Mac, Videos/Kastideo on Windows and Linux), with automatic names like “TF1 – Le goût du détail – 2026-10-18 20h50”. An optional automatic clean-up sends old recordings to the trash, and an alert warns you when disk space runs low.</p>
    <p>Recordings are for private use only, within the limits of the law in your country.</p>
""",
    },
    # --------------------------------------------------------------------- CAST
    {
        "slug": "cast",
        "title_fr": "Envoyer à la télévision",
        "title_en": "Casting to a TV",
        "blurb_fr": "Chromecast, Google TV, Android TV, et AirPlay sur Mac : la barre de lecture devient télécommande.",
        "blurb_en": "Chromecast, Google TV, Android TV, and AirPlay on Mac: the playback bar becomes a remote.",
        "desc": "Diffuser une chaîne, un film, une série ou YouTube de Kastideo vers un téléviseur Chromecast, Google TV ou Android TV, ou une Apple TV par recopie d'écran.",
        "fr": """    <h1>Envoyer à la télévision</h1>
    <p class="page-lead">Envoyez ce que vous regardez vers un téléviseur du même réseau, sans quitter Kastideo. La barre de lecture reste votre télécommande.</p>

    <h2 id="compatible">Ce qui est possible</h2>
    <ul>
      <li><b>Chromecast, Google TV, Android TV</b>, et beaucoup de téléviseurs avec Chromecast intégré : la lecture entière part sur le téléviseur. Chaîne en direct, film, série ou vidéo locale.</li>
      <li><b>Apple TV (AirPlay)</b> : Kastideo ne peut pas envoyer la vidéo directement en AirPlay. Sur Mac, utilisez la recopie d'écran de macOS, puis lisez Kastideo en plein écran. Un raccourci vers les réglages d'écran est proposé dans le menu du bouton téléviseur.</li>
      <li><b>YouTube</b> : la vidéo s'ouvre dans l'application YouTube du téléviseur, ou dans le navigateur avec le bouton Diffuser de Chrome, au choix dans les réglages.</li>
    </ul>

    <h2 id="faire">Diffuser en quatre gestes</h2>
    <ol>
      <li>Lancez une chaîne, un film, une série ou une vidéo.</li>
      <li>Cliquez sur le bouton téléviseur de la barre de lecture.</li>
      <li>Choisissez l'appareil dans la liste (Chercher à nouveau si rien n'apparaît : le téléviseur doit être allumé et sur le même réseau).</li>
      <li>L'image part sur le téléviseur, et la lecture reprend là où vous en étiez.</li>
    </ol>
    <p>Pause, lecture, avance et recul, position, volume et sourdine de la barre agissent sur le téléviseur. Pour revenir, choisissez Arrêter la diffusion : la lecture reprend sur l'ordinateur à la même position.</p>

    <h2 id="limites">Limites à connaître</h2>
    <ul>
      <li>Une seule connexion à votre fournisseur : pendant la diffusion, l'ordinateur ne lit plus la chaîne.</li>
      <li>Le direct ne permet pas de se déplacer dans le temps pendant la diffusion, et le différé de l'ordinateur est coupé.</li>
      <li>L'enregistrement d'une chaîne et la MultiVue ne se combinent pas avec la diffusion.</li>
      <li>Il y a quelques secondes de décalage, plus qu'avec une lecture locale.</li>
    </ul>

    <h2 id="plateformes">Selon votre appareil</h2>
    <ul>
      <li><b>Mac</b> : macOS demande au premier usage l'autorisation de trouver des appareils sur le réseau local. Acceptez, sinon aucun téléviseur n'apparaît.</li>
      <li><b>Windows et Linux</b> : Kastideo prépare la vidéo avec ffmpeg avant l'envoi (fourni avec la version Windows et l'AppImage, à installer avec le paquet .deb). Le pare-feu de Windows peut demander d'autoriser Kastideo : acceptez sur les réseaux privés.</li>
      <li><b>Android</b> : la diffusion se fait en mode direct, l'adresse du flux étant envoyée telle quelle au téléviseur. Les fichiers locaux ne peuvent pas être diffusés.</li>
    </ul>
""",
        "en": """    <h1>Casting to a TV</h1>
    <p class="page-lead">Send what you are watching to a TV on the same network, without leaving Kastideo. The playback bar stays your remote control.</p>

    <h2 id="compatible">What is possible</h2>
    <ul>
      <li><b>Chromecast, Google TV, Android TV</b>, and many TVs with built-in Chromecast: the whole playback moves to the TV. Live channel, movie, series or local video.</li>
      <li><b>Apple TV (AirPlay)</b>: Kastideo cannot send video directly over AirPlay. On Mac, use macOS screen mirroring, then play Kastideo full screen. A shortcut to display settings is offered in the TV button menu.</li>
      <li><b>YouTube</b>: the video opens in the TV's YouTube app, or in the browser with Chrome's Cast button, as chosen in the settings.</li>
    </ul>

    <h2 id="faire">Casting in four steps</h2>
    <ol>
      <li>Start a channel, movie, series or video.</li>
      <li>Click the TV button in the playback bar.</li>
      <li>Pick the device in the list (Search again if nothing shows: the TV must be on and on the same network).</li>
      <li>The picture goes to the TV, and playback resumes where you were.</li>
    </ol>
    <p>Pause, play, skip forward and back, position, volume and mute in the bar act on the TV. To come back, choose Stop casting: playback resumes on the computer at the same position.</p>

    <h2 id="limites">Limits to know</h2>
    <ul>
      <li>One connection to your provider: while casting, the computer no longer plays the channel.</li>
      <li>Live TV cannot be moved back and forth in time while casting, and the computer's timeshift is cut.</li>
      <li>Recording a channel and MultiView cannot be combined with casting.</li>
      <li>There is a delay of a few seconds, more than with local playback.</li>
    </ul>

    <h2 id="plateformes">Depending on your device</h2>
    <ul>
      <li><b>Mac</b>: macOS asks on first use for permission to find devices on the local network. Accept, otherwise no TV appears.</li>
      <li><b>Windows and Linux</b>: Kastideo prepares the video with ffmpeg before sending (included with the Windows version and the AppImage, to install with the .deb package). The Windows firewall may ask to allow Kastideo: accept on private networks.</li>
      <li><b>Android</b>: casting uses direct mode, the stream address being sent as-is to the TV. Local files cannot be cast.</li>
    </ul>
""",
    },
    # ------------------------------------------------------------------- REPLAY
    {
        "slug": "replay",
        "title_fr": "Replay des programmes",
        "title_en": "Programme replay",
        "blurb_fr": "Revoir une émission déjà diffusée grâce à l'archive de votre fournisseur, depuis le guide TV.",
        "blurb_en": "Watch a programme that already aired using your provider's archive, from the TV guide.",
        "desc": "Le replay dans Kastideo : revoir un programme déjà diffusé grâce à l'archive de votre fournisseur IPTV, depuis le guide TV.",
        "fr": """    <h1>Replay des programmes</h1>
    <p class="page-lead">Beaucoup de fournisseurs IPTV conservent les programmes des jours passés. Kastideo place cette archive directement dans le guide TV : vous retrouvez l'émission manquée et vous la lancez.</p>
    <div class="callout"><b class="label">Une condition</b><p>Le replay dépend de votre abonnement : votre fournisseur doit proposer une archive pour la chaîne, et sa durée varie d'un fournisseur à l'autre. Quand c'est le cas, un petit ↺ apparaît à côté de la chaîne.</p></div>

    <h2 id="guide">Dans le guide TV</h2>
    <p>Le menu de la date propose les jours précédents, dans une section Revoir. Cliquez sur un programme passé d'une chaîne marquée ↺, puis sur Revoir. Sur le programme en cours, Revoir depuis le début relit l'émission depuis son commencement, même si vous avez manqué la première partie.</p>

    <h2 id="depuis-chaine">Depuis une chaîne</h2>
    <p>Un clic droit sur une chaîne propose Revoir (replay) avec les programmes récents de cette chaîne. En interface Cinéma, une rangée « À revoir » réunit celles de vos chaînes préférées qui ont une archive.</p>

    <h2 id="pendant">Pendant la lecture</h2>
    <ul>
      <li>La barre du lecteur permet la pause et le déplacement dans le programme.</li>
      <li>À la fin, Kastideo revient au direct de la chaîne. Un réglage permet de le désactiver.</li>
      <li>Enregistrer ce replay télécharge le programme depuis l'archive dans votre dossier d'enregistrements, pour le garder.</li>
    </ul>

    <h2 id="reglages">Les réglages</h2>
    <ul>
      <li>Activer ou non le replay.</li>
      <li>Le nombre de jours de programmes passés gardés dans le guide : plus de jours demandent plus de mémoire.</li>
      <li>Le décalage de l'heure : si le programme revu est décalé de quelques minutes ou d'une heure, vous le corrigez une fois pour toutes. Le fuseau horaire du serveur est lu automatiquement.</li>
    </ul>

    <h2 id="connexion">Une connexion, comme le direct</h2>
    <p>Le replay compte comme une connexion : il ferme la chaîne en cours, comme un changement de chaîne. S'il ne démarre pas, le Journal de lecture indique l'adresse d'archive composée et le décalage utilisé. Le guide du fournisseur doit contenir les programmes passés : rechargez-le après avoir augmenté le nombre de jours conservés.</p>
""",
        "en": """    <h1>Programme replay</h1>
    <p class="page-lead">Many IPTV providers keep the programmes of past days. Kastideo puts this archive right into the TV guide: you find the show you missed and play it.</p>
    <div class="callout"><b class="label">One condition</b><p>Replay depends on your subscription: your provider must offer an archive for the channel, and its length varies from one provider to another. When it does, a small ↺ appears next to the channel.</p></div>

    <h2 id="guide">In the TV guide</h2>
    <p>The date menu offers the previous days, in a Watch again section. Click a past programme of a channel marked ↺, then Watch again. On the current programme, Watch from the start replays the show from its beginning, even if you missed the first part.</p>

    <h2 id="depuis-chaine">From a channel</h2>
    <p>A right-click on a channel offers Replay with the recent programmes of that channel. In Cinema, a “Watch again” row gathers those of your favourite channels that have an archive.</p>

    <h2 id="pendant">During playback</h2>
    <ul>
      <li>The player bar allows pause and seeking within the programme.</li>
      <li>At the end, Kastideo returns to the channel's live broadcast. A setting lets you turn this off.</li>
      <li>Record this replay downloads the programme from the archive into your recordings folder, to keep it.</li>
    </ul>

    <h2 id="reglages">Settings</h2>
    <ul>
      <li>Turn replay on or off.</li>
      <li>The number of days of past programmes kept in the guide: more days need more memory.</li>
      <li>Time offset: if the programme you watch is shifted by a few minutes or an hour, you fix it once and for all. The server's time zone is read automatically.</li>
    </ul>

    <h2 id="connexion">One connection, like live TV</h2>
    <p>Replay counts as one connection: it closes the current channel, like a channel change. If it does not start, the playback log shows the archive address built and the offset used. The provider's guide must contain past programmes: reload it after increasing the number of days kept.</p>
""",
    },
    # ------------------------------------------------------------ FILMS-SERIES
    {
        "slug": "films-series",
        "title_fr": "Films et séries",
        "title_en": "Movies and series",
        "blurb_fr": "Fiches détaillées, saisons et épisodes, reprise là où vous vous étiez arrêté.",
        "blurb_en": "Detailed pages, seasons and episodes, resume where you left off.",
        "desc": "Les fiches de films et de séries de Kastideo : affiche, distribution, bande-annonce, saisons, épisodes et reprise de lecture.",
        "fr": """    <h1>Films et séries</h1>
    <p class="page-lead">Un catalogue qui se parcourt comme une vidéothèque : des affiches, des fiches complètes, et la reprise exactement là où vous vous étiez arrêté.</p>

    <h2 id="fiches">Des fiches complètes</h2>
    <p>Un clic sur l'affiche d'un film ou d'une série ouvre sa fiche : grande image de fond, affiche, année, durée, genres, note, résumé, réalisateur et distribution avec photos. Les boutons Lire ou Reprendre, Bande-annonce, Télécharger et favori sont à portée de main, avec un bouton Retour pour revenir au catalogue.</p>
    <!--shot:films-fiche-->
    <p>Les informations viennent d'abord de votre fournisseur. Avec une clé TMDB gratuite, saisie dans les réglages, les fiches sont plus complètes et les titres, résumés et épisodes sont dans la langue de l'interface.</p>

    <h2 id="series">Saisons et épisodes</h2>
    <p>Une série s'ouvre sur sa fiche avec ses saisons et ses épisodes. Les titres et résumés des épisodes sont localisés quand TMDB les fournit. Vous pouvez télécharger une saison ou la série entière pour la regarder hors connexion.</p>

    <h2 id="reprise">Reprise de lecture</h2>
    <p>Kastideo mémorise votre position. À la réouverture, la lecture reprend là où vous vous étiez arrêté, avec un message proposant de recommencer au début. Des barres de progression apparaissent dans les listes, sur les affiches et dans les épisodes. Vous pouvez désactiver la mémorisation ou effacer les positions.</p>
    <p>Avec Jellyfin, Emby et Plex, la position et le statut « vu » sont partagés dans les deux sens : un film commencé dans Kastideo se reprend sur le téléviseur, et inversement.</p>

    <h2 id="trouver">Trouver quelque chose à regarder</h2>
    <ul>
      <li>Un filtre par pays et par langue en interface Cinéma écarte ce qui ne vous intéresse pas.</li>
      <li>Le bandeau « à la une » met en avant une catégorie de votre choix, les tendances de la semaine et les derniers ajouts.</li>
      <li>Une seule recherche couvre le direct, les films et les séries.</li>
    </ul>

    <h2 id="fichiers">Vos propres fichiers</h2>
    <p>Pour les films de vos disques ou de votre NAS, Kastideo ajoute affiche et résumé quand le nom du fichier est reconnu. Si une affiche est erronée, Corriger la fiche permet de chercher le bon titre : le choix est retenu. Les sous-titres placés à côté du fichier sont chargés à la lecture.</p>
""",
        "en": """    <h1>Movies and series</h1>
    <p class="page-lead">A catalogue you browse like a video library: posters, full details pages, and resume exactly where you left off.</p>

    <h2 id="fiches">Full details pages</h2>
    <p>A click on the poster of a movie or series opens its page: large background image, poster, year, runtime, genres, rating, plot, director and cast with photos. The Play or Resume, Trailer, Download and favourite buttons are close at hand, with a Back button to return to the catalogue.</p>
    <!--shot:films-fiche-->
    <p>Information comes first from your provider. With a free TMDB key, entered in the settings, pages are more complete and titles, plots and episodes are in the interface language.</p>

    <h2 id="series">Seasons and episodes</h2>
    <p>A series opens on its page with its seasons and episodes. Episode titles and plots are localised when TMDB provides them. You can download a season or the whole series to watch offline.</p>

    <h2 id="reprise">Resume playback</h2>
    <p>Kastideo remembers your position. When you reopen an item, playback resumes where you stopped, with a message offering to start over. Progress bars appear in lists, on posters and in episodes. You can turn off memorisation or erase positions.</p>
    <p>With Jellyfin, Emby and Plex, position and “watched” status are shared both ways: a movie started in Kastideo resumes on the TV, and the other way round.</p>

    <h2 id="trouver">Finding something to watch</h2>
    <ul>
      <li>A country and language filter in Cinema hides what does not interest you.</li>
      <li>The “featured” banner highlights a category of your choice, weekly trends and the latest additions.</li>
      <li>A single search covers live TV, movies and series.</li>
    </ul>

    <h2 id="fichiers">Your own files</h2>
    <p>For the movies on your drives or NAS, Kastideo adds a poster and plot when the file name is recognised. If a poster is wrong, Fix the details lets you search for the right title: the choice is remembered. Subtitles placed next to the file are loaded at playback.</p>
""",
    },
    # ----------------------------------------------------------------- SOURCES
    {
        "slug": "sources",
        "title_fr": "Vos sources",
        "title_en": "Your sources",
        "blurb_fr": "Xtream Codes, M3U, dossiers, Jellyfin, Emby, Plex et YouTube : tout au même endroit.",
        "blurb_en": "Xtream Codes, M3U, folders, Jellyfin, Emby, Plex and YouTube: all in one place.",
        "desc": "Les sources que Kastideo sait lire : Xtream Codes, playlists M3U, dossiers et NAS, Jellyfin, Emby, Plex et YouTube.",
        "fr": """    <h1>Vos sources</h1>
    <p class="page-lead">Kastideo ne fournit aucun contenu : vous apportez vos sources, il les lit toutes dans la même interface. Les identifiants restent sur votre appareil.</p>

    <h2 id="xtream">Xtream Codes</h2>
    <p>Le format le plus courant chez les fournisseurs IPTV. Il faut l'adresse du serveur (par exemple http://exemple.com:8080), votre identifiant et votre mot de passe. Le bouton Tester la connexion vérifie vos identifiants et affiche l'état du compte, sa date d'expiration et le nombre de connexions simultanées autorisées.</p>
    <ul>
      <li>Le mot de passe est rangé dans le coffre sécurisé du système, jamais en clair sur le disque.</li>
      <li>Le guide TV du serveur est utilisé automatiquement.</li>
      <li>Les séries s'ouvrent sur une fiche avec leurs saisons et leurs épisodes.</li>
    </ul>

    <h2 id="m3u">Playlist M3U</h2>
    <p>Par adresse ou par fichier .m3u ou .m3u8. Si l'adresse est de la forme get.php?username=…&amp;password=…, Kastideo la reconnaît et l'enregistre comme une source Xtream : le chargement est beaucoup plus rapide et le guide TV est inclus. Les catégories viennent de la playlist, et les entrées sont classées automatiquement en direct, films ou séries.</p>

    <h2 id="dossiers">Dossiers, disques et NAS</h2>
    <p>Ajoutez des dossiers d'un disque, d'une clé USB ou d'un NAS : Kastideo reconnaît les films et séries d'après le nom des fichiers (« Inception (2010).mkv », « Breaking.Bad.S01E02.mkv », un dossier « Kaamelott/Saison 3/… »). Les films apparaissent dans Films, les épisodes sont regroupés en séries avec leurs saisons, et les autres vidéos (vacances, caméra) dans une rubrique Vidéos.</p>
    <ul>
      <li>Les dossiers sont examinés à chaque lancement puis toutes les 20 minutes : une vidéo ajoutée apparaît toute seule.</li>
      <li>Si le disque est débranché, un message l'indique et la liste précédente est gardée.</li>
      <li>Les sous-titres placés à côté d'une vidéo (« Film.srt », « Film.fr.srt ») sont chargés à la lecture.</li>
    </ul>

    <h2 id="serveurs">Jellyfin, Emby et Plex</h2>
    <p>Un bouton Rechercher sur le réseau trouve les serveurs de la maison. Pour Plex, Se connecter avec Plex ouvre plex.tv : vous autorisez Kastideo et choisissez votre serveur. Les bibliothèques apparaissent dans Films et Séries, avec les affiches, fiches, saisons et épisodes du serveur. La lecture est directe, sans conversion, et la reprise et le statut « vu » sont partagés dans les deux sens.</p>

    <h2 id="youtube">YouTube</h2>
    <p>La section YouTube lit les vidéos avec le lecteur officiel de YouTube, en mode confidentialité avancée. Ce n'est pas un bloqueur de publicités.</p>
    <ul>
      <li>Suivez des chaînes en collant leur lien ou leur @pseudo : leurs dernières vidéos s'affichent sans clé ni compte.</li>
      <li>La recherche demande une clé API Google gratuite, que vous créez en quelques minutes.</li>
      <li>Collez un lien de vidéo ou de playlist pour la lire. Favoris, historique et « À regarder plus tard » reprennent là où vous vous étiez arrêté.</li>
      <li>Vous pouvez importer vos abonnements depuis un export Google Takeout.</li>
    </ul>

    <h2 id="sauvegarde">Tout retrouver ailleurs</h2>
    <p>Le fichier de sauvegarde regroupe vos sources, et il s'importe aussi sur un autre appareil : voir <a href="interfaces.html#sauvegarde">Interfaces et personnalisation</a>.</p>
""",
        "en": """    <h1>Your sources</h1>
    <p class="page-lead">Kastideo provides no content: you bring your sources, it plays them all in the same interface. Credentials stay on your device.</p>

    <h2 id="xtream">Xtream Codes</h2>
    <p>The most common format among IPTV providers. You need the server address (for example http://example.com:8080), your username and your password. The Test connection button checks your credentials and shows the account status, its expiry date and the number of simultaneous connections allowed.</p>
    <ul>
      <li>The password is kept in the system's secure store, never in clear text on disk.</li>
      <li>The server's TV guide is used automatically.</li>
      <li>Series open on a page with their seasons and episodes.</li>
    </ul>

    <h2 id="m3u">M3U playlist</h2>
    <p>By address or by .m3u or .m3u8 file. If the address looks like get.php?username=…&amp;password=…, Kastideo recognises it and saves it as an Xtream source: loading is much faster and the TV guide is included. Categories come from the playlist, and entries are automatically sorted into live, movies or series.</p>

    <h2 id="dossiers">Folders, drives and NAS</h2>
    <p>Add folders from a drive, a USB stick or a NAS: Kastideo recognises movies and series from file names (“Inception (2010).mkv”, “Breaking.Bad.S01E02.mkv”, a “Kaamelott/Season 3/…” folder). Movies appear in Movies, episodes are grouped into series with their seasons, and other videos (holidays, camera) go in a Videos section.</p>
    <ul>
      <li>Folders are scanned at every launch and then every 20 minutes: a video you add appears by itself.</li>
      <li>If the drive is unplugged, a message says so and the previous list is kept.</li>
      <li>Subtitles placed next to a video (“Movie.srt”, “Movie.en.srt”) are loaded at playback.</li>
    </ul>

    <h2 id="serveurs">Jellyfin, Emby and Plex</h2>
    <p>A Search the network button finds the servers at home. For Plex, Sign in with Plex opens plex.tv: you authorise Kastideo and pick your server. Libraries appear in Movies and Series, with the server's posters, details, seasons and episodes. Playback is direct, without conversion, and resume and “watched” status are shared both ways.</p>

    <h2 id="youtube">YouTube</h2>
    <p>The YouTube section plays videos with YouTube's official player, in enhanced privacy mode. It is not an ad blocker.</p>
    <ul>
      <li>Follow channels by pasting their link or @handle: their latest videos appear without a key or account.</li>
      <li>Search needs a free Google API key, which you create in a few minutes.</li>
      <li>Paste a video or playlist link to play it. Favourites, history and “Watch later” resume where you left off.</li>
      <li>You can import your subscriptions from a Google Takeout export.</li>
    </ul>

    <h2 id="sauvegarde">Take it all elsewhere</h2>
    <p>The backup file gathers your sources and can also be imported on another device: see <a href="interfaces.html#sauvegarde">Interfaces and personalisation</a>.</p>
""",
    },
    # --------------------------------------------------------------- FIABILITE
    {
        "slug": "fiabilite",
        "title_fr": "Rapide, stable et sobre",
        "title_en": "Fast, stable and frugal",
        "blurb_fr": "Ce que Kastideo fait pour démarrer vite, tenir toute une soirée et respecter vos données.",
        "blurb_en": "What Kastideo does to start fast, last all evening and respect your data.",
        "desc": "Comment Kastideo démarre vite, reste stable (santé du flux, décodage logiciel, journal de lecture) et protège vos données.",
        "fr": """    <h1>Rapide, stable et sobre</h1>
    <p class="page-lead">Un lecteur se juge à ce qui se passe quand ça ne marche pas. Voici ce que Kastideo fait pour démarrer vite, tenir toute une soirée et rester discret.</p>

    <h2 id="rapide">Rapide</h2>
    <ul>
      <li><b>Démarrage des chaînes</b> en moins d'une seconde en général, avec un badge « Prête en x s » qui le mesure.</li>
      <li><b>Mémoire tampon réglable</b> sur Mac : Rapide (par défaut), Équilibré ou Stable, selon que vous préférez l'immédiateté ou la tolérance aux coupures.</li>
      <li><b>Un compte Xtream se charge vite</b> : les catalogues de plusieurs dizaines de milliers de contenus s'ouvrent sans attente, et les adresses get.php sont converties automatiquement en source Xtream, plus rapide.</li>
      <li><b>Navigation fluide</b> : passer du direct aux films ou aux séries ne recharge pas le catalogue.</li>
    </ul>

    <h2 id="stable">Stable</h2>
    <ul>
      <li><b>Santé du flux</b> en permanence : une pastille verte, orange ou rouge, et le détail au survol.</li>
      <li><b>Surveillance du démarrage</b> : si une chaîne ne démarre pas, Kastideo essaie l'autre format de flux (.ts ou .m3u8), puis affiche une erreur explicite avec la dernière réponse du serveur, au lieu de tourner dans le vide.</li>
      <li><b>Image figée</b> : quand l'image reste bloquée plus de 6 secondes alors que le flux arrive, Kastideo rouvre la chaîne en décodage logiciel et s'en souvient pour la suite. Vous pouvez aussi l'activer chaîne par chaîne ou pour tout.</li>
      <li><b>Chaîne sans son</b> : Kastideo essaie les autres pistes audio et signale le problème par une icône.</li>
      <li><b>Une connexion à la fois</b> : le flux précédent est fermé proprement avant chaque nouveau, pour ne pas dépasser votre limite.</li>
    </ul>

    <h2 id="journal">Comprendre un problème</h2>
    <p>Le Journal de lecture garde le détail de chaque ouverture : adresse tentée, réponse du serveur, essais, décisions de Kastideo. Les identifiants y sont masqués. Il se classe par sujet, se filtre, se recherche et se copie en un clic, ce qui permet de signaler un problème précisément.</p>
    <div class="callout"><b class="label">Premier réflexe</b><p>Un VPN actif perturbe souvent les fournisseurs IPTV. Coupez-le avant de chercher plus loin.</p></div>

    <h2 id="sobre">Sobre</h2>
    <ul>
      <li><b>Aucun compte à créer</b> chez Kastideo. L'application fonctionne avec vos sources, et c'est tout.</li>
      <li><b>Vos identifiants restent sur votre appareil</b>, dans le coffre sécurisé du système, et ne sont envoyés qu'aux services que vous configurez.</li>
      <li><b>Aucune statistique d'usage</b> n'est collectée par l'application.</li>
      <li><b>Des mises à jour discrètes</b> : la vérification se fait au démarrage, jamais pendant un visionnage ni un enregistrement, et l'installation est facultative.</li>
    </ul>
    <p>Pour le détail des données, voir la <a href="confidentialite.html">politique de confidentialité</a>.</p>
""",
        "en": """    <h1>Fast, stable and frugal</h1>
    <p class="page-lead">A player is judged by what happens when things go wrong. Here is what Kastideo does to start fast, last all evening and stay discreet.</p>

    <h2 id="rapide">Fast</h2>
    <ul>
      <li><b>Channel start</b> usually in under a second, with a “Ready in x s” badge that measures it.</li>
      <li><b>Adjustable buffer</b> on Mac: Fast (default), Balanced or Stable, depending on whether you prefer immediacy or tolerance to interruptions.</li>
      <li><b>An Xtream account loads quickly</b>: catalogues of tens of thousands of items open without waiting, and get.php addresses are automatically converted to an Xtream source, which is faster.</li>
      <li><b>Smooth navigation</b>: moving from live to movies or series does not reload the catalogue.</li>
    </ul>

    <h2 id="stable">Stable</h2>
    <ul>
      <li><b>Stream health</b> at all times: a green, orange or red pill, with details on hover.</li>
      <li><b>Start watchdog</b>: if a channel does not start, Kastideo tries the other stream format (.ts or .m3u8), then shows an explicit error with the server's last answer, instead of spinning forever.</li>
      <li><b>Frozen picture</b>: when the picture stays stuck for more than 6 seconds while the stream keeps arriving, Kastideo reopens the channel with software decoding and remembers it. You can also enable it per channel or for everything.</li>
      <li><b>Channel with no sound</b>: Kastideo tries the other audio tracks and flags the problem with an icon.</li>
      <li><b>One connection at a time</b>: the previous stream is closed cleanly before each new one, so you do not exceed your limit.</li>
    </ul>

    <h2 id="journal">Understanding a problem</h2>
    <p>The playback log keeps the detail of every opening: address tried, server answer, attempts, Kastideo's decisions. Credentials are masked in it. It is sorted by topic, filterable, searchable and copyable in one click, which lets you report a problem precisely.</p>
    <div class="callout"><b class="label">First reflex</b><p>An active VPN often disturbs IPTV providers. Turn it off before digging further.</p></div>

    <h2 id="sobre">Frugal</h2>
    <ul>
      <li><b>No account to create</b> with Kastideo. The app works with your sources, and that is all.</li>
      <li><b>Your credentials stay on your device</b>, in the system's secure store, and are sent only to the services you configure.</li>
      <li><b>No usage statistics</b> are collected by the app.</li>
      <li><b>Discreet updates</b>: the check happens at launch, never during viewing or recording, and installing is optional.</li>
    </ul>
    <p>For the details of data, see the <a href="confidentialite.html">privacy policy</a>.</p>
""",
    },
]
