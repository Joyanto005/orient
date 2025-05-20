from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def serve_m3u():
    return send_file("output.m3u", mimetype="application/x-mpegURL")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)