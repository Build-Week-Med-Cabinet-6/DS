from flask import Flask, Blueprint, render_template, Request, redirect
from os import getenv

from app.models import db, migrate

from app.routes.home_routes import home_routes
from app.routes.web_routes import web_routes


def create_app():

    app = Flask(__name__)

    # get the pg database url from heroku envenviroment
    DATABASE_URL = getenv("DATABASE_URL")

    # configure the database:
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config[
        "SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # suppress warning messages

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(web_routes)

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
