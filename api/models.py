from flask_login import UserMixin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from uuid import uuid4

db = SQLAlchemy()
migrate = Migrate()


def create_uuid():
    return uuid4().hex


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=create_uuid)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.Text, nullable=False)

    favourite_cities = db.relationship(
        "FavouriteCity", back_populates="user", uselist=True
    )


class UserFavouriteCity(db.Model):
    __tablename__ = "user_favourite_cities"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=create_uuid)
    user_id = db.Column(
        db.String(32), db.ForeignKey("users.id"), nullable=False
    )
    city = db.Column(db.String(150), nullable=False)
    latitude = db.Column(db.Float(precision=10, asdecimal=False))
    longitide = db.Column(db.Float(precision=10, asdecimal=False))

    user = db.relationship(
        "Users", back_populates="favourite_cities"
    )
