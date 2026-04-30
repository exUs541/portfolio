import os
import glob

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details\*.html")

youtube_link = 'https://www.youtube.com/channel/UC09y7qjqBbVcTCWtg1l8j0A'

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Add YouTube to Sidebar
    if youtube_link not in content:
        content = content.replace(
            '<a href="https://www.patreon.com/c/exus541" class="btn-block btn-patreon" target="_blank">',
            f'<a href="{youtube_link}" class="btn-block glass" style="text-decoration:none; color:white;" target="_blank"><i data-lucide="youtube"></i> YouTube Channel</a>\n                    <a href="https://www.patreon.com/c/exus541" class="btn-block btn-patreon" target="_blank">'
        )
    
    # 2. Add GitHub Stars Badge near Title
    if 'img.shields.io' not in content:
        # Determine repo name based on filename
        repo_name = os.path.basename(file_path).replace('.html', '')
        # Specific mappings if needed
        if repo_name == 'siteblocker': repo_name = 'Search-Optimizer'
        if repo_name == 'tabmaster': repo_name = 'Rename-Tabs'
        if repo_name == 'ytfilter': repo_name = 'YT-Filter'
        
        badge = f'\n            <img src="https://img.shields.io/github/stars/exUs541/{repo_name}?style=for-the-badge&color=00f2ff&labelColor=1a1a1a" alt="GitHub Stars" style="margin-top:1rem;">'
        content = content.replace('</h1>', '</h1>' + badge)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")
