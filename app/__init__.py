
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

contactsapp = Flask(__name__)
contactsapp.config.from_object('config')
db = SQLAlchemy(contactsapp)


from app import routes, models
