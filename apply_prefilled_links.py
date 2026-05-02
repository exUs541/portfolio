import os

base_path = r"c:\Users\enmel\Documents\Antigravity\ExtensionGallery\details"

links = {
    "tabmaster.html": "https://docs.google.com/forms/d/e/1FAIpQLSf-42NVu126udKbEQaypBf1iKwih64SgVnQ3LqeCiuHvpSg_w/viewform?usp=pp_url&entry.1537911196=Rename+Tabs+%26+Change+Tab+Icons:+TabMaster",
    "siteblocker.html": "https://docs.google.com/forms/d/e/1FAIpQLSf-42NVu126udKbEQaypBf1iKwih64SgVnQ3LqeCiuHvpSg_w/viewform?usp=pp_url&entry.1537911196=Search+Filter+%26+Site+Blocker+-+Clean+Search+Results",
    "webnote.html": "https://docs.google.com/forms/d/e/1FAIpQLSf-42NVu126udKbEQaypBf1iKwih64SgVnQ3LqeCiuHvpSg_w/viewform?usp=pp_url&entry.1537911196=WebNote:+Draw,+Highlight+%26+Sticky+Notes",
    "ytfilter.html": "https://docs.google.com/forms/d/e/1FAIpQLSf-42NVu126udKbEQaypBf1iKwih64SgVnQ3LqeCiuHvpSg_w/viewform?usp=pp_url&entry.1537911196=YouTube+Video+Filter+(Enhanced)"
}

generic_url = "https://docs.google.com/forms/d/e/1FAIpQLSf-42NVu126udKbEQaypBf1iKwih64SgVnQ3LqeCiuHvpSg_w/viewform"

for filename, prefilled_url in links.items():
    file_path = os.path.join(base_path, filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace the generic URL with the specific pre-filled one
        content = content.replace(generic_url, prefilled_url)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename}")
