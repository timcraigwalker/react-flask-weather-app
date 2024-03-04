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


@weather_blp.route(
    "/<latitude>/<longitude>",
    methods=["GET"],
    tags=["weather"]
)
@login_required
def weather(latitude, longitude):
    url = "https://api.openweathermap.org/data/3.0/onecall"

    params = {
        "appid": current_app.config["OPENWEATHER_API_KEY"],
        "units": "metric",
        "exclude": "minutely,hourly,alerts",
        "lat": latitude,
        "lon": longitude
    }

    response = requests.get(url, params=params)

    return response.json()


@weather_blp.route(
    "current/<latitude>/<longitude>",
    methods=["GET"],
    tags=["weather"]
)
@login_required
def current(latitude, longitude):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "appid": current_app.config["OPENWEATHER_API_KEY"],
        "units": "metric",
        "lat": latitude,
        "lon": longitude
    }

    response = requests.get(url, params=params)

    return response.json()


@weather_blp.route(
    "forecast/<latitude>/<longitude>",
    methods=["GET"],
    tags=["weather"]
)
@login_required
def forecast(latitude, longitude):
    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "appid": current_app.config["OPENWEATHER_API_KEY"],
        "units": "metric",
        "lat": latitude,
        "lon": longitude
    }

    response = requests.get(url, params=params)

    return response.json()
