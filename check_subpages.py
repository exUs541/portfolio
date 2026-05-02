import os
import glob

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details\*.html")

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Fix Logo Link (wrap the logo text in an <a> tag if not already)
    # The current logo might not exist in subpages yet, let's check index first.
    # Actually, in subpages the nav usually has "Back to Hub".
    # I'll check what's there.
    pass

# I'll view one subpage to be sure.
