from flask import Flask
from flask_login import login_required
import requests

from extensions import api, bcrypt, db, login_manager, migrate
from models import User, UserFavouriteCity
from views import user_blp, user_favourite_city_blp

app = Flask("react-flask-weather-app")
app.config.from_object("config")

if app.config["FLASK_DEBUG"]:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

api.init_app(app)
bcrypt.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

with app.app_context():
    db.create_all()

api.register_blueprint(user_blp, path="user")
api.register_blueprint(
    user_favourite_city_blp,
    path="user/<user_id>/favourite_cities"
)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/api/cities/", methods=["GET"], defaults={"name_prefix": ""})
@app.route("/api/cities/<name_prefix>", methods=["GET"])
@login_required
def cities(name_prefix):
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

    params = {"maxPopulation": "1000000", "namePrefix": name_prefix}

    headers = {
        "X-RapidAPI-Key": app.config["RAPID_API_KEY"],
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=params)

    return response.json()


@app.route("/api/weather/<latitude>/<longitude>", methods=["GET"])
@login_required
def weather(latitude, longitude):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "appid": app.config["OPENWEATHER_API_KEY"],
        "lat": latitude,
        "lon": longitude
    }

    response = requests.get(url, params=params)

    return response.json()
