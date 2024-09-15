from flask import Flask
from flask_cors import CORS
from .config import db_config
import mysql.connector


# Initialize the app and load configurations
def create_app():
    # Flask is a web framework for Python that allows you to build web applications and APIs.
    # __name__ special variable in Python that holds the name of the current module (script).
    app = Flask(__name__)  # Create the Flask lk.ijse.flaskPythonAPI instance

    # Enable CORS for all routes
    CORS(app)

    # Initialize the MySQL connection
    db = mysql.connector.connect(**db_config)
    app.db = db  # Attach the db connection to the app object

    # Register Blueprints (routes)
    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    return app, db

# This file initializes the Flask app and sets up the MySQL connection. It also registers the routes (blueprints).
