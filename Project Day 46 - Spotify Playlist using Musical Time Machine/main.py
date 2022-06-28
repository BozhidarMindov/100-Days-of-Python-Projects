import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

user_input = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD.")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_input}/")

#web scraping and finding the song names
soup = BeautifulSoup(response.text,"html.parser")
songs = soup.select(selector="li ul li h3")
song_names = [song.getText().strip("\n\t") for song in songs]
print(song_names)

#acessing the Spotify API

SPOTIFY_CLIENT_ID = os.environ.get("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

#creating the playlist and adding songs to it
song_list = []
year = user_input.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1, market="US")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_list)