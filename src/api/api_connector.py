import requests 
from api.spotify_classes.track import Track
from api.spotify_classes.album import Album
from api.spotify_classes.artist import Artist
from api.spotify_classes.access_token import AccessToken

def get_access_token(client_id: str, client_secret: str) -> AccessToken:
    authorization_keys = {
            "grant_type": "client_credentials",    
            "client_id": client_id,
            "client_secret": client_secret,
    }

    repsonse = requests.post("https://accounts.spotify.com/api/token", authorization_keys)
    json_repsonse = repsonse.json()
    access_token = AccessToken(token = str(json_repsonse["access_token"]),
                                           token_type = str(json_repsonse["token_type"]),
                                           expires_in = int(json_repsonse["expires_in"]))

    return access_token

def get_track(track_id: str, access_token: str) -> Track:
    authorization_keys = { "Authorization": "Bearer " + access_token }

    json_repsonse = requests.get(f"https://api.spotify.com/v1/tracks/{track_id}", headers=authorization_keys).json()
    track = Track(name = json_repsonse["name"],
                  track_id = json_repsonse["id"])

    return track


