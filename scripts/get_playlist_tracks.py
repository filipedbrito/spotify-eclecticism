import pandas as pd

from spotify.auth import get_user_client
from spotify.playlists import get_all_playlists, get_project_playlists
from spotify.tracks import get_playlist_tracks
from config import DATA_RAW_PATH


# -------------------------------------------------
# 1) conectar
# -------------------------------------------------

sp = get_user_client()

# -------------------------------------------------
# 2) buscar playlists
# -------------------------------------------------

playlists = get_all_playlists(sp)

project_playlists = get_project_playlists(playlists)

print("\nPlaylists encontradas:\n")

for p in project_playlists:
    print(p)


# -------------------------------------------------
# 3) buscar músicas
# -------------------------------------------------

tracks_data = []

for playlist in project_playlists:

    print(f"\nPlaylist {playlist['name']}")

    tracks = get_playlist_tracks(sp, playlist)

    tracks_data.extend(tracks)


# -------------------------------------------------
# 4) salvar dataset
# -------------------------------------------------

df = pd.DataFrame(tracks_data)

output_path = f"{DATA_RAW_PATH}/top_tracks.csv"

print("Total de tracks coletadas:", len(tracks_data))

df.to_csv(output_path, index=False)

print(f"\nDataset salvo em: {output_path}")