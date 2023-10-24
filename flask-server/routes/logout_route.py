from . import logout
from flask import redirect, url_for, session

@logout.route("/api/logout")
def logout():
    session.pop("userid", None)
    return redirect(url_for("index"))