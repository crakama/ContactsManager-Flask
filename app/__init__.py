#Import Flask class from the flask module
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config
from oauth import OAuthSignIn



bootstrap = Bootstrap()
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

#Create the database Object
db = SQLAlchemy()


from app import models



def create_app(config_name):

   #Flask application configuration Object#
	contactsapp = Flask(__name__)

	# contactsapp.configauth['SECURITY_POST_LOGIN'] = '/profile'

    #Configures DB URLs as key called SQLALCHEMY_DATABASE_URL
	contactsapp.config.from_object(config[config_name])
	config[config_name].init_app(contactsapp)

	bootstrap.init_app(contactsapp)

	contactsapp.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '184223628621658',
        'secret': 'f6a6041edc65d615a975fe4c6f053154'
        },
    'twitter': {
        'id': 'qtrDRR8LELDpHCwg7AedlfVcj',
        'secret': 'F2xTVvoDWSmveSC4I9Ap4rvKpOov3OLb9iIjc8baQYyFHrxTMM'
        }
        }

	

	mail.init_app(contactsapp)

	login_manager.init_app(contactsapp)
    #Flask sesion, different from db.session
	contactsapp.secrete_key = "development_key"
	

	db.init_app(contactsapp)



	
	from main import main as main_blueprint
	contactsapp.register_blueprint(main_blueprint)

	from .auth import auth as auth_blueprint
	contactsapp.register_blueprint(auth_blueprint, url_prefix='/auth')

	from .crudcontacts import crudcontacts as crudcontacts_blueprint
	contactsapp.register_blueprint(crudcontacts_blueprint, url_prefix='/crudcontacts')
		
	return contactsapp


	'''What this file does for the SQLAlchemy DB framework
	
	Does imports of needed modules
	Creates flask configuration objects
	Instanciates an object of type SQLAchemy
	Configures DB URLs as key called SQLALCHEMY_DATABASE_URL in the flask configuration object, 
	whose value is directory path to where the database is located'''
 

