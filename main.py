"""
This module is a Flask application that serves as a greeting service. 
It can be run both locally and on Google Cloud Run. 
In a cloud environment, it configures a GCP logging client for application logs.
The application provides two routes: 
- / which returns a hello message
- /hello/<name> which returns a personalized greeting message

Inspired by https://code.visualstudio.com/docs/python/tutorial-flask
"""

import logging
import os
from flask import Flask, request

import google.cloud.logging
from dotenv import load_dotenv

import business_logic

# Load environment variables
load_dotenv()

if __name__ != '__main__':
    # Setup GCP logging
    client = google.cloud.logging.Client()
    # Configure the default logger to use the logging client
    # By default this captures all logs at INFO level and higher
    client.setup_logging()
    # Adjust the logging level as per the environment variable
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
    logging.basicConfig(level=LOG_LEVEL)

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    """
    Home route that responds to GET and POST requests.
    Returns a simple greeting message.

    Returns:
        str: A greeting string.
    """
    logging.debug("Home page request received")
    server = request.host_url  # Get the server URL
    return f"Usage: {server}hello/Daniel"

@app.route("/hello/", defaults={'name': None}, methods=["POST", "GET"])
@app.route("/hello/<name>", methods=["POST", "GET"])
def hello_there(name):
    """
    A route that responds to GET and POST requests with a personalized greeting.
    Invokes business logic for the greeting. 

    Args:
        name (str): Name of the person to be greeted.

    Returns:
        str: A personalized greeting string.
    """
    # do not place business logic in the route functions
    logging.debug("Hello page request received")
    return business_logic.greeting(name)

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", '8080'))

    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run. See entrypoint in Dockerfile.
    app.run(host="127.0.0.1", port=PORT, debug=True)
