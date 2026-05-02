import os
import glob

files = glob.glob(r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details\*.html")

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Give Feedback" not in content:
        # Add the Feedback button after the Patreon link in the sidebar
        feedback_btn = '\n                    <a href="https://forms.gle/YOUR_GOOGLE_FORM_ID" class="btn-block glass" style="text-decoration:none; color:var(--accent-color); border: 1px solid var(--accent-color);" target="_blank"><i data-lucide="message-square"></i> Give Feedback</a>'
        content = content.replace('Support on Patreon\n                    </a>', 'Support on Patreon\n                    </a>' + feedback_btn)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    print(f"Updated {file_path}")
