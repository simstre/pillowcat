from flask import Blueprint, render_template, request, flash, url_for, redirect, session
from datetime import datetime, date, timedelta
from app.decorators import login_required
from dateutil import parser
from app import redis, app
import requests
import traceback
import sys


###############################################################################
# Instantiation
###############################################################################
main = Blueprint('app', __name__, template_folder='templates', static_folder='static')

###############################################################################
# Constant
###############################################################################


###############################################################################
# View
###############################################################################
@main.route('/', methods=['GET', 'POST'])
def front():
	if request.method == 'GET':
		return render_template('front.html')
	else:
		success, next_view = validate_credential(request.form)
		return redirect(url_for('.' + next_view))

		# Authenticate user (rate limit to 3 tries, then lock for 1hr, redirect to forgot password page)
		# If first time using app, redirect to "what are you looking for?" page
		# Display main deck, what makes more sense? pins on map showing what people are selling? or "trends" or "hot items" or "similar stuff"?

@main.route('/signup')
def signup():
	return render_template('signup.html')

@main.route('/main/')
@login_required
def main():
	data = None
	return render_template('main.html', data=data)

@main.route('/listings')
@login_required
def listings():
	item = request.args.get('item')
	# generate a page with listings for that item
	listings = None
	return render_template('listings.html', listings=listings)

@main.route('/settings')
@login_required
def settings(): pass

###############################################################################
# Helper function
###############################################################################
def validate_credential(form):
	req = ['username', 'password']
	for field in req:
		if not form.get(field):
			flash("Forgot to enter your " + field + "? :)")
			return False, 'front'
	username = form['username']
	password = form['password']

	#try:
		#redis.get("redis-app22172284")
#    	 except requests.ConnectionError:
#            app.logger.error("Unable to connect to Redis, username: " + username)
#            return redirect(url_for('error', error="Server unavailable"))
#        except Exception:
#            app.logger.warning(traceback.format_exc() + "username: " + username)
#            return redirect(url_for('error', error="Server unavailable"))

	correct_password = redis.hget("user::" + username, "password")
	
	# Checks if the user is in the DB
	if correct_password is not None:
		# Password validation
		if password == correct_password:
			return True, 'main'
		else:
			#flash(parser.unescape(gettext("errorLogin")))
			#return redirect(url_for('login'))
			return False, 'front'
	else:
		# redirect user to sign up for us
		return False, 'signup'
