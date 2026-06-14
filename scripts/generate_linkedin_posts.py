import os
import json
import google.generativeai as genai
from datetime import datetime

CHANGELOG_PATH = "changelog.json"
QUEUE_DIR = "linkedin-queue/pending"

STORE_LINKS = {
    "Google": "https://chromewebstore.google.com/detail/search-filter-site-blocke/dbmhbnmbodpdkhhifkpckaafanchciej",
    "SiteBlocker": "https://chromewebstore.google.com/detail/search-filter-site-blocke/dbmhbnmbodpdkhhifkpckaafanchciej",
    "TabMaster": "https://chromewebstore.google.com/detail/rename-tabs-change-tab-ic/mojpahfolammhpfnfdnghcnnpbaelnko",
    "YtFilter": "https://chromewebstore.google.com/detail/youtube-video-filter-enha/mojpahfolammhpfnfdnghcnnpbaelnko",
    "WebNote": "https://chromewebstore.google.com/detail/webnotes-simple-notes-on/iackibmejkkglddhagppoeifbfgchlni",
    "SAP-Signavio": "https://chromewebstore.google.com/detail/sap-signavio-quick-switch/pffgkgglldjnmiakohgmogkalflfgbae"
}

def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except Exception as e:
                print(f"Error loading {path}: {e}")
                return default
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_gemini_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: Kein GEMINI_API_KEY gefunden!")
        return None
    genai.configure(api_key=api_key)
    # Verwende das empfohlene neuere Modell
    return genai.GenerativeModel('gemini-2.5-flash')

def find_store_link(display_name):
    clean_name = display_name.lower().replace(" ", "").replace("-", "").replace("&", "")
    for key, val in STORE_LINKS.items():
        clean_key = key.lower().replace(" ", "").replace("-", "").replace("&", "")
        if clean_key in clean_name or clean_name in clean_key:
            return val
    return None

def generate_weekly_summary_post():
    model = get_gemini_client()
    if not model:
        return
        
    changelog = load_json(CHANGELOG_PATH, {"updates": []})
    unposted_updates = [upd for upd in changelog["updates"] if not upd.get("posted", False)]
    
    if not unposted_updates:
        print("Keine ungeposteten Updates im Changelog gefunden. Überspringe Post-Generierung.")
        return
        
    grouped_updates = {}
    for upd in unposted_updates:
        name = upd["display_name"]
        commits_str = "\n".join(f"- {c}" for c in upd["commits"])
        if name not in grouped_updates:
            grouped_updates[name] = []
        grouped_updates[name].append(f"Version {upd['version']}:\n{commits_str}")
        
    updates_summary = ""
    links_section = ""
    for name, changes_list in grouped_updates.items():
        changes_str = "\n\n".join(changes_list)
        updates_summary += f"\nExtension: **{name}**\nChanges:\n{changes_str}\n"
        store_link = find_store_link(name)
        if store_link:
            links_section += f"📥 {name} Chrome Web Store: {store_link}\n"
            
    prompt = f"""
    Create a professional, highly engaging LinkedIn weekly update post summarizing the latest improvements and updates across our browser extensions.
    
    Here are the updates for each extension this week:
    {updates_summary}
    
    Guidelines:
    - Title: Start with a catchy, visionary weekly summary title (e.g., "Weekly Tech Digest: Polishing the Web Experience 🛠️", "Weekly Update: Elevating the Browser Experience", etc.).
    - Tone: Visionary, developer-centric, premium, focusing on UX, customization, productivity, and local-first solutions.
    - Format: Group the updates by extension. For each extension, provide a brief, engaging summary of what changed (based on the git logs provided). Keep it readable with bullet points.
    - Emojis: Use relevant emojis to make it visually structured and engaging.
    - Bold: Use Markdown **bolding** for extension names and key features.
    - Mention the company/brand name 'eXus541'.
    - Language: English.
    - Call to Action: Encourage users to update their extensions or try them out.
    - Links: Include the relevant Chrome Web Store links for the updated extensions and general links:
    {links_section}      🌐 Portfolio: https://exus541.github.io/portfolio/
      ☕ Support: https://www.patreon.com/cw/exUs541
    """
    
    try:
        response = model.generate_content(prompt)
        post_text = response.text
        
        date_str = datetime.now().strftime('%Y%m%d')
        post_folder = os.path.join(QUEUE_DIR, f"Weekly_Summary_{date_str}")
        os.makedirs(post_folder, exist_ok=True)
        
        with open(os.path.join(post_folder, "post.txt"), "w", encoding="utf-8") as f:
            f.write(post_text)
            
        print(f"SUCCESS: Wöchentlicher LinkedIn-Post generiert und gespeichert.")
        
        for upd in changelog["updates"]:
            if not upd.get("posted", False):
                upd["posted"] = True
        save_json(CHANGELOG_PATH, changelog)
        
    except Exception as e:
        print(f"Gemini API Fehler: {e}")

def generate_new_release_post():
    model = get_gemini_client()
    if not model:
        return
        
    ext_name = os.environ.get("PAYLOAD_EXTENSION_NAME")
    display_name = os.environ.get("PAYLOAD_DISPLAY_NAME")
    version = os.environ.get("PAYLOAD_VERSION")
    commits_raw = os.environ.get("PAYLOAD_COMMITS", "[]")
    
    try:
        commits = json.loads(commits_raw)
    except:
        commits = [commits_raw]
        
    commits_str = "\n".join(f"- {c}" for c in commits)
    store_link = find_store_link(display_name) or find_store_link(ext_name) or "https://exus541.github.io/portfolio/"
    
    prompt = f"""
    Create a professional, highly engaging LinkedIn announcement post for the LAUNCH of a brand new browser extension.
    
    Extension Name: {display_name} (v{version})
    Initial features & changes:
    {commits_str}
    
    Guidelines:
    - Title: Catchy, highly engaging announcement title (e.g., "Introducing {display_name}: A New Way to Control Your Browser 🚀").
    - Tone: Visionary, product-hunt-style, premium developer vibe, focusing on how this solves a real browser/UX problem.
    - Include Emojis and Hashtags.
    - Mention the company 'eXus541'.
    - Use Markdown **bolding** for emphasis.
    - Language: English.
    - Include these links at the end:
      📥 Chrome Web Store: {store_link}
      🌐 Portfolio: https://exus541.github.io/portfolio/
      ☕ Support: https://www.patreon.com/cw/exUs541
    """
    
    try:
        response = model.generate_content(prompt)
        post_text = response.text
        
        date_str = datetime.now().strftime('%Y%m%d')
        post_folder = os.path.join(QUEUE_DIR, f"New_App_{ext_name}_{date_str}")
        os.makedirs(post_folder, exist_ok=True)
        
        with open(os.path.join(post_folder, "post.txt"), "w", encoding="utf-8") as f:
            f.write(post_text)
            
        print(f"SUCCESS: LinkedIn Launch-Post für {display_name} generiert und gespeichert.")
        
    except Exception as e:
        print(f"Gemini API Fehler: {e}")

def main():
    mode = os.environ.get("MODE")
    if mode == "weekly":
        generate_weekly_summary_post()
    else:
        is_new = os.environ.get("PAYLOAD_IS_NEW", "false")
        if is_new.lower() == "true":
            generate_new_release_post()
        else:
            print("Kein neuer App-Post nötig (is_new == false).")

if __name__ == "__main__":
    main()
