import os
import glob
import re

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details\*.html")

# Subpages nav is slightly different (Back to Hub)
# I'll add the icons there too if they have a nav with links.
# Actually, subpages nav only has "Back to Hub". 
# I'll just add the logo fix to them as I planned before.

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Ensure logo is linked and back-link is clean
    if '<a href="../index.html" class="logo">' not in content:
        content = content.replace('<div class="container">', '<div class="container">\n            <a href="../index.html" class="logo">exus<span>541</span></a>')
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")
