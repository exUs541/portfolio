import os
import requests

# Configuration
GITHUB_TOKEN = os.environ.get('PROJECT_TOKEN')
PROJECT_ID = "PVT_kwDOBrO40M4Ait8y" # Your Project ID

suggestions = [
    {"title": "[SiteBlocker] Analytics Dashboard", "body": "See how much time you've saved by blocking distracting sites."},
    {"title": "[TabMaster] Session Manager", "body": "Save and restore entire sets of tabs with one click."},
    {"title": "[WebNote] Cloud Backup", "body": "Sync your website notes across all your devices."},
    {"title": "[YT Filter] Keyword Blocking", "body": "Automatically hide videos that contain specific words in their title."}
]

def add_item(title, body):
    query = """
    mutation($projectId: ID!, $contentId: String!) {
      addProjectV2DraftItem(input: {projectId: $projectId, title: $contentId}) {
        projectItem { id }
      }
    }
    """
    url = "https://api.github.com/graphql"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    # Draft items in V2 only take a title in this mutation, body is updated separately if needed
    response = requests.post(url, json={"query": query, "variables": {"projectId": PROJECT_ID, "contentId": title}}, headers=headers)
    return response.json()

def main():
    if not GITHUB_TOKEN:
        print("Error: PROJECT_TOKEN environment variable not set.")
        return

    for s in suggestions:
        res = add_item(s['title'], s['body'])
        if 'errors' in res:
            print(f"Error adding {s['title']}: {res['errors'][0]['message']}")
        else:
            print(f"Successfully added: {s['title']}")

if __name__ == "__main__":
    main()
