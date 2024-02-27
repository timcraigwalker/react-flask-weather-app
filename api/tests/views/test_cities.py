import mock


@mock.patch("api.views.cities.requests.get")
def test_cities(app, client, db):
    response = client.get("/cities")

    assert response.status_code == 200
