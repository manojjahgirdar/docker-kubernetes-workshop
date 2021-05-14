from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 align='center'>Hello World from Python Flask!</h1>"

port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)