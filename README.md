# Flask using Visual Studio Code

This "Hello World" style repo demonstrates:

1. The separation of business logic ([business_logic.py](business_logic.py) file) and the web app ([main.py](main.py) file),
2. Quick business logic validation without the webapps (or cloud deployments), and
3. Debugging Flask apps using VSCode as per Microsoft [Flask tutorial](https://code.visualstudio.com/docs/python/tutorial-flask) and [Debugging](https://code.visualstudio.com/docs/editor/debugging) instructions.

## Execution

To execute the application, run the following command:

```bash
FLASK_APP=main.py flask run
```

## Usage

To use this application, you can send HTTP GET and POST requests to the available routes. Here is an example using cURL:

- GET request:

```bash
curl http://127.0.0.1:5000/hello/sara
```

- POST request:

```bash
curl -X POST http://127.0.0.1:5000/hello/sara
```

Replace 'sara' in the URL with the 'name' you want to send in the request.
