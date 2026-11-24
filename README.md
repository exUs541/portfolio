# exUs541 – Portfolio

Helle, minimalistische Übersichtsseite für alle Lösungen von exUs541: Browser-Extensions, VR-Apps und Apps –
mit Stand, Fundorten und geplantem Liefertermin. Läuft als statische Seite auf GitHub Pages
([exus541.github.io/portfolio](https://exus541.github.io/portfolio/)). Kein Build-Schritt, keine Frameworks.

## Kleine Änderungen selbst machen (ohne zusätzliche Programme)

Stand, Termin oder Store-Link eines Projekts änderst du direkt im Browser auf GitHub – ohne etwas zu installieren:

1. Öffne [`projects.json`](https://github.com/exUs541/portfolio/blob/main/projects.json) auf GitHub (eingeloggt) und klicke oben rechts auf das **Stift-Symbol** („Edit this file“).
2. Suche das Projekt (Strg+F nach dem Namen, z. B. `"id": "perspectives"`) und ändere die Felder (Beispiel unten).
3. Klicke auf **„Commit changes…“**, wähle **„Commit directly to the `main` branch“** und bestätige.
4. Nach etwa 1–2 Minuten ist die Seite aktualisiert (im Browser einmal Strg+F5 drücken).

**Beispiel „App ist jetzt veröffentlicht“** (so wurde Perspectives umgestellt):

- `"status": "dev"` → `"status": "live"`
- `"stage": 3` → `"stage": 4`
- die Zeilen `"eta": …` und `"etaWhat": …` löschen (bei `live` gibt es keinen Termin mehr)
- bei `availability` den Link eintragen: `"url": "https://…"` und `"soon": true` entfernen
- optional `stageNote` anpassen, z. B. „Version 1.0 ist im Meta Horizon Store veröffentlicht.“

**Worauf achten:** Anführungszeichen und Kommas müssen stimmen (nach jedem Eintrag ein Komma, nur nach dem letzten nicht).
Ist die Seite danach leer oder fehlen Karten, steckt dort ein Fehler. Dann in GitHub unter **History** die letzte Änderung
öffnen und mit **„Revert“** zurücknehmen – so geht nie etwas verloren.

Texte der Startseite stehen in `index.html` (Deutsch) und `site.js` (Englisch), siehe unten. Den Namen der Marke
(„exUs541“) gibt es in allen HTML-Dateien; für eine Umbenennung ist „Suchen und Ersetzen“ über alle Dateien nötig.

## So pflegst du die Seite

**Alle Projekte stehen in [`projects.json`](projects.json).** Die Startseite (Karten, Filter, Zeitplan, Detail-Panel,
Kennzahlen im Hero) rendert sich komplett daraus. Neues Projekt = neuer Eintrag, Änderung am Stand = Feld ändern.

| Feld | Bedeutung |
| --- | --- |
| `type` | Art, bestimmt Farbe, Filter und Abschnitt: `vr` (VR-App), `android` (Android-App), `game` (PC-Spiel), `desktop` (PC-Anwendung), `extension` (Browser-Extension). Eine Art erscheint auf der Seite, sobald es dazu ein Projekt gibt |
| `status` | `live` (verfügbar), `beta` (nutzbar, noch im Test), `dev` (in Entwicklung) |
| `stage` | Fortschrittsbalken: `1` Idee · `2` Entwicklung · `3` Test & Store · `4` Verfügbar |
| `eta` | geplanter Termin als Quartal `"2027-Q1"`, oder `"open"` (Termin offen). Bei `live` weglassen |
| `etaWhat` | wo es dann erscheint, z. B. „Meta Horizon Store“ |
| `availability` | Fundorte. `url: null` + `"soon": true` zeigt „… · geplant“ ohne Link. `kind`: `chrome`, `edge`, `web`, `play`, `meta`, `soon`. Wer die Seite im Edge-Browser öffnet, sieht den `edge`-Link zuerst. Auf den Kacheln zeigen `chrome` und `edge` nur kurze Buttons („Chrome“, „Edge“), der volle `label` steht im Tooltip und im Detailfenster |
| `stageNote`, `note` | Satz zum aktuellen Stand bzw. Hinweis (z. B. Geräte-Einschränkung) |
| `tags` | Stichwörter, nach denen man filtern und suchen kann, je Sprache gleich viele und in gleicher Reihenfolge, z. B. `"de": ["Fokus", "Spiel"], "en": ["Focus", "Game"]`. Gleiche Tags bei mehreren Projekten werden automatisch zusammengefasst |
| `icon`, `preview` | Bilder aus `assets/projects/` (`null` = Platzhalter-Symbol) |

Texte sind immer zweisprachig als `{ "de": "…", "en": "…" }`. Die Seite wählt die Sprache nach Browser-Einstellung,
der Besucher kann oben über das Sprach-Symbol wechseln.

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
| `roadmap.html`, `roadmap-data.json` | Feature-Wünsche der Extensions (wird von Hand gepflegt) |
| `feedback.html` | Formulare für Ideen und Fehler (Formspree) |
| `details/*.html`, `details/details.css` | Detailseiten der Extensions und Datenschutz |
| `extensions.html` | leitet auf `index.html?typ=extension` weiter (alte Links bleiben gültig) |

Direktlinks: `index.html?typ=vr`, `?status=dev`, `#projekt-nestwise` (öffnet das Detail-Panel).

## Automatisierung

`release.yml` (in den Extension-Repos) löst per `repository_dispatch` den Workflow `update-portfolio.yml` aus.
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
