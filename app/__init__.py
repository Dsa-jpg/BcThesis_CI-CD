from flask import Flask
from .routes import app

def create_app():
    # Create and configure the Flask app
    app = Flask(__name__)

    # Register routes (view functions)
    app.register_blueprint(app)

    return app


