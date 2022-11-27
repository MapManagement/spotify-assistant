from utils import cli_helper, token_helper
import click

ACCESS_TOKEN = None
ACCESS_TOKEN_ERROR = "Your access token could not be used to resolve data from Spotify."

# ----- CLI commands

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
def track_features(track_url: str):
    """ Get the audio features of a track """
    if not valid_access_token():
        return

    audio_features_text = cli_helper.get_audio_features(track_url, str(ACCESS_TOKEN))
    click.echo(audio_features_text)

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
    print(ACCESS_TOKEN)
    artist_text = cli_helper.get_full_artist(artist_url, str(ACCESS_TOKEN))
    click.echo(artist_text)

@artist.command()
@click.argument("artist_url")
def artist_genres(artist_url: str):
    """Get the genre of an artist"""
    if not valid_access_token():
        return

    genres_text = cli_helper.get_artist_genres(artist_url, str(ACCESS_TOKEN))
    click.echo(genres_text)

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

@click.group()
def playlist():
    pass

@playlist.command()
@click.argument("playlist_url")
def full_playlist(playlist_url: str):
    """Get all information about a public playlist"""
    if not valid_access_token():
        return

    playlist_text = cli_helper.get_full_playlist(playlist_url, str(ACCESS_TOKEN))
    click.echo(playlist_text)

# ----- Non-CLI functions

def valid_access_token() -> bool:
    valid = ACCESS_TOKEN is not None or len(str(ACCESS_TOKEN)) == 0

    if not valid:
        click.echo(ACCESS_TOKEN_ERROR)

    return valid

if __name__ == "__main__":
    if ACCESS_TOKEN is None:
        ACCESS_TOKEN = token_helper.get_access_token()

    if ACCESS_TOKEN is None:
        print("The access token is either empty or has not been set!")
        quit()

    cli = click.CommandCollection(sources=[artist, album, track, playlist])
    cli()

