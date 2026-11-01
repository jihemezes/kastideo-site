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

## Pages générées

Les pages de détail (`direct.html`, `guide-tv.html`, `mac.html`, `telecharger.html`, etc.), les pages légales et `sitemap.xml`
sont **générées** par `python3 tools/build_pages.py` à partir des textes de `tools/pages_*.py`.
Ne les modifiez pas à la main : changez le texte dans `tools/`, relancez le script, puis committez le résultat.
`public/index.html` reste écrit à la main ; le script n'y régénère que le plan du site (entre `<!--sitemap-->` et `<!--/sitemap-->`) et s'en sert pour le pied de page commun.

## Liens de téléchargement

`public/site.js` interroge l'API GitHub (`/repos/jihemezes/kastideo/releases`) pour retrouver, par famille (Mac `vX.Y.Z`, Windows et Linux `-desktopN`, Android `-androidN`), la dernière version et le fichier correspondant. En cas d'échec, les liens statiques vers la page des versions restent actifs. Le domaine `api.github.com` est autorisé dans `public/_headers` (`connect-src`).
