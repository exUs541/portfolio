import os
import requests

# Configuration
GITHUB_TOKEN = os.environ.get('PROJECT_TOKEN')
PROJECT_ID = "PVT_kwDOBrO40M4Ait8y" # Your Project ID

suggestions = [
    {
        "title": "[SAP Signavio] Fix Groups view numbers",
        "body": "When 'show users and group numbers' is enabled in User Management, the numbers disappear when switching to the 'Gruppen' (Groups) view. Pls fix."
    },
    {
        "title": "[SAP Signavio] Restrict number display to specific URL",
        "body": "Only show user and group numbers if the URL begins with: https://editor.signavio.com/g/statics/users"
    },
    {
        "title": "[WebNote] Collapse state on refresh & Dashboard improvements",
        "body": "1. Bug fix: Prevent minimized notes (bubbles) from auto-expanding to full notes on page refresh.\\n2. Feature: Add opacity/transparency options for note bubbles.\\n3. Feature: Option to hide specific notes on a page.\\n4. Feature: In the dashboard, make URLs clickable links and allow editing notes directly."
    },
    {
        "title": "[SAC Extension] Custom colors for folder icons",
        "body": "For the SAP Analytics Cloud (SAC) Extension: Implement a feature allowing users to assign colors to folder icons for better visual organization. The colored icons should be saved locally in browser storage so they are only visible to the user who colored them."
    }
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
