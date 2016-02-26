from flask import render_template, flash, redirect,request,url_for,session
from . import main
from .. import db

from ..models import User





@main.route('/')
def index():
	return render_template('index.html')

@main.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name


