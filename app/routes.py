from flask import render_template
from form import LoginForm
  
from app import contactsapp
  
@contactsapp.route('/')
def home():
  return render_template('home.html')
  
@contactsapp.route('/about')
def about():
  return render_template('about.html')

@contactsapp.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name

@contactsapp.route('/login', methods=['GET', 'POST'])	
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)

  

