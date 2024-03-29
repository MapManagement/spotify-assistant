from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class Artist:
    artist_id: str 
    name: str = ""
    image_url: Optional[str] = None
    spotify_url: str = ""
    total_followers: int = 0
    genres: List[str] = field(default_factory=list) 
    popularity: int = 0


