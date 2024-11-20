from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(title=request.form["title"],
                        author=request.form["author"],
                        rating=float(request.form["rating"]))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    book = db.session.execute(db.select(Book).where(Book.id == request.args.get("book_id"))).scalar()
    if request.method == 'POST':
        book = db.get_or_404(Book, request.form["id"])
        new_rating = float(request.form["new-rating"])
        print(book)
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book)


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == request.args.get("book_id"))).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
