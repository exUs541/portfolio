import os
import glob
import re

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\*.html")

# Define the corrected nav with Patreon
new_nav = '''            <div class="nav-links">
                <a href="index.html#extensions" title="Extensions"><i data-lucide="puzzle"></i></a>
                <a href="roadmap.html" title="Roadmap"><i data-lucide="map"></i></a>
                <a href="index.html#feedback" title="Feedback"><i data-lucide="message-square"></i></a>
                <a href="index.html#about" title="About"><i data-lucide="info"></i></a>
                <a href="index.html#socials" title="Socials"><i data-lucide="share-2"></i></a>
                <a href="https://www.patreon.com/c/exus541" class="btn-primary" target="_blank" title="Support on Patreon"><i data-lucide="heart"></i></a>
            </div>'''

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the nav-links div
    content = re.sub(r'<div class="nav-links">.*?</div>', new_nav, content, flags=re.DOTALL)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")
