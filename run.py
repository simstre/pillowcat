from flask import Flask
from app.views import main
from app import app


app.register_blueprint(main)

if __name__ == "__main__":
    app.run()