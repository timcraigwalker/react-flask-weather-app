from flask import jsonify, request
from flask_login import login_required
from flask.views import MethodView
from flask_smorest import Blueprint

from extensions import db
from models import UserFavouriteCity
from schemas.user_favourite_city import UserFavouriteCitySchema

user_favourite_city_blp = Blueprint(
    "user/<user_id>/favourite_cities",
    "user/<user_id>/favourite_cities",
    url_prefix="/user/<user_id>/favourite_cities",
    description="User favourite cities operations",
)


@user_favourite_city_blp.route("/")
class UserFavouriteCities(MethodView):
    """ CRUD User favourite cities """

    @user_favourite_city_blp.response(200, UserFavouriteCitySchema(many=True))
    @login_required
    def get(self, user_id):
        return UserFavouriteCity.query.filter_by(user_id=user_id).all()

    @user_favourite_city_blp.response(200, UserFavouriteCitySchema)
    @login_required
    def post(self, user_id):
        city = request.json["city"]
        latitude = request.json["latitude"]
        longitude = request.json["longitude"]

        favourite_exists = (
            UserFavouriteCity.query
            .filter_by(user_id=user_id)
            .filter_by(city=city)
            .filter_by(latitude=latitude)
            .filter_by(longitude=longitude)
            .first()
        )
        if favourite_exists:
            return jsonify(
                {"error": "User favourite city already exists"}
            ), 409

        new_favourite_city = UserFavouriteCity(
            user_id=user_id,
            city=city,
            latitude=latitude,
            longitude=longitude
        )
        db.session.add(new_favourite_city)
        db.session.commit()

        return new_favourite_city
