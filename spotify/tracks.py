def get_playlist_tracks(sp, playlist):

    tracks = []

    results = sp.playlist_items(
        playlist["id"],
        market="from_token",
        limit=100
    )

    while results:

        for item in results["items"]:

            # alguns retornos usam "track", outros "item"
            track = item.get("track") or item.get("item")

            if track is None:
                continue

            track_name = track["name"]

            artist = track["artists"][0]

            artist_name = artist["name"]
            artist_id = artist.get("id")

            if artist_id is None:
                continue

            tracks.append({
                "year": playlist["year"],
                "track_name": track_name,
                "artist_name": artist_name,
                "artist_id": artist_id
            })

        if results["next"]:
            results = sp.next(results)
        else:
            results = None

    return tracks