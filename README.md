
# ContactsManager-Flask

Project Background:

A Business contacts Manager is a python app that uses flask framework. It's expected to supports creation, retrieval, and search of phonebook entries consisting of a name, phone number and other details. Stores the entries in SQLite database and allows sending of a text message to specific mobile number

Project Requirements:

Add new contactsView Contacts and Save them to database(using SQLAlchemy and SQLite) Search Contacts Enable social authentication using Google, Facebook and/or Twitter

Use SMS API to Send SMS to contacts


Pre-Installation Requirements

1.Install a virtual environment.
2.Prepare it by installing the following Flask extensions
	pip install flask
	pip install flask-login
	pip install flask-openid
	pip install flask-mail
	pip install flask-sqlalchemy
	pip install sqlalchemy-migrate
	pip install flask-whooshalchemy
	pip install flask-wtf
	pip install flask-babel
	pip install guess_language
	pip install flipflop
	pip install coverage


How to use:

1. At the terminal, navigate to your ContactsManager-Flask project directory and activate your virtual environment
2. While inside the folder issue the following commands: python manage.py runserver
3. Go to your browser and type: localhost:5000/auth/register, register and submit the form
4. login with the credentials you used during your registration
5. Use the system!

