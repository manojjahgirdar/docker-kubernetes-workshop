=== "Python Flask Application"
    ### Build a Python Flask App
    #### 1.1. Create a python virtual environment

    * As a best practice create a Virtual Environment to get started. In terminal, run the following command:
    ```bash
    pip install virtualenv
    virtualenv venv
    ```

    * Once the virtualenv is created, source into the venv by running the following command:
    ```bash
    source venv/bin/activate
    ```

    * You will see the prompt change to `(venv)$`.

    #### 1.2. Install flask library

    * Since we are building a flask app make sure to install the flask library, by running the following command:
    ```bash
    pip install flask
    ```

    #### 1.3. Create a python app

    * Create an `app.py` file by running the following command:
    ```bash
    touch app.py
    ```

    * Open the `app.py` in your favourite code editor.
        * Import the flask module
        ```python
        from flask import Flask
        ```
        
        * Set app context
        ```python
        app = Flask(__name__)
        ```

        * Define a route for `/`
        ```python
        @app.route('/')
        def index():
            return "<h1 align='center'>Hello World from Python Flask!</h1>"
        ```

        * Finally set the flask run
        ```python
        if __name__ == "__main__":
            app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
        ```

    * Your `app.py` file should look something like this:
    ```python title="app.py" linenums="1"
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
        return "<h1 align='center'>Hello World from Python Flask!</h1>"

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
    ```

    * Save the file.

    #### 1.4. Run the App

    * Back to terminal, run the following command to start the application and check whether it works
    ```bash
    python app.py
    ```

    * You will see output similar to the following:
    ```
    * Serving Flask app "app" (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: on
    * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 812*299*939
    ```

    * Visit `http://0.0.0.0:8080/` on your browser or run the following command:
    ```bash
    curl http://0.0.0.0:8080
    ```

    * You will see output similar to the following:
    ```
    <h1 align='center'>Hello World from Python Flask!</h1>
    ```

    * If you see `Hello World` message, congrats you have successfully built the basic flask application.

=== "NodeJs Express Application"
    ### Build a NodeJs Express App
    #### 1.1. Initialize Node Environment

    * Initialize a new project by running the following command:
    ```bash
    npm init
    ```

    #### 1.2. Install Express library

    * Since we are building an Express app make sure to install the Express library by running the following command:
    ```bash
    npm install express
    ```

    * A `package.json` file will be created in the root directory of your project.

    #### 1.3. Set npm start command

    * Add `app.js` to the `package.json` scripts section:
    ```json hl_lines="2"
    "scripts": {
        "start": "node app.js",
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    ```

    #### 1.4. Create a NodeJs Express app

    * Create an `app.js` file by running the following command:
    ```bash
    touch app.js
    ```

    * Open the `app.js` in your favourite code editor.
        * Import the express module
        ```javascript
        const express = require('express');
        ```

        * Set app context
        ```javascript
        const app = express();
        ```

        * Set port on which you want the app to listen
        ```javascript
        const port = 3000;
        ```

        * Define a route for `/`
        ```javascript
        app.get('/', (req, res) => {
            res.send("<h1 align='center'>Hello World from NodeJs Express!</h1>");
        });
        ```

        * Finally set the express run
        ```javascript
        app.listen(port, () => {
            console.log(`Example app listening on port ${port}!`);
        });
        ```

    * Your `app.js` file should look something like this:
    ```javascript title="app.js" linenums="1"
    const express = require('express');
    const app = express();
    const port = 3000;

    app.get('/', (req, res) => {
        res.send("<h1 align='center'>Hello World from NodeJs Express!</h1>");
    });

    app.listen(port, () => {
        console.log(`Example app listening on port ${port}!`);
    });
    ```

    * Save the file.

    #### 1.5. Run the App

    * Back to terminal, run the following command to start the application and check whether it works
    ```bash
    npm start
    ```

    * You will see output similar to the following:
    ```
    Example app listening on port 3000!
    ```

    * Visit `http://0.0.0.0:3000/` on your browser or run the following command:
    ```bash
    curl http://0.0.0.0:3000
    ```

    * You will see output similar to the following:
    ```
    <h1 align='center'>Hello World from Python Flask!</h1>
    ```

    * If you see `Hello World` message, congrats you have successfully built the basic express application.