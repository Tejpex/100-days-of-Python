import os
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_API_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_BASE_URL = "https://api.spotify.com/v1/"
REDIRECT_URL = "https://open.spotify.com/"

date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

# ------------------ Get songs from Billboard ----------------------
billboard_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
billboard_response = requests.get(f"{BILLBOARD_BASE_URL}/{date}", headers=billboard_header)
website = billboard_response.text

soup = BeautifulSoup(website, "html.parser")
songs = soup.find_all(name="h3", class_="a-no-trucate")
list_of_titles = [song.getText().strip() for song in songs]

# ------------------- Authorize Spotify --------------------
user = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_API_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri=REDIRECT_URL,
    scope="playlist-modify-private user-read-private user-read-email playlist-modify-public"))

token_request = SpotifyOAuth(
    client_id=SPOTIFY_API_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri=REDIRECT_URL,
    scope="playlist-modify-private user-read-private user-read-email playlist-modify-public")

user_response = token_request.get_access_token()
access_token = user_response["access_token"]

user_id = user.current_user()["id"]
SPOTIFY_USERNAME = user_id

# ------------------ Create A Playlist -----------------
playlist_body = {
    "name": f"Billboard {year}",
    "description": "The top 100 songs from Billboard.",
}
playlist_header = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
playlist_response = requests.post(
    f"{SPOTIFY_BASE_URL}users/{SPOTIFY_USERNAME}/playlists",
    json=playlist_body,
    headers=playlist_header
)
playlist_data = playlist_response.json()
playlist_id = playlist_data["id"]

# ------------------- Find Song URIs ---------------------
song_header = {
    "Authorization": f"Bearer {access_token}",
}
song_uris = []
for title in list_of_titles:
    song_params = {
        "q": f"track:{title}",
        "type": "track",
        "market": "SE",
        "limit": 1
    }
    song_response = requests.get(
        "https://api.spotify.com/v1/search",
        params=song_params, headers=song_header)
    song_data = song_response.json()
    if song_response.status_code != 200:
        print("There was a problem with the song search.")
        print("Response body:", song_response.text)
    else:
        try:
            uri = song_data["tracks"]["items"][0]["uri"]
        except IndexError:
            print(f"IndexError: No song found.")
        else:
            song_uris.append(uri)

print("song_uris")

# ------------------ Add Songs To Playlist ----------------
add_song_body = {
    "uris": song_uris
}
add_song_response = requests.post(
    f"{SPOTIFY_BASE_URL}playlists/{playlist_id}/tracks",
    json=add_song_body,
    headers=playlist_header
)
add_song_data = add_song_response.text
print(add_song_data)
