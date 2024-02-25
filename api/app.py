from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user

from models import db, migrate, User

app = Flask("react-flask-weather-app")
app.config.from_object("config")

if app.config["FLASK_DEBUG"]:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

login_manager = LoginManager()

bcrypt = Bcrypt(app)
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


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

    login_user(user)

    '''# update session user
    session["user_id"] = user.id

    # update user's last login time
    user.last_login = datetime.utcnow()
    db.session.commit()'''

    return jsonify({
        "id": user.id,
        "email": user.email
    })


@app.route("/logout", methods=["POST", "GET"])
@login_required
def logout():
    logout_user()

    return jsonify({})
