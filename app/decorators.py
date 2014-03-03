from functools import wraps
from flask import redirect, url_for, session


def login_required(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return method(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
