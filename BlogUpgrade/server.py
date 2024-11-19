from flask import Flask, render_template, request
import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

smtp_address = os.getenv("SMTP_ADDRESS")
smtp_key = os.getenv("SMTP_PASSWORD")
my_email = os.getenv("MY_EMAIL")
to_email = os.getenv("TO_EMAIL")

app = Flask(__name__)
url = os.getenv("N_POINT")


@app.route("/")
def home():
    response = requests.get(url)
    data = response.json()
    return render_template("index.html", blog=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        mail_to_send = (f"Subject: New Blog Message! \n\n"
                        f"Name: {name} \nEmail: {email} \nPhone: {phone} \nMessage: {message}")
        with smtplib.SMTP(smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=smtp_key)
            connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=mail_to_send)
        return render_template("contact.html", message_sent=True)
    else:
        return render_template("contact.html", message_sent=False)


@app.route("/post/<blog_id>")
def view_post(blog_id):
    response = requests.get(url)
    data = response.json()
    requested_post = [post for post in data if post["id"] == int(blog_id)][0]
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
