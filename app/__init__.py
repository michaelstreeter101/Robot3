# Name: app.py
# Original author: MWS
# Creation date: 2022-08-26
# Purpose: flask app for Robot3 web page
from flask import Flask

app = Flask(__name__)

from app import routes
