# web_app/routes/home_routes.py

from flask import Blueprint, render_template, redirect

home_routes = Blueprint("home_routes", __name__)


@home_routes.route('/')
def root():
    return render_template("index.html")
