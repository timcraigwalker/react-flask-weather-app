import mock


@mock.patch("views.weather.requests.get")
def test_weather_current(app, client, db, user_favourite_city):
    lat = user_favourite_city.latitude
    long = user_favourite_city.longitude

    response = client.get(f"api/weather/current/{lat}/{long}")

    assert response.status_code == 200


@mock.patch("views.weather.requests.get")
def test_weather_forecast(app, client, db, user_favourite_city):
    lat = user_favourite_city.latitude
    long = user_favourite_city.longitude

    response = client.get(f"api/weather/forecast/{lat}/{long}")

    assert response.status_code == 200