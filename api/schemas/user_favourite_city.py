from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import UserFavouriteCity


class UserFavouriteCitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserFavouriteCity
        include_relationships = True
        load_instance = True
