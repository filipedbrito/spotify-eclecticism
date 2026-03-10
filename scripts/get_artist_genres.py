import pandas as pd

from spotify.auth import get_public_client
from spotify.artists import get_artists_genres
from config import DATA_RAW_PATH


# -------------------------------------------------
# 1) CONECTAR NA API DO SPOTIFY
# -------------------------------------------------
sp = get_public_client()


# -------------------------------------------------
# 2) CARREGAR DATASET DE TRACKS
# -------------------------------------------------
tracks = pd.read_csv(f"{DATA_RAW_PATH}/top_tracks.csv")


# -------------------------------------------------
# 3) EXTRAIR LISTA ÚNICA DE ARTISTAS
# -------------------------------------------------
artist_ids = tracks["artist_id"].dropna().unique().tolist()

print("Total de artistas:", len(artist_ids))


# -------------------------------------------------
# 4) BUSCAR GÊNEROS DOS ARTISTAS NA API
# -------------------------------------------------
# usa função do módulo spotify.artists que faz requisições em batch (até 50 artistas por vez)
artists = get_artists_genres(sp, artist_ids)


# -------------------------------------------------
# 5) CONVERTER RESULTADO PARA DATAFRAME
# -------------------------------------------------
df = pd.DataFrame(artists)


# -------------------------------------------------
# 6) SALVAR DATASET DE GÊNEROS
# -------------------------------------------------
output_path = f"{DATA_RAW_PATH}/artist_genres.csv"

df.to_csv(output_path, index=False)

print("Dataset salvo em:", output_path)