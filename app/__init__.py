
from flask import Flask
contactsapp = Flask(__name__)
contactsapp.config.from_object('config')

from app import routes
