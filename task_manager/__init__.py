from flask import Flask

from flask_sqlalchemy import SQLALCHEMY

from settings import Config


app = Flask(__name__)

app.config.from_object(Config)

db = SQLALCHEMY(app)

from . import models, views