from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from api.spotify_classes.artist import Artist
from api.spotify_classes.track import Track

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
    release_data: datetime = datetime.now()
    image_url: str = ""
    artists: Artist = Artist("")
    tracks: Track = Track("")

