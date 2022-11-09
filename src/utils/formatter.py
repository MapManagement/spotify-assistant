from api.spotify_classes.artist import Artist
from api.spotify_classes.album import Album
from api.spotify_classes.audio_features import AudioFeatures
from api.spotify_classes.track import Track
from typing import List

# "public" functions

def format_track(track: Track):
    formatted_artists = format_artist_list(track.artists)
    formatted_genres = format_genre_list(track.genres)
    formatted_duration = format_duration(track.duration)

    track_text = f"---- {track.name.upper()} ----\n"
    track_text += f"Spotify Track ID: {track.track_id}\n"
    track_text += f"Artists: {formatted_artists}\n"
    track_text += f"Popularity: {track.popularity}\n"
    track_text += f"Duration: {formatted_duration}\n"
    track_text += f"Genres: {formatted_genres}\n"
    track_text += f"Image URL {track.image_url}\n"
    track_text += f"Preview: {track.preview_url}\n"
    track_text += f"Track URL: {track.spotify_url}\n"

    return track_text

def format_audio_features(audio_features: AudioFeatures) -> str:
    formatted_duration = format_duration(audio_features.duration)

    features_text = f"---- {audio_features.track_id} ----\n"
    features_text += f"Acousticness: {audio_features.acousticness*100:.2f}%\n"
    features_text += f"Danceability: {audio_features.danceability*100:.2f}%\n"
    features_text += f"Energy: {audio_features.energy*100:.2f}%\n"
    features_text += f"Instrumentalness: {audio_features.instrumentalness*100:.2f}%\n"
    features_text += f"Liveness: {audio_features.liveness*100:.2f}%\n"
    features_text += f"Loudness: {audio_features.loudness*-1:.2f}dB\n"
    features_text += f"Speechiness: {audio_features.speechiness*100:.2f}%\n"
    features_text += f"Tempo: {audio_features.tempo:.2f} BPM\n"
    features_text += f"Valence {audio_features.valence*100:.2f}%\n"
    features_text += f"Pitch Class Integer: {audio_features.pitch_class}\n"
    features_text += f"Duration: {formatted_duration}\n"

    return features_text

def format_track_genres():
    pass

def format_artist(artist: Artist):
    formatted_genres = format_genre_list(artist.genres)

    artist_text = f"---- {artist.name.upper()} ----\n"
    artist_text += f"Spotify Artist ID: {artist.artist_id}\n"
    artist_text += f"Total Followers: {artist.total_followers}\n"
    artist_text += f"Popularity: {artist.popularity}\n"
    artist_text += f"Genres: {formatted_genres}\n"
    artist_text += f"Image URL: {artist.image_url}\n"
    artist_text += f"Artist URL: {artist.spotify_url}\n"

    return artist_text



def format_artist_genres(genres: list[str]):
    genres_text = f"---- GENRES ----\n"

    for genre in genres:
       genres_text += f"{genre}\n"

    return genres_text

def format_album(album: Album):
    formatted_artists = format_artist_list(album.artists)

    album_text = f"---- {album.name.upper()} ----\n"
    album_text += f"Spotify Album ID: {album.album_id}\n"
    album_text += f"Type: {album.album_type}\n"
    album_text += f"Total Tracks: {album.total_tracks}\n"
    album_text += f"Artists: {formatted_artists}\n"
    album_text += f"Image URL: {album.image_url}\n"
    album_text += f"Album URL: {album.spotify_url}\n"

    return album_text

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

def format_duration(duration: int) -> str:
    hours_rest = duration % 3600000 
    hours = duration // 3600000
    minutes_rest = hours_rest % 60000
    minutes = hours_rest // 60000
    seconds = minutes_rest // 1000 
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"

