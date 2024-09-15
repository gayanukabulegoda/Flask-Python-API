import unittest
from flask import Flask, request, jsonify


def create_app():
    app = Flask(__name__)

    # Define the /register route
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()  # Retrieve JSON data from the request
        # Perform user registration logic here (e.g., save user data to the database)
        return jsonify({"message": "User registered successfully"}), 200  # Return 200 OK response

    return app


class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_user_registration(self):
        response = self.client.post('/register', json={
            'name': 'John Doe',
            'address': '123 Street',
            'email': 'john@example.com',
            'password': 'pass123'
        })
        self.assertEqual(response.status_code, 200)  # Expecting 200 OK


if __name__ == "__main__":
    unittest.main()

# (optional) – Unit tests for user registration.
