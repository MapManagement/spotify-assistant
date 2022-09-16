from api.spotify_classes.artist import Artist
from api.spotify_classes.album import Album
from api.spotify_classes.track import Track
from typing import List

# "public" functions

def format_track(track: Track):
    formatted_artists = format_artist_list(track.artists)
    formatted_genres = format_genre_list(track.genres)
    formatted_duration = track.duration / 6000

    track_text = f"---- {track.name.upper()} ----\n"
    track_text += f"Spotify Track ID: {track.track_id}\n"
    track_text += f"Artists: {formatted_artists}\n"
    track_text += f"Popularity: {track.popularity}\n"
    track_text += f"Duration: {formatted_duration}\n"
    track_text += f"Genres: {formatted_genres}\n"
    track_text += f"Preview: {track.preview_url}\n"
    track_text += f"Track URL: {track.spotify_url}\n"

    return track_text

def format_track_genres():
    pass

def format_artist(artist: Artist):
    pass

def format_artist_genre():
    pass

def format_album(album: Album):
    pass

# "private" functions

def format_artist_list(artists: List[Artist]):
    artists_text = ""
    counter = 0

    for artist in artists:
        artists_text += artist.name
        
        counter += 1

        if counter != len(artists):
            artists_text += " | "

    return artists_text

def format_genre_list(genres: List[str]):
    genres_text = ""
    counter = 0

    for genre in genres:
        genres_text += genre
        
        counter += 1

        if counter != len(genres):
            genres_text += " | "

    return genres_text


