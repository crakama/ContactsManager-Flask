#Import th Flask class from the flask module
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

#Create the application Object
contactsapp = Flask(__name__)

#Initializing configuration settings
contactsapp.config.from_object('config')

#Create the database Object
db = SQLAlchemy(contactsapp)

#Create the Bootstrap Object
bootstrap = Bootstrap(contactsapp)


from app import views, models
