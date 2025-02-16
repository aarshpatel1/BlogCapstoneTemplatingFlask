from datetime import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)

current_time = datetime.now()
current_year = current_time.year

response = requests.get("https://api.npoint.io/1c9cbe9a501b252ddd2e")
all_blogs = response.json()


@app.route("/")
def home():
    return render_template("home.html", year=current_year)


@app.route("/blogs")
def get_blogs():
    return render_template("index.html", all_blogs=all_blogs, year=current_year)


@app.route("/blogs/<int:blog_id>")
def each_blog(blog_id):
    return render_template(
        "blog.html", id=blog_id, all_blogs=all_blogs, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
