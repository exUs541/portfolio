import os
import glob
import re

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\*.html")

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Update Navigation link
    content = content.replace('href="index.html#extensions"', 'href="extensions.html"')
    content = content.replace('href="#extensions"', 'href="extensions.html"')
    
    # 2. Update Hero Button link (only in index.html)
    if "index.html" in file_path:
        content = content.replace('href="#extensions" class="btn-glow"', 'href="extensions.html" class="btn-glow"')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")
