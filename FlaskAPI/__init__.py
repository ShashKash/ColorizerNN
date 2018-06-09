import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__author__ = 'shashkash'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
db = SQLAlchemy(app)

original_target = os.path.join(APP_ROOT, 'images/')
if not os.path.isdir(original_target):
    os.mkdir(original_target)
print(original_target)

colored_target = os.path.join(APP_ROOT,'colored_images/')
if not os.path.isdir(colored_target):
    os.mkdir(colored_target)
print(colored_target)

from FlaskAPI import routes
