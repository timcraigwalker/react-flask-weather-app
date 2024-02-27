from flask import current_app
from flask_login import login_required
from flask_smorest import Blueprint
import requests

weather_blp = Blueprint(
    "weather",
    "weather",
    url_prefix="/weather",
    description="External weather api",
)


@weather_blp.route("/<latitude>/<longitude>", methods=["GET"])
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