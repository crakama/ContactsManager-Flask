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


@crudcontacts.route('/editContacts<int:id>', methods=['GET', 'POST'])
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

