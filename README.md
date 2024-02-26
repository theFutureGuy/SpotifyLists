# SpotifyLists

  This Python script generates Spotify playlists based on a seed playlist or liked tracks. It utilizes the Spotify API and Spotipy library for interaction with the Spotify platform.

  ## Features:

  - Refresh playlists from Spotify and save them locally.
  - List user's Spotify playlists.
  - Generate a new playlist based on a seed playlist or liked tracks.
  - Specify the number of tracks to include in the generated playlist.
  - Choose to include only new artists in the generated playlist.
  - Use all tracks in the seed playlist as seeds for generating the new playlist.
    


 ## Available options:

 - refresh: Refresh playlists from Spotify and save them locally.
 - list-playlists: List user's Spotify playlists.
 - seed-playlist <playlist_id>: Generate a new playlist based on the specified seed playlist ID.
 - number-tracks <num>: Specify the number of tracks to include in the generated playlist (default is 20).
 - new-artists: Include only new artists in the generated playlist.
 - use_all: Use all tracks in the seed playlist as seeds for generating the new playlist.
  
## Prerequisites:

  - Python 3.x
  - Spotify Developer Account (to obtain API credentials)
  - Spotipy library (`pip install spotipy`)
  - SQLite database

  ## Setup:

  1. Clone the repository:

     ```
     git clone https://github.com/theFutureGuy/SpotifyLists/.git
     ```

  2. Navigate to the project directory:

     ```
     cd SpotifyLists
     ```

  3. Install dependencies:

     ```
     pip install -r requirements.txt
     ```

  4. Set up environment variables:
     - Create a `.env` file in the project directory.
     - Add the following variables with your Spotify API credentials:

     ```
     SPOTIFY_CLIENT_ID=your_client_id
     SPOTIFY_SECRET=your_client_secret
     SPOTIFY_REDIRECT_URI=your_redirect_uri
     SPOTIFY_USERNAME=your_spotify_username
     ```

  ## Usage:

  Run the script with Python:
  ```
  python main.py
  ```


## Script Explanation:

#### Purpose:
The script is a Python application that generates Spotify playlists based on a seed playlist or liked tracks. It utilizes the Spotify API via the Spotipy library to interact with the Spotify platform.

#### Key Components:

1. **Imports**: The script imports necessary libraries such as `argparse`, `os`, `sqlite3`, `spotipy`, and `dotenv`.

2. **Environment Setup**: It loads environment variables from a `.env` file using `dotenv`. These variables include Spotify API credentials and other configuration parameters.

3. **Argument Parsing**: The script utilizes `argparse` to parse command-line arguments. Users can specify various options like refreshing playlists, listing playlists, specifying a seed playlist, number of tracks to generate, etc.

4. **Spotify Authentication**: It uses SpotifyOAuth from `spotipy.oauth2` to authenticate with Spotify using the provided API credentials.

5. **Database Operations**: The script interacts with a SQLite database (`playlists.db`) to store playlists, playlist tracks, and liked tracks locally.

6. **Playlist Generation**: It generates new playlists by retrieving recommendations from Spotify based on a seed playlist or liked tracks. Users can specify options like including only new artists or using all tracks in the seed playlist as seeds.

7. **Main Functionality**: The main function orchestrates the entire process, including refreshing playlists, listing playlists, and generating new playlists based on user inputs.


#####  Feel free to contribute to this project and contact.
[@theFutureGuy](https://github.com/theFutureGuy/)



