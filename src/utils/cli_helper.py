import api.api_connector as connector
from api.spotify_classes.access_token import AccessToken
from utils.formatter import format_album, format_audio_features, format_track, format_artist

ERROR_TEXT = "Something went wrong..."

def get_full_track(track_url: str, access_token: str) -> str | None:
    track = connector.get_track(track_url, access_token)

    if track is not None:
        formatted_track = format_track(track)
        return formatted_track

    return ERROR_TEXT

def get_audio_features(track_url: str, access_token: str) -> str | None:
    audio_features = connector.get_auido_features(track_url, access_token)

    if audio_features is not None:
        formatted_audio_features = format_audio_features(audio_features)
        return formatted_audio_features

    return ERROR_TEXT

def get_full_artist(artist_url: str, access_token: str) -> str | None:
    artist = connector.get_artist(artist_url, access_token)

    if artist is not None:
        formatted_artist = format_artist(artist)
        return formatted_artist

    return ERROR_TEXT

def get_full_album(album_url: str, access_token: str) -> str | None:
    album = connector.get_album(album_url, access_token)

    if album is not None:
        formatted_album = format_album(album)
        return formatted_album

    return ERROR_TEXT
