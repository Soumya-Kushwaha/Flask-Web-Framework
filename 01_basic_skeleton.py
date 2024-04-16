from flask import Flask

# WSGI Application
app = Flask(__name__)


# Decorator
@app.route('/')
def welcome():
    return "Welcome to my Flask Project!"


if __name__ == '__main__':
    app.run(debug=True)
