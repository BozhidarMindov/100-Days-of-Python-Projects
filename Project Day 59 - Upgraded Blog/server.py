from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_data():
    response = requests.get("https://api.npoint.io/741314c9f3f2c5f8e2fa")
    posts = response.json()
    return posts


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




if __name__ == "__main__":
    app.run(debug=True)