"""
This module is a Flask application that serves both as a market data query service. 
It can be run both locally and on Google Cloud Run. 
In a cloud environment, it configures a GCP logging client for application logs.
The application provides three routes: 
- / which returns a hello message
- /api/v1/marketdataquery which processes market data queries in natural language
"""
import os
import uuid
import logging
from flask import Flask, request, jsonify
import google.cloud.logging
from dotenv import load_dotenv
from langchain.llms.openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_csv_agent

import business_logic

# Load environment variables
load_dotenv()

# Adjust the logging level as per the environment variable
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=LOG_LEVEL)

# Check if running on Google Cloud (Cloud Run)
if 'K_SERVICE' in os.environ:
    # Set default logging level
    client = google.cloud.logging.Client()
    client.setup_logging()
    logging.info("Running on Google Cloud")
else:
    logging.info("Running locally")

# Make sure you have a correct OPENAI_API_KEY in the environment.
CSV_FILE_PATH = "data/nasdaq100_eod_data.csv"
llm = OpenAI(
    temperature=0, # prevent hallucinations
    model="text-davinci-003")
llm_agent = create_csv_agent(
    llm,
    CSV_FILE_PATH,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    """
    Home route that responds to GET and POST requests.
    Returns a simple greeting message.

    Returns:
        str: A greeting string.
    """

    welcome_message = "Welcome to the Ask Market Data service!"
    logging.debug(welcome_message)
    return f"""
    <html>
        <body>
            <h1>{welcome_message}</h1>

            <p>This service accepts both GET and POST requests.</p>
            <H2>Sample GET request</H2>
                {request.host_url}api/v1/marketdataquery?query='What is stock symbol for Microsoft?'
            <H2>Sample POST request</H2>
                curl -X POST -H "Content-Type: application/json" -d '{{"query": "What is the volume for AAPL"}}' {request.host_url}api/v1/marketdataquery

        </body>
    </html>
    """

# Usage: {server}api/v1/marketdataquery

@app.route("/api/v1/marketdataquery", methods=["POST", "GET"])
def market_data_query():
    """
    Endpoint to handle market data queries in natural language.
    Accepts both GET and POST requests.
    """
    if request.method == "POST":
        query = request.json.get("query")
    else:  # GET request
        query = request.args.get("query")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    response = business_logic.process_market_query(query, llm_agent)
     # TODO: UUID should be tied to the request to peserve chat memory
    return jsonify({
        "response_id": uuid.uuid1(),
        "response": response
        })

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", '8080'))

    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run. See entrypoint in Dockerfile.
    app.run(host="127.0.0.1", port=PORT, debug=True)
