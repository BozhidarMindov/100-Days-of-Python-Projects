from flask import Flask, render_template, request
import requests
import smtplib
import os

my_email = "bmindov.test@gmail.com"
password_gmail = os.environ.get("PASSWORD")

app = Flask(__name__)

def get_data():
    response = requests.get("https://api.npoint.io/741314c9f3f2c5f8e2fa")
    posts = response.json()
    return posts


def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email,
                         password=password_gmail)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: New Message \n\nName: {name}\nEmail: {email}\nPhone: {phone}\n Message:{message}"
        )
        connection.close()


@app.route('/')
def home():
    return render_template("index.html", posts=get_data())

@app.route('/index.html')
def index():
    return render_template("index.html",posts=get_data())

@app.route("/about.html")
def go_to_about():
    return render_template("about.html")

@app.route("/contact.html")
def go_to_contacts():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def display_post(num):
    posts = get_data()
    for a_post in posts:
        if a_post["id"] == num:
            return render_template("post.html", post=a_post)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(name=data["name"], email=data["email"], phone=data["phone"], message=data["message"])
        return render_template("contact.html", sent=True)
    return render_template("contact.html", sent=False)


if __name__ == "__main__":
    app.run(debug=True)