from stretching import app, mail
from flask import Flask, render_template, request, redirect, url_for, flash, Response
from stretching.models import *
from stretching.database import db_session
import datetime 
from datetime import timedelta
from flask_mail import Message
from sqlalchemy import desc
from functools import wraps
import json


def check_auth(username, password):
	"""This function is called to check if a username /
	password combination is valid.
	"""
	return username == 'abh' and password == 'abh4050'

def authenticate():
	"""Sends a 401 response that enables basic auth"""
	return Response(
	'Could not verify your access level for that URL.\n'
	'You have to login with proper credentials', 401,
	{'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			return authenticate()
		return f(*args, **kwargs)
	return decorated

@app.route('/')
def home():
	return render_template('index.html')

@app.route("/selectCategory", methods=["POST"])
def selectCategory():
	c = request.form["category"]
	if fname == "" or lname == "" or phone == "":
		flash("Please complete all required fields.")
		return redirect(url_for("contact"))
	a = Application()
	a.FirstName = fname
	a.LastName = lname
	a.Email = email
	a.Phone = phone
	a.DateTime = datetime.datetime.now()
	a.PacketSent = False
	db_session.add(a)
	db_session.commit()

	msg = Message(a.FirstName + " " + a.LastName + " has completed the CAP Referral Form" ,
		sender="jeff12ca@gmail.com",
		recipients=["bcap@qwestoffice.net"])	
	msg.html = "<p>Bob, " + str(fname) + " " + str(lname) + " has filled out the online referral form. " + str(phone) + " is his or her phone number.</p><p>His or her email is " + str(email) + ". All web referrals are available at http://washingtoncap.org/admin/applications </p><p> Thanks! --Jeff</p>"
	mail.send(msg)
	flash("Thank you for contacting CAP. A member of our staff will contact you shortly.")
	return render_template("contact.html")


@app.route('/admin')
@requires_auth
def admin():
	return render_template('admin.html')

@app.route('/admin/applications')
@requires_auth
def applications():
	apps = Application.query.order_by(desc(Application.DateTime)).all()
	return render_template('admin/applications.html', apps=apps)

@app.route("/admin/deleteApplicant?appid=<appid>", methods=["GET", "POST"])
@requires_auth
def deleteApplicant(appid):
	a = Application.query.get(int(appid))
	db_session.delete(a)
	db_session.commit()
	return redirect(url_for("applications"))

