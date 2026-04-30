import base64
import os

def get_base64_image(path):
    with open(path, "rb") as image_file:
        return f"data:image/png;base64,{base64.b64encode(image_file.read()).decode('utf-8')}"

base_path = r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery"

# Read files
with open(os.path.join(base_path, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

with open(os.path.join(base_path, "style.css"), "r", encoding="utf-8") as f:
    css = f.read()

with open(os.path.join(base_path, "main.js"), "r", encoding="utf-8") as f:
    js = f.read()

# Inline CSS and JS
html = html.replace('<link rel="stylesheet" href="style.css">', f'<style>\n{css}\n</style>')
html = html.replace('<script src="main.js"></script>', f'<script>\n{js}\n</script>')

# Remove nav for Google Sites embed? 
# Usually Google Sites has its own nav. But if the user wants the WHOLE thing, we keep it.
# However, many Google Sites embeds are in a frame, so fixed nav might look weird.
# Let's keep it for now as a full-page "landing" experience.

# Replace images with Base64
images = {
    "assets/siteblocker.png": get_base64_image(os.path.join(base_path, "assets", "siteblocker.png")),
    "assets/tabmaster.png": get_base64_image(os.path.join(base_path, "assets", "tabmaster.png")),
    "assets/webnote.png": get_base64_image(os.path.join(base_path, "assets", "webnote.png")),
    "assets/ytfilter.png": get_base64_image(os.path.join(base_path, "assets", "ytfilter.png")),
}

for rel_path, b64 in images.items():
    html = html.replace(rel_path, b64)

# Save the final file
output_path = os.path.join(base_path, "google_sites_embed.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Success! Created {output_path}")
