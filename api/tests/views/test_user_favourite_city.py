import pytest

from utils import create_uuid
from tests.factories import UserFavouriteCityFactory


class TestUserFavouriteCitiesView():
    user_favourite_city_json = {
        "city": "test_new_city",
        "latitude": 3.14364790012351,
        "longitude": -62.58541567157478
    }

    def test_favourite_cities_get_200(
        app,
        client,
        db,
        user,
        user_favourite_city
    ):
        response = client.get(f"/user/{user.id}/favourite_cities")

        assert response.status_code == 200
        assert response.get_json()[0]["city"] == user_favourite_city.city

    @pytest.mark.parametrize(
        "user_favourite_city_json", [user_favourite_city_json]
    )
    def test_favourite_cities_create_200(
        app,
        client,
        db,
        user,
        user_favourite_city,
        user_favourite_city_json
    ):
        response = client.post(
            f"/user/{user.id}/favourite_cities",
            json=user_favourite_city_json
        )

        assert response.status_code == 200
        assert response.get_json()["city"] == user_favourite_city_json["city"]

    def test_favourite_cities_create_missing_input_400(
        app,
        client,
        db,
        user,
        user_favourite_city
    ):
        response = client.post(
            f"/user/{user.id}/favourite_cities",
            json={}
        )

        assert response.status_code == 400

    @pytest.mark.parametrize(
        "user_favourite_city_json, missing_field",
        [
            (user_favourite_city_json.copy(), "city"),
            (user_favourite_city_json.copy(), "latitude"),
            (user_favourite_city_json.copy(), "longitude"),
        ],
    )
    def test_favourite_cities_create_required_field_422(
        app,
        client,
        db,
        user,
        user_favourite_city_json,
        missing_field
    ):
        del user_favourite_city_json[missing_field]

        response = client.post(
            f"/user/{user.id}/favourite_cities",
            json=user_favourite_city_json
        )

        assert response.status_code == 422
        assert response.get_json()["message"] == {
            missing_field: [
                "Missing data for required field."
            ]
        }

    @pytest.mark.parametrize(
        "user_favourite_city_json", [user_favourite_city_json]
    )
    def test_favourite_cities_create_already_exists_409(
        app,
        client,
        db,
        user,
        user_favourite_city,
        user_favourite_city_json
    ):
        UserFavouriteCityFactory.create(
            id=create_uuid(),
            city=user_favourite_city_json["city"],
            latitude=user_favourite_city_json["latitude"],
            longitude=user_favourite_city_json["longitude"]
        )

        response = client.post(
            f"/user/{user.id}/favourite_cities",
            json=user_favourite_city_json
        )

        assert response.status_code == 409

    @pytest.mark.parametrize(
        "user_favourite_city_json", [user_favourite_city_json]
    )
    def test_favourite_cities_delete_200(
        app,
        client,
        db,
        user,
        user_favourite_city,
        user_favourite_city_json
    ):
        UserFavouriteCityFactory.create(
            id=create_uuid(),
            city=user_favourite_city_json["city"],
            latitude=user_favourite_city_json["latitude"],
            longitude=user_favourite_city_json["longitude"]
        )

        response = client.delete(
            f"/user/{user.id}/favourite_cities",
            json=user_favourite_city_json
        )

        assert response.status_code == 200

    @pytest.mark.parametrize(
        "user_favourite_city_json", [user_favourite_city_json]
    )
    def test_favourite_cities_delete_already_deleted_204(
        app,
        client,
        db,
        user,
        user_favourite_city,
        user_favourite_city_json
    ):
        response = client.delete(
            f"/user/{user.id}/favourite_cities",
            json=user_favourite_city_json
        )

        assert response.status_code == 204

    def test_favourite_cities_delete_missing_input_400(
        app,
        client,
        db,
        user,
        user_favourite_city
    ):
        response = client.delete(
            f"/user/{user.id}/favourite_cities",
            json={}
        )

        assert response.status_code == 400

    @pytest.mark.parametrize(
        "user_favourite_city_json, missing_field",
        [
            (user_favourite_city_json.copy(), "city"),
            (user_favourite_city_json.copy(), "latitude"),
            (user_favourite_city_json.copy(), "longitude"),
        ],
    )
    def test_favourite_cities_delete_required_field_422(
        app,
        client,
        db,
        user,
        user_favourite_city_json,
        missing_field
    ):
        del user_favourite_city_json[missing_field]

        response = client.delete(
            f"/user/{user.id}/favourite_cities",
            json=user_favourite_city_json
        )

        assert response.status_code == 422
        assert response.get_json()["message"] == {
            missing_field: [
                "Missing data for required field."
            ]
        }

    def test_favourite_city_get_200(
        app,
        client,
        db,
        user,
        user_favourite_city
    ):
        response = client.get(
            f"/user/{user.id}/favourite_cities/{user_favourite_city.id}"
        )

        assert response.status_code == 200
        assert response.get_json()["city"] == user_favourite_city.city

    def test_favourite_city_delete_200(
        app,
        client,
        db,
        user,
        user_favourite_city
    ):
        response = client.delete(
            f"/user/{user.id}/favourite_cities/{user_favourite_city.id}"
        )

        assert response.status_code == 200
