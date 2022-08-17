import requests 
import base64
import json
import spotify_objects

def get_access_token(client_id: str, client_secret: str) -> spotify_objects.AccessToken:
    authorization_keys = {
            "grant_type": "client_credentials",    
            "client_id": client_id,
            "client_secret": client_secret,
    }

    repsonse = requests.post("https://accounts.spotify.com/api/token", authorization_keys)
    json_repsonse = repsonse.json()
    access_token = spotify_objects.AccessToken(token = str(json_repsonse["access_token"]),
                                               token_type = str(json_repsonse["token_type"]),
                                               expires_in = int(json_repsonse["expires_in"]))

    return access_token

def get_track(track_id: str, access_token: str) -> spotify_objects.Track:
    authorization_keys = {
            "headers":
            {
                "Authorization": access_token,
                "Content-Type": "application/json"
            }
    }

    json_repsonse = requests.get(f"https://api.spotify.com/v1/tracks/{track_id}", authorization_keys).json()
    track = spotify_objects.Track(name = json_repsonse["name"],
                                  track_id = json_repsonse["id"])

    return track


