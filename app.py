from flask import Flask, render_template, jsonify
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/currently-playing')
def currently_playing():
    scope = "user-read-currently-playing"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id='a5f6ed27ca2b416daa27d5e39f5f5877',
                                                  client_secret='a5ae4fd03e1f4d0ea1120a4d7d0d4c4c',
                                                  redirect_uri='http://localhost:5000/callback'))
    current_track = sp.current_user_playing_track()
    if current_track is not None and current_track['is_playing']:
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        album_name = current_track['item']['album']['name']
        album_cover_url = current_track['item']['album']['images'][0]['url']
        return jsonify(track_name=track_name, artist_name=artist_name,
                       album_name=album_name, album_cover_url=album_cover_url)
    else:
        return jsonify(track_name='No track currently playing')

if __name__ == '__main__':
    app.run()
