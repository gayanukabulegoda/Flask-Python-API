from flask import Blueprint, request, jsonify, current_app
from ..services.order_service import place_order, get_order, get_all_orders

order_bp = Blueprint('order', __name__, url_prefix='/api/v1/order')


@order_bp.route('', methods=['POST'])
def place_order_route():
    data = request.json
    customer_id = data.get('customer_id')
    items = data.get('items')  # List of product IDs and quantities

    db = current_app.db
    cursor = db.cursor()

    response, status = place_order(cursor, customer_id, items)
    db.commit()

    return jsonify(response), status


@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order_route(order_id):
    db = current_app.db
    cursor = db.cursor()

    response, status = get_order(cursor, order_id)

    return jsonify(response), status


@order_bp.route('', methods=['GET'])
def get_all_orders_route():
    db = current_app.db
    cursor = db.cursor()

    response, status = get_all_orders(cursor)
    return jsonify(response), status
