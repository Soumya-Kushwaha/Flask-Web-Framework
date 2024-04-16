# Building URL Dynamically

## Variable Rules and URL Building

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to Flask Project!'


@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and has" + str(score) + " marks."


@app.route('/failure/<int:score>')
def failure(score):
    return "The person has passed and has" + str(score) + " marks."


@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks >= 50:
        result = "success"
    else:
        result = "failure"
    return redirect(url_for(result, score=marks))


if __name__ == '__main__':
    app.run(debug=True)
