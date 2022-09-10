import api.api_connector as connector
from api.spotify_classes.access_token import AccessToken
import json
import os

ACCESS_TOKEN = None

def read_secrets() -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
    secrets = read_secrets()
    
    if ACCESS_TOKEN is None:
        token_object = connector.get_access_token(secrets["CLIENT_ID"], secrets["CLIENT_SECRET"])
        ACCESS_TOKEN = token_object.token

    track = connector.get_track("4MDrGVm2yYsMj97CLGdhdI", str(ACCESS_TOKEN))
    print(track)
