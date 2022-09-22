from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from api.spotify_classes.artist import Artist
from api.spotify_classes.track import Track
from typing import List

class AlbumType(Enum):
    ALBUM = 0
    SINGLE = 1
    COMPILATION = 2

@dataclass
class Album:
    album_id: str
    name: str = ""
    album_type: AlbumType = AlbumType.ALBUM
    total_tracks: int = 0
    spotify_url: str = ""
    release_date: datetime = datetime.now()
    image_url: str = ""
    artists: List[Artist] = field(default_factory=list)
    tracks: Track = Track("")

