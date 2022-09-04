from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Artist:
    artist_id: str
    name: str = ""
    image_url: str = ""
    spotify_url: str = ""
    total_followers: int = 0
    genres: List[str] = field(default_factory=list) 
    popularity_score: int = 0


