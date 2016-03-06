from flask import g, session, render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required,current_user
from . import auth
from .. import db
from .. import oauth
from ..models import User, Contacts
from .forms import LoginForm, RegistrationForm
from functools import wraps
from app import login_manager



twitter = oauth.remote_app(
    'twitter',
    consumer_key='qtrDRR8LELDpHCwg7AedlfVcj',
    consumer_secret='F2xTVvoDWSmveSC4I9Ap4rvKpOov3OLb9iIjc8baQYyFHrxTMM',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
)


def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('main.login'))
	return wrap

@twitter.tokengetter
def get_twitter_token():
    if 'twitter_oauth' in session:
        resp = session['twitter_oauth']
        return resp['oauth_token'], resp['oauth_token_secret']




@auth.before_request
def before_request():
    g.user = None
    if 'twitter_oauth' in session:
        g.user = session['twitter_oauth']


@auth.route('/')
def index():

    return render_template('index.html', tweets=tweets)



@auth.route('/home')
def home():
    tweets = None
    if g.user is not None:
        resp = twitter.request('statuses/home_timeline.json')
        if resp.status == 200:
            tweets = resp.data
        else:
            flash('Unable to load tweets from Twitter.')
	return render_template('home.html')



'''
authorize function redirects user to providers website 
to let the user authenticate user there

'''

@auth.route('/oauthorized')
def oauthorized():
    resp = twitter.authorized_response()
    if resp is None:
        flash('You denied the request to sign in.')
    else:
        session['twitter_oauth'] = resp
        return redirect(request.args.get('next') or url_for('auth.home'))
    return redirect(url_for('auth.index'))



    '''
    oauth_callback function redirects the user back 
    to the application after authentication. 
    Redirects back to the URL that called it, 
    because the provider cannot acess directly access internal methods of this app

    '''



@auth.route('/login', methods=['GET', 'POST'])
def login():

    callback_url = url_for('auth.oauthorized', next=request.args.get('next'))
    return twitter.authorize(callback=callback_url or request.referrer or None)

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            session['logged_in'] = True
            return redirect(request.args.get('next') or url_for('auth.home'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)



@auth.route('/logout')
@login_required
def logout():
    session.pop('twitter_oauth', None)
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))



@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # get the user rcontacts default
        #user_contacts = Contacts.query.filter_by(username='User').first()
        user = User(username=form.username.data,
                    password=form.password.data,
                    
                    email =form.email.data,
                    PhoneNum =form.PhoneNum.data
                    )
        #user.relContacts = user_contacts
        db.session.add(user)
        db.session.commit()
        flash('Welcome to your Contacts Manager! \n Please login to continue.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)








