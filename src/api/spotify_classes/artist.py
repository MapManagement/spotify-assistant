from dataclasses import dataclass

@dataclass
class Artist:
    artist_id: str
    name: str = ""
    image_url: str = ""
    spotify_url: str = ""
    total_followers: int = 0
    genres: list = []
    popularity_score: int = 0


