from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

LASTFM_USER = "mrcschnwndt"
API_KEY = "bc5ab33861e059b1cb3e171821426401"

# Define route for serving HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Define route for serving current song data
@app.route('/current-song')
def current_song():
    lastfm_url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={LASTFM_USER}&api_key={API_KEY}&format=json&limit=1"
    response = requests.get(lastfm_url)
    data = response.json()
    # Get the first track (most recent)
    track = data["recenttracks"]["track"][0]
    artist_name = track["artist"]["#text"]
    track_name = track["name"]
    album_name = track["album"]["#text"]
    album_cover = track["image"][-1]["#text"]  # Use the largest available image
    song_info = {
        "artist_name": artist_name,
        "track_name": track_name,
        "album_name": album_name,
        "album_cover": album_cover
    }
    return jsonify(song_info)

if __name__ == '__main__':
    app.run(debug=True)
