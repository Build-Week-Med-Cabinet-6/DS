# web_app/routes/admin_routes.py

from flask import Blueprint, render_template, redirect, request
from app.utils.make_pickles import make_pickles_isaac
from app.utils.make_pickles import make_pickles_mark

admin_routes = Blueprint("admin_routes", __name__)


@admin_routes.route('/admin')
def admin_landingpad():
    return render_template("admin_pannel.html")


@admin_routes.route("/admin/models/rebuild", methods=["POST"])
def reubild_models():
    response = request.form["model"]
    if response == "isaac":
        #make_pickles_isaac()
        print("rebuilt isaac's model and saved it as a pickle")
    elif response == "mark":
        #make_pickles_mark()
        print("rebuilt isaac's model and saved it as a pickle")
    else:
        print("unknown option: {} used to select a model".format(response))
    return render_template("admin_pannel.html")
