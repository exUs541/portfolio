# exus541 – Portfolio

Helle, minimalistische Übersichtsseite für alle Lösungen von exus541: Browser-Extensions, VR-Apps und Apps –
mit Stand, Fundorten und geplantem Liefertermin. Läuft als statische Seite auf GitHub Pages
([exus541.github.io/portfolio](https://exus541.github.io/portfolio/)). Kein Build-Schritt, keine Frameworks.

## So pflegst du die Seite

**Alle Projekte stehen in [`projects.json`](projects.json).** Die Startseite (Karten, Filter, Zeitplan, Detail-Panel,
Kennzahlen im Hero) rendert sich komplett daraus. Neues Projekt = neuer Eintrag, Änderung am Stand = Feld ändern.

| Feld | Bedeutung |
| --- | --- |
| `type` | `extension`, `vr` oder `app` |
| `status` | `live` (verfügbar), `beta` (nutzbar, noch im Test), `dev` (in Entwicklung) |
| `stage` | Fortschrittsbalken: `1` Idee · `2` Entwicklung · `3` Test & Store · `4` Verfügbar |
| `eta` | geplanter Termin als Quartal `"2027-Q1"`, oder `"open"` (Termin offen). Bei `live` weglassen |
| `etaWhat` | wo es dann erscheint, z. B. „Meta Horizon Store“ |
| `availability` | Fundorte. `url: null` + `"soon": true` zeigt „… · geplant“ ohne Link. `kind`: `chrome`, `web`, `play`, `meta`, `soon` |
| `stageNote`, `note` | Satz zum aktuellen Stand bzw. Hinweis (z. B. Geräte-Einschränkung) |
| `icon`, `preview` | Bilder aus `assets/projects/` (`null` = Platzhalter-Symbol) |

Texte sind immer zweisprachig als `{ "de": "…", "en": "…" }`. Die Seite wählt die Sprache nach Browser-Einstellung,
der Besucher kann oben mit DE/EN umschalten.

**Spendenseiten:** unter `site.support` in `projects.json` weitere Einträge ergänzen (z. B. Ko-fi, PayPal.me,
GitHub Sponsors). Sie erscheinen automatisch als Buttons im Bereich „Unterstützen“.

**Texte der Startseite** (Hero, „Über uns“, „Unterstützen“) stehen direkt in [`index.html`](index.html) (Deutsch) und
als englische Übersetzung in [`site.js`](site.js) (Objekt `EN`, gleicher Schlüssel wie das `data-i18n`-Attribut).

## Dateien

| Datei | Zweck |
| --- | --- |
| `index.html`, `main.js` | Startseite und ihre Logik (Filter, Suche, Detail-Panel, Zeitplan) |
| `site.js` | gemeinsam: Sprache DE/EN, Icons, Kopfzeile |
| `style.css` | gesamtes Design (Farben als Variablen ganz oben) |
| `projects.json` | Daten aller Projekte, Spenden- und Social-Links |
| `roadmap.html`, `roadmap-data.json` | Feature-Wünsche der Extensions (wird von `roadmap-sync.yml` aus dem GitHub Project befüllt) |
| `feedback.html` | Formulare für Ideen und Fehler (Formspree) |
| `details/*.html`, `details/details.css` | Detailseiten der Extensions und Datenschutz |
| `extensions.html` | leitet auf `index.html?typ=extension` weiter (alte Links bleiben gültig) |

Direktlinks: `index.html?typ=vr`, `?status=dev`, `#projekt-nestwise` (öffnet das Detail-Panel).

## Automatisierung

`extension-release.yml` (in den Extension-Repos) löst per `repository_dispatch` den Workflow `update-portfolio.yml` aus.
`scripts/update_portfolio_site.py` schreibt dann den Changelog und legt bei neuen Extensions eine Detailseite sowie einen
Eintrag in `projects.json` an (mit Platzhaltertexten, bitte danach verfeinern).

## Lokal ansehen

```bash
python -m http.server 8765
```

Dann `http://localhost:8765` öffnen (die Seite lädt `projects.json` per `fetch`, ein Doppelklick auf die Datei reicht nicht).

## Technik

Reines HTML, CSS und JavaScript. Schriften: Inter und Outfit (Google Fonts). Icons als eingebettete SVGs, keine
externen Skripte.
