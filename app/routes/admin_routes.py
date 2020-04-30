# web_app/routes/admin_routes.py

from flask import Blueprint, render_template, redirect, request, flash
from app.utils.make_pickles import make_pickles_isaac
from app.utils.make_pickles import make_pickles_mark
from os import getenv

admin_routes = Blueprint("admin_routes", __name__)


@admin_routes.route('/admin')
def admin_landingpad():
    return render_template("admin_pannel.html")


@admin_routes.route("/admin/models/rebuild", methods=["POST"])
def reubild_models():
    flash("Rebuilding model (1/2)... this might take a while")
    make_pickles_isaac().save_pickles()
    flash("Rebuilding Model (2/2) .. this might take a while")
    make_pickles_mark().save_pickles()
    return redirect('/')


@admin_routes.route("/admin/db/rebuild", methods=["POST"])
def rebuild_db():
    flash(
        "Rebuilding the database from scratch\njust kidding this isn't implemented"
    )
    return "database rebuilt"
