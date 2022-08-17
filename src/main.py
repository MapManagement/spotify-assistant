import api_connector as api
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
        ACCESS_TOKEN= api.get_access_token(secrets["CLIENT_ID"], secrets["CLIENT_SECRET"])
