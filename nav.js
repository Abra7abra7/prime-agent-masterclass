// Agent Guild - Nav & Footer Injection
(function() {
  var lang = window.location.pathname.startsWith('/en') ? 'en' : 'sk';
  var base = lang === 'en' ? '/en' : '';

  var nav = document.createElement('nav');
  nav.style.cssText = 'padding: 14px 0; border-bottom: 1px solid rgba(205,127,50,0.15);';

  var enLabel = '🇬🇧 EN';
  var skLabel = '🇸🇰 SK';
  var enLink = '/en' + window.location.pathname.replace(/^\/en/, '');
  var skLink = window.location.pathname.replace(/^\/en/, '') || '/';

  nav.innerHTML = '<div class="container">' +
    '<button class="nav-toggle" onclick="this.nextElementSibling.classList.toggle(\'open\')" aria-label="Menu">☰</button>' +
    '<div class="nav-links">' +
    '<a href="' + base + '/" style="color: #c8c8d4; text-decoration: none;">✦ <strong>Agent Guild</strong></a>' +
    '<a href="' + base + '/kurz" style="color: #c8c8d4; text-decoration: none;">Kurz</a>' +
    '<a href="' + base + '/o-nas" style="color: #c8c8d4; text-decoration: none;">O nás</a>' +
    '<a href="' + base + '/faq" style="color: #c8c8d4; text-decoration: none;">FAQ</a>' +
    '<a href="' + base + '/blog" style="color: #c8c8d4; text-decoration: none;">Blog</a>' +
    '<a href="' + base + '/affiliate" style="color: #c8c8d4; text-decoration: none;">Affiliate</a>' +
    '<a href="' + enLink + '" class="lang-switch" style="color: #CD7F32 !important; font-weight: 600;">🇬🇧 EN</a>' +
    '<a href="' + skLink + '" class="lang-switch" style="color: #CD7F32 !important; font-weight: 600;">🇸🇰 SK</a>' +
    '</div></div>';

  document.body.insertBefore(nav, document.body.firstChild);

  var footer = document.createElement('footer');
  footer.innerHTML = '<div class="container">' +
    '<p style="font-style: italic; color: var(--bronze);">Build your AI army.</p>' +
    '<p>© 2026 ASCENTIA s. r. o. — IČO: 51858959 — Klincová 37/B, 821 08 Bratislava</p>' +
    '</div>';
  document.body.appendChild(footer);
})();
