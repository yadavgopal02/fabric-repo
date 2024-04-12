import requests
import os

# Replace these values with your own
tenant_id = os.environ['55ea6196-70b9-4411-92f5-04a54791f120']
client_id = os.environ['80128ec8-dabe-4b3d-a75a-2f7551760ac5']
client_secret = os.environ['F2K8Q~rxUlkDXxEbUbPjXzFULOhkU7Xdw3YnSduo']
resource_url = "https://analysis.windows.net/powerbi/api"

# Get Access Token
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
token_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "resource": resource_url
}
token_response = requests.post(token_url, data=token_data)
token_response.raise_for_status()
access_token = token_response.json()["access_token"]

# Make GET request to list fabric workspaces
list_workspaces_url = "https://api.powerbi.com/v1.0/myorg/groups"
headers = {
    "Authorization": f"Bearer {access_token}"
}
response = requests.get(list_workspaces_url, headers=headers)
response.raise_for_status()

# Print the list of fabric workspaces
workspaces = response.json()["value"]
for workspace in workspaces:
    print("Workspace ID:", workspace["id"])
    print("Workspace Name:", workspace["name"])
    print()
