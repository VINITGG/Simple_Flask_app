import logging
from flask import Flask

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
    logging.info("Home page accessed")
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

