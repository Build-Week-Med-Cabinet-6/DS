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
    if request.form.get("model") == "isaac":
        print("isaac's model is selected")
    else:
        print("mark's models is selected")
    return redirect("/")
