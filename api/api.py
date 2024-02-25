from flask import Flask
import requests

app = Flask("react-flask-weather-app")
app.config.from_object("config")


@app.route("/api/cities/", defaults={"name_prefix": ""})
@app.route("/api/cities/<name_prefix>")
def cities(name_prefix):
    print(name_prefix)
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

    params = {"maxPopulation": "1000000", "namePrefix": name_prefix}

    headers = {
        "X-RapidAPI-Key": app.config["RAPID_API_KEY"],
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=params)

    print(response)

    return response.json()


@app.route("/api/locations")
def locations():
    return {"locations": ["Location1", "Location2"]}
