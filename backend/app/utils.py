import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    with app.app_context():
        from . import routes
        from . import models
        models.db.create_all()

    return app
