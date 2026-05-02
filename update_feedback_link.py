import os
import glob

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details\*.html")
form_url = "https://docs.google.com/forms/d/1luQQ0U15zBXotyz-EqBunhAbFrnN0J7rMvWpBcD87AM/viewform"

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update the YOUR_GOOGLE_FORM_ID placeholder or the old link
    content = content.replace("https://forms.gle/YOUR_GOOGLE_FORM_ID", form_url)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")
