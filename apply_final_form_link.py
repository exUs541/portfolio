import os
import glob

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\*.html") + \
        glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details\*.html")

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf-42NVu126udKbEQaypBf1iKwih64SgVnQ3LqeCiuHvpSg_w/viewform"

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace placeholder URLs and old dev form links
    content = content.replace("https://forms.gle/YOUR_GOOGLE_FORM_ID", form_url)
    content = content.replace("https://docs.google.com/forms/d/1luQQ0U15zBXotyz-EqBunhAbFrnN0J7rMvWpBcD87AM/viewform", form_url)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")
