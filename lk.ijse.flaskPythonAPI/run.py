from app import create_app
app, db = create_app()

if __name__ == '__main__':
    app.db = db  # Assign the DB connection to the app instance
    app.run(debug=True, port=5001) # default port is 5000

# main entry point to run the Flask app. It imports the create_app() function and starts the server.
