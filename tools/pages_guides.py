"""Guides pratiques (une question = une page), page Nouveautés. FR et EN.

Contenu tiré de l'aide de l'application (docs/help/aide-fr.md et aide-en.md).
"""

# ------------------------------------------------------------------ M3U sur Mac
M3U_MAC_FR = """    <h1>Lire une playlist M3U sur Mac</h1>
    <p class="page-lead">Vous avez une playlist au format M3U ou M3U8 (une adresse ou un fichier) et vous voulez la regarder sur votre Mac, avec un guide TV et des chaînes classées. Voici comment faire avec Kastideo, en cinq minutes.</p>

    <h2 id="avant">Avant de commencer</h2>
    <ul>
      <li>Un Mac sous macOS 14 Sonoma ou plus récent.</li>
      <li>Votre playlist : soit son adresse (commençant par http), soit un fichier <code>.m3u</code> ou <code>.m3u8</code>.</li>
    </ul>
    <p>Kastideo ne fournit aucune chaîne : la playlist vient de vous, et vous devez vérifier que son contenu est légal.</p>

    <h2 id="installer">1. Installer Kastideo</h2>
    <p>Téléchargez le fichier <code>.dmg</code> depuis la page <a href="mac.html">Kastideo pour Mac</a>, ouvrez-le et glissez l'application dans le dossier Applications.</p>

    <h2 id="ajouter">2. Ajouter la playlist</h2>
    <ol>
      <li>Au premier lancement, cliquez sur <b>Ajouter une source</b>. Plus tard : <b>Réglages</b> (⌘,) puis <b>Sources</b> puis <b>Ajouter</b>.</li>
      <li>Choisissez <b>Playlist M3U</b>.</li>
      <li><b>Par adresse :</b> collez l'adresse de la playlist. <b>Par fichier :</b> choisissez le fichier <code>.m3u</code> ou <code>.m3u8</code> sur votre Mac. Kastideo garde l'autorisation d'y accéder pour pouvoir l'actualiser.</li>
      <li>Cliquez sur <b>Ajouter</b> : Kastideo charge les chaînes et le guide TV.</li>
    </ol>

    <h2 id="resultat">3. Ce que vous obtenez</h2>
    <ul>
      <li>Les catégories viennent de l'attribut <code>group-title</code> de la playlist, les logos de <code>tvg-logo</code> et l'association au guide TV de <code>tvg-id</code>.</li>
      <li>Kastideo classe les entrées en Direct, Films ou Séries d'après leur adresse.</li>
      <li>Si l'adresse est de la forme <code>get.php?username=…&amp;password=…</code>, Kastideo la reconnaît et l'enregistre comme une source Xtream Codes : le chargement est plus rapide, le guide TV est inclus et le mot de passe est rangé dans le trousseau macOS. Voir <a href="guide-xtream-codes.html">Ajouter un abonnement Xtream Codes</a>.</li>
    </ul>

    <h2 id="guide">Le guide TV est vide ?</h2>
    <p>Une playlist M3U seule ne contient pas toujours de guide. Kastideo peut charger un guide de secours (xmltvfr.fr) et l'associer à vos chaînes d'après leur nom : voir <a href="guide-tv.html#secours">Guide TV et thèmes</a>.</p>

    <h2 id="suite">Et ensuite ?</h2>
    <p>Ouvrez Direct, parcourez les <a href="guide-tv.html">thèmes</a>, essayez la <a href="multivue.html">MultiVue</a> ou <a href="enregistrer.html">enregistrez une émission</a>. Si une chaîne ne démarre pas : <a href="fiabilite.html#journal">Rapide, stable et sobre</a>.</p>
"""
M3U_MAC_EN = """    <h1>Play an M3U playlist on Mac</h1>
    <p class="page-lead">You have an M3U or M3U8 playlist (an address or a file) and want to watch it on your Mac, with a TV guide and sorted channels. Here is how to do it with Kastideo, in five minutes.</p>

    <h2 id="avant">Before you start</h2>
    <ul>
      <li>A Mac running macOS 14 Sonoma or later.</li>
      <li>Your playlist: either its address (starting with http) or an <code>.m3u</code> or <code>.m3u8</code> file.</li>
    </ul>
    <p>Kastideo provides no channels: the playlist comes from you, and you must check that its content is legal.</p>

    <h2 id="installer">1. Install Kastideo</h2>
    <p>Download the <code>.dmg</code> file from the <a href="mac.html">Kastideo for Mac</a> page, open it and drag the app into the Applications folder.</p>

    <h2 id="ajouter">2. Add the playlist</h2>
    <ol>
      <li>At first launch, click <b>Add a source</b>. Later: <b>Settings</b> (⌘,) then <b>Sources</b> then <b>Add</b>.</li>
      <li>Choose <b>M3U playlist</b>.</li>
      <li><b>By address:</b> paste the playlist address. <b>By file:</b> choose the <code>.m3u</code> or <code>.m3u8</code> file on your Mac. Kastideo keeps the permission to access it so it can refresh it.</li>
      <li>Click <b>Add</b>: Kastideo loads the channels and the TV guide.</li>
    </ol>

    <h2 id="resultat">3. What you get</h2>
    <ul>
      <li>Categories come from the playlist's <code>group-title</code> attribute, logos from <code>tvg-logo</code> and the TV guide match from <code>tvg-id</code>.</li>
      <li>Kastideo sorts entries into Live, Movies or Series from their address.</li>
      <li>If the address looks like <code>get.php?username=…&amp;password=…</code>, Kastideo recognises it and saves it as an Xtream Codes source: loading is faster, the TV guide is included and the password is kept in the macOS keychain. See <a href="guide-xtream-codes.html">Add an Xtream Codes subscription</a>.</li>
    </ul>

    <h2 id="guide">Empty TV guide?</h2>
    <p>A plain M3U playlist does not always contain a guide. Kastideo can load a backup guide (xmltvfr.fr) and match it to your channels by name: see <a href="guide-tv.html#secours">TV guide and themes</a>.</p>

    <h2 id="suite">What next?</h2>
    <p>Open Live, browse the <a href="guide-tv.html">themes</a>, try <a href="multivue.html">MultiView</a> or <a href="enregistrer.html">record a show</a>. If a channel does not start: <a href="fiabilite.html#journal">Fast, stable and frugal</a>.</p>
"""

# -------------------------------------------------------------- M3U sur Windows
M3U_WIN_FR = """    <h1>Lire une playlist M3U sur Windows</h1>
    <p class="page-lead">Kastideo lit une playlist M3U sur Windows 10 et 11 avec un guide TV, des thèmes et le replay si votre fournisseur le propose. Installation sans droits administrateur, ajout de la playlist en quelques clics.</p>

    <h2 id="installer">1. Installer Kastideo</h2>
    <ol>
      <li>Téléchargez <code>Kastideo-…-windows-x64-setup.exe</code> depuis la page <a href="windows.html">Kastideo pour Windows</a>. Par défaut l'installation se fait pour votre compte seul, dans votre dossier AppData, sans droits administrateur.</li>
      <li>Ou prenez l'archive <code>windows-x64.zip</code>, décompressez-la où vous voulez et lancez <code>kastideo.exe</code> : rien n'est installé.</li>
      <li>Si Windows affiche « Windows a protégé votre ordinateur », cliquez sur <b>Informations complémentaires</b> puis sur <b>Exécuter quand même</b>. L'application n'est pas encore signée.</li>
    </ol>

    <h2 id="ajouter">2. Ajouter la playlist</h2>
    <ol>
      <li>Ouvrez les <b>Réglages</b> (la roue dentée de l'accueil, ou Ctrl+,) puis <b>Sources</b> puis <b>Ajouter une source</b>.</li>
      <li>Choisissez <b>Playlist M3U</b>.</li>
      <li>Collez l'adresse de la playlist, ou cliquez sur <b>Choisir un fichier…</b> pour un fichier <code>.m3u</code> ou <code>.m3u8</code>.</li>
      <li>Cliquez sur <b>Ajouter</b>.</li>
    </ol>
    <p>Une adresse <code>get.php?username=…&amp;password=…</code> est reconnue et transformée en source Xtream, plus rapide et plus complète : voir <a href="guide-xtream-codes.html">Ajouter un abonnement Xtream Codes</a>.</p>

    <h2 id="double-clic">Ouvrir les fichiers .m3u d'un double-clic</h2>
    <p>Dans <b>Réglages &gt; Général &gt; Démarrage et fichiers</b>, cochez <b>Ouvrir les fichiers .m3u et .m3u8 avec Kastideo</b> : un double-clic sur une playlist propose de l'ajouter comme source. Si Windows ouvre encore un autre programme, faites un clic droit sur le fichier, <b>Ouvrir avec</b>, <b>Choisir une autre application</b>, puis Kastideo.</p>

    <h2 id="enregistrements">Pour les enregistrements programmés</h2>
    <p>Kastideo doit être ouvert à l'heure prévue. Activez <b>Lancer Kastideo à l'ouverture de session</b> et <b>Démarrer réduit</b> pour qu'il reste discret dans la barre des tâches. Voir <a href="enregistrer.html">Enregistrer et télécharger</a>.</p>
"""
M3U_WIN_EN = """    <h1>Play an M3U playlist on Windows</h1>
    <p class="page-lead">Kastideo plays an M3U playlist on Windows 10 and 11 with a TV guide, themes and replay if your provider offers it. Installation with no administrator rights, playlist added in a few clicks.</p>

    <h2 id="installer">1. Install Kastideo</h2>
    <ol>
      <li>Download <code>Kastideo-…-windows-x64-setup.exe</code> from the <a href="windows.html">Kastideo for Windows</a> page. By default it installs for your account only, in your AppData folder, with no administrator rights.</li>
      <li>Or take the <code>windows-x64.zip</code> archive, extract it wherever you like and run <code>kastideo.exe</code>: nothing is installed.</li>
      <li>If Windows shows “Windows protected your PC”, click <b>More info</b> then <b>Run anyway</b>. The app is not signed yet.</li>
    </ol>

    <h2 id="ajouter">2. Add the playlist</h2>
    <ol>
      <li>Open <b>Settings</b> (the cog on the home screen, or Ctrl+,) then <b>Sources</b> then <b>Add a source</b>.</li>
      <li>Choose <b>M3U playlist</b>.</li>
      <li>Paste the playlist address, or click <b>Choose a file…</b> for an <code>.m3u</code> or <code>.m3u8</code> file.</li>
      <li>Click <b>Add</b>.</li>
    </ol>
    <p>A <code>get.php?username=…&amp;password=…</code> address is recognised and turned into an Xtream source, faster and more complete: see <a href="guide-xtream-codes.html">Add an Xtream Codes subscription</a>.</p>

    <h2 id="double-clic">Open .m3u files with a double-click</h2>
    <p>In <b>Settings &gt; General &gt; Startup and files</b>, tick <b>Open .m3u and .m3u8 files with Kastideo</b>: a double-click on a playlist offers to add it as a source. If Windows still opens another program, right-click the file, <b>Open with</b>, <b>Choose another app</b>, then Kastideo.</p>

    <h2 id="enregistrements">For scheduled recordings</h2>
    <p>Kastideo must be open at the scheduled time. Enable <b>Launch Kastideo at sign-in</b> and <b>Start minimised</b> so it stays discreet in the taskbar. See <a href="enregistrer.html">Recording and downloading</a>.</p>
"""

# ------------------------------------------------------------------- Xtream
XT_FR = """    <h1>Ajouter un abonnement Xtream Codes</h1>
    <p class="page-lead">Xtream Codes est le format le plus courant chez les fournisseurs IPTV. Avec trois informations, Kastideo charge vos chaînes, vos films, vos séries et le guide TV du serveur.</p>

    <h2 id="infos">Les trois informations</h2>
    <p>Votre fournisseur vous les a communiquées :</p>
    <ul>
      <li>l'adresse du <b>serveur</b>, par exemple <code>http://exemple.com:8080</code> ;</li>
      <li>votre <b>identifiant</b> ;</li>
      <li>votre <b>mot de passe</b>.</li>
    </ul>

    <h2 id="ajouter">Ajouter la source</h2>
    <ol>
      <li>Au premier lancement, cliquez sur <b>Ajouter une source</b>. Sinon : Réglages (⌘, sur Mac, Ctrl+, sur Windows et Linux), <b>Sources</b>, <b>Ajouter</b>.</li>
      <li>Choisissez <b>Xtream Codes</b> et renseignez le serveur, l'identifiant et le mot de passe.</li>
      <li>Cliquez sur <b>Tester la connexion</b> (Mac) : Kastideo vérifie vos identifiants et affiche l'état du compte, sa date d'expiration et le nombre de connexions simultanées autorisées.</li>
      <li>Cliquez sur <b>Ajouter</b>.</li>
    </ol>

    <h2 id="securite">Où va le mot de passe ?</h2>
    <p>Il est rangé dans le coffre sécurisé de votre système : trousseau macOS, Gestionnaire d'identification de Windows, trousseau GNOME ou KWallet sous Linux. Il n'est jamais écrit en clair sur le disque et n'est envoyé qu'à votre fournisseur.</p>

    <h2 id="resultat">Ce que vous obtenez</h2>
    <ul>
      <li>Le guide TV du serveur est utilisé automatiquement.</li>
      <li>Les séries s'ouvrent sur une fiche avec leurs saisons et leurs épisodes.</li>
      <li>Le <a href="replay.html">replay</a> apparaît sur les chaînes dont le fournisseur conserve une archive.</li>
      <li>Le nombre de connexions simultanées autorisées sert à activer la <a href="multivue.html">MultiVue</a>.</li>
    </ul>

    <h2 id="get-php">Vous avez une adresse get.php ?</h2>
    <p>Si votre fournisseur vous a donné une adresse de playlist de la forme <code>get.php?username=…&amp;password=…</code>, collez-la simplement comme une playlist M3U : Kastideo la reconnaît et l'enregistre en Xtream Codes, avec les avantages ci-dessus. Voir <a href="guide-m3u-mac.html">Lire une playlist M3U sur Mac</a>.</p>

    <h2 id="probleme">Ça ne marche pas ?</h2>
    <ul>
      <li>Vérifiez l'adresse, le port, l'identifiant et le mot de passe, lettre par lettre.</li>
      <li>Coupez un éventuel VPN, qui perturbe souvent les fournisseurs.</li>
      <li>Vérifiez que l'abonnement n'est pas expiré, et qu'aucun autre appareil ne l'utilise si la limite est d'une connexion.</li>
      <li>Consultez le Journal de lecture : <a href="fiabilite.html#journal">Rapide, stable et sobre</a>.</li>
    </ul>
    <p>Kastideo ne fournit aucun abonnement. Vérifiez que votre fournisseur est légal.</p>
"""
XT_EN = """    <h1>Add an Xtream Codes subscription</h1>
    <p class="page-lead">Xtream Codes is the most common format among IPTV providers. With three pieces of information, Kastideo loads your channels, movies, series and the server's TV guide.</p>

    <h2 id="infos">The three pieces of information</h2>
    <p>Your provider gave them to you:</p>
    <ul>
      <li>the <b>server</b> address, for example <code>http://example.com:8080</code>;</li>
      <li>your <b>username</b>;</li>
      <li>your <b>password</b>.</li>
    </ul>

    <h2 id="ajouter">Add the source</h2>
    <ol>
      <li>At first launch, click <b>Add a source</b>. Otherwise: Settings (⌘, on Mac, Ctrl+, on Windows and Linux), <b>Sources</b>, <b>Add</b>.</li>
      <li>Choose <b>Xtream Codes</b> and enter the server, username and password.</li>
      <li>Click <b>Test connection</b> (Mac): Kastideo checks your credentials and shows the account status, its expiry date and the number of simultaneous connections allowed.</li>
      <li>Click <b>Add</b>.</li>
    </ol>

    <h2 id="securite">Where does the password go?</h2>
    <p>It is kept in your system's secure store: macOS keychain, Windows Credential Manager, GNOME keyring or KWallet on Linux. It is never written in clear text on disk and is sent only to your provider.</p>

    <h2 id="resultat">What you get</h2>
    <ul>
      <li>The server's TV guide is used automatically.</li>
      <li>Series open on a page with their seasons and episodes.</li>
      <li><a href="replay.html">Replay</a> appears on channels whose provider keeps an archive.</li>
      <li>The number of simultaneous connections allowed is used to enable <a href="multivue.html">MultiView</a>.</li>
    </ul>

    <h2 id="get-php">Do you have a get.php address?</h2>
    <p>If your provider gave you a playlist address of the form <code>get.php?username=…&amp;password=…</code>, simply paste it as an M3U playlist: Kastideo recognises it and saves it as Xtream Codes, with the benefits above. See <a href="guide-m3u-mac.html">Play an M3U playlist on Mac</a>.</p>

    <h2 id="probleme">Not working?</h2>
    <ul>
      <li>Check the address, port, username and password, letter by letter.</li>
      <li>Turn off any VPN, which often disturbs providers.</li>
      <li>Check the subscription has not expired, and that no other device uses it if the limit is one connection.</li>
      <li>Look at the playback log: <a href="fiabilite.html#journal">Fast, stable and frugal</a>.</li>
    </ul>
    <p>Kastideo provides no subscription. Check that your provider is legal.</p>
"""

# ------------------------------------------------------------------ Android TV
ATV_FR = """    <h1>Installer Kastideo sur Android TV et Google TV</h1>
    <p class="page-lead">Kastideo n'est pas sur Google Play : on l'installe à partir d'un fichier APK. Sur un téléviseur, trois méthodes simples, sans désactiver la sécurité de l'appareil.</p>

    <h2 id="compatible">Appareils concernés</h2>
    <p>Téléviseurs Android TV et Google TV, Chromecast avec Google TV, Nvidia Shield, téléviseurs Philips, Sony, TCL. Un seul APK fonctionne sur téléphone et sur téléviseur. C'est une version en aperçu : elle fonctionne bien, mais vos retours restent précieux.</p>

    <h2 id="fichier">1. Choisir le bon fichier</h2>
    <ul>
      <li><b>arm64-v8a</b> : presque tous les boîtiers et téléviseurs récents. C'est le bon choix dans le doute.</li>
      <li><b>armeabi-v7a</b> : anciens appareils et certains boîtiers 32 bits.</li>
      <li><b>universal</b> : tous les processeurs, mais plus volumineux.</li>
    </ul>
    <p>Les fichiers sont sur la page <a href="android.html">Kastideo pour Android et Android TV</a>, ou sur <a href="telecharger.html">Télécharger</a>.</p>

    <h2 id="methodes">2. Installer sur le téléviseur</h2>
    <p>Le navigateur et le gestionnaire de fichiers d'un téléviseur sont souvent absents. Choisissez l'une de ces méthodes :</p>
    <ul>
      <li><b>Downloader</b> (application gratuite du Play Store du téléviseur) : saisissez l'adresse de téléchargement de l'APK, puis autorisez Downloader à installer des applications.</li>
      <li><b>Clé USB</b> : copiez l'APK sur la clé, branchez-la au téléviseur et ouvrez le fichier avec un gestionnaire de fichiers.</li>
      <li><b>Depuis un téléphone</b> : transférez l'APK avec « Send Files to TV ».</li>
    </ul>
    <p>Android ne demande pas de désactiver ses protections : il demande une autorisation pour une seule application, celle qui ouvre l'APK (Downloader, par exemple). Si Play Protect signale un développeur inconnu, choisissez <b>Plus de détails</b> puis <b>Installer quand même</b> : Kastideo n'est pas publié sur Google Play.</p>

    <h2 id="telecommande">3. Se servir de la télécommande</h2>
    <ul>
      <li>Les flèches déplacent la sélection, OK valide, Retour revient en arrière.</li>
      <li>Pour le direct, l'interface TV s'ouvre : haut et bas (ou Chaîne +/−) changent de chaîne, les chiffres saisissent un numéro, gauche ouvre la liste des chaînes.</li>
      <li>Pour les films et séries, l'interface Cinéma s'ouvre : OK met en pause, gauche et droite reculent de 10 s ou avancent de 30 s.</li>
    </ul>

    <h2 id="source">4. Ajouter votre source</h2>
    <p>Saisir une adresse longue à la télécommande est pénible. Le plus confortable : configurez Kastideo sur un ordinateur, exportez le fichier de sauvegarde, puis importez-le sur le téléviseur. Voir <a href="interfaces.html#sauvegarde">Interfaces et personnalisation</a>, ou <a href="sources.html">Vos sources</a>.</p>

    <h2 id="maj">Mises à jour</h2>
    <p>Les APK sont tous signés avec la même clé : installez le nouvel APK par-dessus l'ancien, vos réglages sont conservés.</p>
"""
ATV_EN = """    <h1>Install Kastideo on Android TV and Google TV</h1>
    <p class="page-lead">Kastideo is not on Google Play: you install it from an APK file. On a TV, three simple methods, without disabling the device's security.</p>

    <h2 id="compatible">Supported devices</h2>
    <p>Android TV and Google TV sets, Chromecast with Google TV, Nvidia Shield, Philips, Sony and TCL TVs. A single APK works on phone and TV. This is a preview version: it works well, but your feedback remains valuable.</p>

    <h2 id="fichier">1. Choose the right file</h2>
    <ul>
      <li><b>arm64-v8a</b>: almost all recent boxes and TVs. The right choice if unsure.</li>
      <li><b>armeabi-v7a</b>: older devices and some 32-bit boxes.</li>
      <li><b>universal</b>: all processors, but larger.</li>
    </ul>
    <p>The files are on the <a href="android.html">Kastideo for Android and Android TV</a> page, or on <a href="telecharger.html">Download</a>.</p>

    <h2 id="methodes">2. Install on the TV</h2>
    <p>A TV's browser and file manager are often missing. Pick one of these methods:</p>
    <ul>
      <li><b>Downloader</b> (free app from the TV's Play Store): type the APK download address, then allow Downloader to install apps.</li>
      <li><b>USB stick</b>: copy the APK onto the stick, plug it into the TV and open the file with a file manager.</li>
      <li><b>From a phone</b>: transfer the APK with “Send Files to TV”.</li>
    </ul>
    <p>Android does not ask you to disable its protections: it asks for a permission for a single app, the one that opens the APK (Downloader, for example). If Play Protect flags an unknown developer, choose <b>More details</b> then <b>Install anyway</b>: Kastideo is not published on Google Play.</p>

    <h2 id="telecommande">3. Using the remote</h2>
    <ul>
      <li>Arrows move the selection, OK confirms, Back goes back.</li>
      <li>For live TV, the TV interface opens: up and down (or Channel +/−) change channel, digits enter a number, left opens the channel list.</li>
      <li>For movies and series, the Cinema interface opens: OK pauses, left and right skip back 10 s or forward 30 s.</li>
    </ul>

    <h2 id="source">4. Add your source</h2>
    <p>Typing a long address with a remote is tedious. The most comfortable way: set Kastideo up on a computer, export the backup file, then import it on the TV. See <a href="interfaces.html#sauvegarde">Interfaces and personalisation</a>, or <a href="sources.html">Your sources</a>.</p>

    <h2 id="maj">Updates</h2>
    <p>All APKs are signed with the same key: install the new APK over the old one, your settings are kept.</p>
"""

# --------------------------------------------------------------- Raspberry Pi
PI_FR = """    <h1>Regarder l'IPTV sur Raspberry Pi 4 ou 5</h1>
    <p class="page-lead">Kastideo existe en AppImage pour processeur ARM 64 bits : un Raspberry Pi 4 ou 5 devient un petit lecteur IPTV pour le salon. Version en aperçu.</p>

    <h2 id="prerequis">Prérequis</h2>
    <ul>
      <li>Un Raspberry Pi 4 ou 5 avec un système <b>64 bits</b>.</li>
      <li>Pour vérifier l'architecture, ouvrez un terminal et tapez <code>uname -m</code> : la réponse doit être <code>aarch64</code>.</li>
    </ul>

    <h2 id="telecharger">1. Télécharger le bon fichier</h2>
    <p>Prenez <code>Kastideo-…-linux-aarch64.AppImage</code> sur la page <a href="linux.html">Kastideo pour Linux</a> ou sur <a href="telecharger.html">Télécharger</a>.</p>

    <h2 id="lancer">2. Le rendre exécutable et le lancer</h2>
    <ol>
      <li>Clic droit sur le fichier, <b>Propriétés</b>, <b>Permissions</b>, puis cochez <b>Autoriser l'exécution comme un programme</b>. Ou en terminal : <code>chmod +x Kastideo-…-linux-aarch64.AppImage</code>.</li>
      <li>Double-cliquez dessus.</li>
      <li>S'il ne démarre pas, installez la bibliothèque FUSE : <code>sudo apt install libfuse2</code> (<code>libfuse2t64</code> sur un système basé sur Ubuntu 24.04).</li>
    </ol>
    <p>ffmpeg est déjà inclus dans l'AppImage, pour l'envoi vers un téléviseur.</p>

    <h2 id="ajouter">3. Ajouter votre source</h2>
    <p>Ouvrez Réglages (Ctrl+,), <b>Sources</b>, <b>Ajouter une source</b>, puis choisissez Xtream Codes ou une playlist M3U. Voir <a href="guide-xtream-codes.html">Ajouter un abonnement Xtream Codes</a>.</p>

    <h2 id="salon">Pour un usage au salon</h2>
    <ul>
      <li>Choisissez l'<a href="interfaces.html">interface TV</a> pour le direct : la chaîne en plein cadre, zapping au clavier ou à la télécommande USB.</li>
      <li>Activez <b>Lancer Kastideo à l'ouverture de session</b> pour qu'il démarre avec la session, ce qui est utile pour les <a href="enregistrer.html">enregistrements programmés</a>.</li>
    </ul>
    <div class="callout"><b class="label">À savoir</b><p>Les performances dépendent du modèle de Pi et de la qualité des flux. Si une image se fige, essayez le décodage logiciel chaîne par chaîne : voir <a href="fiabilite.html#stable">Rapide, stable et sobre</a>.</p></div>
"""
PI_EN = """    <h1>Watch IPTV on a Raspberry Pi 4 or 5</h1>
    <p class="page-lead">Kastideo comes as an AppImage for 64-bit ARM processors: a Raspberry Pi 4 or 5 becomes a small IPTV player for the living room. Preview version.</p>

    <h2 id="prerequis">Requirements</h2>
    <ul>
      <li>A Raspberry Pi 4 or 5 with a <b>64-bit</b> system.</li>
      <li>To check the architecture, open a terminal and type <code>uname -m</code>: the answer must be <code>aarch64</code>.</li>
    </ul>

    <h2 id="telecharger">1. Download the right file</h2>
    <p>Take <code>Kastideo-…-linux-aarch64.AppImage</code> from the <a href="linux.html">Kastideo for Linux</a> page or from <a href="telecharger.html">Download</a>.</p>

    <h2 id="lancer">2. Make it executable and launch it</h2>
    <ol>
      <li>Right-click the file, <b>Properties</b>, <b>Permissions</b>, then tick <b>Allow executing as a program</b>. Or in a terminal: <code>chmod +x Kastideo-…-linux-aarch64.AppImage</code>.</li>
      <li>Double-click it.</li>
      <li>If it does not start, install the FUSE library: <code>sudo apt install libfuse2</code> (<code>libfuse2t64</code> on an Ubuntu 24.04 based system).</li>
    </ol>
    <p>ffmpeg is already included in the AppImage, for casting to a TV.</p>

    <h2 id="ajouter">3. Add your source</h2>
    <p>Open Settings (Ctrl+,), <b>Sources</b>, <b>Add a source</b>, then choose Xtream Codes or an M3U playlist. See <a href="guide-xtream-codes.html">Add an Xtream Codes subscription</a>.</p>

    <h2 id="salon">For living-room use</h2>
    <ul>
      <li>Choose the <a href="interfaces.html">TV interface</a> for live TV: the channel full frame, zapping with the keyboard or a USB remote.</li>
      <li>Enable <b>Launch Kastideo at sign-in</b> so it starts with the session, which is useful for <a href="enregistrer.html">scheduled recordings</a>.</li>
    </ul>
    <div class="callout"><b class="label">Good to know</b><p>Performance depends on the Pi model and the stream quality. If a picture freezes, try software decoding channel by channel: see <a href="fiabilite.html#stable">Fast, stable and frugal</a>.</p></div>
"""

GUIDES = [
    {"slug": "guide-m3u-mac", "title_fr": "Lire une playlist M3U sur Mac", "title_en": "Play an M3U playlist on Mac",
     "blurb_fr": "Ajouter une adresse ou un fichier M3U dans Kastideo, en cinq minutes.",
     "blurb_en": "Add an M3U address or file in Kastideo, in five minutes.", "fr": M3U_MAC_FR, "en": M3U_MAC_EN},
    {"slug": "guide-m3u-windows", "title_fr": "Lire une playlist M3U sur Windows", "title_en": "Play an M3U playlist on Windows",
     "blurb_fr": "Installation sans droits administrateur et ajout de la playlist.",
     "blurb_en": "Install without administrator rights and add the playlist.", "fr": M3U_WIN_FR, "en": M3U_WIN_EN},
    {"slug": "guide-xtream-codes", "title_fr": "Ajouter un abonnement Xtream Codes", "title_en": "Add an Xtream Codes subscription",
     "blurb_fr": "Serveur, identifiant, mot de passe : tout ce qu'il faut savoir.",
     "blurb_en": "Server, username, password: everything you need to know.", "fr": XT_FR, "en": XT_EN},
    {"slug": "guide-android-tv", "title_fr": "Installer Kastideo sur Android TV", "title_en": "Install Kastideo on Android TV",
     "blurb_fr": "APK, Downloader, clé USB et télécommande, sans désactiver la sécurité.",
     "blurb_en": "APK, Downloader, USB stick and remote, without disabling security.", "fr": ATV_FR, "en": ATV_EN},
    {"slug": "guide-raspberry-pi", "title_fr": "L'IPTV sur Raspberry Pi 4 ou 5", "title_en": "IPTV on a Raspberry Pi 4 or 5",
     "blurb_fr": "L'AppImage ARM 64 bits, de l'installation au salon.",
     "blurb_en": "The 64-bit ARM AppImage, from installation to the living room.", "fr": PI_FR, "en": PI_EN},
]

# ------------------------------------------------------------------- Nouveautés
NEWS_FR = """    <h1>Nouveautés de Kastideo</h1>
    <p class="page-lead">Les dernières versions de Kastideo et ce qu'elles apportent, lues directement sur la page des versions GitHub.</p>

    <div id="releases" class="releases" aria-live="polite" data-loading="Chargement des versions…" data-error="Impossible de charger les versions pour le moment. Elles restent consultables sur la page des versions de GitHub." data-more="Toutes les versions sur GitHub" data-download="Télécharger" data-notes="Notes de version" data-none="Pas de notes pour cette version." data-stable="Stable" data-preview="Aperçu" data-mac="Mac" data-desktop="Windows et Linux" data-android="Android">
      <p class="note">Chargement des versions…</p>
      <noscript><p class="note">Activez JavaScript pour voir la liste, ou ouvrez la <a href="https://github.com/jihemezes/kastideo/releases" target="_blank" rel="noopener">page des versions sur GitHub</a>.</p></noscript>
    </div>

    <h2 id="maj">Comment se passent les mises à jour</h2>
    <ul>
      <li><b>Mac :</b> Kastideo vérifie discrètement les mises à jour au démarrage, puis une fois par jour. Un bandeau l'annonce, jamais pendant un visionnage ni un enregistrement. La mise à jour est facultative et chaque mise à jour est signée.</li>
      <li><b>Windows et Linux :</b> la vérification se fait au démarrage puis toutes les 12 heures. <b>Installer et relancer</b> s'adapte à votre type d'installation.</li>
      <li><b>Android :</b> installez le nouvel APK par-dessus l'ancien, vos réglages sont conservés.</li>
    </ul>
    <p>Après une mise à jour, la fenêtre « Nouveautés » de l'application résume les changements de la version installée. Pour télécharger : <a href="telecharger.html">Télécharger Kastideo</a>.</p>
"""
NEWS_EN = """    <h1>What's new in Kastideo</h1>
    <p class="page-lead">The latest Kastideo versions and what they bring, read straight from the GitHub releases page.</p>

    <div id="releases" class="releases" aria-live="polite" data-loading="Loading versions…" data-error="Unable to load the versions right now. They can still be read on the GitHub releases page." data-more="All versions on GitHub" data-download="Download" data-notes="Release notes" data-none="No notes for this version." data-stable="Stable" data-preview="Preview" data-mac="Mac" data-desktop="Windows and Linux" data-android="Android">
      <p class="note">Loading versions…</p>
      <noscript><p class="note">Enable JavaScript to see the list, or open the <a href="https://github.com/jihemezes/kastideo/releases" target="_blank" rel="noopener">releases page on GitHub</a>.</p></noscript>
    </div>

    <h2 id="maj">How updates work</h2>
    <ul>
      <li><b>Mac:</b> Kastideo quietly checks for updates at launch, then once a day. A banner announces it, never during viewing or recording. The update is optional and every update is signed.</li>
      <li><b>Windows and Linux:</b> the check happens at launch and then every 12 hours. <b>Install and restart</b> adapts to your installation type.</li>
      <li><b>Android:</b> install the new APK over the old one, your settings are kept.</li>
    </ul>
    <p>After an update, the app's “What's new” window summarises the changes of the installed version. To download: <a href="telecharger.html">Download Kastideo</a>.</p>
"""

NEWS = {"slug": "nouveautes", "title_fr": "Nouveautés", "title_en": "What's new", "fr": NEWS_FR, "en": NEWS_EN}
