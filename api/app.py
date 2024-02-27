from flask import Flask

from api.extensions import api, bcrypt, db, login_manager, migrate
from api.models import User
from api.views import api_blp, user_blp, user_favourite_city_blp


def create_app(testing=False):
    app = Flask("react-flask-weather-app")
    app.config.from_object("api.config")

    if testing is True:
        app.config["TESTING"] = True
        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "sqlite:///test_weatherapp.db"

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
    api.register_blueprint(api_blp, path="api")
    api.register_blueprint(user_blp, path="user")
    api.register_blueprint(
        user_favourite_city_blp,
        path="user/<user_id>/favourite_cities"
    )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
