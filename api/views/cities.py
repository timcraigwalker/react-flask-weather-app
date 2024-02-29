from flask import current_app
from flask_login import login_required
from flask_smorest import Blueprint
import requests

cities_blp = Blueprint(
    "cities",
    "cities",
    url_prefix="/cities",
    description="External cities api",
)


@cities_blp.route(
    "",
    methods=["GET"],
    defaults={"name_prefix": ""},
    tags=["cities"]
)
@cities_blp.route("/<name_prefix>", methods=["GET"], tags=["cities"])
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
