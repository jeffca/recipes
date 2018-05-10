from jeffcaphotography import app, mail
from flask import Flask, render_template, request, redirect, url_for, flash, Response
# from stretching.models import *
# from stretching.database import db_session
# import datetime 
# from datetime import timedelta
# from flask_mail import Message
# from sqlalchemy import desc
# from functools import wraps
import json

@app.route('/')
def home():
	return render_template('index.html')


