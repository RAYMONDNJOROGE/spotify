from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

# Load environment variables from .env (if available)
load_dotenv()

app = Flask(__name__)

# Use environment variables if available; fallback to hardcoded values for local testing
client_id = os.getenv("SPOTIPY_CLIENT_ID", "36f9c27a476441b998215a3e7d320dc7")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET", "3c64f512eaae4daa9fffafac8ec3f871")

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

@app.route("/", methods=["GET", "POST"])
def index():
    tracks = []
    if request.method == "POST":
        query = request.form.get("query", "").strip()
        if query:
            results = sp.search(q=query, type="track", limit=5)
            tracks = results.get("tracks", {}).get("items", [])
    return render_template("index.html", tracks=tracks)

if __name__ == "__main__":
    app.run(debug=True)