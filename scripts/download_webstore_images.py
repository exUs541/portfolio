import urllib.request
import re
import os

extensions = {
    "siteblocker": "dbmhbnmbodpdkhhifkpckaafanchciej",
    "webnote": "iackibmejkkglddhagppoeifbfgchlni",
    "tabmaster": "mojpahfolammhpfnfdnghcnnpbaelnko",
    "ytfilter": "mbdjpeppmemcbheedochgdejjoenijem",
    "sapsignavio": "pffgkgglldjnmiakohgmogkalflfgbae"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

os.makedirs("assets", exist_ok=True)

for name, ext_id in extensions.items():
    url = f"https://chromewebstore.google.com/detail/{ext_id}"
    print(f"\nProcessing {name} ({ext_id})...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Find all googleusercontent URLs with params
            img_urls = re.findall(r'https://lh3\.googleusercontent\.com/[a-zA-Z0-9_-]+=[a-zA-Z0-9_-]+', html)
            
            # Filter for screenshots (typically contain w550-h350 or s550-w550-h350 or similar)
            screenshot_urls = []
            for img_url in img_urls:
                if any(param in img_url for param in ['w550', 'h350', 'w275', 'h175', 'w640', 'h400']):
                    # Get base URL by splitting at '='
                    base_url = img_url.split('=')[0]
                    high_res_url = f"{base_url}=w1280-h800"
                    if high_res_url not in screenshot_urls:
                        screenshot_urls.append(high_res_url)
            
            if screenshot_urls:
                target_url = screenshot_urls[0]
                print(f"Downloading screenshot from: {target_url}")
                
                # Download and save
                image_req = urllib.request.Request(target_url, headers=headers)
                with urllib.request.urlopen(image_req) as img_resp:
                    img_data = img_resp.read()
                    dest_path = f"assets/{name}.png"
                    with open(dest_path, "wb") as f:
                        f.write(img_data)
                    print(f"Saved to {dest_path} ({len(img_data)} bytes)")
            else:
                # If no screenshot is found, check for og:image
                og_img_match = re.search(r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\'](.*?)["\']', html)
                if og_img_match:
                    og_img_url = og_img_match.group(1)
                    print(f"Downloading og:image from: {og_img_url}")
                    image_req = urllib.request.Request(og_img_url, headers=headers)
                    with urllib.request.urlopen(image_req) as img_resp:
                        img_data = img_resp.read()
                        dest_path = f"assets/{name}.png"
                        with open(dest_path, "wb") as f:
                            f.write(img_data)
                        print(f"Saved og:image to {dest_path} ({len(img_data)} bytes)")
                else:
                    print("No screenshots or og:image found.")
                    
    except Exception as e:
        print(f"Error: {e}")
