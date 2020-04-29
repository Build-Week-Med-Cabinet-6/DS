# web_app/routes/web_routes.py

from flask import Blueprint, render_template, request, jsonify
from app.models import db, parse_records, Strains
from app.services.model_service import modelone
from os import path
from flask_cors import cross_origin

PICKLE_DIR = path.join(path.dirname(__file__), '..', 'pickles', '')
web_routes = Blueprint("web_routes", __name__)


@web_routes.route('/products/fetch')
@cross_origin()
def get_cards():
    """Function/endpoint returns all of the entries in the database
    """
    db_strains = Strains.query.all()
    response = parse_records(db_strains)
    return jsonify(response)


@web_routes.route("/products/query", methods=['POST'])
@cross_origin()
def get_search():
    """Function/Endpoint takes the parameters send in a post request and passes
    them to a model to return the matching strains based on the arguments that
    were passed by the user.
    Arguments:
    -----------
    None impicit arguments
    flavors {str} : the string of comma seperated flavors that is passed to the POST
    request from an input form
    effects {str} : a string of comma seperated values that passed with the POST
    request from an input form
    Returns:
    ----------
    data {jsonb} : the entries in the databse that match the resulting predicted strains
    """
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
@cross_origin()
def get_text_search():
        """Function/Endpoint takes the parameters send in a post request and passes
    them to a model to return the matching strains based on the arguments that
    were passed by the user.
    Arguments:
    -----------
    None impicit arguments
    text {str} : a String that the user send from an imput feild that is passed
    to a model that tried to recommend strains based on their description.
    Returns:
    ----------
    data {jsonb} : the entries in the databse that match the resulting predicted strains
    """"
    text = request.form['text']
    #init the model
    m = modelone(PICKLE_DIR + 'isaac_nn.pickle',
                 PICKLE_DIR + 'isaac_tf.pickle')

    # make predictions based on the passed string
    m.transform_predict([text])
    pred = m.getResults()[0]
    print(pred)
    data = Strains.query.filter(Strains.index.in_([int(x)
                                                   for x in pred])).all()
    return jsonify(parse_records(data))
