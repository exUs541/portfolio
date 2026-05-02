import os
import glob
import re

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\*.html")

patreon_svg = '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M15.386 0.501c-4.139 0-7.511 3.372-7.511 7.511 0 4.139 3.372 7.511 7.511 7.511s7.511-3.372 7.511-7.511c0-4.139-3.372-7.511-7.511-7.511zM0 0.501v22.998h4.28v-22.998h-4.28z"/></svg>'

new_nav = f'''            <div class="nav-links">
                <a href="index.html#extensions"><i data-lucide="puzzle"></i> <span>Extensions</span></a>
                <a href="roadmap.html"><i data-lucide="map"></i> <span>Roadmap</span></a>
                <a href="index.html#feedback"><i data-lucide="message-square"></i> <span>Feedback</span></a>
                <a href="index.html#about"><i data-lucide="info"></i> <span>About</span></a>
                <a href="index.html#socials"><i data-lucide="share-2"></i> <span>Socials</span></a>
                <a href="https://www.patreon.com/c/exus541" class="btn-primary" target="_blank">{patreon_svg} <span>Support on Patreon</span></a>
            </div>'''

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the nav-links div
    content = re.sub(r'<div class="nav-links">.*?</div>', new_nav, content, flags=re.DOTALL)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")
