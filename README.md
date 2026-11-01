# kastideo-site

Site statique de Kastideo (kastideo.com). Aucune étape de compilation.

## Contenu

- `public/` : le site publié.
  - `index.html` (accueil), `confidentialite.html`, `mentions-legales.html`
  - `site.css`, `site.js` : styles et script partagés (bascule français / anglais, bouton Copier)
  - `fonts/` : polices Nunito et Inter, hébergées sur le site (licence OFL), aucune requête vers Google
  - `TMDB-blue_square_1.svg` : logo TMDB (mention obligatoire)
  - `_headers` : en-têtes de sécurité et cache (Cloudflare)
- `wrangler.jsonc` : configuration Cloudflare (le dossier `public/` est servi tel quel).

## Branches

- `main` : production (kastideo.com).
- Autres branches : aperçus Cloudflare, protégés par Cloudflare Access.

## Statistiques

Cloudflare Web Analytics (gratuit, sans cookie). Si l'activation automatique de Cloudflare n'est pas utilisée, renseigner `ANALYTICS_TOKEN` en haut de `public/site.js`.

## Téléchargements

Les boutons pointent vers la page des versions de github.com/jihemezes/kastideo : `releases/latest` pour le Mac, `releases` pour Windows, Linux et Android.

## Pages générées (français à la racine, anglais sous /en/)

Toutes les pages HTML sont **générées** par `python3 tools/build_pages.py` : une page par langue, avec balises `hreflang`, adresses canoniques, Open Graph, données structurées JSON-LD et `sitemap.xml`.
Ne modifiez pas les `.html` de `public/` à la main. Les sources sont :

- `tools/src/index.body.html` : corps de l'accueil, bilingue (attributs `data-fr` / `data-en`) ;
- `tools/pages_features.py`, `pages_versions.py`, `pages_other.py`, `pages_seo.py`, `pages_legal.py` : textes FR et EN des autres pages ;
- `tools/seo.py` : titre et description de référencement de chaque page, dans les deux langues ;
- `tools/illustrations.py` : schémas SVG des pages de fonctions.

Les images de partage `public/og-fr.png` et `og-en.png` se régénèrent avec `python3 tools/make_og.py` (Playwright).
Cloudflare sert les pages sans `.html` (`/direct`, `/en/direct`) : les adresses canoniques et le plan du site utilisent ces formes.

## Liens de téléchargement

`public/site.js` interroge l'API GitHub (`/repos/jihemezes/kastideo/releases`) pour retrouver, par famille (Mac `vX.Y.Z`, Windows et Linux `-desktopN`, Android `-androidN`), la dernière version et le fichier correspondant. En cas d'échec, les liens statiques vers la page des versions restent actifs. Le domaine `api.github.com` est autorisé dans `public/_headers` (`connect-src`).
