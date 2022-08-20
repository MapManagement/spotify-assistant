from dataclasses import dataclass
from artist import Artist
from album import Album

@dataclass
class Track:
    track_id: str
    name: str = ""
    duration: str = ""
    spotify_url: str = ""
    preview_url: str = ""
    popularity: int = 0
    album: Album = Album("")
    artists: list = []
    genres: str = ""
    image_url: str = ""

    
