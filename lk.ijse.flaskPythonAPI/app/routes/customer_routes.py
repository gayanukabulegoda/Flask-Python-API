from flask import Blueprint, request, jsonify, current_app
from ..services.customer_service import add_customer, update_customer, get_customer, delete_customer, get_all_customers

customer_bp = Blueprint('customer', __name__, url_prefix='/api/v1/customer')


@customer_bp.route('', methods=['POST'])
def register_customer_route():
    data = request.json
    name = data.get('name')
    address = data.get('address')
    email = data.get('email')

    db = current_app.db
    cursor = db.cursor()

    response, status = add_customer(cursor, name, address, email)
    db.commit()

    return jsonify(response), status


@customer_bp.route('/<int:customer_id>', methods=['PATCH'])
def update_customer_route(customer_id):
    data = request.json
    name = data.get('name')
    address = data.get('address')
    email = data.get('email')

    db = current_app.db
    cursor = db.cursor()

    response, status = update_customer(cursor, customer_id, name, address, email)
    db.commit()

    return jsonify(response), status


@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer_route(customer_id):
    db = current_app.db
    cursor = db.cursor()

    response, status = get_customer(cursor, customer_id)

    return jsonify(response), status


@customer_bp.route('', methods=['GET'])
def get_all_customers_route():
    db = current_app.db
    cursor = db.cursor()

    response, status = get_all_customers(cursor)
    return jsonify(response), status


@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
def delete_customer_route(customer_id):
    db = current_app.db
    cursor = db.cursor()

    response, status = delete_customer(cursor, customer_id)
    db.commit()

    return jsonify(response), status
