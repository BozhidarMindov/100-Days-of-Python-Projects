from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

#function which is getting the posts data
def get_post_data():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url).json()
    all_posts = []
    for post in response:
        single_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
        all_posts.append(single_post)
    return all_posts

#app starter
@app.route('/')
def home():
    return render_template("index.html", posts=get_post_data())

#route on which the needed post will be displayed
@app.route("/post/<int:index>")
def display_post(index):
    posts = get_post_data()
    for a_post in posts:
        if a_post.id == index:
            return render_template("post.html", post=a_post)

if __name__ == "__main__":
    app.run(debug=True)
