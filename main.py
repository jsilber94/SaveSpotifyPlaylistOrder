import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

os.environ["SPOTIPY_CLIENT_ID"] = "***********"
os.environ["SPOTIPY_CLIENT_SECRET"] = "***********"
os.environ["SPOTIPY_REDIRECT_URI"] = "***********"

scope = "user-library-read"
temp = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=temp)

f = open("spotifysongs.txt",  "w+", encoding="utf-16")
currentOffset = 0
currentIndex = 0
for i in range(40):
    results = sp.current_user_saved_tracks(limit=50, offset=currentOffset)
    for idx, item in enumerate(results['items']):
        currentIndex += 1
        track = item['track']
        print(currentIndex, track['artists'][0]['name'], " – ", track['name'])
        writeMe = track['artists'][0]['name'] + "," + track['name']
        f.write(str(writeMe + "\n").replace("’", "'"))

    currentOffset += 50

f.close()
