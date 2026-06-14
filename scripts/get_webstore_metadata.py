import urllib.request
import re

urls = {
    "siteblocker": "https://chromewebstore.google.com/detail/dbmhbnmbodpdkhhifkpckaafanchciej/",
    "webnote": "https://chromewebstore.google.com/detail/webnote-draw-highlight-st/iackibmejkkglddhagppoeifbfgchlni",
    "tabmaster": "https://chromewebstore.google.com/detail/rename-tabs-change-tab-ic/mojpahfolammhpfnfdnghcnnpbaelnko",
    "ytfilter": "https://chromewebstore.google.com/detail/mbdjpeppmemcbheedochgdejjoenijem/",
    "sapsignavio": "https://chromewebstore.google.com/detail/sap-signavio-quick-switch/nnhnllclbckmcllglfomfllnkjolbcln"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

for name, url in urls.items():
    print(f"\nFetching {name} metadata...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Extract title
            title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
            title = title_match.group(1).strip() if title_match else "N/A"
            
            # Extract og:description
            desc_match = re.search(r'<meta[^>]*property=["\']og:description["\'][^>]*content=["\'](.*?)["\']', html)
            if not desc_match:
                desc_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*property=["\']og:description["\']', html)
            if not desc_match:
                desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', html)
            desc = desc_match.group(1).strip() if desc_match else "N/A"
            
            # Extract og:image (usually the promotional image or screenshot)
            img_match = re.search(r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\'](.*?)["\']', html)
            if not img_match:
                img_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*property=["\']og:image["\']', html)
            img = img_match.group(1).strip() if img_match else "N/A"
            
            print(f"Title: {title}")
            print(f"Description: {desc}")
            print(f"Image: {img}")
            
    except Exception as e:
        print(f"Error fetching {name}: {e}")
