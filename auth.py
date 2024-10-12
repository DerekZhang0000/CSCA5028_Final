import requests
import base64
import json
import os

def get_access_token():
    CLIENT_ID = None
    CLIENT_SECRET = None
    SCOPE = "product.compact"

    if os.path.exists('credentials.json'):
        with open('credentials.json', 'r') as credentials_file:
            credentials_dict = json.loads(credentials_file.readline())
            CLIENT_ID = credentials_dict['CLIENT_ID']
            CLIENT_SECRET = credentials_dict['CLIENT_SECRET']
    else:
            CLIENT_ID = os.getenv('CLIENT_ID')
            CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    url = "https://api.kroger.com/v1/connect/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_credentials}"
    }

    body = {
        "grant_type": "client_credentials",
        "scope": SCOPE
    }

    response = requests.post(url, headers=headers, data=body)

    if response.status_code == 200:
        token_data = response.json()
        return token_data["access_token"]
    else:
        return None