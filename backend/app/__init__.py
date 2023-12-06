from flask import Flask
from .db import close_db

def create_app():
    app = Flask(__name__)

    # app.config.from_pyfile('config.py')
    app.teardown_appcontext(close_db)

    return app