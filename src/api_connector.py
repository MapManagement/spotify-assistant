import requests 
import base64
import json
import spotify_objects

def get_access_token(client_id: str, client_secret: str) -> spotify_objects.AccessToken:
    encoded_key = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8"))
    encoded_string = str(encoded_key, "utf-8")
    

    authorization_keys = {
        "url": "https://accounts.spotify.com/api/token",
        "headers":
        {
            "Authorization": f"Basic {encoded_string}"
        },
        "form":
        {
            "grant_type": "client_credentials"
        },
        "json": True
    };

    json_object = json.dumps(authorization_keys)
    json_repsonse = requests.post("https://accounts.spotify.com/api/token", json_object).json()
    access_token = spotify_objects.AccessToken(token = str(json_repsonse["access_token"]),
                                               token_type = str(json_repsonse["token_type"]),
                                               expires_in = int(json_repsonse["expires_in"]))

    return access_token

def get_track(track_id: str, access_token: str) -> spotify_objects.Track:
    authorization_keys = {
            "url": "https://api.spotify.com/v1/tracks/id",
            "headers": 
            {
                "Authorization": access_token,
                "Content-Type": "application/json"
            }
    }

    json_repsonse = requests.get("https://api.spotify.com/v1/tracks/id", authorization_keys).json()
    track = spotify_objects.Track(name = json_repsonse["name"],
                                  track_id = json_repsonse["id"])

    return track


