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
  apply(lang);
})();
