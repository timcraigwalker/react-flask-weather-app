from flask import Flask

from extensions import api, bcrypt, db, login_manager, migrate
from models import User
from views import api_blp, user_blp, user_favourite_city_blp

app = Flask("react-flask-weather-app")
app.config.from_object("config")

if app.config["FLASK_DEBUG"]:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

api.init_app(app)
bcrypt.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

with app.app_context():
    db.create_all()

api.register_blueprint(api_blp, path="api")
api.register_blueprint(user_blp, path="user")
api.register_blueprint(
    user_favourite_city_blp,
    path="user/<user_id>/favourite_cities"
)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
