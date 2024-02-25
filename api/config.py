"""
Default config
Use env to customise
"""
import os

SECRET_KEY = os.getenv("SECRET_KEY", "default_key")

SQLALCHEMY_DATABASE_URI = os.getenv(
    "WEATHER_APP_DB",
    "sqlite:///weatherapp.db"
)

RAPID_API_KEY = os.getenv("RAPID_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
