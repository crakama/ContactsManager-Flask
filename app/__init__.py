#Import th Flask class from the flask module
from flask import Flask
import os
from flask_bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
basedir = os.path.abspath(os.path.dirname(__file__))


bootstrap = Bootstrap()
mail = Mail()
#moment = Moment()

#Create the database Object
db = SQLAlchemy()

#from .main import views
#from ipdb import ipdb; ipdb.set_trace()
from app import models



def create_app(config_name):
#Create the application Object
	contactsapp = Flask(__name__)

#Initializing configuration settings from config module
	contactsapp.config.from_object(config[config_name])

	config[config_name].init_app(contactsapp)

	bootstrap.init_app(contactsapp)

	mail.init_app(contactsapp)

	contactsapp.secrete_key = "development_key"
	#contactsapp.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

	db.init_app(contactsapp)


	
	from main import main as main_blueprint
	contactsapp.register_blueprint(main_blueprint)
		#attach routes and custom error pages here
	return contactsapp



#
# contactsapp.config["MAIL_SERVER"] = "smtp.gmail.com"
# contactsapp.config["MAIL_PORT"] = 465
# contactsapp.config["MAIL_USE_SSL"] = True
# contactsapp.config["MAIL_USERNAME"] = 'contact@example.com'
# contactsapp.config["MAIL_PASSWORD"] = 'your-password'
 

