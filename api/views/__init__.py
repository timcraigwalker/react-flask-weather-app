from api.views.auth import auth_blp
from api.views.cities import cities_blp
from api.views.user import user_blp
from api.views.user_favourite_city import user_favourite_city_blp
from api.views.weather import weather_blp

__all__ = [
    "auth_blp",
    "cities_blp",
    "user_blp",
    "user_favourite_city_blp",
    "weather_blp"
]
