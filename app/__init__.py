#Import Flask class from the flask module
from flask import Flask

from flask_bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from config import config



bootstrap = Bootstrap()
mail = Mail()

#Create the database Object
db = SQLAlchemy()


#from app import models



def create_app(config_name):

   #Flask application configuration Object#
	contactsapp = Flask(__name__)

    #Configures DB URLs as key called SQLALCHEMY_DATABASE_URL
	contactsapp.config.from_object(config[config_name])
	config[config_name].init_app(contactsapp)

	bootstrap.init_app(contactsapp)

	mail.init_app(contactsapp)
    
    #Flask sesion, different from db.session
	contactsapp.secrete_key = "development_key"
	

	db.init_app(contactsapp)


	
	from main import main as main_blueprint
	contactsapp.register_blueprint(main_blueprint)
		
	return contactsapp


	#What this file does for the SQLAlchemy DB framework
	#
	#Does imports of needed modules
	#Creates flask configuration objects
	#Instanciates an object of type SQLAchemy
	#Configures DB URLs as key called SQLALCHEMY_DATABASE_URL in the flask configuration object, 
	#whose value is directory path to where the database is located
 

