import urllib.request
import re
import os
from PIL import Image, ImageDraw, ImageFont

extensions = {
    "siteblocker": "dbmhbnmbodpdkhhifkpckaafanchciej",
    "webnote": "iackibmejkkglddhagppoeifbfgchlni",
    "tabmaster": "mojpahfolammhpfnfdnghcnnpbaelnko",
    "ytfilter": "mbdjpeppmemcbheedochgdejjoenijem",
    "sapsignavio": "pffgkgglldjnmiakohgmogkalflfgbae",
    "kleinanzeigen": "mnfgejplbhbkedcolciflhihgokpjnnd",
    "syncscrollpro": "mmnagcdibimlgbbdlkkdliojojignoda"
}

extension_names = {
    "siteblocker": "Search Filter & Site Blocker",
    "webnote": "WebNote",
    "tabmaster": "TabMaster",
    "ytfilter": "YouTube Video Filter",
    "sapsignavio": "SAP Signavio Quick Switch",
    "kleinanzeigen": "Kleinanzeigen Plus",
    "syncscrollpro": "Sync Scroll Pro"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

os.makedirs("assets", exist_ok=True)

def generate_placeholder(name, dest_path):
    print(f"Generating placeholder for {name}...")
    width, height = 1280, 800
    # Create dark-mode styled image
    image = Image.new("RGBA", (width, height), "#0e0d13")
    draw = ImageDraw.Draw(image)
    
    # Background grid pattern
    for i in range(0, width, 80):
        draw.line([(i, 0), (i, height)], fill="#16151c", width=1)
    for i in range(0, height, 80):
        draw.line([(0, i), (width, i)], fill="#16151c", width=1)
        
    # Draw central card-like frame
    draw.rectangle([(width//2 - 350, height//2 - 200), (width//2 + 350, height//2 + 200)], fill="#14131a", outline="#00f2ff", width=2)
    
    # Text
    title = extension_names.get(name, name.capitalize())
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 48)
        font_sub = ImageFont.truetype("arial.ttf", 28)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        
    # Draw text
    draw.text((width//2, height//2 - 30), title, fill="#ffffff", anchor="mm", font=font_title)
    draw.text((width//2, height//2 + 40), "Image Missing / Preview Coming Soon", fill="#8b8a9f", anchor="mm", font=font_sub)
    
    # Save as PNG
    image.convert("RGB").save(dest_path, "PNG")
    print(f"Saved placeholder to {dest_path}")

for name, ext_id in extensions.items():
    url = f"https://chromewebstore.google.com/detail/{ext_id}"
    dest_path = f"assets/{name}.png"
    print(f"\nProcessing {name} ({ext_id})...")
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Find the title to verify we aren't getting a generic page
            title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
            title = title_match.group(1).strip() if title_match else ""
            
            if "Chrome Web Store" in title and len(title) <= 20:
                print(f"Page returned 404 or generic Chrome Web Store title. Falling back to placeholder.")
                generate_placeholder(name, dest_path)
                continue
                
            # Find actual screenshot URLs (main extension screenshots are in lists of pattern [1, "lh3URL"])
            screenshot_urls = re.findall(r'\[\d+,\s*"(https://lh3\.googleusercontent\.com/[a-zA-Z0-9_-]+)"\]', html)
            
            if screenshot_urls:
                target_url = f"{screenshot_urls[0]}=w1280-h800"
                print(f"Downloading actual screenshot from: {target_url}")
                
                image_req = urllib.request.Request(target_url, headers=headers)
                with urllib.request.urlopen(image_req) as img_resp:
                    img_data = img_resp.read()
                    with open(dest_path, "wb") as f:
                        f.write(img_data)
                    print(f"Saved actual screenshot to {dest_path} ({len(img_data)} bytes)")
            else:
                # If no screenshot list matches, let's look for og:image fallback (only if not default CWS image)
                og_img_match = re.search(r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\'](.*?)["\']', html)
                if og_img_match and "chrome_web_store_v2" not in og_img_match.group(1):
                    og_img_url = og_img_match.group(1)
                    print(f"Downloading fallback og:image from: {og_img_url}")
                    image_req = urllib.request.Request(og_img_url, headers=headers)
                    with urllib.request.urlopen(image_req) as img_resp:
                        img_data = img_resp.read()
                        with open(dest_path, "wb") as f:
                            f.write(img_data)
                        print(f"Saved fallback og:image to {dest_path} ({len(img_data)} bytes)")
                else:
                    print("No actual screenshots or og:image found. Falling back to placeholder.")
                    generate_placeholder(name, dest_path)
                    
    except Exception as e:
        print(f"Error processing {name}: {e}. Falling back to placeholder.")
        generate_placeholder(name, dest_path)
