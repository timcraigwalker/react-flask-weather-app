import mock


@mock.patch("views.weather.requests.get")
def test_weather(app, client, db, user_favourite_city):
    lat = user_favourite_city.latitude
    long = user_favourite_city.longitude

    response = client.get(f"api/weather/{lat}/{long}")

    assert response.status_code == 200
