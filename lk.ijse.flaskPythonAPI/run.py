from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5001)

# main entry point to run the Flask app. It imports the create_app() function and starts the server.
