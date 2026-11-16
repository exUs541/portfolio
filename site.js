/* M54 – gemeinsame Helfer: Sprache (DE/EN), Icons, Kopfzeile */
(function () {
  'use strict';

  /* ---------- Englische Texte für alle statischen Elemente ----------
     Die deutschen Texte stehen direkt im HTML (Fallback ohne JavaScript). */
  var EN = {
    'skip': 'Skip to content',
    'nav.solutions': 'Solutions',
    'nav.timeline': 'Timeline',
    'nav.about': 'About',
    'nav.roadmap': 'Roadmap',
    'nav.feedback': 'Feedback',
    'nav.support': 'Support us',
    'nav.menu': 'Menu',

    'hero.pill': 'A passion project – built alongside our day jobs',
    'hero.title': 'Software that <em>simply helps.</em>',
    'hero.lead': 'M54 builds browser extensions, VR apps and everyday apps. See at a glance what is available today, what we are working on and when it will be ready.',
    'hero.cta1': 'Explore solutions',
    'hero.cta2': 'What is coming when?',

    'sol.title': 'Our solutions',
    'sol.sub': 'Filter by type and status. Click a card for all details, where to get it and the planned date.',
    'sol.type': 'Type',
    'sol.status': 'Status',
    'sol.search': 'Search, e.g. tabs, fitness, VR',
    'sol.searchlabel': 'Search solutions',
    'sol.reset': 'Reset filters',

    'tl.title': 'What is coming when?',
    'tl.sub': 'Our planned roadmap at a glance. Dates are targets, not promises – we build this alongside our jobs, so things can shift.',
    'tl.link': 'Help us go faster',

    'about.title': 'About us',
    'about.lead': 'Right now, we build all of this as a hobby.',
    'about.p1': 'The people behind M54 have regular day jobs. Everything you see here is made in our spare time – in the evenings, at weekends and out of pure enthusiasm for building useful things.',
    'about.p2': 'Because we work full time, we unfortunately cannot focus on development alone. That is why some things take longer than we would like – and why dates are targets, not guarantees.',
    'about.p3': 'Our wish is to have more time for software one day. If our work convinces you, you can help us get there (see below).',
    'about.badge.t': 'Right now: a hobby next to our jobs',
    'about.badge.d': 'With enough support: more time and faster updates.',
    'about.v1.t': 'Local & private',
    'about.v1.d': 'Our extensions and VR apps run on your device – no tracking, no ads.',
    'about.v2.t': 'Built with care',
    'about.v2.d': 'Lean, understandable tools that solve one problem properly.',
    'about.v3.t': 'Open & transparent',
    'about.v3.d': 'A public roadmap, honest dates and source code of many projects on GitHub.',

    'sup.title': 'Support our work',
    'sup.text': 'If you like our tools, we would be thrilled about your support – for example via Patreon or other donation platforms. Every contribution helps us reduce our working hours at our day jobs or, one day, focus entirely on developing programs like these.',
    'sup.benefit': 'For you that means faster updates, new apps and shorter waiting times.',
    'sup.ladder': 'What your support does',
    'sup.s1.t': 'More time for updates',
    'sup.s1.d': 'Bug fixes and new features arrive faster.',
    'sup.s2.t': 'Fewer hours at the day job',
    'sup.s2.d': 'We can cut our working hours and build more.',
    'sup.s3.t': 'Full focus on development',
    'sup.s3.d': 'In the best case we work on our programs full time.',
    'sup.free.t': 'You can help without money, too',
    'sup.free.1': 'Rate our extensions in the Chrome Web Store',
    'sup.free.2': 'Tell friends and colleagues about them',
    'sup.free.3': 'Send us ideas and bug reports',

    'fb.title': 'Ideas, wishes, bugs?',
    'fb.sub': 'Your feedback decides what we build next.',
    'fb.idea.t': 'Suggest an idea',
    'fb.idea.d': 'Missing a feature or have a new tool in mind? Tell us.',
    'fb.idea.b': 'Submit idea',
    'fb.bug.t': 'Report a bug',
    'fb.bug.d': 'Something does not work as expected? Help us fix it.',
    'fb.bug.b': 'Report bug',
    'fb.road.t': 'Roadmap & wishes',
    'fb.road.d': 'See what is planned for our extensions and vote.',
    'fb.road.b': 'Open roadmap',

    'foot.rights': '© {year} M54. Built with care – in our spare time.',
    'foot.privacy': 'Privacy Policy',
    'foot.marks': 'All product and brand names belong to their respective owners. Our extensions are independent and not affiliated with these companies.',

    /* Roadmap-Seite */
    'rm.title': 'Roadmap & feature wishes',
    'rm.sub': 'Planned improvements for our extensions – straight from our backlog. The big picture is on the <a href="index.html#zeitplan">timeline</a>.',
    'rm.filter': 'Status',
    'rm.sort': 'Sort by',
    'rm.all': 'All',
    'rm.backlog': 'Backlog',
    'rm.planned': 'Planned',
    'rm.progress': 'In progress',
    'rm.published': 'Published',
    'rm.cancelled': 'Cancelled',
    'rm.sort.votes': 'Top votes',
    'rm.sort.az': 'Name (A–Z)',
    'rm.sort.status': 'Status priority',
    'rm.loading': 'Loading roadmap …',
    'rm.empty': 'No items for this filter.',
    'rm.error': 'The roadmap could not be loaded. Please try again later.',
    'rm.type.extension': 'Extension',
    'rm.type.system': 'System',
    'rm.close': 'Close',
    'rm.back': 'Back to overview',
    'rm.note': 'Votes are only stored in your browser for now.',

    /* Feedback-Seite */
    'f.title': 'Feedback hub',
    'f.sub': 'Have an idea or found a bug? Let us make these tools better together.',
    'f.tab.idea': 'Suggest an idea',
    'f.tab.bug': 'Report a bug',
    'f.name': 'Your name',
    'f.email': 'Email address (optional)',
    'f.target': 'Which project?',
    'f.general': 'General / new project',
    'f.idea': 'Your idea',
    'f.idea.ph': 'Describe your feature request in detail …',
    'f.send.idea': 'Submit idea',
    'f.affected': 'Affected project',
    'f.env': 'Browser / device',
    'f.env.ph': 'Chrome on Windows 11, Meta Quest 3 …',
    'f.steps': 'Steps to reproduce',
    'f.steps.ph': '1. Open the popup … 2. Click settings …',
    'f.desc': 'Bug description',
    'f.desc.ph': 'What exactly is happening?',
    'f.send.bug': 'Submit bug report',
    'f.name.ph': 'Alex Example',
    'f.email.ph': 'alex@example.com'
  };

  /* ---------- Icons (Inline-SVG-Sprite, keine externen Skripte) ---------- */
  var STROKE = {
    'arrow-right': '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    'arrow-left': '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
    'arrow-up-right': '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>',
    'check': '<path d="M20 6 9 17l-5-5"/>',
    'x': '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    'menu': '<path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/>',
    'search': '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    'calendar': '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
    'clock': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    'external': '<path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
    'heart': '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
    'globe': '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    'languages': '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>',
    'phone': '<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
    'grid': '<rect width="7" height="7" x="3" y="3" rx="1.5"/><rect width="7" height="7" x="14" y="3" rx="1.5"/><rect width="7" height="7" x="14" y="14" rx="1.5"/><rect width="7" height="7" x="3" y="14" rx="1.5"/>',
    'vr': '<path d="M2 9a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2h-4.2a2 2 0 0 1-1.6-.8l-.7-1a2 2 0 0 0-1.6-.8h-3.8a2 2 0 0 0-1.6.8l-.7 1a2 2 0 0 1-1.6.8H4a2 2 0 0 1-2-2Z"/>',
    'lock': '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    'lightbulb': '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
    'alert': '<circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/>',
    'map': '<path d="M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3Z"/><path d="M9 3v15"/><path d="M15 6v15"/>',
    'chrome': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="M21.17 8H12"/><path d="M3.95 6.06 8.54 14"/><path d="M10.88 21.94 15.46 14"/>',
    'play': '<path d="M6 3l14 9-14 9Z"/>',
    'download': '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/>',
    'send': '<path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/>',
    'rotate': '<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>',
    'shield': '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
    'check-circle': '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
    'star': '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.9L12 17.8 5.8 21l1.2-6.9-5-4.9 6.9-1Z"/>',
    'share': '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4"/><path d="m15.4 6.5-6.8 4"/>',
    'message': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2Z"/>',
    'chevron-up': '<path d="m18 15-6-6-6 6"/>',
    'chevron-down': '<path d="m6 9 6 6 6-6"/>'
  };
  var FILL = {
    'github': '<path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.44 9.8 8.21 11.39.6.11.79-.26.79-.58v-2.23c-3.34.73-4.04-1.42-4.04-1.42-.55-1.39-1.33-1.76-1.33-1.76-1.09-.75.08-.73.08-.73 1.2.08 1.84 1.24 1.84 1.24 1.07 1.83 2.81 1.3 3.49 1 .11-.78.42-1.3.76-1.6-2.67-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.18 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.29-1.55 3.3-1.23 3.3-1.23.66 1.66.24 2.88.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.61-2.81 5.63-5.48 5.92.43.37.82 1.1.82 2.22v3.29c0 .32.19.7.8.58A12 12 0 0 0 24 12c0-6.63-5.37-12-12-12Z"/>',
    'youtube': '<path d="M23.5 6.19a3.02 3.02 0 0 0-2.12-2.14C19.5 3.55 12 3.55 12 3.55s-7.5 0-9.38.5A3.02 3.02 0 0 0 .5 6.19C0 8.07 0 12 0 12s0 3.93.5 5.81a3.02 3.02 0 0 0 2.12 2.14c1.88.5 9.38.5 9.38.5s7.5 0 9.38-.5a3.02 3.02 0 0 0 2.12-2.14C24 15.93 24 12 24 12s0-3.93-.5-5.81ZM9.55 15.57V8.43L15.82 12l-6.27 3.57Z"/>',
    'linkedin': '<path d="M19 0H5a5 5 0 0 0-5 5v14a5 5 0 0 0 5 5h14a5 5 0 0 0 5-5V5a5 5 0 0 0-5-5ZM8 19H5V8h3v11ZM6.5 6.73a1.76 1.76 0 1 1 0-3.53 1.76 1.76 0 0 1 0 3.53ZM20 19h-3v-5.6c0-3.37-4-3.11-4 0V19h-3V8h3v1.77c1.4-2.59 7-2.78 7 2.48V19Z"/>',
    'patreon': '<path d="M22.96 7.21c0-3.08-2.58-5.51-5.63-5.51s-5.51 2.43-5.51 5.51c0 3.04 2.47 5.51 5.51 5.51 3.04 0 5.63-2.43 5.63-5.51ZM2.09 1.7v20.6h4.18V1.7H2.09Z"/>'
  };

  var spriteBuilt = false;
  function buildSprite() {
    if (spriteBuilt) return;
    spriteBuilt = true;
    var out = '<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>';
    Object.keys(STROKE).forEach(function (k) { out += '<symbol id="i-' + k + '" viewBox="0 0 24 24">' + STROKE[k] + '</symbol>'; });
    Object.keys(FILL).forEach(function (k) { out += '<symbol id="i-' + k + '" viewBox="0 0 24 24"><g fill="currentColor" stroke="none">' + FILL[k] + '</g></symbol>'; });
    out += '</defs></svg>';
    document.body.insertAdjacentHTML('afterbegin', out);
  }
  function icon(name, cls) {
    return '<svg class="i' + (cls ? ' ' + cls : '') + '" aria-hidden="true" focusable="false"><use href="#i-' + name + '"></use></svg>';
  }

  /* ---------- Sprache ---------- */
  var listeners = [];
  var lang = 'de';
  /* Weitere Sprachen: hier eintragen (und die Texte in EN/Daten ergänzen). `name` wird in der eigenen Sprache angezeigt. */
  var LANGS = [
    { code: 'de', name: 'Deutsch' },
    { code: 'en', name: 'English' }
  ];
  function langCodes() { return LANGS.map(function (l) { return l.code; }); }
  var LANG_LABEL = { de: 'Sprache wählen', en: 'Choose language' };
  function detectLang() {
    var stored = null;
    try { stored = localStorage.getItem('exus-lang'); } catch (e) { /* privater Modus */ }
    if (stored && langCodes().indexOf(stored) !== -1) return stored;
    var nav = (navigator.languages && navigator.languages[0]) || navigator.language || 'de';
    return /^de/i.test(nav) ? 'de' : 'en';
  }
  function pick(obj) {
    if (obj == null) return '';
    if (typeof obj === 'string') return obj;
    return obj[lang] != null ? obj[lang] : (obj.de != null ? obj.de : obj.en);
  }
  function fill(str) { return str.replace('{year}', String(new Date().getFullYear())); }

  function applyStatic() {
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      if (el.dataset.de === undefined) el.dataset.de = el.innerHTML;
      var key = el.getAttribute('data-i18n');
      el.innerHTML = fill(lang === 'en' && EN[key] != null ? EN[key] : el.dataset.de);
    });
    [['data-i18n-ph', 'placeholder', 'dePlaceholder'], ['data-i18n-aria', 'aria-label', 'deAria']].forEach(function (pair) {
      document.querySelectorAll('[' + pair[0] + ']').forEach(function (el) {
        var store = pair[2];
        if (el.dataset[store] === undefined) el.dataset[store] = el.getAttribute(pair[1]) || '';
        var key = el.getAttribute(pair[0]);
        el.setAttribute(pair[1], lang === 'en' && EN[key] != null ? EN[key] : el.dataset[store]);
      });
    });
    syncLangMenu();
    var titleEl = document.querySelector('title[data-de]');
    if (titleEl) document.title = lang === 'en' ? titleEl.getAttribute('data-en') : titleEl.getAttribute('data-de');
  }
  function setLang(next, silent) {
    if (langCodes().indexOf(next) === -1) return;
    lang = next;
    if (!silent) { try { localStorage.setItem('exus-lang', next); } catch (e) { /* ignorieren */ } }
    applyStatic();
    listeners.forEach(function (fn) { fn(lang); });
  }

  /* ---------- Kopfzeile ---------- */
  function initHeader() {
    var header = document.querySelector('.site-header');
    if (!header) return;
    var btn = header.querySelector('.menu-btn');
    if (btn) {
      btn.addEventListener('click', function () {
        var open = header.classList.toggle('nav-open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      header.querySelectorAll('.nav a').forEach(function (a) {
        a.addEventListener('click', function () {
          header.classList.remove('nav-open');
          btn.setAttribute('aria-expanded', 'false');
        });
      });
    }
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    initLangMenu();
  }

  /* ---------- Sprachmenü: nur ein Symbol, Klick öffnet die Auswahl ---------- */
  function syncLangMenu() {
    document.querySelectorAll('[data-lang-menu]').forEach(function (host) {
      var label = LANG_LABEL[lang] || LANG_LABEL.en;
      var btn = host.querySelector('.lang-btn');
      var menu = host.querySelector('.lang-menu');
      if (btn) { btn.setAttribute('aria-label', label); btn.setAttribute('title', label); }
      if (menu) menu.setAttribute('aria-label', label);
      host.querySelectorAll('[data-lang]').forEach(function (b) {
        b.setAttribute('aria-checked', b.dataset.lang === lang ? 'true' : 'false');
      });
    });
  }

  function initLangMenu() {
    var hosts = document.querySelectorAll('[data-lang-menu]');
    if (!hosts.length) return;

    function closeAll(focusBtn) {
      hosts.forEach(function (host) {
        var menu = host.querySelector('.lang-menu');
        var btn = host.querySelector('.lang-btn');
        if (menu.hidden) return;
        menu.hidden = true;
        btn.setAttribute('aria-expanded', 'false');
        if (focusBtn) btn.focus();
      });
    }

    hosts.forEach(function (host, idx) {
      var uid = 'lang-menu-' + idx;
      host.innerHTML =
        '<button type="button" class="icon-btn lang-btn" aria-haspopup="menu" aria-expanded="false" aria-controls="' + uid + '">' + icon('languages') + '</button>' +
        '<ul class="lang-menu" id="' + uid + '" role="menu" hidden>' +
        LANGS.map(function (l) {
          return '<li role="none"><button type="button" role="menuitemradio" data-lang="' + l.code + '" lang="' + l.code + '" aria-checked="false"><span>' + l.name + '</span>' + icon('check') + '</button></li>';
        }).join('') +
        '</ul>';

      var btn = host.querySelector('.lang-btn');
      var menu = host.querySelector('.lang-menu');
      var items = Array.prototype.slice.call(menu.querySelectorAll('[data-lang]'));

      function open() {
        closeAll(false);
        menu.hidden = false;
        btn.setAttribute('aria-expanded', 'true');
        var current = menu.querySelector('[aria-checked="true"]') || items[0];
        if (current) current.focus();
      }

      btn.addEventListener('click', function () { if (menu.hidden) open(); else closeAll(true); });
      btn.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowDown') { e.preventDefault(); if (menu.hidden) open(); }
      });
      items.forEach(function (b) {
        b.addEventListener('click', function () { setLang(b.dataset.lang); closeAll(true); });
      });
      menu.addEventListener('keydown', function (e) {
        var i = items.indexOf(document.activeElement);
        if (e.key === 'ArrowDown') { e.preventDefault(); items[(i + 1) % items.length].focus(); }
        else if (e.key === 'ArrowUp') { e.preventDefault(); items[(i - 1 + items.length) % items.length].focus(); }
        else if (e.key === 'Home') { e.preventDefault(); items[0].focus(); }
        else if (e.key === 'End') { e.preventDefault(); items[items.length - 1].focus(); }
        else if (e.key === 'Escape') { e.preventDefault(); closeAll(true); }
        else if (e.key === 'Tab') { closeAll(false); }
      });
    });

    document.addEventListener('click', function (e) {
      if (!e.target.closest('[data-lang-menu]')) closeAll(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeAll(true);
    });
    syncLangMenu();
  }

  function init() {
    buildSprite();
    lang = detectLang();
    document.querySelectorAll('[data-icon]').forEach(function (el) {
      el.insertAdjacentHTML('afterbegin', icon(el.getAttribute('data-icon')));
    });
    applyStatic();
    initHeader();
    listeners.forEach(function (fn) { fn(lang); });
  }

  window.EXUS = {
    icon: icon,
    pick: pick,
    get lang() { return lang; },
    setLang: setLang,
    onLang: function (fn) { listeners.push(fn); },
    ready: function (fn) {
      if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn); else fn();
    }
  };
  EXUS.ready(init);
})();
