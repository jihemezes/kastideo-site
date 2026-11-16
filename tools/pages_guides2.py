"""Guides pratiques supplémentaires (EPG et replay, enregistrement, iCloud, fiches TMDB). FR et EN.

Contenu tiré de l'aide de l'application (docs/help/aide-fr.md, aide-en.md, iOS/CHANGELOG.md).
"""

EPG_FR = """    <h1>Régler le guide TV et revoir un programme</h1>
    <p class="page-lead">Un guide TV complet, la possibilité de remonter dans le temps et de revoir une émission (le replay, ou « catch-up ») : voici comment tout mettre en route dans Kastideo.</p>

    <h2 id="guide">1. Un guide pour chaque chaîne</h2>
    <p>Chaque source peut avoir une adresse de guide au format XMLTV (<code>.xml</code> ou <code>.xml.gz</code>). Si vous la laissez vide, Kastideo utilise celle du serveur Xtream Codes ou celle annoncée dans la playlist M3U. Le guide couvre de 6 h en arrière à 48 h en avant et se recharge tout seul.</p>
    <ul>
      <li>Pour changer l'adresse : <b>Réglages &gt; Sources</b>, bouton crayon de la source, champ <b>Guide TV (XMLTV)</b>.</li>
      <li>Pour relancer le téléchargement : bouton <b>Recharger le guide TV</b> (icône calendrier). Sous chaque source, Kastideo indique combien de programmes le fournisseur a envoyés.</li>
    </ul>

    <h2 id="secours">2. Le guide de secours</h2>
    <p>Le guide d'un fournisseur est parfois incomplet. Kastideo peut le compléter avec un guide gratuit de <b>xmltvfr.fr</b> : seules les chaînes <b>sans programme</b> sont complétées, le guide du fournisseur reste prioritaire, et les chaînes sont rapprochées par leur nom.</p>
    <p>Réglages &gt; Général &gt; <b>Guide TV de secours</b> : activer ou non, choisir un autre guide, saisir une adresse XMLTV, <b>Actualiser maintenant</b>.</p>

    <h2 id="grille">3. Lire la grille</h2>
    <ul>
      <li>Les chaînes sont en lignes, les heures en colonnes, un trait rouge marque l'heure actuelle.</li>
      <li><b>Maintenant</b> revient à l'heure actuelle, le menu de la date saute à un autre jour, la durée affichée se règle sur 2, 3 ou 6 heures.</li>
      <li>Filtrez par favoris, récents, catégorie ou thème, ou recherchez une chaîne.</li>
      <li>Un clic sur un programme ouvre sa fiche : <b>Regarder</b>, <b>Enregistrer</b> ou <b>Programmer l'enregistrement</b>.</li>
    </ul>

    <h2 id="replay">4. Revoir un programme (replay, catch-up)</h2>
    <p>Certains abonnements conservent les chaînes jusqu'à 14 jours, selon le fournisseur et la chaîne. Kastideo le détecte tout seul : les chaînes concernées portent l'icône <b>↺</b> dans les listes et dans le guide.</p>
    <ol>
      <li>Ouvrez le guide TV et choisissez un jour passé dans le menu de la date (section <b>Revoir</b>), ou cliquez directement sur un programme marqué ↺.</li>
      <li>Cliquez sur <b>Revoir</b>. Sur le programme en cours, <b>Revoir depuis le début</b> le relit depuis son commencement.</li>
      <li>Pendant la lecture, la barre du lecteur permet la pause et le déplacement. À la fin, Kastideo revient au direct de la chaîne (désactivable).</li>
    </ol>
    <p>Le replay compte comme une connexion : il remplace la chaîne en cours, comme un changement de chaîne. Il dépend entièrement de votre abonnement.</p>

    <h2 id="reglages">5. Réglages du replay</h2>
    <p>Réglages &gt; Général &gt; <b>Replay</b> : activer ou non, nombre de jours de programmes passés gardés dans le guide (plus de jours demandent plus de mémoire), décalage de l'heure et retour au direct.</p>

    <h2 id="depannage">Si cela ne fonctionne pas</h2>
    <ul>
      <li><b>Le guide est vide :</b> vérifiez l'adresse dans les réglages de la source, rechargez le guide, ou activez le guide de secours.</li>
      <li><b>Le programme revu est décalé :</b> corrigez le décalage de l'heure dans les réglages du replay.</li>
      <li><b>Un replay ne démarre pas :</b> rechargez le guide après avoir augmenté le nombre de jours conservés, puis consultez le Journal (sujet « Lecture et relais »).</li>
    </ul>
    <p>Voir aussi : <a href="guide-tv.html">Guide TV et thèmes</a>, <a href="replay.html">Replay</a>.</p>
"""

EPG_EN = """    <h1>Set up the TV guide and watch a past programme</h1>
    <p class="page-lead">A complete TV guide, the ability to go back in time and watch something that already aired (replay, or catch-up): here is how to set it all up in Kastideo.</p>

    <h2 id="guide">1. A guide for every channel</h2>
    <p>Each source can have a guide address in XMLTV format (<code>.xml</code> or <code>.xml.gz</code>). If you leave it empty, Kastideo uses the one from the Xtream Codes server or the one announced in the M3U playlist. The guide covers 6 hours back to 48 hours ahead and reloads by itself.</p>
    <ul>
      <li>To change the address: <b>Settings &gt; Sources</b>, the pencil button of the source, <b>TV guide (XMLTV)</b> field.</li>
      <li>To restart the download: the <b>Reload TV guide</b> button (calendar icon). Under each source, Kastideo shows how many programmes the provider sent.</li>
    </ul>

    <h2 id="secours">2. The backup guide</h2>
    <p>A provider's guide is sometimes incomplete. Kastideo can fill the gaps with a free guide from <b>xmltvfr.fr</b>: only channels <b>without a programme</b> are completed, the provider's guide keeps priority, and channels are matched by name.</p>
    <p>Settings &gt; General &gt; <b>Backup TV guide</b>: turn it on or off, pick another guide, enter an XMLTV address, <b>Refresh now</b>.</p>

    <h2 id="grille">3. Reading the grid</h2>
    <ul>
      <li>Channels are rows, hours are columns, and a red line marks the current time.</li>
      <li><b>Now</b> goes back to the current time, the date menu jumps to another day, and the displayed span can be set to 2, 3 or 6 hours.</li>
      <li>Filter by favourites, recents, category or theme, or search for a channel.</li>
      <li>Click a programme to open its details: <b>Watch</b>, <b>Record</b> or <b>Schedule recording</b>.</li>
    </ul>

    <h2 id="replay">4. Watch a past programme (replay, catch-up)</h2>
    <p>Some subscriptions keep channels for up to 14 days, depending on the provider and the channel. Kastideo detects it by itself: the channels concerned carry the <b>↺</b> icon in lists and in the guide.</p>
    <ol>
      <li>Open the TV guide and choose a past day in the date menu (<b>Watch again</b> section), or click a programme marked ↺ directly.</li>
      <li>Click <b>Watch</b>. On the current programme, <b>Watch from the start</b> plays it from its beginning.</li>
      <li>During playback, the player bar allows pausing and seeking. At the end, Kastideo goes back to the live channel (this can be turned off).</li>
    </ol>
    <p>Replay counts as one connection: it replaces the current channel, like a channel change. It depends entirely on your subscription.</p>

    <h2 id="reglages">5. Replay settings</h2>
    <p>Settings &gt; General &gt; <b>Replay</b>: turn it on or off, how many days of past programmes are kept in the guide (more days need more memory), time offset and return to live.</p>

    <h2 id="depannage">If it does not work</h2>
    <ul>
      <li><b>The guide is empty:</b> check the address in the source settings, reload the guide, or turn on the backup guide.</li>
      <li><b>The programme is shifted in time:</b> fix the time offset in the replay settings.</li>
      <li><b>A replay does not start:</b> reload the guide after raising the number of days kept, then open the Log (topic “Playback and relay”).</li>
    </ul>
    <p>See also: <a href="guide-tv.html">TV guide and themes</a>, <a href="replay.html">Replay</a>.</p>
"""

REC_FR = """    <h1>Enregistrer une émission</h1>
    <p class="page-lead">Enregistrer le direct, programmer une émission à venir, télécharger un film pour la nuit : tout se retrouve dans la section Enregistrements.</p>

    <h2 id="maintenant">1. Enregistrer maintenant</h2>
    <ul>
      <li>Pendant la lecture d'une chaîne, cliquez sur le bouton rond rouge du lecteur, ou utilisez le raccourci (<b>⇧⌘R</b> sur Mac, <b>R</b> sous Windows et Linux).</li>
      <li>Autre possibilité : clic droit sur une chaîne &gt; <b>Enregistrer maintenant</b>.</li>
      <li>L'enregistrement utilise <b>la même connexion</b> que la lecture : rien de plus n'est consommé sur votre abonnement.</li>
    </ul>
    <p>Sur Mac, l'enregistrement démarre tout de suite, puis un bandeau propose de choisir l'arrêt : dans 15 minutes, 1 heure, à une heure précise ou sans limite. Sans choix, il s'arrête à la fin du programme d'après le guide TV (marge comprise), sinon après la durée par défaut des réglages.</p>

    <h2 id="programmer">2. Programmer un enregistrement</h2>
    <ul>
      <li>Dans le guide TV, ouvrez un programme à venir puis <b>Programmer l'enregistrement</b>. Un point rouge le marque dans la grille.</li>
      <li>Clic droit sur une chaîne &gt; <b>Programmer un enregistrement…</b> : choisissez un programme du guide, ou des horaires libres pour une chaîne sans guide.</li>
      <li>Des <b>marges</b> avant et après (réglables) évitent de rater le début ou la fin.</li>
      <li>Sous Windows et Linux, une <b>répétition</b> est possible : tous les jours, du lundi au vendredi ou chaque semaine.</li>
    </ul>
    <div class="callout"><b class="label">Important</b><p>Kastideo doit rester ouvert et l'ordinateur allumé à l'heure prévue. Sur Windows, vous pouvez activer « Lancer Kastideo à l'ouverture de session » dans les réglages.</p></div>

    <h2 id="telecharger">3. Télécharger un film ou une série</h2>
    <p>Clic droit sur un film ou un épisode &gt; <b>Télécharger</b> ou <b>Télécharger cette nuit</b>. Pour une série, le bouton de la fiche propose la saison affichée ou toute la série. Les téléchargements passent l'un après l'autre et peuvent être mis en pause, repris ou annulés dans la section Enregistrements.</p>

    <h2 id="priorite">4. Une seule connexion : qui passe en premier ?</h2>
    <p>Votre abonnement n'autorise souvent qu'une connexion. Kastideo vous demande toujours avant d'interrompre quelque chose : changer de chaîne pendant un enregistrement propose de l'arrêter, lancer une lecture pendant un téléchargement le met en pause jusqu'à la fin de la lecture.</p>

    <h2 id="fichiers">5. Retrouver vos fichiers</h2>
    <ul>
      <li>Section <b>Enregistrements</b> de la barre latérale (<b>⌘6</b> sur Mac) : en cours, programmés, téléchargements et fichiers terminés. Un clic lit un fichier, un clic droit l'affiche dans le dossier ou le supprime.</li>
      <li>Dossier par défaut : <b>Films/Kastideo</b> sur Mac, <b>Vidéos/Kastideo</b> sous Windows. Modifiable dans <b>Réglages &gt; Enregistrements</b>.</li>
      <li>À la fin, l'enregistrement est converti sans perte en MP4 (Mac) ou en MKV (Windows et Linux) pour se lire partout.</li>
      <li>Comptez environ 1 à 3 Go par heure selon la chaîne.</li>
    </ul>
    <p>Sur Mac, vous pouvez aussi nettoyer la liste : retirer un enregistrement, une sélection ou tout, avec ou sans suppression des fichiers, et un bouton Annuler pendant quelques secondes.</p>

    <h2 id="droits">Droits de copie</h2>
    <p>Les droits dépendent des conditions de votre fournisseur : Kastideo enregistre, pour votre usage privé, ce que votre abonnement vous donne déjà.</p>
    <p>Voir aussi : <a href="enregistrer.html">Enregistrer et télécharger</a>, <a href="guide-epg-replay.html">Régler le guide TV et revoir un programme</a>.</p>
"""

REC_EN = """    <h1>Record a programme</h1>
    <p class="page-lead">Record live TV, schedule an upcoming programme, download a film overnight: everything is found in the Recordings section.</p>

    <h2 id="maintenant">1. Record now</h2>
    <ul>
      <li>While a channel is playing, click the round red button in the player, or use the shortcut (<b>⇧⌘R</b> on Mac, <b>R</b> on Windows and Linux).</li>
      <li>Alternatively: right-click a channel &gt; <b>Record now</b>.</li>
      <li>The recording uses <b>the same connection</b> as playback: nothing extra is used on your subscription.</li>
    </ul>
    <p>On Mac, recording starts immediately, then a banner lets you choose when to stop: in 15 minutes, 1 hour, at a precise time or never. Without a choice, it stops at the end of the programme according to the TV guide (margin included), otherwise after the default duration set in the settings.</p>

    <h2 id="programmer">2. Schedule a recording</h2>
    <ul>
      <li>In the TV guide, open an upcoming programme then <b>Schedule recording</b>. A red dot marks it in the grid.</li>
      <li>Right-click a channel &gt; <b>Schedule a recording…</b>: pick a guide programme, or free times for a channel without a guide.</li>
      <li><b>Margins</b> before and after (adjustable) keep you from missing the start or the end.</li>
      <li>On Windows and Linux, <b>repeat</b> is possible: every day, Monday to Friday or every week.</li>
    </ul>
    <div class="callout"><b class="label">Important</b><p>Kastideo must stay open and the computer on at the scheduled time. On Windows, you can turn on “Launch Kastideo at sign-in” in the settings.</p></div>

    <h2 id="telecharger">3. Download a film or a series</h2>
    <p>Right-click a film or an episode &gt; <b>Download</b> or <b>Download tonight</b>. For a series, the details button offers the displayed season or the whole series. Downloads run one after another and can be paused, resumed or cancelled in the Recordings section.</p>

    <h2 id="priorite">4. A single connection: who goes first?</h2>
    <p>Your subscription often allows only one connection. Kastideo always asks before interrupting something: changing channel during a recording offers to stop it, and starting playback during a download pauses it until playback ends.</p>

    <h2 id="fichiers">5. Find your files</h2>
    <ul>
      <li><b>Recordings</b> section of the sidebar (<b>⌘6</b> on Mac): in progress, scheduled, downloads and finished files. A click plays a file, a right-click shows it in the folder or deletes it.</li>
      <li>Default folder: <b>Movies/Kastideo</b> on Mac, <b>Videos/Kastideo</b> on Windows. Changeable in <b>Settings &gt; Recordings</b>.</li>
      <li>At the end, the recording is losslessly converted to MP4 (Mac) or MKV (Windows and Linux) so it plays everywhere.</li>
      <li>Expect roughly 1 to 3 GB per hour depending on the channel.</li>
    </ul>
    <p>On Mac, you can also clean the list: remove one recording, a selection or everything, with or without deleting the files, and an Undo button stays for a few seconds.</p>

    <h2 id="droits">Copy rights</h2>
    <p>Rights depend on your provider's terms: Kastideo records, for your private use, what your subscription already gives you.</p>
    <p>See also: <a href="enregistrer.html">Record and download</a>, <a href="guide-epg-replay.html">Set up the TV guide and watch a past programme</a>.</p>
"""

ICLOUD_FR = """    <h1>Synchroniser avec iCloud</h1>
    <p class="page-lead">Gardez votre Mac, votre iPhone et votre iPad à l'identique : sources, favoris, historique et reprise de lecture suivent d'un appareil à l'autre.</p>

    <div class="callout"><b class="label">En test</b><p>La version iPhone et iPad est en test sur TestFlight (voir <a href="ios.html">Kastideo pour iPhone et iPad</a>). La synchronisation iCloud est désactivée par défaut et n'est pas disponible sur Apple TV, Windows, Linux ni Android.</p></div>

    <h2 id="ce-qui-est-synchronise">Ce qui est synchronisé</h2>
    <ul>
      <li>Vos sources (Xtream Codes, playlists M3U par adresse, Jellyfin, Emby, Plex).</li>
      <li>Les favoris, l'historique, les catégories (ordre, masquages, noms).</li>
      <li>La reprise de lecture et les contenus déjà vus, les fiches corrigées.</li>
      <li>Au choix : les mots de passe des sources et la clé TMDB.</li>
    </ul>
    <p>Les dossiers de vidéos, les fichiers M3U et la galerie restent propres à chaque appareil, ainsi que les réglages d'affichage propres à chaque plateforme.</p>

    <h2 id="mise-en-route">Mise en route, sur chaque appareil</h2>
    <ol>
      <li>Dans iCloud Drive, créez un dossier, par exemple <b>Kastideo</b> (une seule fois). Vérifiez que iCloud Drive est activé sur chaque appareil.</li>
      <li>Ouvrez Kastideo &gt; Réglages &gt; <b>iCloud</b> et activez <b>Synchroniser avec iCloud Drive</b>.</li>
      <li>Touchez <b>Dossier de synchronisation</b> et choisissez <b>le même dossier</b>.</li>
      <li>Choisissez les éléments à synchroniser.</li>
      <li>Si vous synchronisez les mots de passe ou la clé TMDB, saisissez la <b>phrase secrète</b> (la même sur tous les appareils) puis <b>Enregistrer la phrase secrète</b>.</li>
    </ol>

    <h2 id="phrase">La phrase secrète</h2>
    <p>Les mots de passe sont chiffrés avec votre phrase secrète avant d'être déposés dans iCloud Drive : sans elle, personne ne peut les lire. Notez-la dans un endroit sûr, elle ne peut pas être retrouvée. Vous pouvez aussi ne synchroniser aucun mot de passe et les saisir une fois sur chaque appareil.</p>

    <h2 id="fonctionnement">Comment ça marche</h2>
    <ul>
      <li>La modification la plus récente l'emporte. À la première synchronisation, les listes (sources, favoris, historique) sont réunies.</li>
      <li>La synchronisation a lieu toutes les 30 secondes, au retour dans l'application et quand elle passe en arrière-plan. <b>Synchroniser maintenant</b> la force.</li>
      <li>Sur Mac, une petite icône nuage en bas de la barre latérale indique l'état.</li>
      <li><b>Effacer les fichiers de synchronisation</b> supprime les fichiers du dossier pour tous vos appareils. Vos données locales sont conservées.</li>
    </ul>

    <h2 id="autres">Et sur les autres plateformes ?</h2>
    <p>Pour passer de l'un à l'autre (Windows, Linux, Android, Apple TV), exportez votre configuration depuis <b>Réglages &gt; Sauvegarde</b> et importez-la sur l'autre appareil : le fichier est le même partout. Astuce : enregistrez-le dans iCloud Drive pour le retrouver facilement.</p>
    <p>Voir aussi : <a href="ios.html#icloud">iCloud sur iPhone et iPad</a>, <a href="mac.html">Kastideo pour Mac</a>.</p>
"""

ICLOUD_EN = """    <h1>Sync with iCloud</h1>
    <p class="page-lead">Keep your Mac, iPhone and iPad identical: sources, favourites, history and playback position follow you from one device to the next.</p>

    <div class="callout"><b class="label">In testing</b><p>The iPhone and iPad version is being tested on TestFlight (see <a href="ios.html">Kastideo for iPhone and iPad</a>). iCloud sync is off by default and is not available on Apple TV, Windows, Linux or Android.</p></div>

    <h2 id="ce-qui-est-synchronise">What is synced</h2>
    <ul>
      <li>Your sources (Xtream Codes, M3U playlists by address, Jellyfin, Emby, Plex).</li>
      <li>Favourites, history, categories (order, hiding, names).</li>
      <li>Playback position and what you have already watched, corrected details.</li>
      <li>Optionally: source passwords and the TMDB key.</li>
    </ul>
    <p>Video folders, M3U files and the photo library stay specific to each device, as do display settings specific to each platform.</p>

    <h2 id="mise-en-route">Set up, on each device</h2>
    <ol>
      <li>In iCloud Drive, create a folder, for example <b>Kastideo</b> (only once). Make sure iCloud Drive is turned on on each device.</li>
      <li>Open Kastideo &gt; Settings &gt; <b>iCloud</b> and turn on <b>Sync with iCloud Drive</b>.</li>
      <li>Tap <b>Sync folder</b> and choose <b>the same folder</b>.</li>
      <li>Choose which items to sync.</li>
      <li>If you sync passwords or the TMDB key, enter the <b>passphrase</b> (the same on every device) then <b>Save passphrase</b>.</li>
    </ol>

    <h2 id="phrase">The passphrase</h2>
    <p>Passwords are encrypted with your passphrase before being placed in iCloud Drive: without it, nobody can read them. Write it down somewhere safe, it cannot be recovered. You can also sync no passwords at all and enter them once on each device.</p>

    <h2 id="fonctionnement">How it works</h2>
    <ul>
      <li>The most recent change wins. On the first sync, lists (sources, favourites, history) are merged.</li>
      <li>Sync happens every 30 seconds, when you return to the app and when it goes to the background. <b>Sync now</b> forces it.</li>
      <li>On Mac, a small cloud icon at the bottom of the sidebar shows the status.</li>
      <li><b>Erase sync files</b> deletes the folder's files for all your devices. Your local data is kept.</li>
    </ul>

    <h2 id="autres">What about other platforms?</h2>
    <p>To move between them (Windows, Linux, Android, Apple TV), export your configuration from <b>Settings &gt; Backup</b> and import it on the other device: the file is the same everywhere. Tip: save it in iCloud Drive to find it easily.</p>
    <p>See also: <a href="ios.html#icloud">iCloud on iPhone and iPad</a>, <a href="mac.html">Kastideo for Mac</a>.</p>
"""

FILMS_FR = """    <h1>Des fiches complètes pour vos films et séries</h1>
    <p class="page-lead">Affiches, résumés, distribution, bandes-annonces : avec une clé TMDB gratuite, vos films et séries ressemblent à un vrai catalogue.</p>

    <h2 id="pourquoi">Pourquoi une clé TMDB ?</h2>
    <p>TMDB (The Movie Database) est une base de films et séries communautaire. Sans clé, Kastideo affiche les informations de votre fournisseur. Avec une clé gratuite, il ajoute les photos des acteurs, les affiches et fonds en haute définition, la bande-annonce et un résumé traduit dans la langue de l'interface. Les fiches de vos dossiers, de Jellyfin, Emby et Plex sont aussi complétées.</p>

    <h2 id="cle">1. Obtenir une clé gratuite</h2>
    <ol>
      <li>Créez un compte sur <b>themoviedb.org</b> (bouton « Rejoindre TMDB »), puis validez-le avec le lien reçu par e-mail.</li>
      <li>Connecté, ouvrez <b>Paramètres &gt; API</b> (avatar en haut à droite), ou cliquez sur <b>Obtenir une clé gratuite</b> dans les réglages de Kastideo.</li>
      <li>Cliquez sur <b>Créer</b>, choisissez <b>Developer</b> et acceptez les conditions d'utilisation.</li>
      <li>Remplissez le formulaire : usage <b>Personnel</b>, nom de l'application <b>Kastideo</b>, une courte description et vos coordonnées.</li>
      <li>Validez : la page affiche une <b>Clé d'API</b> (32 caractères) et un <b>Jeton d'accès en lecture</b> (long, commence par « eyJ »). Kastideo accepte l'un ou l'autre, la clé d'API est la plus simple à copier.</li>
    </ol>

    <h2 id="saisir">2. La saisir dans Kastideo</h2>
    <p><b>Réglages &gt; Général &gt; Fiches des films et séries</b> : collez la clé puis cliquez sur <b>Enregistrer et vérifier</b>. « Clé valide ✓ » confirme la saisie. Rouvrez une fiche (ou cliquez sur <b>Actualiser</b> en bas de la fiche) : elle est complétée. La clé est conservée dans le trousseau de l'appareil ; <b>Retirer la clé</b> revient aux informations du fournisseur.</p>

    <h2 id="corriger">3. Corriger une mauvaise fiche</h2>
    <p>Quand l'affiche, le titre ou le résumé ne sont pas les bons (deux films portent le même titre, par exemple) :</p>
    <ul>
      <li>Clic droit sur l'affiche (ou lien en bas de la fiche) &gt; <b>Corriger la fiche…</b></li>
      <li><b>Chercher par titre :</b> la recherche par titre et année propose une liste de fiches, choisissez la bonne.</li>
      <li><b>Lier à un code TMDB :</b> collez l'adresse ou le numéro de la bonne fiche.</li>
      <li><b>Personnaliser à la main :</b> saisissez vous-même un titre, une année, l'adresse d'une affiche et un résumé.</li>
    </ul>
    <p>Le choix est retenu. Cela fonctionne pour Mes vidéos (dossiers, Jellyfin, Emby, Plex) comme pour les films et séries de votre abonnement. <b>Retirer la correction</b> revient à l'automatique.</p>

    <h2 id="nommer">4. Aider la recherche automatique</h2>
    <ul>
      <li>Nommez vos fichiers avec le titre exact et l'année, par exemple <code>Titre du film (2019).mkv</code>.</li>
      <li>Pour les séries, rangez les épisodes dans un dossier au nom de la série, avec une numérotation du type <code>S01E03</code>.</li>
      <li>La première recherche des fiches prend quelques minutes, puis les notes, durées, pays et langues apparaissent dans les filtres et les tris.</li>
    </ul>

    <h2 id="affichage">5. En profiter</h2>
    <p>Dans l'interface Cinéma, le bandeau « à la une » met en avant les tendances de la semaine disponibles dans votre catalogue. Les filtres par pays, langue et note, et le tri par note TMDB ou durée, viennent aussi des fiches.</p>
    <p>Kastideo utilise l'API TMDB mais n'est ni approuvé ni certifié par TMDB. Voir aussi : <a href="films-series.html">Films et séries</a>, <a href="sources.html">Vos sources</a>.</p>
"""

FILMS_EN = """    <h1>Complete details for your films and series</h1>
    <p class="page-lead">Posters, synopses, cast, trailers: with a free TMDB key, your films and series look like a real catalogue.</p>

    <h2 id="pourquoi">Why a TMDB key?</h2>
    <p>TMDB (The Movie Database) is a community film and series database. Without a key, Kastideo shows your provider's information. With a free key, it adds actors' photos, high-definition posters and backdrops, the trailer and a synopsis translated into the interface language. Details for your folders, Jellyfin, Emby and Plex are completed too.</p>

    <h2 id="cle">1. Get a free key</h2>
    <ol>
      <li>Create an account on <b>themoviedb.org</b> (“Join TMDB” button), then confirm it with the link sent by email.</li>
      <li>Signed in, open <b>Settings &gt; API</b> (avatar at the top right), or click <b>Get a free key</b> in Kastideo's settings.</li>
      <li>Click <b>Create</b>, choose <b>Developer</b> and accept the terms of use.</li>
      <li>Fill in the form: <b>Personal</b> use, application name <b>Kastideo</b>, a short description and your contact details.</li>
      <li>Submit: the page shows an <b>API key</b> (32 characters) and a <b>Read access token</b> (long, starts with “eyJ”). Kastideo accepts either one; the API key is the easiest to copy.</li>
    </ol>

    <h2 id="saisir">2. Enter it in Kastideo</h2>
    <p><b>Settings &gt; General &gt; Film and series details</b>: paste the key then click <b>Save and check</b>. “Valid key ✓” confirms it. Reopen a details page (or click <b>Refresh</b> at the bottom of the page): it is completed. The key is stored in the device keychain; <b>Remove key</b> goes back to the provider's information.</p>

    <h2 id="corriger">3. Fix a wrong match</h2>
    <p>When the poster, title or synopsis are wrong (two films share a title, for example):</p>
    <ul>
      <li>Right-click the poster (or the link at the bottom of the page) &gt; <b>Correct details…</b></li>
      <li><b>Search by title:</b> a search by title and year offers a list of entries, pick the right one.</li>
      <li><b>Link to a TMDB code:</b> paste the address or number of the right entry.</li>
      <li><b>Customise by hand:</b> enter a title, a year, a poster address and a synopsis yourself.</li>
    </ul>
    <p>Your choice is remembered. It works for My videos (folders, Jellyfin, Emby, Plex) as well as for your subscription's films and series. <b>Remove correction</b> goes back to automatic.</p>

    <h2 id="nommer">4. Help the automatic search</h2>
    <ul>
      <li>Name your files with the exact title and year, for example <code>Film Title (2019).mkv</code>.</li>
      <li>For series, put episodes in a folder named after the series, with numbering like <code>S01E03</code>.</li>
      <li>The first search for details takes a few minutes, then ratings, durations, countries and languages appear in the filters and sorting.</li>
    </ul>

    <h2 id="affichage">5. Enjoy it</h2>
    <p>In the Cinema interface, the “featured” banner highlights this week's trends that are available in your catalogue. Filters by country, language and rating, and sorting by TMDB rating or duration, also come from the details.</p>
    <p>Kastideo uses the TMDB API but is not endorsed or certified by TMDB. See also: <a href="films-series.html">Films and series</a>, <a href="sources.html">Your sources</a>.</p>
"""

GUIDES2 = [
    {"slug": "guide-epg-replay", "cat": "use", "title_fr": "Régler le guide TV et revoir un programme", "title_en": "Set up the TV guide and watch a past programme",
     "blurb_fr": "Adresse du guide, guide de secours, grille, replay jusqu'à 14 jours.",
     "blurb_en": "Guide address, backup guide, grid, replay up to 14 days.", "fr": EPG_FR, "en": EPG_EN},
    {"slug": "guide-enregistrer", "cat": "use", "title_fr": "Enregistrer une émission", "title_en": "Record a programme",
     "blurb_fr": "Enregistrer le direct, programmer, télécharger la nuit, retrouver ses fichiers.",
     "blurb_en": "Record live, schedule, download overnight, find your files.", "fr": REC_FR, "en": REC_EN},
    {"slug": "guide-icloud", "cat": "setup", "title_fr": "Synchroniser avec iCloud", "title_en": "Sync with iCloud",
     "blurb_fr": "Mac, iPhone et iPad à l'identique, avec phrase secrète pour les mots de passe.",
     "blurb_en": "Mac, iPhone and iPad kept identical, with a passphrase for passwords.", "fr": ICLOUD_FR, "en": ICLOUD_EN},
    {"slug": "guide-films-series", "cat": "setup", "title_fr": "Des fiches complètes pour vos films et séries", "title_en": "Complete details for your films and series",
     "blurb_fr": "Clé TMDB gratuite, correction des fiches, nommage des fichiers.",
     "blurb_en": "Free TMDB key, fixing details, naming your files.", "fr": FILMS_FR, "en": FILMS_EN},
]
