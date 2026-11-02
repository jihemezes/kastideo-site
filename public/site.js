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

  // La langue est portée par l'adresse de la page (/ pour le français, /en/ pour l'anglais).
  lang = document.documentElement.lang === 'en' ? 'en' : 'fr';

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

  // ---- Page Nouveautés : notes de version lues sur GitHub, rendues sans innerHTML ----
  function inline(parent, text) {
    var re = /(\*\*[^*]+\*\*|`[^`]+`)/g, parts = text.split(re);
    parts.forEach(function (t) {
      if (!t) return;
      var el;
      if (/^\*\*[^*]+\*\*$/.test(t)) { el = document.createElement('b'); el.textContent = t.slice(2, -2); parent.appendChild(el); }
      else if (/^`[^`]+`$/.test(t)) { el = document.createElement('code'); el.textContent = t.slice(1, -1); parent.appendChild(el); }
      else parent.appendChild(document.createTextNode(t));
    });
  }
  function notes(body, box) {
    var ul = null, p = null;
    String(body || '').replace(/\r/g, '').split('\n').forEach(function (line) {
      var l = line.trim(), m;
      if (!l) { ul = null; return; }
      if ((m = l.match(/^#{1,6}\s+(.*)$/))) { ul = null; var h = document.createElement('h4'); inline(h, m[1]); box.appendChild(h); return; }
      if ((m = l.match(/^[-*]\s+(.*)$/))) {
        if (!ul) { ul = document.createElement('ul'); box.appendChild(ul); }
        var li = document.createElement('li'); inline(li, m[1]); ul.appendChild(li); return;
      }
      ul = null; p = document.createElement('p'); inline(p, l); box.appendChild(p);
    });
  }
  var TYPE = { mac: 'mac', desktop: 'desktop', android: 'android' };
  function renderNews(root, list) {
    var d = root.dataset, nf = new Intl.DateTimeFormat(lang === 'en' ? 'en-GB' : 'fr-FR', { day: 'numeric', month: 'long', year: 'numeric' });
    root.textContent = '';
    var shown = 0;
    list.forEach(function (r) {
      var f = family(r.tag_name);
      if (r.draft || !f || shown >= 15) return;
      shown++;
      var art = document.createElement('article'); art.className = 'release';
      var head = document.createElement('div'); head.className = 'release-head';
      var h = document.createElement('h2'); h.textContent = (f === 'mac' ? 'Kastideo ' : 'Kastideo ') + ver(r.tag_name); head.appendChild(h);
      [d[TYPE[f]], (f === 'mac' && !r.prerelease) ? d.stable : d.preview].forEach(function (t) {
        var b = document.createElement('span'); b.className = 'badge'; b.textContent = t; head.appendChild(b);
      });
      var when = Date.parse(r.published_at || r.created_at);
      if (when) { var tm = document.createElement('time'); tm.dateTime = new Date(when).toISOString(); tm.textContent = nf.format(new Date(when)); head.appendChild(tm); }
      art.appendChild(head);
      var box = document.createElement('div'); box.className = 'release-notes';
      if (r.body && r.body.trim()) notes(r.body, box); else { var n = document.createElement('p'); n.className = 'note'; n.textContent = d.none; box.appendChild(n); }
      art.appendChild(box);
      var a = document.createElement('a'); a.className = 'btn ghost'; a.target = '_blank'; a.rel = 'noopener';
      a.href = 'https://github.com/' + REPO + '/releases/tag/' + encodeURIComponent(r.tag_name); a.textContent = d.download + ' · GitHub';
      art.appendChild(a);
      root.appendChild(art);
    });
    var more = document.createElement('p');
    var ma = document.createElement('a'); ma.href = 'https://github.com/' + REPO + '/releases'; ma.target = '_blank'; ma.rel = 'noopener'; ma.textContent = d.more;
    more.appendChild(ma); root.appendChild(more);
  }
  function loadNews() {
    var root = document.getElementById('releases');
    if (!root || !window.fetch) return;
    var KEY = 'kastideo.news', cached = null;
    try { var raw = sessionStorage.getItem(KEY); if (raw) { var o = JSON.parse(raw); if (Date.now() - o.at < 600000) cached = o.data; } } catch (e) {}
    if (cached) { renderNews(root, cached); return; }
    fetch('https://api.github.com/repos/' + REPO + '/releases?per_page=50', { headers: { Accept: 'application/vnd.github+json' } })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (list) {
        var slim = list.map(function (r) { return { tag_name: r.tag_name, draft: r.draft, prerelease: r.prerelease, published_at: r.published_at, created_at: r.created_at, body: r.body }; });
        try { sessionStorage.setItem(KEY, JSON.stringify({ at: Date.now(), data: slim })); } catch (e) {}
        renderNews(root, slim);
      })
      .catch(function () {
        root.textContent = '';
        var p = document.createElement('p'); p.className = 'note'; p.appendChild(document.createTextNode(root.dataset.error + ' '));
        var a = document.createElement('a'); a.href = 'https://github.com/' + REPO + '/releases'; a.target = '_blank'; a.rel = 'noopener'; a.textContent = root.dataset.more;
        p.appendChild(a); root.appendChild(p);
      });
  }

  loadReleases();
  loadNews();
})();
