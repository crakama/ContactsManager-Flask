from app import db

class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	#email = db.Column(db.String(120), index=True, unique= True)
	password = db.Column(db.String(64),index=True, unique=True)
	#name = db.Column(db.String(64))
	#location = db.Column(db.String(64))
	#about_me = db.Column(db.Text())
	#Contact_since = db.Column(db.DateTime(), default=datetime.utcnow)
	
	

	def __repr__(self):

		return '<User %r>' % (self.username)

class Contacts(db.Model):
	id = db.Column(db.Integer, primary_key =True)
	Name = db.Column(db.String(140))
	MobileNo = db.Column(db.Integer())
	skypeID = db.Column(db.String(140))
	Organization = db.Column(db.String(140))
	Position = db.Column(db.String(140))

	def __repr__(self):
		return '<Contacts %r>' % (self.Position)