import os
import glob

# Path to the details folder
details_path = r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details\*.html"
files = glob.glob(details_path)

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Standard navigation for subpages
    new_nav = '''    <nav>
        <div class="container">
            <a href="../index.html" class="logo">exus<span>541</span></a>
            <a href="../index.html" class="back-link"><i data-lucide="arrow-left"></i> <span>Back to Hub</span></a>
        </div>
    </nav>'''

    # Pattern to find the navigation or the back link area
    if "<nav>" in content:
        start_nav = content.find("<nav>")
        end_nav = content.find("</nav>") + 6
        content = content[:start_nav] + new_nav + content[end_nav:]
    else:
        # If no nav, insert after body
        body_pos = content.find("<body>") + 6
        content = content[:body_pos] + "\n" + new_nav + content[body_pos:]

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed header in {file_path}")
