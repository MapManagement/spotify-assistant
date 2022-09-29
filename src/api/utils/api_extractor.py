from api.spotify_classes.album import Album
from api.spotify_classes.artist import Artist
from api.spotify_classes.track import Track
from typing import List

def extract_artist(artist_dict: dict) -> Artist | None:
    if artist_dict is None:
        return None 

    extracted_artist = Artist(artist_id = artist_dict["id"],
                    name = artist_dict["name"],
                    # image_url
                    spotify_url = artist_dict["external_urls"]["spotify"],
                    total_followers = artist_dict["followers"]["total"],
                    # genres = artist_dict["genres"],
                    popularity = artist_dict["popularity"]
                    )

    return extracted_artist

def extract_multiple_artists(artists_list: List[dict]) -> List[Artist]:
    if artists_list is None or len(artists_list) == 0:
        return []

    extracted_artists_list: List[Artist] = []

    for artist in artists_list:
        extracted_artist = extract_artist(artist)

        if extracted_artist is None:
            continue

        extracted_artists_list.append(extracted_artist)

    return extracted_artists_list


def extract_track(track_dict: dict) -> Track | None:
    extracted_track = Track(name = track_dict["name"],
                  track_id = track_dict["id"],
                  duration = track_dict["duration_ms"],
                  spotify_url = track_dict["external_urls"]["spotify"],
                  preview_url = track_dict["preview_url"],
                  popularity = track_dict["popularity"],
                  album_id = track_dict["album"]["id"],
                  # artists = extract_multiple_artists(track_dict["artists"])
                  # genres = list(json_repsonse["artists"]["genres"]),
                  # image_url
                  )

    return extracted_track

def extract_album(album_dict: dict) -> Album | None:
    extracted_album = Album(name = album_dict.get("name", ""),
                            album_id = album_dict.get("id", ""),
                            # album_type
                            total_tracks = album_dict.get("total_track", 0),
                            spotify_url = album_dict["external_urls"]["spotify"],
                            # release_date
                            # image_url
                            # artists = extract_multiple_artists(album_dict["artists"])
                            # tracks
                            )

    return extracted_album

