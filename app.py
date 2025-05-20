from flask import Flask, send_file
from refresh import update_playlist

app = Flask(__name__)

@app.route('/')
def home():
    return "M3U Auto-Refresh Service is Running"

@app.route('/output.m3u')
def serve_m3u():
    update_playlist()
    return send_file("output.m3u", mimetype="application/x-mpegURL")