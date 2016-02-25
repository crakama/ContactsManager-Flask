from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask.ext.login import UserMixin
from app import login_manager




class User(UserMixin, db.Model):
	__tablename__ = "usertable"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique= True)
	PhoneNum = db.Column(db.Integer,index=True, unique=True)
	password_hash = db.Column(db.String(64),index=True, unique=True)
	
	Contacts_id = db.Column(db.Integer, db.ForeignKey('usercontacts.id'))

	#name = db.Column(db.String(64))
	#location = db.Column(db.String(64))
	#about_me = db.Column(db.Text())
	#Contact_since = db.Column(db.DateTime(), default=datetime.utcnow)

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

	@login_manager.user_loader
	def get_user(ident):
  		return User.query.get(int(ident))




class Contacts(db.Model):
	__tablename__ = "usercontacts"

	id = db.Column(db.Integer, primary_key =True)
	Name = db.Column(db.String(140), nullable=False)
	MobileNo = db.Column(db.Integer(), nullable=False)
	skypeID = db.Column(db.String(140), nullable=False)
	Organization = db.Column(db.String(140), nullable=False)
	Position = db.Column(db.String(140),nullable=False)
	users_rel = db.relationship('User', backref='relContacts')

	def __init__(self,Name,MobileNo,skypeID,Organization,Position):

		self.Name = Name
		self.MobileNo = MobileNo
		self.skypeID = skypeID
		self.Organization = Organization
		self.Position = Position
    #specifies how you want the object to be represented when it gets printed
	def __repr__(self):
		return '<Name %r>' % (self.Position)