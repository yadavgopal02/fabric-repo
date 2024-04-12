import requests
import os

# Replace these values with your own
tenant_id = os.environ['AZURE_TENANT_ID']
client_id = os.environ['AZURE_CLIENT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
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
