
import pytest
from pytest_factoryboy import register

from api.app import create_app
from api.extensions import db as _db
from api.tests.factories import UserFactory, UserFavouriteCityFactory


@pytest.fixture(scope="session")
def app():
    app = create_app(testing=True)
    return app


@pytest.fixture
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()

    app.app_context().push()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def client(app):
    testing_client = app.test_client()

    yield testing_client


register(UserFactory, "user")
register(UserFavouriteCityFactory, "user_favourite_city")
