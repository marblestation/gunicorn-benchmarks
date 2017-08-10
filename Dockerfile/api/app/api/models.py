from flask.ext.security import UserMixin
from flask_sqlalchemy import SQLAlchemy as FlaskSQLAlchemy
import datetime

db = FlaskSQLAlchemy()

class User(UserMixin, db.Model):
    """
    Define the user model
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    _password = db.Column(db.String(120), name='password')
    name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    login_count = db.Column(db.Integer)
    registered_at = db.Column(db.DateTime())
    ratelimit_level = db.Column(db.Integer)

class Foo(db.Model):
    """
    Define the foo model
    """
    __tablename__ = 'foo'

    id = db.Column(db.Integer, primary_key=True)
    registered_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    last_sent = db.Column(db.String(120))
    client = db.Column(db.String(120))
    sent_from = db.Column(db.String(500))
    service = db.Column(db.String(120))
    sleep = db.Column(db.Integer())
