"""Schémas (silhouettes d'écrans) des pages de fonctions, en SVG inline.

Dessins originaux, sans capture de l'application. Les couleurs viennent de classes CSS
(site.css, bloc « Silhouettes ») pour rester accordées à la palette du site.
Légendes FR/EN. Usage : svg(slug, lang) -> HTML <figure> ou None.
"""
from html import escape

W, H = 640, 320


def R(x, y, w, h, c="pn", r=8):
    return f'<rect class="{c}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>'


def T(x, y, s, c="tx", a="start", size=None):
    st = f' font-size="{size}"' if size else ""
    return f'<text class="{c}" x="{x}" y="{y}" text-anchor="{a}"{st}>{escape(s)}</text>'


def C(x, y, r, c="ac"):
    return f'<circle class="{c}" cx="{x}" cy="{y}" r="{r}"/>'


def PLAY(x, y, s=22, c="ac"):
    return f'<path class="{c}" d="M{x} {y - s} L{x + s * 1.7} {y} L{x} {y + s} Z"/>'


def wrap(body, label):
    return (
        f'<figure class="shot"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{escape(label)}" '
        f'xmlns="http://www.w3.org/2000/svg">{R(0, 0, W, H, "bg", 18)}{body}</svg>'
        f'<figcaption>{escape(label)}</figcaption></figure>'
    )


TXT = {
    "fr": {
        "chan": "Chaînes", "ready": "Prête en 0,8 s", "health": "Excellent · HD", "delay": "DIFFÉRÉ −2:34",
        "catch": "Rattraper", "live": "Retour au direct",
        "direct": "Schéma : le lecteur avec la liste des chaînes, la santé du flux et le différé",
        "now": "En ce moment", "tonight": "Ce soir", "chans": "Chaînes", "guide": "Guide TV",
        "guidecap": "Schéma : le guide en grille, avec les thèmes au-dessus",
        "classic": "Classique", "cinema": "Cinéma", "tv": "TV", "side": "Barre", "list": "Liste", "player": "Lecteur",
        "featured": "À la une", "resume": "Reprendre",
        "ifcap": "Schéma : les trois interfaces au choix, Classique, Cinéma et TV",
        "mv": "Schéma : la MultiVue avec quatre chaînes, le son sur la vignette active",
        "sound": "Son",
        "rec": "Enregistrer", "sched": "Programmé", "queue": "Téléchargements",
        "reccap": "Schéma : le bouton d'enregistrement, les programmations et la file de téléchargements",
        "pc": "Ordinateur", "tvs": "Téléviseur", "casting": "Diffusion en cours",
        "castcap": "Schéma : de l'ordinateur au téléviseur, la barre de lecture reste la télécommande",
        "replay": "Revoir", "fromstart": "Revoir depuis le début", "past": "Programmes passés", "today": "Aujourd'hui",
        "replaycap": "Schéma : le guide avec les programmes passés des chaînes qui ont une archive",
        "poster": "Affiche", "movie": "Film", "series": "Série", "plot": "Résumé et distribution",
        "play": "Reprendre", "trailer": "Bande-annonce",
        "fscap": "Schéma : les affiches du catalogue et la fiche d'un film avec reprise de lecture",
        "src": "Vos sources", "mine": "Mes vidéos", "folders": "Dossiers, NAS", "servers": "Jellyfin · Emby · Plex",
        "srccap": "Schéma : toutes vos sources dans une seule interface",
    },
    "en": {
        "chan": "Channels", "ready": "Ready in 0.8 s", "health": "Excellent · HD", "delay": "DELAYED −2:34",
        "catch": "Catch up", "live": "Back to live",
        "direct": "Sketch: the player with the channel list, stream health and timeshift",
        "now": "Now", "tonight": "Tonight", "chans": "Channels", "guide": "TV guide",
        "guidecap": "Sketch: the grid guide, with themes above",
        "classic": "Classic", "cinema": "Cinema", "tv": "TV", "side": "Sidebar", "list": "List", "player": "Player",
        "featured": "Featured", "resume": "Resume",
        "ifcap": "Sketch: the three interfaces to choose from, Classic, Cinema and TV",
        "mv": "Sketch: MultiView with four channels, sound on the active tile",
        "sound": "Sound",
        "rec": "Record", "sched": "Scheduled", "queue": "Downloads",
        "reccap": "Sketch: the record button, scheduled recordings and the download queue",
        "pc": "Computer", "tvs": "TV", "casting": "Casting",
        "castcap": "Sketch: from computer to TV, the playback bar stays your remote",
        "replay": "Watch again", "fromstart": "Watch from the start", "past": "Past programmes", "today": "Today",
        "replaycap": "Sketch: the guide with past programmes on channels that have an archive",
        "poster": "Poster", "movie": "Movie", "series": "Series", "plot": "Plot and cast",
        "play": "Resume", "trailer": "Trailer",
        "fscap": "Sketch: catalogue posters and a movie page with resume playback",
        "src": "Your sources", "mine": "My videos", "folders": "Folders, NAS", "servers": "Jellyfin · Emby · Plex",
        "srccap": "Sketch: all your sources in one interface",
    },
}


def direct(t):
    b = R(16, 16, 170, 288) + T(101, 42, t["chan"], "tt", "middle", 15)
    for i in range(6):
        y = 56 + i * 41
        b += R(28, y, 146, 32, "pn2") + C(46, y + 16, 9, "mg" if i == 1 else "pn3")
        b += R(64, y + 9, 70 + (i % 3) * 14, 6, "pn3", 3) + R(64, y + 19, 50, 4, "pn3", 2)
    b += R(200, 16, 424, 288)
    b += R(212, 28, 400, 190, "vid") + PLAY(386, 123, 24)
    b += R(224, 40, 140, 26, "ok", 13) + C(240, 53, 5, "okdot") + T(252, 58, t["health"], "tt", "start", 12)
    b += R(488, 40, 112, 26, "badge", 13) + T(544, 58, t["ready"], "tt", "middle", 12)
    b += R(224, 196, 376, 6, "pn2", 3) + R(224, 196, 250, 6, "ac", 3) + R(470, 190, 4, 18, "warn", 2)
    b += R(212, 232, 150, 28, "warnbg", 14) + T(287, 251, t["delay"], "warntx", "middle", 12)
    b += R(372, 232, 100, 28, "pn2", 14) + T(422, 251, t["catch"], "tt", "middle", 12)
    b += R(482, 232, 130, 28, "ac", 14) + T(547, 251, t["live"], "night", "middle", 12)
    b += R(212, 274, 400, 18, "pn2", 9)
    return wrap(b, t["direct"])


def guide(t):
    b = R(16, 16, 608, 288)
    for i, (k, on) in enumerate([("now", 1), ("tonight", 0), ("chans", 0)]):
        b += R(30 + i * 124, 28, 116, 26, "ac" if on else "pn2", 13) + T(88 + i * 124, 46, t[k], "night" if on else "tt", "middle", 12)
    b += T(610, 46, t["guide"], "tt", "end", 14)
    for j, h in enumerate(["20:00", "20:30", "21:00", "21:30"]):
        b += T(156 + j * 112, 82, h, "tx", "start", 11)
    rows = [[(0, 2), (2, 2)], [(0, 1), (1, 3)], [(0, 3), (3, 1)], [(0, 2), (2, 2)], [(0, 1), (1, 1), (2, 2)]]
    for i, row in enumerate(rows):
        y = 94 + i * 40
        b += R(28, y, 112, 32, "pn2") + C(46, y + 16, 9, "mg" if i == 2 else "pn3") + R(62, y + 13, 60, 6, "pn3", 3)
        for k, (s, w) in enumerate(row):
            hl = i == 1 and k == 1
            b += R(148 + s * 112, y, w * 112 - 6, 32, "ac" if hl else "pn3", 8)
            b += R(158 + s * 112, y + 13, min(w * 112 - 30, 80), 6, "night" if hl else "pn2", 3)
    b += f'<rect class="redline" x="268" y="68" width="2.5" height="226"/>'
    return wrap(b, t["guidecap"])


def interfaces(t):
    b = ""
    xs = [16, 224, 432]
    for x in xs:
        b += R(x, 16, 192, 260)
    # Classique
    b += R(24, 26, 40, 240, "pn2", 6) + R(70, 26, 62, 240, "pn2", 6) + R(138, 26, 62, 240, "pn2", 6)
    b += R(144, 36, 50, 34, "vid", 5) + PLAY(162, 53, 7)
    for i in range(7):
        b += R(76, 38 + i * 30, 50, 22, "pn3", 5)
    for i in range(4):
        b += R(30, 40 + i * 20, 28, 8, "pn3", 4)
    # Cinéma
    b += R(232, 26, 176, 70, "mg", 8) + T(244, 52, t["featured"], "tt", "start", 13) + R(244, 62, 70, 8, "night", 4)
    for r in range(2):
        for i in range(4):
            b += R(232 + i * 45, 108 + r * 76, 40, 62, "pn3", 6)
    b += R(232, 262, 176, 5, "pn3", 3) + R(232, 262, 80, 5, "ac", 3)
    # TV
    b += R(440, 26, 176, 216, "vid", 8) + PLAY(512, 134, 20)
    b += R(450, 36, 44, 30, "pn2", 8) + T(472, 57, "12", "tt", "middle", 17)
    b += R(450, 214, 156, 18, "pn2", 9) + R(450, 214, 90, 18, "ac", 9)
    for x, k in zip(xs, ["classic", "cinema", "tv"]):
        b += T(x + 96, 300, t[k], "tt", "middle", 14)
    return wrap(b, t["ifcap"])


def multivue(t):
    b = R(16, 16, 608, 288)
    pos = [(28, 28), (324, 28), (28, 164), (324, 164)]
    for i, (x, y) in enumerate(pos):
        on = i == 0
        b += R(x, y, 284, 126, "vid", 10)
        if on:
            b += f'<rect class="outl" x="{x}" y="{y}" width="284" height="126" rx="10"/>'
        b += PLAY(x + 142, y + 56, 16, "ac" if on else "pn3")
        b += C(x + 24, y + 24, 14, "ac" if on else "pn3") + T(x + 24, y + 30, str(i + 1), "night" if on else "tt", "middle", 15)
        b += R(x + 12, y + 100, 130, 18, "pn2", 9)
    b += R(196, 38, 94, 24, "badge", 12) + T(243, 54, "♪ " + t["sound"], "tt", "middle", 12)
    return wrap(b, t["mv"])


def enregistrer(t):
    b = R(16, 16, 300, 288) + R(28, 28, 276, 150, "vid") + PLAY(144, 100, 20)
    b += R(28, 190, 276, 6, "pn2", 3) + R(28, 190, 160, 6, "ac", 3)
    b += C(54, 232, 17, "rec") + T(84, 238, t["rec"], "tt", "start", 15) + R(210, 220, 94, 24, "recbg", 12) + T(257, 237, "● REC 0:42", "tt", "middle", 12)
    b += R(28, 262, 276, 28, "pn2", 14)
    b += R(330, 16, 294, 134) + T(346, 42, t["sched"], "tt", "start", 14)
    for i, (n, d) in enumerate([("21:00", 90), ("23:30", 60)]):
        y = 52 + i * 44
        b += R(344, y, 266, 36, "pn2", 8) + C(362, y + 18, 6, "rec") + T(378, y + 23, n, "tt", "start", 13) + R(430, y + 15, d, 6, "pn3", 3)
    b += R(330, 162, 294, 142) + T(346, 188, t["queue"], "tt", "start", 14)
    for i, p in enumerate([0.8, 0.45, 0.1]):
        y = 200 + i * 33
        b += R(344, y, 266, 24, "pn2", 8) + R(344, y, int(266 * p), 24, "ac" if i == 0 else "pn3", 8)
    return wrap(b, t["reccap"])


def cast(t):
    b = R(16, 40, 250, 190) + R(30, 54, 222, 124, "vid", 6) + PLAY(120, 116, 14)
    b += R(30, 190, 222, 8, "pn2", 4) + R(30, 190, 100, 8, "ac", 4) + R(60, 238, 162, 10, "pn2", 5)
    b += T(141, 276, t["pc"], "tt", "middle", 15)
    b += '<path class="arrow" d="M280 134 H356" /><path class="arrowhead" d="M356 120 L380 134 L356 148 Z"/>'
    b += '<path class="wave" d="M286 106 q16 -22 34 0 M296 106 q8 -10 16 0"/>'
    b += R(394, 30, 230, 150, "pn", 10) + R(404, 40, 210, 130, "vid", 6) + PLAY(484, 105, 18)
    b += R(494, 180, 30, 30, "pn2", 4) + R(464, 208, 90, 8, "pn2", 4)
    b += R(414, 142, 190, 18, "ok", 9) + T(509, 155, t["casting"], "tt", "middle", 11)
    b += T(509, 276, t["tvs"], "tt", "middle", 15)
    return wrap(b, t["castcap"])


def replay(t):
    b = R(16, 16, 608, 288)
    b += R(28, 28, 140, 26, "pn2", 13) + T(98, 46, t["today"] + " ▾", "tt", "middle", 12)
    b += T(612, 46, t["past"], "tx", "end", 12)
    rows = [("pn3", 0), ("pn3", 1), ("pn3", 0)]
    for i in range(4):
        y = 70 + i * 46
        b += R(28, y, 116, 36, "pn2") + C(46, y + 18, 9, "mg" if i == 1 else "pn3") + T(124, y + 24, "↺", "ac", "middle", 18)
        for k in range(3):
            hl = i == 1 and k == 1
            b += R(152 + k * 154, y, 148, 36, "ac" if hl else "pn3", 8) + R(162 + k * 154, y + 15, 70, 6, "night" if hl else "pn2", 3)
    b += R(318, 150, 200, 76, "pop", 12) + R(328, 160, 90, 8, "tt", 4) + R(328, 176, 180, 36, "ac", 18) + T(418, 199, t["replay"], "night", "middle", 14)
    b += R(328, 216, 180, 0, "pn2", 0)
    b += R(28, 258, 200, 28, "pn2", 14) + T(128, 277, t["fromstart"], "tt", "middle", 12)
    return wrap(b, t["replaycap"])


def films(t):
    b = R(16, 16, 330, 288) + T(32, 42, t["movie"] + " · " + t["series"], "tt", "start", 14)
    for r in range(2):
        for i in range(4):
            on = (r, i) == (0, 1)
            x, y = 30 + i * 78, 54 + r * 120
            b += R(x, y, 70, 108, "mg" if on else "pn3", 8)
            if i == 2 and r == 0:
                b += R(x, y + 100, 46, 8, "ac", 4)
    b += R(360, 16, 264, 288) + R(372, 28, 240, 90, "vid", 8) + R(384, 80, 56, 76, "mg", 8)
    b += T(452, 134, "★ 8,1 · 2h08", "tt", "start", 13) + R(452, 144, 150, 7, "pn3", 4)
    b += R(372, 176, 240, 7, "pn3", 4) + R(372, 192, 200, 7, "pn3", 4) + R(372, 208, 220, 7, "pn3", 4)
    b += R(372, 228, 240, 8, "pn2", 4) + R(372, 228, 130, 8, "ac", 4)
    b += R(372, 252, 110, 34, "ac", 17) + T(427, 274, "▶ " + t["play"], "night", "middle", 13) + R(492, 252, 120, 34, "pn2", 17) + T(552, 274, t["trailer"], "tt", "middle", 13)
    return wrap(b, t["fscap"])


def sources(t):
    b = ""
    cx, cy = 320, 160
    items = [(110, 56, "Xtream Codes"), (110, 160, "M3U"), (110, 264, t["folders"]),
             (530, 56, t["servers"]), (530, 160, "YouTube"), (530, 264, t["mine"])]
    for x, y, s in items:
        b += f'<path class="link" d="M{cx} {cy} L{x} {y}"/>'
    b += R(cx - 72, cy - 44, 144, 88, "mg", 16) + T(cx, cy + 6, "Kastideo", "tt", "middle", 22)
    for x, y, s in items:
        b += R(x - 86, y - 24, 172, 48, "solid", 12) + T(x, y + 6, s, "tt", "middle", 14)
    return wrap(b, t["srccap"])


BUILDERS = {
    "direct": direct, "guide-tv": guide, "interfaces": interfaces, "multivue": multivue,
    "enregistrer": enregistrer, "cast": cast, "replay": replay, "films-series": films, "sources": sources,
}


def svg(slug, lang):
    f = BUILDERS.get(slug)
    return f(TXT[lang]) if f else None
