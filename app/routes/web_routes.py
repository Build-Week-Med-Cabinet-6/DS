# web_app/routes/web_routes.py

from flask import Blueprint, render_template, redirect, request, jsonify
from app.models import db, parse_records, Strains
from app.services.model_service import modelone
from random import sample
from os import path
PICKLE_DIR = path.join(path.dirname(__file__), '..', 'pickles', '')

web_routes = Blueprint("web_routes", __name__)


@web_routes.route('/products/fetch')
def get_cards():
    db_strains = Strains.query.all()
    response = parse_records(db_strains)
    return jsonify(response)


@web_routes.route("/products/query", methods=['POST'])
def get_search():

    flavors = request.form['flavors']
    effects = request.form['effects']

    #init the model
    m = modelone(PICKLE_DIR + 'nn.pickle',
                 PICKLE_DIR + 'dtm_combined_tf.pickle')

    # make predictions based on the passed string
    m.transform_predict([effects + flavors])
    pred = m.getResults()[0]
    print(pred)
    data = Strains.query.filter(Strains.index.in_([int(x)
                                                   for x in pred])).all()
    return jsonify(parse_records(data))


@web_routes.route('/products/search', methods=['POST'])
def get_text_search():
    text = request.form['text']
    #init the model
    m = modelone(PICKLE_DIR + 'isaac_nn.pickle',
                 PICKLE_DIR + 'isaac_tf.pickle')

    # make predictions based on the passed string
    m.transform_predict(text)
    pred = m.getResults()[0]
    print(pred)
    data = Strains.query.filter(Strains.index.in_([int(x)
                                                   for x in pred])).all()
    return jsonify(parse_records(data))



