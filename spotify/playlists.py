from config import PLAYLIST_PREFIX, PLAYLIST_LIMIT


def get_all_playlists(sp):

    results = sp.current_user_playlists(limit=PLAYLIST_LIMIT)
    playlists = results["items"]

    while results["next"]:
        results = sp.next(results)
        playlists.extend(results["items"])

    return playlists


def get_project_playlists(playlists):

    project_playlists = []

    for playlist in playlists:

        name = playlist["name"]

        if name.startswith(PLAYLIST_PREFIX):

            year = name.split("_")[-1]

            project_playlists.append({
                "year": year,
                "id": playlist["id"],
                "name": name
            })

    return project_playlists