from flask import current_app
from flask_login import login_required
from flask_smorest import Blueprint
import requests

api_blp = Blueprint(
    "api",
    "api",
    url_prefix="/api",
    description="External apis",
)


@api_blp.route("/cities/", methods=["GET"], defaults={"name_prefix": ""})
@api_blp.route("/cities/<name_prefix>", methods=["GET"])
@login_required
def cities(name_prefix):
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

    params = {"maxPopulation": "1000000", "namePrefix": name_prefix}

    headers = {
        "X-RapidAPI-Key": current_app.config["RAPID_API_KEY"],
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=params)

    return response.json()


@api_blp.route("/weather/<latitude>/<longitude>", methods=["GET"])
@login_required
def weather(latitude, longitude):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "appid": current_app.config["OPENWEATHER_API_KEY"],
        "lat": latitude,
        "lon": longitude
    }

    response = requests.get(url, params=params)

    return response.json()
