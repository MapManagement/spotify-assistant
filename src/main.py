import api.api_connector as connector
from api.spotify_classes.access_token import AccessToken
from utils import cli_helper
import json
import os
import click

ACCESS_TOKEN = None
ACCESS_TOKEN_ERROR = "Your access token could not be used to resolve data from Spotify."

# ----- CLI-Commands

@click.group()
def track():
    pass

@track.command()
@click.argument("track_url")
def full_track(track_url: str):
    """Get all information about a track"""
    if not valid_access_token():
        return

    track_text = cli_helper.get_full_track(track_url, str(ACCESS_TOKEN))
    click.echo(track_text)

@track.command()
@click.argument("track_url")
def track_genre(track_url: str):
    """ Get the genre of a track"""
    pass

@click.group()
def artist():
    pass

@artist.command()
@click.argument("artist_url")
def full_artist(artist_url: str):
    """Get all information about an artist"""
    if not valid_access_token():
        return

    artist_text = cli_helper.get_full_artist(artist_url, str(ACCESS_TOKEN))
    click.echo(artist_text)


@artist.command()
@click.argument("artist_url")
def artist_genre(artist_url: str):
    """Get the genre of an artist"""
    pass

@click.group()
def album():
    pass

@album.command()
@click.argument("album_url")
def full_album(album_url: str):
    """Get all information about an album"""
    if not valid_access_token():
        return

    album_text = cli_helper.get_full_album(album_url, str(ACCESS_TOKEN))
    click.echo(album_text)

# ----- Non-CLI-Commands

def valid_access_token() -> bool:
    valid = ACCESS_TOKEN is not None or len(str(ACCESS_TOKEN)) == 0
    if not valid:
        click.echo(ACCESS_TOKEN_ERROR)

    return valid

def read_secrets() -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

def get_access_token() -> str | None:
    if ACCESS_TOKEN is not None:
        return ACCESS_TOKEN

    secrets = read_secrets()

    if secrets is None or len(secrets) < 1: 
        return None

    token_object = connector.get_access_token(secrets["CLIENT_ID"], secrets["CLIENT_SECRET"])
    return token_object.token

if __name__ == "__main__":
    ACCESS_TOKEN = get_access_token()

    if ACCESS_TOKEN is None:
        print("The access token is either empty or has not been set!")
        quit()

    cli = click.CommandCollection(sources=[artist, album, track])
    cli()

