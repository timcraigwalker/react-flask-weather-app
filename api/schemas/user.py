from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True


class UserResponseSchema(UserSchema):
    class Meta(UserSchema.Meta):
        exclude = ("password", )
