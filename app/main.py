from flask import Flask, jsonify
import os

def create_app():
    # Create the Flask app instance
    app = Flask(__name__)
    
    # Enable debug mode if the FLASK_DEBUG environment variable is set to a truthy value
    app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'true').lower() in ['true', '1', 'yes']

    @app.route("/")
    def index():
        # Return a JSON response for the root endpoint
        return jsonify(message="Welcome back to Flask on Day 2!")

    return app

if __name__ == "__main__":
    # Create the app and run it
    app = create_app()
    app.run(host="0.0.0.0", port=4999)