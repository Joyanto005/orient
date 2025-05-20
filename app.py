from flask import Flask, Response
from refresh import update_playlist

app = Flask(__name__)

@app.route('/')
def index():
    return "Nirapotta m3u server is running"

@app.route('/playlist.m3u')
def serve_playlist():
    update_playlist()
    with open("output.m3u", "r") as f:
        content = f.read()
    return Response(content, mimetype='audio/x-mpegurl')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)