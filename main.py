from bs4 import BeautifulSoup
import requests
import spotipy

SPOTIFY_ID="a9eb1f7746c54f13b44c28301ecb16bb"
SPOTIFY_KEY="79bf968f48a14a4e93ea264c4e2d4258"

date = input("Which date do you want to travel to? Type the date in the format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
songs_names_h3 = soup.select(".o-chart-results-list__item h3.c-title")
songs_names = [song.getText().strip() for song in songs_names_h3]
print(songs_names)

sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_KEY,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
year=date.split('-')[0]

for song in songs_names:
    result=sp.search(q=f"track:{song} year:{year}",type="track")
    print(result)
    