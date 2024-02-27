import factory

from extensions import db
from models import User, UserFavouriteCity
from utils import create_uuid


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    """ User Factory """

    class Meta:
        model = User
        sqlalchemy_session = db.session

    id = create_uuid()
    email = "test@email.com"
    password = "123456789"


class UserFavouriteCityFactory(factory.alchemy.SQLAlchemyModelFactory):
    """ User Favourite City Factory """

    class Meta:
        model = UserFavouriteCity
        sqlalchemy_session = db.session

    id = create_uuid()
    city = "Test City"
    latitide = 52.4955625251478
    longitude = -1.8897333678507744

    user_id = factory.LazyAttribute(lambda a: UserFactory.id)
