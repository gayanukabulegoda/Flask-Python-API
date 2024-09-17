from flask import Blueprint, request, jsonify, current_app
from ..services.product_service import add_product, update_product, get_product, delete_product, get_all_products

product_bp = Blueprint('product', __name__, url_prefix='/api/v1/product')


@product_bp.route('', methods=['POST'])
def add_product_route():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    qty = data.get('qty')

    db = current_app.db
    cursor = db.cursor()

    response, status = add_product(cursor, name, price, qty)
    db.commit()

    return jsonify(response), status


@product_bp.route('/<int:product_id>', methods=['PATCH'])
def update_product_route(product_id):
    data = request.json
    name = data.get('name')
    price = data.get('price')
    qty = data.get('qty')

    db = current_app.db
    cursor = db.cursor()

    response, status = update_product(cursor, product_id, name, price, qty)
    db.commit()

    return jsonify(response), status


@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product_route(product_id):
    db = current_app.db
    cursor = db.cursor()

    response, status = get_product(cursor, product_id)

    return jsonify(response), status


@product_bp.route('', methods=['GET'])
def get_all_products_route():
    db = current_app.db
    cursor = db.cursor()

    response, status = get_all_products(cursor)
    return jsonify(response), status


@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    db = current_app.db
    cursor = db.cursor()

    response, status = delete_product(cursor, product_id)
    db.commit()

    return jsonify(response), status
