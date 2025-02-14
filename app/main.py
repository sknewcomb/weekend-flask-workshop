from flask import Flask, jsonify
import os
from datetime import datetime

def create_app():
    # Create the Flask app instance
    app = Flask(__name__)
    
    # Enable debug mode if the FLASK_DEBUG environment variable is set to a truthy value
    app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'true').lower() in ['true', '1', 'yes']

    @app.route("/")
    def index():
        # Get current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Return a JSON response with message and current time
        return jsonify(
            message="Welcome back to Flask on Day 2!",
            current_time=current_time
        )

    return app

if __name__ == "__main__":
    # Create the app and run it
    app = create_app()
    app.run(host="0.0.0.0", port=4999)