"""
LinkedIn Post Publisher - API-basiert (kein Playwright, kein Cookie)
=====================================================================
Veroeffentlicht Beitraege direkt ueber die offizielle LinkedIn UGC Posts API.

Was gepostet wird:
  - Wochen-Zusammenfassung (Weekly_Summary_*): NUR der Post, den
    generate_linkedin_posts.py in genau diesem Lauf erzeugt hat (Pfad in der
    Umgebungsvariable WEEKLY_POST_DIR). Gibt es keine neuen Updates, wird kein
    Post erzeugt und somit auch nichts gepostet. Aeltere Weekly_Summary-Reste
    in linkedin-queue/pending werden nie gepostet, sondern nach archived/
    verschoben (Suffix _skipped).
  - Andere Queue-Eintraege (z.B. New_App_*): wie bisher der aelteste pro Lauf.

Schlaegt das Veroeffentlichen fehl (z.B. abgelaufener Token), endet das Skript
mit Exit-Code 1, damit der Workflow-Lauf rot wird und nichts committed wird.

Benoetigt GitHub Secrets:
  - LINKEDIN_ACCESS_TOKEN: OAuth Access Token (59 Tage gueltig)
  - LINKEDIN_MEMBER_ID:    LinkedIn Member ID (z.B. dpwBhMvWBp)
"""

import os
import sys
import json
import shutil
import urllib.request
import urllib.error
from datetime import datetime

PENDING_DIR = "linkedin-queue/pending"
ARCHIVE_DIR = "linkedin-queue/archived"
API_URL = "https://api.linkedin.com/v2/ugcPosts"
WEEKLY_PREFIX = "Weekly_Summary_"

os.makedirs(PENDING_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)


def read_post(post_dir):
    text_file = os.path.join(post_dir, "post.txt")
    if not os.path.exists(text_file):
        return None
    with open(text_file, "r", encoding="utf-8") as f:
        return f.read().strip()


def archive_post(post_dir, suffix=""):
    archive_name = os.path.basename(post_dir) + suffix + "_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    archived_path = os.path.join(ARCHIVE_DIR, archive_name)
    shutil.move(post_dir, archived_path)
    return archived_path


def same_path(a, b):
    return bool(a) and bool(b) and os.path.normpath(a) == os.path.normpath(b)


def skip_stale_weekly_posts(current_weekly_dir):
    """Verschiebt Weekly_Summary-Reste aus frueheren Laeufen nach archived/ (ohne sie zu posten)."""
    for item in sorted(os.listdir(PENDING_DIR)):
        item_path = os.path.join(PENDING_DIR, item)
        if (os.path.isdir(item_path)
                and item.startswith(WEEKLY_PREFIX)
                and not same_path(item_path, current_weekly_dir)):
            archived_path = archive_post(item_path, suffix="_skipped")
            print(f"Veralteter Wochen-Post wird nicht gepostet, archiviert: {archived_path}")


def get_next_queued_post():
    """Aeltester Queue-Eintrag, der keine Wochen-Zusammenfassung ist (z.B. New_App_*)."""
    for item in sorted(os.listdir(PENDING_DIR)):
        item_path = os.path.join(PENDING_DIR, item)
        if os.path.isdir(item_path) and not item.startswith(WEEKLY_PREFIX):
            text = read_post(item_path)
            if text:
                return item_path, text
    return None, None


def collect_posts_to_publish():
    """Liste aus (post_dir, text), die in diesem Lauf veroeffentlicht werden."""
    weekly_dir = os.environ.get("WEEKLY_POST_DIR")  # None = nicht vom Workflow gesetzt
    if weekly_dir is not None:
        weekly_dir = weekly_dir.strip()
        skip_stale_weekly_posts(weekly_dir)

    posts = []
    queued_dir, queued_text = get_next_queued_post()
    if queued_dir:
        posts.append((queued_dir, queued_text))

    if weekly_dir:
        weekly_text = read_post(weekly_dir) if os.path.isdir(weekly_dir) else None
        if weekly_text:
            posts.append((weekly_dir, weekly_text))
        else:
            print(f"WARNUNG: Wochen-Post {weekly_dir} nicht gefunden oder leer.")
    return posts


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
    posts = collect_posts_to_publish()

    if not posts:
        print("Keine neuen Posts (keine neuen Updates, Queue leer). Es wird nichts gepostet.")
        return 0

    access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    member_id = os.environ.get("LINKEDIN_MEMBER_ID")

    if not access_token:
        print("ERROR: LINKEDIN_ACCESS_TOKEN fehlt in den Umgebungsvariablen.")
        return 1
    if not member_id:
        print("ERROR: LINKEDIN_MEMBER_ID fehlt in den Umgebungsvariablen.")
        return 1

    for post_dir, text in posts:
        print(f"Post gefunden: {post_dir}")
        print(f"Inhalt (erste 100 Zeichen): {text[:100]}...")

        if not publish_post(text, access_token, member_id):
            print("ERROR: Post konnte nicht veroeffentlicht werden. Lauf wird als fehlgeschlagen beendet.")
            return 1

        print(f"Post archiviert: {archive_post(post_dir)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
