from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,SubmitField,validators,PasswordField
from wtforms.validators import DataRequired,Email,Length

class AddNewContactForm(Form):

	firstname = StringField('First Name', validators=[DataRequired(), Length(1, 64)])
	lastname = StringField('Last Name', validators=[DataRequired(), Length(1, 64)])
	email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
	skypeID = country = StringField('SkypeID', validators=[DataRequired(), Length(1, 64)])
	mobilenumber = StringField('Phone Number', validators=[DataRequired(), Length(1, 64)])
	country = StringField('Country', validators=[DataRequired(), Length(1, 64)])
	position = StringField('Position', validators=[DataRequired(), Length(1, 64)])
	organization = StringField('Organization ', validators=[DataRequired(), Length(1, 64)])
	submit = SubmitField('Save Contact')

class viewAllContacts(Form):
	pass



class EditContactForm(Form):
	firstname = StringField('First Name', validators=[DataRequired(), Length(1, 64)])
	lastname = StringField('Last Name', validators=[DataRequired(), Length(1, 64)])
	email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
	skypeID = country = StringField('SkypeID', validators=[DataRequired(), Length(1, 64)])
	mobilenumber = StringField('Phone Number', validators=[DataRequired(), Length(1, 64)])
	country = StringField('Country', validators=[DataRequired(), Length(1, 64)])
	position = StringField('Position', validators=[DataRequired(), Length(1, 64)])
	organization = StringField('Organization ', validators=[DataRequired(), Length(1, 64)])
	submit = SubmitField('Submit')

class SendSMSForm(Form):
	mobilenumber = StringField('Phone Number', validators=[DataRequired(), Length(1, 64)])
	message = StringField('message ', validators=[DataRequired(), Length(1, 64)])