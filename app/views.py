from flask import render_template, flash, redirect,request,url_for,session
from form import LoginForm, RegForm,AddNewContactForm
from models import User
from flask.ext.mail import Message, Mail
 
mail = Mail()
  
from app import contactsapp
 #Decorators used to link functions to urls 
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

@contactsapp.route('/login/', methods=['GET', 'POST'])
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
@contactsapp.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('login'))

@contactsapp.route('/addnew/', methods=['GET', 'POST'])
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

@contactsapp.route('/register/',methods=['GET', 'POST'])	
def register():
	form = RegForm()
	
	return render_template('register.html', 
                           title='register',
                           form=form,
                           )



