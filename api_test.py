import requests
import os
import pbirest


credentials = pbirest.AzureAD(
tenant_id = os.environ['tenant_id']
client_id = os.environ['client_id']
client_secret = os.environ['client_secret']
)

workspaces_api = pbirest.WorkspacesApi(credentials)

