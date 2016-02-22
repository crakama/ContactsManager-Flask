from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class RegForm(Form):
	email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
	PhoneNum = StringField('PhoneNumber', validators=[DataRequired(), Length(1, 64)])
	
	submit = SubmitField('Save Contact')

class AddNewContactForm(Form):
	email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
	PhoneNum = StringField('PhoneNumber', validators=[DataRequired(), Length(1, 64)])
	Location = StringField('Location', validators=[DataRequired(), Length(1, 64)])
	organization = StringField('Organization ', validators=[DataRequired(), Length(1, 64)])
	submit = SubmitField('Save Contact')