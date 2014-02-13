from flask import Blueprint, render_template
main = Blueprint('app', __name__, template_folder='templates')

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/test/')
def test():
    return "fuck this shit"

