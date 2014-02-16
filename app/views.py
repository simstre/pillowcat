from flask import Blueprint, render_template, request


main = Blueprint('app', __name__, template_folder='templates', static_folder='static')

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return "password peeked!"

@main.route('/test/')
def test():
    return "fuck this shit"

