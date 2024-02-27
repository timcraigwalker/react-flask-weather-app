from flask import abort, make_response, request
from flask_login import login_required
from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import ValidationError

from extensions import db
from models import UserFavouriteCity
from schemas.user_favourite_city import UserFavouriteCitySchema

user_favourite_city_blp = Blueprint(
    "user/<user_id>/favourite_cities",
    "user/<user_id>/favourite_cities",
    url_prefix="/user/<user_id>/favourite_cities",
    description="User favourite cities operations",
)
user_favourite_city_schema = UserFavouriteCitySchema()


def validate_favourite_city_input():
    # check favourite city data is passed
    favourite_city_json = request.get_json()
    if not favourite_city_json:
        return abort(
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
        favourite_city_data = user_favourite_city_schema.load(
            favourite_city_json,
            instance=UserFavouriteCity(),
            session=db.session
        )
    except ValidationError as err:
        return abort(
            make_response(
                {
                    "message": err.messages,
                    "code": 422,
                },
                422,
            )
        )

    return favourite_city_data


@user_favourite_city_blp.route("/")
class UserFavouriteCitiesView(MethodView):
    """ CRUD User favourite cities """

    @user_favourite_city_blp.response(200, UserFavouriteCitySchema(many=True))
    @login_required
    def get(self, user_id):
        return UserFavouriteCity.query.filter_by(user_id=user_id).all()

    @user_favourite_city_blp.response(200, UserFavouriteCitySchema)
    @login_required
    def post(self, user_id):
        favourite_city_data = validate_favourite_city_input()

        # check if favourite city already exists
        favourite_exists = (
            UserFavouriteCity.query
            .filter_by(user_id=user_id)
            .filter_by(city=favourite_city_data.city)
            .filter_by(latitude=favourite_city_data.latitude)
            .filter_by(longitude=favourite_city_data.longitude)
            .first()
        )
        if favourite_exists:
            return abort(
                make_response(
                    {
                        "message": "User favourite city already exists",
                        "code": 409,
                    },
                    409,
                )
            )

        # store favourite city to db
        new_favourite_city = favourite_city_data
        new_favourite_city.user_id = user_id
        db.session.add(favourite_city_data)
        db.session.commit()

        return favourite_city_data

    @user_favourite_city_blp.response(200)
    @login_required
    def delete(self, user_id):
        favourite_city_data = validate_favourite_city_input()

        # try to get favourite city
        favourite_city = (
            UserFavouriteCity.query
            .filter_by(user_id=user_id)
            .filter_by(city=favourite_city_data.city)
            .filter_by(latitude=favourite_city_data.latitude)
            .filter_by(longitude=favourite_city_data.longitude)
            .first()
        )
        if not favourite_city:
            return make_response({}), 204

        # delete favourite city from db
        db.session.delete(favourite_city)
        db.session.commit()

        return make_response({}), 200


@user_favourite_city_blp.route("/<user_favourite_city_id>")
class UserFavouriteCityView(MethodView):
    """ CRUD User favourite city """

    @user_favourite_city_blp.response(200, UserFavouriteCitySchema())
    @login_required
    def get(self, user_id, user_favourite_city_id):
        return UserFavouriteCity.query.get(user_favourite_city_id)

    @user_favourite_city_blp.response(200)
    @login_required
    def delete(self, user_id, user_favourite_city_id):
        # try to get favourite city
        favourite_city = UserFavouriteCity.query.get(user_favourite_city_id)
        if not favourite_city:
            return make_response({}), 204

        # check favourite city belongs to user
        if favourite_city.user_id != user_id:
            return abort(
                make_response(
                    {
                        "message": "Unauthorized",
                        "code": 401,
                    },
                    401,
                )
            )

        # delete favourite city from db
        db.session.delete(favourite_city)
        db.session.commit()

        return make_response({}), 200
