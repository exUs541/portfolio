import os
import json
import requests

# Configuration
GITHUB_TOKEN = os.environ.get('PROJECT_TOKEN')
PROJECT_ID = "PVT_kwDOBrO40M4Ait8y" # This is your project ID from the URL (3)
REPO_OWNER = "exUs541"
JSON_PATH = "roadmap-data.json"

def fetch_project_items():
    query = """
    query($id: ID!) {
      node(id: $id) {
        ... on ProjectV2 {
          items(first: 100) {
            nodes {
              id
              fieldValues(first: 20) {
                nodes {
                  ... on ProjectV2ItemFieldSingleSelectValue {
                    name
                    field { ... on ProjectV2FieldCommon { name } }
                  }
                  ... on ProjectV2ItemFieldTextValue {
                    text
                    field { ... on ProjectV2FieldCommon { name } }
                  }
                }
              }
              content {
                ... on Issue {
                  title
                  body
                  number
                  repository { name }
                }
                ... on DraftIssue {
                  title
                  body
                }
              }
            }
          }
        }
      }
    }
    """
    
    url = "https://api.github.com/graphql"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.post(url, json={"query": query, "variables": {"id": PROJECT_ID}}, headers=headers)
    return response.json()

def process_data(data):
    items = data['data']['node']['items']['nodes']
    processed_projects = []
    
    for item in items:
        status = "backlog" # Default
        fields = item.get('fieldValues', {}).get('nodes', [])
        
        # Extract Status
        for field in fields:
            if field.get('field', {}).get('name') == 'Status':
                status = field.get('name', '').lower()
        
        # Skip if in Suggestions
        if status == 'suggestions':
            continue
            
        content = item.get('content', {})
        title = content.get('title', 'No Title')
        body = content.get('body', '')
        
        # Map GitHub Status to Website Status
        status_map = {
            "backlog": "backlog",
            "in progress": "progress",
            "done": "published",
            "cancelled": "cancelled"
        }
        
        processed_projects.append({
            "id": item['id'],
            "type": "extension" if "[System]" not in title else "system",
            "title": title,
            "desc": body.split('\n')[0][:100] + "..." if body else "No description",
            "fullDesc": body if body else "No details provided.",
            "status": status_map.get(status, "backlog"),
            "votes": 0 # Votes are still handled locally or via Supabase later
        })
        
    return processed_projects

def main():
    if not GITHUB_TOKEN:
        print("Error: PROJECT_TOKEN not found.")
        return

    raw_data = fetch_project_items()
    projects = process_data(raw_data)
    
    with open(JSON_PATH, 'r') as f:
        current_data = json.load(f)
    
    current_data['projects'] = projects
    
    with open(JSON_PATH, 'w') as f:
        json.dump(current_data, f, indent=2)
    
    print(f"Updated {len(projects)} roadmap items.")

if __name__ == "__main__":
    main()
