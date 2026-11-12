"""Pages par plateforme (Mac, Windows, Linux, Android, iPhone et iPad, Apple TV). Texte FR et EN.

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
      <a class="dl" data-dl="apk-arm64" href="{REL}" target="_blank" rel="noopener"><b>arm64-v8a</b><span>Appareil récent (cas le plus courant)</span><span class="short">Adresse courte : <code>kastideo.com/tv</code></span><small data-size="apk-arm64"></small></a>
      <a class="dl" data-dl="apk-v7a" href="{REL}" target="_blank" rel="noopener"><b>armeabi-v7a</b><span>Ancien appareil ou boîtier 32 bits</span><span class="short">Adresse courte : <code>kastideo.com/tv32</code></span><small data-size="apk-v7a"></small></a>
      <a class="dl" data-dl="apk-universal" href="{REL}" target="_blank" rel="noopener"><b>universal</b><span>Si vous hésitez (fichier plus gros)</span><span class="short">Adresse courte : <code>kastideo.com/tvu</code></span><small data-size="apk-universal"></small></a>
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
      <a class="dl" data-dl="apk-arm64" href="{REL}" target="_blank" rel="noopener"><b>arm64-v8a</b><span>Recent device (the most common case)</span><span class="short">Short address: <code>kastideo.com/tv</code></span><small data-size="apk-arm64"></small></a>
      <a class="dl" data-dl="apk-v7a" href="{REL}" target="_blank" rel="noopener"><b>armeabi-v7a</b><span>Older device or 32-bit box</span><span class="short">Short address: <code>kastideo.com/tv32</code></span><small data-size="apk-v7a"></small></a>
      <a class="dl" data-dl="apk-universal" href="{REL}" target="_blank" rel="noopener"><b>universal</b><span>If unsure (larger file)</span><span class="short">Short address: <code>kastideo.com/tvu</code></span><small data-size="apk-universal"></small></a>
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
    # --------------------------------------------------------------------- IOS
    {
        "slug": "ios",
        "title_fr": "Kastideo pour iPhone et iPad",
        "title_en": "Kastideo for iPhone and iPad",
        "blurb_fr": "En test via TestFlight, bientôt sur l'App Store nous l'espérons.",
        "blurb_en": "Being tested through TestFlight, hopefully soon on the App Store.",
        "tag": "preview",
        "desc": "Kastideo pour iPhone et iPad (iOS 17 ou plus récent) : en test via TestFlight, comment participer, ce que propose l'application, synchronisation iCloud.",
        "fr": """    <h1>Kastideo pour iPhone et iPad</h1>
    <p class="page-lead">Une application native pour iOS 17 ou plus récent. Elle est en test via TestFlight, le service d'Apple pour essayer une application avant sa publication. Nous espérons la voir bientôt sur l'App Store, sans date annoncée pour l'instant.</p>
    <div class="callout"><b class="label">Pas encore sur l'App Store</b><p>Pour l'instant, le seul moyen d'essayer Kastideo sur iPhone et iPad est TestFlight. Il n'y a aucun fichier à installer à la main.</p></div>

    <h2 id="participer">Participer au test</h2>
    <ol>
      <li>Écrivez à <code>contact@kastideo.com</code> en indiquant l'adresse e-mail de votre identifiant Apple et votre appareil (iPhone ou iPad). Vous recevez une invitation TestFlight.</li>
      <li>Installez l'application gratuite <b>TestFlight</b> depuis l'App Store.</li>
      <li>Ouvrez l'invitation, puis installez <b>Kastideo</b> depuis TestFlight.</li>
    </ol>
    <p>Les mises à jour arrivent aussi par TestFlight. Vos retours sont précieux : le journal de lecture se partage depuis Réglages &gt; À propos.</p>

    <h2 id="demarrer">Premier lancement</h2>
    <p>Lisez et acceptez l'avertissement, puis appuyez sur <b>Ajouter une source</b> (Xtream Codes ou liste M3U). Vous pouvez aussi importer votre configuration depuis un Mac, un PC ou un appareil Android : sources, favoris et catégories. Kastideo ne fournit aucune chaîne : le contenu vient de vos sources, dont vous devez vérifier la légalité. Voir <a href="guide-m3u.html">Lire une playlist M3U</a>.</p>

    <h2 id="fonctions">Ce que propose l'application</h2>
    <ul>
      <li>Accueil avec reprise de la lecture, favoris et récents.</li>
      <li>Direct en liste, en affichage Cinéma, par thèmes ou dans le guide TV, avec le replay quand votre fournisseur le propose.</li>
      <li>Films et séries en affichage Cinéma ou en grille, avec fiches, saisons et épisodes.</li>
      <li>Lecteur plein écran, mini-lecteur, direct en différé et son qui continue écran verrouillé.</li>
      <li>Enregistrement du direct, téléchargements, alertes de programmes.</li>
      <li>Mes vidéos : Jellyfin, Emby, Plex, dossiers et galerie de l'appareil. YouTube.</li>
      <li><a href="multivue.html">MultiVue</a> avec plusieurs chaînes en même temps, si vos sources autorisent plusieurs connexions.</li>
    </ul>

    <h2 id="icloud">Synchronisation iCloud</h2>
    <p>En option et désactivée par défaut, la synchronisation iCloud retrouve vos sources, favoris, catégories, réglages d'affichage, reprise de lecture et fiches corrigées sur tous vos iPhone et iPad. Les mots de passe passent par le Trousseau iCloud, chiffré de bout en bout.</p>

    <h2 id="limites">Ce qui diffère du Mac</h2>
    <ul>
      <li>Pas d'image dans l'image pour l'instant.</li>
      <li>Pas d'enregistrement programmé : l'application ne peut pas se réveiller seule sur iPhone. Utilisez les alertes de programmes, ou le Mac.</li>
      <li>AirPlay envoie le son vers une Apple TV ou un HomePod. Pour la vidéo, utilisez la recopie d'écran d'iOS.</li>
    </ul>
    <p>Voir aussi <a href="apple-tv.html">Kastideo pour Apple TV</a>.</p>
""",
        "en": """    <h1>Kastideo for iPhone and iPad</h1>
    <p class="page-lead">A native app for iOS 17 or later. It is being tested through TestFlight, Apple's service for trying an app before its release. We hope to see it on the App Store soon, with no date announced for now.</p>
    <div class="callout"><b class="label">Not on the App Store yet</b><p>For now, the only way to try Kastideo on iPhone and iPad is TestFlight. There is no file to install by hand.</p></div>

    <h2 id="participer">Join the test</h2>
    <ol>
      <li>Write to <code>contact@kastideo.com</code> with the email address of your Apple ID and your device (iPhone or iPad). You receive a TestFlight invitation.</li>
      <li>Install the free <b>TestFlight</b> app from the App Store.</li>
      <li>Open the invitation, then install <b>Kastideo</b> from TestFlight.</li>
    </ol>
    <p>Updates also arrive through TestFlight. Your feedback is valuable: the playback log can be shared from Settings &gt; About.</p>

    <h2 id="demarrer">First launch</h2>
    <p>Read and accept the notice, then tap <b>Add a source</b> (Xtream Codes or M3U list). You can also import your configuration from a Mac, a PC or an Android device: sources, favourites and categories. Kastideo provides no channels: content comes from your sources, whose legality you must check. See <a href="guide-m3u.html">Play an M3U playlist</a>.</p>

    <h2 id="fonctions">What the app offers</h2>
    <ul>
      <li>Home with resume playback, favourites and recents.</li>
      <li>Live TV as a list, in Cinema display, by themes or in the TV guide, with replay when your provider offers it.</li>
      <li>Movies and series in Cinema display or as a grid, with details pages, seasons and episodes.</li>
      <li>Full-screen player, mini player, time-shifted live and sound that keeps playing with the screen locked.</li>
      <li>Live recording, downloads, programme alerts.</li>
      <li>My videos: Jellyfin, Emby, Plex, folders and the device gallery. YouTube.</li>
      <li><a href="multivue.html">MultiView</a> with several channels at once, if your sources allow several connections.</li>
    </ul>

    <h2 id="icloud">iCloud sync</h2>
    <p>Optional and off by default, iCloud sync brings your sources, favourites, categories, display settings, resume positions and corrected pages to all your iPhones and iPads. Passwords go through iCloud Keychain, end-to-end encrypted.</p>

    <h2 id="limites">What differs from the Mac</h2>
    <ul>
      <li>No picture in picture for now.</li>
      <li>No scheduled recording: the app cannot wake itself on iPhone. Use programme alerts, or the Mac.</li>
      <li>AirPlay sends sound to an Apple TV or a HomePod. For video, use iOS screen mirroring.</li>
    </ul>
    <p>See also <a href="apple-tv.html">Kastideo for Apple TV</a>.</p>
""",
    },
    # ---------------------------------------------------------------- APPLE TV
    {
        "slug": "apple-tv",
        "title_fr": "Kastideo pour Apple TV",
        "title_en": "Kastideo for Apple TV",
        "blurb_fr": "En test via TestFlight, bientôt sur l'App Store nous l'espérons.",
        "blurb_en": "Being tested through TestFlight, hopefully soon on the App Store.",
        "tag": "preview",
        "desc": "Kastideo pour Apple TV : en test via TestFlight, comment participer, et en attendant, comment regarder Kastideo sur une Apple TV.",
        "fr": """    <h1>Kastideo pour Apple TV</h1>
    <p class="page-lead">Une version pour Apple TV est en préparation. Elle est en test via TestFlight, le service d'Apple pour essayer une application avant sa publication. Nous espérons la voir bientôt sur l'App Store, sans date annoncée pour l'instant.</p>
    <div class="callout"><b class="label">Pas encore sur l'App Store</b><p>Pour l'instant, le seul moyen d'essayer Kastideo sur Apple TV est TestFlight. Cette version est un test : elle peut changer et ses fonctions ne sont pas toutes décrites ici.</p></div>

    <h2 id="participer">Participer au test</h2>
    <ol>
      <li>Écrivez à <code>contact@kastideo.com</code> en indiquant l'adresse e-mail de votre identifiant Apple et le modèle de votre Apple TV. Vous recevez une invitation TestFlight.</li>
      <li>Sur l'Apple TV, installez l'application gratuite <b>TestFlight</b> depuis l'App Store.</li>
      <li>Ouvrez l'invitation, puis installez <b>Kastideo</b> depuis TestFlight.</li>
    </ol>
    <p>Les mises à jour arrivent aussi par TestFlight. Vos retours sont précieux.</p>

    <h2 id="attendant">En attendant</h2>
    <ul>
      <li>Sur iPhone et iPad, Kastideo est aussi en test : voir <a href="ios.html">Kastideo pour iPhone et iPad</a>.</li>
      <li>Depuis un Mac, vous pouvez envoyer l'image vers une Apple TV par la recopie d'écran de macOS : voir <a href="cast.html">Envoyer à la télévision</a>.</li>
    </ul>
    <p>Kastideo ne fournit aucune chaîne : le contenu vient de vos sources, dont vous devez vérifier la légalité.</p>
""",
        "en": """    <h1>Kastideo for Apple TV</h1>
    <p class="page-lead">A version for Apple TV is in the works. It is being tested through TestFlight, Apple's service for trying an app before its release. We hope to see it on the App Store soon, with no date announced for now.</p>
    <div class="callout"><b class="label">Not on the App Store yet</b><p>For now, the only way to try Kastideo on Apple TV is TestFlight. This version is a test: it may change and not all its features are described here.</p></div>

    <h2 id="participer">Join the test</h2>
    <ol>
      <li>Write to <code>contact@kastideo.com</code> with the email address of your Apple ID and your Apple TV model. You receive a TestFlight invitation.</li>
      <li>On the Apple TV, install the free <b>TestFlight</b> app from the App Store.</li>
      <li>Open the invitation, then install <b>Kastideo</b> from TestFlight.</li>
    </ol>
    <p>Updates also arrive through TestFlight. Your feedback is valuable.</p>

    <h2 id="attendant">In the meantime</h2>
    <ul>
      <li>On iPhone and iPad, Kastideo is also being tested: see <a href="ios.html">Kastideo for iPhone and iPad</a>.</li>
      <li>From a Mac, you can send the picture to an Apple TV with macOS screen mirroring: see <a href="cast.html">Casting to a TV</a>.</li>
    </ul>
    <p>Kastideo provides no channels: content comes from your sources, whose legality you must check.</p>
""",
    },
]
