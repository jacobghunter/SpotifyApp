from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import SpotifyClientCredentials

load_dotenv()

scope = "user-read-playback-state"

user = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = user.currently_playing()

print(results)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


tracks = spotify.artist_top_tracks(spotify.search(q='king gizzard', type='artist', limit=1)["artists"]["items"][0]["id"])

# for i, track in enumerate(tracks["tracks"]):
#     print(i, track["name"])