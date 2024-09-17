def place_order(cursor, customer_id, order_items):
    try:
        cursor.execute("START TRANSACTION")

        total = 0

        for item in order_items:
            product_id = item['product_id']
            quantity = item['quantity']

            # Check quantity and product price before proceeding
            cursor.execute("SELECT price, qty FROM products WHERE id = %s", (product_id,))
            product = cursor.fetchone()

            if product and product[1] >= quantity:
                price = product[0]
                total += price * quantity
                item['price'] = price
            else:
                cursor.execute("ROLLBACK")
                return {"message": f"Insufficient quantity for product ID {product_id}!"}, 400

        # Insert order into the orders table
        cursor.execute("INSERT INTO orders (customer_id, total) VALUES (%s, %s)", (customer_id, total))
        order_id = cursor.lastrowid

        for item in order_items:
            product_id = item['product_id']
            quantity = item['quantity']
            price = item['price']

            # Insert into order_items table
            cursor.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
                (order_id, product_id, quantity, price)
            )
            # Update product quantity
            cursor.execute(
                "UPDATE products SET qty = qty - %s WHERE id = %s",
                (quantity, product_id)
            )

        # Commit the transaction
        cursor.execute("COMMIT")
        return {"message": "Order placed successfully!", "order_id": order_id}, 200

    except Exception as e:
        # Rollback the transaction in case of error
        cursor.execute("ROLLBACK")
        print(f"Error: {e}")
        return {"message": "Order placement failed!"}, 500


def get_order(cursor, order_id):
    cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
    order = cursor.fetchone()
    if order:
        return {"order": order}, 200
    return {"message": "Order not found!"}, 404


def get_all_orders(cursor):
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    if orders:
        return {"orders": orders}, 200
    return {"message": "No orders found!"}, 404
