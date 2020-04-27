# web_app/routes/web_routes.py

from flask import Blueprint, render_template, redirect

web_routes = Blueprint("web_routes", __name__)


@web_routes.route('/products/fetch', methods=["GET"])
def get_cards():
    return "fetch ph"


@web_routes.route("/products/query")
def ask_cards():
    return "query ph"
