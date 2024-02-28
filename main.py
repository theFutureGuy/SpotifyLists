import os
import argparse
from os.path import join, dirname
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import sqlite3
from typing import List, Tuple, Union


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
SPOTIFY_USERNAME = os.getenv("SPOTIFY_USERNAME")
SCOPE = "playlist-modify-public user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Spotify playlist generator', add_help=False)

    optional_args = parser.add_argument_group('Optional Arguments')
    optional_args.add_argument('--refresh', action='store_true',help="Refresh playlists from Spotify")
    optional_args.add_argument('--list-playlists', action='store_true', help="List your Spotify playlists")
    optional_args.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    return parser.parse_args()


def create_tables_if_not_exists(table: Union[str, None] = None):
    with sqlite3.connect("playlists.db") as conn:
        cursor = conn.cursor()
        if table == 'playlists' or table is None:
            cursor.execute("CREATE TABLE IF NOT EXISTS playlists (id TEXT PRIMARY KEY, name TEXT, user_id TEXT)")
        if table == 'playlist_tracks' or table is None:
            cursor.execute("CREATE TABLE IF NOT EXISTS playlist_tracks "
                           "(playlist_id TEXT, track_id TEXT, PRIMARY KEY(playlist_id, track_id))")
        if table == 'liked_tracks' or table is None:
            cursor.execute("CREATE TABLE IF NOT EXISTS liked_tracks "
                           "(user_id TEXT, track_id TEXT, PRIMARY KEY(user_id, track_id))")
        conn.commit()

#GET Playlist:
def get_user_playlists(user_id: str) -> List[dict]:
    playlists = []
    offset = 0
    while True:
        results = sp.user_playlists(user_id, offset=offset)
        if not results["items"]:
            break
        playlists.extend(results["items"])
        offset += len(results["items"])
    return playlists



def get_playlist_tracks(playlist_id: str) -> List[str]:
    tracks = []
    offset = 0
    while True:
        results = sp.playlist_tracks(playlist_id, offset=offset)
        if not results["items"]:
            break
        tracks.extend([item["track"]["id"] for item in results["items"]])
        offset += len(results["items"])
    return tracks




def main():
    print("Welcome to Spotify Playlist Generator!")
    user_id = SPOTIFY_USERNAME
  
    print("Program finished.")


if __name__ == "__main__":
    main()
