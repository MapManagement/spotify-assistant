from dataclasses import dataclass, field
from typing import List


@dataclass
class Playlist:
    playlist_id: str
    name: str = ""
    description: str = ""
    spotify_url: str = ""
    image_url: str = ""
    owner_url: str = ""
    followers: int = 0
    total_tracks: int = 0
    tracks: List[str] = field(default_factory=list)
