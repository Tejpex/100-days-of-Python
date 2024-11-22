from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return redirect(os.getenv("DOCS_URL"))


# HTTP GET - Read Record
@app.route("/all")
def get_all():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/random")
def get_random():
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random()).limit(1)).scalar()
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/search")
def search():
    search_result = (db.session.execute(db.select(Cafe).where(Cafe.location.startswith(request.args.get("loc"))))
                     .scalars().all())
    if search_result:
        return jsonify(cafes=[cafe.to_dict() for cafe in search_result])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a café at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add():
    new_cafe = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["location"],
        seats=request.form["seats"],
        has_toilet=request.form["has_toilet"].lower() == "true",
        has_wifi=request.form["has_wifi"].lower() == "true",
        has_sockets=request.form["has_sockets"].lower() == "true",
        can_take_calls=request.form["can_take_calls"].lower() == "true",
        coffee_price=request.form["coffee_price"]
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new café."}), 201


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe_to_update:
        cafe_to_update.coffee_price = request.form["new_price"]
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry, a café with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    if request.args.get("api_key") == "TopSecretAPIKey":
        cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"Success": "Successfully deleted café from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, a café with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Unauthorized": "Sorry, you don't have permission to do this. "
                                              "Do you have the correct API key?"}), 403


if __name__ == '__main__':
    app.run(debug=True)
