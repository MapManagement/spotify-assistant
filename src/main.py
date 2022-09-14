import api.api_connector as connector
from api.spotify_classes.access_token import AccessToken
import json
import os
import click

ACCESS_TOKEN = None

@click.group()
def track():
    pass

@click.command()
@click.argument("track_url")
def track_all(track_url: str):
    pass

@click.command()
@click.argument("track_url")
def track_genre(track_url: str):
    pass

@click.group()
def artist():
    pass

@click.command()
@click.argument("artist_url")
def artist_all(artist_url: str):
    pass

@click.command()
@click.argument("artist_url")
def artist_genre(artist_url: str):
    pass

@click.group()
def album():
    pass

@click.command()
@click.argument("album_url")
def album_all(album_url: str):
    pass

def read_secrets() -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
    secrets = read_secrets()
    
    if ACCESS_TOKEN is None:
        token_object = connector.get_access_token(secrets["CLIENT_ID"], secrets["CLIENT_SECRET"])
        ACCESS_TOKEN = token_object.token

    s_track = connector.get_track("4MDrGVm2yYsMj97CLGdhdI", str(ACCESS_TOKEN))
    print(s_track)
