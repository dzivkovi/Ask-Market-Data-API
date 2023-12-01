"""
This module contains the business logic for a Flask app that serves as a market data query service.
It includes functions to process natural language market data queries using an LLM agent.
"""

import os
import logging
from langchain.llms.openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_csv_agent
from dotenv import load_dotenv

def process_market_query(query, agent):
    """
    Process a natural language market data query using the LLM agent and return the response.

    Args:
        query (str): The natural language query.
        agent: The LLM agent for processing the query.

    Returns:
        str: The response string with the queried market data.
    """
    logging.info("Processing market data query: '%s'", query)

    if not query.strip():
        return "No query provided"

    try:
        answer = agent.run(query)
        logging.info("Query processed. Answer: %s", answer)
        return answer
    except Exception as e:
        logging.error("Error processing query: %s", e)
        return "Error processing query"

# Main function for testing
if __name__=='__main__':

    load_dotenv()
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG').upper()
    LOG_FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

    llm = OpenAI(temperature=0, model="text-davinci-003")
    CSV_FILE_PATH = "data/nasdaq100_eod_data.csv"
    agent = create_csv_agent(
        llm,
        CSV_FILE_PATH,
        verbose=False,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

    TEST_QUERY = "What was the volume for Apple today?"
    logging.info("Test query: '%s'", TEST_QUERY)
    query_response = process_market_query(TEST_QUERY, agent)
    logging.info("Query response: '%s'", query_response)
