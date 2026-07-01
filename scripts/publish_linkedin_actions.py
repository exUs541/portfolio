"""
LinkedIn Post Publisher - API-basiert (kein Playwright, kein Cookie)
=====================================================================
Postet ausstehende Beitraege aus dem linkedin-queue/pending Verzeichnis
direkt ueber die offizielle LinkedIn UGC Posts API.

Benoetigt GitHub Secrets:
  - LINKEDIN_ACCESS_TOKEN: OAuth Access Token (59 Tage gueltig)
  - LINKEDIN_MEMBER_ID:    LinkedIn Member ID (z.B. dpwBhMvWBp)
"""

import os
import json
import shutil
import urllib.request
import urllib.error
from datetime import datetime

PENDING_DIR = "linkedin-queue/pending"
ARCHIVE_DIR = "linkedin-queue/archived"
API_URL = "https://api.linkedin.com/v2/ugcPosts"

os.makedirs(PENDING_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)


def get_next_post():
    if not os.path.exists(PENDING_DIR):
        return None, None
    for item in sorted(os.listdir(PENDING_DIR)):
        item_path = os.path.join(PENDING_DIR, item)
        if os.path.isdir(item_path):
            text_file = os.path.join(item_path, "post.txt")
            if os.path.exists(text_file):
                with open(text_file, "r", encoding="utf-8") as f:
                    text = f.read().strip()
                return item_path, text
    return None, None


def publish_post(text, access_token, member_id):
    author_urn = f"urn:li:person:{member_id}"

    post_body = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    payload = json.dumps(post_body).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202401"
    }

    try:
        req = urllib.request.Request(API_URL, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req) as res:
            if res.status in [200, 201]:
                response_data = json.loads(res.read().decode("utf-8"))
                post_id = response_data.get("id", "unknown")
                print(f"SUCCESS: Post veroeffentlicht! Post-ID: {post_id}")
                return True
            else:
                print(f"FEHLER: Unerwarteter Status {res.status}")
                return False
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"FEHLER beim LinkedIn-Upload (HTTP {e.code}): {error_body}")

        if e.code == 401:
            print("Der Access Token ist abgelaufen! Bitte erneuern:")
            print("  python linkedin_oauth_server.py")
        elif e.code == 403:
            print("Keine Berechtigung. Pruefe den LINKEDIN_ACCESS_TOKEN und LINKEDIN_MEMBER_ID.")

        return False
    except Exception as e:
        print(f"FEHLER: {e}")
        return False


def main():
    access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    member_id = os.environ.get("LINKEDIN_MEMBER_ID")

    if not access_token:
        print("ERROR: LINKEDIN_ACCESS_TOKEN fehlt in den Umgebungsvariablen.")
        return
    if not member_id:
        print("ERROR: LINKEDIN_MEMBER_ID fehlt in den Umgebungsvariablen.")
        return

    post_dir, text = get_next_post()

    if not post_dir or not text:
        print("Queue ist leer. Keine ausstehenden Posts.")
        return

    print(f"Post gefunden: {post_dir}")
    print(f"Inhalt (erste 100 Zeichen): {text[:100]}...")

    success = publish_post(text, access_token, member_id)

    if success:
        archive_name = os.path.basename(post_dir) + "_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        archived_path = os.path.join(ARCHIVE_DIR, archive_name)
        shutil.move(post_dir, archived_path)
        print(f"Post archiviert: {archived_path}")
    else:
        print("ERROR: Post konnte nicht veroeffentlicht werden. Bleibt in Queue.")


if __name__ == "__main__":
    main()
