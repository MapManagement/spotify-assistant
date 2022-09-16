import api.api_connector as connector
from api.spotify_classes.access_token import AccessToken
from formatter.formatter import format_album, format_track, format_artist
import json
import os
import click

ACCESS_TOKEN = None

# ----- CLI-Commands

@click.group()
def track():
    pass

@click.command()
@click.argument("track_url")
def track_all(track_url: str):
    track = connector.get_track(track_url, str(ACCESS_TOKEN))
    
    if track is not None:
        formatted_track = format_track(track)
        click.echo(formatted_track)

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

# ----- Non-CLI-Commands

def read_secrets() -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

def add_track_group():
    track.add_command(track_all)
    track.add_command(track_genre)

def add_artist_group():
    artist.add_command(artist_all)
    artist.add_command(artist_genre)

def add_album_group():
    album.add_command(album_all)

if __name__ == "__main__":
    secrets = read_secrets()
    
    if ACCESS_TOKEN is None:
        token_object = connector.get_access_token(secrets["CLIENT_ID"], secrets["CLIENT_SECRET"])
        ACCESS_TOKEN = token_object.token
    
    add_track_group()
    add_artist_group()
    add_album_group()

    # s_track = connector.get_track("4MDrGVm2yYsMj97CLGdhdI", str(ACCESS_TOKEN))
