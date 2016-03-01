# from .. import AfricasTalkingGateway
# Import the helper gateway class
from ..AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

from flask import session, render_template, redirect, request, url_for, flash
from . import crudcontacts
from .. import db
from ..models import Contacts
from .forms import AddNewContactForm, EditContactForm





@crudcontacts.route('/viewall', methods=['GET', 'POST'])
def viewAllContacts():
    
    cons_ = Contacts.query.all()
    if cons_ is None:
        return redirect(url_for('main.page_not_found'))

    return render_template('home.html', cons_=cons_)

    '''
    sendSMS function is called when the send button on ModalSMS is clicked

    '''



@crudcontacts.route('/sendsms/', methods=['GET','POST'])
def sendSMS():
  # Specify login credentials for sms API
  username = "catherinerakama"
  apikey   = "83d3feea27722bdc80cef9c6921a62bf0fad4cb8a00ddd656927de804a4c111f"
  
  phoneNumber = request.form['recipientNo']
  msg = request.form['msgText']

  #create an empty list and assign variable "to" to the list
  '''Code to send SMS
      Specify the numbers that you want to send to, including country code
      (+254 for Kenya in this case)
   '''


  to = phoneNumber 

  '''
       Contains the message body
  '''




  message = msg

  # Create a new instance of the gateway class
  gateway = AfricasTalkingGateway(username, apikey)
  
  try:

     # Thats it, hit send and we'll take care of the rest.
    results = gateway.sendMessage(to, message)

    for recipient in results:

      # status is either "Success" or "error message"
      flash('Your Message has been sent!') 

  except AfricasTalkingGatewayException, e:

    print 'Encountered an error while sending: %s' % str(e)




  
  
  return render_template('home.html')



@crudcontacts.route('/addnew', methods=['GET', 'POST'])
def addContact():
    form = AddNewContactForm()
    if form.validate_on_submit():
      con = Contacts(firstname=form.firstname.data,
        lastname=form.lastname.data,
        email=form.email.data,
        mobilenumber=form.mobilenumber.data,
        country=form.country.data,
        skypeID=form.skypeID.data,
        position=form.position.data,
        organization=form.organization.data)
      db.session.add(con)
      db.session.commit()
      flash('Welcome to your Contacts Manager! \n Please login to continue.')
      return redirect(url_for('auth.home'))
    return render_template('crudcontacts/addnew.html', form=form)


@crudcontacts.route('/editContacts/<int:id>', methods=['GET', 'POST'])
def editUserContacts(id):
    con = Contacts.query.get_or_404(id)
    form = EditContactForm()
    if form.validate_on_submit():
      con.firstname = form.firstname.data
      con.lastname = form.lastname.data
      con.email = form.email.data
      con.skypeID = form.skypeID.data
      con.mobilenumber = form.mobilenumber.data
      con.country = form.country.data
      con.position = form.position.data
      con.organization = form.organization.data
      db.session.add(con)
      db.session.commit()
      flash('The profile has been updated.')
      return redirect(url_for('auth.home', mobilenumber=con.mobilenumber))

    form.firstname.data = con.firstname
    form.lastname.data = con.lastname
    form.email.data = con.email
    form.skypeID.data = con.skypeID
    form.mobilenumber.data = con.mobilenumber 
    form.country.data = con.country
    form.position.data = con.position
    form.organization.data = con.organization
    return render_template('crudcontacts/editcontacts.html', form=form, con=con)

