import os
import glob
import re

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details\*.html")

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Remove colons inside <strong> tags
    content = re.sub(r'<strong>(.*?):?</strong>', r'<strong>\1</strong>', content)
    
    # 2. Ensure structure is <li><strong>Title</strong> <span>Description</span></li>
    # Handle cases where it might already have spans but with colons
    content = re.sub(r'<li><strong>(.*?)</strong>\s*:?\s*<span>(.*?)</span></li>', r'<li><strong>\1</strong> <span>\2</span></li>', content)
    content = re.sub(r'<li><strong>(.*?)</strong>:?\s*(.*?)</li>', r'<li><strong>\1</strong> <span>\2</span></li>', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")
