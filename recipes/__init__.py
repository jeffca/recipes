from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
# import flask.ext.restless
import base64
# from stretching.database import db_session

app = Flask(__name__)

app.secret_key = 'B\xe82zO\x01\x05\x94\x9fm\xdc\x87\xbbliy\x16\x88_\x90\x99\xb5e\x98'


import sqlite3
from flask import g

DATABASE = 'recipes.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

from recipes.views import aview
