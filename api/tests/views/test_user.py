import pytest

from utils import create_uuid
from tests.factories import UserFactory


class TestUserView():
    def test_user_get_200(app, client, db, user):
        response = client.get("api/user")

        assert response.status_code == 200


class TestRegistrationView():
    user_json = {
        "email": "test_new_user@email.com",
        "password": "fKg3CO3D8VlQ"
    }

    @pytest.mark.parametrize("user_json", [user_json])
    def test_register_user_200(app, client, db, user, user_json):
        response = client.post("api/auth/register", json=user_json)

        assert response.status_code == 200

    def test_register_user_missing_input_400(app, client, db, user):
        response = client.post("api/auth/register", json={})

        assert response.status_code == 400
        assert response.get_json()["message"] == "Missing input data"

    @pytest.mark.parametrize(
        "user_json, missing_field",
        [
            (user_json.copy(), "email"),
            (user_json.copy(), "password"),
        ],
    )
    def test_register_user_missing_required_field_422(
        app,
        client,
        db,
        user,
        user_json,
        missing_field
    ):
        del user_json[missing_field]

        response = client.post("api/auth/register", json=user_json)

        assert response.status_code == 422
        assert response.get_json()["message"] == {
            missing_field: [
                "Missing data for required field."
            ]
        }

    @pytest.mark.parametrize("user_json", [user_json])
    def test_register_user_user_already_exists_409(
        app,
        client,
        db,
        user,
        user_json
    ):
        UserFactory.create(
            id=create_uuid(),
            email=user_json["email"],
            password=user_json["password"]
        )

        response = client.post("api/auth/register", json=user_json)

        assert response.status_code == 409


class TestLoginView():
    user_json = {
        "email": "test_user@email.com",
        "password": "c5y44lwJRMZJ"
    }

    @pytest.mark.parametrize("user_json", [user_json])
    def test_login_user_200(app, client, db, user, user_json):
        response = client.post("api/auth/login", json=user_json)

        assert response.status_code == 200

    def test_login_user_missing_input_400(app, client, db, user):
        response = client.post("api/auth/login", json={})

        assert response.status_code == 400
        assert response.get_json()["message"] == "Missing input data"

    @pytest.mark.parametrize(
        "user_json, missing_field",
        [
            (user_json.copy(), "email"),
            (user_json.copy(), "password"),
        ],
    )
    def test_login_user_missing_required_field_422(
        app,
        client,
        db,
        user,
        user_json,
        missing_field
    ):
        del user_json[missing_field]

        response = client.post("api/auth/login", json=user_json)

        assert response.status_code == 422
        assert response.get_json()["message"] == {
            missing_field: [
                "Missing data for required field."
            ]
        }

    @pytest.mark.parametrize("user_json", [user_json.copy()])
    def test_login_user_user_not_exists_401(
        app,
        client,
        db,
        user,
        user_json
    ):
        user_json["email"] = "test_unknown_user@email.com"

        response = client.post("api/auth/login", json=user_json)

        assert response.status_code == 401
        assert response.get_json()["message"] == "Unauthorized Access"

    @pytest.mark.parametrize("user_json", [user_json])
    def test_login_user_password_incorrect_401(
        app,
        client,
        db,
        user,
        user_json
    ):
        user_json["password"] = "incorrect_password"

        response = client.post("api/auth/login", json=user_json)

        assert response.status_code == 401
        assert response.get_json()["message"] == "Unauthorized"


class TestLogoutView():
    def test_logout_user_200(app, client, db, user):
        response = client.post("api/auth/logout")

        assert response.status_code == 200
