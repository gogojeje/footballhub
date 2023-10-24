from flask import Blueprint

index = Blueprint("index", __name__)
schedule = Blueprint("schedule", __name__)
signup = Blueprint("signup", __name__)
login = Blueprint("login", __name__)
logout = Blueprint("logout", __name__)
teams = Blueprint("teams", __name__)
schedule_and_teams = Blueprint("schedule_and_teams", __name__)

from . import index_route, schedule_route, signup_route, login_route, logout_route, teams_route, schedule_and_teams_route
