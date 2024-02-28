from flask_login import current_user, login_required
from flask_smorest import Blueprint
from flask.views import MethodView

from schemas.user import UserResponseSchema

user_blp = Blueprint(
    "user",
    "user",
    url_prefix="/user",
    description="User operations",
)


@user_blp.route("/")
class UserView(MethodView):
    """ Get user """

    @user_blp.response(200, UserResponseSchema)
    @login_required
    def get(self):
        return current_user
