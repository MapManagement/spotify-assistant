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

@track.command()
@click.argument("track_url")
def track_all(track_url: str):
    """Get all information about a track"""
    track = connector.get_track(track_url, str(ACCESS_TOKEN))
    
    if track is not None:
        formatted_track = format_track(track)
        click.echo(formatted_track)

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
def artist_all(artist_url: str):
    """Get all information about an artist"""
    pass

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
def album_all(album_url: str):
    """Get all information about an album"""
    pass

# ----- Non-CLI-Commands

def read_secrets() -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

cli = click.CommandCollection(sources=[artist, album, track])

if __name__ == "__main__":
    secrets = read_secrets()
    
    if ACCESS_TOKEN is None:
        token_object = connector.get_access_token(secrets["CLIENT_ID"], secrets["CLIENT_SECRET"])
        ACCESS_TOKEN = token_object.token
    
    cli()

