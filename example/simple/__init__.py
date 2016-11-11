from flask import Flask
from flask_page import init_app

app = Flask(__name__)
init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
