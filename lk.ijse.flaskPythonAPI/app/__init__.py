from flask import Flask
from flask_cors import CORS
from .config import db_config
import mysql.connector
from mysql.connector import errorcode
from .models import check_database


def create_app():
    app = Flask(__name__)

    # Enable CORS for all routes
    CORS(app)

    try:
        # Check if the database and tables exist. If not, create them.
        db = mysql.connector.connect(**db_config)
        check_database(db.cursor())
        app.db = db

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    finally:
        db.cursor().close()

    # Register Blueprints (routes)
    from .routes.customer_routes import customer_bp
    from .routes.product_routes import product_bp
    from .routes.order_routes import order_bp
    from .routes.health_check import health_bp

    app.register_blueprint(customer_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(health_bp)

    return app

# This file initializes the Flask app and sets up the MySQL connection. It also registers the routes (blueprints).
