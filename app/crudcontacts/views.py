from flask import session, render_template, redirect, request, url_for, flash
from . import crudcontacts
from .. import db
from ..models import Contacts
from .forms import AddNewContactForm



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

@crudcontacts.route('/viewall', methods=['GET', 'POST'])
def viewAllContacts():
    
    cons_ = Contacts.query.all()
    if cons_ is None:
        return redirect(url_for('main.page_not_found'))

    return render_template('crudcontacts/viewall.html', cons_=cons_)
