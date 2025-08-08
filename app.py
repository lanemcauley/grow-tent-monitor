from flask import Flask, render_template
import os

app = Flask(__name__)
SNAPSHOT_DIR = "static/snapshots"

@app.route("/")
def index():
    images = sorted(os.listdir(SNAPSHOT_DIR), reverse=True)
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)