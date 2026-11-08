// Adresses courtes de téléchargement : /tv, /tv64, /tv32 et /dl/*.
// Le Worker ne sert que ces chemins (voir run_worker_first dans wrangler.jsonc) ;
// tout le reste est servi directement par les fichiers statiques de public/.
// Il lit les releases GitHub et redirige vers le fichier de la dernière version.

const REPO = 'jihemezes/kastideo';
const API = 'https://api.github.com/repos/' + REPO + '/releases?per_page=50';

// chemin -> [famille de version, motif du nom de fichier, page de repli]
const ROUTES = {
  '/tv':             ['android', /android-universal\.apk$/,        '/android'],
  '/tv64':           ['android', /android-arm64-v8a\.apk$/,        '/android'],
  '/tv32':           ['android', /android-armeabi-v7a\.apk$/,      '/android'],
  '/dl/mac':         ['mac',     /^Kastideo-[\d.]+\.dmg$/,         '/mac'],
  '/dl/windows':     ['desktop', /windows-x64-setup\.exe$/,        '/windows'],
  '/dl/windows-zip': ['desktop', /windows-x64\.zip$/,              '/windows'],
  '/dl/linux':       ['desktop', /linux-x86_64\.AppImage$/,        '/linux'],
  '/dl/linux-arm':   ['desktop', /linux-aarch64\.AppImage$/,       '/linux'],
  '/dl/deb':         ['desktop', /ubuntu24\.04_amd64\.deb$/,       '/linux'],
  '/dl/deb22':       ['desktop', /ubuntu22\.04_amd64\.deb$/,       '/linux'],
};

// Même règle que public/site.js : la famille se lit dans l'étiquette de la release.
function family(tag) {
  if (/-desktop\d*$/.test(tag)) return 'desktop';
  if (/-android\d*$/.test(tag)) return 'android';
  if (/^v\d+\.\d+\.\d+$/.test(tag)) return 'mac';
  return null;
}

export function findAsset(releases, fam, re) {
  for (const r of releases) {                 // l'API liste du plus récent au plus ancien
    if (r.draft || family(r.tag_name) !== fam) continue;
    const a = (r.assets || []).find((x) => re.test(x.name));
    if (a) return a.browser_download_url;
  }
  return null;
}

function redirect(url, status) {
  return new Response(null, { status, headers: { Location: url, 'Cache-Control': 'no-store' } });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+$/, '') || '/';
    const route = ROUTES[path.toLowerCase()];
    if (!route) return env.ASSETS.fetch(request);

    let target = null;
    try {
      const res = await fetch(API, {
        headers: { 'User-Agent': 'kastideo-site', Accept: 'application/vnd.github+json' },
        cf: { cacheTtl: 300, cacheEverything: true },
      });
      if (res.ok) target = findAsset(await res.json(), route[0], route[1]);
    } catch (e) { /* repli ci-dessous */ }

    // Si GitHub ne répond pas : la page de téléchargement du site, qui sait réessayer.
    return target ? redirect(target, 302) : redirect(url.origin + route[2], 302);
  },
};
