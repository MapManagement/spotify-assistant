import requests 
from api.spotify_classes.track import Track
from api.spotify_classes.album import Album
from api.spotify_classes.artist import Artist
from api.spotify_classes.access_token import AccessToken
from api.utils.api_extractor import extract_artist, extract_track, extract_album

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

def get_track(track_url: str, access_token: str) -> Track | None:
    if track_url is None or access_token is None:
        return None

    track_id = get_id_from_url(track_url)

    if track_id is None:
        return None

    authorization_keys = { "Authorization": "Bearer " + access_token }
    api_url = f"https://api.spotify.com/v1/tracks/{track_id}" 

    json_repsonse = requests.get(api_url, headers=authorization_keys).json()
    track = extract_track(json_repsonse)

    return track

def get_album(album_url: str, access_token: str) -> Album | None:
    if album_url is None or access_token is None:
        return None

    album_id = get_id_from_url(album_url)

    if album_id is None:
        return None

    authorization_keys = { "Authorization": "Bearer " + access_token }
    api_url = f"https://api.spotify.com/v1/albums/{album_id}" 

    json_repsonse = requests.get(api_url, headers=authorization_keys).json()
    album = extract_album(json_repsonse)

    return album

def get_artist(artist_url: str, access_token: str) -> Artist | None:
    if artist_url is None or access_token is None:
        return None

    artist_id = get_id_from_url(artist_url)

    if artist_id is None:
        return None

    authorization_keys = { "Authorization": "Bearer " + access_token }
    api_url = f"https://api.spotify.com/v1/artists/{artist_id}" 

    json_repsonse = requests.get(api_url, headers=authorization_keys).json()
    artist = extract_artist(json_repsonse)

    return artist

def get_id_from_url(url: str) -> str | None:
    position = url.find("si=")

    if position == -1:
        return None

    position += 3
    object_id = url[position:len(url) - 1]

    return object_id
