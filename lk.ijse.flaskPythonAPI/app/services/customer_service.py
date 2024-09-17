def add_customer(cursor, name, address, email):
    try:
        cursor.execute(
            "INSERT INTO customers (name, address, email) VALUES (%s, %s, %s)",
            (name, address, email)
        )
        return {"message": "Customer added successfully!"}, 200
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Customer addition failed!"}, 500


def update_customer(cursor, customer_id, name=None, address=None, email=None):
    try:
        # Check if the customer exists
        customer_data, status_code = get_customer(cursor, customer_id)
        if status_code == 404:
            return customer_data, status_code

        customer = customer_data['customer']

        updates = []
        values = []

        if name and name != customer[1]:
            updates.append("name = %s")
            values.append(name)
        if address and address != customer[2]:
            updates.append("address = %s")
            values.append(address)
        if email and email != customer[3]:
            updates.append("email = %s")
            values.append(email)

        if not updates:
            return {"message": "Customer not updated! No changes provided."}, 400

        query = "UPDATE customers SET " + ", ".join(updates) + " WHERE id = %s"
        values.append(customer_id)
        cursor.execute(query, values)

        return {"message": "Customer updated successfully!"}, 200
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Customer update failed!"}, 500


def get_customer(cursor, customer_id):
    cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
    customer = cursor.fetchone()
    if customer:
        return {"customer": customer}, 200
    return {"message": "Customer not found!"}, 404


def get_all_customers(cursor):
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    if customers:
        return {"customers": customers}, 200
    return {"message": "No customers found!"}, 404


def delete_customer(cursor, customer_id):
    try:
        cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
        if cursor.rowcount == 0:
            return {"message": "Customer not found!"}, 404
        return {"message": "Customer deleted successfully!"}, 200
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Customer deletion failed!"}, 500
