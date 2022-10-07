from dataclasses import dataclass

@dataclass
class AudioFeatures:
    track_id : str
    acousticness: float = 0.0
    danceability: float = 0.0
    energy: float = 0.0
    instrumentalness: float = 0.0
    liveness: float = 0.0
    loudness: float = 0.0
    speechiness: float = 0.0
    tempo: float = 0.0
    valence: float = 0.0
    pitch_class: int = -1
    duration: int = 0
