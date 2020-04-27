from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Strains(db.Model):
    index = db.Column(db.BigInteger, primary_key=True)
    strain = db.Column(db.String(128), nullable=False)
    type_ = db.Column(db.String(128))
    rating = db.Column(db.Float, nullable=False)
    effects = db.Column(db.String(128), nullable=False)
    flavor = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
