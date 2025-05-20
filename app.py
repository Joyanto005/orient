from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def serve_m3u():
    with open('output.m3u', 'r') as f:
        content = f.read()
    return Response(content, mimetype='application/x-mpegURL')

if __name__ == '__main__':
    app.run()