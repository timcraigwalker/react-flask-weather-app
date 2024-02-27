"""
Default config
Use env to customise
"""
import os

FLASK_APP = os.getenv("FLASK_APP", "app.py")

FLASK_DEBUG = os.getenv("FLASK_DEBUG", False)

SECRET_KEY = os.getenv("SECRET_KEY", "default_key")

SQLALCHEMY_DATABASE_URI = os.getenv(
    "WEATHER_APP_DB",
    "sqlite:///weatherapp.db"
)

# required for flask smorest api
API_TITLE = "Weather App API"
API_VERSION = "v1"
OPENAPI_VERSION = "3.0.3"
OPENAPI_JSON_PATH = "api-spec.json"
OPENAPI_URL_PREFIX = "/"
OPENAPI_REDOC_PATH = "/redoc"
OPENAPI_REDOC_URL = (
    "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
)
OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# external api keys
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
