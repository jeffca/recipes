from flask import Flask
from flask_mail import Mail
# from flask.ext.sqlalchemy import SQLAlchemy
# import flask.ext.restless
import base64
# from stretching.database import db_session

app = Flask(__name__)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'washingtoncapstaff@gmail.com',
	MAIL_PASSWORD = 'rjdflibhucjwyafq'
)

mail = Mail(app)

app.secret_key = 'B\xe82zO\x01\x05\x94\x9fm\xdc\x87\xbbliy\x16\x88_\x90\x99\xb5e\x98'


# db = SQLAlchemy(app)

# manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

from recipes.views import aview
from recipes.models import *

# manager.create_api(comps, methods=['GET', 'POST'], results_per_page=None)
	

# @app.teardown_request
# def shutdown_session(exception=None):
#     db_session.remove()