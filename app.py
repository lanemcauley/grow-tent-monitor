from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)
SNAPSHOT_DIR = "static/snapshots"
CURRENT_SNAPSHOT_DIR = "static/current_snapshot"

@app.route("/")
def index():
    images = sorted(os.listdir(SNAPSHOT_DIR), reverse=True)
    current_image = ""
    try:
        subprocess.Popen("/home/lane/grow-tent-monitor/capture_current_image.py", shell=True)
        current_image = sorted(os.listdir(CURRENT_SNAPSHOT_DIR), reverse=True)
    except:
        pass
    return render_template("index.html", images=images, current_image=current_image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)