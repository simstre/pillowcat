from flask import Blueprint, render_template, request


main = Blueprint('app', __name__, template_folder='templates', static_folder='static')

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    else:
    	return "Please check back later :D"
        # Authenticate user (limit to 3 tries, then lock for 1hr, redirect to forgot password page)
        # If first time using app, redirect to "what are you looking for?" page
        # Display main deck, what makes mroe sense? pins on map showing what people are selling? or "trends" or "hot items" or "similar stuff"?

@main.route('/main/')
def test():
    return "Meh"

