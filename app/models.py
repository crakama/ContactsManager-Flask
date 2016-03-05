import urllib, hashlib
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey,Column, Integer, DateTime, String
from sqlalchemy.orm import relationship
from flask.ext.login import UserMixin
from app import login_manager
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore


Base = declarative_base()


class User(UserMixin, db.Model):
	__tablename__ = "usertable"
	id = db.Column(db.Integer, primary_key=True)
	social_id = db.Column(db.String(64), nullable=False, unique=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique= True)
	PhoneNum = db.Column(db.Integer,index=True, unique=True)
	password_hash = db.Column(db.String(64),index=True, unique=True)
	
	Contacts_id = db.Column(db.Integer, db.ForeignKey('usercontacts.id'))



	@property
	def password(self):
		'''prevents access to password property'''
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):
		'''Sets password to a hashed password
		'''
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
	

	def __repr__(self):

		return '<User %r>' % (self.username)

		#Loads the user by his id
	@login_manager.user_loader
	def load_user(id):
  		return User.query.get(int(id))


class Contacts(db.Model):
	__tablename__ = "usercontacts"

	id = db.Column(db.Integer, primary_key =True)
	firstname = db.Column(db.String(140), nullable=True)
	lastname = db.Column(db.String(140), nullable=True)
	email = db.Column(db.String(140), nullable=True)
	mobilenumber = db.Column(db.String(140), nullable=True)
	country = db.Column(db.String(140), nullable=True)
	skypeID = db.Column(db.String(140), nullable=True)
	organization = db.Column(db.String(140), nullable=True)
	position = db.Column(db.String(140),nullable=True)
	users_rel = db.relationship('User', backref='relContacts')

	def __init__(self,firstname,lastname,email,mobilenumber,country,organization,skypeID,position):
		self.firstname  = firstname 
		self.lastname  = lastname
		self.email  = email
		self.mobilenumber  = mobilenumber
		self.country  = country
		self.organization  = organization
		self.skypeID = skypeID
		self.position = position
  	def avatar(self, size):
  		# gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
  		# gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
  		
  		return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)
    #specifies how you want the object to be represented when it gets printed
	def __repr__(self):
		return '<firstname %r>' % (self.firstname)
