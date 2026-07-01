import os
import time
import shutil
import re
from datetime import datetime
from playwright.sync_api import sync_playwright

PENDING_DIR = "linkedin-queue/pending"
ARCHIVE_DIR = "linkedin-queue/archived"
SESSION_DIR = "linkedin-queue/session_data"

os.makedirs(PENDING_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)

def to_unicode_bold(match):
    text = match.group(1)
    bold_map = {
        'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳', 'g': '𝗴', 'h': '𝗵', 'i': '𝗶', 'j': '𝗷', 'k': '𝗸', 'l': '𝗹', 'm': '𝗺', 'n': '𝗻', 'o': '𝗼', 'p': '𝗽', 'q': '𝗾', 'r': '𝗿', 's': '𝘀', 't': '𝘁', 'u': '𝘂', 'v': '𝘃', 'w': '𝘄', 'x': '𝘅', 'y': '𝘆', 'z': '𝘇',
        'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙', 'G': '𝗚', 'H': '𝗵', 'I': '𝗶', 'J': '𝗷', 'K': '𝗸', 'L': '𝗹', 'M': '𝗺', 'N': '𝗻', 'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥', 'S': '𝗦', 'T': '𝗧', 'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫', 'Y': '𝗬', 'Z': '𝗭',
        '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯', '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳', '8': '𝟴', '9': '𝟵'
    }
    return ''.join(bold_map.get(c, c) for c in text)

def get_next_post():
    if not os.path.exists(PENDING_DIR):
        return None, None, None
        
    for item in os.listdir(PENDING_DIR):
        item_path = os.path.join(PENDING_DIR, item)
        if os.path.isdir(item_path):
            text_file = os.path.join(item_path, "post.txt")
            if os.path.exists(text_file):
                with open(text_file, "r", encoding="utf-8") as f:
                    text = f.read().strip()
                images = []
                for file_in_dir in os.listdir(item_path):
                    if file_in_dir.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        images.append(os.path.join(item_path, file_in_dir))
                return item_path, text, images
    return None, None, None

def publish_post(text, images, cookie_val, company_id):
    print("Starte Playwright für den LinkedIn-Upload...")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir=SESSION_DIR,
                headless=True,
                args=["--disable-blink-features=AutomationControlled"]
            )
            
            if cookie_val:
                browser.add_cookies([{
                    'name': 'li_at',
                    'value': cookie_val,
                    'domain': '.www.linkedin.com',
                    'path': '/'
                }])
                
            page = browser.new_page()
            
            target_url = f"https://www.linkedin.com/company/{company_id}/admin/page-posts/published/?share=true"
            print(f"Navigiere zu: {target_url}")
            page.goto(target_url)
            
            time.sleep(5)
            page.screenshot(path="debug_01_loaded.png")
            
            if any(term in page.url.lower() for term in ["login", "checkpoint", "signup", "join"]):
                print("FEHLER: Nicht eingeloggt! Das li_at Cookie ist abgelaufen oder ungültig.")
                browser.close()
                return False

            print("Erfolgreich auf der Unternehmensseite eingeloggt. Erstelle Post...")
            
            page.wait_for_selector("div[role='textbox']", timeout=20000)
            text = re.sub(r'\*\*(.*?)\*\*', to_unicode_bold, text)
            
            page.fill("div[role='textbox']", text)
            time.sleep(2)
            page.screenshot(path="debug_03_text_filled.png")
            
            if images:
                print(f"Lade {len(images)} Bilder hoch...")
                with page.expect_file_chooser() as fc_info:
                    page.click("button[aria-label*='Media'], button[aria-label*='Medien'], button[aria-label*='Add media'], button[aria-label*='Medien hinzufügen']")
                file_chooser = fc_info.value
                file_chooser.set_files(images)
                
                time.sleep(3)
                try:
                    page.click("button:has-text('Next'), button:has-text('Weiter'), button:has-text('Done'), button:has-text('Fertig')", timeout=8000)
                except Exception as e:
                    print(f"Hinweis beim Foto-Bestätigen: {e}")
                time.sleep(3)
                
            page.screenshot(path="debug_04_ready_to_post.png")
            
            print("Sende Beitrag ab...")
            page.click("button.share-actions__primary-action", timeout=8000)
            
            time.sleep(7)
            page.screenshot(path="debug_05_after_post.png")
            
            print("SUCCESS: Post wurde erfolgreich auf LinkedIn veröffentlicht!")
            browser.close()
            return True
            
    except Exception as e:
        print(f"FEHLER beim LinkedIn-Upload: {e}")
        try:
            page.screenshot(path="debug_error.png")
        except:
            pass
        return False

def main():
    cookie_val = os.environ.get("LINKEDIN_COOKIE")
    company_id = os.environ.get("LINKEDIN_COMPANY_ID")
    
    if not cookie_val or not company_id:
        print("ERROR: LINKEDIN_COOKIE oder LINKEDIN_COMPANY_ID fehlt in den Umgebungsvariablen.")
        return
        
    post_dir, text, images = get_next_post()
    if post_dir and text:
        print(f"Post gefunden in Queue: {post_dir}")
        success = publish_post(text, images, cookie_val, company_id)
        
        if success:
            archive_name = os.path.basename(post_dir) + "_" + datetime.now().strftime("%Y%m%d_%H%M%S")
            archived_path = os.path.join(ARCHIVE_DIR, archive_name)
            shutil.move(post_dir, archived_path)
            print(f"SUCCESS: Post archiviert nach: {archived_path}")
        else:
            print("ERROR: Post konnte nicht veröffentlicht werden.")
    else:
        print("Queue ist leer. Keine ausstehenden Posts zu veröffentlichen.")

if __name__ == "__main__":
    main()
