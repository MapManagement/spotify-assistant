class Artist:

    def __init__(self):
        pass


class Track:

    def __init__(self, name: str, track_id: str):
        self.name = name
        self.track_id = track_id

class Playlist:

    def __init__(self):
        pass

class AccessToken:

    def __init__(self, token: str, token_type: str, expires_in: int):
        self.token = token
        self.token_type = token_type
        self.expires_in = expires_in
