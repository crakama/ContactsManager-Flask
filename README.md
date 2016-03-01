
# ContactsManager-Flask

Project Background:

A Business contacts Manager is a python app that uses flask framework. It's expected to supports creation, retrieval, and search of phonebook entries consisting of a name, phone number and other details. Stores the entries in SQLite database and allows sending of a text message to specific mobile number

Project Requirements:

Add new contactsView Contacts and Save them to database(using SQLAlchemy and SQLite) Search Contacts Enable social authentication using Google, Facebook and/or Twitter

Use SMS API(Africa's Talking) to Send SMS to contacts stored in the database


Pre-Installation Requirements

1.Install a virtual environment.
2.Prepare it by installing the following Flask extensions

	(venv)$ pip install flask
	(venv)$ pip install flask-login
	(venv)$ pip install flask-openid
	(venv)$ pip install flask-mail
	(venv)$ pip install flask-sqlalchemy
	(venv)$ pip install sqlalchemy-migrate
	(venv)$ pip install flask-whooshalchemy
	(venv)$ pip install flask-wtf
	(venv)$ pip install flask-babel
	(venv)$ pip install guess_language
	(venv)$ pip install flipflop
	(venv)$ pip install coverage


How to use:

Locally
1. At the terminal, navigate to your ContactsManager-Flask project directory and activate your virtual environment

2. While inside the folder issue the following commands: python manage.py runserver

3. Go to your browser and type: localhost:5000/, register and submit the form

4. login with the credentials you used during your registration

5. Use the system!

On Heroku:
1. Visit this link: https://businesscontactsmanager.herokuapp.com/ 
2. Register
3. use the credentials that you registered with to login "Please use a VALID email address"

