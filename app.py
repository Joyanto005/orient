from flask import Flask, send_file
from refresh import update_playlist
import os

app = Flask(__name__)

@app.route('/')
def serve_playlist():
    update_playlist()
    return send_file('output.m3u', mimetype='application/x-mpegURL')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))