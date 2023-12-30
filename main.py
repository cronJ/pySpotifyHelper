import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_USER = os.environ.get("SPOTIFY_USER")


def main() -> None:
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlists = sp.user_playlists(SPOTIFY_USER)
    while playlists:
        for i, playlist in enumerate(playlists["items"]):
            print(
                "%4d %s %s"
                % (i + 1 + playlists["offset"], playlist["uri"], playlist["name"])
            )
        if playlists["next"]:
            playlists = sp.next(playlists)
        else:
            playlists = None


if __name__ == "__main__":
    main()
