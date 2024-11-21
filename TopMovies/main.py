from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

API_KEY = os.getenv("API_KEY")
API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = "https://api.themoviedb.org/3/"


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(500))
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


with app.app_context():
    db.create_all()


class EditForm(FlaskForm):
    rating = StringField("Your rating out of 10 eg. 7.5", validators=[DataRequired()])
    review = StringField("Your Review")
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    ranking_num = len(all_movies)
    for movie in all_movies:
        movie.ranking = ranking_num
        ranking_num -= 1
    db.session.commit()

    return render_template("index.html", movie_list=all_movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        params = {
            "query": title
        }
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {API_TOKEN}"
        }
        response = requests.get(f"{BASE_URL}search/movie", params=params, headers=headers)
        response.raise_for_status()
        data = response.json()["results"]
        return render_template("select.html", movies=data)
    return render_template("add.html", form=form)


@app.route("/select", methods=['GET', 'POST'])
def select():
    movie_id = request.args.get("movie_id")
    params = {
        "api_key": API_KEY
    }
    response = requests.get(f"{BASE_URL}movie/{movie_id}", params=params)
    response.raise_for_status()
    data = response.json()
    new_movie = Movie(
        title=data["original_title"],
        year=data["release_date"].split("-")[0],
        description=data["overview"],
        rating=0,
        ranking=0,
        review="Write a review",
        img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    created_movie = db.session.execute(db.select(Movie).where(Movie.title == data["original_title"])).scalar()
    created_id = created_movie.id
    return redirect(url_for('edit', movie_id=created_id))


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie = db.session.execute(db.select(Movie).where(Movie.id == request.args.get("movie_id"))).scalar()
    if form.validate_on_submit():
        try:
            movie.rating = float(form.rating.data)
        except ValueError:
            movie.rating = movie.rating
        finally:
            new_review = form.review.data
            if new_review:
                movie.review = new_review
            db.session.commit()
        return redirect(url_for("home"))
    return render_template('edit.html', movie=movie, form=form)


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == request.args.get("movie_id"))).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
