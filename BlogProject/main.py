from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("index.html", blog=data)


@app.route("/post/<blog_id>")
def view_post(blog_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    requested_post = [post for post in data if post["id"] == int(blog_id)][0]
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
