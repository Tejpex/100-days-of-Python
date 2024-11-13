from flask import Flask, render_template
import requests

app = Flask(__name__)
age_url = "https://api.agify.io/"
gender_url = "https://api.genderize.io/"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guess/<name>")
def guess(name):
    params = {
        "name": name,
        "country_id": "SE"
    }
    age_response = requests.get(url=age_url, params=params)
    age = age_response.json()["age"]
    gender_response = requests.get(url=gender_url, params=params)
    gender = gender_response.json()["gender"]
    print(gender)
    return render_template("guess.html", name=name.title(),
                           age=age, gender=gender)


@app.route("/blog")
def blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)
