from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os


API_KEY = os.environ.get("KEY")
SEARCH_API_URL = "https://developers.themoviedb.org/3/movies/get-movie-details"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"
INFO_URL = "https://api.themoviedb.org/3/movie"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-secret-key'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(300), nullable=True)
    img_url = db.Column(db.String(200), nullable=False)


class EditMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


class AddMovieTitleOnly(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


db.create_all()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i

    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods = ["GET", "POST"])
def edit():
    form = EditMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)

    if request.method == "POST" and form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.add(movie)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')

    delete_movie = Movie.query.get(movie_id)
    db.session.delete(delete_movie)
    db.session.commit()

    return redirect(url_for('home'))


@app.route("/add", methods=["GET", 'POST'])
def add():
    form = AddMovieTitleOnly()
    if request.method == "POST" and form.validate_on_submit():
        movie_title = request.form["title"]
        response = requests.get("https://api.themoviedb.org/3/search/movie",
                                params={"api_key": API_KEY, "query": movie_title})

        data = response.json()["results"]

        return render_template("select.html", result_movies = data)
    return render_template("add.html", form=form)


@app.route("/fetch", methods=["GET", 'POST'])
def fetch():
    movie_api_id = request.args.get("id")
    movie_url = f"{INFO_URL}/{movie_api_id}"
    response = requests.get(movie_url, params={"api_key": API_KEY})
    data = response.json()
    new_movie_details = Movie(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        img_url=f"{IMAGE_URL}{data['poster_path']}",
        description=data["overview"]
    )

    db.session.add(new_movie_details)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
