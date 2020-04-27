import spotipy
import assistant.secrets as secrets

credentials = spotipy.oauth2.SpotifyClientCredentials(
    client_id=secrets.client_id,
    client_secret=secrets.client_secret
)


class SpotifyAssistant:

    def __init__(self):
        self.assistant = spotipy.Spotify(client_credentials_manager=credentials)

    def get_playlist_info(self, playlist_uri: str):
        playlist_id = playlist_uri.split(":")[2]
        playlist_data = self.assistant.playlist(playlist_id)
        response = f"""
Playlist Name: {playlist_data["name"]}
Creator/Owner: {playlist_data["owner"]["display_name"]}
Playlist URL: {playlist_data["external_urls"]["spotify"]}
Followers: {playlist_data["followers"]["total"]}
                    """
        print(response)


if __name__ == "__main__":
    assistant = SpotifyAssistant()
    assistant.get_playlist_info("spotify:playlist:7sZbq8QGyMnhKPcLJvCUFD")
