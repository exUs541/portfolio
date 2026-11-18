import os
import json
from datetime import datetime

CHANGELOG_PATH = "changelog.json"
PROJECTS_PATH = "projects.json"


def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except Exception as e:
                print(f"Error loading {path}: {e}")
                return default
    return default


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def update_changelog(extension_name, display_name, version, commits):
    changelog = load_json(CHANGELOG_PATH, {"updates": []})

    new_update = {
        "extension_name": extension_name,
        "display_name": display_name,
        "version": version,
        "commits": commits if isinstance(commits, list) else [commits],
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "posted": False
    }

    changelog["updates"].append(new_update)
    save_json(CHANGELOG_PATH, changelog)
    print(f"SUCCESS: Changelog aktualisiert für {display_name} v{version}.")


GITHUB_ICON = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true" style="fill:currentColor;stroke:none"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.44 9.8 8.21 11.39.6.11.79-.26.79-.58v-2.23c-3.34.73-4.04-1.42-4.04-1.42-.55-1.39-1.33-1.76-1.33-1.76-1.09-.75.08-.73.08-.73 1.2.08 1.84 1.24 1.84 1.24 1.07 1.83 2.81 1.3 3.49 1 .11-.78.42-1.3.76-1.6-2.67-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.18 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.29-1.55 3.3-1.23 3.3-1.23.66 1.66.24 2.88.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.61-2.81 5.63-5.48 5.92.43.37.82 1.1.82 2.22v3.29c0 .32.19.7.8.58A12 12 0 0 0 24 12c0-6.63-5.37-12-12-12Z"/></svg>'
PATREON_ICON = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true" style="fill:currentColor;stroke:none"><path d="M22.96 7.21c0-3.08-2.58-5.51-5.63-5.51s-5.51 2.43-5.51 5.51c0 3.04 2.47 5.51 5.51 5.51 3.04 0 5.63-2.43 5.63-5.51ZM2.09 1.7v20.6h4.18V1.7H2.09Z"/></svg>'
DOWNLOAD_ICON = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/></svg>'
ARROW_ICON = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="m12 19-7-7 7-7"/><path d="M19 12H5"/></svg>'


def create_details_page(extension_name, display_name):
    details_file = f"details/{extension_name.lower()}.html"
    if os.path.exists(details_file):
        print(f"Detailseite für {extension_name} existiert bereits. Überspringe Erstellung.")
        return

    os.makedirs("details", exist_ok=True)

    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{display_name} | exUs541</title>
    <link rel="icon" type="image/png" href="../assets/favicon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="details.css">
</head>
<body>
    <header class="site-header">
        <div class="container header-inner">
            <a href="../index.html" class="brand" aria-label="exUs541 – home">exUs<span>541</span></a>
            <div class="header-actions">
                <a href="../index.html#loesungen" class="btn btn-ghost btn-sm">{ARROW_ICON}<span>Back to overview</span></a>
            </div>
        </div>
    </header>

    <main class="container">
        <div class="detail-header">
            <span class="tag">Browser extension</span>
            <h1>{display_name}</h1>
            <p>A brand new browser extension by exUs541. Lightweight, powerful, and built to optimize your productivity.</p>
            <img src="https://img.shields.io/github/stars/exUs541/{extension_name}?style=for-the-badge&color=4f5bd5&labelColor=16181d" alt="GitHub Stars">
        </div>

        <div class="content-grid">
            <div class="main-content">
                <h2>Overview</h2>
                <p>Welcome to {display_name}. This extension is part of the exUs541 productivity suite, designed to reclaim and enhance your web browsing experience.</p>

                <h2>Key Features</h2>
                <ul>
                    <li><strong>Smart Optimization</strong> <span><span>Optimized for performance and minimal battery usage.</span></span></li>
                    <li><strong>Privacy First</strong> <span><span>All data is processed locally and never stored on third-party servers.</span></span></li>
                    <li><strong>Clean UI</strong> <span><span>Clear, modern styling that stays out of your way.</span></span></li>
                </ul>
            </div>

            <aside class="sidebar">
                <div class="sidebar-box">
                    <h3>Get Extension</h3>
                    <a href="https://chromewebstore.google.com/" class="btn btn-dark btn-block" target="_blank" rel="noopener noreferrer">{DOWNLOAD_ICON}<span>Install from Web Store</span></a>
                    <a href="https://github.com/exUs541/{extension_name}" class="btn btn-ghost btn-block" target="_blank" rel="noopener noreferrer">{GITHUB_ICON}<span>View on GitHub</span></a>
                    <a href="https://www.patreon.com/c/exus541" class="btn btn-warm btn-block" target="_blank" rel="noopener noreferrer">{PATREON_ICON}<span>Support on Patreon</span></a>
                </div>
            </aside>
        </div>
    </main>

    <footer class="site-footer">
        <div class="container">
            <div class="footer-inner">
                <div class="footer-links">
                    <a href="../index.html" class="brand" style="margin-right: 8px;">exUs<span>541</span></a>
                    <span>&copy; {datetime.now().year} exUs541. Built with care &ndash; in our spare time.</span>
                    <a href="../privacy.html">Privacy Policy</a>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>
"""
    with open(details_file, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"SUCCESS: Detailseite {details_file} erstellt.")


def add_project_entry(extension_name, display_name):
    """Legt das neue Projekt in projects.json an (die Startseite rendert sich daraus).

    Die Texte sind Platzhalter und sollten spaeter in projects.json verfeinert werden.
    """
    data = load_json(PROJECTS_PATH, None)
    if not data or "projects" not in data:
        print(f"ERROR: {PROJECTS_PATH} fehlt oder ist ungültig.")
        return

    pid = extension_name.lower()
    if any(p.get("id") == pid for p in data["projects"]):
        print(f"Projekt {pid} existiert bereits in {PROJECTS_PATH}. Überspringe.")
        return

    ext_orders = [p.get("order", 0) for p in data["projects"] if p.get("type") == "extension"]
    icon = f"assets/projects/{pid}-icon.webp"
    preview = f"assets/projects/{pid}-preview.webp"

    data["projects"].append({
        "id": pid,
        "order": (max(ext_orders) if ext_orders else 100) + 10,
        "type": "extension",
        "status": "live",
        "stage": 4,
        "name": display_name,
        "icon": icon if os.path.exists(icon) else None,
        "preview": preview if os.path.exists(preview) else None,
        "tagline": {
            "de": "Neue Browser-Extension von exUs541.",
            "en": "A new browser extension by exUs541."
        },
        "description": {
            "de": f"{display_name} ist eine schlanke Browser-Extension, die deinen Alltag im Browser erleichtert.",
            "en": f"{display_name} is a lightweight browser extension that makes everyday browsing easier."
        },
        "features": {"de": [], "en": []},
        "platforms": {"de": ["Chrome & Chromium-Browser"], "en": ["Chrome & Chromium browsers"]},
        "tags": {"de": ["Neu"], "en": ["New"]},
        "detail": f"details/{pid}.html",
        "availability": [
            {
                "kind": "chrome",
                "label": {"de": "Chrome Web Store", "en": "Chrome Web Store"},
                "url": "https://chromewebstore.google.com/"
            }
        ],
        "github": f"https://github.com/exUs541/{extension_name}"
    })
    save_json(PROJECTS_PATH, data)
    print(f"SUCCESS: Projekt {display_name} in {PROJECTS_PATH} eingetragen (Texte bitte später verfeinern).")


def main():
    extension_name = os.environ.get("PAYLOAD_EXTENSION_NAME")
    display_name = os.environ.get("PAYLOAD_DISPLAY_NAME")
    version = os.environ.get("PAYLOAD_VERSION")
    commits_raw = os.environ.get("PAYLOAD_COMMITS", "[]")
    is_new = os.environ.get("PAYLOAD_IS_NEW", "false")

    if not extension_name or not display_name or not version:
        print("ERROR: Fehlende Umgebungsvariablen für Portfolio-Update.")
        return

    try:
        commits = json.loads(commits_raw)
    except Exception:
        commits = [commits_raw]

    update_changelog(extension_name, display_name, version, commits)

    if is_new.lower() == "true":
        print("Erkenne neue Anwendung. Lege Portfolio-Einträge an...")
        create_details_page(extension_name, display_name)
        add_project_entry(extension_name, display_name)


if __name__ == "__main__":
    main()
