
# ContactsManager-Flask
#Project Background:

A Business contacts Manager is a python app that uses flask framework. It's expected to supports creation, retrieval, and search of phonebook entries consisting of a name, phone number and other details. Stores the entries in SQLite database and allows sending of a text message to specific mobile number

Project Requirements:

Add new contactsView Contacts and Save them to database(using SQLAlchemy and SQLite) Search Contacts Enable social authentication using Google, Facebook and/or Twitter

Use SMS API to Send SMS to contacts
=======
Business contacts Manager



#Features

#1. Create an account

You create an account by registering with the system using your username and password. Then log in using the credetials you have registered with. 

#2. Add new contact

Once you have registerd and logged in, the system will redirect you to home page. Navigate to the side bar on your left side and click add new contact. For the system to work properly make sure you add new contact with VALID email address and phone number that includes you country code e.g +254 fo Kenya

#3. Edit existing contacts

Once you have added a new contact, go back to the navigation bar on your left side and click view all contacts. You will be able to see the contact you just added in the list of contacts

You will also be able to edit contact details. To do so, click on the edit button.

#4. Send SMS and email.

While still on the viee all contacts page, you can send short message to a specific contact that has a valid mobile number with country code. The system uses AfricaisTalking SMS API to send the messages, so it should be working perfectly. I'm yet to test for users outside Africa.


#Features yet to be implemented:

1. Social auth(facebook, twitter or google+)

2. Edit button to pop up a modal for editing the contacts insted of redirecting edit form to a new page.

3. Implement search functionality to search for a specific contact in the database.

4. Appointments function. To help keep track and scedule appointments


#Technologies used

SQLite3
SQLAlchemy
Python anf flask framework
Ajax(jquery).
Bootstrap


#Set up Locally

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

Once you have all these set up, follow the following steps.

#To run Locally:

1. At the terminal, navigate to your ContactsManager-Flask project directory and activate your virtual environment

2. While inside the folder issue the following commands: python manage.py runserver

3. Go to your browser and type: localhost:5000/, register and submit the form

4. login with the credentials you used during your registration

5. Use the system!


#On Heroku:
1. Visit this link: https://businesscontactsmanager.herokuapp.com/ 
2. Register
3. use the credentials that you registered with to login.


