from flask import Blueprint, request, jsonify, current_app
from ..services.user_service import register_user

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['POST'])
def register_user_route():
    data = request.json
    name = data.get('name')
    address = data.get('address')
    email = data.get('email')
    password = data.get('password')

    # Access the database connection through the app context
    db = current_app.db  # Use current_app to get the app's db attribute
    cursor = db.cursor()

    # Call the service to register the user
    response, status = register_user(cursor, name, address, email, password)
    db.commit()

    # jsonify is a Flask helper function that converts Python dictionaries into JSON (JavaScript Object Notation) format.
    return jsonify(response), status

# This file handles the API routes. We call the service layer to do the actual work.
