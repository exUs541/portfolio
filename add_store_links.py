import os

base_path = r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details"

links = {
    "siteblocker.html": "https://chromewebstore.google.com/detail/dbmhbnmbodpdkhhifkpckaafanchciej/",
    "webnote.html": "https://chromewebstore.google.com/detail/webnote-draw-highlight-st/iackibmejkkglddhagppoeifbfgchlni",
    "ytfilter.html": "https://chromewebstore.google.com/detail/mbdjpeppmemcbheedochgdejjoenijem/"
}

for filename, store_url in links.items():
    file_path = os.path.join(base_path, filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "Chrome Web Store" not in content:
            # Add the Install button before the GitHub button in the sidebar
            install_btn = f'<a href="{store_url}" class="btn-block btn-primary" style="background: white; color: black; border: 1px solid #ddd;" target="_blank"><i data-lucide="download"></i> Install from Web Store</a>\n                    '
            content = content.replace('<a href="https://github.com/exUs541/', install_btn + '<a href="https://github.com/exUs541/')
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filename}")
