from flask import Flask
from flask.ext.redis import Redis


app = Flask('app')

app.config.from_object('base_config')

redis = Redis(app)

from app import views
