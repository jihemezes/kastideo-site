"""Pages Télécharger et Soutenir."""

REL = "https://github.com/jihemezes/kastideo/releases"

ROWS = [
    # (clé data-dl, appareil FR, appareil EN, fichier, état: stable|preview, famille de version)
    ("mac", "Mac (Apple, Intel)", "Mac (Apple, Intel)", "Kastideo-X.Y.Z.dmg", "stable", "mac"),
    ("win-setup", "Windows 10/11, 64 bits : installateur", "Windows 10/11, 64-bit: installer", "…-windows-x64-setup.exe", "preview", "desktop"),
    ("win-zip", "Windows 10/11, 64 bits : portable", "Windows 10/11, 64-bit: portable", "…-windows-x64.zip", "preview", "desktop"),
    ("deb22", "Zorin OS 17, Ubuntu 22.04", "Zorin OS 17, Ubuntu 22.04", "kastideo_…_ubuntu22.04_amd64.deb", "preview", "desktop"),
    ("deb24", "Zorin OS 18, Ubuntu 24.04", "Zorin OS 18, Ubuntu 24.04", "kastideo_…_ubuntu24.04_amd64.deb", "preview", "desktop"),
    ("appimage-x86", "Autre PC Linux 64 bits", "Other 64-bit Linux PC", "Kastideo-…-linux-x86_64.AppImage", "preview", "desktop"),
    ("appimage-arm", "Raspberry Pi 4 ou 5 (64 bits)", "Raspberry Pi 4 or 5 (64-bit)", "Kastideo-…-linux-aarch64.AppImage", "preview", "desktop"),
    ("apk-arm64", "Téléphone ou TV récent", "Recent phone or TV", "Kastideo-…-android-arm64-v8a.apk", "preview", "android"),
    ("apk-v7a", "Ancien appareil, boîtier 32 bits", "Older device, 32-bit box", "Kastideo-…-android-armeabi-v7a.apk", "preview", "android"),
    ("apk-universal", "Vous hésitez", "Not sure", "Kastideo-…-android-universal.apk", "preview", "android"),
]


def _rows(lang):
    out = []
    for key, fr, en, fname, state, fam in ROWS:
        dev = fr if lang == "fr" else en
        if lang == "fr":
            st = "Stable" if state == "stable" else "Aperçu"
            btn = "Télécharger"
        else:
            st = "Stable" if state == "stable" else "Preview"
            btn = "Download"
        href = REL + "/latest" if key == "mac" else REL
        out.append(
            f'          <tr><td>{dev}</td><td><code>{fname}</code></td><td>{st}</td>'
            f'<td><a class="btn ghost small" data-dl="{key}" href="{href}" target="_blank" rel="noopener">{btn}<small data-size="{key}"></small></a></td></tr>'
        )
    return "\n".join(out)


def _telecharger(lang):
    if lang == "fr":
        return f"""    <h1>Télécharger Kastideo</h1>
    <p class="page-lead">Kastideo est gratuit. Choisissez le fichier qui correspond à votre appareil : les liens pointent toujours vers la dernière version publiée.</p>
    <p class="versions-now">Dernières versions : Mac <b data-ver="mac">…</b> · Windows et Linux <b data-ver="desktop">…</b> · Android <b data-ver="android">…</b></p>

    <h2 id="choisir">Quel fichier pour quel appareil</h2>
    <div class="table-wrap" role="region" aria-label="Quel fichier télécharger" tabindex="0">
      <table class="ver-table">
        <thead><tr><th>Votre appareil</th><th>Fichier</th><th>État</th><th>Lien</th></tr></thead>
        <tbody>
{_rows("fr")}
        </tbody>
      </table>
    </div>
    <p class="note">Les versions Windows, Linux et Android sont des aperçus, publiés en pré-version sur GitHub. Elles fonctionnent bien, mais les retours restent précieux. Si un lien ne se met pas à jour, la liste complète est sur la <a href="{REL}" target="_blank" rel="noopener">page des versions</a>.</p>

    <h2 id="guides">Guides d'installation</h2>
    <p><a href="mac.html">Mac</a> · <a href="windows.html">Windows</a> · <a href="linux.html">Linux</a> · <a href="android.html">Android et Android TV</a></p>

    <h2 id="apres">Après l'installation</h2>
    <p>Kastideo ne fournit aucun contenu : à la première ouverture, ajoutez votre source dans les réglages. Voir <a href="sources.html">Vos sources</a>.</p>
"""
    return f"""    <h1>Download Kastideo</h1>
    <p class="page-lead">Kastideo is free. Pick the file that matches your device: the links always point to the latest published version.</p>
    <p class="versions-now">Latest versions: Mac <b data-ver="mac">…</b> · Windows and Linux <b data-ver="desktop">…</b> · Android <b data-ver="android">…</b></p>

    <h2 id="choisir">Which file for which device</h2>
    <div class="table-wrap" role="region" aria-label="Which file to download" tabindex="0">
      <table class="ver-table">
        <thead><tr><th>Your device</th><th>File</th><th>Status</th><th>Link</th></tr></thead>
        <tbody>
{_rows("en")}
        </tbody>
      </table>
    </div>
    <p class="note">Windows, Linux and Android versions are previews, published as pre-releases on GitHub. They work well, but feedback remains valuable. If a link does not update, the full list is on the <a href="{REL}" target="_blank" rel="noopener">releases page</a>.</p>

    <h2 id="guides">Installation guides</h2>
    <p><a href="mac.html">Mac</a> · <a href="windows.html">Windows</a> · <a href="linux.html">Linux</a> · <a href="android.html">Android and Android TV</a></p>

    <h2 id="apres">After installing</h2>
    <p>Kastideo provides no content: at first launch, add your source in the settings. See <a href="sources.html">Your sources</a>.</p>
"""


_KOFI_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path class="steam s1" d="M8 2.5c-.9.9.9 1.6 0 2.5"/><path class="steam s2" d="M11.5 2c-.9.9.9 1.6 0 2.5"/><path class="steam s3" d="M15 2.5c-.9.9.9 1.6 0 2.5"/><path d="M4 8h13v6a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5V8z"/><path d="M17 9.5h1.6a2.4 2.4 0 0 1 0 4.8H16.6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M5 21.5h11" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'


def kofi_button(label, big=False, en=None):
    cls = "kofi-btn big" if big else "kofi-btn"
    attrs = f' data-fr="{label}" data-en="{en}"' if en else ""
    return f'<a class="{cls}" href="https://ko-fi.com/jihemezes" target="_blank" rel="noopener">{_KOFI_SVG}<span{attrs}>{label}</span></a>'


def _soutenir(lang):
    if lang == "fr":
        return f"""    <h1>Soutenir le projet</h1>
    <p class="page-lead">Kastideo est gratuit, et il le reste. Si l'application vous rend service, vous pouvez encourager son développement : c'est entièrement facultatif.</p>
    <p class="actions">{kofi_button("Offrir un café sur Ko-fi", True)}</p>

    <h2 id="gratuit">Gratuit, vraiment</h2>
    <p>Aucune fonction n'est réservée à ceux qui donnent, aucun compte n'est demandé et aucune publicité n'est affichée. Un café, c'est simplement un merci, et du temps pour les prochaines versions.</p>

    <h2 id="autres">Il y a d'autres façons d'aider</h2>
    <ul>
      <li><b>Signaler un problème</b> sur <a href="https://github.com/jihemezes/kastideo/issues" target="_blank" rel="noopener">GitHub</a>. Joignez le Journal de lecture (il se copie en un clic, identifiants masqués) : c'est ce qui permet de corriger vite. Les versions Windows, Linux et Android sont des aperçus, vos retours comptent beaucoup.</li>
      <li><b>Proposer une idée</b> au même endroit.</li>
      <li><b>Parler de Kastideo</b> à quelqu'un qui cherche un lecteur sobre et rapide.</li>
    </ul>
    <p>Pour toute autre question : <code>contact@kastideo.com</code>.</p>
"""
    return f"""    <h1>Support the project</h1>
    <p class="page-lead">Kastideo is free, and stays free. If the app serves you well, you can support its development: it is entirely optional.</p>
    <p class="actions">{kofi_button("Buy me a coffee on Ko-fi", True)}</p>

    <h2 id="gratuit">Really free</h2>
    <p>No feature is reserved for those who give, no account is asked and no ads are shown. A coffee is simply a thank-you, and time for the next versions.</p>

    <h2 id="autres">Other ways to help</h2>
    <ul>
      <li><b>Report a problem</b> on <a href="https://github.com/jihemezes/kastideo/issues" target="_blank" rel="noopener">GitHub</a>. Attach the playback log (copied in one click, credentials masked): it is what lets problems be fixed quickly. Windows, Linux and Android versions are previews, your feedback matters a lot.</li>
      <li><b>Suggest an idea</b> in the same place.</li>
      <li><b>Tell someone</b> looking for a frugal, fast player.</li>
    </ul>
    <p>For anything else: <code>contact@kastideo.com</code>.</p>
"""


OTHER = [
    {
        "slug": "telecharger",
        "title_fr": "Télécharger",
        "title_en": "Download",
        "desc": "Télécharger Kastideo pour Mac, Windows, Linux ou Android : le bon fichier pour chaque appareil, toujours la dernière version.",
        "fr": _telecharger("fr"),
        "en": _telecharger("en"),
    },
    {
        "slug": "soutenir",
        "title_fr": "Soutenir le projet",
        "title_en": "Support the project",
        "desc": "Kastideo est gratuit. Encourager le projet sur Ko-fi, signaler un problème ou proposer une idée.",
        "fr": _soutenir("fr"),
        "en": _soutenir("en"),
    },
]
