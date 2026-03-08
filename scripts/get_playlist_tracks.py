import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# -------------------------------------------------
# 1) AUTENTICAÇÃO NA API
# -------------------------------------------------

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="playlist-read-private"
    )
)

# -------------------------------------------------
# 2) BUSCAR TODAS AS PLAYLISTS
# -------------------------------------------------

results = sp.current_user_playlists(limit=50)
playlists = results["items"]

# paginação caso existam mais de 50 playlists
while results["next"]:
    results = sp.next(results)
    playlists.extend(results["items"])


# -------------------------------------------------
# 3) FILTRAR PLAYLISTS DO PROJETO (top_tracks_YYYY)
# -------------------------------------------------

project_playlists = []

for playlist in playlists:

    name = playlist["name"]

    if name.startswith("top_tracks_"):

        year = name.split("_")[-1]

        project_playlists.append({
            "year": year,
            "id": playlist["id"],
            "name": name
        })


print("\nPlaylists do projeto encontradas:\n")

for p in project_playlists:
    print(p)


print("\nBuscando músicas...\n")


# -------------------------------------------------
# 4) BUSCAR MÚSICAS DE CADA PLAYLIST
# -------------------------------------------------

tracks_data = []

for playlist in project_playlists:

    year = playlist["year"]
    playlist_id = playlist["id"]

    print(f"\nPlaylist {playlist['name']} ({year})")

    results = sp.playlist_items(
        playlist_id,
        market="from_token",
        limit=100
    )

    items = results["items"]

    for item in items:

        track = item.get("item")

        if track is None:
            continue

        track_name = track["name"]
        artist_name = track["artists"][0]["name"]

        print(year, "|", track_name, "|", artist_name)

        tracks_data.append({
            "year": year,
            "track_name": track_name,
            "artist_name": artist_name
        })


# -------------------------------------------------
# 5) SALVAR DATASET
# -------------------------------------------------

df = pd.DataFrame(tracks_data)

output_path = "data/raw/top_tracks.csv"

df.to_csv(output_path, index=False)

print(f"\nDataset salvo em: {output_path}")