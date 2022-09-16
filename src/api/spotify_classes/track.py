from dataclasses import dataclass, field
from api.spotify_classes.artist import Artist
from typing import List

@dataclass
class Track:
    track_id: str
    name: str = ""
    duration: int = 0
    spotify_url: str = ""
    preview_url: str = ""
    popularity: int = 0
    album_id: str = ""
    artists: List[Artist] = field(default_factory=list)
    genres: List[str] = field(default_factory=list)
    image_url: str = ""

    
