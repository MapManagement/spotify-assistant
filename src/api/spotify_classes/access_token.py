from dataclasses import dataclass

@dataclass
class AccessToken:
    token: str
    expires_in: int
    token_type: str
