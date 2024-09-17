def add_product(cursor, name, price, qty):
    try:
        cursor.execute("INSERT INTO products (name, price, qty) VALUES (%s, %s, %s)", (name, price, qty))
        return {"message": "Product added successfully!"}, 200
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Product addition failed!"}, 500


def update_product(cursor, product_id, name=None, price=None, qty=None):
    try:
        # Check if the product exists
        product_data, status_code = get_product(cursor, product_id)
        if status_code == 404:
            return product_data, status_code

        product = product_data['product']

        updates = []
        values = []

        if name and name != product[1]:
            updates.append("name = %s")
            values.append(name)
        if price and float(price) != float(product[2]):
            updates.append("price = %s")
            values.append(price)
        if qty and int(qty) != int(product[3]):
            updates.append("qty = %s")
            values.append(qty)

        if not updates:
            return {"message": "Product not updated! No changes provided."}, 400

        query = "UPDATE products SET " + ", ".join(updates) + " WHERE id = %s"
        values.append(product_id)
        cursor.execute(query, values)

        return {"message": "Product updated successfully!"}, 200
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Product update failed!"}, 500


def get_product(cursor, product_id):
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    if product:
        return {"product": product}, 200
    return {"message": "Product not found!"}, 404


def get_all_products(cursor):
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    if products:
        return {"products": products}, 200
    return {"message": "No products found!"}, 404


def delete_product(cursor, product_id):
    try:
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        if cursor.rowcount == 0:
            return {"message": "Product not found!"}, 404
        return {"message": "Product deleted successfully!"}, 200
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Product deletion failed!"}, 500
