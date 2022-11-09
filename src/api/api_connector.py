import requests
from api.spotify_classes.track import Track
from api.spotify_classes.access_token import AccessToken
from api.spotify_classes.album import Album
from api.spotify_classes.artist import Artist
from api.spotify_classes.audio_features import AudioFeatures
from api.utils.api_extractor import extract_artist, extract_track, extract_album, extract_audio_features, extract_artist_genres

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

    track_id = get_id_from_url(track_url, "track")

    if track_id is None:
        return None

    authorization_keys = { "Authorization": "Bearer " + access_token }
    api_url = f"https://api.spotify.com/v1/tracks/{track_id}" 

    json_repsonse = requests.get(api_url, headers=authorization_keys).json()
    track = extract_track(json_repsonse)

    return track

def get_audio_features(track_url: str, access_token: str) -> AudioFeatures | None:
    if track_url is None or access_token is None:
        return None

    track_id = get_id_from_url(track_url, "track")

    if track_id is None:
        return None

    authorization_keys = { "Authorization": "Bearer " + access_token }
    api_url = f"https://api.spotify.com/v1/audio-features/{track_id}"

    json_response = requests.get(api_url, headers=authorization_keys).json()
    audio_features = extract_audio_features(json_response)

    return audio_features


def get_album(album_url: str, access_token: str) -> Album | None:
    if album_url is None or access_token is None:
        return None

    album_id = get_id_from_url(album_url, "album")

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

    artist_id = get_id_from_url(artist_url, "artist")

    if artist_id is None:
        return None

    authorization_keys = { "Authorization": "Bearer " + access_token }
    api_url = f"https://api.spotify.com/v1/artists/{artist_id}" 

    json_repsonse = requests.get(api_url, headers=authorization_keys).json()
    artist = extract_artist(json_repsonse)

    return artist

def get_artist_genres(artist_url: str, access_token: str) -> list[str] | None:
    if artist_url is None or access_token is None:
        return None
    
    artist_id = get_id_from_url(artist_url, "artist")

    if artist_id is None:
        return None

    authorization_keys = { "Authorization": "Bearer " + access_token }
    api_url = f"https://api.spotify.com/v1/artists/{artist_id}" 

    json_repsonse = requests.get(api_url, headers=authorization_keys).json()
    artist = extract_artist_genres(json_repsonse)

    return artist

def get_id_from_url(url: str, object_type: str) -> str | None:
    position = url.find(f"{object_type}/")

    if position == -1:
        return None

    position += len(object_type) + 1
    object_id = url[position:len(url)]
    
    return object_id
