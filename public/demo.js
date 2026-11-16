/* Aperçu interactif de l'accueil : contenus fictifs, aucune source réelle. */
(function () {
  'use strict';
  var root = document.getElementById('demo');
  if (!root) return;
  var en = document.documentElement.lang === 'en';
  function t(fr, e) { return en ? e : fr; }

  var LIVE = [
    ['Horizon Info', t('Le journal du soir', 'Evening news'), '20:00', '20:45', 62],
    ['Sport Arena', t('Championnat : le match', 'League match of the night'), '20:45', '22:45', 18],
    ['Cinéma Nuit', t('Les Ombres du port', 'Shadows of the Harbour'), '21:00', '22:50', 40],
    ['Planète Nature', t('Au cœur de la forêt', 'Into the Forest'), '20:30', '21:30', 75],
    ['Kids Planet', t('Les Aventures de Pip', 'The Adventures of Pip'), '19:45', '20:15', 90],
    ['Musique 24', t('Concert en direct', 'Live concert'), '20:00', '22:00', 33],
    ['Docs & Co', t('Enquête sur les océans', 'Investigating the oceans'), '20:50', '21:50', 12],
    ['Retro TV', t('Séries cultes', 'Cult series'), '20:15', '21:05', 55]
  ];
  var FILMS = [
    ['Big Buck Bunny', '2008', t('Animation', 'Animation'), 0],
    ['Sintel', '2010', t('Fantasy', 'Fantasy'), 1],
    ['Tears of Steel', '2012', t('Science-fiction', 'Sci-fi'), 2],
    ['Elephants Dream', '2006', t('Animation', 'Animation'), 3],
    ['Cosmos Laundromat', '2015', t('Animation', 'Animation'), 1],
    ['Spring', '2019', t('Animation', 'Animation'), 0],
    ['Agent 327', '2017', t('Comédie', 'Comedy'), 2],
    ['Coffee Run', '2020', t('Animation', 'Animation'), 3]
  ];
  var SERIES = [
    [t('Les Mers du Nord', 'Northern Seas'), t('2 saisons · 16 épisodes', '2 seasons · 16 episodes'), 1],
    [t('Quartier 9', 'District 9'), t('1 saison · 8 épisodes', '1 season · 8 episodes'), 2],
    [t('Le Dernier Phare', 'The Last Lighthouse'), t('3 saisons · 24 épisodes', '3 seasons · 24 episodes'), 3],
    [t('Archives secrètes', 'Secret Archives'), t('1 saison · 6 épisodes', '1 season · 6 episodes'), 0],
    [t('Terres lointaines', 'Distant Lands'), t('2 saisons · 20 épisodes', '2 seasons · 20 episodes'), 2],
    [t('Nuit blanche', 'White Night'), t('1 saison · 10 épisodes', '1 season · 10 episodes'), 1]
  ];
  var VIDEOS = [
    [t('Vacances en Corse', 'Holiday in Corsica'), 'NAS', '4K · MP4', 0],
    [t('Concert 2024', 'Concert 2024'), 'Jellyfin', 'MKV', 3],
    [t('Mariage de Léa', "Lea's wedding"), t('Dossier', 'Folder'), 'MOV', 1],
    [t('Documentaire archives', 'Archive documentary'), 'Plex', 'MKV', 2]
  ];
  var REPLAY = [
    ['Horizon Info', t('Le journal du soir', 'Evening news'), t('hier 20:00', 'yesterday 8:00 pm')],
    ['Cinéma Nuit', t('Les Ombres du port', 'Shadows of the Harbour'), t('hier 21:00', 'yesterday 9:00 pm')],
    ['Planète Nature', t('Au cœur de la forêt', 'Into the Forest'), t('mar. 20:30', 'Tue 8:30 pm')],
    ['Sport Arena', t('Le match de la veille', "Last night's match"), t('lun. 20:45', 'Mon 8:45 pm')]
  ];
  var REC = [
    ['Cinéma Nuit', t('Les Ombres du port', 'Shadows of the Harbour'), 'REC', t('en cours · 38 min', 'recording · 38 min')],
    ['Planète Nature', t('Au cœur de la forêt', 'Into the Forest'), 'PLAN', t('ce soir 20:30', 'tonight 8:30 pm')],
    ['Horizon Info', t('Le journal du soir', 'Evening news'), 'OK', 'MP4 · 1,4 Go'],
    ['Docs & Co', t('Enquête sur les océans', 'Investigating the oceans'), 'OK', 'MP4 · 2,1 Go']
  ];
  var EPG = [
    ['Horizon Info', [[t('Le journal', 'News'), 2], [t('Débat', 'Debate'), 3], [t('Météo+', 'Weather+'), 1]]],
    ['Sport Arena', [[t('Avant-match', 'Pre-match'), 1], [t('Le match', 'The match'), 4], [t('Résumé', 'Highlights'), 1]]],
    ['Cinéma Nuit', [[t('Les Ombres du port', 'Shadows of the Harbour'), 4], [t('Court-métrage', 'Short film'), 2]]],
    ['Planète Nature', [[t('Au cœur de la forêt', 'Into the Forest'), 3], [t('Savane', 'Savannah'), 3]]]
  ];

  var VIEWS = {
    live: { title: t('À la télé maintenant', 'On TV now'), n: LIVE.length, unit: t('chaînes', 'channels') },
    films: { title: t('Films', 'Movies'), n: FILMS.length, unit: t('titres', 'titles') },
    series: { title: t('Séries', 'Series'), n: SERIES.length, unit: t('séries', 'series') },
    videos: { title: t('Mes vidéos', 'My videos'), n: VIDEOS.length, unit: t('vidéos', 'videos') },
    fav: { title: t('Favoris', 'Favourites'), n: 4, unit: t('chaînes', 'channels') },
    recent: { title: t('Récents', 'Recent'), n: 4, unit: t('éléments', 'items') },
    epg: { title: t('Guide TV', 'TV guide'), n: EPG.length, unit: t('chaînes', 'channels') },
    replay: { title: t('Revoir (replay)', 'Watch again (replay)'), n: REPLAY.length, unit: t('programmes', 'programmes') },
    rec: { title: t('Enregistrements', 'Recordings'), n: REC.length, unit: t('éléments', 'items') }
  };
  var view = 'live', query = '';
  var grid = document.getElementById('demo-grid'), ttl = document.getElementById('demo-title'), cnt = document.getElementById('demo-count'),
      note = document.getElementById('demo-note'), q = document.getElementById('demo-q');
  q.placeholder = t('Rechercher une chaîne, un film…', 'Search a channel, a movie…');
  var NOTE0 = note.textContent;

  function norm(s) { return String(s).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); }
  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }
  function match(a) { return !query || norm(a.join(' ')).indexOf(query) !== -1; }
  function play(name) {
    note.textContent = t('▶ Dans l’application, un clic lance « ' + name + ' ».', '▶ In the app, a click plays “' + name + '”.');
  }
  function card(cls, title, sub, extra) {
    var b = el('button', 'dc ' + cls); b.type = 'button';
    b.appendChild(el('span', 'dc-t', title));
    if (sub) b.appendChild(el('span', 'dc-s', sub));
    if (extra) b.appendChild(extra);
    b.addEventListener('click', function () { play(title); });
    return b;
  }
  function chan(c) {
    var b = card('chan', c[0], c[1] + ' · ' + c[2] + '–' + c[3]);
    var bar = el('span', 'dc-bar'), i = el('i'); i.style.width = c[4] + '%'; bar.appendChild(i); b.appendChild(bar);
    b.insertBefore(el('span', 'dc-logo', c[0].charAt(0)), b.firstChild);
    return b;
  }
  function poster(title, sub, g) { var b = card('poster g' + g, title, sub); return b; }

  var out;
  function build() {
    var items = [];
    if (view === 'live') items = LIVE.filter(function (c) { return match([c[0], c[1]]); }).map(chan);
    else if (view === 'fav') items = LIVE.slice(0, 4).filter(function (c) { return match([c[0], c[1]]); }).map(chan);
    else if (view === 'films') items = FILMS.filter(function (f) { return match([f[0], f[2]]); }).map(function (f) { return poster(f[0], f[1] + ' · ' + f[2], f[3]); });
    else if (view === 'series') items = SERIES.filter(function (s) { return match([s[0]]); }).map(function (s) { return poster(s[0], s[1], s[2]); });
    else if (view === 'videos') items = VIDEOS.filter(function (v) { return match([v[0], v[1]]); }).map(function (v) { return poster(v[0], v[1] + ' · ' + v[2], v[3]); });
    else if (view === 'recent') {
      items = FILMS.slice(0, 2).filter(function (f) { return match([f[0]]); }).map(function (f) { return poster(f[0], f[1] + ' · ' + f[2], f[3]); })
        .concat(LIVE.slice(1, 3).filter(function (c) { return match([c[0], c[1]]); }).map(chan));
    } else if (view === 'replay') {
      items = REPLAY.filter(function (r) { return match(r); }).map(function (r) {
        var b = card('chan', r[1], r[0] + ' · ' + r[2]); b.insertBefore(el('span', 'dc-logo rp', '↺'), b.firstChild); return b;
      });
    } else if (view === 'rec') {
      items = REC.filter(function (r) { return match(r); }).map(function (r) {
        var b = card('chan', r[1], r[0] + ' · ' + r[3]);
        b.insertBefore(el('span', 'dc-logo st-' + r[2].toLowerCase(), r[2] === 'REC' ? '●' : r[2] === 'PLAN' ? '◷' : '✓'), b.firstChild); return b;
      });
    }
    return items;
  }
  function epg() {
    var rows = EPG.filter(function (r) { return match([r[0]].concat(r[1].map(function (s) { return s[0]; }))); });
    var wrap = el('div', 'epg');
    var head = el('div', 'epg-row epg-head'); head.appendChild(el('span', 'epg-ch', ''));
    var hours = ['20:00', '21:00', '22:00', '23:00'];
    var hs = el('span', 'epg-slots');
    hours.forEach(function (h) { hs.appendChild(el('span', 'epg-h', h)); });
    head.appendChild(hs); wrap.appendChild(head);
    rows.forEach(function (r) {
      var row = el('div', 'epg-row'); row.appendChild(el('span', 'epg-ch', r[0]));
      var sl = el('span', 'epg-slots');
      r[1].forEach(function (s) {
        var b = el('button', 'epg-p', s[0]); b.type = 'button'; b.style.flex = String(s[1]);
        b.addEventListener('click', function () { play(s[0]); });
        sl.appendChild(b);
      });
      row.appendChild(sl); wrap.appendChild(row);
    });
    return { node: wrap, n: rows.length };
  }
  function render() {
    var v = VIEWS[view], n;
    grid.textContent = '';
    grid.className = 'd-grid' + (view === 'epg' ? ' is-epg' : '');
    if (view === 'epg') { var e = epg(); grid.appendChild(e.node); n = e.n; }
    else { var items = build(); items.forEach(function (i) { grid.appendChild(i); }); n = items.length; }
    ttl.textContent = v.title;
    cnt.textContent = n ? n + ' ' + v.unit : t('Aucun résultat', 'No results');
    var btns = root.querySelectorAll('[data-view]'), i;
    for (i = 0; i < btns.length; i++) btns[i].setAttribute('aria-pressed', btns[i].getAttribute('data-view') === view ? 'true' : 'false');
  }
  root.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('[data-view]') : null;
    if (!b) return;
    view = b.getAttribute('data-view'); note.textContent = NOTE0; render();
  });
  q.addEventListener('input', function () { query = norm(q.value.trim()); note.textContent = NOTE0; render(); });
  render();
})();
