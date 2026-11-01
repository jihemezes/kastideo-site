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
