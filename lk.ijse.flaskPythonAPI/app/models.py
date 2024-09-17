def check_database(cursor):
    cursor.execute("SHOW DATABASES LIKE 'python_flask_API'")
    if not cursor.fetchone():
        create_database(cursor)
        create_customer_table(cursor)
        create_product_table(cursor)
        create_order_table(cursor)
        create_order_item_table(cursor)
    else:
        use_database(cursor)


def create_database(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS python_flask_API")
    use_database(cursor)


def use_database(cursor):
    cursor.execute("USE python_flask_API")


def create_customer_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            address VARCHAR(255) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        )
    """)


def create_product_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            qty INT NOT NULL
        )
    """)


def create_order_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            total DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
    """)


def create_order_item_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT NOT NULL,
            product_id INT NOT NULL,
            quantity INT NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

# This file store the database models
