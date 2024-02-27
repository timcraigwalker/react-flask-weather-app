"""
User Model
"""
from flask_login import UserMixin

from api.extensions import db
from api.utils import create_uuid


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(
        db.String(32), primary_key=True, unique=True, default=create_uuid
    )
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    favourite_cities = db.relationship(
        "UserFavouriteCity", back_populates="user", uselist=True
    )
