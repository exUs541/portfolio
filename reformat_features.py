import os
import glob
import re

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details\*.html")

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace <li><strong>Key:</strong> Value</li> 
    # with <li><strong>Key</strong> <span>Value</span></li>
    # This regex handles cases with and without colons
    new_content = re.sub(
        r'<li><strong>(.*?)</strong>:?\s*(.*?)</li>', 
        r'<li><strong>\1</strong> <span>\2</span></li>', 
        content
    )
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path}")
