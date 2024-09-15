def register_user(cursor, name, address, email, password):
    try:
        cursor.execute(
            "INSERT INTO users (name, address, email, password) VALUES (%s, %s, %s, %s)",
            (name, address, email, password)
        )
        # 200 is the HTTP status code.
        return {"message": "User registered successfully!"}, 200
    except Exception as e:
        # The f in front of the string allows for string interpolation (inserting the value of e into the string).
        print(f"Error: {e}")
        return {"message": "Registration failed!"}, 500


# This service handles the database interaction and any business logic related to user registration.
