import json
import os
import requests
from requests_oauth2client import OAuth2Client, BearerToken

# Globals
auth_endpoint = "https://texas-sos-stage.appiancloud.com/suite/authorization/oauth/token"
upload_endpoint = "https://texas-sos-stage.appiancloud.com/suite/webapi/applications"
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# Get Token
def get_token(cid: str, secret: str, endpoint: str, target: str) -> BearerToken:
    oa_client = OAuth2Client(token_endpoint=endpoint, client_id=cid, client_secret=secret)
    retval = oa_client.client_credentials(resource=target)
    return retval


# Submit List
def submit_application(token: BearerToken, body: any, endpoint: str) -> str:
    response = requests.post(endpoint, json=body, auth=token)
    return response.text


# Main
print('Reading sample file')
with open('/Users/walker/Downloads/SOSSingleUpload.json') as f:
    payload = f.read()

print('Getting Token')
token = get_token(client_id, client_secret, auth_endpoint, upload_endpoint)
print(f'Token: {token.access_token}')

print('Submitting Application')
result = submit_application(token, payload, upload_endpoint)
print(result)
