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


@web_routes.route("/products/query", methods=['POST'])
def get_search():

    flavors = request.form['flavors']
    effects = request.form['effects']
    user_text = request.form['text']
    if user_text == 'None':
        # pred = ml_model_1(effects+flavors)
        #return Strains.query.filter(Strains.index in pred).all()
        pass
    elif user_text != 'None':
        # pred = ml_model_2(user_text)
        # return Strains.query.filter(Strains.index in pred).all()
        pass
    data = Strains.query.first()
    data = data.__dict__
    del data['_sa_instance_state']

    return render_template("dbg.html",
                           flavors=flavors,
                           effects=effects,
                           text=user_text,
                           data=data)
