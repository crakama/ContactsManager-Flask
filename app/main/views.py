from flask import render_template, flash, redirect,request,url_for,session
from . import main
from .. import db
from forms import LoginForm, RegForm,AddNewContactForm
from functools import wraps
from ..models import User

  
#from .. import contactsapp

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap

 #Decorators used to link functions to urls 
@main.route('/')
@main.route('/home')
@login_required
def home():
  return render_template('home.html')
  
@main.route('/about')
def about():
  return render_template('about.html')


@main.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name

@main.route('/login/', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		if request.form['username'] != 'username' or request.form['password'] != 'password':
			flash("Your Credentials are Incorrect! Please try again")
		else:
			session['logged_in'] = True
			return redirect(url_for('home'))
			
			

	return render_template('login.html', 
                           title='Sign In',form=form)

#pops out the session object and replaces it with None upon calling of logout route. Session key gets deleted	
@main.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('login'))

@main.route('/addnew/', methods=['GET', 'POST'])
def addContact():
	form = AddNewContactForm()
	if form.validate_on_submit():

		return redirect(url_for('home'))

	return render_template('addnew.html', 
                           title='Add New',
                           form=form,
                           )
#def login():
# 	form = LoginForm()
# 	if form.validate_on_submit():
# 		if request.method == 'POST':
# 			if request.form['username'] != 'username' or request.form['password'] != 'password':
# 				flash("Your Credentials are Incorrect! Please try again")
# 			else:
# 				return redirect(url_for('home'))

# 	return render_template('login.html', 
#                            title='Sign In',
#                            form=form,
#                            )

@main.route('/register/',methods=['GET', 'POST'])	
def register():
	form = RegForm()
	
	return render_template('register.html', 
                           title='register',
                           form=form,
                           )



