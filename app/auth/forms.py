from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,SubmitField,validators,PasswordField
from wtforms.validators import DataRequired,Email,Length

class LoginForm(Form):
    '''This class creates creates a
    Login form
    '''
    username = StringField('Username',
                           [validators.Required(message='We need your username')])
    password = PasswordField('Password', [validators.Required()])
    remember = BooleanField('Keep me logged in.')
    submit = SubmitField('Log In')

class RegistrationForm(LoginForm):
    '''This class 
    creates a user registration form.
    '''
    PhoneNum = StringField('PhoneNumber', validators=[DataRequired(), Length(1, 64)])
    username = StringField('username', validators=[DataRequired(), Length(1, 64)])
    email = StringField(
        'Email Address',
        [
            validators.Required(),
            validators.Length(
                min=6, max=64, message='Your email is invalid')
        ]
    )
    password = PasswordField('Password', [validators.Required(),
                                          validators.EqualTo(
        'password_confirmation',
        'Passwords do not match.'
    )])
    password_confirmation = PasswordField('Password Confirmation',
                                          [validators.Required()])
    first_name = StringField('First Name', [validators.Required()])
    last_name = StringField('Last Name', [validators.Required()])
    submit = SubmitField('Save Contact')

