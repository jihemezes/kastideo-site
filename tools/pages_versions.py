"""Pages par plateforme (Mac, Windows, Linux, Android). Texte FR et EN.

Les boutons [data-dl] sont complétés par site.js avec les liens de la dernière version.
[data-ver="mac|desktop|android"] reçoit le numéro de version.
"""

REL = "https://github.com/jihemezes/kastideo/releases"

VERSIONS = [
    # --------------------------------------------------------------------- MAC
    {
        "slug": "mac",
        "title_fr": "Kastideo pour Mac",
        "title_en": "Kastideo for Mac",
        "blurb_fr": "La version stable : signée, vérifiée par Apple, mises à jour automatiques.",
        "blurb_en": "The stable version: signed, checked by Apple, automatic updates.",
        "tag": "stable",
        "desc": "Télécharger et installer Kastideo sur Mac : configuration requise, installation, mises à jour automatiques.",
        "fr": f"""    <h1>Kastideo pour Mac</h1>
    <p class="page-lead">La version de référence, celle où les nouveautés arrivent en premier. Version actuelle : <b data-ver="mac">…</b>.</p>
    <p class="actions"><a class="btn primary" data-dl="mac" href="{REL}/latest" target="_blank" rel="noopener">Télécharger pour Mac<small data-size="mac"></small></a></p>
    <p class="short-url">Adresse courte : <code>kastideo.com/dl/mac</code>. Dans un terminal : <code>curl -LJO https://kastideo.com/dl/mac</code></p>

    <h2 id="config">Configuration requise</h2>
    <ul>
      <li>macOS 14 Sonoma ou plus récent.</li>
      <li>Un processeur Apple (M1 à M4) ou Intel.</li>
    </ul>

    <h2 id="installer">Installer</h2>
    <ol>
      <li>Téléchargez le fichier <code>Kastideo-X.Y.Z.dmg</code> avec le bouton ci-dessus.</li>
      <li>Ouvrez-le et glissez Kastideo dans le dossier Applications.</li>
      <li>Lancez l'application. Elle est signée avec un certificat développeur Apple et vérifiée par Apple : macOS ne demande aucun contournement.</li>
    </ol>
    <p>Au premier lancement, ajoutez votre source (Xtream Codes, M3U, dossier ou serveur) dans les réglages : voir <a href="sources.html">Vos sources</a>.</p>

    <h2 id="maj">Mises à jour</h2>
    <p>Kastideo vérifie les mises à jour avec Sparkle, au démarrage. Un bandeau apparaît seulement quand vous ne regardez rien, jamais pendant un visionnage ni un enregistrement. L'installation est facultative et les mises à jour sont signées. Une option permet de recevoir aussi les versions bêta.</p>

    <h2 id="mac-seulement">Ce qui est propre au Mac</h2>
    <ul>
      <li>Enregistrements convertis en MP4, lisibles par QuickTime, l'iPhone et l'iPad.</li>
      <li>Panneau Informations avec choix de la piste audio et des sous-titres.</li>
      <li>Mémoire tampon réglable : Rapide, Équilibré ou Stable.</li>
      <li>Envoi vers Apple TV par la recopie d'écran de macOS : voir <a href="cast.html">Envoyer à la télévision</a>.</li>
    </ul>
""",
        "en": f"""    <h1>Kastideo for Mac</h1>
    <p class="page-lead">The reference version, where new features arrive first. Current version: <b data-ver="mac">…</b>.</p>
    <p class="actions"><a class="btn primary" data-dl="mac" href="{REL}/latest" target="_blank" rel="noopener">Download for Mac<small data-size="mac"></small></a></p>
    <p class="short-url">Short address: <code>kastideo.com/dl/mac</code>. In a terminal: <code>curl -LJO https://kastideo.com/dl/mac</code></p>

    <h2 id="config">Requirements</h2>
    <ul>
      <li>macOS 14 Sonoma or later.</li>
      <li>An Apple processor (M1 to M4) or Intel.</li>
    </ul>

    <h2 id="installer">Installing</h2>
    <ol>
      <li>Download the <code>Kastideo-X.Y.Z.dmg</code> file with the button above.</li>
      <li>Open it and drag Kastideo into the Applications folder.</li>
      <li>Launch the app. It is signed with an Apple developer certificate and checked by Apple: macOS asks for no workaround.</li>
    </ol>
    <p>At first launch, add your source (Xtream Codes, M3U, folder or server) in the settings: see <a href="sources.html">Your sources</a>.</p>

    <h2 id="maj">Updates</h2>
    <p>Kastideo checks for updates with Sparkle, at launch. A banner appears only when you are not watching anything, never during viewing or recording. Installing is optional and updates are signed. An option also lets you receive beta versions.</p>

    <h2 id="mac-seulement">What is specific to Mac</h2>
    <ul>
      <li>Recordings converted to MP4, playable by QuickTime, iPhone and iPad.</li>
      <li>Information panel with audio track and subtitle selection.</li>
      <li>Adjustable buffer: Fast, Balanced or Stable.</li>
      <li>Casting to Apple TV through macOS screen mirroring: see <a href="cast.html">Casting to a TV</a>.</li>
    </ul>
""",
    },
    # ----------------------------------------------------------------- WINDOWS
    {
        "slug": "windows",
        "title_fr": "Kastideo pour Windows",
        "title_en": "Kastideo for Windows",
        "blurb_fr": "Aperçu : installateur sans droits administrateur, ou version portable.",
        "blurb_en": "Preview: installer with no administrator rights, or portable version.",
        "tag": "preview",
        "desc": "Télécharger et installer Kastideo sur Windows 10 ou 11 : installateur Setup.exe ou version portable, avertissement SmartScreen.",
        "fr": f"""    <h1>Kastideo pour Windows</h1>
    <p class="page-lead">Une version en aperçu : elle fonctionne bien, mais vos retours restent précieux. Version actuelle : <b data-ver="desktop">…</b>.</p>
    <p class="actions">
      <a class="btn primary" data-dl="win-setup" href="{REL}" target="_blank" rel="noopener">Installateur Setup.exe<small data-size="win-setup"></small></a>
      <a class="btn ghost" data-dl="win-zip" href="{REL}" target="_blank" rel="noopener">Version portable (.zip)<small data-size="win-zip"></small></a>
    </p>
    <p class="short-url">Adresses courtes : <code>kastideo.com/dl/windows</code> (installateur) et <code>kastideo.com/dl/windows-zip</code> (portable). Dans PowerShell : <code>Invoke-WebRequest https://kastideo.com/dl/windows -OutFile Kastideo-setup.exe</code></p>

    <h2 id="config">Configuration requise</h2>
    <ul><li>Windows 10 ou 11, 64 bits.</li></ul>

    <h2 id="installer">Installer</h2>
    <ol>
      <li>Téléchargez <code>Kastideo-…-windows-x64-setup.exe</code> et lancez-le. L'installation se fait pour votre compte, sans droits administrateur.</li>
      <li>Ou, sans installation : téléchargez <code>Kastideo-…-windows-x64.zip</code>, décompressez-le où vous voulez et lancez Kastideo.exe.</li>
    </ol>
    <div class="callout"><b class="label">Avertissement de Windows</b><p>L'application n'est pas encore signée : Windows affiche « Windows a protégé votre ordinateur ». Cliquez sur Informations complémentaires, puis sur Exécuter quand même. Le message ne revient pas ensuite.</p></div>

    <h2 id="maj">Mises à jour</h2>
    <p>Kastideo consulte les nouvelles versions au démarrage puis toutes les 12 heures. Quand une version est disponible, Installer et relancer télécharge et installe la mise à jour selon votre type d'installation (installateur ou version portable).</p>

    <h2 id="pc-seulement">Ce qui est propre à Windows</h2>
    <ul>
      <li>Enregistrements en MKV, avec répétition (tous les jours, du lundi au vendredi, chaque semaine).</li>
      <li>MultiVue avec choix de la disposition et groupes de chaînes mémorisés.</li>
      <li>ffmpeg est fourni, pour l'envoi vers un téléviseur : voir <a href="cast.html">Envoyer à la télévision</a>.</li>
      <li>Option de lancement à l'ouverture de session, pratique pour les enregistrements programmés.</li>
    </ul>
""",
        "en": f"""    <h1>Kastideo for Windows</h1>
    <p class="page-lead">A preview version: it works well, but your feedback remains valuable. Current version: <b data-ver="desktop">…</b>.</p>
    <p class="actions">
      <a class="btn primary" data-dl="win-setup" href="{REL}" target="_blank" rel="noopener">Setup.exe installer<small data-size="win-setup"></small></a>
      <a class="btn ghost" data-dl="win-zip" href="{REL}" target="_blank" rel="noopener">Portable version (.zip)<small data-size="win-zip"></small></a>
    </p>
    <p class="short-url">Short addresses: <code>kastideo.com/dl/windows</code> (installer) and <code>kastideo.com/dl/windows-zip</code> (portable). In PowerShell: <code>Invoke-WebRequest https://kastideo.com/dl/windows -OutFile Kastideo-setup.exe</code></p>

    <h2 id="config">Requirements</h2>
    <ul><li>Windows 10 or 11, 64-bit.</li></ul>

    <h2 id="installer">Installing</h2>
    <ol>
      <li>Download <code>Kastideo-…-windows-x64-setup.exe</code> and run it. Installation is per user, with no administrator rights.</li>
      <li>Or, with no installation: download <code>Kastideo-…-windows-x64.zip</code>, extract it wherever you like and run Kastideo.exe.</li>
    </ol>
    <div class="callout"><b class="label">Windows warning</b><p>The app is not signed yet: Windows shows “Windows protected your PC”. Click More info, then Run anyway. The message does not come back afterwards.</p></div>

    <h2 id="maj">Updates</h2>
    <p>Kastideo checks for new versions at launch and then every 12 hours. When one is available, Install and restart downloads and installs the update according to your installation type (installer or portable version).</p>

    <h2 id="pc-seulement">What is specific to Windows</h2>
    <ul>
      <li>MKV recordings, with repeat (every day, Monday to Friday, every week).</li>
      <li>MultiView with layout choice and saved channel groups.</li>
      <li>ffmpeg is included, for casting to a TV: see <a href="cast.html">Casting to a TV</a>.</li>
      <li>Option to launch at sign-in, handy for scheduled recordings.</li>
    </ul>
""",
    },
    # ------------------------------------------------------------------- LINUX
    {
        "slug": "linux",
        "title_fr": "Kastideo pour Linux",
        "title_en": "Kastideo for Linux",
        "blurb_fr": "Aperçu : paquets .deb pour Zorin OS et Ubuntu, AppImage pour les autres et le Raspberry Pi.",
        "blurb_en": "Preview: .deb packages for Zorin OS and Ubuntu, AppImage for others and Raspberry Pi.",
        "tag": "preview",
        "desc": "Installer Kastideo sur Linux : paquet .deb pour Zorin OS et Ubuntu 22.04 ou 24.04, AppImage pour les autres distributions et le Raspberry Pi.",
        "fr": f"""    <h1>Kastideo pour Linux</h1>
    <p class="page-lead">Une version en aperçu, en deux formats selon votre système. Version actuelle : <b data-ver="desktop">…</b>.</p>

    <h2 id="choisir">Quel fichier choisir</h2>
    <p>Deux commandes dans un terminal donnent la réponse : <code>lsb_release -d</code> pour la distribution et <code>uname -m</code> pour l'architecture.</p>
    <div class="dl-grid">
      <a class="dl" data-dl="deb22" href="{REL}" target="_blank" rel="noopener"><b>.deb, Zorin OS 17 · Ubuntu 22.04</b><span>ubuntu22.04_amd64</span><span class="short">Adresse courte : <code>kastideo.com/dl/deb22</code></span><small data-size="deb22"></small></a>
      <a class="dl" data-dl="deb24" href="{REL}" target="_blank" rel="noopener"><b>.deb, Zorin OS 18 · Ubuntu 24.04</b><span>ubuntu24.04_amd64</span><span class="short">Adresse courte : <code>kastideo.com/dl/deb</code></span><small data-size="deb24"></small></a>
      <a class="dl" data-dl="appimage-x86" href="{REL}" target="_blank" rel="noopener"><b>AppImage, PC 64 bits</b><span>linux-x86_64 (<code>uname -m</code> : x86_64)</span><span class="short">Adresse courte : <code>kastideo.com/dl/linux</code></span><small data-size="appimage-x86"></small></a>
      <a class="dl" data-dl="appimage-arm" href="{REL}" target="_blank" rel="noopener"><b>AppImage, Raspberry Pi 4 ou 5</b><span>linux-aarch64 (<code>uname -m</code> : aarch64, système 64 bits)</span><span class="short">Adresse courte : <code>kastideo.com/dl/linux-arm</code></span><small data-size="appimage-arm"></small></a>
    </div>
    <p class="short-url">Dans un terminal, par exemple : <code>curl -LJO https://kastideo.com/dl/linux</code> (AppImage PC 64 bits).</p>

    <h2 id="deb">Installer le paquet .deb</h2>
    <p>Double-cliquez sur le fichier, ou ouvrez un terminal dans le dossier Téléchargements :</p>
    <pre><code>sudo apt install ./kastideo_X.Y.Z_ubuntu22.04_amd64.deb</code></pre>
    <p>Remplacez le nom par celui du fichier téléchargé. Pour l'envoi vers un téléviseur, installez aussi ffmpeg :</p>
    <pre><code>sudo apt install ffmpeg</code></pre>

    <h2 id="appimage">Utiliser l'AppImage</h2>
    <ol>
      <li>Faites un clic droit sur le fichier, Propriétés, Permissions, et cochez Autoriser l'exécution comme un programme. Ou en terminal : <code>chmod +x Kastideo-…AppImage</code>.</li>
      <li>Double-cliquez dessus. ffmpeg est déjà inclus.</li>
      <li>S'il ne démarre pas, installez la bibliothèque FUSE : <code>sudo apt install libfuse2</code> (<code>libfuse2t64</code> sur Ubuntu 24.04 et Zorin OS 18).</li>
    </ol>

    <h2 id="maj">Mises à jour</h2>
    <p>Kastideo consulte les nouvelles versions au démarrage puis toutes les 12 heures. Installer et relancer s'adapte à votre type d'installation : pour un .deb, le nouveau paquet est téléchargé puis installé après votre accord.</p>
""",
        "en": f"""    <h1>Kastideo for Linux</h1>
    <p class="page-lead">A preview version, in two formats depending on your system. Current version: <b data-ver="desktop">…</b>.</p>

    <h2 id="choisir">Which file to choose</h2>
    <p>Two terminal commands give the answer: <code>lsb_release -d</code> for the distribution and <code>uname -m</code> for the architecture.</p>
    <div class="dl-grid">
      <a class="dl" data-dl="deb22" href="{REL}" target="_blank" rel="noopener"><b>.deb, Zorin OS 17 · Ubuntu 22.04</b><span>ubuntu22.04_amd64</span><span class="short">Short address: <code>kastideo.com/dl/deb22</code></span><small data-size="deb22"></small></a>
      <a class="dl" data-dl="deb24" href="{REL}" target="_blank" rel="noopener"><b>.deb, Zorin OS 18 · Ubuntu 24.04</b><span>ubuntu24.04_amd64</span><span class="short">Short address: <code>kastideo.com/dl/deb</code></span><small data-size="deb24"></small></a>
      <a class="dl" data-dl="appimage-x86" href="{REL}" target="_blank" rel="noopener"><b>AppImage, 64-bit PC</b><span>linux-x86_64 (<code>uname -m</code>: x86_64)</span><span class="short">Short address: <code>kastideo.com/dl/linux</code></span><small data-size="appimage-x86"></small></a>
      <a class="dl" data-dl="appimage-arm" href="{REL}" target="_blank" rel="noopener"><b>AppImage, Raspberry Pi 4 or 5</b><span>linux-aarch64 (<code>uname -m</code>: aarch64, 64-bit system)</span><span class="short">Short address: <code>kastideo.com/dl/linux-arm</code></span><small data-size="appimage-arm"></small></a>
    </div>
    <p class="short-url">In a terminal, for example: <code>curl -LJO https://kastideo.com/dl/linux</code> (64-bit PC AppImage).</p>

    <h2 id="deb">Installing the .deb package</h2>
    <p>Double-click the file, or open a terminal in the Downloads folder:</p>
    <pre><code>sudo apt install ./kastideo_X.Y.Z_ubuntu22.04_amd64.deb</code></pre>
    <p>Replace the name with that of the downloaded file. To cast to a TV, also install ffmpeg:</p>
    <pre><code>sudo apt install ffmpeg</code></pre>

    <h2 id="appimage">Using the AppImage</h2>
    <ol>
      <li>Right-click the file, Properties, Permissions, and tick Allow executing as a program. Or in a terminal: <code>chmod +x Kastideo-…AppImage</code>.</li>
      <li>Double-click it. ffmpeg is already included.</li>
      <li>If it does not start, install the FUSE library: <code>sudo apt install libfuse2</code> (<code>libfuse2t64</code> on Ubuntu 24.04 and Zorin OS 18).</li>
    </ol>

    <h2 id="maj">Updates</h2>
    <p>Kastideo checks for new versions at launch and then every 12 hours. Install and restart adapts to your installation type: for a .deb, the new package is downloaded then installed after your approval.</p>
""",
    },
    # ----------------------------------------------------------------- ANDROID
    {
        "slug": "android",
        "title_fr": "Kastideo pour Android et Android TV",
        "title_en": "Kastideo for Android and Android TV",
        "blurb_fr": "Aperçu : téléphone, tablette et téléviseur, télécommande prise en charge.",
        "blurb_en": "Preview: phone, tablet and TV, remote control supported.",
        "tag": "preview",
        "desc": "Installer Kastideo sur Android et Android TV : choix de l'APK, installation hors Google Play, gestes tactiles et télécommande.",
        "fr": f"""    <h1>Kastideo pour Android et Android TV</h1>
    <p class="page-lead">Sur téléphone, tablette ou téléviseur (Google TV, Chromecast avec Google TV, Nvidia Shield, téléviseurs Philips, Sony, TCL). Version actuelle : <b data-ver="android">…</b>.</p>

    <h2 id="choisir">Quel APK choisir</h2>
    <div class="dl-grid">
      <a class="dl" data-dl="apk-arm64" href="{REL}" target="_blank" rel="noopener"><b>arm64-v8a</b><span>Appareil récent (cas le plus courant)</span><span class="short">Adresse courte : <code>kastideo.com/tv64</code></span><small data-size="apk-arm64"></small></a>
      <a class="dl" data-dl="apk-v7a" href="{REL}" target="_blank" rel="noopener"><b>armeabi-v7a</b><span>Ancien appareil ou boîtier 32 bits</span><span class="short">Adresse courte : <code>kastideo.com/tv32</code></span><small data-size="apk-v7a"></small></a>
      <a class="dl" data-dl="apk-universal" href="{REL}" target="_blank" rel="noopener"><b>universal</b><span>Si vous hésitez (fichier plus gros)</span><span class="short">Adresse courte : <code>kastideo.com/tv</code></span><small data-size="apk-universal"></small></a>
    </div>

    <h2 id="installer">Installer</h2>
    <p>Kastideo n'est pas sur Google Play : l'installation se fait à partir du fichier APK, sans modifier la sécurité de l'appareil.</p>
    <ol>
      <li>Téléchargez l'APK, puis ouvrez-le.</li>
      <li>Si Android bloque l'installation d'applications inconnues, touchez Paramètres et activez Autoriser depuis cette source pour l'application utilisée (Chrome, par exemple). Les autres restent bloquées.</li>
      <li>Confirmez l'installation. Si Play Protect affiche un avertissement, choisissez Installer quand même.</li>
    </ol>
    <p><b>Sur un téléviseur Android TV</b> : installez l'application gratuite Downloader et saisissez l'adresse de l'APK, ou copiez l'APK sur une clé USB et ouvrez-le avec un gestionnaire de fichiers, ou envoyez-le depuis un téléphone avec « Send Files to TV ».</p>

    <h2 id="telephone">Au doigt</h2>
    <p>Le menu ☰ ouvre les sections. Un appui long sur une chaîne, un film ou un épisode ouvre le menu (favori, enregistrer, replay…). Dans le lecteur, un appui affiche la barre ; un double appui à gauche recule de 10 s, à droite avance de 30 s, au centre met en pause ; glisser verticalement règle le volume (à droite) ou la luminosité (à gauche). En paysage, la chaîne passe en plein écran.</p>

    <h2 id="telecommande">À la télécommande</h2>
    <p>Sur Android TV, les flèches déplacent la sélection, OK valide et Retour revient en arrière. Pour le direct, l'interface TV s'ouvre par défaut : haut et bas (ou Chaîne +/−) changent de chaîne, les chiffres saisissent un numéro, gauche ouvre la liste des chaînes. Pour les films et séries, l'interface Cinéma s'ouvre : OK met en pause, gauche et droite reculent de 10 s ou avancent de 30 s. Les touches Lecture/Pause et Avance/Retour rapide sont prises en charge.</p>

    <h2 id="differences">Ce qui change par rapport à l'ordinateur</h2>
    <ul>
      <li>La diffusion vers un téléviseur se fait en mode direct et ne gère pas les fichiers locaux : voir <a href="cast.html">Envoyer à la télévision</a>.</li>
      <li>Les enregistrements et téléchargements sont rangés dans le dossier de l'application. Android peut interrompre une application en arrière-plan : gardez Kastideo ouvert et l'appareil branché pendant un enregistrement.</li>
      <li>Pas de lancement à l'ouverture de session. YouTube s'ouvre dans le navigateur de l'appareil.</li>
    </ul>

    <h2 id="maj">Mises à jour</h2>
    <p>Kastideo vous prévient quand une nouvelle version existe. Téléchargez le nouvel APK et installez-le par-dessus : vos réglages sont conservés.</p>

    <h2 id="depannage">Un souci ?</h2>
    <ul>
      <li>« Application non installée » : essayez l'APK universal, ou vérifiez qu'il reste de la place.</li>
      <li>Le fichier ne s'ouvre pas : utilisez un gestionnaire de fichiers plutôt que le navigateur.</li>
      <li>Une chaîne ne démarre pas : coupez le VPN et consultez le Journal de lecture (voir <a href="fiabilite.html#journal">Rapide, stable et sobre</a>).</li>
    </ul>
""",
        "en": f"""    <h1>Kastideo for Android and Android TV</h1>
    <p class="page-lead">On phone, tablet or TV (Google TV, Chromecast with Google TV, Nvidia Shield, Philips, Sony and TCL TVs). Current version: <b data-ver="android">…</b>.</p>

    <h2 id="choisir">Which APK to choose</h2>
    <div class="dl-grid">
      <a class="dl" data-dl="apk-arm64" href="{REL}" target="_blank" rel="noopener"><b>arm64-v8a</b><span>Recent device (the most common case)</span><span class="short">Short address: <code>kastideo.com/tv64</code></span><small data-size="apk-arm64"></small></a>
      <a class="dl" data-dl="apk-v7a" href="{REL}" target="_blank" rel="noopener"><b>armeabi-v7a</b><span>Older device or 32-bit box</span><span class="short">Short address: <code>kastideo.com/tv32</code></span><small data-size="apk-v7a"></small></a>
      <a class="dl" data-dl="apk-universal" href="{REL}" target="_blank" rel="noopener"><b>universal</b><span>If unsure (larger file)</span><span class="short">Short address: <code>kastideo.com/tv</code></span><small data-size="apk-universal"></small></a>
    </div>

    <h2 id="installer">Installing</h2>
    <p>Kastideo is not on Google Play: installation uses the APK file, without changing the device's security.</p>
    <ol>
      <li>Download the APK, then open it.</li>
      <li>If Android blocks installing unknown apps, tap Settings and enable Allow from this source for the app you are using (Chrome, for example). Others stay blocked.</li>
      <li>Confirm the installation. If Play Protect shows a warning, choose Install anyway.</li>
    </ol>
    <p><b>On an Android TV</b>: install the free Downloader app and type the APK address, or copy the APK onto a USB stick and open it with a file manager, or send it from a phone with “Send Files to TV”.</p>

    <h2 id="telephone">By touch</h2>
    <p>The ☰ menu opens the sections. A long press on a channel, movie or episode opens the menu (favourite, record, replay…). In the player, a tap shows the bar; a double-tap on the left skips back 10 s, on the right forward 30 s, in the centre pauses; a vertical swipe sets volume (right) or brightness (left). In landscape, the channel goes full screen.</p>

    <h2 id="telecommande">With a remote</h2>
    <p>On Android TV, arrows move the selection, OK confirms and Back goes back. For live TV, the TV interface opens by default: up and down (or Channel +/−) change channel, digits enter a number, left opens the channel list. For movies and series, the Cinema interface opens: OK pauses, left and right skip back 10 s or forward 30 s. The remote's Play/Pause and fast-forward/rewind keys are supported.</p>

    <h2 id="differences">What differs from the computer</h2>
    <ul>
      <li>Casting to a TV uses direct mode and does not handle local files: see <a href="cast.html">Casting to a TV</a>.</li>
      <li>Recordings and downloads are stored in the app's folder. Android may interrupt a background app: keep Kastideo open and the device plugged in during a recording.</li>
      <li>No launch at sign-in. YouTube opens in the device's browser.</li>
    </ul>

    <h2 id="maj">Updates</h2>
    <p>Kastideo tells you when a new version exists. Download the new APK and install it over the old one: your settings are kept.</p>

    <h2 id="depannage">Trouble?</h2>
    <ul>
      <li>“App not installed”: try the universal APK, or check there is enough free space.</li>
      <li>The file does not open: use a file manager rather than the browser.</li>
      <li>A channel does not start: turn off the VPN and check the playback log (see <a href="fiabilite.html#journal">Fast, stable and frugal</a>).</li>
    </ul>
""",
    },
]
