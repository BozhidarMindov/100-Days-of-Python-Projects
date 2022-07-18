import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_KEY = "TopSecretAPIKey"


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def convert_to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def get_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)

    # return jsonify(cafe={
    #             "id": random_cafe.id,
    #             "name": random_cafe.name,
    #             "map_url": random_cafe.map_url,
    #             "img_url": random_cafe.img_url,
    #             "location": random_cafe.location,
    #             "seats": random_cafe.seats,
    #             "has_toilet": random_cafe.has_toilet,
    #             "has_wifi": random_cafe.has_wifi,
    #             "has_sockets": random_cafe.has_sockets,
    #             "can_take_calls": random_cafe.can_take_calls,
    #             "coffee_price": random_cafe.coffee_price,
    # })

    return jsonify(cafe=random_cafe.convert_to_dict())

@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()

    cafes_list = []
    for cafe in all_cafes:
        cafes_list.append(cafe.convert_to_dict())

    return jsonify(cafes=cafes_list)


@app.route("/search")
def search_for_cafe():
    query_loc = request.args["loc"]
    # query_loc = request.args.get("loc")
    cafe_found = db.session.query(Cafe).filter_by(location=query_loc).first()

    if cafe_found:
        return jsonify(cafe=cafe_found.convert_to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/add", methods=["GET", "POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(
        response={"success": "Successfully added the new cafe."}
    )


@app.route("/update-price/<int:cafe_id>", methods = ["GET","PATCH"])
def change_price(cafe_id):
    new_price = request.args["new_price"]
    # new_price = request.args.get("new_price") this will continue to run even if the request is bad
    cafe = db.session.query(Cafe).get(cafe_id)

    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(
            response={"success": "Successfully updated the price."}
        )
    else:
        return jsonify(
            error={"Not Found": "Sorry a cafe with that id was not found in the database."}
        )


@app.route("/report-closed/<int:cafe_id>", methods =["GET", "DELETE"])
def delete(cafe_id):
    api_key_requested = request.args.get("api-key")

    if api_key_requested == API_KEY:
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(
                response={"success": "Successfully deleted the cafe from the database."}
            ), 200
        else:
            return jsonify(
                error={"Not Found": "Sorry a cafe with that id was not found in the database."}
            ), 404
    else:
        return jsonify(
            error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}
        ), 403


if __name__ == '__main__':
    app.run(debug=True)
