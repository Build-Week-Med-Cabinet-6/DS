# web_app/routes/web_routes.py

from flask import Blueprint, render_template, redirect, request

from app.models import db, Strains

web_routes = Blueprint("web_routes", __name__)


@web_routes.route('/products/fetch')
def get_cards():

    db_strains = Strains.query.all()
    return render_template("dbg.html", strains=db_strains)


@web_routes.route("/products/query/<name>", methods=['POST'])
def ask_cards(name):
    # get the name and serch for it in the db
    return f"{name} was passed as a post command to db"
