import time


def get_artists_genres(sp, artist_ids):

    artists_data = []

    for i in range(0, len(artist_ids), 50):

        batch = artist_ids[i:i+50]

        print(f"Buscando artistas {i} - {i+len(batch)}")

        results = sp.artists(batch)

        for artist in results["artists"]:

            if artist is None:
                continue

            artists_data.append({
                "artist_id": artist["id"],
                "artist_name": artist["name"],
                "genres": artist["genres"]
            })

        # pequena pausa para evitar rate limit
        time.sleep(1)

    return artists_data