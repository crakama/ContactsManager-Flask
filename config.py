import os
import re

basedir = os.path.abspath(os.path.dirname(__file__))


WTF_CSRF_ENABLED = True

class Config:

	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASKY_MAIL_SUBJECT_PREFIX = '[ContactsManager]'
	FLASKY_MAIL_SENDER = 'ContactsManager Admin <crakama89@gmail.com>'
	FLASKY_ADMIN = os.environ.get('CONTACTSMANAGER_ADMIN')
	
	@staticmethod
	def init_app(contactsapp):

		pass

class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'contactsDB_dev.sqlite')
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'contactsDB_test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'contactsDB.sqlite')

#
config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}

#What this file does for the SQLAlchemy DB framework
#
#Creates URLs that points to the database location
#Defines a dictionary whose keys are arguments to the create_app function in the init file.
#The key is usually speciafied during database creation when th db_create.py file is run
#The create_app function then uses the value of the key to determine which configurations to pick for database creation
#