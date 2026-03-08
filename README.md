# spotify-eclecticism

This project analyzes **10 years of personal Spotify listening history** to measure **how eclectic my musical taste is over time**.

The analysis is based on the **Top 100 most played tracks per year**, extracted from Spotify playlists and analyzed using Python.

The goal is to explore questions such as:

- How much does my music taste change year to year?
- How many new artists appear in my yearly top tracks?
- Do my favorite songs persist over time?
- Am I becoming more musically eclectic?

---

# Project Structure

```
spotify-eclecticism
│
├── data
│   └── raw
│       └── top_tracks.csv
│
├── notebooks
│   └── exploratory_analysis.ipynb
│
├── scripts
│   ├── spotify_connect.py
│   ├── get_playlists.py
│   └── get_playlist_tracks.py
│
├── .env
├── requirements.txt
└── README.md
```

### Folders

**scripts/**  
Scripts responsible for interacting with the Spotify API.

**data/raw/**  
Raw dataset containing tracks extracted from playlists.

**notebooks/**  
Jupyter notebook used for exploratory analysis and metric calculations.

---

# Data Source

The analysis uses **Spotify yearly Top Tracks playlists**, each containing the **100 most played songs of the year**.

Example:

```
Top Tracks 2016
Top Tracks 2017
Top Tracks 2018
...
Top Tracks 2025
```

These playlists serve as the base dataset for the analysis.

---

# Important Note (Playlist Ownership Issue)

Spotify's official **"Your Top Songs YYYY"** playlists are owned by Spotify itself.

Because of this, they **may not appear when listing playlists through the Spotify API**.

To solve this, the playlists were **manually duplicated** and renamed following this pattern:

```
top_tracks_2016
top_tracks_2017
top_tracks_2018
...
top_tracks_2025
```

This ensures the playlists are **owned by your account and accessible through the API**.

---

# Setup

## 1 — Clone the repository

```bash
git clone <your-repo-url>
cd spotify-eclecticism
```

---

## 2 — Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Mac / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

---

## 3 — Install dependencies

```bash
pip install -r requirements.txt
```

---

# Spotify API Setup

To access Spotify data you must create a **Spotify Developer App**.

---

## 1 — Create a Spotify App

Go to:

https://developer.spotify.com/dashboard

Click **Create App** and fill something like:

```
App name: spotify-eclecticism
App description: Personal Spotify listening analysis
Redirect URI: http://127.0.0.1:8888/callback
```

After creating the app you will obtain:

- **Client ID**
- **Client Secret**

---

## 2 — Create `.env` file

Create a `.env` file in the root of the project.

Example:

```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

These credentials are used by the scripts to authenticate requests to the Spotify API.

---

# Preparing Your Playlists

To reproduce the analysis:

1. Locate your **Spotify "Top Songs of YEAR" playlists**
2. Duplicate each playlist
3. Rename them using the following pattern:

```
top_tracks_2016
top_tracks_2017
top_tracks_2018
...
```

This step is necessary because **Spotify-owned playlists may not appear when listing playlists through the API**.

---

# Data Extraction

## 1 — Fetch playlists

Run:

```bash
python scripts/get_playlists.py
```

This script retrieves the playlists available in your Spotify account.

---

## 2 — Extract tracks from yearly playlists

Run:

```bash
python scripts/get_playlist_tracks.py
```

This script:

- reads playlists named `top_tracks_YYYY`
- extracts track metadata
- saves the dataset to:

```
data/raw/top_tracks.csv
```

---

# Analysis

Open the notebook:

```
notebooks/exploratory_analysis.ipynb
```

The notebook calculates metrics such as:

- yearly artist diversity
- genre distribution
- song persistence between years
- musical novelty over time

---

# Example Questions Explored

Some of the questions explored in the analysis include:

- How many **new artists appear every year?**
- How stable are my **favorite tracks year to year?**
- Is my listening behavior **becoming more diverse?**
- Do I revisit the same artists or constantly discover new ones?

---

# Technologies Used

- Python
- Spotify Web API
- pandas
- Jupyter Notebook