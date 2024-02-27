import pytest


class TestUserOperations():
    user_json = {
        "email": "test@test.com",
        "password": "fKg3CO3D8VlQ"
    }

    @pytest.mark.parametrize("user_json", user_json)
    def test_register_user_200(app, client, user_json):
        response = client.post("user/register", json=user_json)

        assert response.status_code == 200
        assert response.get_json()["email"]

    def test_register_user_missing_input_400(app, client):
        response = client.post("user/register", json={})

        assert response.status_code == 400
        assert response.get_json()["message"] == "Missing input data"

    @pytest.mark.parametrize(
        "user_json, missing_field",
        [
            (user_json.copy(), "email"),
            (user_json.copy(), "password"),
        ],
    )
    def test_register_user_missing_email_400(
        app,
        client,
        db,
        user,
        user_json,
        missing_field
    ):
        print(missing_field)
        print(user_json)

        del user_json[missing_field]

        response = client.post("user/register", json=user_json)

        assert response.status_code == 422
        assert response.get_json()["message"] == {
            missing_field: [
                "Missing data for required field."
            ]
        }
