from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

# Route with spaces in the URL
@app.route("/How-To-Create-A-Song")
def how_to_create_a_song():
    return render_template("create-song.html")

if __name__ == "__main__":
    print("Starting Waitress server on http://127.0.0.1:5000")
    serve(app, host="127.0.0.1", port=5000)
