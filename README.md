# Ask Market Data Service

## Overview

The Ask Market Data service is a REST API designed to seamlessly interpret and respond to queries about stock market data in natural language. The service is built on the Flask web framework and is equipped to be deployed locally or in a cloud environment, with enhanced support for Google Cloud Platform (GCP) where it was tested.

## Data

This API uses a CSV dataset consisting of the Nasdaq-100 stock analytics captured during one trading day. You are responsible for providing your dataset and modifying the `business_logic.py` module to work with your specific data.

## Natural Language Interface Design

To handle and interpret queries, this service leverages Natural Language Processing (NLP) technologies. As such, the implementation of an appropriate NLP model or service within the `business_logic.py` module is essential for the functional transformation of natural language queries into actionable data responses.

### Customization Note

The `business_logic.py` file provided is a skeleton that requires the integration of an NLP service or library. It is recommended to use a modern NLP framework capable of understanding complex queries and fetching relevant market data.

## Installation and Setup

### Prerequisites

Before diving into the setup, make sure you have the following prerequisites installed on your system:

- Python 3.11 or higher.
- Flask 1.1.2 or higher.
- Docker, if you wish to containerize the application.
- pip, for installing Python dependencies.

### Local Environment

To run the application locally, execute the following command in your terminal:

```bash
FLASK_APP=main.py flask run
```

### Docker Containerization

For those preferring Docker, you can containerize the application by following these steps:

1. To build the Docker image, run:

    ```bash
    docker build -t marketdataquery .
    ```

2. To run the container, execute:

    ```bash
    docker run -e PORT=8080 -p 5000:8080 marketdataquery
    ```

The service should now be accessible at `http://localhost:5000`.

### Google Cloud Run Deployment

VSCode extension [Cloud Code for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=GoogleCloudTools.cloudcode) makes the deployment of the containerized Ask Market Data Service as Serverless Cloud Run service on GCP almost trivial.

1. Learn more about Cloud Code for VS Code at [cloud.google.com/code/docs/vscode/cloud-run-overview](https://cloud.google.com/code/docs/vscode/cloud-run-overview)

2. Test drive our Cloud Run service deployed at [Ask Market Data API](https://ask-market-data-api-4e6gjgrfea-uc.a.run.app).

## Usage

### API Endpoint

Make a POST request to the following endpoint to use the service:

```text
POST http://localhost:5000/api/v1/marketdataquery
```

#### Request Format

Your POST request should include the natural language query in JSON format:

```json
{
    "query": "What is the volume for AAPL?"
}
```

#### Response Format

The service will return the market data requested in the following JSON structure:

```json
{
    "response_id": "uuid",
    "response": "AAPL’s volume is 1.2M shares"
}
```
