# web_app/routes/web_routes.py

from flask import Blueprint, render_template, redirect, request, jsonify

from app.models import db, parse_records, Strains
from random import sample

web_routes = Blueprint("web_routes", __name__)


@web_routes.route('/products/fetch')
def get_cards():
    db_strains = Strains.query.all()
    response = parse_records(db_strains)
    return jsonify(response)


@web_routes.route("/products/query/<name>", methods=['POST'])
def ask_cards(name):
    # get the name and serch for it in the db
    return f"{name} was passed as a post command to db"


@web_routes.route("/products/query/", methods=['POST'])
def get_search():

    args = request.args
    print(args)
    db_strains = Strains.query.all()
    # ml.ml(args)

    return
