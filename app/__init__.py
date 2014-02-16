from flask import Flask


app = Flask('app')

from app import views
