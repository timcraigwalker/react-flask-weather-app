from flask import Flask
from flask_smorest import Blueprint

from extensions import api, bcrypt, db, login_manager, migrate
from models import User
from views import (
    auth_blp,
    cities_blp,
    user_blp,
    user_favourite_city_blp,
    weather_blp
)


def create_app(testing=False):
    app = Flask("react-flask-weather-app")
    app.config.from_object("config")
    app.url_map.strict_slashes = False

    if testing is True:
        app.config["TESTING"] = True
        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "sqlite:///test_weatherapp.db"
        app.config["LOGIN_DISABLED"] = True

    configue_extensions(app)
    register_bluprints(api)

    return app


def configue_extensions(app):
    api.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    if not app.config["TESTING"]:
        with app.app_context():
            db.create_all()


def register_bluprints(api):
    api_blp = Blueprint(
        "api",
        "api",
        url_prefix="/api",
        description="Flask API views",
    )

    api_blp.register_blueprint(auth_blp, path="auth")
    api_blp.register_blueprint(cities_blp, path="cities")
    api_blp.register_blueprint(user_blp, path="user")
    api_blp.register_blueprint(
        user_favourite_city_blp,
        path="user/<user_id>/favourite_cities"
    )
    api_blp.register_blueprint(weather_blp, path="weather")

    api.register_blueprint(api_blp, path="api")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
