from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,Length
from ..models import User
