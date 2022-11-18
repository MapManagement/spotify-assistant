from enum import Enum
from api.spotify_classes.album import Album
from api.spotify_classes.artist import Artist
from api.spotify_classes.audio_features import AudioFeatures
from api.spotify_classes.track import Track
from typing import List, Dict

class ExtractType(Enum):
    FULL = 1
    MINIMAL = 2
    ONLY_ID = 3

def extract_artist(artist_dict: dict) -> Artist | None:
    if artist_dict is None:
        return None 

    extracted_artist = Artist(artist_id = artist_dict["id"],
                    name = artist_dict["name"],
                    image_url = get_first_image_url(artist_dict["images"]),
                    spotify_url = artist_dict["external_urls"]["spotify"],
                    total_followers = artist_dict["followers"]["total"],
                    genres = artist_dict["genres"],
                    popularity = artist_dict["popularity"]
                    )

    return extracted_artist

def extract_minimal_artist(artist_dict: dict) -> Artist | None:
    extracted_minimal_artist = Artist(artist_id = artist_dict["id"],
                                      name = artist_dict["name"],
                                      spotify_url = artist_dict["external_urls"]["spotify"]
                                      )
    return extracted_minimal_artist


def extract_multiple_artists(artists_list: List[dict], extract_type: ExtractType) -> List[Artist]:
    if artists_list is None or len(artists_list) == 0:
        return []

    extracted_artists_list: List[Artist] = []

    for artist in artists_list:
        extracted_artist = None

        if extract_type is ExtractType.FULL: 
            extracted_artist = extract_artist(artist)
        elif extract_type is ExtractType.MINIMAL:
            extracted_artist = extract_minimal_artist(artist)

        if extracted_artist is None:
            continue

        extracted_artists_list.append(extracted_artist)

    return extracted_artists_list

def extract_artist_genres(artist_dict: dict) -> Dict[str, List[str]] | None:
    if artist_dict is None:
        return None

    artist_name = artist_dict.get("name")
    genres = artist_dict.get("genres")

    if genres is None or artist_name is None:
        return None

    artist_genres_dict = {artist_name: genres}

    return artist_genres_dict 


def extract_track(track_dict: dict) -> Track | None:
    extracted_track = Track(name = track_dict["name"],
                  track_id = track_dict["id"],
                  duration = track_dict["duration_ms"],
                  spotify_url = track_dict["external_urls"]["spotify"],
                  preview_url = track_dict["preview_url"],
                  popularity = track_dict["popularity"],
                  album_id = track_dict["album"]["id"],
                  artists = extract_multiple_artists(track_dict["artists"], ExtractType.MINIMAL),
                  # genres: only stored with artists
                  image_url = get_first_image_url(track_dict["album"]["images"])
                  )

    return extracted_track

def extract_audio_features(features_dict: dict) -> AudioFeatures | None:
    extracted_features = AudioFeatures(track_id = features_dict["id"],
                                       acousticness = features_dict["acousticness"],
                                       danceability = features_dict["danceability"],
                                       duration = features_dict["duration_ms"],
                                       energy = features_dict["energy"],
                                       instrumentalness = features_dict["instrumentalness"],
                                       liveness = features_dict["liveness"],
                                       loudness =  features_dict["loudness"],
                                       speechiness = features_dict["speechiness"],
                                       tempo = features_dict["tempo"],
                                       valence = features_dict["valence"],
                                       pitch_class = features_dict["key"]
                                       )

    return extracted_features

def extract_album(album_dict: dict) -> Album | None:
    extracted_album = Album(name = album_dict.get("name", ""),
                            album_id = album_dict.get("id", ""),
                            album_type = album_dict["album_type"],
                            total_tracks = album_dict.get("total_tracks", 0),
                            spotify_url = album_dict["external_urls"]["spotify"],
                            # release_date
                            image_url = get_first_image_url(album_dict["images"]),
                            artists = extract_multiple_artists(album_dict["artists"], ExtractType.MINIMAL)
                            # tracks
                            )

    return extracted_album

def get_first_image_url(image_list) -> str | None:
    if len(image_list) == 0:
        return None

    for image in image_list:
        image_url = image["url"]
        return image_url
