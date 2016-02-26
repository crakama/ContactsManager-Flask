from flask import Blueprint
crudcontacts = Blueprint('crudcontacts', __name__)

from . import views