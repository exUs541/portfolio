import os
import json
import re
from datetime import datetime

CHANGELOG_PATH = "changelog.json"
INDEX_PATH = "index.html"
EXTENSIONS_PATH = "extensions.html"

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
    <title>{display_name} | exus541</title>
    <link rel="icon" type="image/png" href="../assets/favicon.png">
    <link rel="stylesheet" href="details.css">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
    <div class="background-glow"></div>
    <nav>
        <div class="container">
            <a href="../index.html" class="logo">exus<span>541</span></a>
            <a href="../index.html" class="back-link"><i data-lucide="arrow-left"></i> <span>Back to Hub</span></a>
        </div>
    </nav>

    <main class="container">
        <div class="detail-header">
            <h1>{display_name}</h1>
            <img src="https://img.shields.io/github/stars/exUs541/{extension_name}?style=for-the-badge&color=00f2ff&labelColor=1a1a1a" alt="GitHub Stars" style="margin-top:1rem;">
            <p>A brand new premium browser extension by exus541. Lightweight, powerful, and built to optimize your productivity.</p>
        </div>

        <div class="content-grid">
            <div class="main-content">
                <h2>Overview</h2>
                <p>Welcome to {display_name}. This extension is part of the exus541 productivity suite, designed to reclaim and enhance your web browsing experience.</p>

                <h2>Key Features</h2>
                <ul>
                    <li><strong>Smart Optimization</strong> <span><span>Optimized for performance and minimal battery usage.</span></span></li>
                    <li><strong>Privacy First</strong> <span><span>All data is processed locally and never stored on third-party servers.</span></span></li>
                    <li><strong>Modern UI</strong> <span><span>Clean, dark-mode styling aligned with modern design aesthetics.</span></span></li>
                </ul>
            </div>

            <div class="sidebar">
                <div class="sidebar-box glass">
                    <h3>Get Extension</h3>
                    <a href="https://chromewebstore.google.com/" class="btn-block btn-primary" style="background: white; color: black; border: 1px solid #ddd;" target="_blank"><i data-lucide="download"></i> Install from Web Store</a>
                    <a href="https://github.com/exUs541/{extension_name}" class="btn-block btn-github" target="_blank">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.042-1.416-4.042-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg> View on GitHub
                    </a>
                    <a href="https://www.patreon.com/c/exus541" class="btn-block btn-patreon" target="_blank">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M22.957 7.21c-.004-3.078-2.584-5.51-5.625-5.51s-5.51 2.432-5.51 5.51c0 3.037 2.473 5.51 5.51 5.51 3.041 0 5.629-2.432 5.625-5.51zM2.091 1.701v20.597h4.182V1.701H2.091z"/></svg> Support on Patreon
                    </a>
                    <a href="https://docs.google.com/forms/" class="btn-block glass" style="text-decoration:none; color:var(--accent-color); border: 1px solid var(--accent-color);" target="_blank"><i data-lucide="message-square"></i> Give Feedback</a>
                </div>
            </div>
        </div>
    </main>

    <footer>
        <div class="container">
            <a href="../index.html" class="logo">exus<span>541</span></a>
            <p>&copy; {datetime.now().year} exus541. Built with ❤️</p>
        </div>
    </footer>

    <script>lucide.createIcons();</script>
</body>
</html>
"""
    with open(details_file, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"SUCCESS: Detailseite {details_file} erstellt.")

def add_card_to_html(file_path, extension_name, display_name):
    if not os.path.exists(file_path):
        return
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if f"details/{extension_name.lower()}.html" in content:
        print(f"Card für {extension_name} existiert bereits in {file_path}. Überspringe.")
        return
        
    card_html = f"""                <!-- {extension_name} -->
                <div class="card glass">
                    <div class="card-image">
                        <img src="assets/{extension_name.lower()}.png" alt="{display_name} Preview" onerror="this.src='assets/siteblocker.png'">
                    </div>
                    <div class="card-content">
                        <h3>{display_name}</h3>
                        <p>A modern utility by exus541 to optimize your browser workflow.</p>
                        <div class="tags">
                            <span>Productivity</span>
                            <span>Utility</span>
                        </div>
                        <a href="details/{extension_name.lower()}.html" class="card-link">View Details <i data-lucide="arrow-right"></i></a>
                    </div>
                </div>
"""
    
    grid_pattern = r'(<div class="grid">)'
    if re.search(grid_pattern, content):
        updated_content = re.sub(grid_pattern, f'\\1\n{card_html}', content, count=1)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"SUCCESS: Card für {display_name} in {file_path} eingefügt.")
    else:
        print(f"ERROR: Konnte <div class=\"grid\"> in {file_path} nicht finden.")

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
    except:
        commits = [commits_raw]
        
    update_changelog(extension_name, display_name, version, commits)
    
    if is_new.lower() == "true":
        print("Erkenne neue Anwendung. Lege Portfolio-Einträge an...")
        create_details_page(extension_name, display_name)
        add_card_to_html(INDEX_PATH, extension_name, display_name)
        add_card_to_html(EXTENSIONS_PATH, extension_name, display_name)

if __name__ == "__main__":
    main()
