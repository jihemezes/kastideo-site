#!/usr/bin/env python3
"""Génère les pages secondaires de kastideo.com dans public/.

Usage : python3 tools/build_pages.py   (depuis la racine du dépôt)

Source unique :
  - public/index.html (écrit à la main) fournit le pied de page commun ;
    le bloc entre <!--sitemap--> et <!--/sitemap--> y est régénéré ici.
  - tools/pages_*.py contiennent les textes FR/EN des pages générées.
Ne modifiez pas à la main les pages générées : relancez ce script.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

from pages_features import FEATURES  # noqa: E402
from pages_versions import VERSIONS  # noqa: E402
from pages_other import OTHER, kofi_button  # noqa: E402
import pages_legal as L  # noqa: E402
import illustrations  # noqa: E402

PUB = os.path.join(ROOT, "public")
SITE = "https://kastideo.com"
TODAY = "2026-11-01"

LEGAL = [
    {"slug": "confidentialite", "title_fr": "Politique de confidentialité", "title_en": "Privacy policy",
     "desc": "Données traitées par le site et par l'application Kastideo, et vos droits.",
     "fr": L.PRIV_FR, "en": L.PRIV_EN},
    {"slug": "mentions-legales", "title_fr": "Mentions légales", "title_en": "Legal notice",
     "desc": "Éditeur, hébergeur, avertissement et crédits de Kastideo.",
     "fr": L.LEGAL_FR, "en": L.LEGAL_EN},
]


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def bi(fr, en, tag="span", extra=""):
    """Élément bilingue (data-fr / data-en), contenu FR par défaut."""
    return f'<{tag}{extra} data-fr="{esc(fr)}" data-en="{esc(en)}">{fr}</{tag}>'


def head(title_fr, title_en, desc, slug):
    url = f"{SITE}/{slug}.html"
    t = f"{title_fr}, Kastideo"
    return f"""<!doctype html>
<html lang="fr" data-title-fr="{esc(t)}" data-title-en="{esc(title_en + ', Kastideo')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#0F0524">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="icon-192.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(t)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE}/icon-512.png">
<link rel="preload" href="fonts/nunito-latin-900.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="site.css">
</head>
"""


def header():
    return f"""<body>
<div class="backdrop" aria-hidden="true">
  <img src="icon-512.png" alt="" width="512" height="512">
</div>

<div class="wrap">
  <header class="top" id="haut">
    <a class="brand" href="index.html">
      <img src="icon-192.png" alt="Icône de Kastideo" width="56" height="56">
      <div>
        <strong>Kastideo</strong>
        {bi("Vos chaînes, vos films et vos séries au même endroit", "Your channels, films and series in one place")}
      </div>
    </a>
    <nav class="main" aria-label="Navigation principale">
      {bi("Fonctions", "Features", "a", ' href="index.html#fonctions"')}
      {bi("Versions", "Versions", "a", ' href="index.html#versions"')}
      {bi("Télécharger", "Download", "a", ' href="telecharger.html"')}
      {kofi_button("Offrir un café", False, "Buy me a coffee")}
      <button class="lang" id="lang" type="button" aria-label="Changer de langue">English</button>
    </nav>
  </header>
"""


def crumbs(group, cur_fr, cur_en):
    if group == "features":
        mid = bi("Fonctions", "Features", "a", ' href="index.html#fonctions"')
    elif group == "versions":
        mid = bi("Versions", "Versions", "a", ' href="index.html#versions"')
    else:
        mid = None
    parts = [bi("Accueil", "Home", "a", ' href="index.html"')]
    if mid:
        parts.append(mid)
    parts.append(bi(cur_fr, cur_en, "span", ' aria-current="page"'))
    return '  <nav class="crumbs" aria-label="Fil d\'Ariane">' + ' <span aria-hidden="true">›</span> '.join(parts) + "</nav>\n"


def related(pages, me):
    """Trois pages voisines dans le même groupe (suivantes, en boucle)."""
    i = [p["slug"] for p in pages].index(me)
    pick = [pages[(i + k) % len(pages)] for k in (1, 2, 3)]
    pick = [p for p in pick if p["slug"] != me][:3]
    cards = []
    for p in pick:
        cards.append(
            f'      <a class="card link" href="{p["slug"]}.html">\n'
            f'        {bi(p["title_fr"], p["title_en"], "h3")}\n'
            f'        {bi(p["blurb_fr"], p["blurb_en"], "p")}\n'
            f'      </a>'
        )
    return (
        '  <section class="related" aria-labelledby="t-related">\n'
        f'    {bi("Voir aussi", "See also", "h2", " id=" + chr(34) + "t-related" + chr(34) + " class=" + chr(34) + "sec" + chr(34))}\n'
        '    <div class="cards">\n' + "\n".join(cards) + "\n    </div>\n  </section>\n"
    )


def cta():
    return (
        '  <aside class="cta-band" aria-label="Télécharger">\n'
        f'    <div>{bi("Prêt à essayer ?", "Ready to try?", "strong")}'
        f'{bi("Kastideo est gratuit et sans compte.", "Kastideo is free and needs no account.", "span")}</div>\n'
        f'    <div class="actions">{bi("Télécharger Kastideo", "Download Kastideo", "a", " class=" + chr(34) + "btn primary" + chr(34) + " href=" + chr(34) + "telecharger.html" + chr(34))}'
        f'{bi("Soutenir le projet", "Support the project", "a", " class=" + chr(34) + "btn ghost" + chr(34) + " href=" + chr(34) + "soutenir.html" + chr(34))}</div>\n'
        "  </aside>\n"
    )


def sitemap_block():
    def col(title_fr, title_en, items):
        li = "\n".join(
            f'        <li><a href="{p["slug"]}.html" data-fr="{esc(p["title_fr"])}" data-en="{esc(p["title_en"])}">{p["title_fr"]}</a></li>'
            for p in items
        )
        return (
            f'      <div><p class="small-title" data-fr="{esc(title_fr)}" data-en="{esc(title_en)}">{title_fr}</p>\n'
            f"      <ul>\n{li}\n      </ul></div>"
        )
    return (
        '<nav class="sitemap" aria-label="Plan du site">\n'
        + col("Fonctions", "Features", FEATURES) + "\n"
        + col("Versions", "Versions", VERSIONS + [OTHER[0]]) + "\n"
        + col("Projet", "Project", [OTHER[1]] + LEGAL) + "\n"
        "    </nav>"
    )


def update_index_sitemap(idx):
    new = "<!--sitemap-->" + sitemap_block() + "<!--/sitemap-->"
    if "<!--sitemap-->" in idx:
        return re.sub(r"<!--sitemap-->.*?<!--/sitemap-->", lambda m: new, idx, flags=re.S)
    raise SystemExit("index.html : marqueur <!--sitemap--> manquant")


def footer_from_index(idx):
    m = re.search(r"  <footer>.*?</footer>", idx, flags=re.S)
    if not m:
        raise SystemExit("index.html : pied de page introuvable")
    f = m.group(0)
    # Sur les pages secondaires les liens internes de la page d'accueil restent valables.
    return f + "\n"


TO_TOP = (
    '  <a class="to-top" href="#haut" aria-label="Remonter en haut de la page" hidden>'
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></a>\n'
)


def with_figure(p, lang):
    """Insère le schéma de la page (s'il existe) juste après le paragraphe d'introduction."""
    html = p[lang]
    fig = illustrations.svg(p["slug"], lang)
    if not fig:
        return html
    m = re.search(r'<p class="page-lead">.*?</p>\n', html, flags=re.S)
    return html[:m.end()] + "    " + fig + "\n" + html[m.end():]


def page(p, group, siblings, footer):
    p = dict(p, fr=with_figure(p, "fr"), en=with_figure(p, "en"))
    out = head(p["title_fr"], p["title_en"], p["desc"], p["slug"])
    out += header()
    out += crumbs(group, p["title_fr"], p["title_en"])
    out += f'\n  <main class="doc" data-lang="fr">\n{p["fr"]}  </main>\n'
    out += f'  <main class="doc" data-lang="en" hidden>\n{p["en"]}  </main>\n\n'
    if siblings:
        out += related(siblings, p["slug"])
    if group in ("features", "versions"):
        out += cta()
    out += footer
    out += TO_TOP
    out += '</div>\n<script src="site.js"></script>\n</body>\n</html>\n'
    return out


def main():
    idx_path = os.path.join(PUB, "index.html")
    idx = update_index_sitemap(open(idx_path, encoding="utf-8").read())
    open(idx_path, "w", encoding="utf-8").write(idx)
    footer = footer_from_index(idx)

    written = []

    def w(slug, html):
        open(os.path.join(PUB, slug + ".html"), "w", encoding="utf-8").write(html)
        written.append(slug)

    for p in FEATURES:
        w(p["slug"], page(p, "features", FEATURES, footer))
    for p in VERSIONS:
        w(p["slug"], page(p, "versions", VERSIONS, footer))
    for p in OTHER:
        w(p["slug"], page(p, "other", None, footer))
    for p in LEGAL:
        w(p["slug"], page(p, "legal", None, footer))

    urls = [""] + [s + ".html" for s in written]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod></url>")
    sm.append("</urlset>")
    open(os.path.join(PUB, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")

    rb = os.path.join(PUB, "robots.txt")
    txt = open(rb).read()
    if "Sitemap:" not in txt:
        open(rb, "w").write(txt.rstrip("\n") + f"\nSitemap: {SITE}/sitemap.xml\n")
    print("Pages générées :", len(written))


if __name__ == "__main__":
    main()
