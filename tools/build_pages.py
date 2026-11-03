#!/usr/bin/env python3
"""Génère le site statique (FR à la racine, EN sous /en/) dans public/.

Usage : python3 tools/build_pages.py   (depuis la racine du dépôt)

Sources :
  - tools/src/index.body.html : corps de l'accueil, bilingue (attributs data-fr / data-en) ;
  - tools/pages_*.py : textes FR et EN des autres pages ;
  - tools/seo.py : titres et descriptions de référencement.
Chaque langue a ses propres pages (adresses séparées, balises hreflang). Cloudflare sert
les pages sans « .html » : les adresses canoniques sont donc /direct et /en/direct.
Ne modifiez pas à la main les .html générés : relancez ce script.
"""
import html as htmllib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

from pages_features import FEATURES  # noqa: E402
from pages_versions import VERSIONS  # noqa: E402
from pages_other import OTHER, kofi_button  # noqa: E402
from pages_seo import COMPARE  # noqa: E402
from pages_guides import GUIDES, NEWS  # noqa: E402
from seo import META  # noqa: E402
import pages_legal as L  # noqa: E402
import illustrations  # noqa: E402

PUB = os.path.join(ROOT, "public")
SITE = "https://kastideo.com"
LASTMOD = "2026-11-01"
LANGS = ("fr", "en")

LEGAL = [
    {"slug": "confidentialite", "title_fr": "Politique de confidentialité", "title_en": "Privacy policy",
     "fr": L.PRIV_FR, "en": L.PRIV_EN},
    {"slug": "mentions-legales", "title_fr": "Mentions légales", "title_en": "Legal notice",
     "fr": L.LEGAL_FR, "en": L.LEGAL_EN},
]

ARIA_EN = {
    "Remonter en haut de la page": "Back to top of the page",
    "Fil d'Ariane": "Breadcrumb",
    "Navigation principale": "Main navigation",
    "Plan du site": "Site map",
    "Icône de Kastideo": "Kastideo icon",
    "Quel fichier télécharger": "Which file to download",
    "Accès principaux": "Main access",
    "Logo TMDB": "TMDB logo",
    "Changer de langue": "Change language",
    "Comparaison": "Comparison",
}


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def bi(fr, en, tag="span", extra=""):
    """Élément bilingue source (data-fr / data-en), résolu par localize()."""
    return f'<{tag}{extra} data-fr="{esc(fr)}" data-en="{esc(en)}">{fr}</{tag}>'


# --------------------------------------------------------------------------- adresses
def url_path(slug, lang):
    """Adresse canonique sans domaine."""
    if slug == "index":
        return "/" if lang == "fr" else "/en/"
    return f"/{slug}" if lang == "fr" else f"/en/{slug}"


def url_abs(slug, lang):
    return SITE + url_path(slug, lang)


# --------------------------------------------------------------------------- langue
BI = re.compile(
    r'<(?P<tag>[a-z0-9]+)(?P<a>[^<>]*?)\sdata-fr="(?P<fr>[^"]*)"\sdata-en="(?P<en>[^"]*)"(?P<b>[^<>]*)>(?P<inner>.*?)</(?P=tag)>',
    re.S,
)
HREF = re.compile(r'(?P<attr>href|src)="(?P<v>[^"]*)"')


def _fix_link(attr, v, lang):
    if re.match(r"^(https?:|mailto:|#|/|data:)", v):
        return v
    m = re.match(r"^([a-z0-9-]+)\.html(#.*)?$", v)
    if m:
        slug, frag = m.group(1), m.group(2) or ""
        return url_path(slug, lang) + frag
    if re.search(r"\.(css|js|png|webp|jpg|svg|woff2|xml|txt)$", v):
        return "/" + v
    return v


def localize(doc, lang):
    """Résout les éléments bilingues, les libellés ARIA et les adresses pour une langue."""
    def rep(m):
        txt = htmllib.unescape(m.group(lang))
        return f'<{m.group("tag")}{m.group("a")}{m.group("b")}>{txt}</{m.group("tag")}>'
    doc = BI.sub(rep, doc)
    if lang == "en":
        def aria(m):
            return f'{m.group(1)}="{ARIA_EN.get(htmllib.unescape(m.group(2)), m.group(2))}"'
        doc = re.sub(r'(aria-label|alt)="([^"]*)"', aria, doc)
    doc = HREF.sub(lambda m: f'{m.group("attr")}="{_fix_link(m.group("attr"), m.group("v"), lang)}"', doc)
    return doc


# --------------------------------------------------------------------------- JSON-LD
def jsonld(slug, lang, title, desc, crumbs_list):
    url = url_abs(slug, lang)
    data = []
    if slug == "index":
        data.append({"@type": "WebSite", "@id": SITE + "/#site", "url": url_abs("index", lang), "name": "Kastideo",
                     "inLanguage": lang})
        data.append({
            "@type": "SoftwareApplication", "name": "Kastideo",
            "applicationCategory": "MultimediaApplication",
            "operatingSystem": "macOS, Windows, Linux, Android",
            "description": desc, "url": url, "image": SITE + "/icon-512.png",
            "inLanguage": lang,
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
            "downloadUrl": url_abs("telecharger", lang),
        })
    else:
        data.append({"@type": "WebPage", "@id": url + "#page", "url": url, "name": title, "description": desc,
                     "inLanguage": lang, "isPartOf": {"@id": SITE + "/#site"}})
        if crumbs_list:
            items = []
            for i, (name, path) in enumerate(crumbs_list, 1):
                it = {"@type": "ListItem", "position": i, "name": name}
                if path:
                    it["item"] = SITE + path
                items.append(it)
            data.append({"@type": "BreadcrumbList", "itemListElement": items})
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": data},
                                                                 ensure_ascii=False, separators=(",", ":")) + "</script>\n"


# --------------------------------------------------------------------------- éléments communs
def head(slug, lang):
    t, d = META[slug][lang]
    full = t if slug == "index" else f"{t} | Kastideo"
    other = "en" if lang == "fr" else "fr"
    img = f"{SITE}/og-{lang}.jpg"
    alt = ("Kastideo, lecteur IPTV pour Mac, Windows, Linux et Android" if lang == "fr"
           else "Kastideo, IPTV player for Mac, Windows, Linux and Android")
    loc, loc2 = ("fr_FR", "en_US") if lang == "fr" else ("en_US", "fr_FR")
    return t, d, f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(full)}</title>
<meta name="description" content="{esc(d)}">
<meta name="theme-color" content="#0F0524">
<link rel="canonical" href="{url_abs(slug, lang)}">
<link rel="alternate" hreflang="fr" href="{url_abs(slug, 'fr')}">
<link rel="alternate" hreflang="en" href="{url_abs(slug, 'en')}">
<link rel="alternate" hreflang="x-default" href="{url_abs(slug, 'fr')}">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/icon-192.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kastideo">
<meta property="og:locale" content="{loc}">
<meta property="og:locale:alternate" content="{loc2}">
<meta property="og:url" content="{url_abs(slug, lang)}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(d)}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(full)}">
<meta name="twitter:description" content="{esc(d)}">
<meta name="twitter:image" content="{img}">
<link rel="preload" href="/fonts/nunito-latin-900.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/site.css">
</head>
"""


def lang_link(slug, lang):
    if lang == "fr":
        return f'<a class="lang" id="lang" href="{url_path(slug, "en")}" hreflang="en" lang="en" aria-label="Changer de langue : English">English</a>'
    return f'<a class="lang" id="lang" href="{url_path(slug, "fr")}" hreflang="fr" lang="fr" aria-label="Change language: Français">Français</a>'


def header(slug):
    return f"""<body>
<a class="skip" href="#contenu" data-fr="Aller au contenu" data-en="Skip to content">Aller au contenu</a>
<div class="backdrop" aria-hidden="true">
  <img src="backdrop.webp" alt="" width="256" height="256">
</div>

<div class="wrap">
  <header class="top" id="haut">
    <a class="brand" href="index.html">
      <img src="icon-112.png" alt="Icône de Kastideo" width="56" height="56">
      <div>
        <strong>Kastideo</strong>
        {bi("Vos chaînes, vos films et vos séries au même endroit", "Your channels, films and series in one place")}
      </div>
    </a>
    <nav class="main" aria-label="Navigation principale">
      {bi("Fonctions", "Features", "a", ' href="index.html#fonctions"')}
      {bi("Versions", "Versions", "a", ' href="index.html#versions"')}
      {bi("Télécharger", "Download", "a", ' href="telecharger.html"')}
      {bi("Nouveautés", "What's new", "a", ' href="nouveautes.html"')}
      {bi("FAQ", "FAQ", "a", ' href="faq.html"')}
      {kofi_button("Offrir un café", False, "Buy me a coffee")}
      @@LANG@@
    </nav>
  </header>
"""


def crumb_data(group, p):
    """Liste (nom FR, nom EN, chemin) du fil d'Ariane."""
    items = [("Accueil", "Home", "index")]
    if group == "features":
        items.append(("Fonctions", "Features", "index#fonctions"))
    elif group == "versions":
        items.append(("Versions", "Versions", "index#versions"))
    items.append((p["title_fr"], p["title_en"], None))
    return items


def crumbs_html(items):
    parts = []
    for fr, en, target in items:
        if target:
            slug, _, frag = target.partition("#")
            href = "index.html" + ("#" + frag if frag else "") if slug == "index" else slug + ".html"
            parts.append(bi(fr, en, "a", f' href="{href}"'))
        else:
            parts.append(bi(fr, en, "span", ' aria-current="page"'))
    return '  <nav class="crumbs" aria-label="Fil d\'Ariane">' + ' <span aria-hidden="true">›</span> '.join(parts) + "</nav>\n"


def related(pages, me):
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
        + col("Guides", "Guides", GUIDES) + "\n"
        + col("Comparer", "Compare", COMPARE) + "\n"
        + col("Projet", "Project", [NEWS, OTHER[1]] + LEGAL) + "\n"
        "    </nav>"
    )


TO_TOP = (
    '  <a class="to-top" href="#haut" aria-label="Remonter en haut de la page" hidden>'
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></a>\n'
)


# Captures réelles de l'application (démo : playlist publique), interface en français.
SHOTS = {
    "index": ("app-home", 1600, 956,
              "Accueil de Kastideo : Direct, Films, Séries, Mes vidéos, Guide TV, YouTube et Enregistrements",
              "Kastideo home screen: Live, Movies, Series, My videos, TV guide, YouTube and Recordings",
              "L'accueil de Kastideo.", "The Kastideo home screen."),
    "direct": ("app-direct", 1600, 1017,
               "Interface Classique de Kastideo : liste des chaînes, lecteur et catégories",
               "Kastideo Classic interface: channel list, player and categories",
               "L'interface Classique : catégories, chaînes et lecteur.", "The Classic interface: categories, channels and player."),
    "guide-tv": ("app-guide-tv", 1600, 957,
                 "Guide TV de Kastideo en grille sur 6 heures",
                 "Kastideo grid TV guide over 6 hours",
                 "Le guide TV en grille, ici sur 6 heures.", "The grid TV guide, here over 6 hours."),
    "interfaces": ("app-interfaces", 900, 848,
                   "Réglages d'apparence : couleur d'accent et choix de l'interface Classique, Cinéma ou TV",
                   "Appearance settings: accent colour and choice of Classic, Cinema or TV interface",
                   "Réglages > Apparence : une interface par type de contenu.", "Settings > Appearance: one interface per content type."),
    "films-series": ("app-films", 1600, 1028,
                     "Mes vidéos dans Kastideo : grille d'affiches de films avec filtres par genre et par année",
                     "My videos in Kastideo: grid of movie posters with genre and year filters",
                     "Mes vidéos : affiches, filtres et fiches corrigées, ici avec des courts-métrages libres de la fondation Blender.",
                     "My videos: posters, filters and corrected pages, here with free short films from the Blender Foundation."),
    "guide-m3u-mac": ("app-welcome", 1400, 834,
                      "Écran de bienvenue de Kastideo avec le bouton Ajouter une source",
                      "Kastideo welcome screen with the Add a source button",
                      "Au premier lancement : Ajouter une source.", "At first launch: Add a source."),
}


def real_figure(slug, lang, lazy=True):
    if slug not in SHOTS:
        return None
    f, w, h, afr, aen, cfr, cen = SHOTS[slug]
    alt, cap = (afr, cfr) if lang == "fr" else (aen, cen)
    if lang == "en":
        cap += " Screenshot of the French interface."
    return (f'<figure class="app-shot"><img src="/img/{f}.webp" width="{w}" height="{h}" alt="{esc(alt)}"'
            f'{" loading=" + chr(34) + "lazy" + chr(34) + " decoding=" + chr(34) + "async" + chr(34) if lazy else ""}>'
            f'<figcaption>{cap}</figcaption></figure>')


def with_figure(p, lang):
    html = p[lang]
    fig = real_figure(p["slug"], lang) or illustrations.svg(p["slug"], lang)
    if not fig:
        return html
    m = re.search(r'<p class="page-lead">.*?</p>\n', html, flags=re.S)
    return html[:m.end()] + "    " + fig + "\n" + html[m.end():]


def index_source():
    src = open(os.path.join(ROOT, "tools", "src", "index.body.html"), encoding="utf-8").read()
    return re.sub(r"<!--sitemap-->.*?<!--/sitemap-->", lambda m: sitemap_block(), src, flags=re.S)


def footer_of(idx):
    m = re.search(r"  <footer>.*?</footer>", idx, flags=re.S)
    if not m:
        raise SystemExit("index.body.html : pied de page introuvable")
    return m.group(0) + "\n"


def subpage(p, group, siblings, footer, lang):
    slug = p["slug"]
    title, desc, h = head(slug, lang)
    items = crumb_data(group, p)
    crumbs_ld = []
    for fr, en, target in items:
        name = fr if lang == "fr" else en
        if target:
            s, _, frag = target.partition("#")
            crumbs_ld.append((name, url_path(s, lang) + ("#" + frag if frag else "")))
        else:
            crumbs_ld.append((name, None))
    out = h + header(slug).replace("@@LANG@@", lang_link(slug, lang))
    out += crumbs_html(items)
    out += f'\n  <main class="doc" id="contenu">\n{with_figure(p, lang)}  </main>\n\n'
    if siblings:
        out += related(siblings, slug)
    if group in ("features", "versions", "compare", "guides"):
        out += cta()
    out += footer + TO_TOP + "</div>\n"
    out += jsonld(slug, lang, title, desc, crumbs_ld)
    out += '<script src="site.js"></script>\n</body>\n</html>\n'
    return localize(out, lang)


def index_page(idx, lang):
    title, desc, h = head("index", lang)
    body = re.sub(r'<button class="lang"[^>]*>[^<]*</button>', lang_link("index", lang), idx)
    body = body.replace("<!--shot:index-->", real_figure("index", lang))
    body = re.sub(r'<script src="site.js"></script>\n?', "", body)
    out = h + "<body>\n<a class=\"skip\" href=\"#contenu\" data-fr=\"Aller au contenu\" data-en=\"Skip to content\">Aller au contenu</a>\n" + body
    out += jsonld("index", lang, title, desc, None)
    out += '<script src="site.js"></script>\n</body>\n</html>\n'
    return localize(out, lang)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)


NEWS_L = [NEWS]


def main():
    idx = index_source()
    footer = footer_of(idx)
    pages = []  # (slug)
    for lang in LANGS:
        base = PUB if lang == "fr" else os.path.join(PUB, "en")
        write(os.path.join(base, "index.html"), index_page(idx, lang))
        for plist, group in ((FEATURES, "features"), (VERSIONS, "versions"), (COMPARE, "compare"), (GUIDES, "guides"), (NEWS_L, "news"),
                             (OTHER, "other"), (LEGAL, "legal")):
            for p in plist:
                write(os.path.join(base, p["slug"] + ".html"),
                      subpage(p, group, plist if group in ("features", "versions", "compare", "guides") else None, footer, lang))
    slugs = ["index"] + [p["slug"] for pl in (FEATURES, VERSIONS, COMPARE, GUIDES, NEWS_L, OTHER, LEGAL) for p in pl]

    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for s in slugs:
        for lang in LANGS:
            sm.append("  <url>")
            sm.append(f"    <loc>{url_abs(s, lang)}</loc>")
            sm.append(f"    <lastmod>{LASTMOD}</lastmod>")
            for l2 in LANGS:
                sm.append(f'    <xhtml:link rel="alternate" hreflang="{l2}" href="{url_abs(s, l2)}"/>')
            sm.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url_abs(s, "fr")}"/>')
            sm.append("  </url>")
    sm.append("</urlset>")
    write(os.path.join(PUB, "sitemap.xml"), "\n".join(sm) + "\n")

    write(os.path.join(PUB, "robots.txt"), f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("Pages générées :", len(slugs) * 2)


if __name__ == "__main__":
    main()
