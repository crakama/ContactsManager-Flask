#import the db server
from app import db

class User(db.Model):
	__tablename__ = "usertable"
	id = db.Column(db.String, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	#email = db.Column(db.String(120), index=True, unique= True)
	password = db.Column(db.String(64),index=True, unique=True)
	Contacts_id = db.Column(db.Integer, db.ForeignKey('usercontacts.id'))

	#name = db.Column(db.String(64))
	#location = db.Column(db.String(64))
	#about_me = db.Column(db.Text())
	#Contact_since = db.Column(db.DateTime(), default=datetime.utcnow)

	

	def __repr__(self):

		return '<User %r>' % (self.username)

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