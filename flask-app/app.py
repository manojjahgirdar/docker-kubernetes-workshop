from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 align='center'>Hello World from Python Flask!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)