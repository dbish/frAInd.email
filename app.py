from flask import jsonify, Flask, render_template, request, redirect, url_for, session, flash, g, send_from_directory
import os
import json
from flask import current_app
from urllib.request import urlopen
import boto3
from botocore.exceptions import ClientError
from datetime import datetime, date
from dateutil.parser import parse
import sqlite3
from sqlite3 import Error
from math import exp

application = Flask(__name__)
app = application
app.config['DEBUG'] = True
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon') 

@app.route('/logout')
def logout():
    session.pop('screen_name', None)
    query = "oauth/invalidate_token.json"

    resp = twitter.post(query)
    flash('You were signed out')
    del blueprint.token
    return redirect(url_for('home'))

if __name__=='__main__':
    print('running')
    #application.run(host='0.0.0.0', port=80)
    application.run(host='0.0.0.0', port='80')