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


contactsapp.secret_key = 'development key'
 
contactsapp.config["MAIL_SERVER"] = "smtp.gmail.com"
contactsapp.config["MAIL_PORT"] = 465
contactsapp.config["MAIL_USE_SSL"] = True
contactsapp.config["MAIL_USERNAME"] = 'contact@example.com'
contactsapp.config["MAIL_PASSWORD"] = 'your-password'
 
from app import views, models
from app.views import mail
mail.init_app(contactsapp)