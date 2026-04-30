import os
import glob

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details\*.html")

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        new_content = content.replace(
            '<link rel="stylesheet" href="details.css">',
            '<link rel="icon" type="image/png" href="../assets/favicon.png">\n    <link rel="stylesheet" href="details.css">'
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path}")
