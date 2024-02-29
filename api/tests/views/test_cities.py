import mock


@mock.patch("views.cities.requests.get")
def test_cities(app, client, db):
    response = client.get("api/cities")

    assert response.status_code == 200
