from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,Length
from ..models import User

class AddNewContactForm(Form):
	email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
	PhoneNum = StringField('PhoneNumber', validators=[DataRequired(), Length(1, 64)])
	Location = StringField('Location', validators=[DataRequired(), Length(1, 64)])
	organization = StringField('Organization ', validators=[DataRequired(), Length(1, 64)])
	submit = SubmitField('Save Contact')