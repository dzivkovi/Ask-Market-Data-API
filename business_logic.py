"""
This module contains the business logic for a Flask application that serves as a greeting service.
It includes a function to create a personalized greeting using a provided name.

Note:
- Business logic goes in here
- To start VSCode Flask debugger make sure to be in the app.py file
- To start Flask app from the command line, run:
    python -m flask run --port 5000
"""
import logging
import os
import re
from datetime import datetime

def greeting(name):
    """
    Generate a personalized greeting with the provided name and current timestamp.
    If the name contains any characters that are not letters, the greeting will use "Friend".

    Args:
        name (str): Name of the person to be greeted. 

    Returns:
        str: A personalized greeting string with current date and time.
    """

    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    if name is not None:
        match_object = re.match("[a-zA-Z]+", name)
    else:
        match_object = None

    logging.info("Name of the person to be greeted: '%s'", name)
    if match_object:
        clean_name = match_object.group(0)
        logging.info("Clean name: '%s'", clean_name)
    else:
        clean_name = "Friend"
        logging.warning("No name found, defaulting to '%s'", clean_name)

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    logging.debug("Greeting: '%s'", content)
    return content

# Main function to quickly test the business logic
if __name__=='__main__':

    # Setup logging
    # https://powerfulpython.com/blog/nifty-python-logging-trick/
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG').upper()
    LOG_FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
    logging.basicConfig(level=LOG_LEVEL,format=LOG_FORMAT)

    FIRSTNAME = "Don@van"
    logging.info("Input name: '%s', greeting: '%s'", FIRSTNAME, greeting(FIRSTNAME))
    logging.info("Empty sting ('') name greeting: '%s'", greeting(''))
    logging.info("Missing name greeting: '%s'", greeting(None))
