/* exUs541 – Startseite: Projekt-Übersicht, Filter, Detail-Panel, Zeitplan */
(function () {
  'use strict';

  var X = window.EXUS;
  var icon = X.icon;
  var pick = X.pick;

  /* ---------- Dynamische Texte (DE/EN) ---------- */
  var S = {
    'status.live': { de: 'Verfügbar', en: 'Available' },
    'status.beta': { de: 'Beta – nutzbar', en: 'Beta – usable' },
    'status.dev': { de: 'In Entwicklung', en: 'In development' },
    'type.vr': { de: 'VR-App', en: 'VR app' },
    'type.android': { de: 'Android-App', en: 'Android app' },
    'type.game': { de: 'PC-Spiel', en: 'PC game' },
    'type.desktop': { de: 'PC-Anwendung', en: 'PC application' },
    'type.extension': { de: 'Browser-Extension', en: 'Browser extension' },
    'f.all': { de: 'Alle', en: 'All' },
    'f.vr': { de: 'VR-Apps', en: 'VR apps' },
    'f.android': { de: 'Android-Apps', en: 'Android apps' },
    'f.game': { de: 'PC-Spiele', en: 'PC games' },
    'f.desktop': { de: 'PC-Anwendungen', en: 'PC applications' },
    'f.extension': { de: 'Browser-Extensions', en: 'Browser extensions' },
    'tags.more': { de: 'Alle Tags ({n})', en: 'All tags ({n})' },
    'tags.less': { de: 'Weniger Tags', en: 'Fewer tags' },
    'd.tags': { de: 'Tags', en: 'Tags' },
    'stat.live': { de: 'Verfügbar', en: 'Available' },
    'stat.beta': { de: 'Beta', en: 'Beta' },
    'stat.dev': { de: 'In Entwicklung', en: 'In development' },
    'stat.next': { de: 'Nächster Release', en: 'Next release' },
    'g.works.t': { de: 'In Arbeit', en: 'In the works' },
    'g.works.d': { de: 'Apps, die gerade entstehen – mit aktuellem Stand und geplantem Termin.', en: 'Apps taking shape right now – with current status and planned date.' },
    'g.live.t': { de: 'Heute verfügbar', en: 'Available today' },
    'g.live.d': { de: 'Fertige Lösungen, die du sofort nutzen kannst.', en: 'Finished solutions you can use right away.' },
    'count.one': { de: '{n} Lösung', en: '{n} solution' },
    'count.many': { de: '{n} Lösungen', en: '{n} solutions' },
    'details': { de: 'Details', en: 'Details' },
    'eta.expected': { de: 'Voraussichtlich', en: 'Expected' },
    'eta.open': { de: 'Termin offen', en: 'Date open' },
    'eta.openLong': { de: 'Noch kein fester Termin', en: 'No fixed date yet' },
    'soon': { de: 'geplant', en: 'planned' },
    'stage.1': { de: 'Idee', en: 'Idea' },
    'stage.2': { de: 'Entwicklung', en: 'Development' },
    'stage.3': { de: 'Test & Store', en: 'Testing & store' },
    'stage.4': { de: 'Verfügbar', en: 'Available' },
    'stage.label': { de: 'Fortschritt', en: 'Progress' },
    'd.status': { de: 'Aktueller Stand', en: 'Current status' },
    'd.eta': { de: 'Geplante Lieferung', en: 'Planned delivery' },
    'd.features': { de: 'Das kann es', en: 'What it does' },
    'd.where': { de: 'Wo erhältlich', en: 'Where to get it' },
    'd.platform': { de: 'Plattform', en: 'Platform' },
    'd.more': { de: 'Mehr Details', en: 'More details' },
    'd.github': { de: 'Quellcode auf GitHub', en: 'Source on GitHub' },
    'd.feedback': { de: 'Feedback geben', en: 'Give feedback' },
    'd.disclaimer': { de: 'Termine sind Zielwerte, keine Zusagen – wir entwickeln neben dem Beruf.', en: 'Dates are targets, not promises – we build this alongside our jobs.' },
    'd.liveNote': { de: 'Veröffentlicht und sofort nutzbar.', en: 'Released and ready to use.' },
    'd.nudge': { de: 'Gefällt dir das Projekt? Mit deiner Unterstützung können wir schneller liefern.', en: 'Like this project? With your support we can deliver faster.' },
    'd.close': { de: 'Schließen', en: 'Close' },
    'tl.liveCap': { de: '{n} fertige Tools – jetzt installierbar', en: '{n} finished tools – install now' },
    'tl.now': { de: 'Heute', en: 'Today' },
    'tl.nowSub': { de: 'Jetzt nutzbar', en: 'Usable now' },
    'tl.later': { de: 'Später / offen', en: 'Later / open' },
    'tl.laterSub': { de: 'Noch ohne festen Termin', en: 'No fixed date yet' },
    'empty.t': { de: 'Dazu haben wir (noch) nichts gefunden.', en: 'We have not found anything for that (yet).' },
    'empty.d': { de: 'Probiere einen anderen Filter oder Suchbegriff.', en: 'Try another filter or search term.' },
    'load.err': { de: 'Die Projektliste konnte nicht geladen werden. Bitte später erneut versuchen.', en: 'The project list could not be loaded. Please try again later.' }
  };
  function s(key, vars) {
    var str = pick(S[key]) || key;
    if (vars) Object.keys(vars).forEach(function (k) { str = str.replace('{' + k + '}', vars[k]); });
    return str;
  }
  var MONTHS = {
    de: ['Januar – März', 'April – Juni', 'Juli – September', 'Oktober – Dezember'],
    en: ['January – March', 'April – June', 'July – September', 'October – December']
  };

  /* ---------- Zustand ---------- */
  var data = null;
  var projects = [];
  /* Reihenfolge = Reihenfolge der Filter und Abschnitte. Neue Art: hier + Farbe in style.css + Texte oben ergänzen. */
  var TYPES = ['vr', 'android', 'game', 'desktop', 'extension'];
  var TYPE_ICON = { vr: 'vr', android: 'phone', game: 'gamepad', desktop: 'monitor', extension: 'puzzle' };
  var TAGS_COLLAPSED = 8;
  var IS_EDGE = /\bEdg(e|A|iOS)?\//.test(navigator.userAgent || '');
  var state = { type: 'all', status: 'all', q: '', tags: [], tagsOpen: false };
  var tagMap = {};
  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var drawer = null;

  function esc(str) {
    return String(str == null ? '' : str).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function typeIcon(type) { return TYPE_ICON[type] || 'grid'; }
  function typeLabel(type) { return S['type.' + type] ? s('type.' + type) : type; }
  function typePlural(type) { return S['f.' + type] ? s('f.' + type) : type; }

  /* ---------- Tags ---------- */
  /* Jedes Tag gibt es je Projekt auf Deutsch und Englisch (gleiche Reihenfolge). Der Schlüssel ist die englische Schreibweise. */
  function slug(t) { return String(t).toLowerCase().replace(/[^a-z0-9äöüß]+/g, '-').replace(/^-+|-+$/g, ''); }
  function buildTags() {
    tagMap = {};
    projects.forEach(function (p) {
      var de = (p.tags && p.tags.de) || [], en = (p.tags && p.tags.en) || [];
      p.tagKeys = [];
      for (var i = 0; i < Math.max(de.length, en.length); i++) {
        var e = en[i] || de[i], d = de[i] || en[i], k = slug(e);
        if (!k || p.tagKeys.indexOf(k) > -1) continue;
        if (!tagMap[k]) tagMap[k] = { key: k, de: d, en: e, n: 0 };
        tagMap[k].n++;
        p.tagKeys.push(k);
      }
    });
  }
  function tagLabel(k) { var t = tagMap[k]; return t ? (X.lang === 'en' ? t.en : t.de) : k; }
  function hasTags(p, keys) { return keys.every(function (k) { return (p.tagKeys || []).indexOf(k) > -1; }); }
  function tagList(p, cls) {
    if (!(p.tagKeys || []).length) return '';
    return '<ul class="tags' + (cls ? ' ' + cls : '') + '">' + p.tagKeys.map(function (k) {
      return '<li><button type="button" class="tag-btn" data-tag="' + esc(k) + '" aria-pressed="' + (state.tags.indexOf(k) > -1) + '">' + esc(tagLabel(k)) + '</button></li>';
    }).join('') + '</ul>';
  }
  function toggleTag(k) {
    var i = state.tags.indexOf(k);
    if (i > -1) state.tags.splice(i, 1); else state.tags.push(k);
  }
  function byId(id) { for (var i = 0; i < projects.length; i++) if (projects[i].id === id) return projects[i]; return null; }
  function parseEta(eta) {
    var m = /^(\d{4})-Q([1-4])$/.exec(eta || '');
    if (m) return { kind: 'q', year: +m[1], q: +m[2], key: +m[1] * 10 + +m[2] };
    if (eta === 'open') return { kind: 'open' };
    return null;
  }
  function etaLabel(e) { return e.kind === 'q' ? 'Q' + e.q + ' ' + e.year : s('eta.open'); }
  function etaRange(e) { return e.kind === 'q' ? MONTHS[X.lang][e.q - 1] + ' ' + e.year : s('eta.openLong'); }
  function supportUrl() {
    var list = (data.site && data.site.support) || [];
    return list.length ? list[0].url : 'https://www.patreon.com/c/exus541';
  }

  /* ---------- Bausteine ---------- */
  function projectIcon(p, big) {
    var cls = 'pi' + (big ? ' pi-lg' : '');
    if (p.icon) return '<img class="' + cls + '" src="' + esc(p.icon) + '" alt="" width="' + (big ? 64 : 48) + '" height="' + (big ? 64 : 48) + '" loading="lazy" decoding="async">';
    return '<span class="' + cls + ' pi-glyph t-' + p.type + '">' + icon(typeIcon(p.type)) + '</span>';
  }
  function badge(p) {
    return '<span class="badge badge-' + p.status + '"><i class="dot"></i>' + esc(s('status.' + p.status)) + '</span>';
  }
  var KIND_ICON = { chrome: 'chrome', edge: 'globe', web: 'globe', play: 'play', meta: 'vr', soon: 'clock' };
  function chip(a) {
    var label = esc(pick(a.label));
    var ic = icon(KIND_ICON[a.kind] || 'globe');
    if (a.url) return '<a class="chip chip-link" href="' + esc(a.url) + '" target="_blank" rel="noopener noreferrer">' + ic + '<span>' + label + '</span></a>';
    return '<span class="chip chip-soon">' + ic + '<span>' + label + (a.kind !== 'soon' ? ' · ' + esc(s('soon')) : '') + '</span></span>';
  }
  function stepper(p) {
    var html = '<ol class="stepper" aria-label="' + esc(s('stage.label')) + '">';
    for (var i = 1; i <= 4; i++) {
      var cls = i < p.stage ? 'done' : (i === p.stage ? 'current' : 'todo');
      if (p.stage === 4) cls = 'done';
      html += '<li class="' + cls + '"' + (i === p.stage ? ' aria-current="step"' : '') + '><span class="node">' + (cls === 'done' ? icon('check') : '') + '</span><span class="lbl">' + esc(s('stage.' + i)) + '</span></li>';
    }
    return html + '</ol>';
  }
  function previewOf(p) { return (X.lang === 'de' && p.previewDe) ? p.previewDe : p.preview; }
  /* Fundorte in der Reihenfolge der Daten; im Edge-Browser steht der Edge-Link vorn. */
  function availOrdered(p) {
    var list = (p.availability || []).slice();
    if (IS_EDGE) {
      var edge = list.filter(function (a) { return a.kind === 'edge' && a.url; });
      list = edge.concat(list.filter(function (a) { return edge.indexOf(a) === -1; }));
    }
    return list;
  }
  function primaryLink(p) {
    var list = availOrdered(p);
    for (var i = 0; i < list.length; i++) if (list[i].url) return list[i];
    return null;
  }
  /* Symbol der Art oben rechts auf der Karte (Farbe + Form zeigen: VR-App, Android-App, PC-Spiel, ...) */
  function typeBadge(p) {
    return '<span class="type-ico" role="img" aria-label="' + esc(typeLabel(p.type)) + '">' + icon(typeIcon(p.type)) + '</span>';
  }
  function typeMeta(p, all) {
    var plat = pick(p.platforms) || [];
    /* kleine Karten: bei Browser-Extensions reicht die Art (die Plattform zeigt der Store-Button) */
    var tail = all ? plat.join(' · ') : (p.type === 'extension' ? '' : (plat[0] || ''));
    return '<p class="meta"><span class="tlabel">' + esc(typeLabel(p.type)) + '</span>' + (tail ? ' · ' + esc(tail) : '') + '</p>';
  }

  function cardLarge(p) {
    var eta = parseEta(p.eta);
    var media = p.preview
      ? '<img src="' + esc(previewOf(p)) + '" alt="" loading="lazy" decoding="async" width="960" height="540">'
      : '<span class="ph t-' + p.type + '">' + icon(typeIcon(p.type)) + '</span>';
    var etaRow = eta
      ? '<div class="eta-row">' + icon('calendar') + '<strong>' + esc(eta.kind === 'q' ? s('eta.expected') + ' ' + etaLabel(eta) : s('eta.open')) + '</strong>' +
        (p.etaWhat && eta.kind === 'q' ? '<span>' + esc(pick(p.etaWhat)) + '</span>' : '') + '</div>'
      : '';
    return '<article class="card card-lg t-' + p.type + '">' + typeBadge(p) +
      '<div class="card-media">' + media + badge(p) + '</div>' +
      '<div class="card-body">' +
        '<div class="card-head">' + projectIcon(p) +
          '<div><h3><button type="button" class="card-open" data-open="' + esc(p.id) + '">' + esc(p.name) + '</button></h3>' +
          typeMeta(p, true) + '</div></div>' +
        '<p class="tagline">' + esc(pick(p.tagline)) + '</p>' +
        tagList(p) +
        etaRow + stepper(p) +
        '<div class="chips">' + availOrdered(p).map(chip).join('') + '</div>' +
      '</div></article>';
  }

  function cardSmall(p) {
    var link = primaryLink(p);
    var action = link
      ? '<a class="btn btn-sm btn-dark" href="' + esc(link.url) + '" target="_blank" rel="noopener noreferrer">' + icon(KIND_ICON[link.kind] || 'globe') + '<span>' + esc(pick(link.label)) + '</span></a>'
      : '';
    return '<article class="card card-sm t-' + p.type + '">' + typeBadge(p) +
      '<div class="card-head">' + projectIcon(p) +
        '<div><h3><button type="button" class="card-open" data-open="' + esc(p.id) + '">' + esc(p.name) + '</button></h3>' +
        typeMeta(p, false) + '</div></div>' +
      '<p class="tagline">' + esc(pick(p.tagline)) + '</p>' +
      tagList(p) +
      '<div class="card-foot">' + action + '<span class="more">' + esc(s('details')) + icon('arrow-right') + '</span></div>' +
    '</article>';
  }

  /* ---------- Filter ---------- */
  function haystack(p) {
    var parts = [p.name, p.id];
    ['type.', 'f.'].forEach(function (pre) { if (S[pre + p.type]) parts.push(S[pre + p.type].de, S[pre + p.type].en); });
    ['tagline', 'description'].forEach(function (k) { parts.push(p[k] && p[k].de, p[k] && p[k].en); });
    ['tags', 'features', 'platforms'].forEach(function (k) {
      if (p[k]) { parts = parts.concat(p[k].de || [], p[k].en || []); }
    });
    return parts.join(' ').toLowerCase();
  }
  function matches(p, ignore) {
    if (ignore !== 'type' && state.type !== 'all' && p.type !== state.type) return false;
    if (ignore !== 'status' && state.status !== 'all' && p.status !== state.status) return false;
    if (ignore !== 'tags' && state.tags.length && !hasTags(p, state.tags)) return false;
    if (state.q && haystack(p).indexOf(state.q.toLowerCase()) === -1) return false;
    return true;
  }
  function presentTypes() {
    var extra = [];
    projects.forEach(function (p) { if (TYPES.indexOf(p.type) === -1 && extra.indexOf(p.type) === -1) extra.push(p.type); });
    return TYPES.concat(extra).filter(function (t) { return projects.some(function (p) { return p.type === t; }); });
  }

  function renderFilters() {
    var types = ['all'].concat(presentTypes());
    var statuses = ['all', 'live', 'beta', 'dev'];
    function count(kind, val) {
      return projects.filter(function (p) {
        if (!matches(p, kind)) return false;
        return val === 'all' || p[kind] === val;
      }).length;
    }
    var th = '', sh = '', tg = '';
    types.forEach(function (t) {
      var cls = t === 'all' ? 'fchip' : 'fchip t-' + t;
      var dot = t === 'all' ? '' : '<span class="ficon">' + icon(typeIcon(t)) + '</span>';
      th += '<button type="button" class="' + cls + '" data-ftype="' + t + '" aria-pressed="' + (state.type === t) + '">' + dot + esc(t === 'all' ? s('f.all') : typePlural(t)) + '<em>' + count('type', t) + '</em></button>';
    });
    statuses.forEach(function (t) {
      var label = t === 'all' ? s('f.all') : s('status.' + t);
      sh += '<button type="button" class="fchip" data-fstatus="' + t + '" aria-pressed="' + (state.status === t) + '">' + esc(label) + '<em>' + count('status', t) + '</em></button>';
    });

    /* Tags: die häufigsten zuerst; die übrigen klappen auf ("Alle Tags") */
    var keys = Object.keys(tagMap).sort(function (a, b) {
      return (tagMap[b].n - tagMap[a].n) || tagLabel(a).localeCompare(tagLabel(b), X.lang);
    });
    var shown = state.tagsOpen ? keys : keys.filter(function (k, i) { return i < TAGS_COLLAPSED || state.tags.indexOf(k) > -1; });
    shown.forEach(function (k) {
      var on = state.tags.indexOf(k) > -1;
      var n = projects.filter(function (p) { return matches(p, 'tags') && hasTags(p, state.tags.concat(on ? [] : [k])); }).length;
      tg += '<button type="button" class="fchip fchip-tag" data-ftag="' + esc(k) + '" aria-pressed="' + on + '"' + (!on && !n ? ' disabled' : '') + '>' + esc(tagLabel(k)) + '<em>' + n + '</em></button>';
    });
    if (keys.length > TAGS_COLLAPSED) {
      tg += '<button type="button" class="link-btn" data-tags-toggle aria-expanded="' + state.tagsOpen + '">' + esc(state.tagsOpen ? s('tags.less') : s('tags.more', { n: keys.length })) + '</button>';
    }
    $('#filter-type').innerHTML = th;
    $('#filter-status').innerHTML = sh;
    $('#filter-tags').innerHTML = tg;
  }

  /* Kacheln einer Gruppe in einem Raster: gleiche Arten stehen beieinander (Reihenfolge der Arten, dann Reihenfolge in projects.json) */
  function gridOf(list, cardFn, gridCls) {
    var sorted = list.slice().sort(function (a, b) {
      var ia = TYPES.indexOf(a.type), ib = TYPES.indexOf(b.type);
      return ((ia < 0 ? 99 : ia) - (ib < 0 ? 99 : ib)) || ((a.order || 0) - (b.order || 0));
    });
    return '<div class="grid ' + gridCls + '">' + sorted.map(cardFn).join('') + '</div>';
  }

  var firstRender = true;
  function renderGrid() {
    var list = projects.filter(function (p) { return matches(p); });
    var works = list.filter(function (p) { return p.status !== 'live'; });
    var live = list.filter(function (p) { return p.status === 'live'; });
    var html = '';
    if (works.length) {
      html += '<section class="group" aria-labelledby="g-works"><div class="group-head"><h3 id="g-works">' + esc(s('g.works.t')) + '</h3><p>' + esc(s('g.works.d')) + '</p></div>' +
        gridOf(works, cardLarge, 'grid-lg') + '</section>';
    }
    if (live.length) {
      html += '<section class="group" aria-labelledby="g-live"><div class="group-head"><h3 id="g-live">' + esc(s('g.live.t')) + '</h3><p>' + esc(s('g.live.d')) + '</p></div>' +
        gridOf(live, cardSmall, 'grid-sm') + '</section>';
    }
    if (!list.length) {
      html = '<div class="empty"><p><strong>' + esc(s('empty.t')) + '</strong></p><p>' + esc(s('empty.d')) + '</p></div>';
    }
    var box = $('#results');
    box.innerHTML = html;
    box.classList.toggle('is-updating', !firstRender);
    firstRender = false;
    var n = list.length;
    $('#result-count').textContent = s(n === 1 ? 'count.one' : 'count.many', { n: n });
    var showReset = state.type !== 'all' || state.status !== 'all' || state.q || state.tags.length;
    $('#reset-filters').hidden = !showReset;
    observeReveal(box);
  }

  function syncUrl() {
    var qs = new URLSearchParams();
    if (state.type !== 'all') qs.set('typ', state.type);
    if (state.status !== 'all') qs.set('status', state.status);
    if (state.q) qs.set('q', state.q);
    if (state.tags.length) qs.set('tag', state.tags.join(','));
    var str = qs.toString();
    try { history.replaceState(null, '', location.pathname + (str ? '?' + str : '') + location.hash); } catch (e) { /* ignorieren */ }
  }
  function update() { renderFilters(); renderGrid(); syncUrl(); }

  function readUrl() {
    var qs = new URLSearchParams(location.search);
    var t = qs.get('typ'), st = qs.get('status');
    if (t === 'app') t = 'android'; /* alter Link */
    if (presentTypes().indexOf(t) > -1) state.type = t;
    if (['live', 'beta', 'dev'].indexOf(st) > -1) state.status = st;
    if (qs.get('q')) state.q = qs.get('q');
    if (qs.get('tag')) state.tags = qs.get('tag').split(',').filter(function (k) { return tagMap[k]; });
    $('#search').value = state.q;
  }

  /* ---------- Hero-Kennzahlen ---------- */
  function nextRelease() {
    var best = null;
    projects.forEach(function (p) {
      var e = parseEta(p.eta);
      if (e && e.kind === 'q' && (!best || e.key < best.key)) best = e;
    });
    if (!best) return null;
    var names = projects.filter(function (p) { var e = parseEta(p.eta); return e && e.key === best.key; }).map(function (p) { return p.name; });
    return { label: etaLabel(best), names: names };
  }
  function renderStats() {
    function n(st) { return projects.filter(function (p) { return p.status === st; }).length; }
    var next = nextRelease();
    var html = ['live', 'beta', 'dev'].map(function (st) {
      return '<li><button type="button" class="stat stat-' + st + '" data-stat="' + st + '"><b>' + n(st) + '</b><span>' + esc(s('stat.' + st)) + '</span></button></li>';
    }).join('');
    if (next) {
      html += '<li><a class="stat stat-next" href="#zeitplan"><b>' + esc(next.label) + '</b><span>' + esc(s('stat.next')) + ' · ' + esc(next.names.join(', ')) + '</span></a></li>';
    }
    $('#hero-stats').innerHTML = html;
  }

  /* ---------- Zeitplan ---------- */
  function renderTimeline() {
    var now = projects.filter(function (p) { return p.status === 'live' || p.status === 'beta'; });
    var quarters = {};
    var open = [];
    projects.forEach(function (p) {
      var e = parseEta(p.eta);
      if (!e) return;
      if (e.kind === 'open') { open.push(p); return; }
      (quarters[e.key] = quarters[e.key] || { e: e, items: [] }).items.push(p);
    });
    var keys = Object.keys(quarters).sort();
    var cols = [];
    var monthYear = new Date().toLocaleDateString(X.lang === 'de' ? 'de-DE' : 'en-GB', { month: 'long', year: 'numeric' });
    var nowBeta = now.filter(function (p) { return p.status !== 'live'; });
    var nowLive = now.filter(function (p) { return p.status === 'live'; });
    cols.push({ cls: 'now', title: s('tl.now'), sub: monthYear + ' · ' + s('tl.nowSub'), items: nowBeta.map(function (p) { return { p: p, what: s('status.' + p.status) }; }), avatars: nowLive });
    keys.forEach(function (k) {
      var q = quarters[k];
      cols.push({ cls: 'q', title: etaLabel(q.e), sub: etaRange(q.e), items: q.items.map(function (p) { return { p: p, what: pick(p.etaWhat) }; }) });
    });
    if (open.length) cols.push({ cls: 'open', title: s('tl.later'), sub: s('tl.laterSub'), items: open.map(function (p) { return { p: p, what: s('status.' + p.status) }; }) });
    var html = cols.map(function (c) {
      var list = c.items.map(function (it) {
        return '<li><button type="button" class="tl-item" data-open="' + esc(it.p.id) + '">' + projectIcon(it.p) + '<span><b>' + esc(it.p.name) + '</b><small>' + esc(it.what) + '</small></span></button></li>';
      }).join('');
      var avatars = '';
      if (c.avatars && c.avatars.length) {
        avatars = '<div class="tl-live"><p>' + esc(s('tl.liveCap', { n: c.avatars.length })) + '</p><div class="tl-avatars">' +
          c.avatars.map(function (p) {
            return '<button type="button" class="tl-avatar" data-open="' + esc(p.id) + '" title="' + esc(p.name) + '" aria-label="' + esc(p.name) + '">' + projectIcon(p) + '</button>';
          }).join('') + '</div></div>';
      }
      return '<li class="tl-col tl-' + c.cls + '"><span class="tl-node" aria-hidden="true"></span><h3>' + esc(c.title) + '</h3><p class="tl-sub">' + esc(c.sub) + '</p><ul class="tl-list">' + list + '</ul>' + avatars + '</li>';
    }).join('');
    var box = $('#timeline');
    box.style.setProperty('--cols', cols.length);
    box.innerHTML = html;
  }

  /* ---------- Detail-Panel ---------- */
  function openProject(id, silent) {
    var p = byId(id);
    if (!p || !drawer) return;
    var eta = parseEta(p.eta);
    var h = '<div class="drawer-panel">';
    h += '<header class="drawer-head">' + projectIcon(p, true) +
      '<div class="drawer-title"><div class="badges"><span class="tag tag-type t-' + esc(p.type) + '">' + esc(typeLabel(p.type)) + '</span>' + badge(p) + '</div>' +
      '<h2 id="drawer-title">' + esc(p.name) + '</h2></div>' +
      '<button type="button" class="icon-btn" data-close aria-label="' + esc(s('d.close')) + '">' + icon('x') + '</button></header>';
    h += '<div class="drawer-scroll">';
    if (p.preview) h += '<img class="drawer-img" src="' + esc(previewOf(p)) + '" alt="" decoding="async">';
    h += '<p class="d-lead">' + esc(pick(p.description)) + '</p>';
    h += tagList(p, 'd-tags');

    h += '<section class="d-block"><h3>' + esc(s('d.status')) + '</h3>' + stepper(p) +
      '<p class="muted">' + esc(p.stageNote ? pick(p.stageNote) : (p.status === 'live' ? s('d.liveNote') : '')) + '</p></section>';

    if (eta) {
      h += '<section class="d-block"><h3>' + esc(s('d.eta')) + '</h3><div class="eta-card">' + icon('calendar') +
        '<div><strong>' + esc(eta.kind === 'q' ? s('eta.expected') + ' ' + etaLabel(eta) : s('eta.open')) + '</strong>' +
        '<span>' + esc(etaRange(eta) + (p.etaWhat && eta.kind === 'q' ? ' · ' + pick(p.etaWhat) : '')) + '</span></div></div>' +
        '<p class="muted small">' + esc(s('d.disclaimer')) + '</p></section>';
    }

    if ((pick(p.features) || []).length) {
      h += '<section class="d-block"><h3>' + esc(s('d.features')) + '</h3><ul class="checks">' +
        pick(p.features).map(function (f) { return '<li>' + icon('check') + '<span>' + esc(f) + '</span></li>'; }).join('') + '</ul></section>';
    }

    h += '<section class="d-block"><h3>' + esc(s('d.where')) + '</h3><div class="where">' +
      availOrdered(p).map(function (a, i) {
        if (a.url) return '<a class="btn ' + (i === 0 ? 'btn-dark' : 'btn-ghost') + '" href="' + esc(a.url) + '" target="_blank" rel="noopener noreferrer">' + icon(KIND_ICON[a.kind] || 'globe') + '<span>' + esc(pick(a.label)) + '</span>' + icon('arrow-up-right', 'i-sm') + '</a>';
        return '<span class="where-soon">' + icon(KIND_ICON[a.kind] || 'clock') + '<span>' + esc(pick(a.label)) + (a.kind !== 'soon' ? ' · ' + esc(s('soon')) : '') + '</span></span>';
      }).join('') + '</div></section>';

    h += '<section class="d-block"><h3>' + esc(s('d.platform')) + '</h3><p>' + esc((pick(p.platforms) || []).join(' · ')) + '</p>' +
      (p.note ? '<p class="note">' + icon('alert') + '<span>' + esc(pick(p.note)) + '</span></p>' : '') + '</section>';

    var links = '';
    if (p.detail) links += '<a class="link" href="' + esc(p.detail) + '">' + icon('arrow-right') + esc(s('d.more')) + '</a>';
    if (p.github) links += '<a class="link" href="' + esc(p.github) + '" target="_blank" rel="noopener noreferrer">' + icon('github') + esc(s('d.github')) + '</a>';
    links += '<a class="link" href="feedback.html?projekt=' + encodeURIComponent(p.id) + '">' + icon('message') + esc(s('d.feedback')) + '</a>';
    h += '<div class="d-links">' + links + '</div>';

    h += '<aside class="nudge">' + icon('heart') + '<p>' + esc(s('d.nudge')) + '</p><a class="btn btn-warm btn-sm" href="' + esc(supportUrl()) + '" target="_blank" rel="noopener noreferrer">' + icon('patreon') + '<span>Patreon</span></a></aside>';
    h += '</div></div>';

    drawer.innerHTML = h;
    drawer.dataset.pid = id;
    if (!drawer.open) {
      drawer.showModal();
      document.documentElement.classList.add('no-scroll');
    }
    var sc = $('.drawer-scroll', drawer);
    if (sc) sc.scrollTop = 0;
    if (!silent) {
      try { history.replaceState(null, '', location.pathname + location.search + '#projekt-' + id); } catch (e) { /* ignorieren */ }
    }
  }
  function onDrawerClosed() {
    document.documentElement.classList.remove('no-scroll');
    drawer.dataset.pid = '';
    if (/^#projekt-/.test(location.hash)) {
      try { history.replaceState(null, '', location.pathname + location.search + '#loesungen'); } catch (e) { /* ignorieren */ }
    }
  }
  function openFromHash() {
    var m = /^#projekt-([\w-]+)$/.exec(location.hash);
    if (m && byId(m[1])) openProject(m[1], true);
  }

  /* ---------- Einblend-Animation ---------- */
  var io = null;
  function observeReveal(root) {
    var els = (root || document).querySelectorAll('.card, .reveal');
    if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      els.forEach(function (el) { el.classList.add('in'); });
      return;
    }
    if (!io) {
      io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    }
    els.forEach(function (el) { if (!el.classList.contains('in')) io.observe(el); });
  }

  /* ---------- Start ---------- */
  function renderAll() {
    if (!data) return;
    renderStats();
    renderFilters();
    renderGrid();
    renderTimeline();
    var d = $('#drawer');
    if (d && d.open && d.dataset.pid) openProject(d.dataset.pid, true);
  }

  function bind() {
    drawer = $('#drawer');
    drawer.addEventListener('close', onDrawerClosed);
    drawer.addEventListener('click', function (e) {
      if (e.target === drawer || e.target.closest('[data-close]')) drawer.close();
    });
    document.addEventListener('click', function (e) {
      var open = e.target.closest('[data-open]');
      if (open) { openProject(open.getAttribute('data-open')); return; }
      var ft = e.target.closest('[data-ftype]');
      if (ft) { state.type = ft.getAttribute('data-ftype'); update(); return; }
      var fs = e.target.closest('[data-fstatus]');
      if (fs) { state.status = fs.getAttribute('data-fstatus'); update(); return; }
      var ftag = e.target.closest('[data-ftag]');
      if (ftag) { toggleTag(ftag.getAttribute('data-ftag')); update(); return; }
      var tgl = e.target.closest('[data-tags-toggle]');
      if (tgl) { state.tagsOpen = !state.tagsOpen; renderFilters(); return; }
      var tag = e.target.closest('[data-tag]');
      if (tag) {
        toggleTag(tag.getAttribute('data-tag'));
        var fromDrawer = drawer && drawer.contains(tag);
        if (fromDrawer) drawer.close();
        update();
        if (fromDrawer) $('#loesungen').scrollIntoView({ behavior: 'smooth' });
        return;
      }
      var st = e.target.closest('[data-stat]');
      if (st) {
        state.status = st.getAttribute('data-stat'); state.type = 'all'; state.q = ''; state.tags = []; $('#search').value = '';
        update();
        $('#loesungen').scrollIntoView({ behavior: 'smooth' });
      }
    });
    $('#search').addEventListener('input', function (e) { state.q = e.target.value.trim(); update(); });
    $('#reset-filters').addEventListener('click', function () {
      state.type = 'all'; state.status = 'all'; state.q = ''; state.tags = [];
      $('#search').value = '';
      update();
    });
    window.addEventListener('hashchange', openFromHash);
  }

  function start() {
    bind();
    observeReveal(document);
    fetch('projects.json', { cache: 'no-cache' })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (json) {
        data = json;
        projects = json.projects.slice().sort(function (a, b) { return (a.order || 0) - (b.order || 0); });
        projects.forEach(function (p) { if (p.type === 'app') p.type = 'android'; }); /* alter Typname */
        buildTags();
        readUrl();
        renderAll();
        syncSupport();
        openFromHash();
      })
      .catch(function () {
        $('#results').innerHTML = '<div class="empty"><p>' + esc(s('load.err')) + '</p></div>';
      });
  }

  /* Weitere Spendenseiten aus projects.json neben dem Patreon-Button anzeigen */
  function syncSupport() {
    var box = $('#support-actions');
    if (!box || !data.site || !data.site.support) return;
    box.innerHTML = data.site.support.map(function (sp) {
      return '<a class="btn ' + (sp.primary ? 'btn-warm' : 'btn-ghost') + '" href="' + esc(sp.url) + '" target="_blank" rel="noopener noreferrer">' + icon(sp.icon || 'heart') + '<span>' + esc(pick(sp.label)) + '</span></a>';
    }).join('');
    var soc = $('#socials');
    if (soc && data.site.socials) {
      soc.innerHTML = data.site.socials.map(function (so) {
        return '<li><a href="' + esc(so.url) + '" target="_blank" rel="noopener noreferrer" aria-label="' + esc(so.label) + '">' + icon(so.icon) + '</a></li>';
      }).join('');
    }
  }

  X.onLang(function () {
    if (!data) return;
    renderAll();
    syncSupport();
  });
  X.ready(start);
})();
