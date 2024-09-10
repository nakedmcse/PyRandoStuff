import json
import os
import requests

# Globals
auth_endpoint = "https://texas-sos-stage.appiancloud.com/suite/authorization/oauth/token"
upload_endpoint = "https://texas-sos-stage.appiancloud.com/suite/webapi/applications"
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# Get Token
def get_token(cid: str, secret: str, endpoint: str, target: str) -> {}:
    response = requests.post(endpoint, data={
        'address': target,
        'client_id': cid,
        'client_secret': secret,
        'grant_type': 'client_credentials'
    },
    headers={
        'Accept': 'application/json'
    })
    return json.loads(response.text)


# Submit List
def submit_application(token: str, body: any, endpoint: str) -> str:
    response = requests.post(endpoint, json=body, headers={
        'UserToken': token
    })
    return response.text


# Main
print('Reading sample file')
with open('/Users/walker/Downloads/SOSSingleUpload.json') as f:
    payload = f.read()

print('Getting Token')
token = get_token(client_id, client_secret, auth_endpoint, upload_endpoint)
print(f'Token: {token["access_token"]}')

print('Submitting Application')
result = submit_application(token["access_token"], payload, upload_endpoint)
print(result)
