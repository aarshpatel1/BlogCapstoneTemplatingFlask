from datetime import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_blogs():
    response = requests.get("https://api.npoint.io/1c9cbe9a501b252ddd2e")
    all_blogs = response.json()
    return render_template("index.html", all_blogs=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)
