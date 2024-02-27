from flask import abort, make_response, request
from flask_login import login_user, login_required, logout_user
from flask_smorest import Blueprint
from flask.views import MethodView
from marshmallow import ValidationError

from extensions import bcrypt, db
from models import User
from schemas.user import UserSchema, UserResponseSchema

user_blp = Blueprint(
    "user",
    "user",
    url_prefix="/user",
    description="User operations",
)
user_schema = UserSchema()


def validate_user_input():
    # check user data is passed
    user_json = request.get_json()
    if not user_json:
        abort(
            make_response(
                {
                    "message": "Missing input data",
                    "code": 400,
                },
                400,
            )
        )

    # validate and deserialize input
    try:
        user_data = user_schema.load(
            user_json,
            instance=User(),
            session=db.session
        )
    except ValidationError as err:
        abort(
            make_response(
                {
                    "message": err.messages,
                    "code": 422,
                },
                422,
            )
        )

    return user_data


@user_blp.route("/register")
class UserRegistrationView(MethodView):
    """ Register user """

    @user_blp.response(200, UserResponseSchema)
    def post(self):
        user_data = validate_user_input()

        # check if user already exists
        user_exists = (
            User.query.filter_by(email=user_data.email).first() is not None
        )
        if user_exists:
            abort(
                make_response(
                    {
                        "message": "User already exists",
                        "code": 409,
                    },
                    409,
                )
            )

        # create user with hashed password
        hashed_pass = bcrypt.generate_password_hash(user_data.password)
        new_user = User(email=user_data.email, password=hashed_pass)
        db.session.add(new_user)
        db.session.commit()

        # TODO: Check if user should be logged in during registration
        login_user(new_user)

        return new_user


@user_blp.route("/login")
class UserLoginView(MethodView):
    """ Login user """

    @user_blp.response(200, UserResponseSchema)
    def post(self):
        user_data = validate_user_input()

        # get user by email
        user = User.query.filter_by(email=user_data.email).first()

        # check user exists
        if not user:
            abort(
                make_response(
                    {
                        "message": "Unauthorized Access",
                        "code": 401,
                    },
                    401,
                )
            )

        # validate user password
        if not bcrypt.check_password_hash(user.password, user_data.password):
            abort(
                make_response(
                    {
                        "message": "Unauthorized",
                        "code": 401,
                    },
                    401,
                )
            )

        # login user to session
        login_user(user)

        return user


@user_blp.route("/logout")
class UserLogoutView(MethodView):
    """ Logout user """

    @user_blp.response(200)
    @login_required
    def post(self):
        logout_user()

        return make_response({}), 200
