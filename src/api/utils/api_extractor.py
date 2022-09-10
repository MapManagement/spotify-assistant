from api.spotify_classes.artist import Artist
from api.spotify_classes.track import Track
from typing import List, Optional

def extract_artist(artist_dict: dict) -> Optional[Artist]:
    if artist_dict is None:
        return None 

    extracted_artist = Artist(artist_id = artist_dict["id"],
                    name = artist_dict["name"],
                    # image_url
                    spotify_url = artist_dict["external_urls"]["spotify"],
                    # total_followers
                    genres = artist_dict["genres"],
                    popularity = artist_dict["popularity"])

    return extracted_artist


def extract_track(track_dict: dict) -> Optional[Track]:
    artist_list: List[Artist] = []

    for track_artist in track_dict["artists"]:
        extracted_artist = extract_artist(track_artist)
        
        if extracted_artist is None:
            continue

        artist_list.append(extracted_artist)

    extracted_track = Track(name = track_dict["name"],
                  track_id = track_dict["id"],
                  duration = track_dict["duration_ms"],
                  spotify_url = track_dict["external_urls"]["spotify"],
                  preview_url = track_dict["preview_url"],
                  popularity = track_dict["popularity"],
                  album_id = track_dict["album"]["id"],
                  artists = artist_list
                  # genres = list(json_repsonse["artists"]["genres"]),
                  # image_url
                  )

    return extracted_track

