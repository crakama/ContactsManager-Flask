
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

contactsapp = Flask(__name__)
contactsapp.config.from_object('config')
db = SQLAlchemy(contactsapp)
bootstrap = Bootstrap(contactsapp)


from app import views, models
