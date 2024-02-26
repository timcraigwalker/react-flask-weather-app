"""
User Favourite City Model
"""
from extensions import db
from utils import create_uuid


class UserFavouriteCity(db.Model):

    __tablename__ = "user_favourite_cities"
    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "city",
            "latitude",
            "longitide",
            name="_user_favourite_city_uc"
        ),
    )

    id = db.Column(
        db.String(32), primary_key=True, unique=True, default=create_uuid
    )
    user_id = db.Column(
        db.String(32), db.ForeignKey("users.id"), nullable=False
    )
    city = db.Column(db.String(150), nullable=False)
    latitude = db.Column(db.Float(precision=10, asdecimal=False))
    longitide = db.Column(db.Float(precision=10, asdecimal=False))

    user = db.relationship(
        "User", back_populates="favourite_cities"
    )
