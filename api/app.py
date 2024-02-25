from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt

from models import db, User

app = Flask("react-flask-weather-app")
app.config.from_object("config")

if app.config["FLASK_DEBUG"]:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

bcrypt = Bcrypt(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/register", methods=["POST"])
def register():
    # get user details from request
    email = request.json["email"]
    password = request.json["password"]

    # check if user already exists
    user_exists = User.query.filter_by(email=email).first() is not None
    if user_exists:
        return jsonify({"error": "User already exists"}), 409

    # create user with hashed password
    hashed_pass = bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_pass)
    db.session.add(new_user)
    db.session.commit()

    session["user_id"] = new_user.id

    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })


@app.route("/login", methods=["POST"])
def login():
    # get user details from request
    email = request.json["email"]
    password = request.json["password"]

    # get user by email
    user = User.query.filter_by(email=email).first()

    # check user exists
    if not user:
        return jsonify({"error": "Unauthorized Access"}), 401

    # validate user password
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized"}), 401

    # update session user
    session["user_id"] = user.id

    return jsonify({
        "id": user.id,
        "email": user.email
    })
