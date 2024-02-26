from flask import jsonify, request
from flask_login import login_user, login_required, logout_user
from flask_smorest import Blueprint
from flask.views import MethodView

from extensions import bcrypt, db
from models import User
from schemas.user import UserSchema

user_blp = Blueprint(
    "user",
    "user",
    url_prefix="/user",
    description="User operations",
)


@user_blp.route("/register")
class UserRegistration(MethodView):
    """ Register users """

    @user_blp.response(200, UserSchema)
    def post(self):
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

        # TODO: Check if user should be logged in during registration
        login_user(new_user)

        return new_user


@user_blp.route("/login")
class UserLogin(MethodView):
    """ Login users """

    @user_blp.response(200, UserSchema)
    def post(self):
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

        # login user to session
        login_user(user)

        return user


@user_blp.route("/logout")
class UserLogout(MethodView):
    """ Logout users """

    @user_blp.response(200)
    @login_required
    def post(self):
        logout_user()

        return jsonify({})
