from flask import Flask, Response
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("output.m3u", "r") as f:
            content = f.read()
        return Response(content, mimetype="application/x-mpegURL")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)