from flask import render_template, flash, redirect
from form import LoginForm
  
from app import contactsapp
  
@contactsapp.route('/')
@contactsapp.route('/home')
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
	if form.validate_on_submit():
		flash('Login request for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
		return redirect('/home')
	return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=contactsapp.config['OPENID_PROVIDERS'])

  

