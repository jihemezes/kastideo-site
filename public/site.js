(function () {
  // Statistiques : Cloudflare Web Analytics (gratuit, sans cookie).
  // Si l'activation automatique de Cloudflare n'est pas utilisée, collez ici le jeton du site
  // (Cloudflare > Web Analytics > le site > « Manage site » > jeton de la balise JavaScript).
  var ANALYTICS_TOKEN = '';
  if (ANALYTICS_TOKEN) {
    var s = document.createElement('script');
    s.defer = true;
    s.src = 'https://static.cloudflareinsights.com/beacon.min.js';
    s.setAttribute('data-cf-beacon', JSON.stringify({ token: ANALYTICS_TOKEN }));
    document.head.appendChild(s);
  }

  var lang = 'fr';
  try { lang = localStorage.getItem('kastideo.lang') === 'en' ? 'en' : 'fr'; } catch (e) {}

  // ---------- Langue ----------
  function apply(l) {
    lang = l;
    document.documentElement.lang = l;
    document.querySelectorAll('[data-' + l + ']').forEach(function (el) {
      el.innerHTML = el.getAttribute('data-' + l);
    });
    document.querySelectorAll('[data-lang]').forEach(function (el) {
      el.hidden = el.getAttribute('data-lang') !== l;
    });
    var btn = document.getElementById('lang');
    if (btn) btn.textContent = l === 'fr' ? 'English' : 'Français';
    var t = document.documentElement.getAttribute('data-title-' + l);
    if (t) document.title = t;
    var toTop = document.querySelector('.to-top');
    if (toTop) toTop.setAttribute('aria-label', l === 'fr' ? 'Remonter en haut de la page' : 'Back to top of the page');
    renderReleases();
    try { localStorage.setItem('kastideo.lang', l); } catch (e) {}
  }
  var langBtn = document.getElementById('lang');
  if (langBtn) langBtn.addEventListener('click', function () { apply(lang === 'fr' ? 'en' : 'fr'); });

  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var text = btn.getAttribute('data-copy');
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () {
          btn.textContent = lang === 'en' ? 'Copied' : 'Copié';
        }, function () {});
      }
    });
  });

  // ---------- Retour en haut ----------
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var toTopBtn = document.querySelector('.to-top');
  function onScroll() {
    if (toTopBtn) toTopBtn.hidden = (window.pageYOffset || document.documentElement.scrollTop) < 500;
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  document.querySelectorAll('.to-top, .top-link').forEach(function (a) {
    a.addEventListener('click', function (ev) {
      ev.preventDefault();
      window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
      var h = document.getElementById('haut');
      if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
    });
  });

  // ---------- Dernières versions (API GitHub) ----------
  var REPO = 'jihemezes/kastideo';
  // Pour chaque clé data-dl : famille de version et motif du nom de fichier.
  var ASSETS = {
    'mac':           ['mac',     /^Kastideo-[\d.]+\.dmg$/],
    'win-setup':     ['desktop', /windows-x64-setup\.exe$/],
    'win-zip':       ['desktop', /windows-x64\.zip$/],
    'deb22':         ['desktop', /ubuntu22\.04_amd64\.deb$/],
    'deb24':         ['desktop', /ubuntu24\.04_amd64\.deb$/],
    'appimage-x86':  ['desktop', /linux-x86_64\.AppImage$/],
    'appimage-arm':  ['desktop', /linux-aarch64\.AppImage$/],
    'apk-arm64':     ['android', /android-arm64-v8a\.apk$/],
    'apk-v7a':       ['android', /android-armeabi-v7a\.apk$/],
    'apk-universal': ['android', /android-universal\.apk$/]
  };
  var latest = null; // { mac: {tag, assets}, desktop: ..., android: ... }

  function family(tag) {
    if (/-desktop\d*$/.test(tag)) return 'desktop';
    if (/-android\d*$/.test(tag)) return 'android';
    if (/^v\d+\.\d+\.\d+$/.test(tag)) return 'mac';
    return null; // bêtas et autres : ignorées
  }
  function ver(tag) { return tag.replace(/^v/, ''); }
  function mb(bytes) {
    var v = bytes / 1048576;
    var n = (v >= 100 ? Math.round(v) : Math.round(v * 10) / 10).toString();
    return lang === 'en' ? n + ' MB' : n.replace('.', ',') + ' Mo';
  }
  function pick(releases) {
    var out = {};
    releases.forEach(function (r) {
      if (r.draft) return;
      var f = family(r.tag_name);
      if (!f) return;
      var t = Date.parse(r.published_at || r.created_at) || 0;
      if (!out[f] || t > out[f].t) out[f] = { t: t, tag: r.tag_name, assets: r.assets || [] };
    });
    return out;
  }
  function renderReleases() {
    if (!latest) return;
    document.querySelectorAll('[data-ver]').forEach(function (el) {
      var r = latest[el.getAttribute('data-ver')];
      if (r) el.textContent = ver(r.tag);
    });
    document.querySelectorAll('[data-dl]').forEach(function (a) {
      var spec = ASSETS[a.getAttribute('data-dl')];
      if (!spec) return;
      var r = latest[spec[0]];
      var size = a.querySelector('[data-size]');
      if (!r) { if (size) size.textContent = ''; return; }
      var asset = null;
      r.assets.forEach(function (x) { if (!asset && spec[1].test(x.name)) asset = x; });
      if (asset) {
        a.href = asset.browser_download_url;
        a.removeAttribute('target');
        if (size) size.textContent = mb(asset.size) + ' · ' + ver(r.tag);
      } else {
        a.href = 'https://github.com/' + REPO + '/releases/tag/' + r.tag;
        if (size) size.textContent = '';
      }
    });
  }
  function needsReleases() {
    return document.querySelector('[data-dl], [data-ver]');
  }
  function loadReleases() {
    if (!needsReleases() || !window.fetch) return;
    var KEY = 'kastideo.releases', cached = null;
    try {
      var raw = sessionStorage.getItem(KEY);
      if (raw) { var o = JSON.parse(raw); if (Date.now() - o.at < 600000) cached = o.data; }
    } catch (e) {}
    if (cached) { latest = cached; renderReleases(); return; }
    fetch('https://api.github.com/repos/' + REPO + '/releases?per_page=50', { headers: { Accept: 'application/vnd.github+json' } })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (list) {
        latest = pick(list);
        try { sessionStorage.setItem(KEY, JSON.stringify({ at: Date.now(), data: latest })); } catch (e) {}
        renderReleases();
      })
      .catch(function () {
        // Les liens statiques vers la page des versions restent en place.
        document.querySelectorAll('[data-ver]').forEach(function (el) { if (el.textContent === '…') el.textContent = '—'; });
      });
  }

  apply(lang);
  loadReleases();
})();
