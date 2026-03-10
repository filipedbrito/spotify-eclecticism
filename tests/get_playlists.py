import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="playlist-read-private"
    )
)

# buscar playlists do usuário
results = sp.current_user_playlists(limit=50)
playlists = results["items"]

# paginação (caso tenha mais de 50)
while results["next"]:
    results = sp.next(results)
    playlists.extend(results["items"])

print("\nPlaylists do projeto encontradas:\n")

for playlist in playlists:

    name = playlist["name"]

    # filtrar apenas playlists top_tracks_YYYY
    if name.startswith("top_tracks_"):

        print(
            name,
            "| id:",
            playlist["id"]
        )