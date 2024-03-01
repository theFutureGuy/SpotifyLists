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

def get_and_save_liked_tracks(user_id: str):
    liked_tracks = set()
    offset = 0
    while True:
        results = sp.current_user_saved_tracks(limit=50, offset=offset)
        if not results["items"]:
            break
        liked_tracks.update([item["track"]["id"] for item in results["items"]])
        offset += len(results["items"])

    with sqlite3.connect("playlists.db") as conn:
        cursor = conn.cursor()
        create_tables_if_not_exists(table='liked_tracks')
        cursor.executemany("REPLACE INTO liked_tracks (user_id, track_id) VALUES (?, ?)",
                           [(user_id, track_id) for track_id in liked_tracks])
        conn.commit()

def display_playlist_tracks(playlist_id: str, user_id: str) -> None:
    tracks = get_playlist_tracks(playlist_id)
    with sqlite3.connect("playlists.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT track_id FROM liked_tracks WHERE user_id = ?", (user_id,))
        liked_track_ids = set([row[0] for row in cursor.fetchall()])

    for idx, track_id in enumerate(tracks):
        track = sp.track(track_id)
        heart_symbol = "<3" if track_id in liked_track_ids else ""
        print(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']} {heart_symbol}")

def save_playlists_to_db(playlists: List[dict], user_id: str):
    with sqlite3.connect("playlists.db") as conn:
        cursor = conn.cursor()
        create_tables_if_not_exists(table='plalylists')
        cursor.executemany("REPLACE INTO playlists (id, name, user_id) VALUES (?, ?, ?)",
                           [(pl["id"], pl["name"], user_id) for pl in playlists])

        create_tables_if_not_exists(table='playlist_tracks')
        for pl in playlists:
            tracks = get_playlist_tracks(pl["id"])
            cursor.executemany("REPLACE INTO playlist_tracks (playlist_id, track_id) VALUES (?, ?)",
                               [(pl["id"], track_id) for track_id in tracks])

        conn.commit()

def main():
    print("Welcome to Spotify Playlist Generator!")
    user_id = SPOTIFY_USERNAME
  
    print("Program finished.")


if __name__ == "__main__":
    main()
