// Agent Guild - Main Application
(function() {
  'use strict';

  // ---- Hamburger menu ----
  document.addEventListener('click', function(e) {
    var toggle = e.target.closest('.nav-toggle');
    if (toggle) {
      var links = toggle.nextElementSibling;
      if (links) links.classList.toggle('open');
    }
    if (!e.target.closest('.nav-toggle') && !e.target.closest('.nav-links')) {
      var nav = document.querySelector('.nav-links');
      if (nav) nav.classList.remove('open');
    }
  });

  // ---- Language detection & switcher ----
  if (!sessionStorage.getItem('lang')) {
    var lang = navigator.language || navigator.userLanguage;
    var path = window.location.pathname;
    var enLangs = ['en','en-US','en-GB','en-AU','en-CA','en-IN','en-PH','en-SG'];
    var skLangs = ['sk','sk-SK','cs','cs-CZ'];

    // Redirect english users to /en/
    if (enLangs.includes(lang) && !path.startsWith('/en') && path !== '/sk' && !path.startsWith('/sk/')) {
      window.location.href = '/en' + path;
    }
    // Redirect slovak users from /en/ to /
    if (skLangs.includes(lang) && path.startsWith('/en')) {
      window.location.href = path.replace('/en', '') || '/';
    }
  }


// ---- Scroll-triggered animations ----
(function() {
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.feature-card, .module-item, .module-card, .pricing-card, article, details').forEach(function(el) {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });
})();

})();