import json
import os
from api import api_connector

def read_secrets() -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

def get_access_token() -> str | None:
    secrets = read_secrets()

    if secrets is None or len(secrets) < 1: 
        return None

    token_object = api_connector.get_access_token(secrets["CLIENT_ID"], secrets["CLIENT_SECRET"])
    return token_object.token

