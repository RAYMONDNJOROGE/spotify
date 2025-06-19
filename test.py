from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

# Replace with your credentials
client_id = "36f9c27a476441b998215a3e7d320dc7"
client_secret = "3c64f512eaae4daa9fffafac8ec3f871"

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

@app.route("/", methods=["GET", "POST"])
def index():
    tracks = []
    if request.method == "POST":
        query = request.form["query"]
        results = sp.search(q=query, type="track", limit=10)
        tracks = results["tracks"]["items"]
    return render_template("index.html", tracks=tracks)

if __name__ == "__main__":
    app.run(debug=True)