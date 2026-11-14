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
    var seen = {}, previews = [];
    function head(r, f, big) {
      var h = document.createElement(big ? 'h3' : 'span'); h.textContent = 'Kastideo ' + ver(r.tag_name);
      var wrap = document.createElement('div'); wrap.className = 'release-head'; wrap.appendChild(h);
      [d[TYPE[f]], (f === 'mac' && !r.prerelease) ? d.stable : d.preview].forEach(function (t) {
        var b = document.createElement('span'); b.className = 'badge'; b.textContent = t; wrap.appendChild(b);
      });
      var when = Date.parse(r.published_at || r.created_at);
      if (when) { var tm = document.createElement('time'); tm.dateTime = new Date(when).toISOString(); tm.textContent = nf.format(new Date(when)); wrap.appendChild(tm); }
      return wrap;
    }
    function link(r) {
      var a = document.createElement('a'); a.className = 'btn ghost'; a.target = '_blank'; a.rel = 'noopener';
      a.href = 'https://github.com/' + REPO + '/releases/tag/' + encodeURIComponent(r.tag_name); a.textContent = d.download + ' · GitHub';
      return a;
    }
    list.forEach(function (r) {
      var f = family(r.tag_name);
      if (r.draft || !f || seen[f]) return;
      seen[f] = true;
      if (f === 'mac') {
        var art = document.createElement('article'); art.className = 'release';
        art.appendChild(head(r, f, true));
        var box = document.createElement('div'); box.className = 'release-notes';
        if (r.body && r.body.trim()) notes(r.body, box); else { var n = document.createElement('p'); n.className = 'note'; n.textContent = d.none; box.appendChild(n); }
        art.appendChild(box); art.appendChild(link(r)); root.appendChild(art);
      } else previews.push([r, f]);
    });
    if (previews.length) {
      var t = document.createElement('p'); t.className = 'note'; t.textContent = d.previews + ' :'; root.appendChild(t);
      previews.forEach(function (x) {
        var row = document.createElement('div'); row.className = 'release compact';
        row.appendChild(head(x[0], x[1], false)); row.appendChild(link(x[0])); root.appendChild(row);
      });
    }
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

  /* ---------- Recherche dans le site ---------- */
  function initSearch() {
    var btn = document.getElementById('search-open');
    if (!btn || !window.fetch) return;
    var fr = lang !== 'en';
    var T = fr
      ? { open: 'Rechercher dans le site', ph: 'Rechercher (ex. Fire TV, playlist M3U…)', close: 'Fermer', pop: 'Recherches fréquentes', none: 'Aucun résultat pour « {q} ».', count1: '1 résultat', countN: '{n} résultats', err: 'Impossible de charger la recherche.' }
      : { open: 'Search the site', ph: 'Search (e.g. Fire TV, M3U playlist…)', close: 'Close', pop: 'Popular searches', none: 'No results for “{q}”.', count1: '1 result', countN: '{n} results', err: 'Search could not be loaded.' };
    var SUGG = fr
      ? ['Fire TV', 'playlist M3U', 'enregistrer', 'replay', 'iCloud', 'MultiVue', 'Android TV', 'Xtream Codes']
      : ['Fire TV', 'M3U playlist', 'recording', 'replay', 'iCloud', 'MultiVue', 'Android TV', 'Xtream Codes'];
    btn.hidden = false; btn.setAttribute('aria-label', T.open); btn.title = T.open + ' (/)';

    var data = null, loading = null, overlay = null, input, list, status, sugg, items = [], cur = -1, lastFocus = null;

    function norm(s) { return String(s).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); }
    function load() {
      if (data) return Promise.resolve(data);
      if (!loading) {
        loading = fetch('/search-' + (fr ? 'fr' : 'en') + '.json').then(function (r) {
          if (!r.ok) throw new Error('http');
          return r.json();
        }).then(function (d) {
          data = d.map(function (e) { return { e: e, t: norm(e.t), h: norm(e.h), x: norm(e.x) }; });
          return data;
        });
        loading['catch'](function () { loading = null; });
      }
      return loading;
    }
    function el(tag, cls, text) {
      var n = document.createElement(tag);
      if (cls) n.className = cls;
      if (text != null) n.textContent = text;
      return n;
    }
    function highlight(parent, text, terms) {
      var n = norm(text), marks = [], i, k;
      for (k = 0; k < terms.length; k++) {
        var from = 0, p;
        while ((p = n.indexOf(terms[k], from)) !== -1) { marks.push([p, p + terms[k].length]); from = p + terms[k].length; }
      }
      marks.sort(function (a, b) { return a[0] - b[0]; });
      var pos = 0;
      for (i = 0; i < marks.length; i++) {
        if (marks[i][1] <= pos) continue;
        var s = Math.max(marks[i][0], pos);
        if (s > pos) parent.appendChild(document.createTextNode(text.slice(pos, s)));
        parent.appendChild(el('mark', null, text.slice(s, marks[i][1])));
        pos = marks[i][1];
      }
      if (pos < text.length) parent.appendChild(document.createTextNode(text.slice(pos)));
    }
    function snippet(text, terms) {
      var n = norm(text), first = -1, k;
      for (k = 0; k < terms.length; k++) { var p = n.indexOf(terms[k]); if (p !== -1 && (first === -1 || p < first)) first = p; }
      if (first === -1) first = 0;
      var start = Math.max(0, first - 50), end = Math.min(text.length, start + 160);
      if (start > 0) { var sp = text.indexOf(' ', start); if (sp !== -1 && sp < first) start = sp + 1; }
      return (start > 0 ? '… ' : '') + text.slice(start, end) + (end < text.length ? ' …' : '');
    }
    function search(q) {
      var terms = norm(q).split(/\s+/).filter(Boolean), res = [];
      if (!terms.length) return { terms: terms, res: res };
      data.forEach(function (d) {
        var score = 0, ok = true;
        for (var i = 0; i < terms.length; i++) {
          var t = terms[i], s = 0, c;
          if (d.t.indexOf(t) !== -1) s += 10;
          if (d.h.indexOf(t) !== -1) s += 6;
          c = d.x.split(t).length - 1;
          if (c) s += Math.min(c, 5);
          if (!s) { ok = false; break; }
          score += s;
        }
        if (ok) res.push({ d: d.e, score: score + (d.e.h ? 0 : 1) });
      });
      res.sort(function (a, b) { return b.score - a.score; });
      var per = {}, out = [];
      res.forEach(function (r) {
        if (out.length >= 10) return;
        per[r.d.u] = (per[r.d.u] || 0) + 1;
        if (per[r.d.u] <= 3) out.push(r.d);
      });
      return { terms: terms, res: out };
    }
    function setCur(i) {
      if (cur >= 0 && items[cur]) { items[cur].classList.remove('on'); items[cur].removeAttribute('aria-current'); }
      cur = i;
      if (cur >= 0 && items[cur]) { items[cur].classList.add('on'); items[cur].setAttribute('aria-current', 'true'); items[cur].scrollIntoView({ block: 'nearest' }); }
    }
    function render() {
      var q = input.value.trim();
      list.textContent = ''; items = []; cur = -1;
      sugg.hidden = !!q;
      if (!q) { status.textContent = ''; return; }
      if (!data) { status.textContent = '…'; return; }
      var r = search(q);
      if (!r.res.length) { status.textContent = T.none.replace('{q}', q); return; }
      status.textContent = r.res.length === 1 ? T.count1 : T.countN.replace('{n}', r.res.length);
      r.res.forEach(function (e) {
        var li = el('li'), a = el('a', 'sr');
        a.href = e.u + (e.a ? '#' + e.a : '');
        var top = el('span', 'sr-t');
        highlight(top, e.t, r.terms);
        if (e.h) { top.appendChild(el('span', 'sr-sep', ' › ')); var h = el('span', 'sr-h'); highlight(h, e.h, r.terms); top.appendChild(h); }
        a.appendChild(top);
        if (e.x) { var sn = el('span', 'sr-x'); highlight(sn, snippet(e.x, r.terms), r.terms); a.appendChild(sn); }
        li.appendChild(a); list.appendChild(li); items.push(a);
      });
    }
    function build() {
      overlay = el('div', 'search-overlay');
      var panel = el('div', 'search-panel');
      panel.setAttribute('role', 'dialog'); panel.setAttribute('aria-modal', 'true'); panel.setAttribute('aria-label', T.open);
      var row = el('div', 'search-row');
      input = el('input'); input.type = 'search'; input.placeholder = T.ph; input.setAttribute('aria-label', T.open);
      input.autocomplete = 'off'; input.spellcheck = false;
      var x = el('button', 'search-x', '×'); x.type = 'button'; x.setAttribute('aria-label', T.close);
      row.appendChild(input); row.appendChild(x);
      sugg = el('div', 'search-sugg');
      sugg.appendChild(el('p', 'search-sugg-t', T.pop));
      var chips = el('div', 'chips');
      SUGG.forEach(function (s) {
        var c = el('button', 'chip', s); c.type = 'button';
        c.addEventListener('click', function () { input.value = s; input.focus(); run(); });
        chips.appendChild(c);
      });
      sugg.appendChild(chips);
      status = el('p', 'search-status'); status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite');
      list = el('ul', 'search-list');
      panel.appendChild(row); panel.appendChild(sugg); panel.appendChild(status); panel.appendChild(list);
      overlay.appendChild(panel);
      document.body.appendChild(overlay);
      x.addEventListener('click', close);
      overlay.addEventListener('mousedown', function (e) { if (e.target === overlay) close(); });
      input.addEventListener('input', run);
      overlay.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { e.preventDefault(); close(); }
        else if (e.key === 'ArrowDown' && items.length) { e.preventDefault(); setCur((cur + 1) % items.length); }
        else if (e.key === 'ArrowUp' && items.length) { e.preventDefault(); setCur(cur <= 0 ? items.length - 1 : cur - 1); }
        else if (e.key === 'Enter' && cur >= 0 && items[cur]) { e.preventDefault(); items[cur].click(); }
        else if (e.key === 'Tab') {
          var f = overlay.querySelectorAll('input,button,a'), vis = [], i;
          for (i = 0; i < f.length; i++) if (f[i].offsetParent !== null) vis.push(f[i]);
          if (!vis.length) return;
          var first = vis[0], last = vis[vis.length - 1];
          if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
          else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
        }
      });
    }
    function run() {
      render();
      if (!data) load().then(render, function () { status.textContent = T.err; });
    }
    function open() {
      if (!overlay) build();
      lastFocus = document.activeElement;
      overlay.hidden = false;
      document.documentElement.classList.add('search-on');
      input.focus(); input.select();
      load()['catch'](function () {});
      render();
    }
    function close() {
      if (!overlay || overlay.hidden) return;
      overlay.hidden = true;
      document.documentElement.classList.remove('search-on');
      if (lastFocus && lastFocus.focus) lastFocus.focus(); else btn.focus();
    }
    btn.addEventListener('click', open);
    document.addEventListener('keydown', function (e) {
      var t = e.target, typing = t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable);
      if ((e.key === '/' && !typing && !e.ctrlKey && !e.metaKey && !e.altKey) || ((e.key === 'k' || e.key === 'K') && (e.ctrlKey || e.metaKey))) {
        e.preventDefault(); open();
      }
    });
  }

  loadReleases();
  loadNews();
  initSearch();
})();
